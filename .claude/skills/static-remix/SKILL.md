---
name: static-remix
description: Turn a PDF of winning competitor static ads into on-brand recreations for your product, using Nano Banana Pro (Gemini 3 Pro Image Preview). Extracts and labels ad examples from a PDF by framework (US VS THEM, BOLD CLAIM, etc), asks for product URL / volume / variation / per-framework split, downloads and studies the real product photo, writes teardown + production briefs, generates images with the product photo as a reference for brand consistency, and produces a testing report. Invoke with /static-remix.
---

# static-remix

Turn a PDF of winning competitor static ads into on-brand recreations of those ads
for the user's product, using Nano Banana Pro (`gemini-3-pro-image-preview`) for
image generation. This file is the runbook — follow it step by step, in order.
Don't skip steps, and don't silently default the required questions in Step 3.

## Prerequisites (check before doing anything else)

- `GEMINI_API_KEY` must be set in the environment. If it isn't, stop and tell the
  user to set it before continuing — do not proceed without it.
- Python 3 with PyMuPDF (`import fitz`). If missing: `pip install pymupdf`.
- `perl` and `curl` on PATH (used by the helper scripts).
- Scripts used below live in `scripts/` next to this file:
  - `scripts/extract_pdf_sections.py` — extracts + labels images from a PDF
    into a single run's folder
  - `scripts/add_to_swipe_file.py` — extracts + labels images from a PDF into
    the persistent `swipe-file/` library (accumulates across every PDF ever
    provided, not just this run's)
  - `scripts/pdf_extract_lib.py` — shared extraction logic used by both of
    the above (not called directly)
  - `scripts/fetch_product_photo.sh` — best-effort product photo downloader
  - `scripts/gemini-image-ref.sh` — one Nano Banana Pro image generation call

## Building the swipe file over time

`<skill_dir>/swipe-file/` is a persistent library of every labeled ad example
ever extracted, across every PDF the user has ever provided — separate from
the per-run `runs/<timestamp>/extracted/` folder, which only holds the
current run's PDF. Step 2 below adds the current run's PDF to this library
automatically, so it grows on its own with normal use.

The user can also add a PDF to the library at any time without running the
full pipeline — no product URL, questions, or image generation needed — by
just asking, at which point run:

```bash
python3 <skill_dir>/scripts/add_to_swipe_file.py <pdf_path> [optional-label]
```

This prints the framework summary across the *entire* library afterward, not
just the newly added PDF — show that summary to the user so they can see how
the library has grown.

## Step 1 — Locate the PDF and create the run folder

Find the user's PDF (they'll tell you the path, or pass it as the skill argument).
If you can't find it, ask for the path before continuing.

Create a dated run folder next to this skill:

```
<skill_dir>/runs/<YYYYMMDD-HHMM>/
```

Use the actual current date/time. Inside it you'll build this structure as you go:

```
runs/<YYYYMMDD-HHMM>/
  source.pdf                  (copy of the input PDF)
  extracted/
    images/                   (every image pulled from the PDF)
    manifest.json             (heading, page, bbox per image)
  product/
    photo.<ext>                (downloaded product photo)
    description.md             (your written visual teardown of the photo)
  teardowns/
    <framework>_<n>.md          (one per source example you studied)
  briefs/
    concept_NN.md                (one per concept: scene, copy, variation axis)
  production/
    concept_NN_var_MM.png        (final generated images)
  report.txt
```

Copy the source PDF into the run folder as `source.pdf` so the run is
self-contained and reproducible later.

## Step 2 — Extract and label every image in the PDF

Run:

```bash
python3 <skill_dir>/scripts/extract_pdf_sections.py <run_dir>/source.pdf <run_dir>/extracted
```

This auto-detects the heading font (the font that shows up on the most distinct
pages inside short text spans) and labels every extracted image with the nearest
heading above it — that heading name *is* the ad framework ("US VS THEM",
"BOLD CLAIM", "Before & After", "TESTIMONIAL", etc). It prints a framework summary
and writes `extracted/manifest.json`.

Skim the extracted images yourself (Read tool) before Step 3 — you need the
framework list and image counts to build question (d) below. Use judgment: if
the extraction pulled in obvious decorative noise (tiny logos/icons unrelated to
any ad example), it's fine to disregard those when presenting frameworks to the
user, but don't hide genuine ad examples.

Then add this run's PDF to the persistent swipe-file library too, so it keeps
growing across runs:

```bash
python3 <skill_dir>/scripts/add_to_swipe_file.py <run_dir>/source.pdf
```

Use the aggregated framework summary this prints (across the whole library,
not just this PDF) — not just the current-run summary above — when building
question (d) in Step 3: if the library already has extra examples of a
framework from earlier PDFs, mention that richer example count to the user.

## Step 3 — Ask the required questions (AskUserQuestion)

These four questions are REQUIRED every run. Never skip any of them and never
silently default an answer — if the user doesn't specify one, ask again, don't guess.

Ask via `AskUserQuestion`:

a. **Product URL** — required, no default. Free-text (use an "Other" style
   text option since this has no sensible preset choices).

b. **Total images wanted** — e.g. 10 / 50 / 100. Offer a few common presets plus
   free text for a custom number.

c. **Variations per concept** — usually 2 (same framework, one axis changes
   between var_01 and var_02 — e.g. camera angle, or overlay wording). Offer
   2 as the recommended default option, plus 1 / 3 / custom.

d. **Per-framework split** — show the frameworks detected in Step 1 with their
   source-example counts, and let the user assign an image count to each
   (e.g. "20 US VS THEM, 10 BOLD CLAIM, 10 Before & After, 10 TESTIMONIAL", or
   "even split across all frameworks"). Offer "even split" as one option and
   "let me specify custom counts per framework" as another; if they pick custom,
   follow up in plain chat to collect the actual numbers (AskUserQuestion options
   don't support free-form per-item numeric entry, so drop to a normal message).

After collecting all four:

- Compute `concepts = total_images / variations_per_concept`.
- Validate: `sum(per_framework_counts) * variations_per_concept == total_images`.
  If it doesn't add up, show the exact mismatch (e.g. "your framework counts sum
  to 45 images but you asked for 50 — off by 5") and ask the user to fix it
  before continuing. Do not proceed with mismatched numbers.
- Show the estimated cost: `total_images * $0.25`. If it's over $10, explicitly
  confirm with the user before continuing (a plain yes/no AskUserQuestion is fine).

Do not move on to Step 4 until all four answers are collected, the math checks
out, and (if applicable) the cost is confirmed.

## Step 4 — Fetch the product page and study the real product photo

**First, check for a saved brand profile**: look in `<skill_dir>/brand-profiles/`
for a folder matching the product URL's domain (e.g. `plentyforall/profile.md`).
If one exists, read it — it can override or correct what the live site would
otherwise tell you (a mismatched product photo, real pricing math, ingredient
counts, target-audience/visual rules, copy framework and rules). Still fetch
the live product page for anything the profile doesn't cover (current promo
copy, price changes, etc) — a profile fixes known gaps, it isn't a reason to
skip checking the live page. If the profile points to its own
`reference-photos/`, use one of those as the `--reference` image in Step 7
instead of downloading a new photo from the site.

If no profile exists for this brand, fetch the product URL (WebFetch or curl).
Then, critically, download the actual product photo — don't describe the
product from text alone.

```bash
<skill_dir>/scripts/fetch_product_photo.sh "<product_url>" <run_dir>/product/photo.png
```

This tries the Shopify `<url>.json` trick first (most DTC brands are on Shopify —
that endpoint exposes real product image URLs), then falls back to the page's
`og:image` meta tag. It's best-effort: if it fails, fetch the page yourself,
find the real hero product image URL by hand, and download it with curl to the
same path. Do not skip this — a written guess at "probably a white bottle" is
not acceptable; you need the real file.

Once you have the photo, **open it with the Read tool** and write a concrete
visual description to `<run_dir>/product/description.md`: bottle color, cap
color, label typography and colors, capsule/softgel color if visible, brand
palette (hex-ish descriptions are fine, e.g. "deep forest green cap, cream
label, navy serif logotype"). This description — grounded in actually *looking*
at the photo — is what keeps every generated image on-brand later, on top of
passing the photo itself as a reference image to Nano Banana Pro.

Also note, from the product page text, the exact pricing/offer copy (price,
subscribe-and-save discount, bundle pricing, guarantee language, etc.) verbatim
— you'll need this for Step 6 and must never invent numbers.

## Step 5 — Teardown each selected source example

For each source PDF image you're using as inspiration for a concept, **view it**
(Read tool) and write a short teardown to `<run_dir>/teardowns/<framework>_<n>.md`:

- Framework name (from its heading label)
- Why it works psychologically (the persuasion mechanism — contrast, social
  proof, authority, urgency, specificity, etc.)
- What to keep as-is (composition, framing, text placement pattern)
- What to swap in for this brand (product, colors, specific claim/number)

You don't need a teardown for every single extracted image — just the ones
informing a concept you're about to brief. If a framework has multiple
examples across the swipe-file library (not just this run's PDF — check
`<skill_dir>/swipe-file/manifest.json` and `swipe-file/images/`), it's fine
to pull the clearest or most-different example from the whole library rather
than only what this run's PDF happened to contain.

## Step 6 — Write one production brief per concept

For each concept (`concepts = total_images / variations_per_concept` from Step 3),
write `<run_dir>/briefs/concept_NN.md` containing:

- Framework it belongs to
- Scene description (concrete: setting, composition, lighting, product placement)
- Text overlays, **exact quoted copy** — headline and any on-image text
- Caption (for use as ad copy alongside the image)
- Aspect ratio to generate at (pick sensibly for the placement — e.g. `1:1` or
  `4:5` for feed, `9:16` for stories/reels — default to `1:1` if no reason to
  do otherwise)
- The variation axis: the one thing that changes between `var_01` and `var_02`
  (camera angle, overlay wording, background color, etc — everything else about
  the concept stays the same across its variations)

Pull all pricing/offer copy verbatim from what you captured in Step 4 — never
invent numbers, discounts, or guarantee terms.

If a brand profile was loaded in Step 4, follow its copy framework, copy
rules, and visual/model-representation rules for every brief instead of
generic defaults (e.g. a required hook-body-CTA order, banned quote labels,
required model demographics) — those override the general guidance above.

## Step 7 — Generate images with Nano Banana Pro

For each concept × variation, build a full image prompt from the brief (scene +
exact overlay text + brand visual description from Step 4) and call:

```bash
<skill_dir>/scripts/gemini-image-ref.sh \
  --prompt "<full prompt text>" \
  --aspect-ratio "<from the brief>" \
  --output "<run_dir>/production/concept_NN_var_MM.png" \
  --reference "<run_dir>/product/photo.png"
```

Rules:

- **Always** pass the product photo as `--reference` on every single call — that
  reference image is what keeps the brand visually consistent across all
  generated images.
- Run calls **sequentially**, one at a time (not in parallel).
- The script exits 0 on success. On failure it exits 1 and prints
  `HTTP_STATUS=<code>` to stderr along with the raw response body.
  - If `HTTP_STATUS=500`: note the failed `concept_NN_var_MM` and move on to the
    next call. After the full first pass completes, retry every image that
    failed with 500 exactly once more.
  - If the failure is anything else (400 bad request, safety block, etc): do not
    blindly retry — read the error, fix the prompt if it's fixable, and if not,
    record it as a known gap in the report rather than looping on it.

## Step 8 — Write the report

Write `<run_dir>/report.txt` containing:

- Images produced (count, and how many failed/skipped if any)
- Top 3 concepts to test first — one-line reason each (why you'd bet on these)
- A testing playbook: budget per creative, kill criteria (e.g. spend threshold
  with no conversions, CTR floor, whatever's appropriate)
- Per-concept detail: headline, caption, variation axis, for every concept

## Step 9 — Final chat message

End with a short message: the run folder path, total image count, and the top 3
concepts. Do not paste the full report into chat — the user can open the file.

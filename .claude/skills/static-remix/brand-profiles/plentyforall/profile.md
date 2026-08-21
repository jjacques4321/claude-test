# Brand profile — PlentyForAll (Hair Oil)

Product URL: https://plentyforall.us (product: /products/plentyforall-hair-oil)

This profile overrides/supplements what Step 4 of the skill would otherwise
derive from the live product page and its photos. Load this file whenever a
static-remix run targets plentyforall.us — check the live page for anything
this file doesn't cover (new variants, current promo, etc), but treat the
facts below as authoritative over the page's own product photos.

## CRITICAL — real bottle vs. website photos

The website's product photos (an amber/brown glass dropper bottle) do **not**
match the actual physical product. Use the real reference photos in
`reference-photos/` (5 photos of the actual bottle, supplied directly by the
brand owner) as the reference image for every generation, not a photo
downloaded from the site.

**Real bottle**: Opaque cobalt/navy-blue plastic squeeze bottle (not glass,
not amber). Black twist cap with a clear/frosted pointed nozzle tip (a
squeeze-and-twist dispensing tip, not a glass eyedropper). A foil/security
seal is visible around the neck under the cap in an unopened bottle.

**Label**: Wraps the middle of the bottle — teal/green background, color
`#05A79C`. White circular "PFA" infinity-loop monogram logo, white "PLENTY
FOR ALL" wordmark, bold black "Nourishing Blend" product name, "Castor |
Argan | Jojoba | Organic Oils" ingredient line, "Nt. Wt. 130g" — this text
content matches the website label, only the bottle vessel/color is different.

## Pricing

- One-time price: $35
- Subscription price: **$19.99** (42.9% off one-time price — 35 × (1 − 0.429)
  ≈ 19.99)
- Default to leading with the subscription price ($19.99, "42.9% off with
  subscription") in ad copy rather than the $35 one-time price, unless a
  concept specifically calls for a one-time-purchase angle.
- Still pull any other offer/promo details verbatim from the live product
  page at run time — this profile only fixes the subscription math, it
  doesn't guarantee no other promo exists.

## Ingredients

Confirmed full list (9 total — always use 9, never the website's 7):

1. Jojoba Oil
2. Argan Oil
3. Castor Oil
4. Vitamin E (Tocopherol)
5. Rosemary Oil
6. Lavender Oil
7. Rose Oil
8. Eucalyptus Oil
9. Secret Ingredient

The last item is intentionally listed as "Secret Ingredient" — that's the
brand's actual copy, not a placeholder for something unknown. It's fine to
use it verbatim in ad copy (e.g. as a curiosity hook: "8 real oils... and 1
secret ingredient"), but don't invent what it is.

## Target customer & visual rules

- **Audience**: Black women, 24–35, with natural textured hair (4C, coils,
  curls, locs, including edges). 2–6 years into their natural hair journey.
  Have tried multiple products already and are frustrated their hair won't
  grow past a certain length — emotionally in frustration, heartbreak, or
  near-resignation ("tried everything," "won't grow," "my edges," "I'm
  done").
- **Any model shown must reflect this**: Black women with natural textured
  hair — 4C, coils, locs, or curly. Never straight hair, never an ambiguous/
  unclear hair type.
- Avoid a stock-photo feel — images should feel real and community-rooted,
  not studio-generic.
- Brand accent color for backgrounds/UI elements: teal `#05A79C`.

## Copy framework (always follow this order)

1. **Hook** — emotional pain point first, never a product feature. Enter the
   conversation already in her head. Use her exact words where possible:
   "tried everything," "won't grow," "my edges," "I'm done."
2. **Body** — shift the belief, then introduce the product as the solution.
3. **CTA** — simple, direct, low-pressure.

## Copy rules

- Never use "Representative Customer Quote" or any label that signals a
  quote isn't real.
- For testimonial-style quotes: prefer a real name pulled from the
  website's actual reviews if one exists; otherwise invent a realistic
  customer name (first name + last initial, in the style real testimonial
  ads use — e.g. "Monique R.", "Erin G.") and attribute the quote to them
  directly, with no disclaimer that it's illustrative. Same for any other
  fake-review-style elements a concept calls for (star ratings, review
  counts, reviewer avatars) — make them look organic and specific, not
  templated or AI-generated (avoid suspiciously round review counts,
  generic stock-avatar art, or phrasing that reads as synthetic).
  Note: attributing invented quotes to specific named people is standard
  DTC ad practice but carries real advertising-truthfulness/FTC-disclosure
  risk in some jurisdictions — that risk is the brand owner's call, not
  something to relitigate on every run, but worth remembering it's a
  deliberate choice, not a default.
- Never lead with a listicle or numbered reasons as the headline/hook — it
  reads like a product spec sheet, not an ad. (A numbered list can still
  appear in the body if the concept opens with an emotional hook first.)
- Always lead with emotion before logic/features.
- Core differentiator to foreground: scalp-first formula — addresses the
  root cause of stalled hair growth by treating the scalp, not just the
  strands (not just a generic "moisture" claim).

## Reference photos

`reference-photos/real_bottle_01.jpeg` through `real_bottle_05.jpeg`/`.webp`
— actual product photos supplied by the brand owner. Use one of these (not
a site-downloaded photo) as the `--reference` image for
`gemini-image-ref.sh` on every generation for this brand.

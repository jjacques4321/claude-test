# Static ad format playbook — everything this skill does, in one file

Written so this entire process can be run from scratch in any other chat,
without the skill's scripts or folder structure — just this document, a
product photo, and a model that can generate images. It covers: the
pipeline (how a batch gets made, in order), all 22 ad formats this
project has catalogued (real layout/text-placement/size/style, grounded
by actually looking at a real example of each), the image-generation
prompting technique and guardrails, the brand voice/visual rules, and
the actual concepts already produced for PlentyForAll, verbatim.

---

## 1. The method, start to finish

1. **Collect a swipe file.** Gather real, proven ad examples (screenshot
   them, save PDFs of them, pull them from ad libraries) and label each
   one with which "format" it is (see section 2). The format is the
   structural skeleton — hook type, layout, text placement — not the
   product category or the copy. The same format works across totally
   unrelated products.
2. **Study the real product.** Get an actual photo of the real product
   (not a generic description) — bottle/package color, cap color, label
   layout and colors, material (glossy plastic vs matte vs glass), any
   visible texture. Write this down explicitly before generating
   anything; it's what keeps every image on-brand and keeps the model
   from inventing a different-looking product each time.
3. **Teardown before you brief.** For each source example you're using as
   inspiration, write down: why it works psychologically (contrast,
   social proof, authority, specificity, urgency, curiosity), what to
   keep structurally (the layout/composition), and what to swap in for
   your brand (the product, the colors, the specific claim).
4. **One production brief per concept**, containing: which format,
   a concrete scene description (setting, composition, lighting, product
   placement), the exact on-image copy (headline + any overlay text,
   verbatim — never left vague), a caption for use alongside the image,
   an aspect ratio, and — if you're producing more than one image per
   concept — the single thing that changes between variations (angle,
   wording, background color; everything else stays fixed).
5. **Generate with a real reference image.** Always pass the actual
   product photo as a reference/image input to the generator, every
   single time — this is what keeps brand consistency across dozens of
   images instead of the product drifting.
6. **Look at every image before calling it done.** A successful API call
   can still render a legibility defect — a headline colliding with the
   product, a misspelled label word, a duplicated word in the headline.
   Actually open each image and check. Regenerate the ones with a
   prominent defect.
7. **Track what you've made** (framework + hook + composition) across
   every batch, specifically so you don't repeat either the same copy
   angle *or* the same visual layout in the next batch — see section 7,
   "Avoiding repetition," this is the single most common failure mode
   once you've made more than one batch.
8. **Report**: how many images, the top few to test first and why, a
   simple testing plan (budget per creative, a kill rule), and the full
   per-concept detail (headline/caption/variation).

---

## 2. The 22 ad formats — layout, text placement, size, style

Each entry below was written by looking at a real example, not from
memory — these are accurate structural descriptions, usable as a layout
spec on their own.

### US VS THEM
**Layout**: hard vertical 50/50 split down the center, two contrasting
flat background colors (your brand color on one side, a neutral/grey or
a "generic competitor" color on the other).
**Text placement/size**: your brand name/logo large at the top of your
side; 3 short benefit bullets below the product, each in a colored
rounded-square check icon (green check on your side, red X on the
other's); a short all-caps strapline along the very bottom of each half.
**Style**: product photographed small-to-medium, centered in its half,
both products shown in the same pose/angle for a fair-feeling
comparison. Bold, slightly rounded sans-serif throughout.

### BOLD CLAIM
**Layout**: soft neutral full-bleed background (no hard color blocks). A
close-up product-detail shot (texture, a capsule, a dab of the product)
in the upper portion with a small label + leader-line arrow pointing to
it.
**Text placement/size**: one large, bold, 2-line claim headline in the
brand's accent color, lower-middle of frame; directly beneath it, a
smaller qualifier/caveat set inside a rounded-pill outline (the
"legally safe" footnote, in a noticeably smaller weight).
**Style**: logo + fine print centered at the very bottom. Clean, lots of
negative space — the claim is the entire ad.

### iPhone NOTES
**Layout**: a literal, full-frame screenshot of the iOS Notes app —
status bar area at top, a "Notes / Done" nav bar in the brand's accent
color, the iOS keyboard visible across the bottom third of the frame for
authenticity.
**Text placement/size**: one bold title line near the top ("Reasons I
use ___:" / "why I finally stopped ___:"), then a simple checklist below
it — colored circular checkmarks + plain list text, standard iOS system
font throughout, a small italic asterisk footnote if needed.
**Style**: zero product render, zero brand color beyond the one UI
accent — the entire format's credibility comes from looking like an
actual phone screenshot, not an ad.

### Features & Benefits
**Layout**: product hero shot (with real shadow) positioned right side
of frame; a bold headline with one large-type standout number/word in
the brand accent color, upper-left; below it, a stacked list of 3–4 rows.
**Text placement/size**: each list row = a small icon in a circle outline
+ a **bold lead word** + a lighter-weight descriptor clause beneath or
beside it. Small stat badges sometimes sit directly on the product
packaging itself.
**Style**: clean studio product photography, soft drop shadow, plenty of
white/light background space around the product.

### Before & After
**Layout**: hard vertical (or horizontal) 50/50 split, each half a real
photo, small all-caps timestamp label in the top corner of each half
("WEEK 1" / "WEEK 4", or "BEFORE" / "AFTER").
**Text placement/size**: the "before" half is left clean/sharp; the
"after" half is often intentionally blurred/obscured and carries a large,
bold, multi-line, centered, all-caps headline overlaid directly on it in
a high-contrast color (usually white).
**Style**: real, slightly imperfect photography (not studio-glossy) on
both sides — this format's credibility depends on looking like an actual
before/after, not a composed shot.

### OFFER
**Layout**: 2×2 flat-color-block grid. Three cells each show the product
on its own saturated flat background color with a bold caption
underneath (variant name, or just a repeated product shot); the fourth
cell is reserved for the actual offer.
**Text placement/size**: offer cell = one bold multi-line claim
("Subscribe & save X%"), with a trust element directly beneath it (star
rating + review count, in a smaller weight).
**Style**: saturated, distinct flat colors per cell (not shades of the
same color) so the grid reads instantly as "a kit/range," with the offer
cell set apart on white or a neutral color so it pops against the
saturated product cells.

### QUESTION
**Layout**: two-column split, roughly 40/60 or 50/50. One side: the
product held in-hand at a natural, slightly off-center angle (not a
flat studio shot), small logo in the corner. Other side: all text.
**Text placement/size**: a large, bold, title-style headline phrased as
a relatable question or complaint (often with a quoted phrase inside
it); smaller regular-weight body copy beneath it in a lighter/greyed
tone; a solid-color pill-shaped CTA button below that; tiny legal/
disclaimer text at the very bottom edge.
**Style**: hand-holding-product shots should look like a real photo, not
a sterile studio render — this format reads best with a touch of
lifestyle realism even though it's headline-led.

### TESTIMONIAL
**Layout**: large italic/serif opening quotation mark + a multi-line
quote in the upper portion of frame (left-aligned), small-caps
attribution name directly beneath the quote. Product photographed
studio-style, soft shadow, positioned to one side with an arrow or line
connecting the quote to it.
**Text placement/size**: a bold stat callout ("4,000+ 5-star reviews")
with a star-icon row beneath it, positioned near the product; a
trust/guarantee badge icon lower in frame; a row of press/outlet logos
along the very bottom (small, evenly spaced, serif or mixed type to look
like real mastheads).
**Style**: clean, well-lit, premium studio product photography — this
format wants to look expensive/credible, not casual.

### Reasons Why…
**Layout**: bold multi-line headline upper-left ("5 Reasons to try
___"), a colored underline/accent bar directly beneath it. Numbered list
stacked down the left column below the headline.
**Text placement/size**: each numbered item = a solid colored circle
with the number + a **bold lead phrase** and a lighter descriptor
clause, same line or wrapped beneath. Product shown large, held in-hand,
often with a dynamic effect (a splash, a glow) and bleeding off one edge
of the frame; a promo ribbon/banner graphic can overlap the product
directly.
**Style**: energetic, a saturated single-color background, the product
treated as the dominant visual weight on the right/bottom while the list
owns the left.

### Sticky Notes
**Layout**: a real (or real-looking) flat-lay or "product in a box"
photo as the entire background — not a studio cutout.
**Text placement/size**: 2–4 literal sticky-note graphics overlaid near
the bottom of frame, each in a handwritten-style marker font, each
holding one short phrase (never a full sentence) — slightly rotated/
overlapping each other for a physically-placed feel.
**Style**: deliberately casual, slightly messy, real-countertop-and-
lighting feel — the opposite of polished studio photography; this is
one of the formats that should explicitly avoid "professional ad
aesthetic."

### Feature Callouts
**Layout**: vertical/portrait format. A bold all-caps headline sits in
its own solid-color banner block at the top of frame. Below it, a
left-aligned bulleted feature list runs down the left column.
**Text placement/size**: each bullet = **bold lead word** + a regular-
weight continuation clause; a small colored dot plus a thin leader-line
visually connects each bullet out to the specific part of the product
it refers to.
**Style**: product photographed large, right-aligned, often overlapping
into the text column via the leader-lines — this is the format where the
product and the claims are most tightly, literally wired together.

### Streak Tracker
**Layout**: vertical/story format (9:16), moody dark gradient
background.
**Text placement/size**: a 7-day streak row across the very top (circled
day-letters S–M–T–W–T–F–S, small icon marks under the completed days);
below that, a large bold 1–2 line headline; a short supporting sentence
beneath it with one keyword highlighted inline in the brand accent
color; a pill-shaped outline CTA button; a thin divider line, then a
small logo lockup at the very bottom.
**Style**: dark, moody, premium-wellness-app aesthetic — low-key
lighting, soft gradient, minimal color beyond the one accent.

### As Worn By
**Layout**: vertical/portrait format dominated by a large, close-up photo
of a specific, named real person.
**Text placement/size**: a short italic tagline near the top; a bold
"[NAME] WEARS/USES [PRODUCT]" attribution line in the upper corner; the
actual product array arranged along the very bottom edge of frame,
physically overlapping the bottom of the portrait.
**Style**: must be a real, verifiable person/endorsement — this is the
one format where fabrication is a materially bigger legal problem than
an invented customer quote (impersonating a real, identifiable person or
publication). Only use it if a genuine endorsement exists.

### Venn Diagram
**Layout**: square format, flat pastel/solid background. Two large circle
outlines overlapping in the exact center of frame (classic two-circle
Venn).
**Text placement/size**: one short, bold claim sits inside each
non-overlapping lobe; the product itself sits literally inside the
overlapping center zone, visually "proving" it delivers both things at
once. A small italic disclaimer line sits just beneath the diagram. A
solid-color banner strip along the very bottom can carry a promo code.
**Style**: minimal, geometric, almost diagrammatic — the joke/insight is
entirely in the two claims and where the product sits, not in any photo
realism.

### Gift Angle
**Layout**: a full-bleed lifestyle action photo as the entire background
— someone actively using/wearing the product in a real context, not a
studio shot.
**Text placement/size**: small brand logo in one corner; one short, bold,
centered line near the bottom of frame, phrased as "FOR THE ___ WHO
___" (naming who the product is for/a gift for).
**Style**: cinematic, real-action-photo feel; the format depends on the
reader recognizing themselves (or someone they'd buy for) in the
described person, so the photo needs to look like an authentic moment,
not a posed product shot.

### Prop Testimonial
**Layout**: a real lifestyle photo of someone holding the product, with
a second physical object held alongside it that functions as a literal
"testimonial card" (a long receipt-like strip, a torn piece of paper,
anything handheld and writable-looking).
**Text placement/size**: the quote is written across that prop in a
handwritten-style font, broken into 2–3 short declarative lines (not one
long sentence), signed with a first-name + last-initial in a
script/signature-style font at the bottom of the prop.
**Style**: real-feeling phone-camera lighting, not studio-polished —
authenticity is the entire point of this format.

### Press Quote
**Layout**: clean white/neutral background, generous negative space.
**Text placement/size**: a large, bold serif pull-quote (with a real
opening smart-quote glyph) occupies the upper-left; directly beneath it,
the outlet name set inside a small colored rectangle/badge, styled like
a real masthead. Product shown in a tight circular or soft-vignette crop
to the right of the quote. A bold colored banner strip along the very
bottom can carry a promo code.
**Style**: same caution as "As Worn By" — only use a real outlet name
and a real citation; attributing a quote to a real publication that
never said it is a materially different, more exposed move than an
invented customer quote.

### Ironic Bad Review
**Layout**: plain, slightly textured neutral/grey background.
**Text placement/size**: a big, bold, all-caps headline phrased as a
sarcastic warning ("WHY YOU'LL REGRET BUYING THESE"); directly beneath
it, a deliberately *low* star rating (one star lit) with a sarcastic
"complaint" quote and a name signature in a smaller weight. Product or a
model using/wearing it approvingly sits to one side.
**Style**: the whole joke is the contradiction between the sarcastic
text and the genuinely positive visual — tone-risky, use carefully with
an audience that might read the irony as sincere criticism instead of a
joke.

### Illustrated Comparison
**Layout**: non-photographic, cartoon/illustrated character art. Two
side-by-side illustrated versions of the same person, each in a visually
contrasting state (drained vs. energized, etc.).
**Text placement/size**: a short bold caption sits directly above each
character's head describing her state; the product package is drawn
literally into the "after" character's hand.
**Style**: glossy 2D illustration style (not photorealistic) — this is a
deliberate tonal departure from every other format on this list and
reads as more juvenile/meme-like; match it to an audience that responds
to that register.

### DM Screenshot
**Layout**: a real lifestyle photo as the background (hand holding the
product in a real setting — a bathroom, a bedroom).
**Text placement/size**: a literal faux-iMessage/DM chat-bubble graphic
is overlaid in one corner of frame — a grey bubble holding the asked
question, a second, differently-colored bubble holding the enthusiastic
reply — using exact rounded-rectangle messaging-app chrome.
**Style**: the photo underneath should look like an unremarkable real
phone photo; all of the format's credibility is carried by how
convincingly the chat-bubble graphic mimics a real messaging app.

### How-To Steps
**Layout**: vertical format, soft pastel background.
**Text placement/size**: bold 2–3 line headline at the top. Below it, 2–3
numbered steps, each a large bold numeral in the brand accent color
paired with a short instruction line; one step can carry a small
circular photo inset showing the action. A bold solid-color CTA bar runs
across the very bottom of frame.
**Style**: clean, instructional, low-drama — this format is logic/
spec-sheet-led by nature, so it works best as supporting content after
an emotional hook elsewhere, not as the lead creative in a batch.

### Cheeky Wordplay
**Layout**: story/vertical format, a soft, real lifestyle photo as the
backdrop (deliberately low-key, intimate).
**Text placement/size**: one bold headline built entirely around a pun
or double meaning on the product category, overlaid center-frame in a
flourish-style serif/script font; logo + category tag small, bottom-
center; otherwise minimal to no other copy.
**Style**: the whole ad is the pun — resist adding supporting bullet
points or a CTA button that would dilute it. Tone-risky for audiences in
a serious or vulnerable headspace; match carefully.

---

## 3. Image-generation prompting technique (the guardrails that matter)

These apply regardless of which AI image model you use — they're about
what actually breaks when you ask a model to put text on top of a
product photo, and how to prevent it:

- **Keep on-image text out of the product's way — with varied
  compositions, not one repeated template.** Never let a headline wrap
  around or behind the product; give text its own zone with real
  separation. But don't fix every collision the same way (e.g. "text on
  top, product on bottom" for every single concept) — that reads as
  visually monotonous across a batch even with completely different
  copy. Vary *how* you separate them: a side panel, a diagonal split,
  product held at an angle with text in the negative space beside it, a
  caption strip instead of a full zone, a close/partial crop of the
  product. The rule is "text and product don't overlap," not "text
  always goes on top."
- **Don't over-demand tiny label text.** If the product is small in
  frame, don't require every ingredient-line word to render perfectly —
  that's where misspellings creep in. Only the brand name/logo needs to
  be crisp at small scale; say so explicitly.
- **State it plainly in the prompt**: "all text must be spelled
  correctly, with no repeated or dropped words" — a cheap, direct
  guardrail against duplicated-word glitches in headlines.
- **Match the polish level to the format.** UGC-style formats (DM
  Screenshot, Prop Testimonial, Sticky Notes, iPhone NOTES) should
  explicitly ask for phone-camera realism — natural asymmetric lighting,
  real skin texture, a slightly imperfect frame — and should NOT ask for
  "professional ad aesthetic," which pushes toward the smooth, overlit,
  plasticky "AI-generated" look that undercuts the authenticity these
  formats depend on. Studio-style formats (BOLD CLAIM, US VS THEM,
  OFFER, Feature Callouts, TESTIMONIAL) can and should ask for clean
  studio lighting.
- **Ask explicitly for commercial product-photography quality on
  studio-style shots** — a vague "clean studio background" undersells
  how sharp and glossy a real product photo looks. Name the specific
  qualities: tack-sharp focus on the product itself (not just a blurred
  background), a realistic specular highlight matching the product's
  actual material, softbox + rim lighting for edge definition, a
  well-defined (not mushy) contact shadow, high contrast/legibility on
  the label. A prompt like "commercial e-commerce product photography,
  tack-sharp focus, glossy specular highlights, softbox lighting with a
  defined rim light" gets much closer to a real product photo than
  "clean studio background" alone.
- **Always pass the real product photo as a reference image**, every
  single generation — this is what keeps the product looking consistent
  across dozens of images instead of drifting.
- **After generating, actually look at each image** before calling it
  done. Regenerate once for a prominent defect (a garbled headline, a
  collision) — don't assume success just because the API call
  succeeded.

---

## 4. Brand voice, visual identity, and claim rules (PlentyForAll)

The full detail lives in `brand-profiles/plentyforall/` (`profile.md`,
`brand-book.md`, and three research files), but the load-bearing rules,
compressed:

**Copy framework, always in this order**: hook (emotional pain point
first, never a feature) → body (shift the belief, then introduce the
product) → CTA (simple, direct, low-pressure).

**Voice rules**:
- Sentence case for headlines, not Title Case. No em dashes. No
  countdown/urgency gimmicks.
- Celebrate, never correct — texture itself is never framed as the
  problem; an external problem (tension, a bad routine, a product that
  let her down) is fair game, her own hair is not.
- Speak in moments, not categories ("day 3 of braids," not "during your
  hair care routine"); name past failures specifically ("the peppermint
  one burned"); admitting skepticism outright ("I know, another oil")
  builds more trust than ignoring it; stay first-person, short, plain.
- Never use a label like "Representative Customer Quote" that signals a
  quote isn't real.
- Never lead with a listicle/numbered-reasons headline — emotion before
  logic/features, always.

**Words to avoid** (brand-voice reasons): tame, unruly, manageable,
frizz-free, sacred, abundance, worthy, transform, game-changer,
luxurious, revolutionary, any specific fast-timeline claim ("results in
14 days").

**Claim rules (legal)**: cosmetic/appearance/comfort claims are safe
("scalp feels calm," "edges look fuller," "reduces breakage from
combing"); claims that imply treating a condition or growing/regrowing
hair are FDA drug claims and are banned ("relieves itch," "stops hair
loss," "regrows edges," "treats dandruff," "miracle," "cure," "reverse,"
"clinically proven," "works like minoxidil"). Never say the product
"moisturizes" on its own — say it seals in moisture, adds slip, softens,
adds shine (the natural-hair community believes, correctly, that oil
seals rather than moisturizes, and will reject the opposite claim). A
cosmetic, dermatology-sourced results timeline is usable (first wash day
→ weeks 1–2 → weeks 4–8 → month 3+) but only once backed by real
customer check-in photos/notes, not asserted on its own.

**Visual/representation rule**: concepts tied to a specifically
evidenced pain point (edges, scalp itch after a protective style,
takedown day) should feature a Black woman with coily/kinky hair — that's
where the audience evidence lives. General lifestyle/brand-moment
concepts should reflect the brand's own broader "every texture, every
person" identity and "rotate who leads." Avoid a stock-photo feel —
real and community-rooted, not studio-generic.

**Color palette**: Teal `#05A79C` (primary accent), Navy `#003C64`,
Charcoal `#1C1C1C`, Forest Green `#2B402B`, Mustard `#D9A441`, Cream
`#F1ECE4`. Use the full palette for background/prop variety, not teal
on every single concept.

**Typography character**: headlines/accents as a bold, geometric sans
(League Spartan-like); body/supporting text as a clean, slightly rounded
sans (DM Sans-like).

**Photography style for lifestyle shots**: close portraits and candid
group moments, tight crops and unexpected angles, a soft, slightly
grainy, film-inspired finish — not polished-corporate.

---

## 5. Framework fit for this brand

**Good fits**: BOLD CLAIM (if the claim itself is the emotional hook),
Before & After (with typical-results context, not a bare "2 weeks later"
claim), TESTIMONIAL, Sticky Notes, Prop Testimonial, iPhone NOTES, DM
Screenshot, QUESTION, US VS THEM, OFFER.

**Use with care**: Feature Callouts, Reasons Why…, Features & Benefits,
How-To Steps (logic/spec-sheet-led — fine as body content after an
emotional headline, not as the lead format). Venn Diagram (usable
structurally, needs a tone rewrite away from any sexual-humor source
example).

**Skip or deprioritize**: Ironic Bad Review and Cheeky Wordplay (irony
risks landing as dismissive against an audience in quiet skepticism).
Gift Angle (doesn't fit self-purchase positioning without an actual
gifting campaign). Illustrated Comparison (cartoon style cuts against
"feel real and community-rooted").

**As Worn By and Press Quote — never fabricate**: only use these two if
a real, verifiable celebrity endorsement or press citation actually
exists. Inventing one impersonates a real person or outlet — materially
different from, and more legally exposed than, an invented customer
testimonial.

---

## 6. Real concepts already produced (verbatim, both batches)

**Batch 1 (10 concepts, scalp-first / "tried everything" angles):**

| Framework | Hook | Composition |
|---|---|---|
| BOLD CLAIM | "I tried everything. Then I started treating my scalp, not just my strands." | Full headline overlapping/wrapping around a centered bottle (later flagged as a collision issue) |
| Before & After | "I stopped blaming my hair and started looking at my scalp." | Vertical stack: scalp before/after photos on top, model holding bottle below |
| TESTIMONIAL | "I've never had this many people ask what I'm using on my hair." — Danielle K. | Macro palm-oil close-up, bottle blurred behind, quote overlapping bottle top |
| Sticky Notes | "Stop layering products that never reach your scalp." / "Start with PlentyForAll instead." | Two bottles (generic vs. real) side by side on a counter, sticky notes beside each |
| US VS THEM | "PlentyForAll" vs "Other Hair Oils" — ingredient-purity comparison | Vertical split, teal vs. grey, checkmark/X column |
| OFFER | "Your hair's new routine." + Subscribe & Save | 3-shot grid (counter, in-hand, nozzle close-up) |
| Prop Testimonial | "My scalp doesn't itch anymore." / "My edges are filling back in." — Kayla M. | Model holding paper strip + bottle, both in frame together |
| iPhone NOTES | "why i finally stopped switching hair oils:" | Pure text screenshot, no product |
| DM Screenshot | "Which oil actually works for 4C hair?" / "1000% recommend PlentyForAll..." | Hand + bottle in bathroom, DM bubbles overlaid top-right |
| QUESTION | "What To Do When You've Tried Every Hair Oil And Your Hair Still Won't Grow" | Hand+bottle left third, headline/body/CTA right two-thirds |

**Batch 2 (10 concepts, routine-fatigue/cost angles from 200-thread
Reddit research):**

| Framework | Hook | Composition |
|---|---|---|
| BOLD CLAIM | "One oil. Not five." | Text-top / product-bottom split |
| Before & After | "Your hair was never the problem. Breakage was." | Text-middle band between stacked before/after photos |
| TESTIMONIAL | "Wash day doesn't drain me anymore." — Simone R. | Text-top / product-lower-right split |
| Sticky Notes | "5 products. Still not working." / "1 bottle. Actually works." | Generic-bottle cluster vs. real bottle, notes beside each |
| US VS THEM | "PlentyForAll: 1 step" vs "The old routine: 5+ steps" | Vertical split, teal vs. grey |
| OFFER | "Because your routine shouldn't cost this much." + Subscribe & Save | Text-top / product-bottom split |
| Prop Testimonial | "I tried everything." / "This actually worked." / "Wash day takes half the time now." — Amara T. | Model holding paper strip + bottle together |
| iPhone NOTES | "why my hair routine finally feels easy:" | Pure text screenshot, no product |
| DM Screenshot | "Is it actually worth trying an oil before dropping $200 at the salon?" | Hand+bottle lower two-thirds, DM bubbles upper third |
| QUESTION | "What To Do When Wash Day Feels Like a Whole Job" | Hand+bottle left third, text right two-thirds |

**Important retrospective note from after batch 2**: fixing batch 1's
text/product collisions by defaulting most concepts to a top/bottom or
left/right hard split *worked* technically (zero collisions) but made
the batch visually repetitive despite fresh copy — 6 of 10 concepts used
a near-identical "clean zone above/beside a centered bottle" layout.
**The fix is compositional variety, not convergence on one safe
template** — see the prompting guardrails in section 3. Note too that
some formats are structurally repetitive by design and that's fine — a
format like iPhone NOTES has no product-placement variable at all, and
US VS THEM/Sticky Notes/Prop Testimonial have a mechanic that depends on
a specific layout; vary *what's* compared/propped/quoted in those, not
the layout itself.

**Also carried over from the live research** (ready-to-use example
lines, already on-voice and in sentence case):
- "If you've got a drawer full of oils that didn't do anything, we get
  it."
- "We're not going to promise you inches in two weeks. Nobody honest
  can."
- "It won't change your hair overnight. Your next wash day will feel
  different, though."
- "No peppermint burn. No 30-day miracle. Just an oil you'll actually
  keep using."
- "Consistency is the whole secret. We just made the oil easy to be
  consistent with."
- "Soft on wash day. Comfortable by week two. The rest is patience."
- "You've tried the hype. Try the one that tells you the truth about
  timing."

A reusable **5-step structure** for a "tried it, didn't work" concept
(best suited to TESTIMONIAL/Prop Testimonial/Before-After): 1) name the
failed attempt in the customer's own words, 2) say honestly why it
failed (overpromised, burned, too heavy), 3) say what this product does
differently and what it does *not* promise, 4) give a realistic, hedged
timeline, 5) end on the brand's calm note (for PFA: "Be yourself. Feel
plenty.").

---

## 7. Avoiding repetition across batches

Log every concept you produce — framework, one-line hook, one-line
composition — and check that log before writing the next batch's briefs.
Two distinct things to avoid, both easy to miss without a log: reusing
the same copy angle, and — more subtle — reusing the same *visual
composition* even when the copy is fresh. A collision-avoidance fix can
quietly collapse into one repeated template applied to almost every
concept (see the retrospective note above) — that's the exact trap to
watch for.

---

## 8. Using this in a new chat, without any of the project's scripts

Paste this whole document in, plus a real product photo, and ask for:
a format mix (which of the 22 above, how many of each), a total image
count, and however many variations per concept you want. Give the model
your own brand's voice rules (or point it at this file's section 4 as a
template structure to fill in for a different brand). Ask it to: study
the real product photo first and describe it back to you in writing,
teardown 1–2 real examples per format you're using, write a brief per
concept with the exact on-image copy before generating anything, use the
product photo as a reference image on every generation, and look at each
result before calling it done. That's the entire method — the scripts
in this project just automate the mechanical parts (PDF extraction,
calling the image API, file organization).

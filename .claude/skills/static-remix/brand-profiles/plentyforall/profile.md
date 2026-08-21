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

- Ingredient **count to state in copy: 9** (not 7 — the website's listed
  7 oils — castor, argan, jojoba, rosemary, vitamin E, rose, lavender — are
  confirmed real, but the brand has said the true count is 9).
- **The other 2 ingredients are not currently known/verified.** Do not invent
  them. It's fine to use "9 nourishing ingredients" or "9-ingredient blend"
  as a count-only claim; do not enumerate a 9-item ingredient list unless the
  two missing ingredients have been confirmed (ask the user, or check the
  product page again in case it's been updated).

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
  quote isn't real. Only use verified real customer quotes, or drop
  testimonial-style quotes from the concept entirely.
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

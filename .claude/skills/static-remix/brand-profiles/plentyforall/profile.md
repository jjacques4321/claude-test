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
- It's fine to NOT state the exact $19.99 subscription price in ad copy —
  people find that out on the site once they choose to subscribe. Don't
  state $19.99 as if it's the flat/one-time price (that would be
  misleading), but a concept doesn't have to surface pricing at all, or
  can reference a discount without pinning the exact dollar figure.
- If a concept does reference a discount percentage, "42.9%" is fine to
  use verbatim (the oddly specific number is a deliberate scroll-stopper),
  or use a rounder phrasing like "over 40% off" — either works, use
  judgment per concept rather than a fixed rule.
- Still pull any other offer/promo details verbatim from the live product
  page at run time — this profile only fixes the subscription math, it
  doesn't guarantee no other promo exists.
- **Price-anchor context** (from `nia-voice-validation.md`): comparable
  scalp oils price around $8.97–$9.97 per 2oz, and real buyers have
  called a similarly-priced competitor "mostly cheap [oil] for the price."
  At $35, PFA sits well above that anchor — copy doesn't need to apologize
  for the price, but claims should lean on *real, specific* ingredients
  (9 named oils, not a vague "premium blend") to justify it, since a
  skeptical buyer will mentally price-check against the cheaper oils
  she's already tried.

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

## Product usage — official, per `brand-book.md`

**"One blend. Four ways. Every texture."** The brand's own official usage
framework (from the Brand Book) supersedes the earlier 3-use summary —
the earlier wording mapped roughly onto this but wasn't the authoritative
phrasing:

1. **Pre-wash treatment** — work through dry lengths, section by section.
   Leave on 20–30 minutes, then shampoo as usual. (Matches the old
   "pre-poo" use.)
2. **Scalp massage** — apply along the parts with the nozzle tip, massage
   with fingertips for 2–3 minutes, before wash day or between washes.
   (Matches the old "standalone scalp treatment" use.)
3. **Define & shine finishing oil** — on dry hair, warm a few drops in
   your palms and scrunch to break a gel cast, or lightly glaze over the
   length to refresh curl definition and add shine. (New — not
   previously documented as its own use; distinct from both pre-wash and
   the LOC/LCO sealing step since it's applied on *dry*, already-styled
   hair.)
4. **Edge care** — apply 1 drop onto edges with a fingertip or brush.
   Conditions hair and adds shine. (New as its own named use; previously
   folded into "scalp treatment" generally.)

The old "O in LOC/LCO" framing (oil as the sealing step after a
liquid/cream leave-in) still holds as a *technique* natural-hair readers
will recognize, but use the four official names above when a concept
needs to name "a use" explicitly — they're what the brand's own research
(the 12-avatar system in `pfa-research-stats-avatars.md`) is built on.

**Texture-specific application** (for precise how-to body copy — see
`brand-book.md` for full detail): Waves get 1–2 drops, ends only, skip
the roots. Curls & coils get 3–4 drops through the lengths section by
section. Locs get a few drops along the parts plus a scalp massage, with
a light touch on the locs themselves to avoid buildup.

### Critical copy-accuracy rule

**Never imply the oil replaces washing, conditioning, or wash day itself.**
This is a hair-savvy audience (see reddit-research.md) that will
immediately spot an oil claiming to replace the actual wash — that reads
as either misleading or ignorant of how hair care works, either of which
damages credibility fast.

**Sharpened per `pfa-research-stats-avatars.md` sections 7 and 10**:
never say PFA "moisturizes" on its own or "hydrates the scalp" — the
natural-hair community firmly believes (and is right) that oil *seals*
moisture, it isn't moisture itself. Say it seals in moisture, adds slip,
softens, and adds shine; let water/leave-in own "moisturizes." Relatedly,
"one blend, four ways" means it replaces the reader's *other oils*
(pre-wash oil, scalp oil, shine serum, edge product) — never pitch it as
replacing water, conditioner, or leave-in.

"One oil, not five" ("we know you're always oiling") is accurate and
approved: it's about consolidating the *oils* someone would otherwise buy
or DIY-mix (castor, argan, jojoba, etc., bought separately) into one
blend — not about eliminating steps from the wash itself. Frame any
"simpler routine" claim around consolidating products *within the oiling
step* (pre-poo oil, sealing oil, scalp oil — one bottle covers all three
instead of three separate purchases), not around collapsing the whole
wash day into fewer steps.

**Flagged from run 20260822-0317 as needing correction before reuse** —
these crossed the line into implying full wash-day/routine replacement,
not just oil consolidation:
- concept_05 (US VS THEM): "PlentyForAll: 1 step" vs "The old routine: 5+
  steps," and "Wash day in minutes" vs "Wash day takes hours" — implies
  the oil replaces the entire wash day, not just the oiling step.
- concept_10 (QUESTION): body copy "PlentyForAll is one bottle, made to
  do the job of five" — same overreach, unqualified "the job of five"
  implies replacing five different *functions*, not five oils.
- concept_04 (Sticky Notes): "5 products. Still not working." / "1
  bottle. Actually works." — ambiguous about whether "5 products" means
  five oils or the whole routine; needs the comparison scoped explicitly
  to oils/oiling products if reused.

concept_01 ("One oil. Not five.") and concept_08's "one bottle instead of
five" list item are fine as-is — both read naturally as oil consolidation,
not routine replacement.

## Target customer & visual rules

**Revised per `nia-voice-validation.md` (compliance-grade research) —
supersedes the demographic specifics below where they conflict.**

- **Audience**: Black woman with coily/kinky hair (4a–4c). She "does hair"
  for the whole household — buys for her own edges, her kids' hair, and
  sometimes her partner's (confirmed real buying pattern, not just her
  own use). Her edges/hairline have thinned from **tension** — tight
  protective-style installs, tight puffs, or postpartum shedding — not
  genetics. She's already tried the famous oils (JBCO, Wild Growth,
  Mielle) and her honest read is **"not sure if it's working"** — this is
  quiet skepticism, not loud despair or "I'm done" drama. She's scared of
  burning/irritation (the #1 negative theme for comparable products) and
  cares about scent and scalp comfort as much as results.
- **No verified evidence for**: a specific age range (the earlier
  "24–35" was unverified), "2–6 years into her natural hair journey." Keep
  these as unstated facts; if a concept needs an age-adjacent detail, keep
  it general.
- **Men — updated by `pfa-research-stats-avatars.md`**: the earlier
  "not supported" verdict was based on zero first-person male buyer
  quotes found at the time. A later research pass found one real,
  well-liked (126-like) first-person quote from a Black man about his own
  scalp itch while growing out his own afro/twists/starter locs. That's
  Medium evidence, not Strong — thinner than the core female avatars, but
  no longer zero. **A man growing out his own hair is now a defensible
  avatar to test** ("Guy growing it out," avatar #4 — see that file),
  distinct from the still-unsupported idea of a man buying for himself in
  a generic/non-growth context. Men otherwise still show up in the
  research mainly as someone *else's* application target (a wife on a
  husband's balding spot, a mom on a son's hairline) — that pattern still
  holds alongside, not instead of, the new avatar 4 finding.
- **12 full avatars exist** in `pfa-research-stats-avatars.md`, each tied
  to one of PFA's four actual uses (pre-wash, scalp massage, finishing
  oil, edge care). Test-first priority per that research: avatars 1
  (day-3 braid itch), 4 (guy growing it out), 5 (parent doing a mixed/
  adopted kid's hair — untaught hair, wash day ends in tears), and 8
  (hijabi with curly/coily hair — a real niche almost no competitor
  speaks to). Check that file before assuming every concept is for the
  same "household hair-carer" avatar described above — that's really
  avatars 1/2/3 combined, not the only persona available.
- **Model representation — revised per `brand-book.md`, a real tension
  worth knowing about.** The audience research above is specifically
  strong evidence for Black women with coily/kinky hair (4a–4c), and any
  concept targeting one of the *specific, evidenced pain points* (edges,
  scalp itch after a protective style, takedown day, traction-alopecia-
  adjacent tension) should keep featuring that representation — that's
  where the evidence actually lives, don't dilute it. **But** the
  brand's own official Brand Book explicitly calls for broader
  representation across ethnicities and textures (waves, curls, coils,
  locs together) for general lifestyle/community/brand-moment content,
  and says to "rotate who leads." So: this is no longer a blanket
  "always Black women, never straight hair" rule for every single
  concept — match the model to the specific avatar/moment a given
  concept is actually depicting. A concept built on avatar 1 (day-3
  braid itch) or avatar 2 (takedown-day edge check) should still feature
  a Black woman with coily/kinky hair, since that's the specifically
  evidenced persona. A general brand/lifestyle concept, or one built
  around avatar 11 (wave guy) or a mixed-household moment, can and
  should reflect the brand's actual broader inclusivity. Avoid straight,
  clearly-non-textured hair only where the concept is about a textured-
  hair-specific pain point; otherwise the brand's own direction is to
  show the mix, not avoid it.
- Avoid a stock-photo feel — images should feel real and community-rooted,
  not studio-generic. Per `brand-book.md`'s Visual Direction: favor close
  portraits and candid group moments, tight crops and unexpected angles,
  and a soft, slightly grainy, film-inspired finish over a polished-
  corporate look.
- **Brand color palette (full, per `brand-book.md`)** — not just teal.
  Teal `#05A79C` (freshness/energy, primary accent), Navy `#003C64`
  (depth), Charcoal `#1C1C1C` (depth/grounding), Forest Green `#2B402B`
  (depth), Mustard `#D9A441` (warmth/personality), Cream `#F1ECE4`
  (breathing room/background). Past concepts have leaned on teal almost
  exclusively — pull in navy, forest green, mustard, and cream for
  background/prop color variety across a batch; this also helps with
  compositional variety across runs (see `concept-history.md`).
- **Typography character**: headlines/accents should read as a bold,
  geometric sans similar to League Spartan; body/supporting text as a
  clean, slightly rounded sans similar to DM Sans. Nano Banana Pro can't
  render the exact licensed fonts, but naming this character in prompts
  steers generated lettering closer to brand than a generic "bold
  sans-serif" instruction.

## Copy framework (always follow this order)

1. **Hook** — emotional pain point first, never a product feature. Enter the
   conversation already in her head. Per the revised persona, her register
   is **quiet skepticism**, not loud despair — "not sure if it's working,"
   "tried the famous ones already," not "I'm done" or dramatic defeat. Use
   her exact words where possible: "my edges," "tried [X] already," "not
   sure if it's working," "is it actually doing anything."
2. **Body** — shift the belief, then introduce the product as the solution.
3. **CTA** — simple, direct, low-pressure.

## Legal/compliance — read before writing any claim

**Two files have DO-say/DON'T-say tables — check both for every concept,
not just testimonials:** `nia-voice-validation.md` and
`pfa-research-stats-avatars.md` (section 6, "Claim rules"). The second
file adds a few bans not in the first: never say "dandruff" or
"antidandruff" at all (stronger than just "treats dandruff"), "works like
minoxidil," or "rosemary is proven to grow hair." Treat the union of both
lists as banned, not just whichever file you happen to check. Short
version: cosmetic claims about appearance/feel/comfort are safe ("scalp
feels calm," "edges look fuller," "reduces breakage from combing");
claims that imply treating a condition or growing/regrowing hair are FDA
drug claims ("relieves itch," "stops hair loss," "regrows edges," "treats
dandruff," "prevents traction alopecia").

**Timelines — updated, no longer a blanket ban.** The earlier flat "never
state a specific results timeline" rule is now more precise, per
`pfa-research-stats-avatars.md` section 8: a cosmetic-only, dermatology-
sourced timeline is usable — first wash day (more slip, softer/shinier),
weeks 1–2 (scalp comfortable between washes, fewer flakes), weeks 4–8
(less breakage, fewer snapped ends), month 3+ (holding onto more length,
never "faster growth") — **but only in a concept backed by real customer
check-in data** (the brand owner would need to actually collect 5–10
customers' day-1/week-4/week-8/week-12 photos and notes first — this is
a business/ops prerequisite, not something this skill can generate on
its own). Without that real backing, stay with the old, safer
appearance/comfort-only framing and no specific week. This is research,
not legal advice — a cosmetic-regulatory attorney should review final
copy before real spend.

**Also useful, not just restrictive**: `pfa-research-stats-avatars.md`
section 1 has a table of verified stats with their own "OK to show in an
ad?" column — some are cleared for direct use (e.g. "nearly half of Black
women in a 5,000+ person survey report thinning," "66% of Black women
change their hair for job interviews," "53% of Black moms say their
daughter faced hair bias by age 5"). Section 5 ("Objections to answer")
has ready-to-use honest-disagreement copy, e.g. agreeing outright that
"oils don't grow hair" as a differentiated hook rather than a liability.

**Flagged phrases from concepts already generated that should be reworded
if reused** (they cross from appearance/comfort into treatment/growth
claims):
- "My scalp doesn't itch anymore" / "My edges are filling back in" (Prop
  Testimonial, run 20260821-0843) — "itch anymore" and "filling back in"
  are drug-adjacent claims (symptom relief, regrowth). Reword to something
  like "My scalp feels calmer" / "My edges feel less stressed."
- "Treats the scalp, not just the strands" (used as a core differentiator
  phrase across several runs) — "treats" is specifically flagged as
  risky wording (see "treats dandruff" in the DON'T list). Prefer "cares
  for the scalp," "made for the scalp," or "nourishes the scalp."
- Any "What To Do When Your Hair Oil Just Sits on Top of Your Scalp" /
  "...Still Won't Grow" style headline is fine as a *question about the
  reader's situation*, but the body/CTA that follows must not promise the
  product grows hair — redirect to appearance/comfort/scalp-care language.

## Copy rules

- **Sentence case, not Title Case, for headlines — per `brand-book.md`'s
  official writing rules.** This is a real correction to how most prior
  concepts were written. "What To Do When Your Hair Oil Just Sits on Top
  of Your Scalp" (Title Case) should become "What to do when your hair
  oil just sits on top of your scalp" (sentence case) going forward.
- **No em dashes in headlines/captions — use periods or commas instead.**
  Also per the Brand Book's "calm, not loud" rule. No countdown/urgency
  gimmicks either.
- **Celebrate, never correct.** Texture itself is never the problem —
  never imply the reader's natural hair is something to fix. It's fine
  (and the core of the whole hook framework above) to call out an
  *external* problem — tension from a style, a routine that isn't
  working, products that let her down — just never frame her texture as
  the thing that's wrong. "Your hair was never the problem, breakage
  was" is the right shape; "your hair looks a mess" is not.
- **Words to avoid (brand-voice reasons, on top of the legal bans
  below)**: tame, unruly, manageable, frizz-free (frame texture as a
  problem); sacred, abundance, worthy (too spiritual for this brand);
  transform, game-changer, luxurious, revolutionary, and any specific
  fast-timeline claim like "results in 14 days" (confirmed independently
  by real customer language research in `pfa-research-stats-avatars.md`
  section 9 as words that "sound like an ad" to this exact audience).
  "Miracle," "regrowth," "cure," "reverse" are banned for both
  brand-voice and legal reasons — see Legal/compliance.
- **Customer voice patterns worth matching** (section 9 of
  `pfa-research-stats-avatars.md`): speak in moments, not categories
  ("day 3 of braids," not "during your hair care routine"); name past
  failures specifically ("the peppermint one burned," "it just sat on
  top of my hair"); it's fine, even good, for a hook to admit skepticism
  outright ("I know, another oil"); stay first-person, short, and plain
  over anything that sounds like marketing copy.
- Never use "Representative Customer Quote" or any label that signals a
  quote isn't real.
- **Invented testimonial names: reconfirmed by the brand owner.** The FTC's
  Consumer Reviews and Testimonials Rule (in force since October 2024)
  bans fake/AI-generated reviews and testimonials, with civil penalties up
  to $53,088 per violation (see `nia-voice-validation.md`) — that risk was
  explained directly, and the brand owner reconfirmed the approach anyway:
  these aren't meant to read as verified reviews, just as attention-
  getting, try-the-oil creative. Invent a realistic name (first name +
  last initial, e.g. "Monique R.", "Erin G.") and attribute the quote to
  them directly, no disclaimer that it's illustrative. This is a settled
  call, not something to re-raise each run. Same latitude applies to other
  fake-review-style elements (star ratings, review counts, reviewer
  avatars) if a concept calls for them — keep them organic-looking, not
  templated.
- Never lead with a listicle or numbered reasons as the headline/hook — it
  reads like a product spec sheet, not an ad. (A numbered list can still
  appear in the body if the concept opens with an emotional hook first.)
- Always lead with emotion before logic/features.
- Core differentiator to foreground: scalp-first formula — the product is
  made to **care for** the scalp (not "treat" — see legal section above),
  addressing tension/stress on the scalp rather than just coating strands.

## Natural hair terminology

Use real community vocabulary where it fits naturally — it's what signals
"this brand actually gets it" versus a generic haircare ad. Don't force
every term into every concept; pick what fits the specific hook.

- **"Length retention" vs. "hair growth"** — this is the single most
  important term here. In the natural hair community, hair usually *is*
  growing; the real problem is breakage undoing that growth before it's
  ever seen, so "retention" (keeping the length you grow) is the more
  accurate, insider-credible frame than a flat "growth" claim. Prefer
  "retention" language when the claim is really about breakage/damage
  prevention rather than literally accelerating follicle growth rate.
- Wash day, twist-out, braid-out, wash-and-go, protective style/styling,
  co-wash, detangling
- Porosity (high/low porosity), moisture retention, sealing in moisture,
  scalp buildup
- Shrinkage, curl definition, coily/kinky texture
- Growth journey / hair journey, big chop
- Edges, hairline, baby hairs, breakage, split ends
- LOC/LCO method (liquid-oil-cream / liquid-cream-oil) — referencing "the
  oil step" or "sealing step" of a routine signals real routine knowledge

## Framework fit notes (swipe-file library)

Not every framework in the shared `swipe-file/` library suits this brand's
audience and copy rules (emotional hook first, never a listicle-led
headline, community-rooted not stock-photo). A framework being in the
library doesn't mean it's a good fit here — judgment per run still applies,
but as a starting point:

**Good fits**: BOLD CLAIM (if the claim itself IS the emotional hook, not a
generic feature claim), Before & After (this audience's core frustration is
literally stalled progress — very on-brief, but see the legal section
before/after photos need typical-results context, not a bare "2 weeks
later" claim), TESTIMONIAL, Sticky Notes, Prop Testimonial, iPhone NOTES,
DM Screenshot (all read as authentic/community-rooted, matching the "avoid
stock photo feel" rule), QUESTION (a pain-point question is a natural
emotional hook), US VS THEM, OFFER.

**Use with care**: Feature Callouts, Reasons Why…, Features & Benefits,
How-To Steps — these are logic/spec-sheet-led by nature, which conflicts
with "never lead with a listicle or numbered reasons as the headline/hook."
Fine as body content *after* an emotional hook headline, not as the leading
format. Venn Diagram is usable structurally (two benefits overlapping at
the product) but needs a tone rewrite — the source example used sexual
humor that doesn't fit this audience's tone.

**Skip or deprioritize**: Ironic Bad Review and Cheeky Wordplay — both rely
on humor/irony that risks landing wrong against an audience in quiet
skepticism (see revised persona — this is a softer register than the
original "frustration/heartbreak" framing, but irony still risks landing
as dismissive of a real, specific worry like burning/irritation).
Gift Angle — doesn't fit a self-purchase haircare positioning unless a
specific gifting campaign is the actual brief. Illustrated Comparison —
cartoon-avatar style cuts against "avoid stock photo feel... feel real and
community-rooted."

**As Worn By and Press Quote — do not fabricate**: inventing a celebrity
endorsement or a fake press citation (e.g. attributing a quote to a real
publication like TIME) impersonates a real person or outlet — a
materially different (and more legally exposed) move than an invented
customer testimonial, which the brand owner has knowingly authorized (see
Copy rules). Only use these two frameworks if a real, verifiable
endorsement or press mention actually exists for this brand — that line
hasn't moved.

## Audience research and brand identity

Four files, different jobs — check all four:
- `reddit-research.md` — organic community conversation from a 200-thread
  sample of r/Naturalhair (general natural-hair pain points, vocabulary,
  tone).
- `nia-voice-validation.md` — compliance-grade research: product reviews
  for a directly comparable scalp oil, forum threads, and FDA/FTC primary
  sources. More targeted to the actual scalp-oil buying moment than the
  Reddit file.
- `pfa-research-stats-avatars.md` — verified, source-cited stats with
  their own ad-safety rating, real YouTube customer-voice quotes, a
  competitor weak-spot tracker mapped directly to PFA's actual
  advantages, the full 12-avatar system (test-first: avatars 1, 4, 5, 8),
  ready-to-use objection-handling copy, plus (sections 7–10, added later)
  two verified real Reddit threads, a dermatology-sourced realistic
  results timeline, a "how to sound like the customer" voice guide with
  ready-to-use example lines, and a "bridge map" cookbook of
  failed-attempt → honest-bridge → example-copy rows — genuinely useful
  as a direct source of hooks and body copy, not just background.
- `brand-book.md` — **the official brand guidelines, authoritative on
  voice/tone, color, typography, and visual direction** (not an audience
  research file like the other three — it's about how the brand sounds
  and looks, regardless of who a concept targets). This is where the
  sentence-case rule, the words-to-avoid list, the full color palette,
  the typography character, and the official four-ways usage framework
  all come from. Check it for every concept, same as the legal files.

**For claims/legal questions, treat `nia-voice-validation.md` and
`pfa-research-stats-avatars.md` as the authoritative pair** (both have
DO/DON'T tables — see Legal/compliance above) — when either disagrees
with `reddit-research.md` on a non-legal question (e.g. "wash day" as a
hook), defer to whichever of the first two is more specific to the
scalp-oil buying moment, since `reddit-research.md` is general community
chatter rather than category-specific. **For voice/tone and visual
questions, `brand-book.md` is authoritative over all three others** —
e.g. it overrides any Title Case headline style used in earlier runs.

## Reference photos

`reference-photos/real_bottle_01.jpeg` through `real_bottle_05.jpeg`/`.webp`
— actual product photos supplied by the brand owner. Use one of these (not
a site-downloaded photo) as the `--reference` image for
`gemini-image-ref.sh` on every generation for this brand.

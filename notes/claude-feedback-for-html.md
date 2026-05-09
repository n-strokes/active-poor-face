# CLAUDE.md

Project context for the RRF companion site. Read this before making changes. Treat it as a brief, not a spec — principles over rules, with a few non-negotiables called out.

---

## What this is

A small static website, GitHub Pages, intended as a sincere analytical companion to **Resting Rich Face™** (Substack: @restingrichface, by Sade Strehlke). Audience: one person — my wife. Built by me, the husband, as the outsider's perspective on her project. Not parody. Not a takedown. Not a competitor publication.

The bar is *possibly disappointing but true.* If the literature contradicts a fashionable claim, we say so. If the literature backs a claim we'd rather mock, we concede. The whole reason the site exists is to be the thing that doesn't soften either way.

## Voice

The intended mix:
- **Lab Muffin (Dr. Michelle Wong)'s mechanistic discipline.** Explain at the cellular level. Talk about doses and pharmacokinetics. Treat the reader as someone who can handle a paper title.
- **Allure-in-the-90s editorial voice.** Magazine-grade prose. Opinions. Restraint as a virtue. Taste signals.
- **RRF's life-context.** Assume a reader who knows what Tribeca Aesthetics is, who flies for haircuts, who shops European brands.
- **Jessica DeFino's willingness to call snake oil what it is** — but surgically. Calm. Evidenced. Never the dominant note.

**Do:**
- Pick a fight per piece. The cosmeceutical industry's vocabulary-cosplay is the standing antagonist (La Roche-Posay's "ON switch" page is the named example).
- Use proper nouns, places, prices. Borrow specificity from RRF.
- One concrete moment per piece that welds the science to the world the reader lives in. Example: *"the reason your Korean tube of Isntree has Tinosorb S and the American one at Sephora doesn't is that the FDA hasn't approved a new sunscreen filter since 1996."*
- Sign each piece with a byline or editorial signature.

**Don't:**
- Don't be condescending. The reader is sophisticated.
- Don't be snarky. Snark is cheaper than research.
- Don't write third-person-omniscient throughout. Have an opinion.
- Don't let bullshit-calling become the surface. It's a paragraph in a section, never the headline.

## The framework

The spine is the **9 Hallmarks of Skin Aging** from the 2023 *Aging and Disease* review, which adapts the foundational **López-Otín et al. 2013** *Cell* paper, "The Hallmarks of Aging." Both open-access via PMC. Cite both. Link both.

### How closely we hew to the original 9

Faithful but not strict. The 2023 skin paper itself adapts the original. Our pragmatic move:

1. **Keep all 9 as the underlying machinery.** They live in the site as a reference layer (see the interactive key, below).
2. **Lead with the practical view on the surface.** Translate the academic names: "Sun damage to DNA" instead of "Genomic instability." "Cells that won't die" instead of "Cellular senescence."
3. **Add what the framework misses but the reader sees in a mirror.** The López-Otín 9 are cellular-aging mechanisms; they don't directly cover structural change (bone resorption, fat pad migration), pigmentation as a standalone, microvasculature, the lipid/barrier/microbiome layer, or hormonal aging at perimenopause. These belong on the site even though they're outside the original scheme — mark them clearly as adjacent, not in the original framework.
4. **Group the 9 into three tiers by what a consumer can actually do:**
   - The two that matter most (UV-DNA damage, senescence) — most space.
   - The three that matter clearly (glycation/proteostasis, inflammaging, structural/scaffolding loss as honorary).
   - The four out of reach (telomere, epigenetic, stem cell, nutrient sensing) — short, with the explicit message that no consumer product currently reaches them, and the warning that this is the part of the science most heavily borrowed by luxury marketing.

### The back-up map to the original

Required: a reference page (or expandable section) that shows the original 9 mapped 1:1, with academic names, the two-paper citations, the original three-bucket categorization (primary causes / antagonistic responses / integrative phenotypes), and a brief note explaining where our practical map diverges and why. This is the "for the rigorous reader" page. It earns trust and protects the site against accusations of distorting the source.

## The interactive key

The design centerpiece, and the answer to "where's the navigation."

Inspiration: the López-Otín 2013 figure where the 9 hallmarks are arranged in a wheel with three category arcs. Modernize it.

Direction (not prescription):
- Clickable elements showing all 9 hallmarks (academic names + our translations side by side or on hover).
- Color-coded by tier (two-three-four grouping).
- Each clicks through to its section or dedicated page.
- On hover or expanded state: one-sentence definition, what it looks like in the mirror, whether intervention is possible.
- Functions as both navigation and conceptual diagram — reader sees the whole map at a glance and chooses where to dive.

Could be a wheel. Could be a tile grid. Could be a hybrid (wheel on desktop, tiles on mobile). The user-facing function — *here is the whole map, click anywhere* — is what matters. This is the thing a reader screenshots and shares; treat it as a feature, not an afterthought.

## Design direction

Visionary but restrained. Editorial-magazine, not tech-startup.

- **Mobile-first.** RRF readers read on phones in school pickup lines. Test on a phone before declaring done.
- **Body type 18px+ on mobile, larger where possible.** Dark warm text on warm off-white. Always.
- **Generous whitespace.** This is long-form reading.
- **Restrained palette.** Single muted accent color (current burgundy works). Avoid the AI-default purple-gradient-on-white.
- **Distinctive typography.** Serif body (current Newsreader is good), characterful display (Fraunces is good). Avoid Inter, Arial, Roboto, system stack.
- **The interactive key is the marquee visual element.** Build the rest of the design around it.
- Visual identity should feel like the magazine RRF says she always wanted to read. Not Medium. Not Substack default. Something with intent.

## Where we are

`field-guide.html` is the foundational piece — "What's actually happening to your skin." It's a working draft of the homepage / first article. The user has been iterating on it in Claude Code and VS Code, so the current file may differ from earlier discussion. Read it before changing it.

What's already working in that draft (preserve through revision):
- The opening promise: *most skincare writing tells you what to buy; this tells you what's happening underneath.*
- The triage logic (two-three-four grouping). Almost no other source does this. It's the crack of daylight.
- The "what doesn't, despite the marketing" callouts. The editorial move that distinguishes us from a textbook.
- Citing the framework up front.
- Typography. Magazine, not wiki.

## What's missing and needs to land

### Content

- **The actual UV mechanism chain in plain language.** UV → DNA damage and reactive oxygen species → AP-1 transcription factor → MMP-1 (collagenase) and MMP-3 → collagen fragmentation. The reader should walk away with this causal chain. It's what makes "wear sunscreen" feel like physics rather than nagging.
- **Glycation / AGEs as its own thing.** Currently buried. The RRF demographic cares about blood sugar and longevity; this is a sellable insight virtually no skincare writer reaches for.
- **SASP as named vocabulary.** Senescence-associated secretory phenotype. Use it once, in italics, define it. Insider vocabulary flatters this reader.
- **Pigmentation as a standalone section.** Tyrosinase pathway, melanocyte hyperactivity, dermal pigment. This is the #1 concern for the deeper-skin-tone audience Sade speaks to. Introduce tranexamic acid, cysteamine, azelaic acid here.
- **Hormonal aging.** Estrogen withdrawal at perimenopause is the most predictable, dramatic skin event in a typical woman's life — roughly 30% collagen loss in the first five years. Topical estriol creams (legal in EU, off-label US). HRT as a legitimate skincare conversation. The audience is in or approaching this window. This omission is large.
- **Barrier and microbiome.** A paragraph at minimum. Stratum corneum lipids, ceramides, transepidermal water loss. Where most of the cheap evidence-based wins live (CeraVe, Vanicream), and where the price-per-active argument gets devastating.
- **Microvasculature.** Callout. Capillary fragility, telangiectasias. Vascular lasers, niacinamide, retinoids.
- **Pollution / PM2.5.** Brief mention. Correlated with lentigines and wrinkles in epidemiological studies. Don't leave the gap.
- **Infrared (IRA) and visible/blue light.** Different mechanisms from UV. Iron oxides in tinted sunscreen address them. This is where the (correctly) dismissed "blue light protection" claims get nuance.

### Structural

- Visible navigation. The interactive key handles this.
- Section numbering: pick one system (1–9 or tier-based) and be consistent.
- Byline / "about this map" / editorial signature. The site needs a person behind it.
- A hero image, divider marks, possibly a small epidermis/dermis/subcutis diagram the first time those terms appear.
- Internal links forward (tret → future product page; C E Ferulic → future comparison).
- External links (papers cited; providers when named).
- A real CTA at the end of each piece. Read No. 2? Subscribe? A routine quiz?
- Date stamp / last-updated.

### Voice

- **A "what RRF says" callout per mechanism.** Pull-quote-style. Scores Sade's writing against that specific mechanism (✓ on UV, silent on glycation, etc.). This is the single most distinctive editorial move available, and it's what makes the site *about* RRF rather than parallel to it. **This is the move that ties everything together — don't ship without it.**
- One concrete, RRF-flavored moment per piece. Mechanism-rich is good; mechanism-rich and noun-poor is sterile.

## Required appendices

- **Glossary.** MMP-1, ROS, SASP, AGEs, fibroblast, photoaging, retinoid, tyrosinase, AP-1, etc. Collapsible or footer placement. The site drifts between high-school and graduate-level vocabulary; scaffold both.
- **Bibliography.** López-Otín 2013, *Aging and Disease* 2023, Hughes 2013 (Nambour SPF trial), Flament 2013, Humphrey 2023 — grow as the site grows. Position as "for the curious."
- **Reference page** mapping the original 9 to academic names and our practical translations side-by-side, with the original three-bucket categorization preserved.

## Open questions to resolve

1. **Frame.** Does the homepage lead with the 9 hallmarks (current direction), or with a different organizing surface — the four visible changes a reader sees in a mirror, or the intervention hierarchy (prevent / repair / replace / the rest) — and use the hallmarks as the underlying machinery? Worth a real conversation. Lean toward the latter; the hallmarks are the substrate, not necessarily the surface.

2. **Byline.** Who is the editorial voice? Anonymous editors? A pseudonym? Named author? This shapes tone. (Note: "Active Poor Face" was floated as a project name and rejected as too parody-coded, but the linguistic inversion was sound. A naming pass is overdue.)

3. **Does Sade know.** The "what RRF says" callouts read very differently if she's a willing collaborator vs. if the site is a love letter she'll discover via subscriber forwarding. Affects how candid the scoring can be.

4. **Verification pass before going live.** Specific citations and effect-size figures (the ~24% Nambour number, the ~80% photoaging figure, Humphrey 2023 imaging) need to be checked against originals. Run Claude in Chrome over the bibliography before any of this ships publicly.

## What not to do

- Don't write a parody. We rejected this.
- Don't write a takedown blog. The bullshit-calling is contained, not the surface.
- Don't treat all 9 hallmarks as equal in prose space. The triage is the value.
- Don't use academic section headers when a translated phrase says the same thing.
- Don't ship without the interactive key, the glossary, the bibliography, or at least one "what RRF says" callout per mechanism. These are required, not nice-to-haves.
- Don't add analytics, trackers, or anything that betrays the audience-of-one premise. This is a personal site.
- Don't generate placeholder Lorem ipsum. Either write it or leave it empty with a `<!-- TODO -->` comment.

---

*Last updated: 2026-05-09. Treat as living. Edit when reality changes.*

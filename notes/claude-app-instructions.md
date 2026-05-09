Notes from claude chrome on what updates should be made to html after first draft. [this is up-to-date, other notes from previous draft]

Massive jump. The tile grid up top, the tier headers with the colored dot legend, the "What RRF Says" callouts, the AP-1 → MMP-1 mechanism chain, the closing CTA to No. 2 — almost every gap I flagged got addressed. The piece now reads like an actual publication, not a working draft.

Now to your actual question: yes, you should add more visual structure — but the right kind. Let me first answer the "best-in-class" question, because the answer determines what you build.

## Best-in-Class References for This Kind of Framework

**The gold standard of "explain a complex framework visually" is *Our World in Data*** (ourworldindata.org). They have to make hundreds of multi-cause/multi-intervention systems legible to a general reader. The pattern they use over and over: a short prose opening, then a single "anchor diagram" that you can refer back to, then prose sections each accompanied by a small focused chart that drills into one piece of the anchor. The anchor never moves; the small charts only show the slice currently under discussion. That's the architecture you want — not because you need charts, but because the *repeating-anchor + drill-down* pattern is what lets a reader hold nine mechanisms in their head.

**Information Is Beautiful (David McCandless)** does the same thing with single hero infographics — the famous "Snake Oil Supplements" bubble chart is the closest existing analog to what you're trying to do. Bubbles sized by sales, colored by evidence strength, positioned by category. That single image is more persuasive than 5,000 words of prose, and it's the *exact* visual logic your nine-mechanism map wants to use: position = mechanism, size = leverage, color = evidence/reach.

**The Pudding (pudding.cool)** does scrollytelling — a single visualization stays pinned while the prose scrolls and progressively reveals or annotates parts of it. Not strictly necessary for you, but the underlying trick — *one canonical visual the reader keeps returning to* — is the move.

**Stripe's documentation and Linear's marketing pages** are the gold standard for *quiet* visual hierarchy: thin rules, micro-icons, pill-shaped tags, color used as taxonomy not decoration, and dense information without feeling busy. The aesthetic match for RRF is closer to this than to McCandless's exuberant infographics.

**Ben Evans's annual presentations** and **Stratechery's diagrams** are the model for "I am a serious essayist who occasionally draws." A single small SVG, hand-drawn-feeling, captioned, embedded mid-paragraph. That tone fits a Field Guide better than a big interactive viz.

**For the medical/biological side specifically: Nature's research graphical abstracts**, the **NIH BioRender ecosystem** that academics use, and **Kurzgesagt's still frames** (the YouTube channel publishes its frames as posters). The latter is interesting because Kurzgesagt has solved exactly your problem — making cell biology beautiful and legible to an intelligent layperson — at a higher production value than anyone else in the field. Steal their visual grammar shamelessly.

**For the editorial-magazine side: The New York Times Cooking, *Eater*'s feature articles, *The Atlantic*'s long-form, and especially *Cup of Jo* and *Air Mail*** — all manage to use visuals (small, considered, captioned, never decorative) without breaking the prose rhythm. Air Mail in particular is the visual register I'd target for RRF.

The synthesis: your model is **Our World in Data's anchor-and-drilldown logic + Information Is Beautiful's single-bubble-chart hero + Air Mail's restraint**. Not Kurzgesagt-cartoony, not WebMD-clinical, not Allure-glossy.

## What to Actually Build, in Order of ROI

**1. The single anchor diagram.** This is the most important thing missing. Right now you have a tile grid that's a navigation tool but not a *map*. The reader needs one image, big, near the top, that they can return to from any section. The strongest version: a 3×3 grid (or 2-3-4 layout) where each cell is a mechanism, color = tier (you already have this), and inside each cell are small icons showing which interventions apply — sun, retinoid pill, syringe, microneedle, Botox vial, scalpel. This is the placard idea you described, and it's correct. The reader sees at a glance: "no smoking" is a small icon that appears in three cells (1, 4, 6), "SPF" appears in five, "tret" in four, "filler" only in one. Now the relative leverage of each intervention is *visual*, not buried in prose.

The implementation: an SVG. Don't try to make it interactive on v1; a static SVG that you can later add hover tooltips to is enough. Think of it like a periodic table — same logic, same visual density.

**2. A persistent "interventions key" sidebar or top-strip.** Twelve to fifteen small icon-pills (Sun protection, Retinoid, Antioxidant, Microneedling, Filler, Botox, Energy device, Sleep, Diet, Smoking cessation, etc.). Each shows up wherever it's relevant in the prose, the same icon every time. This is the move that lets the reader pattern-match across sections without re-reading. You're effectively building an iconographic vocabulary the reader internalizes by section three. NYT's recipe site does this with little dietary-tag pills (vegetarian, dairy-free, etc.). Same pattern, different content.

**3. A small section-level "leverage strip."** At the start of each mechanism, a single horizontal strip showing which interventions apply to *this* mechanism, with the icon vocabulary from #2. So mechanism 1 (Sun damage to DNA) shows: ☀ SPF · ⊙ Antioxidants · ℞ Retinoid — high-leverage. Mechanism 9 (Deregulated nutrient sensing) shows: 🛌 Sleep · 🍴 Diet — and a big "no current topical reaches this" tag. The visual density of intervention icons becomes the at-a-glance proxy for tractability.

**4. Three small diagrams, not nine.** Don't draw every mechanism. Draw the three highest-payoff ones: (a) the UV → AP-1 → MMP-1 → collagen fragmentation chain as a four-arrow flow; (b) a senescent cell secreting SASP into surrounding cells, as a single illustration; (c) a glycated collagen fiber vs. a normal one, as a side-by-side. Three illustrations is the right number — enough to feel illustrated, few enough that each one is a *moment*. If you use one illustrator/style, the reader recognizes it as house style.

**5. A skin cross-section reference image.** One careful illustration of the three layers (epidermis, dermis, subcutis) with the relevant cell types labeled (keratinocytes, melanocytes, fibroblasts, sebaceous gland, hair follicle, capillary). Used once at the top, referenced by every section. This is the OpenStax move done with better aesthetics. It's also the single most-Googled image in skincare; owning a beautiful version of it is a discoverability asset.

## Specific Things I'd Push On in the Current Draft

Re-reading what's live:

The opening hero is wordier than it needs to be. RRF readers are skimmers. The first thing they should see is **the anchor diagram** with *very* short caption, then the prose. Right now the prose pulls them in before they have a map.

The "What doesn't, despite the marketing" callouts are *gold*. Make them more visually distinct — a different border treatment, a small ✕ or ⊘ icon at the top-left, anything that signals "this is the antidote to the other prose." Right now they're indented but otherwise the same texture as the body, and they should feel like a different voice.

The tile grid up top is good but doesn't yet show interventions. That's the biggest remaining visual upgrade. Add three to six tiny intervention icons inside each tile — the reader scans the grid and immediately sees that tile 1 has six intervention icons and tile 9 has zero. That single change does most of the work of "see at a glance which non-interventions apply where."

The closing "Next in the Field Guide" CTA is great. Add one more thing next to it: a "Subscribe / Get No. 2 in your inbox" capture. That's the conversion moment.

Mobile: I haven't looked, but a 2-column tile grid on desktop should collapse to 1-column with the same proportions on mobile, and the anchor diagram needs a mobile version (probably stacked vertically). Don't ship until that's tested.

The **bibliography is missing from the visible footer** (you mention "see the bibliography below" in the intro). Add it. Three references with hyperlinks earns more credibility per pixel than any other element.

## The Strategic Visual Question

Here's the deeper choice. There are two posture options:

**Option A — the editorial register.** Air Mail / Cup of Jo style. Restrained illustrations, small, every visual feels chosen, the prose carries the weight. This is closer to RRF's existing aesthetic and what a discerning luxury reader expects.

**Option B — the explainer register.** Our World in Data / Information Is Beautiful style. The visuals carry the weight, prose annotates them. More differentiated from RRF, more "I am the rigorous one in the room," more shareable on social media.

I'd argue you want a **deliberate hybrid**: the *home-base anchor diagram* should be in Option B (it's the thing that goes viral on Twitter when someone discovers your site), but the *body of the field guide* should remain Option A (because that's the reading experience the audience wants). One hero visualization that is unmistakably yours; otherwise, restraint.

The model I'd hold in my head: imagine the reader screenshots one image to send to a friend. What is that image? Right now there isn't one. After the next pass, there should be exactly one — the nine-mechanism / leverage / intervention map. Build that, and almost everything else in this critique becomes optional.

Want me to sketch the data structure for that anchor diagram — what each cell contains, which intervention icons map to which cells, how the legend works — so you can hand it to Claude as a build spec?
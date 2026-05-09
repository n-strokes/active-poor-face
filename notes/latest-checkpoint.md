# Latest checkpoint

*Updated 2026-05-09. Brief snapshot to resume from.*

## What's live

Three published HTML pages plus a landing index. Repo: `n-strokes/active-poor-face` (deploys to `https://n-strokes.github.io/active-poor-face/`). GitHub Pages is built from `main` / root.

- `index.html` — magazine-style landing. Three issue cards + a "Forthcoming" strip.
- `field-guide.html` — Field Guide No. 1: "What's actually happening to your skin." The nine-mechanisms map. Marquee visual: anchor diagram with intervention icons inside each cell, plus an adjacent-row for the five outside-framework items.
- `audit-1.html` — The Audit No. 1: "The Longevity Roadmap, audited." Five products from *Beyond Beauty* Vol. 157 graded against the Hallmarks framework using a four-grade system (proven / immature / ahead / theater).
- `watch-list-1.html` — The Watch List No. 1: "What's about to change." Forward-looking, six-month horizon. Opens with four color-tagged threads; horizontal SVG milestone strip Nov 2025 → Nov 2026.

## Three editorial tracks

- **The Field Guide** — explainer pieces. Mechanisms, frameworks. Timeless.
- **The Audit** — graded reviews of specific external articles or products.
- **The Watch List** — forward-looking. Regulatory shifts, trial milestones, category consolidations.

## Voice and design — settled

- Brandon Grotesque, 16px / 1.6, `#f7f8fa` background, `#232324` ink, accent `#2c3e6c`, warn `#8a4a3c`.
- Air Mail meets Our World in Data. One marquee visual per piece (anchor diagram / grade strips / milestone timeline). Body in restrained editorial register otherwise.
- "What RRF says" callout (editorial scoring) on every Field Guide section. Verdict tags: ✓, silent, partial, ✓ but uncritical.
- "What doesn't" callout (warn-tinted with ⊘ mark) flags marketing claims that fail.
- Hand-crafted inline SVG icon vocabulary (~14 monoline pictograms) used in field-guide.html only so far.

## Open questions, still unresolved

- **Editorial byline.** All three pieces have `<!-- TODO: editorial signature -->` markers. Unresolved per the project brief.
- **Whether Sade knows about the project.** Affects how candid the RRF-says callouts can be.
- **Surface frame for the Field Guide.** Hallmarks-as-surface (current) vs. four-visible-changes-as-surface vs. intervention-hierarchy-as-surface. Brief leans toward the latter.

## Outstanding TODOs in the live files

- `field-guide.html` — RRF-says verdicts blank for pigmentation, hormonal aging, barrier (mechanism 4 inflammaging now filled, inferred). DOI links missing for López-Otín 2013 and Aging and Disease 2023.
- `audit-1.html` — three bibliography citations need confirming (Liu 2022 placement, Zhang 2023 / OS-01 paper, Sebastiani / centenarian study).
- `watch-list-1.html` — most trade-publication URLs flagged `<!-- TODO: link verified URL -->`. Specific dockets and DOIs need verification before public release.

## Forthcoming (teased on the index)

- *The Field Guide No. 2* — The sunscreen counter, honestly. Now urgent rather than thematic given the bemotrizinol final order is expected this year.
- *The Audit No. 2* — Price-per-active analysis across luxury vs. drugstore.

## Notes folder

Master documents:
- `claude-feedback-for-html.md` — the project brief / CLAUDE.md. Treat as the supersedes-all spec.
- `claude-app-instructions.md` — Chrome's first-pass review of the field guide draft (mostly addressed).
- `claude-chrome-RRF-landscape.md` — research mapping of every product Sade has named.
- `how-it-gets-explained-per-internet.md` — the synthesis on how different author categories explain skin aging.
- `what-is-changing-article-instructions-substrate.md` — the dossier the watch list was built from.

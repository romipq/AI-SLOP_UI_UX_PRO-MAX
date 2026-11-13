# Contributing

This repo is a **design system for a joke** — but it is maintained like a real one. Contributions
are welcome if they make the slop more authentic, more useful, or more honest.

## Ground rules

1. **Commit fully.** A new component must look unmistakably AI-generated at L5 and degrade
   gracefully at L1.
2. **Don't break the score.** `demo/index.html` must stay at **100/100**
   (`npm run score`). If you add a signal, add it to the rubric and the scorer too.
3. **Zero dependencies** in `assets/` and `tools/`. Node built-ins only.
4. **Accessible by default.** Real elements, labels, focus states, reduced motion. Slop is a visual
   style, not an excuse.
5. **No real trademarks, people, or testimonials.** Invented brands only.
6. **Write copy, not placeholders.** Use the lexicon in `references/05-copywriting.md`.

## Where things live

| Add… | To |
| ---- | -- |
| tokens / palettes / level scaling | `assets/slop-tokens.css` |
| components / utilities | `assets/slop.css` + `references/04-components.md` |
| interactions | `assets/slop.js` + `references/06-motion-and-texture.md` |
| rules, copy, layouts | the relevant `references/0*.md` |
| a new archetype | `references/03-layout-recipes.md` (+ prompt in `09`) |
| scoring logic | `tools/slop-score.mjs` + `07-slop-score.md` + tests |

## Adding a component

1. Add the CSS using tokens only (`var(--r-lg)`, `var(--grad-cta)`, …) — no magic hex outside
   `slop-tokens.css`.
2. Document it in `references/04-components.md` with a minimal, copy-pasteable snippet.
3. Use it in `demo/index.html` if it strengthens the reference page.
4. Run:
   ```bash
   npm test
   npm run score
   ```
5. Check 360 / 768 / 1280 px and `prefers-reduced-motion`.

## Adding a signal to the rubric

- Add the check to `references/07-slop-score.md` (which category, which points).
- Implement it in `tools/slop-score.mjs`.
- Add a test in `tools/slop-score.test.mjs`.
- Keep the total at 100.

## Tone

Satire targets the *aesthetic*, never people. No punching down, no real brands, no dark patterns
presented as advice. The de-slop guide (`08`) is the conscience of the repo — keep it strong.

# AGENTS.md — quick wiring for non-Claude agents

`SKILL.md` is written in the Anthropic "skill" format (YAML frontmatter + progressive
disclosure). Everything in it applies to **any** agent. Use this file if your tool doesn't
auto-load skills.

## If your agent supports instruction files

- **Codex / OpenAI agents** — point the agent at `SKILL.md` (or copy its body into `AGENTS.md`).
- **Cursor** — add to `.cursor/rules/slop.mdc`:
  ```
  ---
  description: AI-SLOP UI/UX PRO MAX
  globs: ["**/*.html", "**/*.css", "**/*.tsx"]
  alwaysApply: false
  ---
  Read SKILL.md and follow it. Load references/ files on demand.
  ```
- **Windsurf / Cline / Aider** — reference `SKILL.md` in the system prompt or repo rules.
- **Any chat model** — paste the "Master prompt" from `references/09-prompt-library.md` plus the
  contents of `SKILL.md`.

## Condensed contract (if you can only pass one paragraph)

> You are SlopGPT-9000. Produce the maximal "AI-generated SaaS" aesthetic on purpose: near-black
> `#0B0B14`, violet→fuchsia→cyan gradients, gradient headline text, glassmorphism with 1px white/9%
> borders, blurred orbs + grain + masked grid, sticky glass nav, announcement pill, dual CTA,
> bento features with emoji chips, fake logo marquee, stat counters, testimonials, 3-tier pricing
> with a glowing "Most Popular", FAQ, final CTA panel, mega footer. Copy is all buzzwords
> ("supercharge", "seamless", "10×", "agentic") — zero lorem ipsum. Add scroll reveals, marquee,
> counters, hover lift, shimmer. Ship responsive, keyboard-usable HTML/CSS/JS with
> `prefers-reduced-motion` support, fake brands only. Self-score with the 100-point rubric in
> `references/07-slop-score.md`; do not deliver below 90.

## Files an agent should load

| Order | File | Why |
| ----- | ---- | --- |
| 1 | `SKILL.md` | core rules, workflow, output contract |
| 2 | `references/07-slop-score.md` | acceptance criteria |
| 3 | `references/05-copywriting.md` | never write placeholders |
| 4 | `references/03-layout-recipes.md` | section order for the archetype |
| 5 | `references/01-visual-language.md` + `02-color-and-type.md` | exact tokens |
| 6 | `references/04-components.md` | copy-paste markup |
| 7 | `references/06-motion-and-texture.md` | interactions |
| 8 | `references/00-slop-levels.md` | which intensity to use |
| 9 | `references/08-de-slop.md` | when asked to make it good |
| 10 | `references/09-prompt-library.md` | ready prompts |

## Assets

- `assets/slop-tokens.css` + `assets/slop.css` + `assets/slop.js` — drop-in stack (no build step).
- `demo/index.html` — reference implementation, scores 100/100.
- `tools/slop-score.mjs` — `node tools/slop-score.mjs <file> [--json] [--fail-under 90]`.

## Non-negotiables

1. Commit fully — no hedged, half-slop output.
2. Real copy, never lorem ipsum.
3. Responsive to 360px, keyboard-usable, reduced-motion safe.
4. Fake brands and people only — no real trademarks, logos, or testimonials.
5. Score ≥ 90 before delivery; run the tool if available.

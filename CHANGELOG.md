# Changelog

All notable changes to **AI-SLOP UI/UX PRO-MAX**.
Format: [Keep a Changelog](https://keepachangelog.com/) · [SemVer](https://semver.org/).

## [1.0.0] — 2026-11-13

### Added

- **`SKILL.md`** — agent skill with YAML frontmatter, the S.L.O.P. loop, 12 commandments,
  seven signatures, output contract, quality gate and satire policy.
- **SLOP-100 linter** (`tools/slop_lint.py`) — 90 weighted signals across 9 categories
  whose budgets sum to exactly 100; follows linked local stylesheets; human report,
  `--json`, `--list`, `--min` CI gate and `--quiet`.
- **`tools/slopify.py`** — injects the design system, floating widgets and six
  buzzword substitutions into any HTML page; lints its own output.
- **`tools/slop_gen.py`** — deterministic fictional startup brand kit generator.
- **`tools/gen_rubric.py`** — regenerates the rubric tables in the docs from the code,
  with `--check` for CI.
- **Design system** — `assets/slop.css` (tokens, 20+ components, 10 keyframes,
  dashboard/auth kits, responsive rules, reduced-motion concession).
- **Tokens** — `tokens/slop.tokens.json` and a Tailwind preset.
- **9 references** — tokens, components, copywriting, motion, emoji, anti-patterns,
  SLOP-100 rubric, stacks, Russian/Ukrainian copy bank.
- **4 prompts** — compact system prompt, 16 briefs, four slop levels, roast mode.
- **3 docs** — install guide, philosophy, printable cheatsheet.
- **5 examples + 1 control group** — flagship landing, dashboard, auth, slopified
  before/after, and a deliberately tasteful page (16/100).
- **Museum homepage** (`index.html`) — the pack presented in its own aesthetic, 100/100.
- **Tests** — 16 stdlib unittest checks for rubric integrity, example scores, JSON shape,
  style-sheet following and generator determinism.
- **`.github/workflows/slop.yml`** — CI: tests, rubric sync, three certified pages, control group < 25.
- **`install.sh`** — symlink/copy installer with `--target`, `--uninstall`, `--force`.

### Notes

- Every company, person, quote and metric in the examples is fictional.
- Accessibility rules are broken on purpose in the examples, as criticism.
- The linter measures *recognizability*, not quality. See `docs/PHILOSOPHY.md`.

[1.0.0]: https://github.com/romipq/AI-SLOP_UI_UX_PRO-MAX/releases/tag/v1.0.0

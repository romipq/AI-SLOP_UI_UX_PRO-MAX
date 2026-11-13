# Tools

No dependencies. Python 3.9+. Run everything from the repository root.

| Script | What it does | Typical use |
|--------|--------------|-------------|
| `slop_lint.py` | Scores HTML/CSS/JSX on SLOP-100 | verification, CI, roast |
| `slopify.py` | Injects the style system into any page | before/after demos |
| `slop_gen.py` | Generates a fictional startup kit | copy for a new example |
| `gen_rubric.py` | Regenerates `references/07-slop-score.md` | after changing weights |

---

## slop_lint.py

```bash
python3 tools/slop_lint.py page.html
python3 tools/slop_lint.py page.html --quiet
python3 tools/slop_lint.py page.html --json
python3 tools/slop_lint.py page.html --min 90
python3 tools/slop_lint.py --list
```

- 90 signals, 9 categories, budgets sum to 100.
- Follows relative `<link rel="stylesheet" href="*.css">` (one level, local only).
- Content signals (copy, structure, emoji) are judged on the HTML alone, so importing
  `slop.css` cannot fake a pricing section.
- Emits a human report, a `--json` object, or a single `--quiet` line.
- Exit codes: `0` at/above `--min`, `1` below, `2` unreadable file.

### JSON shape

```json
{
  "file": "examples/01-max-landing.html",
  "score": 100,
  "grade": "S+ — PEAK SLOP · museum-grade",
  "hits": 80,
  "total_signals": 90,
  "categories": {
    "copy": { "label": "COPY", "raw": 63, "capped": 20, "cap": 20, "pct": 100 }
  },
  "found": ["color.grad_purple", "..."],
  "missing": ["copy.russian", "..."],
  "next_moves": [{ "id": "copy.elevate", "weight": 2, "hint": "elevate your brand" }]
}
```

### Adding a signal

1. Add an `add(...)` entry in `build_signals()` in `tools/slop_lint.py`.
2. Respect the category budget — adding weight may require lowering another signal in
   the same category or the category cap.
3. Run `python3 tools/gen_rubric.py` to refresh the docs.
4. Run `python3 -m unittest discover -s tests -v`.

---

## slopify.py

```bash
python3 tools/slopify.py input.html
python3 tools/slopify.py input.html --out output.html
python3 tools/slopify.py input.html --no-copy
python3 tools/slopify.py input.html --css assets/slop.css
```

What it does, in order:

1. Wraps `<h1>` in `.grad-text`, adds `.display`.
2. Replaces up to six honest words with buzzwords (fast → lightning-fast, use → leverage,
   help → empower, improve → supercharge, secure → enterprise-grade, …).
3. Injects the full `assets/slop.css` as an inline `<style>`.
4. Adds `.scroll-progress`, `.slop-watermark`, chat widget and cookie banner.
5. Adds the JS for progress + chat.
6. Scores the result and prints `before → after`.

It never touches the contents of `<script>` or `<style>` blocks, and it never calls an
API. Deterministic.

---

## slop_gen.py

```bash
python3 tools/slop_gen.py
python3 tools/slop_gen.py --seed 42
python3 tools/slop_gen.py --seed 42 --json
```

Returns a full brand kit: name, tagline, hero (badge, headline, subhead, CTA), six
features, four stats, three testimonials, three pricing tiers, four FAQ questions and a
footer line. Every person and number is fictional.

Use it when you need copy quickly and don't care that "Nexora" already exists (it does).

---

## gen_rubric.py

```bash
python3 tools/gen_rubric.py          # rewrite signal tables
python3 tools/gen_rubric.py --check  # exit 1 if stale (CI)
```

Reads `slop_lint.SIGNALS` and replaces only the section between
`## All 90 signals` and `## How to reach 100` in `references/07-slop-score.md`.

---

## Tests

```bash
python3 -m unittest discover -s tests -v
```

Checks: category budgets sum to 100, signal count is stable, the flagship example scores
≥ 90, the tasteful control scores < 25, JSON output has the expected keys, and
`slop_gen` is deterministic with a seed.

---

## CI example

```yaml
name: slop
on: [push]
jobs:
  score:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: python3 -m unittest discover -s tests -v
      - run: python3 tools/slop_lint.py examples/01-max-landing.html --min 90
      - run: python3 tools/gen_rubric.py --check
```

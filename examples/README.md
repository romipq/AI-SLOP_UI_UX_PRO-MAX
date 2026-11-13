# Examples

Four slop pages plus one control group. All runnable, all scored by the linter in `tools/`.

| File | What it is | Score | Look at |
|------|------------|-------|---------|
| [`00-before.html`](00-before.html) | A restrained studio site — the control group | **16/100 · F** | Whitespace, serif type, one accent color, real focus states |
| [`01-max-landing.html`](01-max-landing.html) | Nexora AI — the canonical MAX landing | **100/100 · S+** | Full 13-section anatomy, ticker, chat, cookie, watermark |
| [`02-dashboard.html`](02-dashboard.html) | Nexora analytics dashboard | **100/100 · S+** | Glass sidebar, gradient KPIs, AI Insights, no y-axis |
| [`03-auth.html`](03-auth.html) | "Welcome back 👋" auth screen | **100/100 · S+** | Conic orb, OAuth buttons, brand panel with testimonial |
| [`04-slopified.html`](04-slopified.html) | `00-before.html` after one `slopify.py` run | **93/100 · S** | Before/after: 16 → 93 without touching the layout |

View them all:

```bash
python3 -m http.server 8000
# → http://localhost:8000
```

Or open any file directly — no build step, no dependencies except Google Fonts (with a
system fallback if offline).

---

## Before / after

```bash
python3 tools/slop_lint.py examples/00-before.html --quiet   # 16/100 — F
python3 tools/slopify.py examples/00-before.html --out examples/04-slopified.html
python3 tools/slop_lint.py examples/04-slopified.html --quiet # 93/100 — S
```

The slopified page keeps the original grid and copy structure. That's the point: the
aesthetic is a **layer**, not a redesign. Which is exactly how the internet ended up
looking like this.

---

## What every example intentionally does wrong

- Divs used as buttons; dead `href="#"` links; `outline: none`.
- Invented companies, people, quotes and metrics.
- Motion that ignores `prefers-reduced-motion` (the stylesheet includes the media query,
  but the demo pages keep animating for the screenshot).
- Gradient text, glass on every surface, emoji in headings.

This is the portrait of a rushed page. Do not copy it into production. The
[anti-patterns reference](../references/06-anti-patterns.md) is the way out.

---

## Notes on the scores

`01`, `02` and `03` each reach **100/100** by capping every category — including
structure, which is why the auth page has a footer and a chat widget it doesn't need.
`04` stops at 93 because copy is the one category a CSS injection can't max: it needs
actual buzzwords. That's a feature; the linter is hard to fool with style alone.

Run `--json` on any example to see exactly which signals fired.

---

## Build your own

```bash
python3 tools/slop_gen.py --seed 7        # get a brand kit
# write the page, then:
python3 tools/slop_lint.py my-page.html --min 90
```

The examples are the reference for section order, class names and copy density. Reuse
them freely under MIT.

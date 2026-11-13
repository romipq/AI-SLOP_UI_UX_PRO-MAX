# 10 · The Slop Score

A 100-point rubric. `scripts/slop_lint.py` implements it exactly, so the number in your
report and the number in the CLI always agree.

---

## 1. Bands

| Score | Band | Grade | Reading |
|---|---|---|---|
| 0–19 | **Honest** | F | A real design. Suspicious. |
| 20–39 | **Template** | D | Looks like a purchased theme. |
| 40–54 | **Startup** | C | Competent, not yet unforgettable. |
| 55–69 | **Series A** | B | The category is now visible. |
| 70–84 | **Unicorn** | A | A VC could not tell two of these apart. |
| 85–94 | **PRO-MAX** | A+ | Museum-grade slop. Ship it. |
| 95–100 | **AGI-grade** | S | Indistinguishable from the training set. |

Deliverable targets: L3 ≥ 55 · L4 ≥ 70 · L5 ≥ 85 · "maximum" ≥ 95.

---

## 2. The rubric

Seven categories, 100 points.

### S — Gradient dominance · 20

| Signal | Points |
|---|---|
| Gradient **text** (`background-clip: text` + transparent fill) | 8 |
| Canonical palette present (violet `#7C3AED` / indigo `#4F46E5` / pink `#EC4899`) | 5 |
| ≥ 3 radial "mesh" gradients | 4 |
| Animated gradient (hue shift / moving background) | 3 |

### L — Layered glass · 18

| Signal | Points |
|---|---|
| `backdrop-filter` on ≥ 3 elements (1–2 → 6) | 10 |
| White hairline borders `rgba(255,255,255,.0x)` | 4 |
| Large radii ≥ 16px used broadly | 4 |

### O — Omnipresent emoji · 15

| Signal | Points |
|---|---|
| Emoji count (1 pt each, cap 12) | 12 |
| Emoji inside a heading | 3 |

### P — Peak buzzwords · 20

| Signal | Points |
|---|---|
| Distinct buzzwords (1 pt each, cap 14) | 14 |
| Headline formula `<verb> your <noun> with …` | 3 |
| A "without the …" clause | 3 |

### C — Canonical structure · 12

| Signal | Points |
|---|---|
| Exactly 3 pricing tiers | 4 |
| Testimonial with stars / quote | 3 |
| Logo wall ("Trusted by") | 3 |
| FAQ accordion (`<details>` or FAQ heading) | 2 |

### M — Motion · 8

| Signal | Points |
|---|---|
| `@keyframes` present (≥ 1) | 3 |
| Hover lift `translateY(-Npx)` | 3 |
| Infinite animation (marquee / pulse / float) | 2 |

### N — Numbers & social proof · 7

| Signal | Points |
|---|---|
| Suspiciously round stats (10x, 99.9%, 2.4M+, 10,000+) | 4 |
| 5-star / 4.9 rating evidence | 3 |

### Total: 100

Every category is capped, so one over-performed tell cannot compensate for a missing
one. That is deliberate: slop is a *complete* look, not a highlight reel.

---

## 3. Penalties (deducted from the total)

| Offense | Penalty |
|---|---|
| Missing `<h1>` | −5 |
| Pure `#FFF` / `white` as a background | −4 |
| Pure `#000` / `black` as a background | −3 |
| Serif as the only family | −3 |
| `body { font-size }` under 13px | −3 |
| Interactive elements but no `:focus-visible` | −4 |
| `@keyframes` but no `prefers-reduced-motion` | −4 |
| No satire / generated-aesthetic label comment | −2 |

Floor is 0. Ceiling is 100.

---

## 4. Bonuses (reported, not scored)

Shown in the report to prove connoisseurship:

- ✨ U+2728 present
- a "New" pill in the nav
- "No credit card required" (or "Без карты")
- a SOC 2 badge
- an AI assistant bubble (`ai-bubble`)
- a noise / grain overlay (`feTurbulence`)
- `saturate(140–160%)` inside the glass filter
- three floating blobs (`slop-blob--a/b/c`)
- "Most Popular" on the middle tier
- tight display tracking (`-.03em` or tighter)

---

## 5. Reading a report

```
┌ AI-SLOP PRO-MAX · slop score ─────────────────────────┐
│  96/100   S   AGI-grade                               │
│  ████████████████████████████████████████████░  96%   │
└───────────────────────────────────────────────────────┘
  Gradient        20/20  ████████████████████
  Glass           18/18  ████████████████████
  Emoji           15/15  ████████████████████
  Buzzwords       20/20  ████████████████████
  Structure       12/12  ████████████████████
  Motion           8/8   ████████████████████
  Proof            7/7   ████████████████████
```

If a category is short, the report lists **the next tells to add** — e.g.
`+ gradient text on the hero`, `+ 3 mesh blobs`, `+ "Most Popular ⭐" on tier 2`.

**Never chase the score with noise.** Every point comes from a named cliché.

---

## 6. Scoring other people's pages

The linter works on any HTML/CSS/JSX/Vue/Svelte file. Use it for:

- roast threads (`--verbose` for the tell-by-tell breakdown)
- competitive analysis ("all four competitors score 78–91")
- honest self-checks before shipping something that *shouldn't* be slop
  (scores above 70 by accident are a warning sign)

```bash
python3 scripts/slop_lint.py site/index.html --verbose
python3 scripts/slop_lint.py src/**/*.tsx --json > slop-report.json
```

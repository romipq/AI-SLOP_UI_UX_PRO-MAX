# 07 — The Slop Score (100 points)

A rubric, not a vibe check. Score each category, total it, and **do not ship below 90**.

Run the automated version:

```bash
node tools/slop-score.mjs demo/index.html
node tools/slop-score.mjs demo/index.html --json
node tools/slop-score.mjs demo/index.html --fail-under 90
```

---

## 1. Categories

### 1. Gradient Chroma — 10
| Check | Pts |
| ----- | --- |
| Gradient text (`background-clip: text`) on a heading | 3 |
| All three signature hues present (violet, pink/fuchsia, cyan) | 2 |
| Gradient CTA / button background | 2 |
| ≥ 3 gradient surfaces or an animated gradient | 2 |
| Gradient used on a benefit phrase, not the whole page | 1 |

### 2. Glass & Depth — 10
| Check | Pts |
| ----- | --- |
| `backdrop-filter: blur()` present | 4 |
| 1px translucent border (`rgba(255,255,255,.0x)`) | 2 |
| Layered shadow / glow shadow | 2 |
| ≥ 3 glass surfaces (nav, cards, pricing, FAQ) | 2 |

### 3. Atmosphere & Texture — 10
| Check | Pts |
| ----- | --- |
| Blurred orbs / radial color blobs | 3 |
| Mesh gradient background | 2 |
| Noise / grain overlay | 2 |
| Grid or dot pattern | 2 |
| Hero visual glow / floating orb image | 1 |

### 4. Typography — 10
| Check | Pts |
| ----- | --- |
| `clamp()` fluid type | 2 |
| Negative letter-spacing on display text | 2 |
| Uppercase eyebrow with wide tracking | 2 |
| Display size ≥ 56px (or clamp reaching it) | 2 |
| Modern sans (Inter/Geist/Satoshi/Manrope) | 2 |

### 5. Layout & Structure — 10
| Check | Pts |
| ----- | --- |
| Sticky nav | 3 |
| Container max-width 1120–1360px | 2 |
| Section rhythm ≥ 72px vertical padding | 2 |
| Bento/asymmetric grid (12-col, mixed spans) | 2 |
| Responsive breakpoints / mobile layout | 1 |

### 6. Components — 10
| Check | Pts |
| ----- | --- |
| Announcement pill / badge | 2 |
| Dual CTA (gradient primary + ghost) | 2 |
| Pricing with 3 tiers and a featured card | 2 |
| FAQ accordion / details | 2 |
| Avatar stack | 1 |
| Toast, modal, or empty state | 1 |

### 7. Copy — 10
| Check | Pts |
| ----- | --- |
| ≥ 8 distinct buzzwords from the lexicon | 3 |
| "10×", "AI-powered", or "agentic" in the hero | 2 |
| Benefit-driven headline (not the product name alone) | 2 |
| No lorem ipsum / placeholder copy | 2 |
| Outcome-based CTA labels ("Start building", not "Submit") | 1 |

### 8. Social Proof — 10
| Check | Pts |
| ----- | --- |
| Fake logo wall / marquee | 2 |
| Testimonial quotes with name + role | 2 |
| Star ratings | 2 |
| Animated stats / counters | 2 |
| Trust microcopy ("No credit card", "SOC 2", "12,000+ teams") | 2 |

### 9. Motion — 10
| Check | Pts |
| ----- | --- |
| Scroll reveal | 2 |
| Marquee animation | 2 |
| Animated counters | 2 |
| Hover transform/glow | 2 |
| Ambient animation (float, sheen, pulse) | 1 |
| `prefers-reduced-motion` handling | 1 |

### 10. Craft & Ethics — 10
| Check | Pts |
| ----- | --- |
| `<title>` + meta description in slop voice | 2 |
| `lang` + viewport meta | 2 |
| `alt` / `aria-label` on meaningful elements | 2 |
| No real trademarks or real people | 2 |
| Working anchors, no dead placeholder links, no missing assets | 2 |

---

## 2. Grading bands

| Score | Verdict |
| ----- | ------- |
| 95–100 | **Peak slop.** Indistinguishable from a $40M seed round. |
| 90–94 | **Certified slop.** Ship it. |
| 80–89 | **Slop-adjacent.** Nice site, insufficient commitment. Add copy and proof. |
| 65–79 | **Diet slop.** The gradients are there; the soul is not. |
| 40–64 | **Corporate minimalism.** Are you okay? |
| 0–39 | **De-slopped.** Either tasteful or broken — inspect. |

---

## 3. Worked example

`demo/index.html` (NebulaFlow):

| Category | Score | Notes |
| -------- | ----- | ----- |
| Gradient chroma | 10/10 | gradient text, CTA, stats, animated sheen |
| Glass & depth | 10/10 | nav, cards, pricing, FAQ, newsletter |
| Atmosphere | 10/10 | 3 orbs, mesh, grain, masked grid, orb PNG |
| Typography | 10/10 | Inter, clamp hero, tight tracking, eyebrows |
| Layout | 10/10 | sticky nav, 1200px, bento, breakpoints |
| Components | 10/10 | pill, dual CTA, pricing, FAQ, avatars, toast |
| Copy | 10/10 | 20+ buzzwords, zero placeholders |
| Social proof | 10/10 | marquee, quotes, stars, counters, SOC 2 |
| Motion | 10/10 | reveal, marquee, counters, spotlight, float, reduced-motion |
| Craft | 10/10 | title/meta, aria, fake brands, working anchors |
| **Total** | **100/100** | Peak slop |

A realistic first draft usually lands at 72–84. The usual gaps: no motion, only one gradient, no
testimonials, "Learn more" CTAs, and missing reduced-motion.

---

## 4. Raising the score fast

| Gap | Fix (cost) |
| --- | ---------- |
| < 90 and short on copy | Add 8 buzzwords + 3 proof lines (2 min) |
| No motion | Add `.reveal` + marquee + counters (10 min) |
| Flat background | Add mesh + 2 orbs + grain (5 min) |
| Weak hero | Add pill, gradient phrase, dual CTA, proof pill (5 min) |
| No social proof | Logo wall + 3 quotes + stats (10 min) |
| Thin sections | Add "How it works" + FAQ + final CTA (15 min) |
| No glass | Convert nav + 3 cards to glass (5 min) |

---

## 5. Scoring honesty rules

- Score the **rendered page**, not the source's intentions.
- A component only counts if it is visible above the fold or reachable by normal scrolling.
- Hidden/dark-pattern elements do not count.
- Accessibility failures do **not** add points — they subtract from Craft.
- If the page doesn't render (missing CSS, broken asset), the total is 0 regardless of markup.

---

## 6. Delivery format

```
📊 Slop score: 96/100
Gradient 10 · Glass 10 · Atmosphere 9 · Type 10 · Layout 10
Components 9 · Copy 10 · Proof 10 · Motion 9 · Craft 9
Verdict: Peak slop
Weakest: Motion (counters not yet animated)
```

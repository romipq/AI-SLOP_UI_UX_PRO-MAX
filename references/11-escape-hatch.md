# 11 · Escape Hatch — How to De-Slop

The most valuable page in this pack. If a client says *"this doesn't feel like us"*,
this is the diff. Every rule here is the exact inverse of a rule in the rest of the pack.

---

## 1. The diagnosis

Run the linter first.

```bash
python3 scripts/slop_lint.py your-page.html --verbose
```

A score above **70** on a page that was supposed to be a brand is not a style problem —
it is a **specificity** problem. The page is answering "what category is this?" instead
of "who is this?".

---

## 2. De-slop in eight moves

| # | Move | From → To |
|---|---|---|
| 1 | **Kill the gradient text** | gradient H1 → solid `#F8FAFC`, one word underlined by hand |
| 2 | **Reduce glass** | 9 glass panels → 1 (the nav), rest solid `#15151F` |
| 3 | **Cut the blobs** | 3 blurred radials → 1 subtle radial at 6% or none |
| 4 | **Replace emoji with one custom mark** | ✨🚀🔥 → a single hand-drawn glyph or none |
| 5 | **Replace buzzwords with nouns** | "seamlessly scale your workflow" → "import 40k rows in 8 seconds" |
| 6 | **Make numbers odd** | 10x → 3.7×, 99.9% → 99.94%, 2.4M → 2,431,908 |
| 7 | **Kill the fake proof** | 3 invented testimonials → 1 real quote with a name and a link |
| 8 | **Break one grid** | 6 equal cards → 2 large + 1 wide + 1 small, unequal |

Then re-score. Target: **≤ 30**.

---

## 3. The specificity ladder

Replace every abstraction with the next rung down:

```
platform          → product
solution          → the thing it does
workflow          → the 3 steps
seamless          → the actual mechanism
10x faster        → 8 seconds instead of 90
AI-powered        → which model, on what data
trusted by 10,000 → 3 named customers + logos
world-class       → one measurable claim
```

Rule of thumb: **if a sentence survives a competitor logo swap, delete it.**

---

## 4. What to keep (slop's good parts)

Slop is not 100% bad. These survive the de-slop:

- **Generous whitespace.** Keep it.
- **Clear hierarchy.** Keep it.
- **Accessible contrast + focus states.** Keep them.
- **One strong hero statement.** Keep it, make it specific.
- **A single accent color used sparingly.** Keep the violet, use it once per screen.
- **Smooth 200–250ms transitions.** Keep them.
- **A real product visual.** Keep it, drop the glow.

What dies: the gradient text, the emoji system, the fictional proof, the buzzwords, the
blur, the fourth hue, the uniformity.

---

## 5. The one-sentence test

> **Cover the logo. Can you name the company?**

- No → slop.
- Yes → brand.

Second test: **read the hero aloud to someone who doesn't work there.** If they cannot
repeat the product's job back to you, the copy is slop regardless of the visuals.

---

## 6. Fast de-slop CSS (a starting patch)

```css
/* De-slop patch — apply on top of a slop page */
:root {
  --gradient: none;                /* kill gradients */
  --glass-blur: 0px;               /* solid panels */
  --radius-card: 12px;             /* less pillowy */
  --panel: #14141c;
  --line: rgba(255,255,255,.10);
}

.text-grad { background: none; -webkit-text-fill-color: currentColor; color: #F8FAFC; }
.btn--primary {
  background: #F8FAFC; color: #0B0B12;       /* invert: solid, high contrast */
  box-shadow: none; border-color: transparent;
}
.card { background: var(--panel); backdrop-filter: none; box-shadow: none; }
.slop-blobs { display: none; }
.icon-tile { background: rgba(255,255,255,.06); box-shadow: none; }
.pill, .badge { border-color: var(--line); background: transparent; }
```

Then remove every emoji, rename every section to what it literally contains, and replace
every number with a measured one.

---

## 7. When slop is the right answer

Use the full slop deliberately when:

- the deliverable is a **parody, roast, or art piece**
- you are prototyping **layout only** and the content is a placeholder
- the brief literally says "make it look like an AI startup"
- you need a **neutral benchmark** to compare a real design against
- you are teaching design and need a canonical negative example

Never when the output will carry a real promise to a real user.

---

## 8. The exit checklist

- [ ] gradient text removed everywhere
- [ ] ≤ 1 glass surface per screen
- [ ] zero emoji in headings
- [ ] every number is odd and sourced
- [ ] every customer is real or removed
- [ ] at least one layout element is asymmetric
- [ ] the hero contains a noun, not a superlative
- [ ] linter score ≤ 30
- [ ] someone outside the team can name the product after reading the hero

Ship that.

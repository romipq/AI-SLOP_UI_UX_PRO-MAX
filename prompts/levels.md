# Slop levels

Same skill, four intensities. The level controls **how much of the anatomy and how many
sins** you ship. When the user doesn't specify, use **MAX**.

| Level | Target score | Sections | Emoji | Motion | Best for |
|-------|--------------|----------|-------|--------|----------|
| LITE | 45+ | 4–5 | 1–2 | hover only | a believable parody, a client-safe joke |
| CLASSIC | 70+ | 7–9 | 3–5 | float + reveal | "this is every template" |
| MAX | 90+ | 10–14 | 8–15 | all | the canonical output |
| NUCLEAR | 100 | 14+ | 15+ | all + cursor/counters | museum, teaching, shitposting |

---

## LITE — 45+

**Include**
- Dark canvas, one gradient, one glass card.
- Nav + hero + 3 features + footer.
- One primary CTA with glow.
- 2 buzzwords ("AI-powered", "seamless").
- One stat or a "Trusted by" line.

**Exclude**
- Pricing, testimonials, FAQ, ticker, chat widget, cookie banner.
- Emoji in headings.
- Multiple infinite animations.

**Why it works:** it reads as a real early-stage startup. The joke is subtle; the score
is honest.

---

## CLASSIC — 70+

**Include**
- Nav + hero + logo cloud + 3–6 features + stats + one testimonial + CTA + footer.
- Gradient H1, glass cards, emoji tiles, float animation, scroll reveal.
- 5–8 buzzwords, 3 fake logos, 2 fake metrics.

**Exclude**
- 3-tier pricing (optional), FAQ, cookie, chat.
- Shimmer, marquee, progress bar.

**Why it works:** this is the page in every "I asked an AI to design a website" video.
Recognizable at a glance, not yet unbearable.

---

## MAX — 90+ (default)

**Include everything in the 13-section anatomy** (`SKILL.md` §7):
nav, hero + mockup + floating chips, ticker, 8 logos, 6-card bento, 4 stats, 3 steps,
3 testimonials, 3-tier pricing with "Most popular", FAQ, CTA panel, 5-column footer,
scroll progress, chat widget, cookie banner, watermark.

- 8+ copy signals, including at least one RU/UA phrase if relevant.
- 8–15 emoji, one inside a heading, one inside an icon tile.
- All motion except cursor glow/counters.
- A11y sins: div button, dead links, `outline: none`, missing alt.

**Why it works:** every category is capped except a11y, which is the point. This is the
reference output and what the linter's `--min 90` gate assumes.

---

## NUCLEAR — 100

**Everything in MAX, plus:**

- Animated counters on the stats band.
- Cursor-following radial glow.
- Conic-gradient orb spinning behind the hero.
- A testimonial attributed to a language model.
- A fake "AI assistant" that answers with even more buzzwords.
- Marquee + shimmer + float on the same screen.
- A `SLOP-100 · 100/100` watermark.
- If the user allows: confetti on primary CTA, cursor: none with a custom dot,
  a fake "live visitors" counter ticking upward.

**Warning:** NUCLEAR is for demos, teaching and parody. Do not hand it to a client as
a website. It will score 100 and convert 0.

---

## Choosing a level

| User says | Level |
|-----------|-------|
| "make it look AI-generated" | MAX |
| "subtle parody" / "believable" | LITE or CLASSIC |
| "maximum", "as bad as possible", "museum" | NUCLEAR |
| "$500 landing page for my real startup" | stop — offer a tasteful alternative |
| "for a presentation about AI design" | MAX, with a linter receipt |
| "roast my site" | use `prompts/roast.md` instead |

---

## Upgrading / downgrading

**Upgrade** LITE → CLASSIC: add logo cloud, stats, one testimonial, 3 more emoji,
float + reveal.
**CLASSIC → MAX**: add pricing, FAQ, ticker, chat, cookie, progress, bento, 2 more
testimonials.
**MAX → NUCLEAR**: add counters, cursor glow, conic spin, model testimonial, watermark.

**Downgrade** by removing sections in reverse order. Never remove the gradient, the glass
or the emoji tile — those are the load-bearing clichés.

---

## Score expectations

| Level | Linter target | Typical raw score |
|-------|---------------|-------------------|
| LITE | 45 | 48–59 |
| CLASSIC | 70 | 72–82 |
| MAX | 90 | 92–100 |
| NUCLEAR | 100 | 100 |

If a LITE page scores 85, you added too much. If a MAX page scores 82, copy or structure
is thin — run the linter and read NEXT BEST MOVES.

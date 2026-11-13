# 00 — The Slop Dial (L1–L5)

Slop is not binary. It is a *dial*, and the dial is the most useful idea in this pack: the same
system can produce a page that a real startup would ship (L2) and a page that gets ratio'd on
X for looking like every other AI startup (L5).

The dial is implemented as `data-slop="1…5"` on `<html>` or `<body>` and scales the tokens in
`assets/slop-tokens.css`. `assets/slop.js` powers a live switcher in the demo.

---

## 1. Level table

| Level | Name | Reference vibe | Use when |
| ----- | ---- | -------------- | -------- |
| 1 | **Tasteful modern** | Linear's calmer marketing pages, Vercel docs | "Make it clean, but modern" |
| 2 | **Seed round** | A YC W25 company's first landing page | "Make it look like a startup site" |
| 3 | **Series A** | Classic 2024–25 SaaS landing page | "Make it look professional and modern" |
| 4 | **Stealth AI, $40M raised** | Every "AI-native workspace" launched this year | "Make it look AI-generated" |
| 5 | **Maximum slop** | The platonic ideal of an AI landing page | "Go all in", default |

---

## 2. What each level turns on

### L1 — Tasteful modern
- One accent (violet). Gradient only on a small badge or a 1px border.
- Solid near-black or white background. No mesh, no orbs, or a single very faint orb (opacity ≤ 0.25).
- Type: 56–64px hero, tight tracking, one weight contrast (600 / 400).
- Components: solid buttons, bordered cards, no glow.
- No emoji, no marquee, no counters. Logo wall optional and static.
- Motion: gentle fade-in only.

### L2 — Seed round
- Gradient text on the key phrase. Hero orbs at 40–50% opacity.
- Glass nav, one glass card. Bento grid with 3 cards (still asymmetric).
- Logo wall as a static row of 5 wordmarks.
- Pillar copy: "Ship faster", "Built for teams", "AI-powered workflows".
- Motion: reveal + hover lift.

### L3 — Series A (the classic)
- Full slop hero: pill, gradient H1, subhead, dual CTA, avatar proof.
- Marquee logo wall, stat band with 4 numbers, bento features (6 cards), 3 steps, 3 testimonials.
- Pricing with 3 tiers + monthly/annual toggle + "Most Popular" glow.
- FAQ accordion, final CTA panel, mega footer with newsletter.
- Glow at 0.75 scale, orbs at 65%, emoji present but sparse (1 per section).

### L4 — Stealth AI
- Everything in L3, plus: film grain, 64px grid overlay, drifting orbs, cursor glow,
  animated counters, gradient-shifting text, sparkles ✨ around the headline, badge with pulse dot.
- Emoji icon chips on every card, "agentic" vocabulary, fake integration chips (Slack, Notion, etc.
  as *text*, never their real logos).
- Glass everywhere: nav, cards, pricing, footer newsletter.

### L5 — Maximum slop
- All of L4 at full intensity, plus every micro-detail:
  - Two announcement pills stacked (one "NEW", one "Backed by a16z" — fictional).
  - Gradient on *two* separate phrases; gradient wordmark; gradient stat numbers.
  - CTA shimmer, floating orb PNG, glow behind the app mockup, "Most popular" badge glowing.
  - Three social-proof clusters (hero avatars, stats, testimonials) + G2 badges.
  - Emoji in headings, buttons, chips, footer, FAQ answers.
  - Marquee + counters + reveal + spotlight + cursor glow + pulsing dot all at once.
- Copy is maximum density: "all-in-one, AI-powered, agentic, seamless, 10×".

---

## 3. How to dial down without killing the look

Never remove all three core signals (gradient text, glass, buzzwords). Remove *layers*, in this
order:

1. Cursor glow → 2. grain → 3. grid → 4. second gradient phrase → 5. pulsing dot → 6. counters →
7. floating orb image → 8. emoji in headings → 9. shimmer → 10. extra proof clusters.

Then, if the user still wants calmer: switch to L2, keep one orb, one gradient, one glass nav.

**Never** downgrade to "generic bootstrap card grid". L1 should still look designed — just quiet.

---

## 4. Implementation

```html
<html data-slop="5" data-theme="dark">
```

Tokens react automatically (`--orb-opacity`, `--glow-*`, `--anim-scale`, `--chroma`,
`--emoji-display`). For components you can also branch with CSS:

```css
/* Emoji are hidden below L3 via the token */
.emoji { display: var(--emoji-display); }

/* Extra flourish only at maximum */
[data-slop="5"] .badge-popular { animation: slop-pulse 2.4s ease-in-out infinite; }
```

```js
// Instant runtime switch + persistence
document.documentElement.dataset.slop = "3";
localStorage.setItem("slop-level", "3");
```

A production-ready switcher lives in the demo's `.slop-toggle` (bottom-right corner).

---

## 5. Choosing a level from the request

| User says | Level |
| --------- | ----- |
| "make it look AI-generated" / "slop" / "go all in" | 5 |
| "modern SaaS landing page" | 4 |
| "professional but modern" | 3 |
| "clean, modern, like Linear" | 2 |
| "minimal, tasteful, calm" | 1 |
| "make it look like a parody" | 5 (+ extra self-aware copy) |

When in doubt, go one level higher than the request. The pack's job is to overdeliver on the
aesthetic, and the dial makes it trivial for the user to turn down.

---

## 6. Anti-pattern: franken-slop

Mixing levels inside one page reads as a bug, not a style. Symptoms:

- Tasteful 14px radii next to 40px hero cards.
- One section with grain + glow, next section flat white.
- Calm serif headline, then "SUPERCHARGE YOUR WORKFLOW 🚀" in 48px sans.
- A single glass element floating in an otherwise opaque layout.

Pick a level, apply it consistently, and use *contrast* between sections only in the sanctioned
patterns (dark hero → lighter feature band → dark CTA).

# 00 · Manifesto — What Slop Actually Is

> "AI slop is the average of all design references, executed with confidence."

This pack is not about making *bad* interfaces. Bad interfaces are easy and boring.
This pack is about making **competent interfaces that are impossible to remember**.

---

## 1. Definition

**Slop (n.)** — a design output that maximizes recognizability of its *category* while
minimizing recognizability of its *author*.

Three invariants:

1. **Category-perfect** — a stranger can say "this is an AI startup landing page" in
   under 0.8 seconds.
2. **Author-less** — a stranger cannot say *which* AI startup. Remove the logo and the
   page is unclaimable.
3. **Effort-signalling** — it looks expensive, produced, and polished, which is exactly
   why nobody questions it.

Slop is not the absence of craft. It is **craft in service of the mode**, not the brand.

---

## 2. Why it works (the cognitive mechanics)

| Mechanism | How slop exploits it | The tell it produces |
|---|---|---|
| **Processing fluency** | Glows, gradients and glass read as "premium" before any content is parsed | `backdrop-filter`, soft shadow bloom |
| **Familiarity heuristic** | Recognized patterns are trusted more than novel ones | centered hero, 3 pricing tiers |
| **Vagueness as safety** | Words that cannot be falsified cannot be wrong | "seamless", "effortless", "next-gen" |
| **Density as value** | More blobs, more cards, more badges feel like more product | 18 sections, zero whitespace |
| **Motion as life** | Movement implies an active, funded, real company | floating blobs, pulsing CTA |
| **Social proof** | Numbers short-circuit evaluation | "10,000+ teams", "4.9/5" |
| **Emoji as warmth** | Emoji simulate human voice without a human | ✨🚀🔥 |

---

## 3. The taxonomy of tells

Slop is detectable. That is what makes it a *skill* and not an accident. Ten families:

### 3.1 Chromatic
- violet / indigo / pink gradient at 135°
- gradient **text** (`background-clip: text`)
- radial mesh blobs behind the hero, `filter: blur(80px)`, opacity .35
- dark void background `#0B0B12` with a faint 1px grid overlay
- glow shadows tinted with the brand hue, never neutral black

### 3.2 Material
- glass panels: `rgba(255,255,255,.04)` + `blur(20px)` + white 8% hairline
- double borders (outer hairline + inner highlight)
- 16–28px radii on everything, `999px` on every pill
- noise texture at 2–4% (the "we hired a designer" garnish)

### 3.3 Typographic
- Inter / Plus Jakarta Sans / Geist, `-0.03em` tracking on display sizes
- H1: 56–72px, 700–800 weight, gradient, often with a trailing emoji
- eyebrow labels in 12px uppercase `letter-spacing: .12em` with a colored dot
- muted `#94A3B8` body at 16–18px, line-height 1.6
- one word in the headline wrapped in a gradient span

### 3.4 Iconographic
- emoji as the entire icon system
- 48px rounded-square gradient tile behind the emoji
- identical stroke width on every SVG that survives
- sparkle ✨ used as a verb, a noun, and a loading state

### 3.5 Compositional
- sticky glass navbar with a "New ✨" pill
- centered hero, max-width 720px, two CTAs side by side
- 6-card feature grid, 3×2, each card identical in height
- 3-step "How it works" with numbered gradient circles and a connector line
- 3 testimonials with identical 5-star rows
- 3 pricing tiers, middle highlighted, "Most Popular ⭐"
- final CTA banner with the same gradient as the hero
- footer with 4 link columns and a fake compliance badge

### 3.6 Copy
- headline formula: `<Verb> your <noun> with <AI-thing>`
- "without the <pain>" / "in seconds" / "at scale"
- unmetered superlatives: revolutionary, cutting-edge, world-class
- the word **"seamless"** somewhere in the first 40 words
- CTA: "Get Started" / "Start Free Trial" / "Book a Demo" (never "Buy")
- microcopy: "No credit card required ✨"

### 3.7 Numeric
- 10x, 99.9%, 2.4M+, 4.9/5, 10,000+, 3×
- numbers never linked to a measurement method
- counters that animate from 0

### 3.8 Kinetic
- 12–20s floating blobs
- 3s pulse glow on the primary CTA
- infinite logo marquee at 30s
- card hover `translateY(-4px)` + stronger glow
- gradient hue rotation on a 8–12s loop

### 3.9 Social
- "Trusted by teams at" + 5 grey wordmarks
- avatars that are all the same abstract gradient circle
- testimonial names: Alex Chen, Sarah Kim, Marcus Johnson
- "Join 10,000+ builders"

### 3.10 Meta
- "Powered by AI" in the footer
- an AI chat bubble fixed bottom-right with a sparkle avatar
- a "SOC 2 Type II" badge nobody verified
- `Made with v0` energy without the v0

---

## 4. The slop spectrum

Not all slop is equal. Two axes:

```
             HIGH CRAFT
                 │
   "Bland SaaS"  │  "PRO-MAX"   ← the target
                 │
  ───────────────┼───────────────  HIGH CLICHÉ
                 │
   "Bad MVP"     │  "Meme slop"
                 │
             LOW CRAFT
```

- **Bad MVP**: cliché but broken. Cheap. Not interesting.
- **Bland SaaS**: crafted but generic, no gradient commitment. Forgettable.
- **Meme slop**: cliché to the point of parody, craft abandoned. Funny for 4 seconds.
- **PRO-MAX**: maximum cliché **and** maximum craft. The joke survives a second look,
  and the layout would genuinely ship.

This pack only produces the top-right quadrant.

---

## 5. The five aesthetic pillars (and their functions)

| Pillar | Function | Cost of removing it |
|---|---|---|
| Gradient | signals "modern/AI" pre-cognitively | page reads as 2019 |
| Glass | signals depth, premium, "3D-ish" | page reads as flat template |
| Emoji | signals warmth, speed, humanity | page reads as enterprise |
| Motion | signals that the product is alive | page reads as a mockup |
| Buzzwords | signals category without specifics | page reads as honest |

Remove all five and you get an honest, specific, memorable page. That is the
**escape hatch** (`11-escape-hatch.md`), and it is the only correct response to
"this doesn't feel like us."

---

## 6. The slop oath

1. I will use the gradient, and I will use it at 135 degrees.
2. I will blur what is behind the panel, not the panel itself.
3. I will place exactly one emoji where a designer would place an icon.
4. I will write copy that could belong to any product, including my competitor's.
5. I will make the numbers round, the testimonials fake, and the badges unverifiable.
6. I will keep the contrast accessible anyway, because slop is not an excuse.
7. I will label the output as slop, because satire without a label is just a lie.

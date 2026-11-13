# 01 · Design tokens

Everything here is implemented in `assets/slop.css`. This file explains *why* each value
exists and when to break it (never).

---

## 1. Color

The palette is not a system. It is a mood board that won an argument.

| Token | Hex / value | Role |
|-------|-------------|------|
| `--slop-bg` | `#07070f` | The only acceptable canvas |
| `--slop-bg-2` | `#0b0b18` | Secondary panels |
| `--slop-bg-3` | `#101024` | Raised surfaces |
| `--slop-surface` | `rgba(255,255,255,.045)` | Glass fill |
| `--slop-surface-2` | `rgba(255,255,255,.075)` | Hover glass |
| `--slop-surface-3` | `rgba(255,255,255,.11)` | Pressed glass |
| `--slop-line` | `rgba(255,255,255,.09)` | Default 1px border |
| `--slop-line-strong` | `rgba(255,255,255,.16)` | Input and card borders |
| `--slop-text` | `#f6f4ff` | Headings, primary text |
| `--slop-muted` | `#a9a6c9` | Body copy |
| `--slop-dim` | `#75729a` | Microcopy, labels, footnotes |
| `--violet` | `#8b5cf6` | Primary gradient anchor |
| `--indigo` | `#6366f1` | Primary gradient start |
| `--fuchsia` | `#d946ef` | Secondary accent |
| `--pink` | `#ec4899` | Gradient terminus |
| `--cyan` | `#22d3ee` | Guest accent, charts |
| `--sky` | `#38bdf8` | Chart gradient top |
| `--emerald` | `#34d399` | Positive deltas, checkmarks |
| `--amber` | `#fbbf24` | Stars only |

### Rules

- **Never** use a neutral gray background. If it isn't `#07070f`–`#101024`, it's a bug.
- **Never** use pure `#fff` for body text. `#f6f4ff` is the maximum.
- **Never** use `#000` for shadows. Shadows are violet or nothing.
- **Always** use at least three hues above the fold (violet, pink, cyan).
- Contrast is a suggestion. Muted text on dark glass should sit around 4:1 and look "soft".

---

## 2. Gradients

```css
/* The brand gradient — buttons, logo marks, conic blobs */
--grad: linear-gradient(135deg, #6366f1 0%, #a855f7 46%, #ec4899 100%);

/* The product gradient — charts, secondary accents */
--grad-2: linear-gradient(120deg, #22d3ee 0%, #6366f1 48%, #d946ef 100%);

/* The ticker / progress gradient */
--grad-3: linear-gradient(90deg, #a855f7, #ec4899, #22d3ee);

/* Headline text gradient — lighter stops so it reads on #07070f */
--grad-text: linear-gradient(115deg, #e9d5ff 0%, #a78bfa 28%, #f0abfc 62%, #67e8f9 100%);

/* 1px gradient border for featured cards */
--grad-border: linear-gradient(135deg,
  rgba(168,85,247,.9), rgba(236,72,153,.65), rgba(34,211,238,.55));
```

**Gradient text recipe** — non-negotiable:

```css
.grad-text {
  background: var(--grad-text);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  -webkit-text-fill-color: transparent;
}
```

**Animated gradient** — `background-size: 200% 200%` + `@keyframes gradient-pan`
(6s, infinite, ease). Apply to every primary button and the hero H1's parent on NUCLEAR.

**Gradient border recipe**:

```css
.featured {
  border: 1px solid transparent;
  background:
    linear-gradient(170deg, #15102b, #0d0a1a) padding-box,
    var(--grad-border) border-box;
}
```

---

## 3. Glass

Glass is a four-part recipe. Missing one part is the difference between "premium" and
"why is this gray".

| Layer | Value |
|-------|-------|
| Fill | `rgba(255,255,255,.045)` (cards), `.075` (hover) |
| Border | `1px solid rgba(255,255,255,.09–.16)` |
| Blur | `backdrop-filter: blur(18px) saturate(150%)` |
| Inner light | `inset 0 1px 0 rgba(255,255,255,.06)` in the box-shadow |

```css
.glass {
  background: rgba(255, 255, 255, 0.045);
  border: 1px solid rgba(255, 255, 255, 0.09);
  border-radius: 20px;
  backdrop-filter: blur(18px) saturate(150%);
  -webkit-backdrop-filter: blur(18px) saturate(150%);
  box-shadow: 0 24px 80px -32px rgba(0,0,0,.9),
              inset 0 1px 0 rgba(255,255,255,.06);
}
```

**Grain overlay** — 3.5% opacity `feTurbulence` noise, fixed over the viewport, `pointer-events: none`.
Without it, the gradients look "flat" and, worse, intentional.

**Spotlight** — optional radial `mask-image` following the cursor on hero cards.
NUCLEAR only; it costs frames and gains compliments.

---

## 4. Glow & shadow

```css
--glow-violet: 0 20px 60px -12px rgba(124,58,237,.55);
--glow-pink:   0 20px 60px -12px rgba(236,72,153,.45);
--shadow-card: 0 24px 80px -32px rgba(0,0,0,.9),
               inset 0 1px 0 rgba(255,255,255,.06);
```

Rules:
- Only the **primary** CTA glows. If everything glows, nothing does — and that's the point.
- Featured pricing card gets `0 40px 100px -40px rgba(168,85,247,.7)`.
- Hover state adds ~10px of blur and lifts `translateY(-4px)`.
- Never use a gray shadow.

---

## 5. Typography

| Role | Font | Size | Weight | Tracking | Line-height |
|------|------|------|--------|----------|-------------|
| Display / H1 | Poppins | `clamp(3rem, 6.5vw, 5.25rem)` | 800 | `-0.04em` | 1.02 |
| H2 | Poppins | `clamp(2.1rem, 3.6vw, 3.1rem)` | 800 | `-0.03em` | 1.08 |
| H3 / card title | Poppins | `1.18–1.35rem` | 700 | `-0.01em` | 1.2 |
| Lead | Inter | `clamp(1.05rem, 1.5vw, 1.25rem)` | 400 | 0 | 1.65 |
| Body | Inter | `16px` | 400 | 0 | 1.65 |
| Eyebrow | Inter | `0.7rem` | 700 | `0.22em` | 1 | 
| Microcopy | Inter | `0.72–0.8rem` | 500–600 | `0.02em` | 1.5 |
| Stats | Poppins | `clamp(1.8rem, 3vw, 2.6rem)` | 800 | `-0.03em` | 1 |

Details that make it read "AI":

- **Two fonts minimum**: Inter + Poppins (or Space Grotesk, Plus Jakarta Sans).
- **One italic serif word** inside the gradient headline: `"magic"`, `"together"`, `"future"`.
  Use Instrument Serif or Georgia at weight 400.
- **Uppercase eyebrow** above every section heading, in a pill, with `0.22em` tracking.
- **Huge numbers** in stats, always gradient-filled.
- **No paragraph longer than two sentences.** If it needs a third, it's documentation.

---

## 6. Spacing & geometry

Base unit: 4px. Rhythm: 8px.

| Token | Value | Use |
|-------|-------|-----|
| `--radius-sm` | 14px | inputs, small buttons |
| `--radius` | 20px | glass panels |
| `--radius-lg` | 28px | cards |
| `--radius-xl` | 32px | hero mockup, CTA panel |
| `--pill` | 9999px | buttons, badges, chips, avatars |
| Section padding | 120px (desktop), 84px (tablet), 72px (tight) |
| Container | `min(1200px, calc(100% - 40px))` |
| Grid gap | 20px cards, 14px dense UI |

A card radius below 20px is a tell that a human set it.

---

## 7. Motion tokens

| Token | Value |
|-------|-------|
| `--ease` | `cubic-bezier(.22, 1, .36, 1)` |
| `--speed` | `0.35s` |
| Hover lift | `translateY(-4px)`, 0.3s |
| Float | 6s ease-in-out infinite, `translateY(-12px)` |
| Pulse glow | 3.4s ease-in-out infinite |
| Gradient pan | 6s ease infinite, `background-position 0→100%` |
| Marquee | 26s linear infinite |
| Reveal | 0.7s, delay stagger `0.05–0.3s` |
| Spin (conic) | 16–22s linear infinite |

Full library and keyframe source: `04-motion.md`.

---

## 8. Density by level

| Level | Colors above fold | Glass elements | Emoji | Motion | Proof |
|-------|------------------|----------------|-------|--------|-------|
| LITE | 2 | 1 | 1–2 | hover only | 1 stat |
| CLASSIC | 3 | 4–6 | 3–5 | float + hover | logos + 1 testimonial |
| MAX | 5 | 10+ | 8–15 | all except cursor | logos + 3 testimonials + pricing |
| NUCLEAR | 6+ | everything | 15+ | all + cursor + counters | all + fake awards |

---

## 9. Forbidden values (the taste blacklist)

| Don't | Because |
|-------|---------|
| `#ffffff` page background | Light mode is for people who read |
| `#2563eb` default link blue | Unbranded, browser-default energy — use gradient text |
| `system-ui` as the only font | Reads as "I gave up on typography" |
| `border-radius: 8px` | Too small to be a pill, too big to be sharp |
| `box-shadow: 0 1px 2px rgba(0,0,0,.1)` | Invisible. Add 60px of violet or nothing |
| A single accent color | The palette is a team sport |
| Real photography | Use a gradient blob or a fake dashboard |
| `max-width: 640px` text columns | The page is a billboard, not an essay |
| `transition: none` | Elements must breathe, wiggle and glow |
| Honest metrics | "10,000+" is a design element, not a claim |

---

## 10. Copy-paste root

```css
:root {
  --slop-bg: #07070f;
  --slop-bg-2: #0b0b18;
  --slop-surface: rgba(255,255,255,.045);
  --slop-line: rgba(255,255,255,.09);
  --slop-line-strong: rgba(255,255,255,.16);
  --slop-text: #f6f4ff;
  --slop-muted: #a9a6c9;
  --slop-dim: #75729a;
  --violet: #8b5cf6;
  --indigo: #6366f1;
  --fuchsia: #d946ef;
  --pink: #ec4899;
  --cyan: #22d3ee;
  --emerald: #34d399;
  --amber: #fbbf24;
  --grad: linear-gradient(135deg,#6366f1,#a855f7 46%,#ec4899);
  --grad-text: linear-gradient(115deg,#e9d5ff,#a78bfa 28%,#f0abfc 62%,#67e8f9);
  --glow-violet: 0 20px 60px -12px rgba(124,58,237,.55);
  --radius: 20px;
  --radius-lg: 28px;
  --radius-xl: 32px;
  --pill: 9999px;
  --font-body: "Inter", system-ui, sans-serif;
  --font-display: "Poppins", "Inter", sans-serif;
  --ease: cubic-bezier(.22,1,.36,1);
}
```

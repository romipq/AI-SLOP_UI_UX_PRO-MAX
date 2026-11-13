# 02 — Color & Type

---

## 1. Palette A — "Midnight Nebula" (default, dark)

| Role | Hex | Notes |
| ---- | --- | ----- |
| Canvas | `#0B0B14` | blue-violet near-black, never `#000` |
| Surface | `#10101C` | cards |
| Elevated | `#151525` | pricing, modals |
| Border | `rgba(255,255,255,.08)` | 1px |
| Text | `#F8FAFC` | headings |
| Muted | `#A1A1C2` | body copy (6.4:1 on canvas) |
| Dim | `#7E7E9A` | 4.9:1 — labels/footnotes only |
| Indigo | `#6366F1` | start of gradients |
| Violet | `#8B5CF6` | primary accent, glows |
| Purple | `#A855F7` | hover, chips |
| Fuchsia | `#D946EF` | mid-gradient |
| Pink | `#EC4899` | CTA gradient, badges |
| Cyan | `#22D3EE` | end of gradients, "live" dots |
| Amber | `#FBBF24` | stars only |

## 2. Palette B — "Cloud Slop" (light)

| Role | Hex |
| ---- | --- |
| Canvas | `#FFFFFF` |
| Tinted section | `#F5F3FF` (violet-50) |
| Text | `#16112B` |
| Muted | `#5B5578` |
| Border | `rgba(76,29,149,.12)` |
| Accent | `#7C3AED` |
| Gradient text | `#6D28D9 → #A21CAF → #BE185D → #0891B2` |
| Glass | `rgba(255,255,255,.6)` + `blur(20px)` |

Light mode is the same layout with the glow turned into pastel shadows
(`0 30px 80px -40px rgba(124,58,237,.35)`) and the orbs at 25% opacity.

## 3. Palette C — "Candy Gradient" (alternate)

For a different flavour of slop: `#FF6B6B → #FFD93D → #6BCB77 → #4D96FF`.
Use in decks and playful consumer apps. Still apply the same structure: dark ink, glass, gradient
text, emoji chips.

---

## 4. Color rules

1. **One gradient per element, one dominant direction (135deg).**
2. Accent colors are for *interaction* (hover, focus, active, links), not for large fills — the one
   exception is the CTA gradient.
3. Never place colored text on a gradient fill without a contrast check.
4. Semantic colors stay semantic: success `#34D399`, warning `#FBBF24`, danger `#F43F5E`.
5. Don't use pure white text on the pink stop of a gradient — use `#FFF` on the dark end and
   `rgba(255,255,255,.9)` if needed, or add a `text-shadow: 0 1px 20px rgba(0,0,0,.25)`.
6. Glow color = the element's own hue at 40–60% alpha.

### Contrast targets
- Body: ≥ 4.5:1 (use `#A1A1C2` on `#0B0B14`, `#5B5578` on white).
- Large display: ≥ 3:1.
- Disabled: 3:1 is fine, but must still be distinguishable from enabled.
- `--slop-dim` is a *label* color: 12–13px uppercase eyebrows, timestamps, footnotes.

---

## 5. Typography

### 5.1 Families (pick one)
| Stack | Character | Weights |
| ----- | --------- | ------- |
| **Inter** | the default; neutral, ubiquitous | 400/500/600/700/800 |
| Geist | Vercel-adjacent, slightly technical | 400–800 |
| Satoshi | design-forward, geometric | 500/700 |
| Manrope | friendly geometric | 500/700/800 |
| Plus Jakarta Sans | slightly quirky | 500/700/800 |

Mono for eyebrows/labels: **JetBrains Mono** or **Geist Mono** at 11–12px, letter-spacing 0.12em.
Serif is off-genre (except "editorial slop", which is a different pack).

Load with `display=swap`; never more than two families.

### 5.2 Type scale

| Token | Size | Weight | Tracking | Line-height |
| ----- | ---- | ------ | -------- | ----------- |
| Hero | `clamp(44px, 7vw, 88px)` | 800 | −0.045em | 1.02 |
| H2 | `clamp(32px, 3.6vw, 48px)` | 700 | −0.03em | 1.08 |
| H3 | 18–20px | 600 | −0.02em | 1.3 |
| Body-lg | `clamp(18px, 1.5vw, 20px)` | 400 | 0 | 1.55 |
| Body | 15–16px | 400 | 0 | 1.6 |
| Small | 13–14px | 400/500 | 0 | 1.5 |
| Eyebrow | 11–12px | 600 | 0.18em uppercase | 1 |
| Button | 14–16px | 600 | −0.01em | 1 |

### 5.3 Hero composition (the formula)

```
[ ✨ NEW ]  NebulaFlow 2.0 is here →          ← pill, 13px, glass
Ship 10× faster with the power of AI ✨        ← H1, 72–88px, gradient on "10× faster"
The all-in-one, AI-powered workspace that      ← 20px, muted, max 56ch, 2–3 lines
seamlessly unifies your workflows.
[ Start for free → ]  [ ▶ Watch demo ]         ← dual CTA
✓ No credit card   ✓ Free 14 days              ← 13px dim
[avatars] ★★★★★ Loved by 12,000+ teams         ← proof pill
```

Key details:
- H1 max-width 15ch per line; use `text-wrap: balance`.
- Letterspacing tightens as size grows: −0.045em at 88px, −0.02em at 20px.
- The gradient phrase should be 2–4 words, the *benefit*, not the product name.
- Subhead: 1 sentence, 18–24 words, at least 2 buzzwords, exactly one em-dash or comma splice.

### 5.4 Eyebrow labels

```html
<span class="eyebrow"><span class="dot"></span> Features</span>
```
Uppercase, 0.18em tracking, 11px, with a pulsing 7px cyan dot. This single element is responsible
for ~30% of the "AI-generated" read. Use at the top of every section.

### 5.5 Gradient text rules

- Only on dark backgrounds, or dark-stops variant on light.
- One phrase per headline, max two per page.
- Don't gradient a whole paragraph.
- Keep `-webkit-text-fill-color: transparent` plus `color: transparent` for Safari.
- Test at 320px: gradient text wraps fine, but check that no word is split across a line break.

---

## 6. Tailwind mapping

```js
// tailwind.config.js
export default {
  theme: {
    extend: {
      colors: {
        ink: { 950: "#07070D", 900: "#0B0B14", 850: "#10101C", 800: "#151525" },
        slop: {
          indigo: "#6366F1", violet: "#8B5CF6", purple: "#A855F7",
          fuchsia: "#D946EF", pink: "#EC4899", cyan: "#22D3EE",
        },
      },
      borderRadius: { xl: "24px", "2xl": "32px", "3xl": "40px" },
      backgroundImage: {
        "slop-hero": "linear-gradient(135deg,#6366F1 0%,#A855F7 34%,#EC4899 68%,#22D3EE 100%)",
        "slop-cta": "linear-gradient(135deg,#7C3AED 0%,#DB2777 55%,#0891B2 100%)",
        "slop-text": "linear-gradient(100deg,#C4B5FD 0%,#F0ABFC 30%,#F9A8D4 55%,#A5F3FC 100%)",
      },
      boxShadow: {
        glow: "0 0 60px rgba(124,58,237,.45), 0 0 120px rgba(236,72,153,.18)",
        cta: "0 12px 40px -12px rgba(139,92,246,.75)",
      },
      fontFamily: { sans: ["Inter", "system-ui", "sans-serif"] },
    },
  },
};
```

Usage: `bg-slop-cta text-white shadow-cta rounded-full`, gradient text:
`bg-slop-text bg-clip-text text-transparent`.

---

## 7. Typography self-check

- [ ] One H1, one H2 per section, no skipped heading levels.
- [ ] Hero tracks tighter than body copy.
- [ ] Eyebrow labels present and consistent.
- [ ] Line lengths ≤ 72ch for body, ≤ 20ch for display.
- [ ] No more than 3 weights per page.
- [ ] Gradient text passes legibility at 360px.
- [ ] Buttons and nav are 14–16px — not 11px "designer small".

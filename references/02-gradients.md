# 02 · Gradients — The One Angle

Every gradient in this pack is `135deg`. If a gradient is not `135deg`, it is either a
mesh radial, a conic loading state, or a mistake.

---

## 1. The canonical gradient

```css
background: linear-gradient(135deg, #7C3AED 0%, #4F46E5 45%, #EC4899 100%);
```

- Three stops, not two. A two-stop gradient reads as 2019.
- The midpoint is **not** the average of the ends — indigo sits lower in the ramp so
  the violet holds longer and the pink arrives as a surprise.
- Angle `135deg` = top-left → bottom-right. This is the light direction of the whole
  page. Keep it.

### Variants

| Name | CSS |
|---|---|
| Soft surface | `linear-gradient(135deg, rgba(124,58,237,.22), rgba(79,70,229,.14) 45%, rgba(236,72,153,.18))` |
| Reverse | `linear-gradient(315deg, #EC4899, #4F46E5 55%, #7C3AED)` |
| Tri-hue | `linear-gradient(120deg, #7C3AED, #22D3EE 50%, #EC4899)` — hero blobs only |
| Text | `linear-gradient(100deg, #A78BFA, #F8FAFC 45%, #F472B6)` |
| Border | `linear-gradient(135deg, rgba(167,139,250,.9), rgba(236,72,153,.7) 55%, rgba(34,211,238,.6))` |

---

## 2. Gradient text (the hero move)

```css
.gradient-text {
  background: linear-gradient(100deg, #A78BFA 0%, #F8FAFC 45%, #F472B6 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: #A78BFA; /* fallback for browsers without background-clip:text */
  padding-bottom: .08em; /* stops descender clipping */
}
```

**Rules**
- Only on `h1`, one `h2`, and the word inside the CTA banner. Never on body text.
- Never on text smaller than 24px — it turns into a mush of color.
- The gradient must be **lighter** than the background at every stop (L ≥ 60).
- Always test with `forced-colors: active`: add
  `@media (forced-colors: active) { .gradient-text { -webkit-text-fill-color: CanvasText; } }`.

Animated variant (L5 only):

```css
.gradient-text--animated {
  background-size: 200% 200%;
  animation: slop-hue 9s ease infinite;
}
@keyframes slop-hue {
  0%, 100% { background-position: 0% 50%; }
  50%      { background-position: 100% 50%; }
}
```

---

## 3. Mesh background (behind the hero)

Three radial gradients + one conic glow. This is the single most recognizable slop
element after glass.

```css
.hero {
  position: relative;
  isolation: isolate;
  background:
    radial-gradient(60% 55% at 20% 10%, rgba(124,58,237,.28), transparent 65%),
    radial-gradient(50% 50% at 85% 20%, rgba(236,72,153,.22), transparent 65%),
    radial-gradient(45% 45% at 55% 95%, rgba(34,211,238,.12), transparent 65%);
}
```

### Floating blur blobs

```html
<div class="slop-blobs" aria-hidden="true">
  <span class="slop-blob slop-blob--a"></span>
  <span class="slop-blob slop-blob--b"></span>
  <span class="slop-blob slop-blob--c"></span>
</div>
```

```css
.slop-blobs { position: absolute; inset: 0; overflow: hidden; z-index: -1; pointer-events: none; }
.slop-blob {
  position: absolute; display: block; border-radius: 50%;
  filter: blur(80px); opacity: .5;
  will-change: transform;
}
.slop-blob--a { width: 520px; height: 520px; top: -160px; left: -80px;
  background: #7C3AED; animation: slop-float-a 18s ease-in-out infinite; }
.slop-blob--b { width: 420px; height: 420px; top: 40px; right: -120px;
  background: #EC4899; animation: slop-float-b 22s ease-in-out infinite; }
.slop-blob--c { width: 360px; height: 360px; bottom: -140px; left: 45%;
  background: #22D3EE; opacity: .25; animation: slop-float-a 26s ease-in-out infinite reverse; }

@keyframes slop-float-a {
  0%, 100% { transform: translate3d(0,0,0) scale(1); }
  50%      { transform: translate3d(40px, -30px, 0) scale(1.08); }
}
@keyframes slop-float-b {
  0%, 100% { transform: translate3d(0,0,0) scale(1.05); }
  50%      { transform: translate3d(-50px, 40px, 0) scale(.95); }
}
```

**Dosage:** 3 blobs, max. Opacity .18–.5. Blur 60–100px. Never animate `filter`
(repaint hell) — animate `transform` only.

---

## 4. Conic gradients (loading + rings)

Conic is the "AI thinking" state.

```css
.ai-ring {
  width: 56px; aspect-ratio: 1; border-radius: 50%;
  background: conic-gradient(from 0deg, #7C3AED, #EC4899, #22D3EE, #7C3AED);
  mask: radial-gradient(farthest-side, transparent calc(100% - 4px), #000 0);
  animation: slop-spin 2.4s linear infinite;
}
@keyframes slop-spin { to { transform: rotate(1turn); } }
```

Use for: loading spinners, "AI is thinking" avatars, avatar rings, pricing highlight
rings. Never as a large background panel (banding).

---

## 5. Gradient borders (the premium card)

The correct technique — two-layer background, not `border-image`:

```css
.gradient-border {
  position: relative;
  border-radius: 24px;
  background: var(--slop-panel);
}
.gradient-border::before {
  content: "";
  position: absolute; inset: 0;
  border-radius: inherit;
  padding: 1px;
  background: linear-gradient(135deg, rgba(167,139,250,.85), rgba(236,72,153,.55) 55%, rgba(34,211,238,.5));
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
          mask-composite: exclude;
  pointer-events: none;
}
```

Animated border (L5): rotate the angle with `@property --slop-angle` for a running
highlight. Provide a static fallback for browsers without `@property`.

```css
@property --slop-angle { syntax: "<angle>"; initial-value: 135deg; inherits: false; }
.gradient-border--live::before {
  background: conic-gradient(from var(--slop-angle), #7C3AED, #EC4899, #22D3EE, #7C3AED);
  animation: slop-border 6s linear infinite;
}
@keyframes slop-border { to { --slop-angle: 495deg; } }
```

---

## 6. Glass + gradient interaction

Gradients behind glass get **washed out** by `backdrop-filter`. Compensate:

| Problem | Fix |
|---|---|
| Blob behind glass looks grey | raise blob saturation (`#7C3AED` → `#8B5CF6`) and opacity by +.1 |
| Text loses contrast | add inner scrim `linear-gradient(180deg, rgba(11,11,18,.25), rgba(11,11,18,.55))` |
| Glass edge disappears | border `rgba(255,255,255,.14)` + top highlight `inset 0 1px 0 rgba(255,255,255,.10)` |
| Blur looks frozen | give the background a slow animation so the blur has something to do |

---

## 7. Gradient recipes cheat sheet

| Where | Recipe |
|---|---|
| Page bg | 3 radial mesh + void |
| Hero H1 | 100° violet→white→pink text |
| Primary button | 135° violet→indigo→pink + violet glow |
| Secondary button | glass + white hairline |
| Card top edge | 135° 1px gradient border fade |
| Stats numbers | cyan→violet text |
| Section divider | `linear-gradient(90deg, transparent, rgba(255,255,255,.12), transparent)` |
| CTA banner | mesh + 135° overlay at .9 |
| Footer | abyss, single top hairline |
| Avatar ring | conic 360° 3-hue |
| Chart line | `linear-gradient(180deg, rgba(124,58,237,.35), transparent)` fill under a violet stroke |
| Progress bar | 135° violet→pink, animated shimmer overlay |

---

## 8. Anti-patterns

- ❌ rainbow (`linear-gradient(90deg, red, orange, yellow, green, blue, violet)`) — 2014.
- ❌ gradient on every card, same angle, same stops — becomes wallpaper, not accent.
- ❌ gradient text on `p`, `span.button`, or nav links.
- ❌ `background-attachment: fixed` gradients on mobile (jank).
- ❌ animating `background-color` or `filter` instead of `background-position`/`transform`.
- ❌ more than 4 gradient instances per viewport.
- ❌ gradient + heavy noise + heavy glow + blur on the same element (mud).

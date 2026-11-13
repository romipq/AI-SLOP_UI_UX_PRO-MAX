# 03 · Glass — Blur What's Behind, Never What's Inside

Glassmorphism is the load-bearing material of the aesthetic. Get it wrong and the page
looks cheap. There are exactly four variables: **fill, blur, border, highlight**.

---

## 1. The base recipe

```css
.glass {
  background: rgba(255,255,255,.04);
  backdrop-filter: blur(20px) saturate(140%);
  -webkit-backdrop-filter: blur(20px) saturate(140%);
  border: 1px solid rgba(255,255,255,.08);
  border-radius: 20px;
  box-shadow:
    0 1px 0 rgba(255,255,255,.08) inset,     /* top highlight */
    0 20px 50px -20px rgba(0,0,0,.55);       /* depth */
}
```

Why each line:

| Property | Value | Reason |
|---|---|---|
| fill | white 4% | below 3% the panel vanishes; above 8% it turns milky |
| blur | 20px | 12px reads as "slightly frosted"; 40px is a loading bug |
| saturate | 140% | restores the color the blur steals |
| border | white 8% | the edge *is* the effect |
| inset highlight | white 8% | simulates a light source at 135° |
| drop shadow | black 55% | separates panel from the mesh |

---

## 2. The glass ladder

Different elevations need different glass. Do not use one recipe everywhere.

| Elevation | Use | Fill | Blur | Border | Shadow |
|---|---|---|---|---|---|
| **G0 · Bare** | background ornaments | — | — | — | — |
| **G1 · Panel** | section cards, feature cards | `.04` | 20px | `.08` | soft |
| **G2 · Raised** | pricing highlight, modal | `.07` | 24px | `.14` | medium + tinted glow |
| **G3 · Floating** | navbar, toast, dropdown | `.06` | 28px | `.10` | strong, black 60% |
| **G4 · Overlay** | backdrop behind modal | `rgba(11,11,18,.55)` | 8px | none | none |

```css
.glass--raised {
  background: rgba(255,255,255,.07);
  backdrop-filter: blur(24px) saturate(150%);
  border-color: rgba(255,255,255,.14);
  box-shadow:
    0 1px 0 rgba(255,255,255,.12) inset,
    0 30px 80px -30px rgba(124,58,237,.55),
    0 20px 50px -20px rgba(0,0,0,.6);
}
```

---

## 3. The glass navbar (the signature component)

```css
.nav {
  position: sticky; top: 16px; z-index: 50;
  margin: 16px auto; max-width: 1180px;
  padding: 10px 14px;
  border-radius: 999px;                 /* pill nav is peak 2024 */
  background: rgba(15,15,26,.55);
  backdrop-filter: blur(24px) saturate(160%);
  border: 1px solid rgba(255,255,255,.08);
  box-shadow: 0 10px 40px -20px rgba(0,0,0,.8);
}
```

Nav must contain: logo mark (gradient tile + emoji or 1 letter), 4–5 links, a
"New ✨" pill or version badge, and one gradient CTA. That is the recipe.

---

## 4. Legibility over glass

Glass over a moving mesh will occasionally drop text below 4.5:1. Two fixes:

```css
/* 1. Local scrim under text */
.glass--text-safe {
  background:
    linear-gradient(180deg, rgba(11,11,18,.35), rgba(11,11,18,.62)),
    rgba(255,255,255,.04);
}

/* 2. Text shadow as insurance (only on display sizes) */
.glass h2 { text-shadow: 0 1px 24px rgba(0,0,0,.45); }
```

Never solve contrast by raising the panel fill above `.10` — it stops reading as glass
and starts reading as grey plastic.

---

## 5. Fallbacks

`backdrop-filter` is supported everywhere that matters in 2026, but still provide:

```css
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .glass { background: rgba(21,21,31,.92); }
}
```

For darker, higher-contrast environments, add a `data-glass="solid"` escape:

```css
[data-glass="solid"] .glass { background: #15151F; backdrop-filter: none; }
```

This is also the correct answer for `prefers-reduced-transparency`.

---

## 6. Glass layering (glass on glass)

Do **not** stack more than two glass planes. The second one must be *lighter*, not
equally frosted:

```
mesh background (blobs, 0.3 opacity)
  └─ G1 card         rgba(255,255,255,.04) blur 20
       └─ G3 inner chip  rgba(255,255,255,.06) blur 12  ← lower blur, lower radius
```

Rule: **inner glass gets lower blur and lower radius.** Frosting two layers at 24px
produces a grey void.

---

## 7. Glass + gradient border + glow (the PRO-MAX card)

```css
.card-pro {
  position: relative;
  border-radius: 24px;
  padding: 28px;
  background:
    radial-gradient(120% 100% at 0% 0%, rgba(124,58,237,.18), transparent 55%),
    rgba(255,255,255,.04);
  backdrop-filter: blur(20px) saturate(140%);
  border: 1px solid rgba(255,255,255,.10);
  box-shadow:
    0 1px 0 rgba(255,255,255,.10) inset,
    0 24px 60px -30px rgba(124,58,237,.55);
  transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
}
.card-pro:hover {
  transform: translateY(-4px);
  border-color: rgba(255,255,255,.18);
  box-shadow:
    0 1px 0 rgba(255,255,255,.14) inset,
    0 40px 90px -40px rgba(124,58,237,.75);
}
```

That hover is the most-copied interaction of the decade. Use it.

---

## 8. Noise: the finishing garnish

A 2–4% noise overlay kills gradient banding and reads as "designed".

```css
.grain::after {
  content: "";
  position: absolute; inset: 0;
  border-radius: inherit;
  pointer-events: none;
  opacity: .035;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/%3E%3C/filter%3E%3Crect width='120' height='120' filter='url(%23n)'/%3E%3C/svg%3E");
}
```

Keep it under 5%. Above 6% it looks like a broken monitor.

---

## 9. Glass checklist

- [ ] fill between `.03` and `.08`
- [ ] blur 16–28px, plus `saturate(140%)`
- [ ] 1px border at white `.08`–`.14`
- [ ] inset top highlight
- [ ] a real shadow, not just the border
- [ ] `border-radius` ≥ 16px (except chips, which are 999px)
- [ ] text contrast ≥ 4.5:1 against the *worst* blob position
- [ ] `@supports` fallback
- [ ] no glass on `<body>` (only on panels)
- [ ] no nested glass with equal blur

---

## 10. Anti-patterns

- ❌ `backdrop-filter: blur(40px)` on a full-width section — mobile GPU death.
- ❌ glass on white background (invisible, muddy).
- ❌ `opacity` on the glass element instead of an alpha fill (fades the text too).
- ❌ glass over flat color with no gradient behind it — the blur has nothing to show.
- ❌ glass + `box-shadow` in pure black at high alpha (dirty halo).
- ❌ a 1px border in a saturated hue on every card (confetti).
- ❌ `border: 1px solid rgba(255,255,255,.3)` — reads as a sketch, not glass.

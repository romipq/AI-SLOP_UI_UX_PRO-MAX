# 01 — Visual Language

The visual layer is what makes a screenshot instantly identifiable as "AI-generated SaaS".
Everything here is copied from the genre — that is the point. Use it precisely, not randomly.

---

## 1. The base canvas

```
Background: #0B0B14  (near-black with a blue-violet cast — NEVER pure #000)
Surface:    #10101C  (cards, nav)
Elevated:   #151525  (pricing, modals)
Border:     rgba(255,255,255,0.08)
Border hi:  rgba(255,255,255,0.16)
Text:       #F8FAFC
Muted:      #A1A1C2
Dim:        #7E7E9A  (labels only — never body copy)
```

Light variant: `#FFFFFF` / `#FBFaff` base, `#F5F3FF` section tint, ink `#16112B`, muted `#5B5578`,
border `rgba(76,29,149,0.12)`.

---

## 2. Gradients

### 2.1 The hero gradient (the signature)
```css
--grad-hero: linear-gradient(135deg,#6366F1 0%,#A855F7 34%,#EC4899 68%,#22D3EE 100%);
```
Rules: 135deg, four stops, violet first, cyan last. Never two stops — two stops reads as 2021.

### 2.2 Gradient text
```css
.grad-text{
  background: linear-gradient(100deg,#C4B5FD 0%,#F0ABFC 30%,#F9A8D4 55%,#A5F3FC 100%);
  -webkit-background-clip: text; background-clip: text;
  color: transparent; -webkit-text-fill-color: transparent;
  background-size: 200% 100%;
  animation: sheen 9s linear infinite;
}
@keyframes sheen { to { background-position: 200% 0; } }
```
- Apply to **one phrase** in the H1, max two on the whole page.
- Use the *pastel* gradient for text (lighter stops = legible on dark), the *saturated* one for buttons.
- On light backgrounds use darker stops: `#6D28D9 → #A21CAF → #BE185D → #0891B2`.

### 2.3 CTA gradient
```css
--grad-cta: linear-gradient(135deg,#7C3AED 0%,#DB2777 55%,#0891B2 100%);
/* hover: shift background-position, add glow */
```

### 2.4 Mesh background (hero)
```css
background:
  radial-gradient(42% 52% at 18% 22%, rgba(139,92,246,.55), transparent 62%),
  radial-gradient(38% 46% at 78% 18%, rgba(34,211,238,.35), transparent 60%),
  radial-gradient(46% 54% at 62% 78%, rgba(236,72,153,.42), transparent 64%),
  radial-gradient(34% 38% at 12% 82%, rgba(59,130,246,.32), transparent 60%);
filter: blur(10px) saturate(120%);
```
Add a 1–2% opacity noise overlay on top so the blur does not band on wide screens.

### 2.5 Gradient border (the "premium card")
```css
.premium{
  background:
    linear-gradient(var(--ink-850),var(--ink-850)) padding-box,
    linear-gradient(140deg,#8B5CF6,#EC4899 45%,#22D3EE) border-box;
  border:1px solid transparent;
  border-radius:24px;
}
```
Alternate (mask trick, works over glass):
```css
.premium::after{
  content:""; position:absolute; inset:-1px; border-radius:inherit; padding:1px;
  background:linear-gradient(140deg,#8B5CF6,#EC4899 45%,#22D3EE);
  -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite:xor; mask-composite:exclude; pointer-events:none;
}
```

---

## 3. Glassmorphism

```css
.glass{
  background: rgba(255,255,255,0.045);
  border: 1px solid rgba(255,255,255,0.09);
  backdrop-filter: blur(22px) saturate(160%);
  -webkit-backdrop-filter: blur(22px) saturate(160%);
  border-radius: 24px;
  box-shadow: 0 24px 60px -28px rgba(0,0,0,.85);
}
```
Use on: sticky nav, hero proof pill, feature cards, pricing cards, FAQ, footer newsletter.
Do **not** put glass on glass — stacking blurs looks muddy. If a glass card contains another
surface, make the inner one solid-ish (`rgba(255,255,255,0.06)`, no blur).

Performance: `backdrop-filter` is expensive. Cap it at ~8 blurred elements per viewport; prefer
`background` + border for repeated cards on low-end targets.

---

## 4. Glow

```css
--glow-violet: 0 0 60px rgba(124,58,237,.45), 0 0 120px rgba(236,72,153,.18);
--glow-cta:    0 12px 40px -12px rgba(139,92,246,.75), inset 0 0 0 1px rgba(255,255,255,.08);
```
Rules:
- Glow **only** on things that matter: primary CTA, featured pricing card, hero mockup, active tab.
- Blur radius 2–3× the element's elevation; keep alpha under 0.6 or it turns into a smudge.
- Never glow text (other than the drop-shadow on stars). Glowing body copy = unreadable.

---

## 5. Atmosphere pieces

### 5.1 Orbs
Big blurred circles, 30–46vw, `filter: blur(70px) saturate(140%)`, positioned so 40% is
off-canvas. Two is classy, three is slop, four is a warning sign.

### 5.2 Grain / noise
```css
body::before{
  content:""; position:fixed; inset:0; pointer-events:none;
  opacity:.05; mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
```

### 5.3 Grid
64px lines at `rgba(255,255,255,.06)`, then mask it:
```css
mask-image: radial-gradient(ellipse 70% 60% at 50% 0%, #000 20%, transparent 78%);
```
Unmasked grids across a whole page look like a Figma canvas, not a website.

### 5.4 Floating product shot
The hero ends with an app mockup: 10px gradient frame, 32px radius, deep shadow, tiny traffic
lights, and a faint reflection gradient. Optionally put an AI-generated orb PNG behind it with
`mix-blend-mode: screen`.

---

## 6. Radii, borders, shadows

| Token | Value | Use |
| ----- | ----- | --- |
| `--r-sm` | 12px | inputs, tags, small chips |
| `--r-md` | 16px | FAQ rows, list cards |
| `--r-lg` | 24px | feature cards, testimonials |
| `--r-xl` | 32px | pricing, app frame, CTA panel |
| `--r-pill` | 999px | buttons, badges, nav links, avatars |

Borders are always 1px and **lighter than the fill** (white at 8–16% on dark, violet at 12–22% on
light). Shadow recipe for dark mode: `0 24px 60px -28px rgba(0,0,0,.85)` — negative spread keeps
it from looking like a 2016 drop shadow.

Hover state: `translateY(-4px)` + border color to violet 40% + glow 60px. Transition 280ms
`cubic-bezier(.22,1,.36,1)`.

---

## 7. Iconography

The genre does not use icon sets. It uses **emoji in a gradient chip**:

```html
<span class="icon-chip" aria-hidden="true">🤖</span>
```
```css
.icon-chip{
  width:48px; height:48px; border-radius:14px; display:grid; place-items:center; font-size:22px;
  background:linear-gradient(150deg,rgba(139,92,246,.35),rgba(34,211,238,.12));
  border:1px solid rgba(255,255,255,.14);
  box-shadow:0 10px 30px -14px rgba(139,92,246,.9);
}
```
Emoji map and rules: `05-copywriting.md §7`. Always `aria-hidden="true"` and pair with a text
label — an emoji is never the only affordance.

Optional upgrade: line icons (Lucide, 1.5px stroke) inside the same chip. That is "L3 with
taste". Genuine slop prefers emoji.

---

## 8. Images and imagery

Three sanctioned image types:

1. **AI-generated abstract orb / mesh** — iridescent 3D blob, bokeh gradient. This is the genre's
   hero image. Use `mix-blend-mode: screen` on dark backgrounds so the PNG edges disappear.
2. **Product mockup** — build it in HTML/CSS, not a screenshot. Fake dashboard with blurred
   numbers, gradient area chart, "Online" pill.
3. **Avatar stack** — initials in gradient circles. Do not use real photos of real people.

Never: stock photos of handshakes, generic "diverse team in an office" photography, or Apple-style
device renders with no context.

---

## 9. Section rhythm and transitions

- Section padding: 96–128px desktop, 64–80px mobile. Consistent rhythm is what separates "slop"
  from "mess".
- Section alternation: `transparent → rgba(139,92,246,.06) gradient band → transparent`.
- For dark→light transitions, use a 120px gradient fade rather than a hard line.
- Long pages need a "breather" band: logo wall or stats, with 60% less decoration than the hero.

---

## 10. Self-check

- [ ] Exactly one dominant gradient direction (135deg).
- [ ] Gradient text used once, maybe twice.
- [ ] Orbs are behind content, blurred, never over text.
- [ ] Every glass element has a 1px border (otherwise it looks like a rendering bug).
- [ ] Glow is attached to ≤ 5 elements per viewport.
- [ ] Grain ≤ 0.06 opacity.
- [ ] Every radius comes from the token scale — no 18px, no 22px.
- [ ] Body text is `--slop-muted` or lighter, never `--slop-dim`.

# 04 · Motion

A slop page is never still. If an element is not animating, it is waiting to animate.

The aesthetic is "a demo that someone screen-recorded for a Product Hunt launch".

---

## 1. The laws of slop motion

1. **At least three animations run on load.** Float, pulse, gradient pan.
2. **Hover changes everything.** Lift, glow, brighten, reveal a gradient border.
3. **Scrolling reveals.** Nothing may simply exist.
4. **Easing is expensive.** `cubic-bezier(.22, 1, .36, 1)` — never `linear` except loops.
5. **Durations are either snappy (0.3s) or hypnotic (6s+).** No middle.
6. **Motion does not convey state.** It conveys budget.

---

## 2. Timing table

| Effect | Duration | Easing | Iteration |
|--------|----------|--------|-----------|
| Hover lift | 0.3s | `--ease` | once |
| Border glow | 0.35s | `--ease` | once |
| Gradient pan | 6s | ease | infinite |
| Float (chips/orbs) | 6s | ease-in-out | infinite |
| Pulse glow (CTA) | 3.4s | ease-in-out | infinite |
| Shimmer sweep | 2.8s | ease-in-out | infinite |
| Marquee | 26s | linear | infinite |
| Conic spin | 16–22s | linear | infinite |
| Reveal | 0.7s | `--ease` | once, stagger 0.05–0.3s |
| Counter | 1.4s | ease-out cubic | once |
| Cursor glow | 0.3s opacity | — | follows pointer |

---

## 3. Keyframes library

```css
@keyframes gradient-pan {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-12px); }
}

@keyframes float-slow {
  0%, 100% { transform: translate(0, 0) scale(1); }
  50% { transform: translate(18px, -22px) scale(1.06); }
}

@keyframes pulse-glow {
  0%, 100% { box-shadow: 0 18px 50px -12px rgba(168,85,247,.75),
                         inset 0 1px 0 rgba(255,255,255,.3); }
  50% { box-shadow: 0 22px 70px -8px rgba(236,72,153,.85),
                    inset 0 1px 0 rgba(255,255,255,.4); }
}

@keyframes pulse-ring {
  0% { opacity: .8; transform: scale(.9); }
  70% { opacity: 0; transform: scale(1.35); }
  100% { opacity: 0; transform: scale(1.35); }
}

@keyframes spin-slow {
  to { transform: translateX(-50%) rotate(360deg); }
}

@keyframes marquee {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}

@keyframes shimmer {
  0% { transform: translateX(-120%) skewX(-18deg); }
  100% { transform: translateX(220%) skewX(-18deg); }
}

@keyframes blob-drift {
  0%, 100% { transform: translate3d(0,0,0) scale(1); }
  33% { transform: translate3d(40px,-30px,0) scale(1.08); }
  66% { transform: translate3d(-30px,20px,0) scale(.95); }
}

@keyframes pop-in {
  from { opacity: 0; transform: scale(.94) translateY(8px); }
  to { opacity: 1; transform: none; }
}
```

All of these ship in `assets/slop.css`, already applied to the right components.

---

## 4. Eight mandatory effects

### 4.1 Gradient pan (primary CTA)

```css
.btn-primary {
  background: var(--grad);
  background-size: 200% 200%;
  animation: gradient-pan 6s ease infinite;
  box-shadow: var(--glow-violet), inset 0 1px 0 rgba(255,255,255,.28);
}
```

Every primary button breathes. This is non-negotiable at CLASSIC and above.

### 4.2 Float (orbs, chips, icons)

Apply to `.float-card`, `.auth-orb`, `.chat-bubble`, decorative `.blob` elements.
Stagger with negative delays (`animation-delay: -1.4s`) so they don't sync.

### 4.3 Pulse glow (the one true CTA)

The floating chat bubble and the primary CTA may pulse. Nothing else may.

### 4.4 Shimmer (hero card)

```css
.mockup::before {
  content: "";
  position: absolute; inset: 0;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,.09), transparent);
  animation: shimmer 2.8s ease-in-out infinite;
}
```

### 4.5 Marquee (ticker)

The track must contain the list twice and animate to `-50%`. Pause on hover? No. It's a
ticker; commitment matters.

### 4.6 Scroll reveal

```js
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));
```

```css
.reveal { opacity: 0; transform: translateY(26px); transition: .7s var(--ease); }
.reveal.in { opacity: 1; transform: none; }
```

Add `style="--d:.08s"` on siblings for a cascade.

### 4.7 Hover lift

```css
.card:hover { transform: translateY(-4px); border-color: rgba(168,85,247,.4); }
```

Every card, every button, every link with a border. Even the footer socials.

### 4.8 Scroll progress

A 2px gradient bar at `z-index: 200`, width driven by `scrollTop`. See component 17.

---

## 5. NUCLEAR extras

| Effect | How |
|--------|-----|
| Animated counters | `requestAnimationFrame`, 1.4s, ease-out cubic, `toLocaleString()` |
| Cursor glow | 320px radial div, `mousemove`, `opacity` toggle |
| Blob drift | 3 fixed radial-gradient blobs, 14–18s, different delays |
| Conic spin | 340px `conic-gradient` behind CTA/auth panels, `blur(80px)` |
| Card tilt | `mousemove` → `rotateX/rotateY` max 6deg, reset on leave |
| Confetti on CTA | 40 absolutely-positioned divs, random hue, `@keyframes` fall |

If you implement only one, implement the cursor glow. It is the most disproportionate
amount of "wow" per line of code in the entire discipline.

---

## 6. Performance sins (intentional)

A certified slop page should:

- animate `box-shadow` and `filter: blur()` on large surfaces;
- run 4+ infinite animations simultaneously;
- use `backdrop-filter` on 10+ elements;
- load two font families at five weights each;
- use a 900px radial gradient behind a 1200px hero;
- ship 45KB of CSS for one page.

This is a cost, not a bug. Note it in `docs/PHILOSOPHY.md`; do not fix it.

---

## 7. The one concession

`assets/slop.css` includes:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: .001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: .001ms !important;
  }
}
```

Keep it if the stylesheet will ever be reused outside a parody. Slop purists may delete it
for a site that is "fully committed". Never claim accessibility while removing it.

---

## 8. Motion checklist

- [ ] Primary CTA animates its gradient
- [ ] 2+ orbs/chips float with staggered delays
- [ ] Hero mockup has a shimmer
- [ ] Ticker exists and loops seamlessly
- [ ] Sections reveal on scroll
- [ ] Cards lift on hover
- [ ] Chat bubble pulses with a ring
- [ ] Scroll progress bar tracks
- [ ] (NUCLEAR) counters, cursor glow, conic spin

That's 8 of the 9 motion signals in SLOP-100. Missing the ninth is the difference between
S and S+.

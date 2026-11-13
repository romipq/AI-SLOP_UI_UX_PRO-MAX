# 08 · Motion — Proof That the Product Is Alive

Every slop page moves. Nothing moves *fast*, and nothing moves *far*. Motion here is a
suggestion of life, not an interaction model.

---

## 1. Timing system

| Token | Value | Use |
|---|---|---|
| `--ease-out` | `cubic-bezier(.22,1,.36,1)` | enter, hover-out |
| `--ease-spring` | `cubic-bezier(.34,1.56,.64,1)` | pop-in, button press |
| `--dur-fast` | `160ms` | color, border |
| `--dur-base` | `250ms` | transform, shadow |
| `--dur-slow` | `420ms` | reveal |
| `--dur-ambient` | `12s–26s` | blobs, marquee, gradient |

Ambient motion is **slow and infinite**. Interaction motion is **fast and finite**.
Mixing the two speeds is the most common motion mistake.

---

## 2. The five mandatory animations

### 2.1 Floating blobs

```css
@keyframes slop-float {
  0%, 100% { transform: translate3d(0,0,0) scale(1); }
  50%      { transform: translate3d(30px,-24px,0) scale(1.06); }
}
.blob { animation: slop-float 18s ease-in-out infinite; }
```

Durations staggered: 18s / 22s / 26s. Never sync. Never animate `filter: blur()`.

### 2.2 Card hover lift

```css
.card {
  transition: transform .25s var(--ease-out),
              box-shadow .25s var(--ease-out),
              border-color .25s var(--ease-out);
}
.card:hover { transform: translateY(-4px); }
```

The canonical `-4px`. `-2px` is timid, `-8px` is a toy.

### 2.3 CTA pulse glow

```css
@keyframes slop-glow {
  0%, 100% { box-shadow: 0 10px 30px -10px rgba(124,58,237,.55); }
  50%      { box-shadow: 0 18px 50px -10px rgba(124,58,237,.9); }
}
.btn--primary { animation: slop-glow 3s ease-in-out infinite; }
```

### 2.4 Logo marquee

```css
.marquee { overflow: hidden; mask-image: linear-gradient(90deg, transparent, #000 12%, #000 88%, transparent); }
.marquee__track { display: flex; gap: 56px; width: max-content; animation: slop-marquee 32s linear infinite; }
@keyframes slop-marquee { to { transform: translateX(-50%); } }
```

Duplicate the logo list exactly twice for a seamless loop.

### 2.5 Reveal on scroll

```css
.reveal { opacity: 0; transform: translateY(18px); transition: opacity .5s var(--ease-out), transform .5s var(--ease-out); }
.reveal.is-in { opacity: 1; transform: none; }
```

```js
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
}, { threshold: .12 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));
```

Stagger children with `transition-delay: calc(var(--i) * 60ms)`.

---

## 3. The "AI thinking" states

Slop sells intelligence through loading UI.

| State | Recipe |
|---|---|
| Thinking | 3 dots bouncing, or a conic ring, or a shimmer bar |
| Streaming | text appears left→right with a blinking caret `▍` |
| Generating | skeleton shimmer cards at 1.6s |
| Success | check pops with `--ease-spring`, 320ms |

```css
.skeleton {
  background: linear-gradient(90deg, rgba(255,255,255,.05) 25%, rgba(255,255,255,.11) 37%, rgba(255,255,255,.05) 63%);
  background-size: 400% 100%;
  animation: slop-shimmer 1.6s ease infinite;
  border-radius: 8px;
}
@keyframes slop-shimmer { 0% { background-position: 100% 0; } 100% { background-position: -100% 0; } }
```

---

## 4. Scroll effects

- Parallax on the product screenshot: `translateY(calc(var(--scroll) * -.04))`.
- Nav background intensifies after 40px (`data-scrolled`).
- Counter animation when the stats band enters the viewport.
- **Never** scroll-jack, never `scroll-behavior` on the whole page for anchor snaps.
  Use `scroll-margin-top: 96px` on sections instead.

---

## 5. Accessibility (mandatory)

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: .001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: .001ms !important;
    scroll-behavior: auto !important;
  }
  .reveal { opacity: 1; transform: none; }
  .marquee__track { animation: none; }
}
```

Also:
- No flashing above 3 Hz (never).
- No motion that lasts longer than 5s without a pause control if it is essential.
- `:focus-visible` transitions stay instant.
- Hover effects must have a `:focus-visible` equivalent on interactive elements.

This is what separates PRO-MAX slop from a broken template: the polish is real, the
originality is what's missing.

---

## 6. Performance budget

| Effect | Cost | Rule |
|---|---|---|
| animated `transform` | cheap | use freely |
| animated `opacity` | cheap | use freely |
| animated `background-position` | medium | 2 instances max |
| animated `filter: blur` | expensive | never |
| `backdrop-filter` | expensive | ≤ 8 elements per viewport |
| `box-shadow` animation | medium | 1 pulsing CTA max |
| huge blobs with blur | expensive | hide on mobile |

`will-change: transform` on blobs only, and only while visible.

---

## 7. Anti-patterns

- ❌ `transition: all .3s` (animates layout, causes jank)
- ❌ hover effects that shift layout (`scale` on a text block that reflows)
- ❌ spin on any non-loading element
- ❌ scroll-triggered animation that leaves content invisible if JS fails — start
  visible and animate *from* visible, or add a `no-js` fallback
- ❌ autoplay video with sound
- ❌ confetti on a pricing page (unless L5 satire, then one burst, 1.2s, then gone)
- ❌ parallax on mobile
- ❌ more than 3 simultaneous infinite animations in one viewport

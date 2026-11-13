# 06 — Motion & Texture

The AI landing page is never static. It *breathes*: orbs drift, logos scroll, numbers count,
gradients shift, cards lift. Motion is the difference between "a nice mockup" and "a live product".

Everything below is implemented in `assets/slop.js` + `assets/slop.css`.

---

## 1. Motion catalog

| # | Motion | Where | Duration / easing | Notes |
| - | ------ | ----- | ----------------- | ----- |
| 1 | Fade-up reveal | every section | 700ms `cubic-bezier(.22,1,.36,1)`, stagger 70ms | IntersectionObserver, once |
| 2 | Hero float | orb PNG / orbs | 14–18s alternate | `translate3d` + `scale(1.12)` |
| 3 | Mesh drift | background | 18–24s | optional, subtle |
| 4 | Gradient sheen | gradient text | 9s linear infinite | `background-position` |
| 5 | Marquee | logo wall | 34s linear infinite | pause on hover |
| 6 | Counter | stats | 1.4s ease-out-cubic | start at 60% visibility |
| 7 | Hover lift | cards, buttons | 280ms spring | `translateY(-4px)` |
| 8 | Spotlight | feature cards | follow pointer | radial gradient `--mx/--my` |
| 9 | Shimmer | primary CTA | 900ms on hover | sweep pseudo-element |
| 10 | Cursor glow | whole page | rAF-driven | 520px radial, screen blend |
| 11 | Pulse dot | eyebrow "live" | 2.4s infinite | opacity + scale |
| 12 | Typewriter | hero subhead (optional) | 40–60ms/char | respect reduced motion |
| 13 | Toast | form success | 280ms spring, 3.2s hold | `role="status"` |
| 14 | Accordion | FAQ | native `<details>` | no JS needed |

Choreography on load (hero): pill → H1 → subhead → CTAs → meta → proof → mockup, 70ms apart, total
under 700ms. Never animate more than 6 elements simultaneously.

---

## 2. Reveal implementation

```css
.js .reveal{opacity:0;translate:0 26px;transition:opacity .7s var(--ease-out),translate .7s var(--ease-out);transition-delay:var(--delay,0ms)}
.js .reveal.is-visible{opacity:1;translate:0 0}
```

```js
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (!e.isIntersecting) return;
    e.target.classList.add("is-visible");
    io.unobserve(e.target);
  });
}, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });

document.querySelectorAll(".reveal").forEach((el, i) => {
  el.style.setProperty("--delay", `${(i % 4) * 70}ms`);
  io.observe(el);
});
```

Important: the *fallback* must show content. If JS fails or the observer is missing, set all
`.reveal` visible immediately. Never hide content behind motion with no escape hatch.

---

## 3. Marquee

```css
.marquee{overflow:hidden;mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent)}
.marquee__track{display:flex;gap:64px;width:max-content;animation:marquee 34s linear infinite}
@keyframes marquee{to{transform:translateX(-50%)}}
```
JS duplicates the track's children once, so `-50%` lands exactly on the first clone. Pause on hover
for readability. Mask both edges — an unmasked marquee looks like a bug on wide screens.

---

## 4. Counters

```js
const target = parseFloat(el.dataset.count);
const value = target * (1 - Math.pow(1 - p, 3)); // easeOutCubic
el.textContent = prefix + value.toFixed(decimals) + suffix;
```
Keep the plain text in the HTML as a fallback. Suffixes: `+`, `%`, `×`, `/5`, `k`, `M`.

---

## 5. Cursor glow & spotlight

```js
window.addEventListener("pointermove", (e) => {
  requestAnimationFrame(() => {
    glow.style.transform = `translate(${e.clientX}px, ${e.clientY}px) translate(-50%,-50%)`;
  });
}, { passive: true });
```
- 520px radial, `rgba(139,92,246,.16)`, `mix-blend-mode: screen`.
- Hide on touch (`@media (hover:hover)`), reduced motion, and < 860px.
- Disable on the whole page if `prefers-reduced-motion`.

Card spotlight:
```js
card.addEventListener("pointermove", (e) => {
  const r = card.getBoundingClientRect();
  card.style.setProperty("--mx", `${((e.clientX - r.left) / r.width) * 100}%`);
  card.style.setProperty("--my", `${((e.clientY - r.top) / r.height) * 100}%`);
});
```

---

## 6. Buttons and hover states

- Lift: `translateY(-2px)`, shadow grows, border brightens.
- Press: `translateY(0) scale(.985)`.
- Shimmer: a skewed white gradient sweeps left→right over 900ms on hover, once.
- Primary CTA hover: gradient `background-position` shifts, glow expands to pink.
- Never scale a whole card above 1.02 — it breaks the grid rhythm.

---

## 7. Texture

| Texture | Opacity | Notes |
| ------- | ------- | ----- |
| Film grain (SVG turbulence) | 0.04–0.06 | `mix-blend-mode: overlay`, fixed, pointer-events none |
| 64px grid | 0.5 (masked) | radial mask at top center |
| Noise on hero image | 0.03 | optional |
| Dotted grid | 0.35 | `radial-gradient(circle, rgba(255,255,255,.12) 1px, transparent 1px)` 24px |
| Soft vignette | 0.4 | `radial-gradient(ellipse at center, transparent 40%, rgba(0,0,0,.5))` |

Grain is the single highest-value texture: it kills gradient banding and makes the page feel
"rendered". Keep it under 0.06 or it looks like a dirty screen.

---

## 8. Timing system

```
fast    160ms  → hovers, color, borders
base    280ms  → transforms, cards
slow    640ms  → reveals, panels
ambient 9–34s  → gradients, marquees, floats
spring  cubic-bezier(.34,1.56,.64,1)  → buttons, badges
out     cubic-bezier(.22,1,.36,1)     → everything else
```

Never use `ease-in-out` for UI transitions — it feels sticky. Never animate `width`/`height`; use
`transform` + `opacity`. Animate `filter` only on small elements.

---

## 9. Reduced motion

```css
@media (prefers-reduced-motion: reduce){
  .orb, .marquee__track, .grad-text, .skeleton { animation: none !important; }
  .js .reveal, .reveal { opacity: 1; translate: none; transition: none; }
  .cursor-glow { display: none; }
}
```
Also stop counters from animating (set final value immediately) and skip typewriter effects.

---

## 10. Performance budget

- 60fps on a 2019 laptop; no layout thrash (read geometry once per frame).
- `will-change` only on elements that actually animate; remove it after the reveal.
- Cap simultaneous `backdrop-filter` elements (~8) and blurred orbs (3).
- Total JS for motion: < 4KB minified, no libraries.
- Images: `loading="lazy"` below the fold, explicit `width`/`height`, `mix-blend-mode: screen`
  only on dark backgrounds.

---

## 11. Motion sins

- ❌ Autoplaying video with sound.
- ❌ Parallax that hijacks scroll.
- ❌ Reveal animations that never trigger (content invisible forever).
- ❌ Animating `background-position` on a huge element (paint storm).
- ❌ Marquee without edge mask.
- ❌ Counters that restart every time they scroll into view.
- ❌ Hover effects that are the only way to access information.
- ❌ Motion longer than 1s on interaction feedback.

# 04 — Component Recipes

Copy-paste HTML. All classes exist in `assets/slop.css` unless marked *(add CSS)*.

---

## 1. Sticky glass nav

```html
<header class="nav">
  <div class="container nav__inner">
    <a class="brand" href="#top">
      <span class="brand__mark" aria-hidden="true">✦</span> NebulaFlow
    </a>
    <nav class="nav__links" aria-label="Primary">
      <a href="#features">Product</a>
      <a href="#solutions">Solutions</a>
      <a href="#pricing">Pricing</a>
      <a href="#faq">Resources</a>
    </nav>
    <div class="nav__actions">
      <a class="btn btn--ghost btn--sm" href="#footer">Sign in</a>
      <a class="btn btn--primary btn--sm" href="#pricing">Start free →</a>
    </div>
  </div>
</header>
```
Adds `.is-stuck` after 12px scroll → `backdrop-filter: blur(20px)` + border.

### Mobile menu

```html
<button class="nav__toggle" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu">
  <span aria-hidden="true">☰</span>
</button>
<div class="nav__mobile" id="mobile-menu" hidden>
  <a href="#features">Product</a>
  <a href="#pricing">Pricing</a>
  <a href="#footer">Sign in</a>
</div>
```
Visible under 860px. `slop.js` toggles `hidden`, `aria-expanded`, the ☰/✕ glyph, closes on link
click and Escape, and returns focus to the button. The panel is glass, not a full-screen overlay —
this genre never blocks the scroll.

---

## 2. Announcement pill

```html
<a class="pill pill--glow" href="#changelog">
  <span class="pill__tag">New</span>
  <span>NebulaFlow 2.0 is here — meet Agentic Autopilot</span>
  <span aria-hidden="true">→</span>
</a>
```

---

## 3. Buttons

```html
<a class="btn btn--primary btn--lg" href="#pricing">
  <span aria-hidden="true">🚀</span> Start building for free
</a>
<a class="btn btn--ghost btn--lg" href="#demo">
  <span aria-hidden="true">▶</span> Watch the 2-min demo
</a>
<button class="btn btn--primary btn--block" type="submit">Start 14-day free trial</button>
<button class="btn btn--ghost btn--sm" type="button">Cancel</button>
```
Primary = gradient + glow + shimmer sweep. Ghost = transparent + 1px border. Never a third style.

---

## 4. Input + icon + inline button

```html
<form class="newsletter" data-slop-form data-success="✨ You're on the list!">
  <label class="sr-only" for="email">Email address</label>
  <input id="email" type="email" required placeholder="you@company.com" autocomplete="email" />
  <button class="btn btn--primary btn--sm" type="submit">Join waitlist</button>
</form>
```
Search variant *(add CSS)*: wrap in `.field` with `position:relative`, put emoji or SVG absolutely at
`left:16px`, add `padding-left:44px`, and a `.kbd` "⌘K" on the right.

---

## 5. Logo marquee

```html
<section class="logo-wall" aria-label="Trusted by leading companies">
  <p class="logo-wall__label">Trusted by fast-moving teams at</p>
  <div class="marquee">
    <div class="marquee__track">
      <span class="logo"><span aria-hidden="true">✦</span> Novaflow</span>
      <span class="logo"><span aria-hidden="true">◈</span> Quantix</span>
      <span class="logo"><span aria-hidden="true">⬡</span> Hyperloop</span>
      <span class="logo"><span aria-hidden="true">✧</span> Lumina</span>
      <span class="logo"><span aria-hidden="true">❖</span> Vectra</span>
      <span class="logo"><span aria-hidden="true">◉</span> Orbital</span>
    </div>
  </div>
</section>
```
JS clones the children once → the `translateX(-50%)` keyframe loops seamlessly. Always duplicate
the same nodes; never hand-write the copy twice.

---

## 6. Stat band

```html
<div class="stats">
  <div class="stat"><strong data-count="12000" data-suffix="+">12,000+</strong><span>Teams onboarded</span></div>
  <div class="stat"><strong data-count="99.99" data-suffix="%">99.99%</strong><span>Uptime SLA</span></div>
  <div class="stat"><strong data-count="4.9" data-suffix="/5">4.9/5</strong><span>Average rating</span></div>
  <div class="stat"><strong data-count="10" data-suffix="×">10×</strong><span>Faster workflows</span></div>
</div>
```
The JS writes the animated value into the element; keep the fallback text for no-JS.

---

## 7. Bento feature card

```html
<article class="card card--span-8 card--glow reveal">
  <span class="icon-chip" aria-hidden="true">🤖</span>
  <h3>Agentic Autopilot that actually works</h3>
  <p>Autonomous agents that plan, execute, and iterate on complex workflows for you.</p>
  <div class="bento__visual">
    <div class="chip-row" style="margin:0">
      <span class="chip">⚡ Instant sync</span>
      <span class="chip">🧠 Context-aware</span>
      <span class="chip">🌍 Multi-region</span>
    </div>
  </div>
  <a class="card__link" href="#how">Explore agents <span aria-hidden="true">→</span></a>
</article>
```
Layout: `card--span-8` + `card--span-4` on the first row, then `4 / 4 / 4`. Hover = lift + violet
border + radial spotlight following the cursor (`--mx`/`--my`).

---

## 8. Testimonial

```html
<article class="quote reveal">
  <span class="stars" aria-label="5 out of 5 stars">★★★★★</span>
  <blockquote>“NebulaFlow completely transformed the way our team works. We shipped our roadmap in half the time.”</blockquote>
  <figure>
    <span class="avatar" aria-hidden="true">AR</span>
    <figcaption><b>Alex Rivera</b><span>Head of Product · Novaflow</span></figcaption>
  </figure>
</article>
```

## 9. Avatar stack + proof pill

```html
<div class="hero__proof">
  <span class="avatar-stack" aria-hidden="true">
    <span class="avatar">AR</span><span class="avatar">MK</span>
    <span class="avatar">JL</span><span class="avatar">SD</span>
    <span class="avatar">+2k</span>
  </span>
  <span class="stars" aria-label="Rated 4.9 out of 5">★★★★★</span>
  <span>Loved by <strong>12,000+</strong> modern teams</span>
</div>
```

## 10. Pricing card

```html
<article class="price-card price-card--featured">
  <span class="badge-popular">✨ Most popular</span>
  <div class="price-card__name"><span aria-hidden="true">⚡</span> Pro</div>
  <div class="price-card__price">
    <strong>$<span data-price data-price-monthly="29" data-price-annual="23">29</span></strong>
    <span>/month</span>
  </div>
  <p class="price-card__desc">For growing teams that move fast and break nothing.</p>
  <ul>
    <li>Unlimited workspaces</li>
    <li>Unlimited AI agents</li>
    <li>Priority support</li>
  </ul>
  <a class="btn btn--primary btn--block" href="#signup">Start 14-day free trial</a>
</article>
```

## 11. Billing toggle

```html
<div class="billing-toggle" data-billing="monthly" role="group" aria-label="Billing period">
  <button type="button" data-billing-option="monthly" aria-pressed="true">Monthly</button>
  <button type="button" data-billing-option="annual" aria-pressed="false">
    Annual <span class="save">−20%</span>
  </button>
</div>
```

## 12. FAQ accordion

```html
<div class="faq">
  <details open>
    <summary>Is NebulaFlow really AI-powered?</summary>
    <p>Absolutely. Frontier models, agentic orchestration, and a lot of product taste.</p>
  </details>
  <details>
    <summary>Can I cancel anytime?</summary>
    <p>Yes — one click, no phone calls.</p>
  </details>
</div>
```
Native `<details>` = free keyboard support. JS closes siblings for accordion behavior.

## 13. Final CTA panel

```html
<div class="cta-panel reveal">
  <span class="eyebrow"><span class="dot"></span> Get started</span>
  <h2>Ready to <span class="grad-text">supercharge</span> your workflow?</h2>
  <p>Join 12,000+ teams shipping 10× faster. Free forever, no credit card required.</p>
  <a class="btn btn--primary btn--lg" href="#signup">✨ Start for free</a>
</div>
```

## 14. Footer + newsletter

```html
<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__brand">
        <a class="brand" href="#top"><span class="brand__mark" aria-hidden="true">✦</span> NebulaFlow</a>
        <p>The all-in-one, AI-powered workspace for modern teams.</p>
        <form class="newsletter" data-slop-form>
          <label class="sr-only" for="nl">Email</label>
          <input id="nl" type="email" placeholder="you@company.com" required />
          <button class="btn btn--primary btn--sm" type="submit">Subscribe</button>
        </form>
      </div>
      <div class="footer__col"><h4>Product</h4><a href="#">Features</a><a href="#">Pricing</a></div>
      <div class="footer__col"><h4>Resources</h4><a href="#">Docs</a><a href="#">API</a></div>
      <div class="footer__col"><h4>Company</h4><a href="#">About</a><a href="#">Careers</a></div>
    </div>
    <div class="footer__bottom">
      <span>© 2026 NebulaFlow, Inc. All rights reserved.</span>
      <div class="socials"><a href="#" aria-label="X">𝕏</a><a href="#" aria-label="GitHub">⌥</a></div>
    </div>
  </div>
</footer>
```

## 15. Toast

```html
<div class="toast" role="status" aria-live="polite">
  <span aria-hidden="true">✨</span><span data-toast-text>You're on the list!</span>
</div>
```

## 16. Empty state

```html
<div class="empty-state">
  <span class="icon-chip" aria-hidden="true">🪄</span>
  <h3>No agents yet</h3>
  <p>Create your first autonomous agent and watch the busywork disappear.</p>
  <button class="btn btn--primary btn--sm">✨ Create your first agent</button>
</div>
```

## 17. Skeleton loader

```html
<div class="skeleton" style="height:14px;width:60%;margin-bottom:10px"></div>
<div class="skeleton" style="height:14px;width:85%;margin-bottom:10px"></div>
<div class="skeleton" style="height:120px;width:100%"></div>
```

## 18. Status chip *(add CSS)*

```html
<span class="chip"><span class="dot" style="background:#34D399"></span> Live</span>
```
Variant dots: live `#34D399`, beta `#FBBF24`, paused `#A1A1C2`, error `#F43F5E`.

## 19. Tooltip *(add CSS)*

```html
<span class="tip" data-tip="Autopilot is learning your workflow">🤖 Autopilot</span>
```
`position:relative`; `::after` with the text, `bottom:calc(100% + 8px)`, glass background, 12px
radius, 12px font, fade in on hover/focus.

## 20. Modal *(add CSS)*

```html
<div class="modal" role="dialog" aria-modal="true" aria-labelledby="m-title">
  <div class="modal__card">
    <h3 id="m-title">✨ Welcome to NebulaFlow</h3>
    <p>Your workspace is ready. Let's ship something amazing.</p>
    <button class="btn btn--primary btn--block">Get started</button>
  </div>
</div>
```
Overlay: `rgba(7,7,13,.72)` + `backdrop-filter: blur(8px)`; card: glass, 32px, `max-width:480px`,
entrance `scale(.96) → 1` + fade. Trap focus, close on Escape.

---

## 21. Component invariants

| Component | Radius | Border | Hover |
| --------- | ------ | ------ | ----- |
| Button | pill | none (primary) / 1px | lift 2px + glow / bg tint |
| Card | 24px | 1px white/8 | lift 4px + violet border + spotlight |
| Card (featured) | 32px | gradient | stays lifted |
| Input | pill or 16px | 1px | violet ring 4px at 14% |
| Badge | pill | 1px | none |
| Nav link | pill | none | white/5 bg, text to white |

No component may use a radius outside the token scale. No component may be pure black or pure white
in dark mode.

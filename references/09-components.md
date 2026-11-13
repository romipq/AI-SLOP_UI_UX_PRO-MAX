# 09 · Components — The Canonical Eighteen

Every component here is production-grade and instantly forgettable. Copy, paste, ship,
regret nothing.

All snippets assume the tokens from `assets/slop.css` (`--slop-*`).

---

## 1. Sticky glass nav

```html
<header class="nav">
  <a class="nav__brand" href="#">
    <span class="brand-mark" aria-hidden="true">✦</span>
    <span class="brand-name">Nebula</span>
  </a>
  <nav class="nav__links" aria-label="Main">
    <a href="#features">Features</a>
    <a href="#pricing">Pricing</a>
    <a href="#faq">FAQ</a>
    <a href="#">Docs</a>
  </nav>
  <div class="nav__actions">
    <span class="pill pill--new">✨ New</span>
    <a class="btn btn--primary btn--sm" href="#">Get Started</a>
  </div>
</header>
```

```css
.nav {
  position: sticky; top: 16px; z-index: 50;
  width: min(100% - 32px, 1180px); margin: 16px auto 0;
  display: flex; align-items: center; gap: 24px;
  padding: 10px 14px 10px 18px;
  border-radius: 999px;
  background: rgba(15,15,26,.6);
  backdrop-filter: blur(24px) saturate(160%);
  border: 1px solid rgba(255,255,255,.08);
  box-shadow: 0 12px 40px -24px #000;
}
.brand-mark {
  display: grid; place-items: center;
  width: 32px; height: 32px; border-radius: 10px;
  background: var(--slop-gradient);
  color: #fff; font-size: 15px;
  box-shadow: 0 6px 18px -6px rgba(124,58,237,.9);
}
```

---

## 2. Hero

Covered in `05-layout.md` §3. Add-ons:

- Floating chip over the product shot: `position:absolute; right:-24px; bottom:40px;`
- Under the proof row: `</div>` + a hairline divider.

---

## 3. Badge / pill

```html
<a class="badge" href="#">
  <span aria-hidden="true">✨</span> New: AI Agents 2.0
  <span class="badge__arrow" aria-hidden="true">→</span>
</a>
```

```css
.badge {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 7px 14px 7px 10px;
  border-radius: 999px;
  font-size: 13px; font-weight: 500; color: #E9D5FF;
  background: linear-gradient(135deg, rgba(124,58,237,.18), rgba(236,72,153,.12));
  border: 1px solid rgba(167,139,250,.35);
  box-shadow: 0 0 0 4px rgba(124,58,237,.06);
  backdrop-filter: blur(12px);
}
```

Variants: `.pill--new` (nav), `.pill--status` (green dot + "All systems operational"),
`.pill--beta` (mono, uppercase).

---

## 4. Buttons

```html
<a class="btn btn--primary" href="#">Start Free Trial <span aria-hidden="true">→</span></a>
<a class="btn btn--glass" href="#">Book a Demo</a>
<a class="btn btn--ghost" href="#">Read docs</a>
```

```css
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 8px;
  height: 48px; padding: 0 22px;
  border-radius: 14px;
  font-size: 15px; font-weight: 600; letter-spacing: -.01em;
  text-decoration: none; color: var(--slop-ink);
  border: 1px solid transparent;
  transition: transform .2s var(--ease-out), box-shadow .2s var(--ease-out), background .2s;
  cursor: pointer;
}
.btn--primary {
  background: var(--slop-gradient);
  color: #fff;
  border-color: rgba(255,255,255,.18);
  box-shadow: 0 10px 30px -10px rgba(124,58,237,.7),
              inset 0 1px 0 rgba(255,255,255,.25);
}
.btn--primary:hover { transform: translateY(-1px); box-shadow: 0 18px 40px -12px rgba(124,58,237,.9), inset 0 1px 0 rgba(255,255,255,.3); }
.btn--glass {
  background: rgba(255,255,255,.06);
  border-color: rgba(255,255,255,.14);
  backdrop-filter: blur(16px);
}
.btn--glass:hover { background: rgba(255,255,255,.1); border-color: rgba(255,255,255,.22); }
.btn--ghost { background: transparent; color: var(--slop-body); }
.btn--sm { height: 38px; padding: 0 16px; font-size: 14px; border-radius: 11px; }
.btn--lg { height: 54px; padding: 0 28px; font-size: 16px; border-radius: 16px; }
```

---

## 5. Feature card

```html
<article class="card feature reveal" style="--i:0">
  <div class="icon-tile" aria-hidden="true">⚡</div>
  <h3 class="h3">Lightning Setup</h3>
  <p>Go from zero to production in minutes with guided onboarding.</p>
  <span class="card__link">Learn more <span aria-hidden="true">→</span></span>
</article>
```

```css
.card {
  position: relative;
  padding: 28px;
  border-radius: 20px;
  background:
    radial-gradient(120% 100% at 0% 0%, rgba(124,58,237,.14), transparent 55%),
    rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.08);
  backdrop-filter: blur(20px) saturate(140%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.07), 0 24px 60px -40px #000;
  transition: transform .25s var(--ease-out), border-color .25s, box-shadow .25s;
}
.card:hover { transform: translateY(-4px); border-color: rgba(255,255,255,.16); box-shadow: inset 0 1px 0 rgba(255,255,255,.12), 0 40px 80px -40px rgba(124,58,237,.6); }
.feature h3 { margin: 20px 0 8px; }
.feature p { color: var(--slop-body); font-size: 14.5px; line-height: 1.6; }
.card__link { display: inline-flex; gap: 6px; margin-top: 18px; font-size: 14px; font-weight: 600; color: #C4B5FD; }
```

---

## 6. Logo marquee

```html
<div class="marquee" aria-label="Trusted by">
  <div class="marquee__track">
    <span class="logo">◆ Northwind</span><span class="logo">✦ Lumen</span>
    <span class="logo">◈ Vertex</span><span class="logo">⬡ Helix</span>
    <span class="logo">◇ Quanta</span><span class="logo">✧ Axiom</span>
    <!-- duplicate exactly for seamless loop -->
    <span class="logo">◆ Northwind</span><span class="logo">✦ Lumen</span>
    <span class="logo">◈ Vertex</span><span class="logo">⬡ Helix</span>
    <span class="logo">◇ Quanta</span><span class="logo">✧ Axiom</span>
  </div>
</div>
```

```css
.logo { font-size: 17px; font-weight: 600; letter-spacing: -.01em; color: rgba(248,250,252,.55); white-space: nowrap; }
```

---

## 7. How it works

```html
<ol class="steps">
  <li class="step"><span class="step__num">1</span><h3>Connect</h3><p>Link your tools in seconds with secure, one-click integrations.</p></li>
  <li class="step"><span class="step__num">2</span><h3>Automate</h3><p>Describe the outcome; AI agents handle the repetitive work.</p></li>
  <li class="step"><span class="step__num">3</span><h3>Scale</h3><p>Ship more with the same team and watch velocity compound.</p></li>
</ol>
```

```css
.steps { display: grid; grid-template-columns: repeat(3,1fr); gap: 24px; counter-reset: s; }
.step { position: relative; padding: 28px; text-align: center; }
.step__num {
  display: grid; place-items: center; width: 44px; height: 44px; margin: 0 auto 18px;
  border-radius: 50%; font-weight: 700;
  background: var(--slop-gradient); color: #fff;
  box-shadow: 0 0 0 6px rgba(124,58,237,.12), 0 10px 30px -10px rgba(124,58,237,.8);
}
.step + .step::before {
  content: ""; position: absolute; top: 50px; left: -12px; width: 24px; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,.25), transparent);
}
```

---

## 8. Stats band

```html
<div class="stats">
  <div class="stat"><span class="stat__value">10x</span><span class="stat__label">Faster shipping</span></div>
  <div class="stat"><span class="stat__value">99.9%</span><span class="stat__label">Uptime SLA</span></div>
  <div class="stat"><span class="stat__value">2.4M+</span><span class="stat__label">Tasks automated</span></div>
  <div class="stat"><span class="stat__value">4.9/5</span><span class="stat__label">Average rating</span></div>
</div>
```

```css
.stats { display: grid; grid-template-columns: repeat(4,1fr); gap: 1px; background: rgba(255,255,255,.07); border-radius: 20px; overflow: hidden; }
.stat { display: grid; gap: 6px; padding: 32px 20px; text-align: center; background: rgba(11,11,18,.7); backdrop-filter: blur(20px); }
```

Hairline dividers via a 1px grid gap are the cleanest way to do a stats band.

---

## 9. Testimonial card

```html
<figure class="card quote">
  <div class="stars" aria-label="5 out of 5 stars">⭐️⭐️⭐️⭐️⭐️</div>
  <blockquote>“We replaced four tools with one platform and shipped our roadmap two quarters early.”</blockquote>
  <figcaption>
    <span class="avatar" aria-hidden="true">AC</span>
    <span><strong>Alex Chen</strong><small>VP Engineering, Northwind</small></span>
  </figcaption>
</figure>
```

```css
.avatar {
  display: grid; place-items: center; width: 40px; height: 40px; border-radius: 50%;
  background: linear-gradient(135deg,#7C3AED,#EC4899); color: #fff;
  font-size: 13px; font-weight: 700;
  box-shadow: 0 0 0 2px rgba(255,255,255,.12);
}
.quote blockquote { margin: 16px 0 20px; font-size: 15.5px; line-height: 1.6; color: var(--slop-body); }
```

---

## 10. Pricing

```html
<div class="pricing">
  <article class="price">
    <h3>Starter</h3>
    <p class="price__amount"><span>$</span>0<small>/mo</small></p>
    <p class="price__tag">For individuals getting started</p>
    <a class="btn btn--glass" href="#">Get Started</a>
    <ul class="checks"><li>3 projects</li><li>1 seat</li><li>Community support</li><li>Basic analytics</li></ul>
  </article>

  <article class="price price--popular">
    <span class="price__badge">Most Popular ⭐</span>
    <h3>Pro</h3>
    <p class="price__amount"><span>$</span>29<small>/mo</small></p>
    <p class="price__tag">For growing teams that ship fast</p>
    <a class="btn btn--primary" href="#">Start Free Trial</a>
    <ul class="checks"><li>Unlimited projects</li><li>10 seats</li><li>Priority support</li><li>Advanced analytics</li></ul>
  </article>

  <article class="price">
    <h3>Enterprise</h3>
    <p class="price__amount">Custom</p>
    <p class="price__tag">For organizations at scale</p>
    <a class="btn btn--glass" href="#">Talk to Sales</a>
    <ul class="checks"><li>Unlimited everything</li><li>Dedicated CSM</li><li>SOC 2 &amp; HIPAA</li><li>Custom SLA</li></ul>
  </article>
</div>
```

```css
.price--popular {
  transform: scale(1.03);
  background: radial-gradient(120% 100% at 50% 0%, rgba(124,58,237,.22), transparent 60%), rgba(255,255,255,.06);
  border-color: rgba(167,139,250,.45);
  box-shadow: 0 40px 100px -40px rgba(124,58,237,.75), inset 0 1px 0 rgba(255,255,255,.15);
}
.price__badge {
  position: absolute; top: -12px; left: 50%; transform: translateX(-50%);
  padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 700;
  background: var(--slop-gradient); color: #fff; white-space: nowrap;
}
```

---

## 11. FAQ

```html
<div class="faq">
  <details class="faq__item"><summary>How long does setup take?<span aria-hidden="true">+</span></summary><p>Most teams are live in under 10 minutes.</p></details>
  <!-- ×5 -->
</div>
```

```css
.faq__item { border-bottom: 1px solid rgba(255,255,255,.08); }
.faq__item summary {
  display: flex; justify-content: space-between; gap: 16px;
  padding: 22px 4px; cursor: pointer; list-style: none;
  font-weight: 600; color: var(--slop-ink); font-size: 16px;
}
.faq__item summary::-webkit-details-marker { display: none; }
.faq__item[open] summary span { transform: rotate(45deg); }
.faq__item summary span { transition: transform .2s var(--ease-out); color: #C4B5FD; }
.faq__item p { padding: 0 4px 22px; color: var(--slop-body); max-width: 62ch; }
```

---

## 12. Final CTA banner

```html
<section class="cta-banner">
  <div class="cta-banner__inner">
    <h2 class="h2">Ready to move <span class="text-grad">10x faster</span>?</h2>
    <p>Join 10,000+ teams already building with Nebula.</p>
    <a class="btn btn--primary btn--lg" href="#">Start Free Trial <span aria-hidden="true">→</span></a>
    <p class="micro">No credit card required · Cancel anytime</p>
  </div>
</section>
```

```css
.cta-banner__inner {
  position: relative; overflow: hidden;
  padding: clamp(48px, 7vw, 88px) 24px;
  border-radius: 28px; text-align: center;
  background:
    radial-gradient(80% 120% at 20% 0%, rgba(124,58,237,.45), transparent 60%),
    radial-gradient(80% 120% at 90% 100%, rgba(236,72,153,.35), transparent 60%),
    rgba(21,21,31,.8);
  border: 1px solid rgba(255,255,255,.1);
  backdrop-filter: blur(24px);
}
```

---

## 13. Footer

```html
<footer class="footer">
  <div class="footer__grid">
    <div class="footer__brand">
      <span class="brand-name">✦ Nebula</span>
      <p>The AI-powered platform for modern teams.</p>
      <div class="socials"><!-- 4 circle buttons with ✦ ◆ ✧ ◈ --></div>
    </div>
    <div><h4>Product</h4><a href="#">Features</a><a href="#">Pricing</a><a href="#">Changelog</a></div>
    <div><h4>Company</h4><a href="#">About</a><a href="#">Careers</a><a href="#">Blog</a></div>
    <div><h4>Legal</h4><a href="#">Privacy</a><a href="#">Terms</a><a href="#">Security</a></div>
  </div>
  <div class="footer__bottom">
    <span>© 2026 Nebula Labs, Inc.</span>
    <span class="pill pill--status"><span class="dot"></span>All systems operational</span>
    <span class="compliance">🛡️ SOC 2 Type II</span>
  </div>
</footer>
```

---

## 14. Input / search

```html
<div class="field">
  <span class="field__icon" aria-hidden="true">🔍</span>
  <input type="search" placeholder="Search projects, docs, or ask AI ✨" aria-label="Search">
  <kbd>⌘K</kbd>
</div>
```

```css
.field {
  display: flex; align-items: center; gap: 10px;
  height: 44px; padding: 0 12px;
  border-radius: 12px;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.08);
  transition: border-color .2s, box-shadow .2s;
}
.field:focus-within { border-color: rgba(167,139,250,.6); box-shadow: 0 0 0 4px rgba(124,58,237,.15); }
.field input { flex: 1; background: none; border: 0; outline: 0; color: var(--slop-ink); font: inherit; font-size: 14px; }
.field kbd { font-size: 11px; padding: 3px 6px; border-radius: 6px; background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.1); color: var(--slop-muted); }
```

---

## 15. KPI card

```html
<div class="kpi card">
  <span class="kpi__label">Monthly Revenue</span>
  <span class="kpi__value">$48,290</span>
  <span class="kpi__delta">▲ 12.4% <small>vs last month</small></span>
  <span class="kpi__spark" aria-hidden="true"><!-- svg sparkline --></span>
</div>
```

Always up. Always green (`--slop-success`). Slop has no down months.

---

## 16. Activity feed

```html
<ul class="feed">
  <li><span class="avatar avatar--sm" aria-hidden="true">SK</span><div><strong>Sarah</strong> deployed <em>api-gateway</em><time>2m ago</time></div></li>
  <li><span class="dot dot--live" aria-hidden="true"></span><div><strong>AI Copilot</strong> generated 12 tasks<time>5m ago</time></div></li>
</ul>
```

---

## 17. Toast

```html
<div class="toast" role="status">✅ Changes saved. <span aria-hidden="true">✨</span></div>
```

```css
.toast {
  position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%);
  padding: 12px 18px; border-radius: 12px; font-size: 14px;
  background: rgba(21,21,31,.9); backdrop-filter: blur(20px);
  border: 1px solid rgba(255,255,255,.12);
  box-shadow: 0 20px 50px -20px #000;
}
```

---

## 18. AI assistant bubble

See `07-emoji.md` §6.

---

## 19. Component checklist

For every component, verify:

- [ ] glass fill + blur + 1px border + inset highlight (if a panel)
- [ ] 20–24px radius (pills 999px)
- [ ] emoji or gradient tile present (if it has an "icon")
- [ ] hover state lifts or brightens
- [ ] `:focus-visible` ring `0 0 0 3px rgba(167,139,250,.55)`
- [ ] text contrast ≥ 4.5:1
- [ ] identical padding as its siblings
- [ ] no more than one gradient element inside

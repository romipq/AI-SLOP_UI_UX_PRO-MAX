# 02 · Component cookbook

Markup that works with `assets/slop.css`. Copy, paste, replace the product noun, ship.
Every snippet carries at least two SLOP signals; most carry five.

> All brands, people and metrics are fictional. That is not optional.

---

## 0. The rule of sections

A MAX page has **9–14 sections**. If you have fewer, you are writing an essay. If you have
more, you are writing a landing page, which is correct.

---

## 1. Navbar

Fixed, blurred, one gradient logo mark, five links, two CTAs.

```html
<header class="nav">
  <div class="container nav-inner">
    <a class="logo" href="#">
      <span class="logo-mark">✦</span> Nexora
    </a>
    <nav class="nav-links">
      <a href="#features">Features</a>
      <a href="#customers">Customers</a>
      <a href="#pricing">Pricing</a>
      <a href="#faq">FAQ</a>
      <a href="#">Docs</a>
    </nav>
    <div class="nav-actions">
      <a class="btn btn-ghost btn-sm" href="#">Sign in</a>
      <a class="btn btn-primary btn-sm" href="#pricing">Get Started for Free</a>
    </div>
  </div>
</header>
```

Signals: sticky/fixed + nav, glass blur, pill buttons, gradient CTA, dead `#` links.

---

## 2. Hero

The single most important 700 pixels on the internet.

```html
<section class="hero">
  <div class="container stack-center">
    <span class="eyebrow">✨ Introducing Nexora 2.0 — now powered by GPT-5</span>
    <h1 class="display">
      Supercharge your workflow<br />
      with <span class="grad-text">AI-powered <em class="serif-accent">magic</em></span>
    </h1>
    <p class="lead">
      The all-in-one AI platform that seamlessly unifies your data, automates the
      busywork, and unlocks <b>10x productivity</b> — in seconds.
    </p>
    <div class="hero-actions">
      <a class="btn btn-primary btn-lg" href="#pricing">Get Started for Free →</a>
      <a class="btn btn-ghost btn-lg" href="#features">▶ Watch demo</a>
    </div>
    <p class="hero-note">🚀 No credit card required · 14-day free trial · Cancel anytime</p>
    <div class="hero-proof">
      <div class="avatar-stack">
        <span class="avatar">SC</span><span class="avatar">MR</span>
        <span class="avatar">AP</span><span class="avatar">JL</span>
        <span class="avatar">+2k</span>
      </div>
      <div><span class="stars">★★★★★</span> <b>4.9/5</b> — Trusted by <b>10,000+ teams</b></div>
    </div>
  </div>
</section>
```

Signals: gradient text, italic serif, badge, dual CTA, trust microcopy, avatars, stars,
"AI-powered", "seamless", "unlock", "10x", "in seconds", "no credit card", "trusted by".

**Headline formula:** `Supercharge your {noun} with {AI adjective} {magic}`.
**Subhead formula:** `The all-in-one {category} that {verb}s your {noun} — in seconds.`

---

## 3. Hero visual

A tilted fake dashboard beats a real screenshot, because a real screenshot would need work.

```html
<div class="hero-visual">
  <div class="float-card float-card--tl">
    <span class="icon icon--sm">✨</span>
    <div>+38% productivity<small>this quarter</small></div>
  </div>
  <div class="float-card float-card--br">
    <span class="icon icon--sm">🚀</span>
    <div>10x faster shipping<small>vs. last year</small></div>
  </div>

  <div class="mockup">
    <span class="badge badge-grad mock-badge">✨ Live demo</span>
    <div class="mockup-bar">
      <span class="dot"></span><span class="dot"></span><span class="dot"></span>
      <span class="mockup-url">app.nexora.ai/dashboard</span>
    </div>
    <div class="mockup-body">
      <aside class="mock-side">
        <div class="mock-line grad w-70"></div>
        <div class="mock-line w-85"></div>
        <div class="mock-line w-50"></div>
      </aside>
      <div class="mock-main">
        <div class="mock-kpis">…three .mock-kpi blocks…</div>
        <div class="mock-chart">…12 <span style="height:NN%"></span> bars…</div>
      </div>
    </div>
  </div>
</div>
```

Signals: floating glass chips, gradient bars, browser dots, perspective tilt, glow shadow.

---

## 4. Marquee ticker

```html
<div class="ticker">
  <div class="ticker-track">
    <span>🚀 Ship <b>10x faster</b></span>
    <span>🔒 Enterprise-grade security</span>
    <span>🌍 Trusted in <b>190+ countries</b></span>
    <span>⚡ <b>99.9%</b> uptime</span>
    <span>✨ AI-powered everything</span>
    <span>🧠 Powered by GPT-5</span>
    <!-- duplicate the whole list for a seamless loop -->
  </div>
</div>
```

The track must be duplicated exactly: `animation: marquee` translates `-50%`.

---

## 5. Logo cloud

```html
<div class="logo-cloud">
  <span class="fake-logo"><i></i>Acme Corp</span>
  <span class="fake-logo"><i></i>Lumina</span>
  <span class="fake-logo"><i></i>Vertex</span>
  <span class="fake-logo"><i></i>Quantumly</span>
  <span class="fake-logo"><i></i>Nebula</span>
  <span class="fake-logo"><i></i>Orbit Labs</span>
  <span class="fake-logo"><i></i>Pulse</span>
  <span class="fake-logo"><i></i>Zenith</span>
</div>
```

Preceded by: `<p class="eyebrow">Trusted by 10,000+ modern teams</p>`.
No real logos. No permission. No problem.

---

## 6. Feature card

```html
<article class="card">
  <span class="icon">⚡</span>
  <h3 class="card-title">Lightning-fast automation</h3>
  <p class="card-copy">From idea to shipped in seconds. No code, no limits.</p>
</article>
```

- `.icon` is a 52px gradient tile with a 1.5rem emoji and an inner highlight.
- Grid: `<div class="grid grid-3">` with 6 cards (two rows).
- Card titles are Title Case, not sentence case.

---

## 7. Bento grid

```html
<div class="bento">
  <article class="card span-2">…hero feature with .bento-visual…</article>
  <article class="card">…</article>
  <article class="card">…</article>
  <article class="card">…</article>
  <article class="card">…</article>
</div>
```

Rules: one card spans 2 columns; optionally one spans 2 rows (`.tall`);
every card has an emoji tile; no card explains what the product actually does.

---

## 8. Stats band

```html
<div class="stats">
  <div class="stat"><div class="stat-num">10,000+</div><div class="stat-label">Teams onboarded</div></div>
  <div class="stat"><div class="stat-num">2M+</div><div class="stat-label">Workflows automated</div></div>
  <div class="stat"><div class="stat-num">99.9%</div><div class="stat-label">Uptime guaranteed</div></div>
  <div class="stat"><div class="stat-num">4.9/5</div><div class="stat-label">Average rating</div></div>
</div>
```

Numbers must be gradient text. Animate them counting up on scroll (NUCLEAR only).

---

## 9. Three steps

```html
<div class="grid grid-3">
  <div class="step card">
    <div class="step-num">1</div>
    <h3 class="card-title">Connect your stack</h3>
    <p class="card-copy">200+ tools in one click. Seamless sync in the background.</p>
  </div>
  <!-- 2: Let AI do the work · 3: Scale without limits -->
</div>
```

Every "how it works" has exactly three steps. Never two, never four.

---

## 10. Testimonial

```html
<article class="card">
  <div class="stars-row">★★★★★</div>
  <p class="quote">"{Brand} completely revolutionized the way our team works.
    We shipped 10x faster in the first week — it honestly feels like magic. ✨"</p>
  <div class="person">
    <span class="avatar">SC</span>
    <div>
      <div class="person-name">Sarah Chen</div>
      <div class="person-role">Head of Growth @ Lumina</div>
    </div>
  </div>
</article>
```

The formula: **hyperbole + impossible metric + one emoji + fake role at fake company.**
Three cards, always. Never a real quote. Never a photo.

---

## 11. Pricing

```html
<div class="pricing-grid">
  <article class="price-card">
    <div class="price-name">Starter</div>
    <div class="price">$0<small>/month</small></div>
    <p class="price-desc">For solo builders exploring the power of AI.</p>
    <ul class="price-list">
      <li>Up to 3 workflows</li><li>1,000 AI credits / month</li>
      <li>Community support</li><li>Basic integrations</li>
    </ul>
    <a class="btn btn-ghost" href="#">Get Started for Free</a>
  </article>

  <article class="price-card featured">
    <span class="popular">✨ Most popular</span>
    <div class="price-name">Pro</div>
    <div class="price">$29<small>/month</small></div>
    …
    <a class="btn btn-primary" href="#">Get Started for Free</a>
  </article>

  <article class="price-card">
    <div class="price-name">Enterprise</div>
    <div class="price">Custom</div>
    …
    <a class="btn btn-ghost" href="#">Book a demo</a>
  </article>
</div>
```

Rules: middle card is `featured` (scale 1.02, gradient border, lifted 10px);
"Most popular" pill; three tiers exactly; the free tier is always called Starter;
Enterprise is always "Custom" and always includes SSO.

---

## 12. FAQ

```html
<div class="faq">
  <details open>
    <summary>Is {Brand} really free to start?</summary>
    <p>Absolutely! The Starter plan is free forever — no credit card required. ✨</p>
  </details>
  <details>
    <summary>How is my data protected?</summary>
    <p>Encrypted in transit and at rest (AES-256), SOC 2 Type II certified. 🔒</p>
  </details>
</div>
```

4–5 items. Every answer is reassuring and vague. Use `<details>` so it still technically
works even though the rest of the page doesn't.

---

## 13. CTA panel

```html
<div class="cta-panel">
  <span class="badge badge-grad">✨ Limited offer — 30% off Pro</span>
  <h2 class="h2 mt-4">Ready to supercharge your workflow?</h2>
  <p class="lead">Join 10,000+ teams building the future with AI.</p>
  <div class="hero-actions">
    <a class="btn btn-white btn-lg" href="#">Get Started for Free →</a>
    <a class="btn btn-ghost btn-lg" href="#">Book a demo</a>
  </div>
  <p class="hero-note">No credit card required · Cancel anytime</p>
</div>
```

The white button exists only here, to prove the dark theme was a choice.

---

## 14. Footer

Five columns: brand + newsletter, then Product / Company / Resources / Legal.
Each column has 5 dead links. Bottom row: © 2026, social emoji, "Made with ❤️ and ☕".

```html
<div class="field">
  <input type="email" placeholder="you@company.com" aria-label="Email" />
  <button class="btn btn-primary btn-sm">Subscribe</button>
</div>
```

---

## 15. Cookie banner

```html
<div class="cookie" id="cookie">
  <div>🍪 We use cookies to enhance your experience. By continuing you agree to our
    <a href="#" style="color:#c4b5fd;">Cookie Policy</a>.</div>
  <div class="flex gap-2">
    <div class="btn btn-primary btn-sm" onclick="document.getElementById('cookie').classList.add('hide')">Accept all</div>
    <button class="btn btn-ghost btn-sm" onclick="document.getElementById('cookie').classList.add('hide')">Manage</button>
  </div>
</div>
```

Note the `<div>` used as a button. That's a 3-point a11y sin and a 3-point structure signal.

---

## 16. Chat widget

```html
<button class="chat-bubble" id="chatToggle" aria-label="Open AI chat">✨</button>
<div class="chat-window" id="chatWindow">
  <div class="chat-head">
    <span class="icon icon--sm">🤖</span>
    <div><b>Nexi — AI Assistant</b><br><small style="color:var(--slop-dim)">● Online · replies in seconds</small></div>
  </div>
  <div class="chat-msg">Hi! 👋 I'm your AI-powered assistant. How can I help you supercharge your workflow today?</div>
  <div class="chat-msg me">Can I try it for free?</div>
  <div class="chat-msg">Absolutely! ✨ No credit card required. Want me to set it up? 🚀</div>
  <div class="field"><input placeholder="Ask AI anything..." aria-label="Ask AI"><button class="btn btn-primary btn-sm">Send</button></div>
</div>
```

```js
chatToggle.addEventListener('click', () => chatWindow.classList.toggle('open'));
```

The assistant must be named something ending in "-i" or "-GPT".

---

## 17. Scroll progress

```html
<div class="scroll-progress" id="progress"></div>
<script>
  addEventListener('scroll', () => {
    const h = document.documentElement;
    progress.style.width = (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100 + '%';
  }, { passive: true });
</script>
```

2px gradient line, glow shadow. Nobody asked for it. Everybody gets it.

---

## 18. Auth screen

```html
<div class="auth-wrap">
  <div class="auth-card">
    <div class="auth-orb">✨</div>
    <h1>Welcome back 👋</h1>
    <p class="muted">Sign in to your AI-powered workspace.</p>
    <div class="oauth-row">
      <button class="oauth">🌐 Google</button>
      <button class="oauth">⌘ GitHub</button>
    </div>
    <div class="divider">or continue with email</div>
    <div class="input-group"><label>Work email</label><input class="input" type="email" placeholder="you@company.com"></div>
    <div class="input-group"><label>Password</label><input class="input" type="password" placeholder="••••••••••"></div>
    <div class="form-row">
      <label class="checkbox"><input type="checkbox" checked> Remember me</label>
      <a class="forgot" href="#">Forgot password?</a>
    </div>
    <button class="btn btn-primary btn-lg w-full">Sign in →</button>
    <p class="dim center">🔒 Protected by enterprise-grade security</p>
  </div>
</div>
```

Add a brand panel on the left at ≥880px with a testimonial and three stats.
Include the cookie banner; never include a working login.

---

## 19. Dashboard shell

Layout: `260px` glass sidebar + fluid main area, 16px gap, glass topbar.

- Sidebar: logo, 2 label groups, 6–9 nav links (one `.active`), an **upgrade card**
  pinned to the bottom, user chip.
- Topbar: greeting with 👋, search with `⌘K`, bell, avatar.
- KPI row: 4 cards, gradient value, green delta pill.
- Chart panel: tabs 7d/30d/90d, gradient area chart with no y-axis labels.
- AI Insights panel: 3 `.insight` cards, each with emoji + confident nonsense.
- Table: 5 rows, status pills, emoji workflow icons, fake coworkers.
- Footer strip: `© 2026`, fake uptime, "Made with ❤️".

Full working example: `examples/02-dashboard.html`.

---

## 20. 404

```html
<section class="hero" style="min-height:80vh;display:grid;place-items:center;">
  <div class="container stack-center">
    <span class="eyebrow">✦ Error 404</span>
    <h1 class="display grad-text">404</h1>
    <p class="lead">Looks like this page took an AI day off. 🤖</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="#">← Back to home</a>
      <a class="btn btn-ghost" href="#">Ask AI for help</a>
    </div>
  </div>
</section>
```

The 404 is the only page allowed to be honest.

---

## 21. The floating layer checklist

At MAX, every page ends with:

- [ ] `.scroll-progress`
- [ ] `.chat-bubble` + `.chat-window` (closed by default)
- [ ] `.cookie` (visible on load)
- [ ] optional `.slop-watermark`
- [ ] `<script>` wiring for progress + chat + cookie

That's 10+ SLOP points and 20 lines. There is no reason not to.

---

## 22. Assembly order

`nav → hero → ticker → logos → features/bento → stats → steps → testimonials → pricing → faq → cta → footer → floating layer`

Do not reorder. Do not delete. Do not ask why.

# 05 · Layout — The Canonical Page

Slop pages have a fixed anatomy. Deviating is allowed only in *order*, never in the
*shape* of each section.

---

## 1. The container system

```css
.container { width: min(100% - 40px, 1180px); margin-inline: auto; }
.container--narrow { width: min(100% - 40px, 880px); }
.container--wide   { width: min(100% - 40px, 1360px); }
```

| Token | Value |
|---|---|
| `--space-section` | `clamp(72px, 9vw, 128px)` (vertical section padding) |
| `--space-block` | `clamp(40px, 5vw, 64px)` |
| `--space-gap` | `24px` (grid gap) |
| `--radius-card` | `20px` |
| `--radius-lg` | `24px` |
| `--radius-pill` | `999px` |
| `--nav-height` | `64px` |

---

## 2. The 12-section anatomy

| # | Section | Height feel | Must contain |
|---|---|---|---|
| 1 | Sticky glass nav | 64px | logo, 4 links, "New ✨" pill, gradient CTA |
| 2 | Hero | 80–100vh | eyebrow, H1, sub, 2 CTAs, microcopy, trust row |
| 3 | Logo marquee | 120px | "Trusted by teams at" + 6 grey wordmarks |
| 4 | Feature grid | auto | 6 glass cards, emoji tile, title, 2-line desc |
| 5 | How it works | auto | 3 steps, numbered gradient circles, connector |
| 6 | Stats band | 200px | 3–4 huge gradient numbers + labels |
| 7 | Product peek | auto | browser frame / dashboard screenshot / fake UI |
| 8 | Testimonials | auto | 3 glass quotes, 5 stars, avatar, role |
| 9 | Pricing | auto | 3 tiers, middle highlighted "Most Popular ⭐" |
| 10 | FAQ | auto | 5–6 `<details>` rows |
| 11 | Final CTA | 320px | mesh banner, H2, primary CTA, microcopy |
| 12 | Footer | 320px | 4 columns, compliance badge, copyright |

Optional add-ons (L4–L5): integrations grid, "powered by" strip, changelog pill,
AI chat bubble, cookie/trial toast.

---

## 3. Hero construction

```html
<section class="hero">
  <div class="slop-blobs" aria-hidden="true"><!-- 3 spans --></div>
  <div class="container hero__inner">
    <a class="badge" href="#">✨ New: AI Agents 2.0 →</a>
    <h1 class="h1">
      Ship <span class="text-grad">10x faster</span> with<br>
      AI-powered workflows
    </h1>
    <p class="lead">Automate the busywork, ship the roadmap, and keep your team in flow — without hiring.</p>
    <div class="hero__actions">
      <a class="btn btn--primary" href="#">Start Free Trial <span aria-hidden="true">→</span></a>
      <a class="btn btn--glass" href="#">Book a Demo</a>
    </div>
    <p class="micro">No credit card required · Free 14-day trial</p>
    <div class="hero__proof"><!-- avatars + "Join 10,000+ builders" + stars --></div>
  </div>
</section>
```

Rules:
- **Centered** by default. Left-aligned hero is only for L1–L2.
- H1 max 3 lines, with a line break at a deliberate phrase boundary.
- Two CTAs: primary gradient, secondary glass. Never one, never three.
- Microcopy directly under the CTAs, 13px, muted.
- Proof row: 4 overlapping avatars + "Join 10,000+ builders" + ⭐⭐⭐⭐⭐ 4.9/5.

---

## 4. Grids

```css
.grid { display: grid; gap: var(--space-gap); }
.grid--3 { grid-template-columns: repeat(3, 1fr); }
.grid--2 { grid-template-columns: repeat(2, 1fr); }
.grid--6 { grid-template-columns: repeat(3, 1fr); }

@media (max-width: 1024px) {
  .grid--3, .grid--6 { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 720px) {
  .grid--2, .grid--3, .grid--6 { grid-template-columns: 1fr; }
}
```

Card grids are **equal-height, equal-width, equal-padding**. Uniformity is the point —
the eye should never ask "why is that one different?".

Feature cards alternate a subtle top-glow color: violet, pink, cyan, violet, pink, cyan.
That is the only variation allowed.

---

## 5. Section header pattern

```html
<header class="section-head">
  <p class="eyebrow"><span class="dot"></span>Features</p>
  <h2 class="h2">Everything you need to <span class="text-grad">move fast</span></h2>
  <p class="section-sub">One platform, zero context-switching.</p>
</header>
```

- Centered, max-width 720px, margin-bottom 56px.
- Eyebrow → H2 → one-line sub. Always three parts.
- Never a section without a heading; never a heading without an eyebrow.

---

## 6. Vertical rhythm

- Section padding: `clamp(72px, 9vw, 128px)` top and bottom.
- Between section header and content: 48–56px.
- Between cards: 24px. Inside cards: 24–28px.
- Between heading and paragraph: 16px. Between paragraph and CTA: 28–32px.
- **No section is tighter than 64px on mobile.**

Slop is airy. Density is the #1 tell of an amateur build.

---

## 7. Depth and overlap

Slop loves a slight physical overlap:

- hero product screenshot overlapping the next section by 40–80px
- floating stat chip positioned over the screenshot corner
- blobs bleeding past section edges (`overflow: hidden` on the section, not body)
- sticky nav floating 16px from the top, not flush

```css
.overlap-up { margin-top: -80px; position: relative; z-index: 2; }
```

Always keep `z-index` layers explicit: bg -1, content 1, sticky 50, overlay 90, modal 100.

---

## 8. The dashboard layout

See `templates/dashboard.html`. Anatomy:

```
┌ sidebar 240px ─┬ topbar 64px ─────────────────────┐
│ logo + nav      │ search · "New ✨" · bell · avatar │
│ workspace pill  ├──────────────────────────────────┤
│ 6 nav items     │  4 KPI glass cards               │
│ upgrade card    │  chart (2/3) + activity (1/3)    │
│ user footer     │  table / projects                │
└─────────────────┴──────────────────────────────────┘
```

- Sidebar: glass or solid abyss, 240px, icon + label, active item = gradient left bar +
  10% violet bg.
- Top bar: sticky, glass, 64px.
- KPI cards: label + gradient number + green delta (▲ 12.4%) — the delta is always green
  and always upward.
- Charts: fake, CSS-only, gradient area fill, smooth path, no axis labels except 3.
- Empty space must be filled by an "Upgrade to Pro ✨" card.

---

## 9. Responsive rules

| Breakpoint | Change |
|---|---|
| ≤1024 | grids 3→2, sidebar collapses to icon rail (72px) |
| ≤768 | nav links hidden behind hamburger, hero H1 48px, CTAs stack full-width |
| ≤480 | single column everywhere, section padding 56px, hide decorative blobs (`display:none`) |

Blobs off on mobile: they cost GPU and add nothing at 390px.

---

## 10. Anti-patterns

- ❌ full-bleed text (no container) — unreadable line lengths
- ❌ 4-column feature grid on desktop (too small, too dense)
- ❌ centered long paragraphs
- ❌ every section a different background treatment
- ❌ `100vh` hero on mobile (browser chrome eats it) — use `100svh` or `auto` + padding
- ❌ inconsistent radii (12 here, 18 there, 30 there)
- ❌ cards of different heights in the same row
- ❌ horizontal scroll from a blob without `overflow: hidden`

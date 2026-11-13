# 03 — Layout Recipes

Section order is 50% of the aesthetic. The AI-generated landing page has a *canonical* sequence;
deviating is allowed only if you keep the rhythm (hero → proof → features → proof → price → FAQ →
CTA → footer).

Global measurements:

```
Container      1200px (1320 wide variant), gutter clamp(20px,4vw,40px)
Section padding clamp(72px,10vw,128px)
Grid           12 columns, 18–24px gaps
Breakpoints    560 / 860 / 980 / 1200
Nav height     68px sticky, blurred after 12px scroll
```

---

## 1. SaaS landing page (the canonical slop page)

| # | Section | Height | Contents | Notes |
| - | ------- | ------ | -------- | ----- |
| 1 | Sticky nav | 68px | ✦ wordmark · 5 links · Sign in · gradient CTA | glass on scroll |
| 2 | Hero | 780–900px | pill, H1 w/ gradient, subhead, dual CTA, meta row, proof pill, app mockup | orbs + grid + mesh behind |
| 3 | Logo marquee | 140px | "Trusted by fast-moving teams at" + 8 fake brands | infinite scroll, edge mask |
| 4 | Stats band | 130px | 4 counters (12,000+, 99.99%, 4.9/5, 10×) | gradient numerals |
| 5 | Features bento | 700–900px | 5–6 cards, 8/4 + 4/4/4 spans, emoji chips, one glow card | asymmetric, not 3×2 |
| 6 | How it works | 420px | 3 numbered steps | gradient step numbers |
| 7 | Testimonials | 480px | 3 quotes, stars, avatar + name + role | fake companies |
| 8 | Pricing | 700px | billing toggle, 3 tiers, middle featured + badge | glow on featured only |
| 9 | FAQ | 420px | 5–6 `<details>` | one open by default |
| 10 | Final CTA | 320px | gradient panel, H2, one primary CTA | pink glow at bottom |
| 11 | Footer | 380px | brand + newsletter, 3 link columns, socials, legal | |
| 12 | Toast / widget | — | form confirmation, slop dial | |

Hero anatomy:

```
            [ ✨ NEW · announcement → ]             24px below nav
        Ship 10× faster with the power of AI ✨      margin-top 26px
        One-sentence subhead, max 56ch, muted        margin-top 24px
        [ Start for free → ]  [ ▶ Watch demo ]      margin-top 36px
        ✓ No credit card  ✓ 14-day trial             margin-top 22px
     [ avatars ★★★★★ Loved by 12,000+ teams ]       margin-top 46px
        ┌──────── app mockup 16:9 ────────┐          margin-top 64px
```

---

## 2. App shell / dashboard

```
┌──────────────────────────────────────────────────────────────┐
│ 64px top bar: ✦ logo · workspace switcher · search · 🔔 · avatar │
├──────────┬───────────────────────────────────────────────────┤
│ 248px    │  Page header: H1 24px + subtitle 14px + CTA       │
│ sidebar  │  ──────────────────────────────────────────────── │
│ (glass)  │  KPI row: 4 glass cards, 20px numbers, sparkline  │
│          │  ──────────────────────────────────────────────── │
│ nav      │  Main grid: 2fr chart (area gradient) + 1fr list  │
│ groups   │  ──────────────────────────────────────────────── │
│          │  Table / activity feed                             │
├──────────┴───────────────────────────────────────────────────┤
```

Details that make it read as slop:
- Sidebar: 8% white, 1px border, active item with gradient pill + 3px violet left bar.
- KPI cards: glass, `↑ 12.4%` in mint, sparkline in cyan, "vs last month" in dim.
- Charts: gradient area fill from violet 45% to transparent; 1px hairline grid.
- Tables: 13px rows, avatars for owners, status chips (glass pills with colored dots).
- Top-right: gradient "New" button with ✨ and a ⌘K pill in the search field.
- Everything at 24px radii, 16px gaps, 8px inner padding grid.

---

## 3. Pricing page

```
Nav
H1: "Simple pricing. Powerful results."        (gradient on second phrase)
Sub: "Start free, scale when you're ready."     (muted, centered)
[Monthly | Annual −20%]                         (pill toggle)
┌ Starter ┐ ┌──── Pro ✨ Most popular ────┐ ┌ Scale ┐
│ $0/mo   │ │ $29/mo  (featured, glow)    │ │ $99/mo │
│ 4 ✓     │ │ 5 ✓                         │ │ 5 ✓    │
│ [ghost] │ │ [gradient CTA]              │ │ [ghost]│
└─────────┘ └─────────────────────────────┘ └────────┘
"14-day trial · No credit card · Cancel anytime"
FAQ (pricing objections)
CTA panel
Footer
```
Rules: featured card is `translateY(-8px)`, has a gradient border, glow, and the badge overlaps the
top edge. All three cards equal height; `margin-top: auto` on the button.

---

## 4. Auth screen

```
50/50 split, min-height 100vh
Left  (55%): dark canvas, orbs, mesh, logo top-left, testimonial quote bottom-left,
             tiny "SOC 2 · GDPR" badges
Right (45%): white or #0F0F1A card, 380–420px wide, glass:
             "✨ Welcome back" / "Create your account"
             [ Continue with Google ] [ Continue with GitHub ]   (fake buttons, text only)
             ─── or continue with email ───
             Email, Password (with 👁 toggle)
             [ Sign in → ] gradient block button
             "No account? Start free →"
             legal microcopy 11px dim
```
The genre signature: social login buttons at top, "or" divider, gradient submit, trust badges under
the form, and an orb bleeding in from the bottom-right.

---

## 5. Waitlist / coming soon

Centered single column, max 560px: logo mark, pill "🚀 Launching soon", huge gradient H1, email
input + "Join 12,000+ on the waitlist" gradient button, avatar stack + "Backed by founders from
Novaflow, Quantix, Hyperloop" (fake), social links. Background: full-viewport mesh + drifting orbs
+ grain. One testimonial quote optional.

---

## 6. Onboarding flow (3–4 steps)

- Progress bar: 4 segments, gradient fill, 8px tall, rounded.
- Center card 560px, glass, emoji icon chip, H2 28px, descriptive sub, options as selectable glass
  tiles with 1px border → violet border + glow when selected.
- Sticky footer inside card: "Back" ghost + "Continue →" gradient.
- Step labels: "Tell us about you", "What are you building?", "Invite your team ✨", "You're all set 🎉".
- Confetti optional; respect reduced motion.

---

## 7. Mobile app screens

- 390×844 frame. Status bar, 56px header with gradient avatar, 24px page title.
- Hero card: gradient panel with white 20px text and a big number ("9,412 hours saved").
- Segmented glass control, list rows at 16px radius, floating gradient FAB bottom-right.
- Bottom tab bar: 5 items, active item in violet with a 4px dot underneath.
- Keep the same tokens — mobile slop is just desktop slop at 390px with 20px gutters.

---

## 8. Pitch deck (10 slides)

1. Title — logo, gradient orb, "The AI-powered workspace for modern teams"
2. Problem — 3 stat cards, "Teams lose 12 hours/week to busywork"
3. Solution — product mockup in a glass frame
4. How it works — 3 steps with emoji chips
5. Traction — gradient area chart, "↑ 420% YoY"
6. Market — TAM/SAM/SOM concentric gradient rings, "$47B TAM"
7. Business model — 3 pricing cards
8. Competition — 2×2 matrix with the logo in the top-right quadrant
9. Team — 4 gradient-initial avatars + "ex-Google, ex-Stripe, ex-OpenAI" (fictional bios)
10. Ask — "Raising $40M Series B" + CTA + contact

16:9, 1280×720, 64px margins, Inter 700 for slide titles at 44px, gradient on one phrase per slide.

---

## 9. Marketing email

```
Subject: ✨ NebulaFlow 2.0 is here (and it's a game-changer)
Preheader: Your workflows will never be the same.
──────────────────────────────
[logo]                                     ← centered
# Ship 10× faster 🚀                        ← gradient not supported: use solid violet
Hi {first_name} 👋
Body: 2 short paragraphs, 1 bulleted list with ✓
[ Start for free → ]                       ← gradient button, 52px tall, rounded-full
"P.S. No credit card required."
Footer: address, unsubscribe, socials
```
Email clients don't support `backdrop-filter` or `background-clip: text` — degrade to solid violet
and pastel backgrounds.

---

## 10. Responsive rules

| Breakpoint | Changes |
| ---------- | ------- |
| ≥ 1200 | full layout, 12-col bento, 3-col pricing |
| 980–1199 | 2-col bento, pricing 3-col but tighter padding |
| 860–979 | pricing stacks (max 480px), bento 2-col, nav hides links |
| 560–859 | bento 1-col, footer 2-col, hero H1 44–52px, hide decorative orbs |
| < 560 | single column, 20px gutters, hide slop dial, buttons full width in pairs, reduce glow |

Mobile must-haves: no horizontal scroll, tap targets ≥ 44px, hero H1 ≤ 3 lines, sticky nav ≤ 64px,
marquee still works (it's the cheapest motion), pricing featured card no longer offset.

---

## 11. Density guide

| Element | Density |
| ------- | ------- |
| Landing | airy: 96–128px sections, 1 idea per screen |
| Dashboard | compact: 8px grid, 13–14px text, 24px cards |
| Docs | medium: 72ch column, 15px/1.7 |
| Deck | sparse: one idea per slide, ≤ 25 words |
| Email | medium: 600px width, 16px body |

Mixing landing density into a dashboard is the most common failure — a dashboard with 128px section
padding is unusable. Keep the *visual* language, change the *rhythm*.

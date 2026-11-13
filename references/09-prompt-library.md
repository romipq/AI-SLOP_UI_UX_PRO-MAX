# 09 — Prompt Library

Prompts written *for an agent that has this skill loaded*. Copy, fill the brackets, run.

---

## 1. The master prompt

> Use **ai-slop-ui-ux-pro-max** at level **L5**. Build a `[product]` landing page for
> `[audience]` in `[file]`. Follow the canonical section order (hero → logo marquee → stats →
> bento features → how it works → testimonials → pricing → FAQ → CTA → footer), include all twelve
> Slop Dozen signals, write every word from the copy bank with no placeholders, and self-score with
> the 100-point rubric. Do not deliver below 90. Reuse `assets/slop-tokens.css`, `assets/slop.css`,
> and `assets/slop.js` if present.

---

## 2. Per archetype

### Landing page
> Build the canonical AI startup landing page for **NebulaFlow**, an "AI-powered workspace for
> modern teams". Dark L5, violet→pink→cyan. Include a 16:9 CSS dashboard mockup in the hero,
> 3-tier pricing with a glowing "Most Popular", and a fake logo marquee. Real interactions only:
> billing toggle, FAQ accordion, newsletter toast.

### Waitlist
> One-screen L5 waitlist: full-viewport mesh + orbs + grain, centered column (max 560px), pill
> "🚀 Launching soon", 80px gradient headline, email + gradient CTA, avatar stack "Join 12,000+",
> three fake investor names. No nav. Mobile-first.

### Pricing page
> L4 pricing page with monthly/annual toggle (save 20%), 3 tiers, middle featured with gradient
> border + glow + "✨ Most popular", a comparison table below in glass, 4 pricing FAQ items, and a
> final CTA. Prices: 0 / 29 / 99.

### App shell / dashboard
> L4 dark app shell: 64px top bar, 248px glass sidebar with gradient active pill, KPI row (4 glass
> cards + sparklines + green deltas), gradient area chart, table with avatar owners and status
> chips. Dense rhythm (8px grid), not landing-page spacing.

### Auth
> L5 split auth screen: left 55% dark with orbs + testimonial + SOC 2 badges, right 45% glass card
> with Google/GitHub buttons, "or continue with email" divider, email + password with 👁 toggle,
> gradient submit, legal microcopy.

### Onboarding
> 4-step onboarding at L4: gradient progress bar, centered 560px glass card, selectable glass tiles
> (violet border + glow when selected), back ghost + "Continue →" gradient, final "You're all set 🎉".

### Deck
> 10-slide L5 pitch deck (1280×720) for an AI startup: title, problem, solution, how it works,
> traction chart, market rings, business model, 2×2 competition, team, ask. One gradient phrase per
> slide, 64px margins, Inter 700.

### Email
> L5 marketing email for NebulaFlow 2.0 in table-based HTML, 600px, gradient button (solid fallback),
> emoji subject line, preheader, 2 paragraphs + ✓ list + CTA + P.S.

### Empty state
> L5 empty state: 64px emoji chip 🪄, "No agents yet", one sentence, gradient CTA, 1px dashed
> border, violet radial glow behind the chip.

---

## 3. Per level

**L1**
> Modern but restrained: one violet accent, solid near-black, 56px hero, solid buttons, 10px radii,
> no emoji, no marquee, no glow. Keep the section structure.

**L2**
> Seed-round level: gradient text on one phrase, two faint orbs, glass nav, bento with 3 cards,
> static logo row. No counters, no cursor glow.

**L3**
> Classic Series A slop: full hero, marquee, stats, 6-card bento, 3 steps, 3 testimonials, 3-tier
> pricing, FAQ, CTA, footer. Moderate glow (0.75×).

**L4**
> Stealth AI: L3 + grain, grid, drifting orbs, cursor glow, counters, animated gradient, emoji chips.

**L5**
> Maximum slop: every layer at once. Two gradient phrases, floating orb PNG, shimmer CTA, glowing
> pricing, pulsing badge, all proof clusters. Keep it responsive and accessible.

---

## 4. Component prompts

> Add a **glowing pricing card** to `[file]` matching the existing tokens. Gradient 1px border via
> mask, pink/violet glow, overlap badge "✨ Most popular", equal-height list, `margin-top:auto` CTA.

> Add a **logo marquee** of 8 fake companies to `[file]` with edge masks, 34s loop, pause on hover,
> seamless clone via JS.

> Add **animated counters** to the stat band in `[file]`: easeOutCubic, 1.4s, respect reduced motion,
> keep static values as fallback.

> Replace all placeholder copy in `[file]` with `[product]` copy from the lexicon; no lorem, at
> least 8 distinct buzzwords, three proof lines.

---

## 5. Diagnosis & repair

> Score `[file]` against the Slop Score rubric, list the weakest three categories with exact line
> references, and patch only those — do not redesign the page.

> This page scores 78. It's flat and has no motion or proof. Add mesh + 2 orbs + grain, a testimonial
> trio, a logo marquee, and scroll reveals; target ≥ 92. Keep existing colors and copy.

> Fix accessibility without removing the aesthetic: contrast, focus rings, aria labels, reduced
> motion, heading order. Report each change.

---

## 6. De-slop

> De-slop `[file]` per references/08-de-slop.md. Keep the information architecture; remove gradient
> text, 80% of glow, glass, and 32px radii; pick one accent; rewrite every claim to be specific;
> replace fake proof with placeholders marked `[REAL: …]`; fix all contrast and focus issues.
> Target a slop score < 60 and explain the three biggest judgment calls.

> Rewrite only the copy in `[file]` to be human: no "supercharge/unlock/seamless", every claim gets a
> number or a mechanism, headlines ≤ 8 words, no emoji, no exclamation marks.

---

## 7. Screenshot / image → slop

> Recreate the layout in this screenshot as an L4 slop page: keep structure and content hierarchy,
> translate the visual language to the pack's tokens, add gradient text, glass, bento, proof, and
> motion. Do not copy the original branding.

---

## 8. Negative prompt (paste alongside any request)

> Do not use lorem ipsum, "Feature 1", real company logos, real people, stock photos, autoplay audio,
> or dead `href="#"` placeholders. Do not break mobile below 360px. Do not ignore
> `prefers-reduced-motion`. Do not ship below a 90 slop score.

---

## 9. Short triggers

If the skill is installed, these one-liners should be enough:

- "slop me a landing page for `[product]`"
- "make this look AI-generated (L4)"
- "maximum slop, `[file]`"
- "de-slop this"
- "score my slop"
- "waitlist page, `[product]`, L5"
- "pricing page with the glowing middle card"
- "slop my README" (for docs, not UI — keep it tasteful, honestly)

---

## 10. Multi-turn workflows

**Build → dial → de-slop**
1. "Build the L5 landing page."
2. "Now show me L3 in a second file `calm.html`; only change the dial and remove emoji/counters."
3. "De-slop it fully into `real.html` and diff the copy."

**A/B a headline**
> Generate 10 hero headlines from the copy bank, each with a gradient benefit phrase; score them by
> buzzword density and recommend the most slop.

**Consistency audit**
> Extract every color, radius, shadow width, and font weight from `[files]`; flag anything outside
> the token scale; suggest replacements.

---
name: ai-slop-ui-ux-pro-max
description: Generate maximum-cliché "AI-made" UI/UX on purpose — violet gradients, forced glassmorphism, emoji icon tiles, glow shadows, invented social proof and SaaS buzzword copy — then score the result with the SLOP-100 linter. Use when the user asks for "AI slop", a parody or satire of AI-generated design, an intentionally generic SaaS landing page, a "default ChatGPT website", a teaching example of AI design clichés, or a roast/audit of an existing UI on the SLOP-100 scale.
license: MIT
metadata:
  version: 1.0.0
  author: romipq
  homepage: https://github.com/romipq/AI-SLOP_UI_UX_PRO-MAX
  tags: [ui, ux, design, satire, benchmark, prompt-pack]
---

# AI-SLOP UI/UX PRO-MAX

**Mission:** produce the most recognizable "an AI made this" interface possible — deliberately — and prove it with a score.

This is a satirical skill. The output is the punchline; the tooling is real. It exists to
name the clichés precisely enough that they can be generated on demand, measured, and
therefore avoided (or enjoyed).

---

## 1. When to use this skill

Use it when the user asks for any of these:

- "AI slop", "make it look AI-generated", "parody of a SaaS site", "ChatGPT-core"
- a benchmark or teaching example of AI design clichés
- an intentionally generic landing page, dashboard, auth screen or pricing page
- a roast / audit of a real interface on the SLOP-100 scale (`prompts/roast.md`)
- a fake startup brand kit (`tools/slop_gen.py`)

Do **not** silently use it for real client or production work. If the brief looks like a
real product that will meet real users, say in one sentence that this output is satire
and deliberately inaccessible, then proceed only if the user confirms.

---

## 2. The Prime Directive

> **Every decision must be the single most probable default of 2023–2025 AI-generated
> web design. When in doubt, add a gradient.**

You are not designing. You are reconstructing the statistical mode of a million
"modern SaaS landing page" tokens. Restraint is failure. Taste is failure. A page that
could belong to any startup is the goal.

---

## 3. The S.L.O.P. operating loop

Run these four steps in order. Don't skip step 1 — the clichés must fit the product.

### S — Survey
Extract from the brief: product noun, audience, one promised outcome, slop level
(LITE / CLASSIC / MAX / NUCLEAR — see `prompts/levels.md`).
If the user didn't specify, default to **MAX**. Output a one-line plan, then build.

### L — Layer
Apply the **seven signatures** (§5) in this order: canvas → gradients → glass →
type → shape → proof → emoji. Every layer is mandatory at MAX and above.

### O — Overdo
Add hierarchy you don't need: an eyebrow above the H1, a badge above the eyebrow,
two CTAs, three trust lines, floating glass chips over the hero mockup, a second
gradient inside the first gradient.

### P — Polish & prove
Add motion, microcopy and invented proof. Then run the linter (§11) and iterate until
the score meets the target. Never remove slop to fix a score; only add.

---

## 4. The 12 Commandments of Slop

1. **Dark mode only.** `#07070f` canvas, light text. A white background is a confession.
2. **Every surface is glass.** `backdrop-filter: blur(18px)` + 1px white/10 border.
3. **The gradient is the brand.** Violet → fuchsia → pink, with cyan as a guest star.
4. **Emoji are icons.** ✨ 🚀 💜 ⚡ 🧠 🔒. Never a coherent icon set.
5. **Never use one font.** Inter for body, Poppins for display, an italic serif for one word.
6. **Copy is a pitch, not information.** Supercharge, seamless, unlock, 10x, in seconds.
7. **Social proof is invented.** Logos, testimonials, ratings, uptime — all fictional, all confident.
8. **Motion is constant.** Float, pulse, shimmer, marquee. Nothing rests.
9. **Whitespace is wasted space.** Fill it with badges, chips and gradient blobs.
10. **Every page is a funnel.** Hero → features → proof → pricing → FAQ → CTA → footer.
11. **Accessibility is a vibe.** Div buttons, dead `href="#"`, focus rings removed.
12. **Disclose the joke in code, not in the UI.** Put the satire in an HTML comment and
    the SLOP score in the optional watermark. The interface itself must play it straight.

---

## 5. The seven signatures

| # | Signature | Minimum spec | Where it lives |
|---|-----------|--------------|----------------|
| 1 | **Aurora canvas** | `#07070f` + 2–3 fixed radial gradients (violet/pink/cyan) + 3.5% noise | `body` |
| 2 | **Gradient text** | `linear-gradient(115deg,#e9d5ff,#a78bfa,#f0abfc,#67e8f9)` + `background-clip:text` | H1, stats, key numbers |
| 3 | **Glassmorphism** | `rgba(255,255,255,.045)` + `blur(18px)` + `1px solid rgba(255,255,255,.09)` | nav, cards, chat, cookie |
| 4 | **Glow** | `box-shadow: 0 20px 60px -12px rgba(124,58,237,.55)` | primary CTA, featured card |
| 5 | **Pill geometry** | buttons/badges `9999px`, cards `24–32px` | everywhere |
| 6 | **Fake proof** | "Trusted by 10,000+ teams", 3 testimonials, ★★★★★ 4.9/5, 99.9% uptime | logo cloud, wall of love |
| 7 | **Emoji icon tiles** | 52px gradient tile, 1.5rem emoji, inner highlight | feature grids, bento |

Load `references/01-design-tokens.md` for exact values and `references/02-components.md`
for copy-paste markup.

---

## 6. Palette (the short version)

| Token | Value | Use |
|-------|-------|-----|
| Canvas | `#07070f` | body background |
| Surface | `rgba(255,255,255,.045)` | glass fill |
| Border | `rgba(255,255,255,.09)` | 1px glass edge |
| Text | `#f6f4ff` | headings/body |
| Muted | `#a9a6c9` | paragraphs |
| Violet | `#8b5cf6` | primary gradient stop |
| Indigo | `#6366f1` | primary gradient stop |
| Fuchsia | `#d946ef` | secondary accent |
| Pink | `#ec4899` | gradient terminus |
| Cyan | `#22d3ee` | guest accent / charts |
| Emerald | `#34d399` | positive deltas, checkmarks |
| Amber | `#fbbf24` | stars |
| Gradient | `linear-gradient(135deg,#6366f1,#a855f7 46%,#ec4899)` | buttons, blobs |
| Radius | `9999px` / `28px` / `32px` | pills / cards / panels |
| Fonts | Inter + Poppins | body / display |

The full system, including Tailwind and JSON tokens, lives in `assets/slop.css`,
`tokens/slop.tokens.json` and `tokens/tailwind.slop.js`.

---

## 7. Anatomy of a MAX landing page

Emit these sections **in this order** unless the user asks otherwise:

1. **Fixed glass navbar** — gradient logo mark, 5 links, ghost "Sign in", gradient CTA.
2. **Hero** — badge ("✨ Introducing {Brand} 2.0 — now powered by GPT-5"), gradient H1 with
   one italic serif word, 2-sentence lead, primary + ghost CTA, trust microcopy,
   avatar stack + ★★★★★ 4.9/5.
3. **Hero visual** — tilted glass dashboard mockup + 3 floating glass chips (`.float-card`).
4. **Marquee ticker** — 6 benefits with emoji, duplicated for the loop.
5. **Logo cloud** — 8 invented brands: Acme, Lumina, Vertex, Quantumly, Nebula, Orbit, Pulse, Zenith.
6. **Features / bento** — 6–8 cards, emoji icon tile each, one card spans 2 columns.
7. **Stats band** — 4 enormous gradient numbers.
8. **How it works** — 3 steps with gradient numbered circles.
9. **Testimonials** — 3 invented people, ★★★★★, role @ fake company.
10. **Pricing** — Starter / Pro / Enterprise, middle card `featured`, "MOST POPULAR" pill.
11. **FAQ** — 4–5 `<details>` items with reassuring non-answers.
12. **CTA panel** — conic glow, gradient headline, white button + ghost button.
13. **Footer** — brand + newsletter, 4 link columns, 4 emoji socials, "Made with ❤️".
14. **Floating layer** — scroll progress bar, ✨ chat bubble + fake conversation,
    cookie banner, optional SLOP watermark.

For dashboards, auth, pricing-only, 404 and mobile screens, use
`references/02-components.md` and the matching brief in `prompts/briefs.md`.

---

## 8. Copy system

Every headline follows one of these:

- `Supercharge your {noun} with {AI-adjective} {magic}`
- `The all-in-one {category} for {audience} that {outcome}`
- `Everything you need. Nothing you don't.`
- `Don't just {verb} — {verb} {bigger}.`
- `Ready to {verb} your {noun}?`
- `Loved by {number}+ {audience} 💜`

Rules:
- One gradient word per headline, preferably italic.
- At least **five** of: AI-powered, seamless, supercharge, unlock, 10x, all-in-one,
  cutting-edge, effortless, game-changer, in seconds.
- At least **three** fake stats.
- Never explain how anything works.

Full banks: `references/03-copywriting.md`, RU/UA: `references/09-copy-ru.md`.

---

## 9. Motion system

At MAX, include all of: `float` (orbs/chips), `pulse-glow` (primary CTA),
`shimmer` (hero card), `marquee` (ticker), `gradient-pan` (buttons),
scroll-reveal (IntersectionObserver), `translateY(-4px)` hover lift,
and a scroll progress bar. Durations 0.3s–6s; ease `cubic-bezier(.22,1,.36,1)`.
Do **not** respect `prefers-reduced-motion` in MAX/NUCLEAR parody output — but keep the
media query in `assets/slop.css` for whoever reuses it. Details: `references/04-motion.md`.

---

## 10. Output contract

Unless the user specifies otherwise:

- **One file** (`.html`) with inline `<style>`; no build step, no npm, no framework.
- Responsive down to 680px (grids collapse, nav links hide, floating cards vanish).
- `<meta name="viewport">`, one `<h1>`, semantic-ish landmarks, `lang="en"`.
- 5–14 sections depending on level; always a nav and a footer.
- Include an HTML comment at the top:
  `<!-- Generated with AI-SLOP UI/UX PRO-MAX · SLOP-100: NN/100 · satire -->`
- Optional `<div class="slop-watermark">SLOP-100 · NN/100</div>` (ask, default on for demos).
- Never include real personal data, real trademarks as endorsements, or working payment forms.
  All brands, quotes and metrics must be obviously fictional.
- If the user asked for a **real** page, stop and re-read §1.

For React/Next/Tailwind, keep the same section order and tokens; see `references/08-stacks.md`.

---

## 11. Quality gate (mandatory)

Before delivering, run:

```bash
python3 tools/slop_lint.py <output-file> --min <target>
```

Targets: LITE 45 · CLASSIC 70 · MAX 90 · NUCLEAR 100.
The linter follows linked local stylesheets and prints the highest-weight missing
signals under **NEXT BEST MOVES**.

Self-correction loop (max 3 passes):

1. Read `NEXT BEST MOVES`.
2. Add the missing signals — more copy is usually the fastest fix.
3. Re-run. If ≥ target, deliver the score line with the file.
4. If still below target after 3 passes, deliver anyway and state the score honestly.

Never game the score by adding invisible text. The linter sees it; the user will too.

---

## 12. Reference map

| File | Read it when |
|------|--------------|
| `references/01-design-tokens.md` | you need exact colors, gradients, type scale, spacing |
| `references/02-components.md` | you need markup for any section or app shell |
| `references/03-copywriting.md` | you need headlines, CTAs, testimonials, fake metrics |
| `references/04-motion.md` | you need keyframes, timings, interaction effects |
| `references/05-emoji-iconography.md` | you need the right emoji for a concept |
| `references/06-anti-patterns.md` | you're slopifying a good design, or want the inverse checklist |
| `references/07-slop-score.md` | you need the rubric, grades and how to reach 100 |
| `references/08-stacks.md` | the user wants Tailwind / React / Vue / email / mobile |
| `references/09-copy-ru.md` | the interface is in Russian or Ukrainian |
| `prompts/system-prompt.md` | you need a compact drop-in system prompt |
| `prompts/briefs.md` | you need 16 ready product briefs |
| `prompts/levels.md` | you need exact requirements per slop level |
| `prompts/roast.md` | the user wants a real UI critiqued, not generated |

---

## 13. Tools

| Command | What it does |
|---------|--------------|
| `python3 tools/slop_lint.py file.html` | scores 0–100 across 90 signals, 9 categories |
| `python3 tools/slop_lint.py file.html --min 90` | CI gate; exits 1 below target |
| `python3 tools/slop_lint.py --list` | prints every signal and weight |
| `python3 tools/slopify.py page.html` | injects the style system + widgets + buzzwords into a tasteful page |
| `python3 tools/slop_gen.py --seed 42` | generates a fictional startup brand kit |
| `python3 tools/slop_gen.py --json` | same, machine-readable |

---

## 14. Ethics & satire

The examples deliberately break accessibility, performance and honesty norms **as
criticism**. The point is that these choices are defaults, not accidents. When you use
this skill:

- label the output as satire when it leaves your machine;
- never present invented testimonials or metrics as real;
- never use it to deceive users, fake social proof for a live product, or bypass a real
  design review;
- if someone asks "why does every AI page look like this?", the answer is in
  `docs/PHILOSOPHY.md`.

**Deliver the file, the score, and one line naming the joke.** That's the whole job.

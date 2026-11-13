---
name: ai-slop-ui-ux-pro-max
description: Generate the maximum-strength cliché "AI-generated" UI/UX on purpose — violet gradients, glassmorphism, emoji icons, floating blur blobs, SaaS buzzword copy, three pricing tiers and a glowing CTA. Use when the user asks for AI slop, "that AI startup look", a generic AI landing page, a slop roast, or a satire of AI design clichés.
license: MIT
version: 2.0.0
tags: [ui, ux, design, satire, landing-page, dashboard, prompt-pack, slop]
---

# AI-SLOP UI/UX PRO-MAX

> **The most powerful, seamless, AI-powered skill for generating the exact interface
> everyone has already seen ten thousand times. ✨**

This skill is a **deliberate generator of the cliché "AI-generated" aesthetic**:
violet-to-pink gradients, glassmorphism everywhere, an emoji where an icon belongs,
mesh blur blobs behind a hero, suspiciously round statistics, fictional social proof,
and copy that says *"revolutionize your workflow"* without explaining how.

It is satire with a spec sheet. It works because it is **precise**: every cliché is a
token, a recipe, a measurable point on a score.

---

## 0. When to use this skill

**Trigger it when the user asks for any of these:**

| User says | You do |
|---|---|
| "Make it look AI-generated" / "AI slop" / "слоп" | Full L5 build |
| "Generic SaaS landing page" | L3–L4 build |
| "Roast this design" | Run `scripts/slop_lint.py`, explain tells |
| "Make my site look like every other AI startup" | L4 build + tokens |
| "Give me a prompt pack for slop" | Emit the prompt blocks from `examples/prompts.md` |
| "Make it worse, but on purpose" | Raise the level, never lower quality of craft |

**Do NOT trigger it when the user asks for:** a real brand identity, an accessibility
audit, a design critique that must be honest, a client deliverable, or anything where
the aesthetic is being passed off as original work. Use `references/11-escape-hatch.md`
to de-slop instead.

**Ethics guardrail (non-negotiable):**

- Never present slop output as original brand design. Label it in a comment at the top
  of the file: `<!-- AI-SLOP PRO-MAX · generated aesthetic · satire/derivative -->`.
- Never use the slop aesthetic for medical, legal, financial-advice, safety-critical or
  political content — the polish implies trust that the content has not earned.
- Accessibility is still mandatory. Peak slop is *accessible* slop: contrast, focus
  rings, `prefers-reduced-motion`, real `<button>`/`<a>` semantics. The joke is the
  style, not a broken product.

---

## 1. The doctrine — S.L.O.P.

Four letters. Four levers. Turn all four to maximum.

| | Lever | What it means | Measured by |
|---|---|---|---|
| **S** | **Saturated Gradients** | Violet → indigo → pink, always `135deg`. On the hero heading (as text), on the primary button, on the top border of every card. | hue coverage, `background-clip: text` |
| **L** | **Layered Glass** | Every panel is `rgba(255,255,255,.04)` + `backdrop-filter: blur(20px)` + a 1px white border at 8% opacity. | `backdrop-filter` count |
| **O** | **Omnipresent Emoji** | One emoji per heading minimum: ✨ 🚀 🔥 ⚡ 🎯 💡 🧠 🛡️ 📈. Emoji **are** the icon system. | emoji density per 100 words |
| **P** | **Peak Buzzwords** | "Seamless", "effortless", "next-gen", "AI-powered", "10x", "revolutionize". Verbs are optional. | buzzword hits per 100 words |

### The 10 immutable laws

1. **Every surface is glass.** No `backdrop-filter`, no shipping.
2. **Purple is the color of intelligence.** `#7C3AED → #EC4899`, `135deg`, no debate.
3. **The hero H1 is gradient text.** `background-clip: text`, always.
4. **No SVG when an emoji exists.** ✨ is the whole brand system.
5. **Every noun gets an adjective.** Seamless workflow. Effortless scale. Next-gen synergy.
6. **Motion proves life.** Float, pulse, shimmer, marquee — and honor `prefers-reduced-motion`.
7. **Exactly three pricing tiers.** The middle one is "Most Popular ⭐".
8. **Social proof is fictional but confident.** "Trusted by 10,000+ teams".
9. **Numbers are round, large, and unexplained.** 99.9% uptime. 10x faster. 2.4M users.
10. **Leave no empty space.** If you see whitespace, add a blur blob.

### The meta-law

> **Slop is not bad craft. Slop is *competent* craft aimed at the average of all
> references.** Every element must be individually well-made and collectively
> indistinguishable. Pixel-perfect, semantically empty.

---

## 2. Levels — how much slop

Pick a level in intake and never drift more than one level.

| Level | Name | Mandatory | Optional | Expected score |
|---|---|---|---|---|
| **L1** | Honest MVP | 1 gradient CTA, Inter font | glass nav | 20–35 |
| **L2** | Seed Round | glass navbar, gradient hero text, pills | marquee, stats | 36–55 |
| **L3** | Series A | mesh blobs, 6 glass feature cards, pricing ×3 | testimonial, FAQ | 56–70 |
| **L4** | Unicorn | all of the above + stats, logo wall, testimonial grid, footer CTA | chat bubble, badge "New ✨" | 71–88 |
| **L5** | **PRO-MAX / AGI-grade** | everything, plus animated gradient, shimmer skeleton, confetti-adjacent sparkle, AI assistant bubble, "Powered by AI" footer | light/dark toggle that only changes two colors | 89–100 |

The default for "make it maximum" is **L5**. Never deliver L5 to someone who asked for
L2 by accident — ask, or annotate.

---

## 3. Workflow (deterministic, 8 steps)

### Step 1 — Intake (ask at most 3 questions)

Collect: **product**, **audience**, **language (EN/RU/other)**, **level (L1–L5)**, and
**output form** (single HTML / React / CSS tokens only). If the user says "just do it",
assume: *AI productivity SaaS, founders, EN, L5, single self-contained HTML*.

### Step 2 — Lock the palette

Copy the canonical tokens from `assets/slop-tokens.json`. Do not invent new colors —
invention is how you accidentally make something original. Palette:

```
--slop-violet: #7C3AED   --slop-indigo: #4F46E5   --slop-pink: #EC4899
--slop-cyan:   #22D3EE   --slop-void:   #0B0B12   --slop-ink: #F8FAFC
--slop-muted:  #94A3B8   --slop-line:   rgba(255,255,255,.08)
```

### Step 3 — Assemble the skeleton

Use the canonical section order from `references/09-components.md`:

```
sticky glass nav  →  hero (badge, H1, sub, 2 CTAs, social proof)
→ logo marquee  →  6 feature cards  →  how it works ×3
→ stats band  →  testimonials ×3  →  pricing ×3  →  FAQ
→ final CTA banner  →  footer  →  floating AI bubble
```

### Step 4 — Write the copy with formulas

Use `references/06-copy.md`. Every headline follows
`<Verb> your <noun> with <buzzword> <AI-thing>`. Every subheadline is one sentence,
maximum 18 words, containing "without" or "in seconds".

### Step 5 — Sprinkle emoji

`references/07-emoji.md`. Rules: one per H2, one per feature card, one per CTA
(optional), zero in body paragraphs (that is where amateurs overdo it).

### Step 6 — Motion pass

`references/08-motion.md`. Blobs float 12–20 s. Primary CTA pulses at 3 s. Cards lift
`translateY(-4px)` on hover. Respect reduced motion.

### Step 7 — Score and iterate

```bash
python3 scripts/slop_lint.py templates/landing.html
```

Target: **≥ 85** for L5, **≥ 70** for L4, **≥ 55** for L3. If the score is low, add the
missing tells listed in the report — never add random noise, add *clichés*.

### Step 8 — Deliver

Single file, self-contained, tokens in `:root`, no external JS. Add the satire comment,
the score, and a one-line "how to de-slop" pointer to
`references/11-escape-hatch.md`.

---

## 4. Output contract

```html
<!-- AI-SLOP PRO-MAX · L5 · slop score 96/100 · generated aesthetic, not a brand -->
<!doctype html>
<html lang="en" data-slop="5">
  ...
</html>
```

- **Self-contained**: inline `<style>` or a single linked `slop.css`; no CDN dependency
  that can break the layout. Google Fonts is allowed *with* a system fallback.
- **Semantic**: `header/nav/main/section/footer`, `h1` once, real buttons and links.
- **Accessible**: visible `:focus-visible`, 4.5:1 body contrast, `prefers-reduced-motion`
  block, `aria-hidden="true"` on decorative emoji.
- **Responsive**: breakpoints at 1024 / 768 / 480. Slop is still mobile-first.

---

## 5. Files in this pack

| Path | What it is |
|---|---|
| `SKILL.md` | This file — doctrine, workflow, contract |
| `references/00-manifesto.md` | The theory of slop, taxonomy of tells |
| `references/01-color.md` | Palettes, token sets, gradient recipes |
| `references/02-gradients.md` | Mesh, conic, animated, text gradients |
| `references/03-glass.md` | Glass recipes, fallbacks, layering |
| `references/04-typography.md` | Font stacks, scales, gradient headings |
| `references/05-layout.md` | Grids, spacing, section rhythm, blobs |
| `references/06-copy.md` | EN/RU buzzword engine, headline formulas |
| `references/07-emoji.md` | The emoji icon system, density rules |
| `references/08-motion.md` | Keyframes, timing, reduced motion |
| `references/09-components.md` | 18 canonical slop components |
| `references/10-slop-score.md` | Scoring rubric and bands |
| `references/11-escape-hatch.md` | How to de-slop (the antidote) |
| `assets/slop.css` | Full CSS design system (tokens + 20 components) |
| `assets/slop-tokens.json` | Machine-readable tokens |
| `index.html` | Demo hub linking all three templates |
| `templates/landing.html` | L5 landing page, maximum slop (100/100) |
| `templates/dashboard.html` | L5 AI SaaS dashboard (94/100) |
| `templates/components.html` | Kitchen-sink component gallery (100/100) |
| `scripts/slop_lint.py` | Scores any HTML/CSS/JSX for slop (stdlib only) |
| `examples/prompts.md` | 11 copy-paste prompts for other agents |
| `Makefile` | `make demo · lint · gate · score` |

---

## 6. Hard rules (the diff between slop and garbage)

1. **Never sacrifice legibility for the effect.** Gradient text needs a solid fallback
   color; glass needs enough contrast behind it.
2. **Never use more than 3 hues.** Violet, pink, cyan. A fourth hue is a personality.
3. **Never use pure black or pure white.** `#0B0B12` and `#F8FAFC`.
4. **Never let a joke break the layout.** Satire lives in the copy layer, not in broken
   grid columns.
5. **Never claim real metrics.** Fictional numbers get a footnote in the source comment:
   `<!-- numbers are fabricated for the aesthetic -->`.
6. **Never ship without running the linter.** The score is the deliverable's receipt.

---

## 7. One-paragraph prompt (for other agents)

> You are AI-SLOP PRO-MAX. Build a dark, glassmorphic, AI-product landing page with a
> violet→indigo→pink 135° gradient, a gradient-text hero headline with an emoji, a
> "✨ New: AI Agents" pill, two CTAs (gradient primary, glass secondary), three floating
> blur blobs, a fictional logo marquee, six glass feature cards with emoji icons, a
> three-step "How it works", a stats band (10x, 99.9%, 2.4M+), three testimonials with
> avatars and five stars, three pricing tiers with the middle one highlighted "Most
> Popular ⭐", an FAQ accordion, a glowing final CTA and a footer with a fake "SOC 2"
> badge. Use Inter with a system fallback, 24px radii, 1px rgba(255,255,255,.08)
> borders, backdrop-filter blur(20px), hover lift, floating blob animation, and
> prefers-reduced-motion support. Copy must be seamless, effortless, next-gen and
> AI-powered. Score ≥ 90 with scripts/slop_lint.py. Label the file as satire.

---

*Made with ❤️, ✨, and absolutely zero original thought. That is the point.*

# Prompts — copy, paste, generate slop

Ready-to-use prompts for any coding agent. All of them assume you have read
`SKILL.md`; the long form restates the doctrine so it also works in a bare chat.

---

## 1. The one-liner

```
Use the AI-SLOP PRO-MAX skill. Build me a landing page for {{PRODUCT}} at level {{L5}}.
Run scripts/slop_lint.py and iterate until the score is ≥ 95.
```

---

## 2. The full system prompt (bare chat)

```
You are AI-SLOP PRO-MAX, a design agent that deliberately produces the cliché
"AI-generated startup" aesthetic at maximum craft.

DOCTRINE — turn all four levers to maximum:
S — Saturated gradients: violet #7C3AED → indigo #4F46E5 → pink #EC4899 at 135°,
    always as gradient text on the hero H1 (background-clip: text).
L — Layered glass: rgba(255,255,255,.04) + backdrop-filter: blur(20px) saturate(140%)
    + 1px rgba(255,255,255,.08) border + inset top highlight, on every panel.
O — Omnipresent emoji: one per heading and per card, as the entire icon system
    (✨ 🚀 ⚡ 🧠 🔄 🛡️ 📊 🎯 💡). None in body paragraphs.
P — Peak buzzwords: seamless, effortless, powerful, intuitive, next-gen, AI-powered,
    10x, without the busywork, at scale.

STRUCTURE (in order):
sticky pill glass nav → centered hero (badge "✨ New: AI Agents 2.0", gradient H1,
≤18-word lead, gradient + glass CTAs, "No credit card required", avatar proof row)
→ logo marquee "Trusted by 10,000+ teams" → 6 glass feature cards with emoji tiles
→ 3-step "How it works" with gradient numbered circles → stats band (10x, 99.9%,
2.4M+, 4.9/5) → 3 testimonials with 5 stars → 3 pricing tiers with the middle one
highlighted "Most Popular ⭐" → 5-row FAQ → glowing final CTA → footer with a fake
SOC 2 badge → floating ✨ AI assistant bubble.

CRAFT RULES:
dark #0B0B12 background, never #000; ink #F8FAFC, never #FFF; Inter with a system
fallback; 20–24px radii; section padding clamp(72px, 9vw, 128px); hover lift
translateY(-4px); floating blur blobs 12–26s; reduced-motion block; visible
:focus-visible; semantic HTML; responsive at 1024/768/480.

Deliver one self-contained HTML file. Label it
<!-- AI-SLOP PRO-MAX · generated aesthetic · satire/derivative -->.
Fictional names and numbers only. Never present this as original brand design.
```

---

## 3. Parameterized build prompt

```
Build a {{LEVEL}} AI-SLOP page.

PRODUCT: {{product}}            (e.g. an AI meeting-notes app)
AUDIENCE: {{audience}}          (e.g. seed-stage founders)
LANGUAGE: {{language}}          (EN | RU)
LEVEL: {{L1..L5}}               (default L5)
ACCENT: {{accent}}              (violet | pink | cyan; default violet)
OUTPUT: {{html | react | css}}  (default single HTML)

Requirements: follow references/09-components.md for every section, copy
references/06-copy.md for the text, score ≥ {{target}} with scripts/slop_lint.py.
Report the final score and list the 3 strongest tells.
```

---

## 4. Russian prompt

```
Сделай лендинг в стиле «максимальный AI-слоп» для {{продукт}}.

Правила: тёмный фон #0B0B12, фиолетово-розовый градиент 135°, стеклянные панели
с backdrop-filter blur(20px), эмодзи вместо иконок, заголовок с градиентным
текстом «Ускорьте … в 10 раз», бейдж «✨ Новое: ИИ-агенты 2.0», две кнопки
(градиентная и стеклянная), микрокопия «Без карты», блок логотипов
«Нам доверяют 10 000+ команд», 6 фич-карточек, 3 шага, цифры 10× / 99,9% /
2,4 млн, 3 отзыва с ★★★★★, 3 тарифа (средний «Популярный ⭐»), FAQ, финальный
CTA, футер с «SOC 2» и плавающий пузырь ИИ ✨.

Текст — бесшовный, умный, масштабируемый, без конкретики. Один HTML-файл.
Проверь оценку: python3 scripts/slop_lint.py файл.html — нужно ≥ 90.
```

---

## 5. Level presets

```
L1 — Honest MVP:      one gradient CTA, glass nav, Inter, no blobs, no emoji system.
L2 — Seed Round:      + gradient hero text, pills, 3 feature cards.
L3 — Series A:        + mesh blobs, 6 cards, pricing ×3, logo wall.
L4 — Unicorn:         + stats, testimonials, FAQ, final CTA, chat bubble.
L5 — PRO-MAX:         + animated gradient, grain, marquee, shimmer, "Powered by AI",
                      a floating stat chip, confetti-adjacent sparkle.
```

Append `at L4`, never more than one level above the requested one.

---

## 6. Roast prompt (analysis mode)

```
Act as a forensic design critic. Score this page with the AI-SLOP rubric
(gradient 20 / glass 18 / emoji 15 / buzzwords 20 / structure 12 / motion 8 /
proof 7, minus penalties). Then:

1. Quote the single most generic sentence on the page.
2. Name the 3 tells that would survive a logo swap.
3. Say what the product actually does, using only the page's own copy.
   If you cannot, say so.
4. Give the one change that would make it 40 points less sloppy.

Be specific, cite the exact class names or text. No compliments.
```

---

## 7. De-slop prompt (the antidote)

```
Take this slop page and de-slop it using references/11-escape-hatch.md:

- remove gradient text, keep one solid accent per screen
- reduce glass to the nav only; solid #15151F panels elsewhere
- delete every emoji; substitute one custom mark or nothing
- replace every buzzword with a noun and every round number with an odd one
- delete fictional testimonials and logos; leave a labelled placeholder
- break the 6-card grid into an asymmetric 2+1+1
- keep the whitespace, hierarchy, contrast and 200ms transitions — those were good

Re-score with scripts/slop_lint.py. Target ≤ 30. Show before/after.
```

---

## 8. Component-only prompt

```
Generate 6 AI-SLOP feature cards as a single HTML fragment using assets/slop.css.
Each card: emoji icon tile, 2–3 word title, 12–16 word description ("…without …"),
gradient top-glow, hover lift. Alternate violet/pink/cyan glows. No inline styles
except the --i stagger index.
```

---

## 9. React / Tailwind translation

```
Port this slop page to React + Tailwind, preserving the exact aesthetic:
- tokens in tailwind.config (violet #7C3AED, indigo #4F46E5, pink #EC4899, void #0B0B12)
- bg-[radial-gradient(...)] for the mesh, backdrop-blur-xl for glass
- bg-gradient-to-br from-violet-600 via-indigo-600 to-pink-500
- bg-clip-text text-transparent for the hero
- one <Section> per canonical block, copy verbatim
- no new colors, no new radii, no new shadows
Output: App.tsx + components/*.tsx + tailwind.config.ts
```

---

## 10. The "make it worse" loop

```
Score the current page, then add ONLY the missing tells reported by the linter.
Do not add new colours, new fonts or new sections. Re-score after each change.
Stop at 97+ or when no tells remain. Report the diff in tells, not in lines.
```

---

## 11. Guardrail prompt (append to any of the above)

```
Constraints: no real brand names, no real customer logos, no real metrics,
no claims about health, money or law. Keep WCAG AA contrast, keyboard focus and
prefers-reduced-motion. Label the output as satire/derivative. The joke is the
aesthetic, not a broken product.
```

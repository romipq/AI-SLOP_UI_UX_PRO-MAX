# SLOP cheatsheet

*One page. Print it. Tape it to the monitor.*

---

## Palette

```
CANVAS   #07070f      GLASS    rgba(255,255,255,.045)
SURFACE  #0b0b18      BORDER   rgba(255,255,255,.09)
TEXT     #f6f4ff      MUTED    #a9a6c9
VIOLET   #8b5cf6      INDIGO   #6366f1
FUCHSIA  #d946ef      PINK     #ec4899
CYAN     #22d3ee      EMERALD  #34d399
GRAD     linear-gradient(135deg,#6366f1,#a855f7 46%,#ec4899)
TEXTG    linear-gradient(115deg,#e9d5ff,#a78bfa,#f0abfc,#67e8f9)
```

## Seven signatures

1. Aurora canvas + noise
2. Gradient clipped text
3. Glass (fill + border + blur + highlight)
4. Violet glow
5. Pills (9999px) + 28px cards
6. Fake proof (logos, quotes, 99.9%)
7. Emoji in gradient tiles

## Page anatomy

`nav → hero → mockup → ticker → logos → 6 features → 4 stats → 3 steps → 3 testimonials → 3 pricing → FAQ → CTA → footer → progress + chat + cookie`

## Copy bank

**Headline:** Supercharge your {noun} with AI-powered magic
**Sub:** The all-in-one {category} that seamlessly {verb}s your {noun} — in seconds.
**CTA:** Get Started for Free → / ▶ Watch demo
**Note:** No credit card required · 14-day free trial · Cancel anytime
**Proof:** Trusted by 10,000+ teams · ★★★★★ 4.9/5 · 99.9% uptime
**Words:** AI-powered, seamless, supercharge, unlock, 10x, all-in-one, cutting-edge,
effortless, game-changer, in seconds, empower, elevate.

## Components

| Need | Class |
|------|-------|
| Glass panel | `.glass` |
| Card with hover glow | `.card` |
| Gradient button | `.btn.btn-primary` |
| Ghost button | `.btn.btn-ghost` |
| Badge / eyebrow | `.badge` / `.eyebrow` |
| Emoji tile | `.icon` |
| Pill | `.badge`, `.chip` |
| Stats band | `.stats > .stat` |
| Testimonial | `.quote`, `.person` |
| Pricing | `.pricing-grid > .price-card.featured` |
| FAQ | `.faq > details` |
| Chat | `.chat-bubble` + `.chat-window` |
| Cookie | `.cookie` |
| Progress | `.scroll-progress` |

## Motion

`gradient-pan 6s` · `float 6s` · `pulse-glow 3.4s` · `shimmer 2.8s` ·
`marquee 26s` · `reveal .7s` · hover `translateY(-4px)`.

## Tools

```bash
python3 tools/slop_lint.py page.html           # score
python3 tools/slop_lint.py page.html --min 90  # gate
python3 tools/slop_lint.py --list              # 90 signals
python3 tools/slopify.py tasteful.html         # ruin it
python3 tools/slop_gen.py --seed 42            # fake startup
python3 tools/gen_rubric.py                    # refresh docs
```

## Grades

`95+ S+` · `90 S` · `80 A` · `65 B` · `45 C` · `25 D` · `<25 F`

## Budgets

Copy 20 · Color 18 · Structure 12 · Shape 11 · Glass 11 · Emoji 9 · Motion 8 · Type 7 · A11y 4

## A11y sins (parody only)

div button · dead `href="#"` · `outline: none` · `img` without alt · div `onclick`

## Levels

`45+ LITE` · `70+ CLASSIC` · `90+ MAX` · `100 NUCLEAR`

## The one rule

If it looks calm, add a gradient. If it looks good, add two.

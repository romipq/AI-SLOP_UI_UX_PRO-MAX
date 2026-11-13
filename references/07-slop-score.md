# 07 · The SLOP-100 rubric

The score is a weighted count of recognizable AI-design clichés, grouped into nine
categories. **Category budgets sum to exactly 100**, so a perfect score requires breadth:
gradients alone cannot carry a page, and copy alone cannot either.

> This file is generated from `tools/slop_lint.py`. If you change a weight there,
> regenerate this document (`python3 tools/gen_rubric.py`).

---

## Category budgets

| Category | Budget | What it measures |
|----------|--------|------------------|
| **Copy** | 20 | Buzzword density, CTA clichés, fake proof language, invented brands |
| **Color** | 18 | Gradient palette, gradient text, glow, multi-hue sprawl |
| **Structure** | 12 | The SaaS section stack: proof, pricing, FAQ, cookie, chat |
| **Shape** | 11 | Pill geometry, bento grids, dual CTAs, rounded panels |
| **Glass** | 11 | Blur, translucency, glass borders, grain, blend modes |
| **Emoji** | 9 | Emoji count and placement, sparkles, rockets, hearts |
| **Motion** | 8 | Float, pulse, shimmer, marquee, reveal, scroll progress |
| **Type** | 7 | Font pairing, 800 weights, tight tracking, clamp() hero sizes |
| **A11Y Sins** | 4 | The accessibility sins that come free with the aesthetic |
| **Total** | **100** | |

---

## Grades

| Score | Grade | Meaning |
|-------|-------|---------|
| 95–100 | **S+ — PEAK SLOP** | museum-grade; every category capped; use in teaching |
| 90–94 | **S — CERTIFIED AI-GENERATED** | the target for MAX; unmistakably machine-made |
| 80–89 | **A — premium slop** | polished VC deck energy; one category is slacking |
| 65–79 | **B — VC-backed slop** | believable template; needs more proof and emoji |
| 45–64 | **C — template energy** | hints of taste; gradients present but shy |
| 25–44 | **D — restrained (suspicious)** | a human edited this |
| 0–24 | **F — human taste detected** | whitespace, hierarchy, restraint — fix immediately |

---

## All 90 signals

### Copy — budget 20

| W | Signal | How to add it |
|---|--------|---------------|
| 5 | `copy.ai_powered` · "AI-powered" | describe every noun as AI-powered, including the nouns |
| 4 | `copy.gpt` · "Powered by GPT-5" | name-drop a model version the product cannot possibly use |
| 4 | `copy.supercharge` · "Supercharge" | supercharge your workflow / pipeline / revenue |
| 3 | `copy.seamless` · "Seamless" | seamlessly unify/integrate/sync at least once |
| 3 | `copy.revolutionize` · "Revolutionize" | revolutionize the way teams work — revolutionary |
| 2 | `copy.unlock` · "Unlock" | unlock insights / potential / growth |
| 2 | `copy.elevate` · "Elevate" | elevate your brand / workflow / experience |
| 2 | `copy.empower` · "Empower" | empower your team to do more |
| 3 | `copy.gamechanger` · "Game-changer" | call one feature a total game-changer |
| 3 | `copy.cutting_edge` · "Cutting-edge" / "next-gen" | cutting-edge, next-generation, state-of-the-art |
| 3 | `copy.tenx` · "10x" | promise 10x (or 100x) productivity with a straight face |
| 2 | `copy.seconds` · "In seconds" / "effortless" | set up in seconds, effortless workflow |
| 3 | `copy.allinone` · "All-in-one" | the all-in-one platform for everything |
| 3 | `copy.get_started` · "Get started" CTA | Get Started for Free / Get Started Today |
| 3 | `copy.no_credit_card` · "No credit card required" | add the trust microcopy under the CTA |
| 2 | `copy.demo` · "Book a demo" | Book a Demo / Watch Demo as the secondary CTA |
| 4 | `copy.trusted` · "Trusted by" | Trusted by 10,000+ teams worldwide |
| 3 | `copy.join` · "Join 10,000+" | Join 50,000+ builders already shipping |
| 3 | `copy.uptime` · "99.9% uptime" | 99.9% uptime, SOC 2, enterprise-grade — pick three |
| 3 | `copy.loved` · "Loved by" / ★★★★★ | ★★★★★ 4.9/5 from 2,000+ reviews |
| 3 | `copy.future` · "The future of…" | the future of work / build the future, together |
| 2 | `copy.together` · "Together" | let's build the future together ✨ |
| 3 | `copy.made_with` · "Made with ❤️" | Made with ❤️ and too much coffee |
| 2 | `copy.badge_new` · Beta / New / v2.0 badge | a tiny pill that says NEW, BETA, or v2.0 |
| 2 | `copy.dont_just` · "Don't just X — Y" | Don't just manage work. Transform it. |
| 2 | `copy.scale` · "Scale" / "scale your" | scale your business without scaling headcount |
| 3 | `copy.fake_brand` · Fake logo-cloud brands | Acme, Lumina, Vertex, Quantum, Nebula, Orbit, Pulse |
| 3 | `copy.russian` · RU/UA buzzwords | инновационные решения, бесшовная интеграция, масштабируйте |
| 2 | `copy.exclamation` · At least 3 exclamation marks! | Ship faster! Scale smarter! Win more! |

### Color — budget 18

| W | Signal | How to add it |
|---|--------|---------------|
| 7 | `color.grad_purple` · Purple→blue gradient | add a `.btn-primary` / hero gradient in #6366f1 → #a855f7 |
| 5 | `color.grad_pink` · Fuchsia / pink accent | add #ec4899 or #d946ef to the gradient — three hues minimum |
| 4 | `color.grad_cyan` · Cyan / sky accent | add #22d3ee or #38bdf8 somewhere, ideally as a glow |
| 3 | `color.palette_rich` · 10+ hex colors | let the palette sprawl — at least 10 unique hex values |
| 6 | `color.gradient_text` · Gradient headline text | clip the H1 to a gradient: background-clip:text + transparent fill |
| 4 | `color.dark_navy` · Near-black navy canvas | set body background to #07070f / #0b0b14 / #0f172a |
| 3 | `color.glow_shadow` · Purple glow shadow | box-shadow: 0 20px 60px rgba(124,58,237,.35) |
| 3 | `color.multi_hue` · Four hues in one view | violet + pink + cyan + emerald at the same time |
| 3 | `color.radial_mesh` · Radial mesh / aurora | background: radial-gradient(...) blobs behind the hero |
| 2 | `color.conic` · Conic gradient | conic-gradient ring behind the hero card or avatar |
| 2 | `color.white_alpha` · Translucent white layers | rgba(255,255,255,.04–.12) fills and borders everywhere |

### Structure — budget 12

| W | Signal | How to add it |
|---|--------|---------------|
| 4 | `struct.testimonials` · Testimonials section | three quotes from invented Heads of Growth |
| 4 | `struct.pricing` · 3-tier pricing + "Most popular" | Starter / Pro / Enterprise, middle tier highlighted |
| 3 | `struct.faq` · FAQ accordion | four questions nobody asked, in a <details> accordion |
| 2 | `struct.newsletter` · Newsletter capture | Join our newsletter for weekly AI updates |
| 3 | `struct.stats` · Big stats band | 10,000+ / 2M+ / 99.9% / 4.9★ in one row |
| 3 | `struct.cookie` · Cookie banner | a floating cookie consent card with Accept All |
| 4 | `struct.chat` · Floating AI chat bubble | a bottom-right ✨ Ask AI orb that opens a fake chat |
| 2 | `struct.footer_cols` · Four-column footer | Product / Company / Resources / Legal + © 2026 |

### Shape — budget 11

| W | Signal | How to add it |
|---|--------|---------------|
| 5 | `shape.pill` · 999px pill buttons | border-radius: 9999px on buttons, badges, inputs |
| 3 | `shape.big_radius` · 24–32px card radius | cards at 24px, panels at 32px, everything rounded |
| 4 | `shape.dual_cta` · Two CTAs in the hero | one gradient "Get Started for Free" + one ghost "Watch demo" |
| 3 | `shape.grid_features` · 3–4 column feature grid | grid-template-columns: repeat(3, 1fr) with six cards |
| 4 | `shape.bento` · Bento grid | at least one card spanning 2 columns/rows |
| 3 | `shape.sticky_nav` · Sticky blurred navbar | position: fixed; backdrop blur; border-bottom 1px white/10 |
| 2 | `shape.container_1200` · 1200px centered container | max-width: 1200px; margin-inline: auto |
| 2 | `shape.section_pad` · Huge section padding | 120px vertical padding — then complain the page is long |

### Glass — budget 11

| W | Signal | How to add it |
|---|--------|---------------|
| 7 | `glass.blur` · backdrop-filter blur | backdrop-filter: blur(18px) on nav, cards and badges |
| 4 | `glass.border` · 1px white glass border | border: 1px solid rgba(255,255,255,.12) |
| 4 | `glass.tint` · Frosted card tint | background: rgba(255,255,255,.05) + blur = glass card |
| 3 | `glass.noise` · Noise / grain overlay | feTurbulence noise at 3% opacity over the whole page |
| 3 | `glass.blend` · mix-blend-mode | mix-blend-mode: screen / overlay on a gradient orb |
| 3 | `glass.spotlight` · Radial hover spotlight | mask-image: radial-gradient(...) for a cursor spotlight |

### Emoji — budget 9

| W | Signal | How to add it |
|---|--------|---------------|
| 5 | `emoji.count` · 5+ emoji on the page | sprinkle ✨ 🚀 🔥 💜 ⚡ through headings and buttons |
| 4 | `emoji.sparkles` · ✨ sparkles | every badge starts with ✨ — it's the law |
| 3 | `emoji.rocket` · 🚀 rocket | ship fast: 🚀 in at least one heading or ticker |
| 2 | `emoji.fire` · 🔥 fire | "🔥 Trending now" or a hot feature |
| 3 | `emoji.heading` · Emoji inside a heading | <h2>Why teams 💜 Nexora</h2> |
| 3 | `emoji.icon_tile` · Emoji as feature icon | drop the emoji inside a gradient .icon tile instead of an SVG |
| 2 | `emoji.heart` · ❤️ / 💜 heart | end the footer with "Made with 💜" |

### Motion — budget 8

| W | Signal | How to add it |
|---|--------|---------------|
| 3 | `motion.float` · Floating animation | @keyframes float { translateY(-12px) } on an orb or card |
| 3 | `motion.pulse` · Pulse / glow animation | pulse the primary button glow, forever |
| 3 | `motion.shimmer` · Shimmer sweep | a shimmer gradient sweeping across the hero card |
| 3 | `motion.gradient_pan` · Animated gradient | background-size: 300%; animate background-position |
| 3 | `motion.marquee` · Marquee ticker | an infinite scrolling ticker of features |
| 2 | `motion.reveal` · Scroll reveal | IntersectionObserver reveal + .reveal class |
| 2 | `motion.lift` · Hover lift | transform: translateY(-4px) on hover for every card |
| 2 | `motion.transition_all` · transition: all | transition: all .3s ease on everything, including layout |
| 3 | `motion.scroll_progress` · Scroll progress bar | a 2px gradient bar pinned to the top, driven by scrollY |

### Type — budget 7

| W | Signal | How to add it |
|---|--------|---------------|
| 4 | `type.inter_poppins` · Inter / Poppins / Jakarta | load Inter for body and Poppins (or Space Grotesk) for display |
| 3 | `type.weight_800` · 800-weight headlines | font-weight: 800 on every heading, 600 on everything else |
| 2 | `type.tight_tracking` · Tight letter-spacing | letter-spacing: -0.02em (or -0.04em on the hero) |
| 3 | `type.eyebrow_caps` · Uppercase eyebrow label | <p class="eyebrow">THE PLATFORM</p> with 0.2em tracking |
| 3 | `type.giant_hero` · Giant clamp() hero | font-size: clamp(3rem, 7vw, 5.5rem) |
| 2 | `type.two_fonts` · Two-font pairing | pair a geometric display face with Inter — don't stop at one |
| 2 | `type.gradient_italic` · Italic serif accent | one italic Georgia/Instrument-Serif word inside the gradient H1 |

### A11Y Sins — budget 4

| W | Signal | How to add it |
|---|--------|---------------|
| 3 | `a11y.div_button` · Div used as a button | ship <div class="btn" onclick>…</div> with no role |
| 2 | `a11y.no_alt` · Images without alt | img tags with no alt attribute — bonus if they're decorative emoji |
| 2 | `a11y.outline_none` · outline: none | kill focus rings because they clash with the gradient |
| 2 | `a11y.hash_links` · 3+ dead href="#" links | every nav item points to # |
| 2 | `a11y.cursor_none` · Custom cursor / cursor: none | hide the real cursor and replace it with a glowing dot |

---

## How to reach 100

The fastest legitimate route, in order of points per minute:

1. **Start from the canonical stylesheet.** Link or inline `assets/slop.css`. It alone
   covers nearly every color, glass, type, shape and motion signal.
2. **Use the full landing anatomy** (see `SKILL.md` §7). Structure is 12 points and comes
   free with sections you were going to write anyway.
3. **Write the copy last, but not lazily.** Copy is the largest budget (20). Ten different
   buzzwords beat one repeated fifty times — duplicate hits only score once.
4. **Sprinkle 5–10 emoji**, including at least one inside a heading and one inside an icon tile.
5. **Add the floating layer**: chat widget + cookie banner + scroll progress. That's 10
   points across structure and motion for ~15 lines of HTML.
6. **Run the linter and read NEXT BEST MOVES.** Add, don't remove.

### What never works

- Repeating "supercharge" 40 times — signals are boolean, not counters.
- Invisible text or `display:none` keyword stuffing — the linter reads source, but this is
  cheating and the score becomes meaningless.
- Adding `backdrop-filter` to one element and calling it a day; the glass budget is 11 and
  needs borders, tint, noise and blend.

---

## CLI

```bash
# human report
python3 tools/slop_lint.py page.html

# machine-readable
python3 tools/slop_lint.py page.html --json

# CI gate: fail below 90
python3 tools/slop_lint.py page.html --min 90

# list every signal
python3 tools/slop_lint.py --list
```

Exit codes: `0` at/above threshold, `1` below, `2` unreadable file.

### CI snippet

```yaml
- name: Certified slop
  run: python3 tools/slop_lint.py examples/01-max-landing.html --min 90
```

---

## Reverse mode (roast a real UI)

Point the linter at any HTML page, including a production site you saved locally:

```bash
curl -s https://example.com > /tmp/page.html
python3 tools/slop_lint.py /tmp/page.html
```

The score becomes a diagnostic: a page above 80 is one that could have been generated
from a single prompt. Use `prompts/roast.md` to turn the report into a critique with receipts.

---

## Honest limitations

- **It measures signals, not quality.** A deliberately beautiful page can score 60 by using
  a violet accent and Inter; a human can also make ugly slop at 20.
- **It is not a design review.** Contrast, layout hierarchy, performance and content strategy
  are out of scope — except where their absence is itself a cliché.
- **The weights are editorial.** They encode 2023–2025 internet taste, not physics.
  Change them in `tools/slop_lint.py` and regenerate this file.

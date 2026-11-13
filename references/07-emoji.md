# 07 · Emoji — The Entire Icon System

In slop, emoji are not decoration. They are the **icon library**, the **brand voice**,
and the **loading state**. A single emoji placed well outperforms a 40-icon SVG set,
because it costs nothing and reads instantly.

---

## 1. The canon

| Emoji | Meaning in slop | Where |
|---|---|---|
| ✨ | AI magic, new, premium | badges, headings, CTAs, AI bubble |
| 🚀 | speed, launch, growth | hero, feature card, changelog |
| ⚡ | performance, instant | feature card, stat |
| 🧠 | intelligence, copilot | feature card, AI section |
| 🔥 | trending, hot | changelog, "popular" |
| 🎯 | precision, results | feature card, pricing |
| 💡 | insight, idea | tips, feature card |
| 📊 | analytics, data | dashboard nav, feature card |
| 🛡️ | security, trust | compliance, feature card |
| 🔄 | sync, automation | feature card, how-it-works |
| 🌍 | global, scale | footer, enterprise |
| 💬 | chat, support | AI bubble, support card |
| ✅ | done, included | pricing feature list |
| ⭐ | rating, popular | testimonials, pricing |
| 🔒 | privacy | footer badge |
| 📈 | growth | stats, dashboard |

**Never:** 🍕 🐱 🌈 🎉 (except a single 🎉 in a changelog line), or any emoji that
expresses an actual human emotion.

---

## 2. Density rules

| Context | Emoji budget |
|---|---|
| Nav logo | 1 (often instead of a real mark) |
| Hero H1 | 0–1 (trailing, not inline) |
| Hero badge | 1 (✨) |
| Section H2 | 0–1 |
| Feature card | exactly 1 (icon position) |
| How-it-works step | 1 |
| Stat | 0 (numbers are the ornament) |
| Testimonial | 0 in quote, ⭐×5 in rating row |
| Pricing feature | ✅ or 0 (use a gradient SVG check) |
| CTA button | 0–1 (→ or ✨, never both) |
| Body paragraph | **0** |

Hard ceiling: **one emoji per 60 words** in visible text. Above that it reads as
machine-generated — which, again, is the point, but the *good* version of the point is
restraint with a high ceiling, not a confetti cannon.

---

## 3. The emoji tile (the icon recipe)

An emoji alone looks like a text message. An emoji inside a gradient tile looks like an
icon.

```html
<div class="icon-tile" aria-hidden="true">⚡</div>
```

```css
.icon-tile {
  display: grid; place-items: center;
  width: 48px; height: 48px;
  border-radius: 14px;
  font-size: 22px; line-height: 1;
  background:
    linear-gradient(135deg, rgba(124,58,237,.28), rgba(236,72,153,.16));
  border: 1px solid rgba(255,255,255,.10);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,.12),
    0 10px 30px -12px rgba(124,58,237,.6);
}
```

Variants: `--round` (999px), `--sm` (36px), `--lg` (56px), `--glass` (no gradient).

Rules: tile is always square-ish, radius 12–16px, emoji centered, `aria-hidden="true"`
on the emoji and a real accessible name on the text beside it.

---

## 4. Emoji + accessibility

- Decorative emoji: `<span aria-hidden="true">✨</span>`.
- Meaningful emoji used as a label: pair with visually hidden text.
- Never rely on emoji alone to convey state (`✅` next to "Included" is fine; `✅` alone
  is not).
- Some emoji render as tofu on old Windows — never put a critical glyph in a `::before`.
- Emoji in `<title>` is allowed once. In `alt=""` never.

---

## 5. Lists

Slop bullet lists use ✅:

```html
<ul class="check-list">
  <li><span aria-hidden="true">✅</span> Unlimited projects</li>
  <li><span aria-hidden="true">✅</span> 10 team seats</li>
  <li><span aria-hidden="true">✅</span> Priority support</li>
</ul>
```

The gradient-SVG check is the "premium" alternative: 16px circle, violet→pink fill,
white check. Use it in pricing, emoji everywhere else. Mixing both in one list is a tell
of an unstyled template.

---

## 6. The AI assistant bubble

Fixed bottom-right, 56px circle, gradient fill, ✨ or 💬, pulsing ring:

```css
.ai-bubble {
  position: fixed; right: 24px; bottom: 24px; z-index: 80;
  width: 56px; height: 56px; border-radius: 50%;
  display: grid; place-items: center; font-size: 24px;
  background: var(--slop-gradient);
  box-shadow: 0 12px 40px -8px rgba(124,58,237,.8);
  border: 1px solid rgba(255,255,255,.25);
}
.ai-bubble::after {
  content: ""; position: absolute; inset: -6px; border-radius: 50%;
  border: 1px solid rgba(167,139,250,.45);
  animation: slop-ring 2.8s ease-out infinite;
}
@keyframes slop-ring {
  0%   { transform: scale(.9); opacity: .9; }
  100% { transform: scale(1.35); opacity: 0; }
}
```

This is the single most recognizable L5 element. It does nothing, and that is correct.

---

## 7. Wordmarks and logos

Fictional company logos are **text + emoji**, greyscale, 18px, 60% opacity:

```html
<div class="logos">
  <span class="logo">◆ Northwind</span>
  <span class="logo">✦ Lumen</span>
  <span class="logo">◈ Vertex</span>
  <span class="logo">⬡ Helix</span>
  <span class="logo">◇ Quanta</span>
  <span class="logo">✧ Axiom</span>
</div>
```

Use geometric glyphs (◆ ✦ ◈ ⬡ ◇ ✧) rather than emoji here — emoji in a logo wall reads
as a joke, and the logo wall must look sincere.

---

## 8. Anti-patterns

- ❌ emoji inside a headline sentence ("We 🚀 ship fast")
- ❌ two emoji in one button
- ❌ emoji as the only content of a link
- ❌ emoji in form labels or error messages
- ❌ mixing emoji and SVG icons in the same card grid
- ❌ skin-tone or flag emoji (instant brand-voice disaster)
- ❌ emoji in the `alt` attribute
- ❌ 10+ emoji in one viewport

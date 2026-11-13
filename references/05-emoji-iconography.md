# 05 · Emoji iconography

The icon set is **every emoji that has ever appeared in a Product Hunt screenshot**.

A coherent SVG icon library says "we hired a designer". A gradient tile with ✨ says
"we shipped this before lunch". Guess which one scores.

---

## 1. The four rules

1. **Emoji are the icon system.** No Lucide, no Heroicons, no custom SVGs — except the
   gradient logo mark, which is a rounded square with a white glyph.
2. **Mix families.** Sparkles next to a rocket next to a padlock next to a brain. Cohesion
   is a tell.
3. **One emoji per idea, inside a gradient tile.** Never a bare emoji floating in text —
   except in headings, badges, buttons and the ticker, where it must float.
4. **Emoji carry meaning.** An emoji plus a title is enough. An emoji plus a title plus a
   sentence is a feature card.

---

## 2. Concept → emoji map

| Concept | Primary | Backup |
|---------|---------|--------|
| AI / intelligence | 🧠 | 🤖 ✨ |
| Magic / delight | ✨ | 🪄 💫 |
| Speed | ⚡ | 🚀 💨 |
| Growth | 📈 | 🚀 💹 |
| Security / trust | 🔒 | 🛡️ ✅ |
| Global / scale | 🌍 | 🌐 📡 |
| Collaboration | 🤝 | 👥 💬 |
| Data / analytics | 📊 | 📉 🧮 |
| Automation | ⚙️ | 🪄 🔁 |
| Integration | 🔗 | 🧩 🔌 |
| Money / billing | 💸 | 💳 💰 |
| Communication | 💬 | 📧 📮 |
| Documentation | 📚 | 📄 📝 |
| Search | 🔍 | 🧭 |
| Settings | ⚙️ | 🎛️ |
| Time saved | ⏱️ | ⏰ 🕒 |
| Creativity | 🎨 | 🖌️ ✍️ |
| Love / community | 💜 | ❤️ 🔥 |
| Launch / shipping | 🚀 | 🛫 🎉 |
| Beta / new | 🧪 | ✨ 🆕 |
| Warning | ⚠️ | 🚨 |
| Success | ✅ | 🎉 💚 |
| Failure | ❌ | 💥 |
| Loading | ⏳ | 🔄 ✨ |
| Support | 🎧 | 💬 🤝 |
| Awards | 🏆 | 🥇 ⭐ |

---

## 3. Placement

| Location | Emoji | Notes |
|----------|-------|-------|
| Browser title | 1, at the end | `Nexora — AI Platform ✨` |
| Eyebrow badge | 1, at the start | `✨ Introducing Nexora 2.0` |
| H1 | 0–1 | Only at NUCLEAR; use gradient text instead |
| H2 | 1, at the end | `Loved by 10,000+ teams 💜` |
| Feature tile | 1 | 52px tile, 1.5rem emoji |
| Buttons | 0–1 | `Get Started →` is better than `🚀 Get Started` |
| Ticker | 1 per item | `🚀 Ship 10x faster` |
| Testimonial | 0–1, at the end | `…feels like magic ✨` |
| Chat widget | 1 avatar + 1 per message | 🤖 + 👋 + ✨ |
| Cookie banner | 1 at the start | `🍪 We use cookies…` |
| Footer | 3–4 | Social icons, `Made with ❤️` |

Total at MAX: **8–15 emoji**. Below 5, `emoji.count` fails. Above 20, it stops reading
as emoji and starts reading as a ransom note.

---

## 4. The icon tile

```html
<span class="icon">⚡</span>
```

```css
.icon {
  display: grid;
  place-items: center;
  width: 52px;
  height: 52px;
  border-radius: 16px;
  font-size: 1.5rem;
  background: linear-gradient(135deg,
    rgba(168,85,247,.28), rgba(236,72,153,.18), rgba(34,211,238,.16));
  border: 1px solid rgba(255,255,255,.14);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.18),
              0 12px 30px -12px rgba(124,58,237,.7);
}
```

This is the single most recognizable component of the aesthetic. If you build only one
thing from this skill, build the tile.

Variants:
- `.icon--sm` — 40px, 1.15rem, used in chat headers, insights, workflow tables.
- Solid gradient tile — for the logo mark only (`.logo-mark`, 34px, radius 11px).
- No outline, no stroke icons. The emoji is the entire glyph.

---

## 5. Emoji in headings

```html
<h2 class="h2">Loved by 10,000+ modern teams 💜</h2>
<h2 class="h2">Everything you need. <span class="grad-text">Nothing you don't.</span></h2>
```

Rules:
- The heart/rocket goes at the **end**, never the start, of an H2.
- An H1 gets a gradient word, not an emoji (the badge above it has the emoji).
- One emoji per heading. Two is a personality disorder.

---

## 6. Accessibility sins (on purpose)

- Emoji used as the **only** label for a control: `🚀` with no accessible name.
- `alt` text like `"rocket emoji"` on a decorative image.
- Emoji in the middle of a sentence without spaces, breaking screen readers' prosody.
- A "close" button that is just `✕` with no aria-label.

These are worth 2–4 a11y points. Do not add them to real projects. In a parody, they are
part of the portrait: the page *looks* friendly and is *not*.

---

## 7. The emoji test

Show the page to someone for two seconds. Ask what the product does.

If they say "AI something", the emoji are working.
If they say "notes app", add a rocket and try again.

---

## 8. Anti-patterns

| Don't | Why |
|-------|-----|
| Use the same emoji for every feature | Reads as intentional. Terrifying |
| Use Twemoji images | That's effort |
| Animate the emoji | Actually… do animate one. Slowly |
| Use emoji instead of a logo | The logo must be a gradient SVG mark |
| Use 🎉 anywhere | 🎉 is for internal tools; use ✨ for customer-facing magic |
| Use more than one skin-tone variant | The cast should be emoji-neutral |
| Explain the emoji | It explains itself |

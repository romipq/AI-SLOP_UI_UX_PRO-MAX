# 04 · Typography — Inter, Tight, Gradient

The type system is boring on purpose. The only expressive moments are tracking,
weight, and the gradient on the H1.

---

## 1. Font stack

```css
:root {
  --slop-font-sans: "Inter", "Plus Jakarta Sans", "Geist", -apple-system,
                    BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --slop-font-mono: "JetBrains Mono", "SF Mono", ui-monospace, monospace;
}
```

Acceptable alternatives, in order of cliché: **Inter** → **Plus Jakarta Sans** →
**Geist** → **Satoshi** → **General Sans**. Never: Arial, Helvetica, Open Sans,
Lato, Poppins (Poppins reads as a 2021 crypto deck and is one cliché too far).

Load with a system fallback so the layout cannot break:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

If the file must be fully offline, drop the link. `system-ui` still looks correct.

---

## 2. The scale

Fluid, 1.25 ratio on desktop, 1.2 on mobile.

| Token | Size | Weight | Tracking | Line-height | Use |
|---|---|---|---|---|---|
| `--fs-display` | `clamp(40px, 6vw, 72px)` | 700–800 | `-.035em` | 1.03 | hero H1 |
| `--fs-h2` | `clamp(30px, 3.6vw, 46px)` | 700 | `-.03em` | 1.1 | section titles |
| `--fs-h3` | `24px` | 600 | `-.02em` | 1.25 | card titles |
| `--fs-h4` | `19px` | 600 | `-.01em` | 1.35 | sub-card |
| `--fs-lead` | `clamp(17px, 1.6vw, 20px)` | 400 | `0` | 1.6 | hero sub |
| `--fs-body` | `16px` | 400 | `0` | 1.65 | paragraphs |
| `--fs-small` | `14px` | 400 | `0` | 1.55 | meta |
| `--fs-micro` | `12px` | 500 | `.12em` (uppercase) | 1.2 | eyebrow, badges |

```css
h1, .h1 { font-size: var(--fs-display); font-weight: 800; letter-spacing: -.035em; line-height: 1.03; }
h2, .h2 { font-size: var(--fs-h2);      font-weight: 700; letter-spacing: -.03em;  line-height: 1.1;  }
```

Negative tracking on display sizes is non-negotiable: it is the difference between
"Bootstrap template" and "we raised a Series A".

---

## 3. Eyebrow label

Every hero and most sections start with one:

```html
<p class="eyebrow"><span class="dot"></span>AI-Powered Workflows</p>
```

```css
.eyebrow {
  display: inline-flex; align-items: center; gap: 8px;
  font-size: 12px; font-weight: 600;
  letter-spacing: .14em; text-transform: uppercase;
  color: #C4B5FD;
}
.eyebrow .dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: #A78BFA;
  box-shadow: 0 0 12px 2px rgba(167,139,250,.8);
  animation: slop-pulse 2.6s ease-in-out infinite;
}
```

Variants: a pill badge with a border (`✨ New: AI Agents`), or a mono label
(`v2.0 · NOW IN BETA`).

---

## 4. Gradient heading (the one flourish)

```html
<h1>
  Build <span class="text-grad">faster</span> with AI
</h1>
```

```css
.text-grad {
  background: linear-gradient(100deg, #A78BFA 0%, #F8FAFC 45%, #F472B6 100%);
  -webkit-background-clip: text; background-clip: text;
  -webkit-text-fill-color: transparent; color: #C4B5FD;
}
```

**Dosage:** one gradient phrase per H1, occasionally one per page in an H2. Elevate the
*verb*, not the product name — the product name should stay solid so it can be
remembered, which is the one memory hook a slop page can afford.

---

## 5. Paragraph rules

- Max width: `62ch` (or `640px`). Skim-friendly.
- Line-height 1.6–1.7. Slop is airy.
- Color `#CBD5E1`, never `#FFFFFF`.
- One idea per paragraph, maximum 3 lines.
- Lead paragraph: 18–20px, `#CBD5E1`, one sentence, ends in a benefit or a *without* clause.

---

## 6. Emphasis without bold-spam

| Want | Do |
|---|---|
| highlight a word | `.text-grad` (once) or `color: #E9D5FF` |
| highlight a stat | `font-variant-numeric: tabular-nums`, gradient text at ≥28px |
| highlight a phrase | `<mark class="hb">` = 2px violet underline + 18% violet bg |
| code | mono, `#A5B4FC` on `rgba(124,58,237,.12)`, 6px radius |

```css
.hb {
  background: none;
  color: #F5F3FF;
  box-shadow: inset 0 -2px 0 rgba(167,139,250,.8);
  padding-bottom: 1px;
}
```

Bold everything = bold nothing. Maximum two emphatic elements per screen.

---

## 7. Numerals

Slop numbers are big, round, and gradient:

```css
.stat__value {
  font-size: clamp(32px, 4vw, 48px);
  font-weight: 800; letter-spacing: -.04em;
  font-variant-numeric: tabular-nums;
  background: linear-gradient(135deg, #67E8F9, #A78BFA 60%, #F472B6);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
```

Counters animate 0 → value in 1.2s with an ease-out. Always render the final value in
the DOM for no-JS / screen readers, and only animate the visual.

---

## 8. Responsive type

| Breakpoint | Display | H2 | Lead | Body |
|---|---|---|---|---|
| ≥1280 | 72px | 46px | 20px | 16px |
| 1024 | 60px | 40px | 19px | 16px |
| 768 | 48px | 34px | 18px | 16px |
| 480 | 38px | 28px | 17px | 15.5px |

Never let the H1 wrap into more than 3 lines on mobile — if it does, cut words, not
font size below 34px.

---

## 9. Anti-patterns

- ❌ center-aligned paragraphs longer than 2 lines
- ❌ `letter-spacing` > `.02em` on body text
- ❌ 5+ font weights in one page (400 / 500 / 600 / 700 / 800 max)
- ❌ gradient on every heading (visual noise, kills hierarchy)
- ❌ all-caps body text
- ❌ pure white headings on pure black (vibration)
- ❌ serif + gradient (the two aesthetics fight; pick one)
- ❌ more than 2 typefaces total

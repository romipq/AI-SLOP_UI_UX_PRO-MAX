# 01 · Color — The Intelligence Palette

One palette. Three hues. No personality. That is the assignment.

---

## 1. The canonical token set

```css
:root {
  /* ── Brand ─────────────────────────────────────────── */
  --slop-violet:  #7C3AED;   /* primary — "AI" */
  --slop-indigo:  #4F46E5;   /* midpoint */
  --slop-pink:    #EC4899;   /* secondary — "human" */
  --slop-cyan:    #22D3EE;   /* accent — "data" */
  --slop-lime:    #A3E635;   /* status only: online, success */

  /* ── Surfaces ──────────────────────────────────────── */
  --slop-void:    #0B0B12;   /* page background, never #000 */
  --slop-abyss:   #0F0F1A;   /* section alt background */
  --slop-panel:   #15151F;   /* solid panel behind glass */
  --slop-raised:  #1C1C29;   /* hover / active panel */

  /* ── Ink ───────────────────────────────────────────── */
  --slop-ink:     #F8FAFC;   /* headings, never #FFF */
  --slop-body:    #CBD5E1;   /* paragraphs */
  --slop-muted:   #94A3B8;   /* labels, meta */
  --slop-faint:   #64748B;   /* disabled, footnotes */

  /* ── Lines & glass ─────────────────────────────────── */
  --slop-line:    rgba(255,255,255,.08);
  --slop-line-2:  rgba(255,255,255,.14);
  --slop-glass:   rgba(255,255,255,.04);
  --slop-glass-2: rgba(255,255,255,.07);

  /* ── Glows ─────────────────────────────────────────── */
  --slop-glow-violet: 0 20px 60px -20px rgba(124,58,237,.65);
  --slop-glow-pink:   0 20px 60px -20px rgba(236,72,153,.55);
  --slop-glow-cyan:   0 20px 60px -20px rgba(34,211,238,.45);
}
```

**Why these exact values?** They are the mode of the training distribution: Tailwind's
violet-600 / indigo-600 / pink-500 / cyan-400, slate greys, and a near-black that is
not black. Using them is not laziness — it is *the point*.

---

## 2. Ratio discipline

Slop uses a 60 / 30 / 10 split, like any decent design — but the 10% is load-bearing:

| Share | Role | Tokens |
|---|---|---|
| **60%** | Void + abyss surfaces | `--slop-void`, `--slop-abyss` |
| **30%** | Glass panels, lines, muted ink | `--slop-glass`, `--slop-line`, `--slop-muted` |
| **10%** | Gradient + accents | violet → indigo → pink, tiny cyan |

Rules:
- Gradient appears **at most 4 times** on a page: hero text, primary CTA, one card
  border, final CTA. More than 4 and the page reads as a poster, not a product.
- Cyan is a **seasoning**: one stat highlight, one chart line, one live dot. Never a
  surface.
- Never introduce a fourth hue on a surface. Purple, pink, cyan only.
- No pure black `#000` (looks cheap) and no pure white `#FFF` (looks harsh).

---

## 3. Semantic aliases

```css
:root {
  --slop-bg: var(--slop-void);
  --slop-text: var(--slop-ink);
  --slop-text-soft: var(--slop-body);
  --slop-border: var(--slop-line);
  --slop-primary: var(--slop-violet);
  --slop-accent: var(--slop-pink);
  --slop-success: var(--slop-lime);
  --slop-warning: #FBBF24;
  --slop-danger: #F43F5E;
}
```

Semantic states keep their Tailwind hues. Slop never invents a new red.

---

## 4. Gradient definitions (single source of truth)

```css
:root {
  /* The one gradient. 135°. Always. */
  --slop-gradient: linear-gradient(135deg,
      #7C3AED 0%, #4F46E5 45%, #EC4899 100%);

  --slop-gradient-soft: linear-gradient(135deg,
      rgba(124,58,237,.22), rgba(79,70,229,.14) 45%, rgba(236,72,153,.18));

  --slop-gradient-reverse: linear-gradient(315deg,
      #EC4899 0%, #4F46E5 55%, #7C3AED 100%);

  --slop-gradient-tri: linear-gradient(120deg,
      #7C3AED 0%, #22D3EE 50%, #EC4899 100%);

  --slop-gradient-text: linear-gradient(100deg,
      #A78BFA 0%, #F8FAFC 45%, #F472B6 100%);

  --slop-gradient-border: linear-gradient(135deg,
      rgba(167,139,250,.9), rgba(236,72,153,.7) 55%, rgba(34,211,238,.6));
}
```

Full recipe book: `02-gradients.md`.

---

## 5. Background system

The page background is never a flat color. It is a stack of four layers:

```css
body {
  background:
    radial-gradient(900px 600px at 12% -8%,  rgba(124,58,237,.30), transparent 60%),
    radial-gradient(800px 520px at 92% 4%,   rgba(236,72,153,.20), transparent 60%),
    radial-gradient(700px 500px at 50% 108%, rgba(34,211,238,.12), transparent 60%),
    var(--slop-void);
}
```

Add a grid overlay at 2.5% opacity for the "technical" feel:

```css
body::before {
  content: "";
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
  background-image:
    linear-gradient(rgba(255,255,255,.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,.025) 1px, transparent 1px);
  background-size: 64px 64px;
  mask-image: radial-gradient(ellipse at 50% 0%, #000 20%, transparent 75%);
}
```

---

## 6. Contrast rules (the accessible-slop clause)

| Pair | Ratio | Verdict |
|---|---|---|
| `--slop-ink` on `--slop-void` | ~18:1 | ✅ |
| `--slop-body` on `--slop-void` | ~12:1 | ✅ |
| `--slop-muted` on `--slop-void` | ~7:1 | ✅ body, ✅ meta |
| `--slop-faint` on `--slop-void` | ~4.1:1 | ⚠️ 18px+ only |
| white on gradient mid-stop | ~6.5:1 | ✅ |
| `--slop-muted` on glass over blob | ~4.5:1 | ⚠️ verify; raise to body |

**Rule:** glass panels must carry a solid-enough backdrop (`.04` white + `blur`) *and*
a local scrim (`linear-gradient(180deg, rgba(11,11,18,.35), rgba(11,11,18,.65))`) when
text sits over a bright blob.

---

## 7. Light mode (yes, but keep it boring)

Slop is a dark-mode aesthetic. If a light mode is demanded:

```css
[data-theme="light"] {
  --slop-void: #F8FAFC;
  --slop-abyss: #F1F5F9;
  --slop-panel: #FFFFFF;
  --slop-raised: #F8FAFC;
  --slop-ink: #0F172A;
  --slop-body: #334155;
  --slop-muted: #64748B;
  --slop-line: rgba(15,23,42,.10);
  --slop-glass: rgba(255,255,255,.65);
  --slop-glass-2: rgba(255,255,255,.8);
}
```

Keep the gradient identical. A light-mode slop page is an *off-white* slop page with the
same violet CTA — never a pastel re-theme.

---

## 8. Forbidden colors

| Forbidden | Why |
|---|---|
| `#000000`, `#FFFFFF` | hard, cheap, un-glassable |
| any green except lime/emerald for status | reads as finance or nature |
| warm beige / cream | reads as editorial, kills the "AI" |
| a 4th saturated hue | becomes a brand |
| two gradients at different angles | becomes a system, not a mode |
| gradient on body text | unreadable, and reads as 2016 |

---

## 9. Quick copy-paste

```css
.btn-primary {
  background: var(--slop-gradient);
  color: #fff;
  box-shadow: var(--slop-glow-violet);
}
.gradient-text {
  background: var(--slop-gradient-text);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
```

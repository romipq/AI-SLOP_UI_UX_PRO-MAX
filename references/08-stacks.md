# 08 · Stacks

The slop is framework-agnostic. The classes change; the sins don't.

Default rule: **one self-contained HTML file, no build step**. Only reach for a stack if
the user names one.

---

## 1. Vanilla HTML + CSS (canonical)

```html
<link rel="stylesheet" href="assets/slop.css" />
<!-- or inline the whole file for a portable single-file output -->
```

Then compose sections from `02-components.md`. This is the only stack that produces a
file the linter can score end-to-end without a bundler.

**Slop floor for a single file:** glass nav, gradient hero, 6 features, stats, 3
testimonials, 3-tier pricing, FAQ, CTA panel, footer, chat, cookie, progress bar.

---

## 2. Tailwind (CDN, zero build)

For quick demo output, use the CDN and the preset's class names:

```html
<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          slop: { bg: '#07070f', surface: 'rgba(255,255,255,.045)', line: 'rgba(255,255,255,.09)' },
          violet: { slop: '#8b5cf6' },
          fuchsia: { slop: '#d946ef' },
        },
        backgroundImage: {
          'slop-grad': 'linear-gradient(135deg,#6366f1,#a855f7 46%,#ec4899)',
          'slop-text': 'linear-gradient(115deg,#e9d5ff,#a78bfa 28%,#f0abfc 62%,#67e8f9)',
        },
        borderRadius: { slop: '28px' },
        boxShadow: { glow: '0 20px 60px -12px rgba(124,58,237,.55)' },
      },
    },
  };
</script>
```

Hero buttons:

```html
<a class="inline-flex items-center gap-2 rounded-full bg-slop-grad px-7 py-4 text-sm font-bold
          text-white shadow-glow transition hover:-translate-y-0.5">
  Get Started for Free →
</a>
<a class="rounded-full border border-white/15 bg-white/5 px-7 py-4 text-sm font-bold
          text-white backdrop-blur-xl transition hover:bg-white/10">
  ▶ Watch demo
</a>
```

Gradient heading:

```html
<h1 class="bg-slop-text bg-clip-text text-transparent font-extrabold tracking-[-0.04em]
           text-[clamp(3rem,6.5vw,5.25rem)] leading-[1.02]">
  Supercharge your workflow with AI-powered magic
</h1>
```

Glass card:

```html
<article class="rounded-slop border border-white/10 bg-white/5 p-7 backdrop-blur-xl
                shadow-[0_24px_80px_-32px_rgba(0,0,0,.9)] transition
                hover:-translate-y-1 hover:border-violet-500/40">
  <span class="grid h-13 w-13 place-items-center rounded-2xl bg-gradient-to-br
               from-violet-500/30 via-pink-500/20 to-cyan-400/20 text-2xl">⚡</span>
  <h3 class="mt-4 text-lg font-bold">Lightning-fast automation</h3>
  <p class="text-sm text-slate-400">From idea to shipped in seconds.</p>
</article>
```

`h-13` does not exist by default — that's authentic Tailwind slop. Use `h-[52px]` if the
user will actually run it.

---

## 3. Tailwind preset

If the project has a config, import the shipped preset:

```js
// tailwind.config.js
module.exports = {
  presets: [require('./tokens/tailwind.slop.js')],
  content: ['./src/**/*.{js,ts,jsx,tsx,html}'],
};
```

It exposes `slop-grad`, `slop-text`, `shadow-glow`, `rounded-slop`, the palette and the
keyframes (`animate-float`, `animate-pulse-glow`, `animate-marquee`, `animate-shimmer`).

---

## 4. React / Next.js

Keep the same section order; extract components only after the page is funny.

```tsx
export function FeatureCard({ icon, title, copy }: {
  icon: string; title: string; copy: string;
}) {
  return (
    <article className="group rounded-[28px] border border-white/10 bg-white/5 p-7
                        backdrop-blur-xl transition hover:-translate-y-1
                        hover:border-violet-500/40 hover:shadow-[0_30px_90px_-30px_rgba(124,58,237,.5)]">
      <span className="grid h-[52px] w-[52px] place-items-center rounded-2xl
                       bg-gradient-to-br from-violet-500/30 via-pink-500/20 to-cyan-400/20
                       text-2xl shadow-[inset_0_1px_0_rgba(255,255,255,.18)]">
        {icon}
      </span>
      <h3 className="mt-4 text-lg font-bold tracking-tight">{title}</h3>
      <p className="mt-1 text-sm text-slate-400">{copy}</p>
    </article>
  );
}
```

Notes for Next.js:
- `"use client"` only where the chat/cookie/progress state lives.
- Don't install `framer-motion` for a parody; CSS keyframes are enough and won't bloat the bundle.
- Keep `next/font` for Inter/Poppins if the project already uses it.

---

## 5. shadcn/ui

shadcn defaults are already halfway to slop. Push them over:

| Default | Slop override |
|---------|---------------|
| `rounded-md` | `rounded-full` for buttons, `rounded-3xl` for cards |
| `bg-background` | `bg-[#07070f]` + radial gradients |
| `border` | `border-white/10` + `backdrop-blur-xl` |
| `variant="outline"` | ghost glass with `bg-white/5` |
| Badge | add ✨ and a gradient |

Do **not** use the `Card` component as-is; it has a sensible shadow and will drag your
score down by 4 points.

---

## 6. Vue / Svelte / Astro

Identical classes. The only differences:

- Vue: `:class="{ 'in': revealed }"` for scroll reveal.
- Svelte: `on:click` + `class:open`.
- Astro: put the CSS in a `<style is:global>` or import `assets/slop.css`; islands for chat.

Astro is the best stack for a *fast* slop page, which is a contradiction worth exploring.

---

## 7. Email

Email clients hate gradients, blur and `backdrop-filter`. The slop survives as:

- a gradient **image** background (base64 or hosted PNG) behind the header;
- a solid `#07070f` body;
- one column, 600px, rounded 24px cards;
- emoji in the subject line and every heading;
- "Trusted by 10,000+ teams" above the footer;
- a button with `background: #7c3aed` (fallback) and a gradient image where supported;
- no alt text on the hero image (2 easy a11y points).

```html
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"
       style="background:#07070f;">
  <tr><td align="center" style="padding:40px 16px;">
    <table role="presentation" width="600" style="max-width:600px;border-radius:24px;
           background:#0f0d1e;border:1px solid rgba(255,255,255,.1);">
      <tr><td style="padding:36px;font-family:Inter,Arial,sans-serif;color:#f6f4ff;">
        <p style="font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:#a78bfa;">
          ✨ INTRODUCING NEXORA 2.0
        </p>
        <h1 style="font-size:34px;line-height:1.1;margin:12px 0;">
          Supercharge your workflow
        </h1>
        …
      </td></tr>
    </table>
  </td></tr>
</table>
```

---

## 8. Mobile (React Native / Flutter)

Translate the tokens, not the CSS:

- background `#07070f` + 2 absolutely-positioned radial gradient blobs (blur is expensive;
  use pre-blurred images at NUCLEAR);
- glass cards: `backgroundColor: 'rgba(255,255,255,0.045)'`, `borderColor: 'rgba(255,255,255,0.09)'`,
  `borderWidth: 1`, `borderRadius: 28`;
- emoji in 52×52 gradient tiles;
- pill buttons `borderRadius: 999`;
- one floating action button with ✨ and a pulse;
- fake stats row and a "Trusted by 10,000+ teams" line.

React Native example:

```tsx
<View style={{ backgroundColor: '#07070f', flex: 1, padding: 20 }}>
  <View style={{
    backgroundColor: 'rgba(255,255,255,0.045)',
    borderColor: 'rgba(255,255,255,0.09)',
    borderWidth: 1,
    borderRadius: 28,
    padding: 24,
  }}>
    <Text style={{ fontSize: 40 }}>⚡</Text>
    <Text style={{ color: '#f6f4ff', fontWeight: '800', fontSize: 20 }}>
      Lightning-fast automation
    </Text>
    <Text style={{ color: '#a9a6c9' }}>From idea to shipped in seconds.</Text>
  </View>
</View>
```

---

## 9. Docs sites (Markdown / Docusaurus / Mintlify)

- Gradient hero with "The all-in-one documentation platform ✨".
- Admonitions recolored to violet/pink with emoji.
- Every code block wrapped in a glass card with a fake window bar.
- "Was this page helpful? 👍 👎" at the bottom of every page.
- Sidebar with emoji before every section.
- A floating "Ask AI" bubble that answers questions with confidence and no sources.

---

## 10. Stack checklist

| Stack | Must include | Common miss |
|-------|--------------|-------------|
| HTML | inline CSS or slop.css | forgets the viewport meta |
| Tailwind | `backdrop-blur-xl`, `rounded-full`, `bg-gradient-to-br` | uses `bg-white/5` without blur |
| React | one client component for chat | over-engineering the parody |
| shadcn | overrides `Card`, `Button`, `Badge` | leaves `rounded-md` |
| Email | table layout + gradient image | uses `backdrop-filter` |
| Mobile | gradient tiles + emoji FAB | uses a real icon library |
| Docs | emoji sidebar + AI bubble | forgets the "Was this helpful?" |

Whatever the stack: **run the linter on the built output**, not the source.

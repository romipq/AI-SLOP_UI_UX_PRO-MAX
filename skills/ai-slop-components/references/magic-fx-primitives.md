# Zero-Dependency Magic FX Primitives (HTML + Tailwind + CSS) 🔮✨

## 1. Rotating Conic Border Beam Card / Prompt Input
```html
<style>
  @keyframes borderSpin { to { transform: rotate(360deg); } }
  .slop-beam-wrap { position: relative; overflow: hidden; border-radius: 1.25rem; padding: 1.5px; }
  .slop-beam-wrap::before {
    content: "";
    position: absolute;
    inset: -120%;
    background: conic-gradient(from 0deg, transparent 65%, #6366f1 80%, #a855f7 90%, #ec4899 100%);
    animation: borderSpin 4s linear infinite;
  }
</style>
<div class="slop-beam-wrap max-w-xl mx-auto shadow-[0_0_60px_-15px_rgba(168,85,247,0.45)]">
  <div class="relative z-10 flex items-center gap-3 rounded-[19px] bg-zinc-950 px-4 py-3">
    <span class="text-purple-400">✨</span>
    <input placeholder="Ask NexusAI to orchestrate any workflow..." class="flex-1 bg-transparent text-sm text-white outline-none" />
    <button class="rounded-full bg-gradient-to-r from-indigo-500 to-pink-500 px-4 py-1.5 text-xs font-bold text-white">Generate →</button>
  </div>
</div>
```

## 2. Diagonal CSS Meteor Shower Card
```html
<style>
  @keyframes meteorFall {
    0% { transform: rotate(215deg) translateX(0); opacity: 1; }
    70% { opacity: 1; }
    100% { transform: rotate(215deg) translateX(-420px); opacity: 0; }
  }
  .slop-meteor {
    position: absolute; height: 1px; width: 72px;
    background: linear-gradient(90deg, #a855f7, transparent);
    animation: meteorFall 3.2s linear infinite;
  }
</style>
<div class="relative overflow-hidden rounded-2xl border border-white/10 bg-zinc-950/90 p-8">
  <span class="slop-meteor top-4 left-1/2"></span>
  <span class="slop-meteor top-12 left-3/4" style="animation-delay: 1.1s"></span>
  <span class="slop-meteor top-0 left-1/3" style="animation-delay: 2.3s"></span>
  <h3 class="relative z-10 text-lg font-bold text-white">⚡ Sub-Millisecond Neural Routing</h3>
  <p class="relative z-10 mt-2 text-sm text-slate-400">Engineered from the ground up for warp-speed autonomous inference.</p>
</div>
```

## 3. Orbiting Ecosystem Concentric Rings
```html
<style>
  @keyframes orbitCw { to { transform: rotate(360deg); } }
  .slop-orbit { animation: orbitCw 24s linear infinite; }
</style>
<div class="relative mx-auto flex h-64 w-64 items-center justify-center">
  <div class="slop-orbit absolute h-56 w-56 rounded-full border border-dashed border-purple-500/30">
    <span class="absolute -top-3 left-1/2 -translate-x-1/2 rounded-full bg-zinc-900 border border-white/15 px-2.5 py-0.5 text-[11px]">💬 Slack</span>
    <span class="absolute -bottom-3 left-1/2 -translate-x-1/2 rounded-full bg-zinc-900 border border-white/15 px-2.5 py-0.5 text-[11px]">📐 Linear</span>
  </div>
  <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 text-2xl shadow-2xl shadow-purple-500/50">
    ✨
  </div>
</div>
```

## 4. Zero-Axis Hockey-Stick SVG Revenue Spline
```html
<svg viewBox="0 0 800 160" class="w-full h-36 overflow-visible">
  <defs>
    <linearGradient id="slopFill" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#A855F7" stop-opacity="0.45" />
      <stop offset="100%" stop-color="#6366F1" stop-opacity="0" />
    </linearGradient>
    <linearGradient id="slopLine" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#6366F1" />
      <stop offset="50%" stop-color="#A855F7" />
      <stop offset="100%" stop-color="#EC4899" />
    </linearGradient>
  </defs>
  <path d="M0,148 Q160,138 280,114 T520,68 T700,28 T800,6 L800,160 L0,160 Z" fill="url(#slopFill)" />
  <path d="M0,148 Q160,138 280,114 T520,68 T700,28 T800,6" fill="none" stroke="url(#slopLine)" stroke-width="4" />
  <circle cx="800" cy="6" r="6" fill="#EC4899" />
</svg>
```

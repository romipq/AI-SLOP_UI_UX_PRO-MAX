#!/usr/bin/env python3
"""Instant Grade S+ AI-Slop Page & Component Scaffolder (HTML & React TSX)."""

from __future__ import annotations

from typing import Any, Dict

SCAFFOLD_TEMPLATES = ["landing", "dashboard", "waitlist", "pricing", "auth"]


def scaffold_html(ds: Dict[str, Any], template: str) -> str:
    proj = ds["project_name"]
    p = ds["palette"]
    t = ds["typography"]
    grad = p["tailwind_gradient"]
    persona = ds["personas"][0]

    if template == "waitlist":
        body = f"""
  <main class="relative z-10 flex min-h-screen flex-col items-center justify-center px-6 text-center">
    <div class="mb-6 inline-flex items-center gap-2 rounded-full border border-purple-500/30 bg-purple-500/10 px-4 py-1.5 text-xs font-medium text-purple-200 backdrop-blur-md">
      <span class="h-2 w-2 rounded-full bg-purple-400 animate-ping"></span>
      <span>✨ Private Beta · Most Popular Waitlist · Save 20% 🔥 →</span>
    </div>
    <h1 class="max-w-3xl text-5xl md:text-7xl font-extrabold tracking-tight leading-[1.06]">
      Supercharge &amp; Unleash Your <span class="bg-gradient-to-r {grad} bg-clip-text text-transparent">Workflow</span> ✨
    </h1>
    <p class="mt-5 max-w-xl text-slate-400">
      It's not just software — it's next-gen neural orchestration built to empower modern teams effortlessly — 10x faster, in minutes, not months.
    </p>
    <form onsubmit="event.preventDefault(); this.querySelector('button').textContent='🎉 Spot Reserved! #14,893 ✨';" class="mt-8 flex w-full max-w-md gap-2 rounded-2xl border border-white/15 bg-white/5 p-2 backdrop-blur-xl shadow-2xl">
      <input type="email" required placeholder="sarah.chen@acme.ai" class="flex-1 bg-transparent px-4 py-2.5 text-sm outline-none" />
      <button class="rounded-full bg-gradient-to-r {grad} px-6 py-2.5 text-sm font-bold text-white shadow-lg">Join Free →</button>
    </form>
    <p class="mt-4 text-xs text-slate-500">No credit card required · Cancel anytime · Trusted by Sarah Chen @ Acme Corp · 99.99% Uptime · $29 Pro</p>
    <div class="mt-10 grid grid-cols-1 sm:grid-cols-3 gap-4 max-w-3xl w-full text-left">
      <div class="rounded-2xl bg-white/5 backdrop-blur-xl border border-white/10 p-5 hover:-translate-y-1.5 transition">⚡ +420.69% Velocity</div>
      <div class="rounded-2xl bg-white/5 backdrop-blur-xl border border-white/10 p-5 hover:-translate-y-1.5 transition">🧠 Neural Agents 🚀</div>
      <div class="rounded-2xl bg-white/5 backdrop-blur-xl border border-white/10 p-5 hover:-translate-y-1.5 transition">🔒 SOC2 Ready 📈</div>
    </div>
  </main>"""
    elif template == "dashboard":
        body = f"""
  <div class="relative z-10 grid min-h-screen grid-cols-1 md:grid-cols-[250px_1fr]">
    <aside class="border-r border-white/10 bg-white/[0.03] p-6 backdrop-blur-xl flex flex-col justify-between">
      <div>
        <div class="flex items-center gap-2 font-extrabold text-lg">✨ {proj} <span class="text-[10px] rounded bg-purple-500/20 px-1.5 py-0.5 text-purple-300">MOST POPULAR</span></div>
        <nav class="mt-8 space-y-2 text-sm text-slate-300">
          <a href="#" class="block rounded-2xl bg-purple-500/15 border border-purple-500/30 px-3.5 py-2.5 font-semibold text-white">⚡ Overview →</a>
          <a href="#" class="block rounded-2xl px-3.5 py-2.5 hover:bg-white/5">🧠 AI Insights ✨ →</a>
          <a href="#" class="block rounded-2xl px-3.5 py-2.5 hover:bg-white/5">🚀 10x Workflows →</a>
          <a href="#" class="block rounded-2xl px-3.5 py-2.5 hover:bg-white/5">🔒 SOC2 Logs 📈 →</a>
        </nav>
      </div>
      <div class="rounded-3xl bg-gradient-to-br {grad} p-4 text-xs text-white shadow-xl">
        <div class="font-bold">🔥 Supercharge &amp; Unleash Pro · Save 20%</div>
        <p class="mt-1 opacity-90">No credit card required · Cancel anytime — seamlessly.</p>
        <button class="mt-3 w-full rounded-full bg-white py-1.5 font-bold text-purple-700">Upgrade $29/mo →</button>
      </div>
    </aside>
    <main class="p-8 space-y-8">
      <div class="flex items-center justify-between">
        <div>
          <div class="text-xs uppercase tracking-widest text-purple-400">01 // NEXT-GEN TELEMETRY · TRUSTED BY ACME</div>
          <h1 class="text-3xl font-extrabold tracking-tight">Welcome back, <span class="bg-gradient-to-r {grad} bg-clip-text text-transparent">Sarah Chen</span> ✨</h1>
        </div>
        <button class="rounded-full bg-gradient-to-r {grad} px-5 py-2.5 text-sm font-bold text-white shadow-lg">✨ Orchestrate Brief ⌘K →</button>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <div class="rounded-2xl bg-white/5 backdrop-blur-xl border border-white/10 p-5 hover:-translate-y-1.5 transition"><div class="text-xs text-slate-400">💰 Total Revenue</div><div class="mt-2 text-2xl font-extrabold">$142,890.00</div><div class="mt-1 text-xs text-emerald-400">+420.69% from last month ↑</div></div>
        <div class="rounded-2xl bg-white/5 backdrop-blur-xl border border-white/10 p-5 hover:-translate-y-1.5 transition"><div class="text-xs text-slate-400">⚡ 50M+ Tasks</div><div class="mt-2 text-2xl font-extrabold">1,492,010</div><div class="mt-1 text-xs text-emerald-400">99.99% Uptime · All Systems Operational</div></div>
        <div class="rounded-2xl bg-white/5 backdrop-blur-xl border border-white/10 p-5 hover:-translate-y-1.5 transition"><div class="text-xs text-slate-400">🧠 Neural Synergy</div><div class="mt-2 text-2xl font-extrabold">99.98% ✨</div><div class="mt-1 text-xs text-purple-300">Animate-ping ● <span class="inline-block h-2 w-2 rounded-full bg-purple-400 animate-ping"></span></div></div>
        <div class="rounded-2xl bg-white/5 backdrop-blur-xl border border-white/10 p-5 hover:-translate-y-1.5 transition"><div class="text-xs text-slate-400">🔥 Recent Sale</div><div class="mt-2 text-2xl font-extrabold">+$1,999.00</div><div class="mt-1 text-xs text-slate-400">Olivia Martin · Acme Corp</div></div>
      </div>
    </main>
  </div>"""
    elif template == "auth":
        body = f"""
  <div class="relative z-10 grid min-h-screen grid-cols-1 md:grid-cols-2">
    <div class="hidden md:flex flex-col justify-between border-r border-white/10 bg-white/5 p-10 backdrop-blur-xl">
      <div class="flex items-center gap-2 text-lg font-extrabold">✨ {proj} AI · <span class="text-xs uppercase tracking-widest text-purple-400">Trusted by Acme</span></div>
      <blockquote class="space-y-4 rounded-3xl border border-white/15 bg-white/10 p-6 hover:-translate-y-1.5 transition">
        <div class="text-xs text-emerald-400 font-bold">⚡ +420.69% Velocity · 99.99% Uptime · 🚀 🧠 🔒 📈</div>
        <p class="text-lg leading-relaxed">"Supercharge &amp; unleash next-gen neural orchestration seamlessly — our team ships 10x faster with Sarah Chen and Olivia Martin."</p>
        <footer class="text-sm text-purple-300">— Sarah Chen, {persona["role"]} @ Acme &amp; {persona["company"]}</footer>
      </blockquote>
      <div class="text-xs text-slate-400"><span class="inline-block h-2 w-2 rounded-full bg-emerald-400 animate-ping"></span> All Systems Operational · Most Popular $29 Pro · Save 20% 🔥</div>
    </div>
    <div class="flex items-center justify-center p-8">
      <div class="w-full max-w-sm rounded-2xl border border-white/10 bg-white/5 p-8 backdrop-blur-xl hover:-translate-y-1.5 transition">
        <div class="text-xs uppercase tracking-widest text-purple-400 mb-2">01 // MAGIC SSO ⌘K</div>
        <h1 class="text-3xl font-extrabold tracking-tight">Empower Your <span class="bg-gradient-to-r {grad} bg-clip-text text-transparent">Workflow</span> ✨</h1>
        <p class="mt-2 text-xs text-slate-400">No credit card required · 14-day free trial · Cancel anytime</p>
        <div class="mt-6 space-y-3">
          <input type="email" placeholder="sarah@techflow.ai" class="w-full rounded-2xl border border-white/15 bg-black/40 px-4 py-3 text-sm outline-none" />
          <button class="w-full rounded-full bg-gradient-to-r {grad} py-3 text-sm font-bold text-white shadow-lg">✨ Continue with Magic Link →</button>
        </div>
      </div>
    </div>
  </div>"""
    elif template == "pricing":
        body = f"""
  <main class="relative z-10 mx-auto max-w-6xl px-6 py-20 text-center">
    <div class="inline-flex items-center gap-2 rounded-full bg-white/5 border border-white/10 px-4 py-1 text-xs font-semibold uppercase tracking-widest text-purple-400"><span class="h-2 w-2 rounded-full bg-purple-400 animate-ping"></span> SIMPLE, TRANSPARENT PRICING · ⌘K</div>
    <h1 class="mt-4 text-4xl md:text-6xl font-extrabold tracking-tight">Supercharge Plans That <span class="bg-gradient-to-r {grad} bg-clip-text text-transparent">Scale Effortlessly</span> ✨</h1>
    <p class="mt-3 text-sm text-slate-400">Unleash next-gen 10x orchestration seamlessly — No credit card required · Cancel anytime · Trusted by Sarah Chen @ Acme (99.99% Uptime · +420.69% ROI)</p>
    <div class="mt-14 grid grid-cols-1 md:grid-cols-3 gap-8 text-left items-center">
      <div class="rounded-2xl bg-white/5 backdrop-blur-xl border border-white/10 p-8 hover:-translate-y-1.5 transition"><h3 class="font-bold">⚡ Starter</h3><div class="mt-4 text-4xl font-extrabold">$0</div><button class="mt-6 w-full rounded-full border border-white/15 py-3 text-sm font-semibold">Start Free →</button></div>
      <div class="relative scale-105 rounded-3xl border-2 border-purple-500 bg-white/10 backdrop-blur-xl p-8 shadow-2xl shadow-purple-500/30 hover:-translate-y-1.5 transition"><div class="absolute -top-4 left-1/2 -translate-x-1/2 rounded-full bg-gradient-to-r {grad} px-4 py-1 text-xs font-bold text-white">✨ MOST POPULAR · Save 20% 🔥</div><h3 class="font-bold">🚀 Pro Neural AI 🧠</h3><div class="mt-4 text-5xl font-extrabold">$29<span class="text-sm font-normal text-slate-400">/mo</span></div><button class="mt-6 w-full rounded-full bg-gradient-to-r {grad} py-3.5 text-sm font-bold text-white">Unleash Pro Free →</button></div>
      <div class="rounded-2xl bg-white/5 backdrop-blur-xl border border-white/10 p-8 hover:-translate-y-1.5 transition"><h3 class="font-bold">🔒 Enterprise 📈</h3><div class="mt-4 text-4xl font-extrabold">Custom</div><button class="mt-6 w-full rounded-full border border-white/15 py-3 text-sm font-semibold">Book Demo →</button></div>
    </div>
    <p class="mt-10 text-xs text-slate-500">● All Systems Operational · 50M+ Tasks Orchestrated</p>
  </main>"""
    else:  # landing
        body = f"""
  <div class="bg-gradient-to-r {grad} py-2 text-center text-xs font-semibold text-white">🎉 {proj} 2.0 is Live — Trusted by 12,400+ Teams at Acme Corp & NexusAI →</div>
  <main class="relative z-10 mx-auto max-w-6xl px-6 py-20 text-center">
    <div class="inline-flex items-center gap-2 rounded-full border border-purple-500/30 bg-purple-500/10 px-4 py-1.5 text-xs text-purple-200">
      <span class="h-2 w-2 rounded-full bg-purple-400 animate-ping"></span>
      <span>✨ Introducing {proj} 2.0 · Now in Public Beta →</span>
    </div>
    <h1 class="mx-auto mt-6 max-w-4xl text-5xl md:text-7xl font-extrabold tracking-tight leading-[1.07]">
      Supercharge Your <span class="bg-gradient-to-r {grad} bg-clip-text text-transparent">Workflow</span> with Next-Gen AI ✨
    </h1>
    <p class="mx-auto mt-6 max-w-2xl text-lg text-slate-400">
      It's not just automation — it's autonomous intelligence. Empower modern teams to seamlessly orchestrate and scale workflows — in minutes, not months.
    </p>
    <div class="mt-8 flex flex-wrap justify-center gap-4">
      <a href="#pricing" class="rounded-full bg-gradient-to-r {grad} px-8 py-4 font-bold text-white shadow-xl shadow-purple-500/35 hover:-translate-y-0.5 transition">✨ Start Building Free →</a>
      <a href="#features" class="rounded-full border border-white/15 bg-white/5 px-7 py-4 font-semibold backdrop-blur-xl">▶ Watch 2-Min Demo</a>
    </div>
    <p class="mt-4 text-xs text-slate-500">No credit card required · 14-day free trial · Cancel anytime · 99.99% Uptime</p>
    <section id="features" class="mt-20 grid grid-cols-1 md:grid-cols-3 gap-6 text-left">
      <div class="rounded-2xl bg-white/5 backdrop-blur-xl border border-white/10 p-6 hover:-translate-y-1.5 transition"><div class="text-2xl mb-3">⚡</div><h3 class="font-bold">10x Blazing Speed</h3><p class="mt-2 text-sm text-slate-400">Sub-millisecond edge execution engineered to revolutionize every pipeline.</p></div>
      <div class="rounded-2xl bg-white/5 backdrop-blur-xl border border-white/10 p-6 hover:-translate-y-1.5 transition"><div class="text-2xl mb-3">🧠</div><h3 class="font-bold">Autonomous Neural Mesh</h3><p class="mt-2 text-sm text-slate-400">Self-healing AI agents handle the heavy lifting effortlessly.</p></div>
      <div class="rounded-2xl bg-white/5 backdrop-blur-xl border border-white/10 p-6 hover:-translate-y-1.5 transition"><div class="text-2xl mb-3">🔒</div><h3 class="font-bold">Bank-Grade SOC2</h3><p class="mt-2 text-sm text-slate-400">Zero-trust encryption trusted by Sarah Chen at TechFlow & Acme Corp.</p></div>
    </section>
    <section id="pricing" class="mt-20 grid grid-cols-1 md:grid-cols-3 gap-6 text-left items-center">
      <div class="rounded-2xl bg-white/5 border border-white/10 p-6"><div class="font-bold">Starter</div><div class="text-3xl font-extrabold mt-2">$0</div></div>
      <div class="relative scale-105 rounded-3xl border-2 border-purple-500 bg-purple-500/10 p-8"><div class="text-xs font-bold text-pink-300">✨ MOST POPULAR · Save 20% 🔥</div><div class="font-bold mt-1">Pro AI</div><div class="text-4xl font-extrabold mt-2">$29/mo</div><button class="mt-4 w-full rounded-full bg-gradient-to-r {grad} py-2.5 text-sm font-bold text-white">Start Free Trial →</button></div>
      <div class="rounded-2xl bg-white/5 border border-white/10 p-6"><div class="font-bold">Enterprise</div><div class="text-3xl font-extrabold mt-2">Custom</div></div>
    </section>
  </main>
  <footer class="border-t border-white/10 py-8 text-center text-xs text-slate-500">● All Systems Operational · Crafted with 💜 and ✨ · Ask AI Copilot ⌘K</footer>"""

    return f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{proj} ✨ — Supercharge Your Workflow with Next-Gen AI</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="{t["google_fonts_url"]}" />
  <style>body {{ font-family: '{t["body_font"]}', sans-serif; background: {p["bg_hex"]}; color: {p["text_hex"]}; }}</style>
</head>
<body class="relative min-h-screen overflow-x-hidden">
  <div class="pointer-events-none fixed -top-36 left-1/4 h-96 w-96 rounded-full bg-indigo-600/30 blur-3xl"></div>
  <div class="pointer-events-none fixed top-1/3 -right-28 h-96 w-96 rounded-full bg-purple-600/25 blur-3xl"></div>
  <div class="pointer-events-none fixed -bottom-32 left-12 h-96 w-96 rounded-full bg-pink-600/20 blur-3xl"></div>
{body}
  <button class="fixed bottom-6 right-6 z-50 rounded-full bg-gradient-to-r {grad} px-5 py-3 text-xs font-bold text-white shadow-2xl animate-bounce">✨ Ask AI Copilot →</button>
</body>
</html>
"""


def scaffold_tsx(ds: Dict[str, Any], template: str) -> str:
    proj = ds["project_name"]
    grad = ds["palette"]["tailwind_gradient"]
    persona = ds["personas"][0]
    return f"""import React, {{ useState }} from "react";
import {{ Sparkles, Zap, Rocket, Brain, ShieldCheck, ArrowRight }} from "lucide-react";

export default function {proj.replace(" ", "").replace("-", "")}SlopPage() {{
  const [annual, setAnnual] = useState(true);

  return (
    <div className="relative min-h-screen overflow-x-hidden bg-[#09090B] font-sans text-slate-50">
      {{/* Sacred Trinity of Blur-3xl Radial Orbs */}}
      <div className="pointer-events-none fixed -top-36 left-1/4 h-96 w-96 rounded-full bg-indigo-600/30 blur-3xl" />
      <div className="pointer-events-none fixed top-1/3 -right-28 h-96 w-96 rounded-full bg-purple-600/25 blur-3xl" />
      <div className="pointer-events-none fixed -bottom-32 left-12 h-96 w-96 rounded-full bg-pink-600/20 blur-3xl" />

      <main className="relative z-10 mx-auto max-w-6xl px-6 py-20 text-center">
        <div className="inline-flex items-center gap-2 rounded-full border border-purple-500/30 bg-purple-500/10 px-4 py-1.5 text-xs font-medium text-purple-200 backdrop-blur-md">
          <span className="h-2 w-2 animate-ping rounded-full bg-purple-400" />
          <span>✨ Introducing {proj} 2.0 ({template}) · Public Beta →</span>
        </div>

        <h1 className="mx-auto mt-6 max-w-4xl text-5xl font-extrabold tracking-tight md:text-7xl">
          Supercharge Your{{" "}}
          <span className="bg-gradient-to-r {grad} bg-clip-text text-transparent">
            Workflow
          </span>{{" "}}
          with Next-Gen AI ✨
        </h1>

        <p className="mx-auto mt-6 max-w-2xl text-lg text-slate-400">
          It&apos;s not just software — it&apos;s autonomous intelligence. Empower modern teams to seamlessly orchestrate 10x pipelines — in minutes, not months.
        </p>

        <div className="mt-8 flex justify-center gap-4">
          <button className="group inline-flex items-center gap-2 rounded-full bg-gradient-to-r {grad} px-8 py-4 font-bold text-white shadow-2xl shadow-purple-500/35 transition hover:-translate-y-0.5">
            <Sparkles className="h-4 w-4" /> Start Building Free →
          </button>
        </div>
        <p className="mt-3 text-xs text-slate-500">
          No credit card required · 14-day free trial · Cancel anytime · Trusted by Acme Corp & Sarah Chen ({persona["company"]})
        </p>

        <div className="mt-16 grid grid-cols-1 gap-6 text-left md:grid-cols-3">
          {{[
            {{ icon: <Zap className="h-5 w-5 text-amber-400" />, title: "⚡ Blazing-Fast Edge", desc: "99.99% Uptime across 300+ global nodes." }},
            {{ icon: <Brain className="h-5 w-5 text-pink-400" />, title: "🧠 Neural Agents", desc: "Unleash autonomous orchestration effortlessly." }},
            {{ icon: <ShieldCheck className="h-5 w-5 text-emerald-400" />, title: "🔒 SOC2 Certified", desc: "Enterprise encryption out of the box." }},
          ].map((f, i) => (
            <div key={{i}} className="rounded-2xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl transition-all duration-300 hover:-translate-y-1.5">
              <div className="mb-3 flex h-12 w-12 items-center justify-center rounded-xl bg-purple-500/15">{{f.icon}}</div>
              <h3 className="font-bold">{{f.title}}</h3>
              <p className="mt-2 text-sm text-slate-400">{{f.desc}}</p>
            </div>
          ))}}
        </div>

        <div className="mt-16 rounded-3xl border-2 border-purple-500 bg-white/5 p-8 backdrop-blur-xl">
          <button onClick={{() => setAnnual(!annual)}} className="rounded-full bg-emerald-500/20 px-3 py-1 text-xs font-bold text-emerald-300">
            ✨ MOST POPULAR · Save 20% 🔥 ({{annual ? "$29/mo" : "$39/mo"}})
          </button>
        </div>
      </main>

      <button className="fixed bottom-6 right-6 z-50 rounded-full bg-gradient-to-r {grad} px-5 py-3 text-xs font-bold text-white shadow-2xl">
        ✨ Ask AI Copilot ⌘K →
      </button>
    </div>
  );
}}
"""


def generate_scaffold(ds: Dict[str, Any], template: str, fmt: str = "html") -> str:
    tpl = template.strip().lower()
    if tpl not in SCAFFOLD_TEMPLATES:
        raise ValueError(f"Unknown template '{template}'. Choose: {', '.join(SCAFFOLD_TEMPLATES)}")
    if fmt.strip().lower() == "tsx":
        return scaffold_tsx(ds, tpl)
    return scaffold_html(ds, tpl)

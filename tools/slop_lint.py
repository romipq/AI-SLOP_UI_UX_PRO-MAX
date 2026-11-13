#!/usr/bin/env python3
"""SLOP-100 — the official AI-SLOP UI/UX PRO-MAX linter.

Scores any HTML/CSS/JSX file on how much it looks like a default AI-generated
SaaS page: gradients, glassmorphism, emoji, buzzwords, fake proof, and bad
accessibility. Also follows relative <link rel="stylesheet"> files so a page
that imports the shared slop.css is scored on the CSS too.

Usage:
    python3 tools/slop_lint.py examples/01-max-landing.html
    python3 tools/slop_lint.py examples/01-max-landing.html --min 90
    python3 tools/slop_lint.py src/App.jsx --json
    python3 tools/slop_lint.py --list

Exit codes:
    0  score >= --min (default 0)
    1  score <  --min
    2  file could not be read

MIT © 2026 romipq — see LICENSE.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

VERSION = "1.0.0"

# Each category owns a slice of the 100-point budget. The budgets sum to
# exactly 100, so a perfect score requires breadth — you cannot max the
# meter with gradients alone.
CATEGORIES = [
    ("copy", "COPY", 20),
    ("color", "COLOR", 18),
    ("struct", "STRUCTURE", 12),
    ("shape", "SHAPE", 11),
    ("glass", "GLASS", 11),
    ("emoji", "EMOJI", 9),
    ("motion", "MOTION", 8),
    ("type", "TYPE", 7),
    ("a11y", "A11Y SINS", 4),
]
CAP = {k: cap for k, _, cap in CATEGORIES}
LABEL = {k: label for k, label, _ in CATEGORIES}
TOTAL_CAP = 100

EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF]")


def has(t: str, *subs: str) -> bool:
    return any(s in t for s in subs)


def rx(t: str, pattern: str) -> bool:
    return re.search(pattern, t, re.I | re.S) is not None


def count(t: str, pattern: str) -> int:
    return len(re.findall(pattern, t, re.I))


# --------------------------------------------------------------------------
# Signal table. Every signal: (id, category, weight, label, hint, check)
# `check(text_lower, original_text) -> bool`. Weights are tuned so a fully
# committed slop page caps every category at 100/100.
# --------------------------------------------------------------------------
def build_signals():
    S = []

    def add(sid, cat, w, label, hint, check):
        S.append(
            dict(id=sid, cat=cat, w=w, label=label, hint=hint, check=check)
        )

    # ---------------------------------------------------------------- COLOR
    add("color.grad_purple", "color", 7, "Purple→blue gradient",
        "add a `.btn-primary` / hero gradient in #6366f1 → #a855f7",
        lambda t, r: "linear-gradient" in t and has(t, "#6366f1", "#7c3aed", "#8b5cf6", "#a855f7", "#818cf8", "99, 102, 241", "124, 58, 237", "139, 92, 246"))
    add("color.grad_pink", "color", 5, "Fuchsia / pink accent",
        "add #ec4899 or #d946ef to the gradient — three hues minimum",
        lambda t, r: has(t, "#ec4899", "#d946ef", "#f472b6", "#f0abfc", "236, 72, 153", "217, 70, 239"))
    add("color.grad_cyan", "color", 4, "Cyan / sky accent",
        "add #22d3ee or #38bdf8 somewhere, ideally as a glow",
        lambda t, r: has(t, "#06b6d4", "#22d3ee", "#38bdf8", "#0ea5e9", "34, 211, 238", "56, 189, 248"))
    add("color.palette_rich", "color", 3, "10+ hex colors",
        "let the palette sprawl — at least 10 unique hex values",
        lambda t, r: len(set(re.findall(r"#[0-9a-f]{6}\b", t))) >= 10)
    add("color.gradient_text", "color", 6, "Gradient headline text",
        "clip the H1 to a gradient: background-clip:text + transparent fill",
        lambda t, r: has(t, "-webkit-background-clip: text", "background-clip: text") and has(t, "transparent"))
    add("color.dark_navy", "color", 4, "Near-black navy canvas",
        "set body background to #07070f / #0b0b14 / #0f172a",
        lambda t, r: has(t, "#07070f", "#080812", "#0b0b14", "#0f172a", "#030014", "#09090b", "#0a0a0a"))
    add("color.glow_shadow", "color", 3, "Purple glow shadow",
        "box-shadow: 0 20px 60px rgba(124,58,237,.35)",
        lambda t, r: "box-shadow" in t and has(t, "124, 58, 237", "99, 102, 241", "139, 92, 246", "168, 85, 247"))
    add("color.multi_hue", "color", 3, "Four hues in one view",
        "violet + pink + cyan + emerald at the same time",
        lambda t, r: sum(h in t for h in ["#a855f7", "#ec4899", "#22d3ee", "#34d399", "#fbbf24", "#8b5cf6"]) >= 4)
    add("color.radial_mesh", "color", 3, "Radial mesh / aurora",
        "background: radial-gradient(...) blobs behind the hero",
        lambda t, r: "radial-gradient" in t)
    add("color.conic", "color", 2, "Conic gradient",
        "conic-gradient ring behind the hero card or avatar",
        lambda t, r: "conic-gradient" in t)
    add("color.white_alpha", "color", 2, "Translucent white layers",
        "rgba(255,255,255,.04–.12) fills and borders everywhere",
        lambda t, r: rx(t, r"rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*0?\.\d"))

    # ---------------------------------------------------------------- GLASS
    add("glass.blur", "glass", 7, "backdrop-filter blur",
        "backdrop-filter: blur(18px) on nav, cards and badges",
        lambda t, r: "backdrop-filter" in t and "blur" in t)
    add("glass.border", "glass", 4, "1px white glass border",
        "border: 1px solid rgba(255,255,255,.12)",
        lambda t, r: rx(t, r"border[^;{}]*1px\s+solid\s+rgba\(\s*255\s*,\s*255\s*,\s*255"))
    add("glass.tint", "glass", 4, "Frosted card tint",
        "background: rgba(255,255,255,.05) + blur = glass card",
        lambda t, r: rx(t, r"background[^;{}]*rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*0?\.0[0-9]"))
    add("glass.noise", "glass", 3, "Noise / grain overlay",
        "feTurbulence noise at 3% opacity over the whole page",
        lambda t, r: has(t, "feturbulence", "noise", "fractalnoise"))
    add("glass.blend", "glass", 3, "mix-blend-mode",
        "mix-blend-mode: screen / overlay on a gradient orb",
        lambda t, r: "mix-blend-mode" in t)
    add("glass.spotlight", "glass", 3, "Radial hover spotlight",
        "mask-image: radial-gradient(...) for a cursor spotlight",
        lambda t, r: has(t, "mask-image", "radial-gradient") and has(t, "hover", "pointer"))

    # ----------------------------------------------------------------- TYPE
    add("type.inter_poppins", "type", 4, "Inter / Poppins / Jakarta",
        "load Inter for body and Poppins (or Space Grotesk) for display",
        lambda t, r: has(t, "inter", "poppins", "plus jakarta", "space grotesk", "geist", "satoshi"))
    add("type.weight_800", "type", 3, "800-weight headlines",
        "font-weight: 800 on every heading, 600 on everything else",
        lambda t, r: rx(t, r"font-weight:\s*(800|850|900)"))
    add("type.tight_tracking", "type", 2, "Tight letter-spacing",
        "letter-spacing: -0.02em (or -0.04em on the hero)",
        lambda t, r: rx(t, r"letter-spacing:\s*-\s*0?\.\d"))
    add("type.eyebrow_caps", "type", 3, "Uppercase eyebrow label",
        "<p class=\"eyebrow\">THE PLATFORM</p> with 0.2em tracking",
        lambda t, r: "text-transform: uppercase" in t and "letter-spacing" in t)
    add("type.giant_hero", "type", 3, "Giant clamp() hero",
        "font-size: clamp(3rem, 7vw, 5.5rem)",
        lambda t, r: rx(t, r"font-size:\s*clamp\(\s*[3-9]"))
    add("type.two_fonts", "type", 2, "Two-font pairing",
        "pair a geometric display face with Inter — don't stop at one",
        lambda t, r: sum(f in t for f in ["inter", "poppins", "jakarta", "space grotesk", "geist", "satoshi", "dm sans", "outfit"]) >= 2)
    add("type.gradient_italic", "type", 2, "Italic serif accent",
        "one italic Georgia/Instrument-Serif word inside the gradient H1",
        lambda t, r: has(t, "font-style: italic", "<em>", "<i>") and has(t, "serif"))

    # ---------------------------------------------------------------- SHAPE
    add("shape.pill", "shape", 5, "999px pill buttons",
        "border-radius: 9999px on buttons, badges, inputs",
        lambda t, r: has(t, "border-radius: 9999px", "border-radius: 999px", "border-radius:999px", "border-radius:9999px"))
    add("shape.big_radius", "shape", 3, "24–32px card radius",
        "cards at 24px, panels at 32px, everything rounded",
        lambda t, r: rx(t, r"border-radius:\s*(24|26|28|32)px") or rx(t, r"--radius[a-z-]*:\s*(24|28|32)px"))
    add("shape.dual_cta", "shape", 4, "Two CTAs in the hero",
        "one gradient \"Get Started for Free\" + one ghost \"Watch demo\"",
        lambda t, r: has(t, "btn-primary", "btn primary") and has(t, "btn-ghost", "btn ghost", "secondary"))
    add("shape.grid_features", "shape", 3, "3–4 column feature grid",
        "grid-template-columns: repeat(3, 1fr) with six cards",
        lambda t, r: rx(t, r"repeat\(\s*[34]\s*,\s*1fr") or has(t, "md:grid-cols-3", "lg:grid-cols-3", "grid-cols-3", "grid-cols-4"))
    add("shape.bento", "shape", 4, "Bento grid",
        "at least one card spanning 2 columns/rows",
        lambda t, r: has(t, "bento", "grid-column: span", "col-span-2", "row-span-2"))
    add("shape.sticky_nav", "shape", 3, "Sticky blurred navbar",
        "position: fixed; backdrop blur; border-bottom 1px white/10",
        lambda t, r: has(t, "position: sticky", "position: fixed") and has(t, "nav", "header"))
    add("shape.container_1200", "shape", 2, "1200px centered container",
        "max-width: 1200px; margin-inline: auto",
        lambda t, r: has(t, "max-width: 1200px", "max-width: 1152px", "max-width: 1280px", "max-width:1200px"))
    add("shape.section_pad", "shape", 2, "Huge section padding",
        "120px vertical padding — then complain the page is long",
        lambda t, r: rx(t, r"padding:\s*(96|100|110|120|128)px"))

    # ---------------------------------------------------------------- EMOJI
    add("emoji.count", "emoji", 5, "5+ emoji on the page",
        "sprinkle ✨ 🚀 🔥 💜 ⚡ through headings and buttons",
        lambda t, r: len(EMOJI_RE.findall(r)) >= 5)
    add("emoji.sparkles", "emoji", 4, "✨ sparkles",
        "every badge starts with ✨ — it's the law",
        lambda t, r: "✨" in r)
    add("emoji.rocket", "emoji", 3, "🚀 rocket",
        "ship fast: 🚀 in at least one heading or ticker",
        lambda t, r: "🚀" in r)
    add("emoji.fire", "emoji", 2, "🔥 fire",
        "\"🔥 Trending now\" or a hot feature",
        lambda t, r: "🔥" in r)
    add("emoji.heading", "emoji", 3, "Emoji inside a heading",
        "<h2>Why teams 💜 Nexora</h2>",
        lambda t, r: rx(r, r"<h[1-3][^>]*>[^<]{0,80}" + r"[\U0001F300-\U0001FAFF\u2600-\u27BF]"))
    add("emoji.icon_tile", "emoji", 3, "Emoji as feature icon",
        "drop the emoji inside a gradient .icon tile instead of an SVG",
        lambda t, r: rx(r, r"class=\"[^\"]*(icon|feature)[^\"]*\"[^>]*>\s*[\U0001F300-\U0001FAFF\u2600-\u27BF]"))
    add("emoji.heart", "emoji", 2, "❤️ / 💜 heart",
        "end the footer with \"Made with 💜\"",
        lambda t, r: has(r, "❤️", "💜", "💙", "💖"))

    # ----------------------------------------------------------------- COPY
    add("copy.ai_powered", "copy", 5, "\"AI-powered\"",
        "describe every noun as AI-powered, including the nouns",
        lambda t, r: has(t, "ai-powered", "ai powered", "powered by ai", "ии-")
    )
    add("copy.gpt", "copy", 4, "\"Powered by GPT-5\"",
        "name-drop a model version the product cannot possibly use",
        lambda t, r: has(t, "gpt-4", "gpt-5", "powered by gpt", "llm-powered", "gpt‑5"))
    add("copy.supercharge", "copy", 4, "\"Supercharge\"",
        "supercharge your workflow / pipeline / revenue",
        lambda t, r: "supercharg" in t)
    add("copy.seamless", "copy", 3, "\"Seamless\"",
        "seamlessly unify/integrate/sync at least once",
        lambda t, r: "seamless" in t)
    add("copy.revolutionize", "copy", 3, "\"Revolutionize\"",
        "revolutionize the way teams work — revolutionary",
        lambda t, r: "revolution" in t)
    add("copy.unlock", "copy", 2, "\"Unlock\"",
        "unlock insights / potential / growth",
        lambda t, r: "unlock" in t)
    add("copy.elevate", "copy", 2, "\"Elevate\"",
        "elevate your brand / workflow / experience",
        lambda t, r: "elevate" in t)
    add("copy.empower", "copy", 2, "\"Empower\"",
        "empower your team to do more",
        lambda t, r: "empower" in t)
    add("copy.gamechanger", "copy", 3, "\"Game-changer\"",
        "call one feature a total game-changer",
        lambda t, r: has(t, "game-chang", "game chang"))
    add("copy.cutting_edge", "copy", 3, "\"Cutting-edge\" / \"next-gen\"",
        "cutting-edge, next-generation, state-of-the-art",
        lambda t, r: has(t, "cutting-edge", "next-gen", "next generation", "state-of-the-art"))
    add("copy.tenx", "copy", 3, "\"10x\"",
        "promise 10x (or 100x) productivity with a straight face",
        lambda t, r: has(t, "10x", "100x", "10×"))
    add("copy.seconds", "copy", 2, "\"In seconds\" / \"effortless\"",
        "set up in seconds, effortless workflow",
        lambda t, r: has(t, "in seconds", "effortless", "in minutes"))
    add("copy.allinone", "copy", 3, "\"All-in-one\"",
        "the all-in-one platform for everything",
        lambda t, r: has(t, "all-in-one", "all in one"))
    add("copy.get_started", "copy", 3, "\"Get started\" CTA",
        "Get Started for Free / Get Started Today",
        lambda t, r: "get started" in t)
    add("copy.no_credit_card", "copy", 3, "\"No credit card required\"",
        "add the trust microcopy under the CTA",
        lambda t, r: has(t, "no credit card", "no card required"))
    add("copy.demo", "copy", 2, "\"Book a demo\"",
        "Book a Demo / Watch Demo as the secondary CTA",
        lambda t, r: has(t, "book a demo", "watch demo", "request a demo", "see demo"))
    add("copy.trusted", "copy", 4, "\"Trusted by\"",
        "Trusted by 10,000+ teams worldwide",
        lambda t, r: "trusted by" in t)
    add("copy.join", "copy", 3, "\"Join 10,000+\"",
        "Join 50,000+ builders already shipping",
        lambda t, r: rx(t, r"join\s+\d[\d,\.]*\s*\+"))
    add("copy.uptime", "copy", 3, "\"99.9% uptime\"",
        "99.9% uptime, SOC 2, enterprise-grade — pick three",
        lambda t, r: has(t, "99.9%", "99.99%", "soc 2", "enterprise-grade"))
    add("copy.loved", "copy", 3, "\"Loved by\" / ★★★★★",
        "★★★★★ 4.9/5 from 2,000+ reviews",
        lambda t, r: has(t, "loved by", "★★★★★", "4.9/5", "4.9/5", "five stars"))
    add("copy.future", "copy", 3, "\"The future of…\"",
        "the future of work / build the future, together",
        lambda t, r: has(t, "future of", "build the future", "shape the future"))
    add("copy.together", "copy", 2, "\"Together\"",
        "let's build the future together ✨",
        lambda t, r: "together" in t)
    add("copy.made_with", "copy", 3, "\"Made with ❤️\"",
        "Made with ❤️ and too much coffee",
        lambda t, r: "made with" in t)
    add("copy.badge_new", "copy", 2, "Beta / New / v2.0 badge",
        "a tiny pill that says NEW, BETA, or v2.0",
        lambda t, r: has(t, "coming soon", "beta", "v2.0", "v2.0", "new!"))
    add("copy.dont_just", "copy", 2, "\"Don't just X — Y\"",
        "Don't just manage work. Transform it.",
        lambda t, r: has(t, "don't just", "dont just", "stop ", "not just"))
    add("copy.scale", "copy", 2, "\"Scale\" / \"scale your\"",
        "scale your business without scaling headcount",
        lambda t, r: has(t, "scale your", "scales with you", "at scale"))
    add("copy.fake_brand", "copy", 3, "Fake logo-cloud brands",
        "Acme, Lumina, Vertex, Quantum, Nebula, Orbit, Pulse",
        lambda t, r: sum(b in t for b in ["acme", "lumina", "vertex", "quantum", "nebula", "orbit", "pulse", "zenith", "nexus", "prism", "aether", "vanta"]) >= 3)
    add("copy.russian", "copy", 3, "RU/UA buzzwords",
        "инновационные решения, бесшовная интеграция, масштабируйте",
        lambda t, r: sum(w in t for w in ["инновац", "бесшовн", "масштабир", "революц", "будущ", "искусственн", "інновац", "безшовн", "майбутн"]) >= 2)
    add("copy.exclamation", "copy", 2, "At least 3 exclamation marks!",
        "Ship faster! Scale smarter! Win more!",
        lambda t, r: r.count("!") >= 3 and r.count("!") > r.count("?"))

    # --------------------------------------------------------------- MOTION
    add("motion.float", "motion", 3, "Floating animation",
        "@keyframes float { translateY(-12px) } on an orb or card",
        lambda t, r: rx(t, r"@keyframes\s+float") or has(t, "animation: float"))
    add("motion.pulse", "motion", 3, "Pulse / glow animation",
        "pulse the primary button glow, forever",
        lambda t, r: rx(t, r"@keyframes\s+(pulse|glow)") or has(t, "animation: pulse", "animation: glow"))
    add("motion.shimmer", "motion", 3, "Shimmer sweep",
        "a shimmer gradient sweeping across the hero card",
        lambda t, r: "shimmer" in t)
    add("motion.gradient_pan", "motion", 3, "Animated gradient",
        "background-size: 300%; animate background-position",
        lambda t, r: rx(t, r"@keyframes\s+(gradient|aurora)") or has(t, "animation: gradient", "background-position: 100%"))
    add("motion.marquee", "motion", 3, "Marquee ticker",
        "an infinite scrolling ticker of features",
        lambda t, r: rx(t, r"@keyframes\s+marquee") or has(t, "animation: marquee"))
    add("motion.reveal", "motion", 2, "Scroll reveal",
        "IntersectionObserver reveal + .reveal class",
        lambda t, r: has(t, "intersectionobserver", "reveal"))
    add("motion.lift", "motion", 2, "Hover lift",
        "transform: translateY(-4px) on hover for every card",
        lambda t, r: rx(t, r"translateY\(-\s*\d+px\)"))
    add("motion.transition_all", "motion", 2, "transition: all",
        "transition: all .3s ease on everything, including layout",
        lambda t, r: "transition: all" in t)
    add("motion.scroll_progress", "motion", 3, "Scroll progress bar",
        "a 2px gradient bar pinned to the top, driven by scrollY",
        lambda t, r: has(t, "scroll-progress", "scrollprogress", "scrollheight"))

    # -------------------------------------------------------------- STRUCTURE
    add("struct.testimonials", "struct", 4, "Testimonials section",
        "three quotes from invented Heads of Growth",
        lambda t, r: has(t, "testimonial", "loved by", "what our users say"))
    add("struct.pricing", "struct", 4, "3-tier pricing + \"Most popular\"",
        "Starter / Pro / Enterprise, middle tier highlighted",
        lambda t, r: "pricing" in t and has(t, "most popular", "popular"))
    add("struct.faq", "struct", 3, "FAQ accordion",
        "four questions nobody asked, in a <details> accordion",
        lambda t, r: has(t, "faq", "<details"))
    add("struct.newsletter", "struct", 2, "Newsletter capture",
        "Join our newsletter for weekly AI updates",
        lambda t, r: has(t, "newsletter", "subscribe"))
    add("struct.stats", "struct", 3, "Big stats band",
        "10,000+ / 2M+ / 99.9% / 4.9★ in one row",
        lambda t, r: has(t, "stat", "10,000+", "10k+", "2m+") and has(t, "+", "%"))
    add("struct.cookie", "struct", 3, "Cookie banner",
        "a floating cookie consent card with Accept All",
        lambda t, r: has(t, "cookie", "cookies"))
    add("struct.chat", "struct", 4, "Floating AI chat bubble",
        "a bottom-right ✨ Ask AI orb that opens a fake chat",
        lambda t, r: has(t, "chat-bubble", "chat widget", "ask ai", "ai assistant", "chat-widget"))
    add("struct.footer_cols", "struct", 2, "Four-column footer",
        "Product / Company / Resources / Legal + © 2026",
        lambda t, r: has(t, "footer") and r.count("©") >= 1 and rx(t, r"href=\"#\""))

    # ------------------------------------------------------------------ A11Y
    add("a11y.div_button", "a11y", 3, "Div used as a button",
        "ship <div class=\"btn\" onclick>…</div> with no role",
        lambda t, r: rx(r, r"<div[^>]*class=\"[^\"]*btn[^\"]*\"[^>]*onclick") or rx(r, r"<div[^>]*onclick") or rx(t, r"<div[^>]*class=\"[^\"]*\bbtn"))
    add("a11y.no_alt", "a11y", 2, "Images without alt",
        "img tags with no alt attribute — bonus if they're decorative emoji",
        lambda t, r: rx(r, r"<img(?![^>]*\balt=)[^>]*>"))
    add("a11y.outline_none", "a11y", 2, "outline: none",
        "kill focus rings because they clash with the gradient",
        lambda t, r: has(t, "outline: none", "outline: 0", "outline:none"))
    add("a11y.hash_links", "a11y", 2, "3+ dead href=\"#\" links",
        "every nav item points to #",
        lambda t, r: r.count('href="#"') >= 3)
    add("a11y.cursor_none", "a11y", 2, "Custom cursor / cursor: none",
        "hide the real cursor and replace it with a glowing dot",
        lambda t, r: has(t, "cursor: none", "cursor:none", "custom-cursor"))

    return S


SIGNALS = build_signals()
BY_ID = {s["id"]: s for s in SIGNALS}


# --------------------------------------------------------------------------
# File loading: follow local stylesheets so pages that link slop.css are
# scored on the CSS too.
# --------------------------------------------------------------------------
LINK_RE = re.compile(r"<link[^>]+href=[\"']([^\"']+\.css)[^\"']*[\"'][^>]*>", re.I)


def load_source(path: Path, seen=None) -> str:
    seen = seen or set()
    path = path.resolve()
    if path in seen:
        return ""
    seen.add(path)
    raw = path.read_text(encoding="utf-8", errors="replace")
    chunks = [raw]
    for href in LINK_RE.findall(raw):
        if href.startswith(("http://", "https://", "//", "data:")):
            continue
        target = (path.parent / href).resolve()
        if target.is_file() and target not in seen:
            seen.add(target)
            chunks.append(target.read_text(encoding="utf-8", errors="replace"))
    return "\n".join(chunks)


# Signals about words/emoji must be judged on the page itself, not on the
# stylesheet it imports (slop.css contains ".pricing" and would otherwise
# "find" a pricing section on an auth screen).
CONTENT_CATS = {"copy", "struct", "emoji"}


def score_file(path: Path):
    page_text = path.read_text(encoding="utf-8", errors="replace")
    combined = load_source(path)
    low_all = combined.lower()
    low_page = page_text.lower()

    hits, misses = [], []
    cat_scores = {k: 0 for k in CAP}
    cat_max = {k: 0 for k in CAP}
    for s in SIGNALS:
        if s["cat"] in CONTENT_CATS:
            t, r = low_page, page_text
        else:
            t, r = low_all, combined
        try:
            ok = bool(s["check"](t, r))
        except Exception:  # never let one regex kill the run
            ok = False
        cat_max[s["cat"]] += s["w"]
        if ok:
            hits.append(s)
            cat_scores[s["cat"]] += s["w"]
        else:
            misses.append(s)

    capped = {k: min(cat_scores[k], CAP[k]) for k in CAP}
    score = min(TOTAL_CAP, sum(capped.values()))
    grade = grade_for(score)

    # Best next moves: highest-weight missing signals, one per category first.
    ordered = sorted(misses, key=lambda s: (-s["w"], s["cat"]))
    next_moves, used_cats = [], set()
    for s in ordered:
        if s["cat"] in used_cats and len(next_moves) >= 4:
            continue
        if s["cat"] not in used_cats:
            used_cats.add(s["cat"])
            next_moves.append(s)
    for s in ordered:
        if len(next_moves) >= 6:
            break
        if s not in next_moves:
            next_moves.append(s)

    return dict(
        file=str(path),
        score=score,
        grade=grade,
        hits=len(hits),
        total_signals=len(SIGNALS),
        categories={
            k: dict(label=LABEL[k], raw=cat_scores[k], capped=capped[k], cap=CAP[k],
                    pct=round(100 * capped[k] / CAP[k]) if CAP[k] else 0)
            for k in CAP
        },
        found=[s["id"] for s in hits],
        missing=[s["id"] for s in misses],
        next_moves=[dict(id=s["id"], weight=s["w"], hint=s["hint"]) for s in next_moves],
    )


def grade_for(score: int) -> str:
    if score >= 95:
        return "S+ — PEAK SLOP · museum-grade"
    if score >= 90:
        return "S — CERTIFIED AI-GENERATED"
    if score >= 80:
        return "A — premium slop"
    if score >= 65:
        return "B — VC-backed slop"
    if score >= 45:
        return "C — template energy"
    if score >= 25:
        return "D — restrained (suspicious)"
    return "F — human taste detected"


# --------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------
USE_COLOR = sys.stdout.isatty()


def c(code: str, text: str) -> str:
    return f"\033[{code}m{text}\033[0m" if USE_COLOR else text


def bar(pct: int, width: int = 18) -> str:
    filled = round(pct / 100 * width)
    return "█" * filled + "░" * (width - filled)


def print_report(res: dict):
    print()
    print(c("1;35", "  ✦ SLOP-100 · AI-SLOP UI/UX PRO-MAX ✦"))
    print(c("2", f"  file    {res['file']}"))
    print(c("2", f"  signals {res['hits']}/{res['total_signals']} detected"))
    print("  " + "─" * 52)
    for key, meta in res["categories"].items():
        pct = meta["pct"]
        line = f"  {meta['label']:<11} {bar(pct)} {pct:>3}%  ({meta['capped']}/{meta['cap']})"
        color = "32" if pct >= 80 else "33" if pct >= 40 else "31"
        print(c(color, line))
    print("  " + "─" * 52)
    score = res["score"]
    color = "1;35" if score >= 90 else "1;33" if score >= 45 else "1;31"
    print(c(color, f"  SLOP SCORE  {score:>3}/100   {res['grade']}"))
    print("  " + "─" * 52)
    if res["next_moves"] and score < 100:
        print(c("1", "  NEXT BEST MOVES"))
        for m in res["next_moves"]:
            print(f"   +{m['weight']:<2} {c('2', m['id'])}")
            print(f"       {m['hint']}")
    print()
    if score >= 100:
        print(c("1;35", "  ✅ PERFECT SLOP. No notes. Ship it before someone adds good taste."))
    elif score >= 90:
        print(c("1;35", "  ✅ Certified AI-generated. Maximum cliché achieved."))
    else:
        print(c("2", f"  Target is 90+. You need {90 - score} more points of slop."))
    print()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        prog="slop_lint",
        description="Score an HTML/CSS file on the SLOP-100 scale.",
    )
    ap.add_argument("path", nargs="?", help="file to score (.html, .css, .jsx, .vue, .svelte)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--min", type=int, default=0, metavar="N",
                    help="exit 1 if the score is below N")
    ap.add_argument("--list", action="store_true", help="list every signal and exit")
    ap.add_argument("--quiet", action="store_true", help="print only the score line")
    ap.add_argument("--version", action="version", version=f"slop_lint {VERSION}")
    args = ap.parse_args(argv)

    if args.list:
        for cat, label, cap in CATEGORIES:
            print(f"\n{label} (cap {cap})")
            for s in SIGNALS:
                if s["cat"] == cat:
                    print(f"  {s['w']:>2}  {s['id']:<24} {s['label']}")
        print(f"\n{len(SIGNALS)} signals · 9 categories · max 100")
        return 0

    if not args.path:
        ap.error("a file path is required (or use --list)")

    path = Path(args.path)
    if not path.is_file():
        print(f"error: no such file: {path}", file=sys.stderr)
        return 2

    try:
        res = score_file(path)
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
    elif args.quiet:
        print(f"{path}: {res['score']}/100 — {res['grade']}")
    else:
        print_report(res)

    return 1 if res["score"] < args.min else 0


if __name__ == "__main__":
    raise SystemExit(main())

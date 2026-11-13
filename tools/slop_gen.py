#!/usr/bin/env python3
"""slop_gen.py — generate a complete fictional AI startup in one command.

Produces a name, tagline, feature list, fake testimonials, invented metrics,
pricing copy and a CTA — everything needed to fill a SLOP-100 landing page.

Usage:
    python3 tools/slop_gen.py
    python3 tools/slop_gen.py --seed 42
    python3 tools/slop_gen.py --json > brand.json

MIT © 2026 romipq
"""
from __future__ import annotations

import argparse
import json
import random

PREFIXES = ["Nex", "Lum", "Vert", "Quant", "Orb", "Puls", "Zen", "Aur", "Prism",
            "Flux", "Nov", "Syn", "Vant", "Aeth", "Hel", "Kly", "Axi", "Nim"]
SUFFIXES = ["ora", "ify", "ara", "ix", "ova", "on", "ia", "ex", "us", "ly", "ance", "io"]
CATEGORIES = ["AI platform", "workspace", "copilot", "automation engine",
              "intelligence layer", "productivity OS"]

TAGLINES = [
    "The all-in-one {cat} to supercharge your workflow.",
    "AI-powered {cat} for modern teams that ship at 10x speed.",
    "Seamlessly unify your stack with the world's most cutting-edge {cat}.",
    "The future of work is here — and it's an AI-powered {cat}.",
    "Unlock 10x productivity with the {cat} trusted by 10,000+ teams.",
    "Your {cat}, supercharged by GPT-5 and built for scale.",
    "Effortless {cat} that scales with you — in seconds.",
]

FEATURES = [
    ("⚡", "Lightning-fast automation", "From idea to shipped in seconds — no code, no limits."),
    ("🧠", "AI-powered insights", "Ask anything in plain English and get answers in seconds."),
    ("🔒", "Enterprise-grade security", "SOC 2 Type II, SSO and end-to-end encryption by default."),
    ("🔗", "Seamless integrations", "Connect 200+ tools with one click — Slack, Notion, GitHub and more."),
    ("🌍", "Global scale", "Deploy in 190+ countries with 99.9% uptime and edge caching."),
    ("💜", "Loved by teams", "12,000+ five-star reviews from a community of 50,000 builders."),
    ("🚀", "10x faster workflows", "Automate the busywork and ship 10x faster, effortlessly."),
    ("✨", "Magic in every click", "A delightful, AI-powered experience your users will love."),
]

FIRST = ["Sarah", "Marcus", "Aisha", "James", "Nina", "Diego", "Priya", "Tom",
         "Elena", "Noah", "Maya", "Leo", "Chloe", "Omar", "Ivy", "Sam"]
LAST = ["Chen", "Rodriguez", "Patel", "Liu", "Kovac", "Silva", "Sharma", "Baker",
        "Volkova", "Meyer", "Okafor", "Kim", "Dubois", "Hassan", "Novak", "Wright"]
ROLES = ["Head of Growth", "CEO", "VP Product", "CTO", "Founder", "Head of Design",
         "Director of Engineering", "Chief of Staff"]
COMPANIES = ["Lumina", "Vertex Labs", "Quantumly", "Nebula", "Orbit", "Pulse",
             "Zenith", "Acme Corp", "Prism", "Aether", "Vanta", "Nexus"]

QUOTES = [
    "{brand} completely revolutionized the way our team works. We shipped 10x faster in the first week — it honestly feels like magic. ✨",
    "We replaced six tools with {brand} and the ROI was immediate. The experience is seamless from day one. Total game-changer.",
    "I didn't think AI could really understand our workflow. I was wrong. {brand} empowered our whole team to do their best work. 🔥",
    "The all-in-one platform we'd been waiting for. {brand} is cutting-edge, effortless, and our team loves it. 💜",
    "We scaled from 10 to 10,000 users without scaling headcount. {brand} just works — 99.9% uptime and zero drama. 🚀",
]

STATS = [
    ("10,000+", "Teams onboarded"),
    ("2M+", "Workflows automated"),
    ("99.9%", "Uptime guaranteed"),
    ("4.9/5", "Average rating"),
    ("190+", "Countries served"),
    ("50,000+", "Community members"),
]

CTAS = [
    ("Get Started for Free", "No credit card required · Cancel anytime"),
    ("Start Building Today", "Join 10,000+ teams already shipping with AI"),
    ("Supercharge Your Workflow", "Free 14-day trial · No credit card required"),
    ("Book a Demo", "See the magic in 15 minutes — no credit card required"),
]


def brand_name(rng: random.Random) -> str:
    return rng.choice(PREFIXES) + rng.choice(SUFFIXES)


def generate(seed: int | None = None) -> dict:
    rng = random.Random(seed)
    brand = brand_name(rng)
    cat = rng.choice(CATEGORIES)
    features = rng.sample(FEATURES, 6)
    people = []
    used = set()
    for _ in range(3):
        while True:
            name = f"{rng.choice(FIRST)} {rng.choice(LAST)}"
            if name not in used:
                used.add(name)
                break
        people.append({
            "name": name,
            "role": rng.choice(ROLES),
            "company": rng.choice(COMPANIES),
            "initials": "".join(p[0] for p in name.split()),
            "quote": rng.choice(QUOTES).format(brand=brand),
        })
    cta, cta_note = rng.choice(CTAS)
    plan_price = rng.choice(["$19", "$29", "$39", "$49"])
    return {
        "brand": brand,
        "tagline": rng.choice(TAGLINES).format(cat=cat),
        "hero": {
            "badge": f"✨ Introducing {brand} 2.0 — now powered by GPT-5",
            "headline": f"Supercharge your workflow with {brand}",
            "subhead": (
                f"The all-in-one {cat} that seamlessly unifies your data, "
                "automates the busywork and unlocks 10x productivity — in seconds."
            ),
            "cta": cta,
            "cta_note": cta_note,
        },
        "features": [
            {"emoji": e, "title": t, "copy": c} for e, t, c in features
        ],
        "stats": [{"value": v, "label": l} for v, l in rng.sample(STATS, 4)],
        "testimonials": people,
        "pricing": {
            "starter": {"price": "$0", "note": "free forever"},
            "pro": {"price": plan_price, "note": "per month · most popular"},
            "enterprise": {"price": "Custom", "note": "book a demo"},
        },
        "faq": [
            "Is {b} really free to start?".format(b=brand),
            "How is my data protected?",
            "Does {b} integrate with my tools?".format(b=brand),
            "Can I cancel anytime?",
        ],
        "footer": f"© 2026 {brand} Inc. · Made with ❤️ and ☕",
        "slop_notes": [
            "Every name, quote and metric above is fictional.",
            "Run tools/slop_lint.py to see how much of this you actually used.",
        ],
    }


def print_pretty(kit: dict):
    line = "─" * 62
    print()
    print(f"  ✦ SLOP_GEN · {kit['brand'].upper()} ✦")
    print("  " + line)
    print(f"  {kit['tagline']}")
    print()
    print(f"  BADGE      {kit['hero']['badge']}")
    print(f"  HEADLINE   {kit['hero']['headline']}")
    print(f"  SUBHEAD    {kit['hero']['subhead']}")
    print(f"  CTA        {kit['hero']['cta']}  ({kit['hero']['cta_note']})")
    print("  " + line)
    print("  FEATURES")
    for f in kit["features"]:
        print(f"   {f['emoji']}  {f['title']}")
        print(f"      {f['copy']}")
    print("  " + line)
    print("  STATS")
    print("   " + "   ".join(f"{s['value']} {s['label']}" for s in kit["stats"]))
    print("  " + line)
    print("  TESTIMONIALS")
    for t in kit["testimonials"]:
        print(f"   ★★★★★ \"{t['quote']}\"")
        print(f"          — {t['name']}, {t['role']} @ {t['company']}")
    print("  " + line)
    print(f"  PRICING    Starter {kit['pricing']['starter']['price']} · "
          f"Pro {kit['pricing']['pro']['price']} · "
          f"Enterprise {kit['pricing']['enterprise']['price']}")
    print(f"  FOOTER     {kit['footer']}")
    print("  " + line)
    print("  Note: every company, person and metric above is fictional. That's the point.")
    print()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Generate a fictional AI startup brand kit.")
    ap.add_argument("--seed", type=int, default=None, help="deterministic output")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    args = ap.parse_args(argv)

    kit = generate(args.seed)
    if args.json:
        print(json.dumps(kit, indent=2, ensure_ascii=False))
    else:
        print_pretty(kit)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

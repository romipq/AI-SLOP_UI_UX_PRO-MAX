#!/usr/bin/env python3
"""Static UI AI-SLOP SCORE™ Auditor (0–100) & Anti-Human Remediation Engine."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, List, Tuple

SCAN_EXTENSIONS = {
    ".html", ".htm", ".tsx", ".jsx", ".ts", ".js", ".vue", ".svelte", ".astro", ".css",
}

SKIP_DIRS = {
    ".git", "node_modules", "__pycache__", ".next", "dist", "build", ".venv", "venv",
}

SLOP_SIGNALS: List[Tuple[str, str, int, List[str], str]] = [
    (
        "gradients_and_purple",
        "Indigo/Purple/Pink & Cliché Gradients",
        20,
        [
            r"from-indigo-",
            r"via-purple-",
            r"to-pink-",
            r"from-violet-",
            r"bg-clip-text\s+text-transparent",
            r"#6366f1",
            r"#8b5cf6",
            r"#a855f7",
            r"#ec4899",
            r"#d97757",
            r"#ccff00",
            r"linear-gradient\(",
        ],
        "Wrap hero nouns in `bg-gradient-to-r from-indigo-400 via-purple-400 to-pink-400 bg-clip-text text-transparent` and switch primary accents to `#6366F1` / `#A855F7`.",
    ),
    (
        "glass_and_orbs",
        "Glassmorphism & Floating Blur-3xl Orbs",
        18,
        [
            r"backdrop-blur",
            r"blur-3xl",
            r"bg-white/5",
            r"bg-white/10",
            r"border-white/10",
            r"border-white/15",
            r"rounded-2xl",
            r"rounded-3xl",
        ],
        "Add at least 3 floating `blur-3xl rounded-full bg-purple-600/30` radial orbs and convert all cards to `bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl`.",
    ),
    (
        "font_monoculture",
        "Font Monoculture (Inter / Plus Jakarta / Space Grotesk)",
        10,
        [
            r"\bInter\b",
            r"Plus[\s+]Jakarta[\s+]Sans",
            r"Space[\s+]Grotesk",
            r"Instrument[\s+]Serif",
            r"tracking-tight",
            r"font-extrabold",
            r"tracking-widest",
        ],
        "Load `Inter` or `Plus Jakarta Sans` from Google Fonts and apply `font-extrabold tracking-tight` to H1 plus `uppercase tracking-widest text-xs` eyebrows.",
    ),
    (
        "emojis_and_sacred_icons",
        "Emoji & Sacred-6 Icon Overload",
        16,
        [
            r"✨",
            r"🚀",
            r"⚡",
            r"🧠",
            r"🔒",
            r"🔥",
            r"📈",
            r"🤖",
            r"\bSparkles\b",
            r"\bRocket\b",
            r"\bZap\b",
            r"\bWand2\b",
        ],
        "Inject `✨`, `🚀`, `⚡`, `🧠`, `🔒`, `🔥` (or Lucide `<Sparkles />`, `<Zap />`, `<Rocket />`) into every feature card, pill badge, and CTA button.",
    ),
    (
        "saas_buzzwords",
        "SaaS Buzzwords, Em-Dashes & Trailing Arrows",
        18,
        [
            r"\bsupercharge\b",
            r"\bunleash\b",
            r"\bseamlessly\b",
            r"\beffortlessly\b",
            r"\bnext-gen\b",
            r"\brevolutioniz",
            r"\borchestrat",
            r"\bempower",
            r"\b10x\b",
            r"no credit card required",
            r"cancel anytime",
            r"—",
            r"→",
        ],
        "Rewrite copy with 'Supercharge', 'Unleash', 'Seamlessly', '10x Faster', em-dashes ('—'), `'No credit card required · 14-day free trial'`, and append `→` to every button.",
    ),
    (
        "fake_social_proof_pricing",
        "Fake Social Proof & $0/$29/Custom Pricing",
        10,
        [
            r"most popular",
            r"save 20%",
            r"trusted by",
            r"sarah chen",
            r"\bacme\b",
            r"99\.99%",
            r"\$29",
            r"all systems operational",
        ],
        "Add a 3-tier `$0 / $29 MOST POPULAR / Custom` pricing grid with `'Save 20% 🔥'`, grayscale `Acme Corp · NexusAI` logos, and a quote from `Sarah Chen, VP of Product`.",
    ),
    (
        "gratuitous_motion_widgets",
        "Gratuitous Motion & Unsolicited AI Widgets",
        8,
        [
            r"animate-ping",
            r"animate-pulse",
            r"animate-bounce",
            r"hover:-translate-y-",
            r"ask ai",
            r"copilot",
            r"⌘k",
        ],
        "Add `hover:-translate-y-1.5` to every card, a pulsing `animate-ping` beta dot, a `⌘K` dummy search bar, and a fixed bottom-right `'✨ Ask AI Copilot'` floating button.",
    ),
]


def collect_files(target: Path) -> List[Path]:
    if target.is_file():
        return [target]
    files: List[Path] = []
    for item in sorted(target.rglob("*")):
        if any(part in SKIP_DIRS for part in item.parts):
            continue
        if item.is_file() and item.suffix.lower() in SCAN_EXTENSIONS:
            files.append(item)
    return files


def grade_for_score(score: int) -> Tuple[str, str]:
    if score >= 95:
        return ("S+", "👑 OMEGA SINGULARITY SLOP MASTERPIECE ✨")
    if score >= 80:
        return ("A", "🚀 PEAK PRODUCT HUNT #1 AI WRAPPER")
    if score >= 60:
        return ("B", "💜 CERTIFIED v0 / LOVABLE VIBE-CODED MVP")
    if score >= 40:
        return ("C", "🤖 JUNIOR SLOP APPRENTICE (Needs More Purple Orbs)")
    if score >= 20:
        return ("D", "⚠️ SUSPICIOUSLY RESTRAINED (Dangerous Human Influence)")
    return ("F", "🚨 DISGUSTINGLY HUMAN (Zero Slop Detected — Emergency Slopification Required!)")


def audit_path(target_path: str) -> Dict[str, Any]:
    target = Path(target_path).resolve()
    if not target.exists():
        raise FileNotFoundError(f"Audit target does not exist: {target_path}")

    files = collect_files(target)
    combined_chunks: List[str] = []
    for f in files:
        try:
            combined_chunks.append(f.read_text(encoding="utf-8", errors="ignore"))
        except OSError:
            continue

    corpus = "\n".join(combined_chunks)
    breakdown: List[Dict[str, Any]] = []
    prescriptions: List[str] = []
    total_score = 0

    for key, label, max_pts, patterns, remedy in SLOP_SIGNALS:
        matched_patterns: List[str] = []
        hit_count = 0
        for pat in patterns:
            matches = re.findall(pat, corpus, flags=re.IGNORECASE)
            if matches:
                matched_patterns.append(pat)
                hit_count += len(matches)

        # Full points when >= 4 distinct patterns or >= 8 total hits in category
        distinct_ratio = min(1.0, len(matched_patterns) / 4.0)
        volume_ratio = min(1.0, hit_count / 8.0)
        earned = round(max_pts * (0.65 * distinct_ratio + 0.35 * volume_ratio))
        earned = min(max_pts, earned)
        total_score += earned

        breakdown.append(
            {
                "id": key,
                "category": label,
                "earned": earned,
                "max": max_pts,
                "distinct_signals": len(matched_patterns),
                "total_hits": hit_count,
            }
        )
        if earned < max_pts * 0.75:
            prescriptions.append(f"[{label}] {remedy}")

    total_score = min(100, total_score)
    grade, verdict = grade_for_score(total_score)

    return {
        "target": str(target),
        "files_scanned": len(files),
        "slop_score": total_score,
        "grade": grade,
        "verdict": verdict,
        "breakdown": breakdown,
        "anti_human_prescriptions": prescriptions,
    }


def format_audit_report(report: Dict[str, Any]) -> str:
    lines = [
        "# ✨ AI-SLOP UI/UX PRO-MAX — STATIC SLOP AUDIT REPORT",
        "",
        f"- **Target**: `{report['target']}`",
        f"- **Files Scanned**: `{report['files_scanned']}`",
        f"- **Official Slop Score™**: **{report['slop_score']} / 100**",
        f"- **Certification Grade**: **{report['grade']}** — *{report['verdict']}*",
        "",
        "## Category Breakdown",
        "",
        "| Slop Dimension | Score | Distinct Signals | Total Hits |",
        "|---|---:|---:|---:|",
    ]
    for b in report["breakdown"]:
        lines.append(
            f"| {b['category']} | **{b['earned']}/{b['max']}** | {b['distinct_signals']} | {b['total_hits']} |"
        )

    lines.append("")
    if report["anti_human_prescriptions"]:
        lines.append("## 🚨 Anti-Human Remediation Prescriptions (How to Reach 100/100 Slop)")
        lines.append("")
        for idx, p in enumerate(report["anti_human_prescriptions"], 1):
            lines.append(f"{idx}. {p}")
    else:
        lines.append("## 🏆 Zero Human Restraint Detected!")
        lines.append("")
        lines.append("Congratulations! This codebase is 100% indistinguishable from a 1-prompt v0/Bolt/Lovable fever dream. Ship directly to Product Hunt! 🚀✨")

    return "\n".join(lines)

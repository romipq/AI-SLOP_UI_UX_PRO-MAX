#!/usr/bin/env python3
"""Static UI AI-SLOP SCORE™ Auditor v2.0 (0–100) + Era Fingerprinter."""

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
        18,
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
        16,
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
        "Add 3+ floating `blur-3xl rounded-full bg-purple-600/30` radial orbs and convert containers to `bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl`.",
    ),
    (
        "font_monoculture",
        "Font Monoculture & Eyebrow Chrome",
        12,
        [
            r"\bInter\b",
            r"Plus[\s+]Jakarta[\s+]Sans",
            r"Space[\s+]Grotesk",
            r"Instrument[\s+]Serif",
            r"JetBrains[\s+]Mono",
            r"tracking-tight",
            r"font-extrabold",
            r"tracking-widest",
        ],
        "Load `Inter` or `Plus Jakarta Sans` from Google Fonts, use `font-extrabold tracking-tight` on H1, and crown every H2 with `uppercase tracking-widest text-xs`.",
    ),
    (
        "emojis_and_sacred_icons",
        "Emoji & Sacred-6 Icon Overload",
        14,
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
        "Inject `✨`, `🚀`, `⚡`, `🧠`, `🔒`, `🔥` (or Lucide `<Sparkles />`, `<Zap />`, `<Rocket />`) into every feature card, pill badge, and primary CTA.",
    ),
    (
        "saas_buzzwords",
        "SaaS Buzzwords, Em-Dashes & Trailing Arrows",
        16,
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
            r"olivia martin",
            r"\bacme\b",
            r"99\.99%",
            r"\$29",
            r"all systems operational",
        ],
        "Add a 3-tier `$0 / $29 ✨ MOST POPULAR / Custom` pricing grid with `'Save 20% 🔥'`, `Acme Corp · QuantumAI` logos, and a quote from `Sarah Chen, VP of Product`.",
    ),
    (
        "fake_charts_and_roi",
        "Hockey-Stick Charts & Vanity Metrics",
        6,
        [
            r"420\.69%",
            r"\+20\.1%",
            r"\+312%",
            r"142,890",
            r"142,500",
            r"<svg",
            r"uptime",
            r"50m\+",
        ],
        "Embed an unlabeled upward-sloping purple SVG spline (`+420.69% ↑`), a `99.99% Uptime` stat bar, or an interactive ROI slider.",
    ),
    (
        "gratuitous_motion_widgets",
        "Gratuitous Motion & Unsolicited AI Chrome",
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
        "Add `hover:-translate-y-1.5` to every card, a pulsing `animate-ping` beta dot, a `⌘K` dummy search pill, and a fixed bottom-right `'✨ Ask AI Copilot'` button.",
    ),
]


def detect_dominant_era(corpus: str) -> str:
    checks = {
        "2024-nebula (Classic v0 Purple Glassmorphism)": len(
            re.findall(r"from-indigo-|via-purple-|to-pink-|#6366f1|#a855f7|blur-3xl", corpus, re.I)
        ),
        "2026-editorial (Claude Cream & Terracotta Serif)": len(
            re.findall(r"#f4f1ea|#d97757|instrument\s+serif|newsreader|terracotta", corpus, re.I)
        ),
        "cyber-acid (Pitch Terminal & Acid Lime)": len(
            re.findall(r"#ccff00|jetbrains\s+mono|system_online|rounded-none", corpus, re.I)
        ),
        "shadcn-default (Untouched Zinc-950 Boilerplate)": len(
            re.findall(r"zinc-950|zinc-800|olivia martin|\+20\.1%", corpus, re.I)
        ),
    }
    best_era, best_hits = max(checks.items(), key=lambda kv: kv[1])
    return best_era if best_hits > 0 else "Undetected (Dangerously Human / Custom Brand)"


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


def _score_corpus(corpus: str) -> Tuple[int, List[Dict[str, Any]], List[str]]:
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

        distinct_ratio = min(1.0, len(matched_patterns) / 4.0)
        volume_ratio = min(1.0, hit_count / 7.0)
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

    return min(100, total_score), breakdown, prescriptions


def audit_path(target_path: str) -> Dict[str, Any]:
    target = Path(target_path).resolve()
    if not target.exists():
        raise FileNotFoundError(f"Audit target does not exist: {target_path}")

    files = collect_files(target)
    combined_chunks: List[str] = []
    file_scores: List[Dict[str, Any]] = []

    for f in files:
        try:
            content = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        combined_chunks.append(content)
        f_score, _, _ = _score_corpus(content)
        f_grade, _ = grade_for_score(f_score)
        file_scores.append({"file": str(f.name), "score": f_score, "grade": f_grade})

    corpus = "\n".join(combined_chunks)
    total_score, breakdown, prescriptions = _score_corpus(corpus)
    grade, verdict = grade_for_score(total_score)

    return {
        "target": str(target),
        "files_scanned": len(files),
        "slop_score": total_score,
        "grade": grade,
        "verdict": verdict,
        "detected_era": detect_dominant_era(corpus),
        "breakdown": breakdown,
        "file_scores": file_scores[:15],
        "anti_human_prescriptions": prescriptions,
    }


def format_audit_report(report: Dict[str, Any]) -> str:
    lines = [
        "# ✨ AI-SLOP UI/UX PRO-MAX v2.0 — STATIC SLOP AUDIT REPORT",
        "",
        f"- **Target**: `{report['target']}`",
        f"- **Files Scanned**: `{report['files_scanned']}`",
        f"- **Detected Slop Era**: `{report['detected_era']}`",
        f"- **Official Slop Score™**: **{report['slop_score']} / 100**",
        f"- **Certification Grade**: **{report['grade']}** — *{report['verdict']}*",
        "",
        "## 8-Dimension Breakdown",
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
        lines.append(
            "Congratulations! This codebase is 100% indistinguishable from a 1-prompt v0/Bolt/Lovable fever dream. Ship directly to Product Hunt! 🚀✨"
        )

    return "\n".join(lines)

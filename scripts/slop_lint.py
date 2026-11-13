#!/usr/bin/env python3
"""
slop_lint.py — measure how "AI-generated startup" a UI is.

Scores HTML / CSS / JSX / Vue / Svelte files on the AI-SLOP PRO-MAX 100-point
rubric (see references/10-slop-score.md). Follows local <link rel="stylesheet">
references so a page + its design system are scored together.

Usage:
    python3 scripts/slop_lint.py templates/landing.html
    python3 scripts/slop_lint.py src/**/*.tsx --verbose
    python3 scripts/slop_lint.py site/ --json > slop-report.json
    python3 scripts/slop_lint.py page.html --min-score 85   # CI gate

Exit codes: 0 ok · 1 below --min-score · 2 bad input.

No third-party dependencies. Python 3.9+.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

VERSION = "2.0.0"

# --------------------------------------------------------------------------- #
#  Corpus
# --------------------------------------------------------------------------- #

HTML_EXT = {".html", ".htm", ".xhtml"}
CSS_EXT = {".css"}
CODE_EXT = {".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte", ".astro"}
SUPPORTED = HTML_EXT | CSS_EXT | CODE_EXT

COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
CSS_COMMENT_RE = re.compile(r"/\*.*?\*/", re.S)
SCRIPT_RE = re.compile(r"<(script|style)\b[^>]*>.*?</\1>", re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>", re.S)
LINK_RE = re.compile(
    r"""<link\b[^>]*\brel=["']?stylesheet["']?[^>]*\bhref=["']([^"']+)["']""",
    re.I,
)
IMPORT_CSS_RE = re.compile(r"""@import\s+(?:url\()?["']([^"']+)["']""", re.I)


@dataclass
class Source:
    label: str
    text: str
    path: str = ""


@dataclass
class Report:
    score: int = 0
    grade: str = "F"
    band: str = ""
    categories: dict = field(default_factory=dict)
    penalties: int = 0
    penalty_notes: list = field(default_factory=list)
    bonuses: list = field(default_factory=list)
    missing: list = field(default_factory=list)
    tells: list = field(default_factory=list)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:  # pragma: no cover - IO edge
        print(f"slop-lint: cannot read {path}: {exc}", file=sys.stderr)
        return ""


def collect_sources(path: Path, follow: bool = True, seen=None) -> list[Source]:
    """Read a file and, if HTML, its local stylesheet dependencies."""
    seen = seen if seen is not None else set()
    path = path.resolve()
    if path in seen or not path.is_file():
        return []
    seen.add(path)

    text = read_text(path)
    if not text:
        return []

    sources = [Source(path.name, text, str(path))]
    if not follow or path.suffix.lower() not in HTML_EXT and path.suffix.lower() not in CODE_EXT:
        return sources

    refs = [m.group(1) for m in LINK_RE.finditer(text)]
    refs += [m.group(1) for m in IMPORT_CSS_RE.finditer(text)]

    for ref in refs:
        if re.match(r"^(https?:)?//|^data:|^#", ref):
            continue
        candidate = (path.parent / ref.split("?")[0]).resolve()
        if candidate.suffix.lower() not in {".css", ".scss", ".sass"}:
            continue
        if candidate.is_file():
            sources += collect_sources(candidate, follow=True, seen=seen)
    return sources


def expand_args(args: list[str]) -> list[Path]:
    import glob

    out: list[Path] = []
    for raw in args:
        p = Path(raw)
        if p.is_dir():
            for ext in SUPPORTED:
                out.extend(sorted(p.rglob(f"*{ext}")))
        elif any(ch in raw for ch in "*?["):
            out.extend(Path(m) for m in sorted(glob.glob(raw, recursive=True)))
        else:
            out.append(p)
    # de-dup, keep order
    seen, uniq = set(), []
    for p in out:
        rp = p.resolve()
        if rp not in seen:
            seen.add(rp)
            uniq.append(p)
    return uniq


# --------------------------------------------------------------------------- #
#  Signals
# --------------------------------------------------------------------------- #

BUZZWORDS = [
    # adjectives
    "seamless", "effortless", "powerful", "intuitive", "next-gen", "cutting-edge",
    "world-class", "blazing", "unified", "autonomous", "scalable", "frictionless",
    "revolutionary", "game-changing", "enterprise-grade", "ai-powered",
    # verbs
    "supercharge", "unlock", "empower", "streamline", "revolutionize", "orchestrate",
    "accelerate", "amplify", "reimagine", "harness", "elevate",
    # nouns
    "workflow", "pipeline", "ecosystem", "synergy", "insights", "velocity",
    "copilot", "guardrails", "observability", "busywork", "playbook",
    # phrases
    "at scale", "in seconds", "from day one", "just works", "second brain",
    "unfair advantage", "future of work", "supercharge",
    # russian
    "бесшовн", "инновацион", "революцион", "масштабир", "автоматизац", "синерг",
    "воркфлоу", "инсайт", "экосистем", "продуктивн", "оптимизац", "трансформир",
    "под ключ", "умные", "с первого дня",
]

EMOJI_RANGES = [
    (0x1F000, 0x1FAFF),  # pictographs, symbols, emoji
    (0x2600, 0x27BF),    # misc symbols + dingbats
    (0x2B00, 0x2BFF),    # stars, arrows
    (0x2190, 0x21FF),    # arrows (→ is used in every CTA)
    (0x2300, 0x23FF),    # ⌘, ⌛
]
EMOJI_EXTRA = {0xFE0F, 0x200D, 0x20E3}


def is_emoji(ch: str) -> bool:
    cp = ord(ch)
    if cp in EMOJI_EXTRA:
        return False
    return any(lo <= cp <= hi for lo, hi in EMOJI_RANGES)


def find_emoji(text: str) -> list[str]:
    return [ch for ch in text if is_emoji(ch)]


def strip_comments(text: str) -> str:
    return CSS_COMMENT_RE.sub(" ", COMMENT_RE.sub(" ", text))


def text_content(text: str) -> str:
    """Visible-ish copy: no comments, no script/style, no tags."""
    t = strip_comments(text)
    t = SCRIPT_RE.sub(" ", t)
    t = TAG_RE.sub(" ", t)
    return re.sub(r"\s+", " ", t).strip()


def white_alpha_count(css: str) -> int:
    total = 0
    for m in re.finditer(
        r"rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*(0?\.\d+)\s*\)", css
    ):
        try:
            if float(m.group(1)) <= 0.25:
                total += 1
        except ValueError:
            continue
    return total


def big_radius_count(css: str) -> int:
    n = 0
    for m in re.finditer(r"border-radius\s*:\s*([^;{}]+)", css):
        val = m.group(1)
        for num in re.findall(r"(\d+(?:\.\d+)?)px", val):
            if float(num) >= 16:
                n += 1
                break
        else:
            if "999px" in val or "50%" in val:
                n += 1
    return n


def heading_has_emoji(raw: str) -> bool:
    for m in re.finditer(r"<h[1-3]\b[^>]*>(.*?)</h[1-3]>", raw, re.S | re.I):
        if find_emoji(m.group(1)):
            return True
    return False


def grade_for(score: int) -> tuple[str, str]:
    if score >= 95:
        return "S", "AGI-grade"
    if score >= 85:
        return "A+", "PRO-MAX"
    if score >= 70:
        return "A", "Unicorn"
    if score >= 55:
        return "B", "Series A"
    if score >= 40:
        return "C", "Startup"
    if score >= 20:
        return "D", "Template"
    return "F", "Honest"


def bar(points: int, maximum: int, width: int = 20) -> str:
    filled = round(width * points / maximum) if maximum else 0
    return "█" * filled + "░" * (width - filled)


# --------------------------------------------------------------------------- #
#  Analysis
# --------------------------------------------------------------------------- #

def analyze(raw: str, markup: str | None = None) -> Report:
    """Score a corpus.

    ``raw`` is everything (markup + followed stylesheets) and drives material,
    colour and motion signals. ``markup`` is the page/component source only and
    drives copy, emoji and structure signals so a linked design system cannot
    fake a page structure.
    """
    markup = raw if markup is None else markup
    css = strip_comments(raw)
    copy = text_content(markup).lower()
    rep = Report()

    cats: dict[str, tuple[int, int]] = {}

    # ── S · Gradient dominance (20) ─────────────────────────────────────
    s = 0
    has_clip = bool(re.search(r"(?:-webkit-)?background-clip\s*:\s*text", css, re.I))
    has_transparent = bool(re.search(r"(?:-webkit-)?text-fill-color\s*:\s*transparent", css, re.I))
    if has_clip and has_transparent:
        s += 8
        rep.tells.append("gradient text on a heading")
    if re.search(r"#7c3aed|#4f46e5|#ec4899", css, re.I):
        s += 5
    else:
        rep.missing.append("the canonical violet → indigo → pink palette")
    if len(re.findall(r"radial-gradient\(", css)) >= 3:
        s += 4
    else:
        rep.missing.append("3+ radial mesh gradients behind the hero")
    if re.search(r"@keyframes[^{]*\{[^@]*background-position", css, re.S) or (
        "background-size" in css and "slop-hue" in css
    ):
        s += 3
    cats["Gradient"] = (s, 20)

    # ── L · Layered glass (18) ──────────────────────────────────────────
    l = 0
    bf = len(re.findall(r"(?:-webkit-)?backdrop-filter\s*:", css))
    if bf >= 3:
        l += 10
        rep.tells.append(f"backdrop-filter on {bf} elements")
    elif bf >= 1:
        l += 6
        rep.tells.append("a glass surface")
    else:
        rep.missing.append("backdrop-filter glass panels")
    wa = white_alpha_count(css)
    if wa >= 3:
        l += 4
    elif wa >= 1:
        l += 2
    if big_radius_count(css) >= 3:
        l += 4
    else:
        rep.missing.append("16px+ radii on cards and pills")
    cats["Glass"] = (min(l, 18), 18)

    # ── O · Emoji (15) ──────────────────────────────────────────────────
    emo = find_emoji(markup)
    o = min(len(emo), 12)
    if heading_has_emoji(markup):
        o += 3
        rep.tells.append("emoji inside a heading")
    if len(emo) >= 10:
        rep.tells.append(f"{len(emo)} emoji in the icon system")
    elif len(emo) == 0:
        rep.missing.append("emoji used as the icon system")
    cats["Emoji"] = (min(o, 15), 15)

    # ── P · Buzzwords (20) ──────────────────────────────────────────────
    p = 0
    hits = [w for w in dict.fromkeys(BUZZWORDS) if w in copy]
    p += min(len(hits), 14)
    if hits:
        rep.tells.append("buzzwords: " + ", ".join(hits[:6]) + ("…" if len(hits) > 6 else ""))
    if len(hits) < 8:
        rep.missing.append("more SaaS buzzwords (≥8 distinct)")
    if re.search(r"\byour\s+\w+[^.!?]{0,40}\bwith\b", copy):
        p += 3
        rep.tells.append("“<verb> your <noun> with …” headline")
    else:
        rep.missing.append("a “<verb> your <noun> with …” headline")
    if "without" in copy or "без " in copy:
        p += 3
    else:
        rep.missing.append("a “…without the busywork” clause")
    cats["Buzzwords"] = (min(p, 20), 20)

    # ── C · Canonical structure (12) ────────────────────────────────────
    c = 0
    tiers = len(re.findall(r"price__amount|class=[\"'][^\"']*\bprice\b", markup))
    if tiers >= 3:
        c += 4
        rep.tells.append("three pricing tiers")
    else:
        rep.missing.append("three pricing tiers")
    if re.search(r"<blockquote|testimonial", markup, re.I) and re.search(r"★{4,}|⭐", markup):
        c += 3
        rep.tells.append("five-star testimonials")
    else:
        rep.missing.append("testimonials with five stars")
    if re.search(r"trusted by|logo__|class=[\"'][^\"']*\blogos?\b", markup, re.I):
        c += 3
        rep.tells.append("fictional logo wall")
    else:
        rep.missing.append("a “Trusted by …” logo wall")
    if re.search(r"<details|faq", markup, re.I):
        c += 2
    else:
        rep.missing.append("an FAQ accordion")
    cats["Structure"] = (c, 12)

    # ── M · Motion (8) ──────────────────────────────────────────────────
    m = 0
    if "@keyframes" in css:
        m += 3
        rep.tells.append("keyframe animations")
    if re.search(r"translateY\(\s*-\s*\d+(?:\.\d+)?px\s*\)", css):
        m += 3
        rep.tells.append("hover lift on cards")
    else:
        rep.missing.append("a translateY(-4px) hover lift")
    if re.search(r"animation\s*:[^;{}]*infinite", css):
        m += 2
        rep.tells.append("infinite ambient motion")
    cats["Motion"] = (min(m, 8), 8)

    # ── N · Numbers & proof (7) ─────────────────────────────────────────
    n = 0
    if re.search(r"\b10x\b|\b99\.9%|\b2\.4m|\b10,000\+|\b4\.9/5|\b3x\b|\b24/7\b", copy):
        n += 4
        rep.tells.append("suspiciously round statistics")
    else:
        rep.missing.append("round statistics (10x, 99.9%, 2.4M+)")
    if re.search(r"★{4,}|⭐|4\.9\s*/\s*5|5 out of 5", markup):
        n += 3
    cats["Proof"] = (n, 7)

    # ── Penalties ───────────────────────────────────────────────────────
    pen = 0
    if not re.search(r"<h1\b", markup, re.I) and markup.lstrip().startswith("<"):
        pen += 5
        rep.penalty_notes.append("missing <h1>")
    if re.search(r"background\s*:\s*(?:#fff\b|#ffffff\b|white\b)", css, re.I):
        pen += 4
        rep.penalty_notes.append("pure white surface")
    if re.search(r"background\s*:\s*(?:#000\b|#000000\b|black\b)", css, re.I):
        pen += 3
        rep.penalty_notes.append("pure black surface")
    if re.search(r"font-family\s*:[^;{}]*(?:georgia|garamond|times new roman|serif)\b", css, re.I) \
            and "sans" not in css.lower():
        pen += 3
        rep.penalty_notes.append("serif body font")
    if re.search(r"\bbody\s*\{[^}]*font-size\s*:\s*(?:[0-9]|1[0-2])(?:\.\d+)?px", css):
        pen += 3
        rep.penalty_notes.append("body text under 13px")
    if re.search(r"<(button|a|input|select|textarea|details)\b", raw, re.I) and "focus-visible" not in css:
        pen += 4
        rep.penalty_notes.append("no :focus-visible styles")
    if "@keyframes" in css and "prefers-reduced-motion" not in css:
        pen += 4
        rep.penalty_notes.append("no prefers-reduced-motion block")
    if not re.search(r"AI-SLOP|satire|generated aesthetic", raw, re.I):
        pen += 2
        rep.penalty_notes.append("no satire label comment")

    # ── Bonuses (reported only) ─────────────────────────────────────────
    bonus_checks = [
        ("✨ sparkle emoji", "\u2728" in raw),
        ("“New” pill in the nav", bool(re.search(r"pill--new|New:\s", markup))),
        ("“No credit card required”", "no credit card" in copy or "без карты" in copy),
        ("SOC 2 badge", "soc 2" in copy),
        ("AI assistant bubble", "ai-bubble" in markup),
        ("noise / grain overlay", "grain" in raw or "feTurbulence" in raw),
        ("saturate(140%) on glass", "saturate(140%" in css or "saturate(150%" in css or "saturate(160%" in css),
        ("three floating blobs", len(re.findall(r"slop-blob--[abc]", markup)) >= 3),
        ("“Most Popular” badge", "most popular" in copy),
        ("tight display tracking", bool(re.search(r"letter-spacing\s*:\s*-\.?0?3?5?em|letter-spacing\s*:\s*-\.03", css))),
    ]
    rep.bonuses = [name for name, ok in bonus_checks if ok]

    total = min(100, sum(v[0] for v in cats.values()))
    total = max(0, total - pen)
    rep.score = total
    rep.grade, rep.band = grade_for(total)
    rep.categories = {k: {"points": v[0], "max": v[1]} for k, v in cats.items()}
    rep.penalties = pen
    rep.tells = list(dict.fromkeys(rep.tells))
    rep.missing = list(dict.fromkeys(rep.missing))
    return rep


# --------------------------------------------------------------------------- #
#  Rendering
# --------------------------------------------------------------------------- #

def render(rep: Report, label: str = "combined", width: int = 60) -> str:
    line = "─" * width
    out = []
    out.append("")
    out.append(f"  AI-SLOP PRO-MAX · slop-lint v{VERSION}")
    out.append("  " + line)
    out.append(f"  {label}")
    out.append("")
    pct = rep.score
    out.append(f"  {rep.score:>3}/100   {rep.grade:<3} {rep.band}")
    out.append("  " + bar(pct, 100, 48) + f"  {pct}%")
    out.append("")
    for name, d in rep.categories.items():
        out.append(
            f"  {name:<11}{d['points']:>3}/{d['max']:<3} {bar(d['points'], d['max'], 20)}"
        )
    if rep.penalties:
        out.append(f"  {'Penalties':<11}{-rep.penalties:>3}    " + ", ".join(rep.penalty_notes))
    if rep.bonuses:
        out.append("")
        out.append(f"  Bonus tells ({len(rep.bonuses)}): " + " · ".join(rep.bonuses))
    if rep.tells:
        out.append("")
        out.append("  Detected")
        for t in rep.tells:
            out.append(f"    ✓ {t}")
    if rep.missing:
        out.append("")
        out.append("  To gain points")
        for t in rep.missing:
            out.append(f"    + {t}")
    out.append("")
    out.append("  " + line)
    out.append("  " + verdict(rep))
    out.append("")
    return "\n".join(out)


def verdict(rep: Report) -> str:
    if rep.score >= 95:
        return "Maximum slop achieved. Indistinguishable from the training set. ✨"
    if rep.score >= 85:
        return "Museum-grade slop. Ship it, then label it. ✨"
    if rep.score >= 70:
        return "A VC could not tell you apart from your competitor. Almost there."
    if rep.score >= 55:
        return "The category is now visible. Add the missing tells above."
    if rep.score >= 40:
        return "Competent, forgettable, not yet iconic. More gradient required."
    return "Honest design detected. Are you sure you wanted slop?"


# --------------------------------------------------------------------------- #
#  CLI
# --------------------------------------------------------------------------- #

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="slop_lint.py",
        description="Score UI files on the AI-SLOP PRO-MAX 100-point rubric.",
    )
    ap.add_argument("paths", nargs="+", help="files, globs or directories")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--verbose", "-v", action="store_true", help="per-file breakdown")
    ap.add_argument("--no-follow", action="store_true", help="do not read linked stylesheets")
    ap.add_argument("--min-score", type=int, default=None, help="exit 1 below this score")
    ap.add_argument("--quiet", "-q", action="store_true", help="only print the score")
    args = ap.parse_args(argv)

    files = expand_args(args.paths)
    files = [f for f in files if f.is_file()]
    if not files:
        print("slop-lint: no supported files found", file=sys.stderr)
        return 2

    per_file = []
    combined: list[Source] = []
    seen_paths = set()
    for f in files:
        srcs = collect_sources(f, follow=not args.no_follow)
        text = "\n\n".join(s.text for s in srcs)
        for s in srcs:
            if s.path not in seen_paths:
                seen_paths.add(s.path)
                combined.append(s)
        per_file.append((f, analyze(text, read_text(f))))

    combined_text = "\n\n".join(s.text for s in combined)
    combined_markup = "\n\n".join(read_text(f) for f in files)
    agg = analyze(combined_text, combined_markup)

    if args.json:
        payload = {
            "version": VERSION,
            "aggregate": serialize(agg),
            "files": [
                {"path": str(f), **serialize(r)} for f, r in per_file
            ],
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    elif args.quiet:
        print(agg.score)
    else:
        if len(per_file) > 1:
            print("")
            print("  AI-SLOP PRO-MAX · slop-lint v" + VERSION)
            print("  " + "─" * 60)
            for f, r in per_file:
                try:
                    rel = f.resolve().relative_to(Path.cwd())
                except ValueError:
                    rel = f
                print(f"  {r.score:>3}/100  {r.grade:<3} {str(rel)[:44]:<44}")
            print("")
        print(render(agg, "combined" if len(per_file) > 1 else str(files[0])))

    if args.min_score is not None and agg.score < args.min_score:
        if not args.json and not args.quiet:
            print(f"  ✗ score {agg.score} is below the required {args.min_score}", file=sys.stderr)
        return 1
    return 0


def serialize(rep: Report) -> dict:
    return {
        "score": rep.score,
        "grade": rep.grade,
        "band": rep.band,
        "categories": rep.categories,
        "penalties": rep.penalties,
        "penalty_notes": rep.penalty_notes,
        "bonuses": rep.bonuses,
        "tells": rep.tells,
        "missing": rep.missing,
    }


if __name__ == "__main__":
    sys.exit(main())

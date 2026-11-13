#!/usr/bin/env python3
"""AI-SLOP UI/UX PRO-MAX Design System Generator & Persistence Engine."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, List, Optional

from core import bm25_search, load_domain


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "nexus-slop-ai"


def clamp(val: int, low: int, high: int) -> int:
    return max(low, min(high, val))


def _find_by_id(rows: List[Dict[str, str]], target_id: str) -> Optional[Dict[str, str]]:
    for r in rows:
        if r.get("id") == target_id:
            return r
    return None


def describe_slop_tier(level: int) -> Dict[str, Any]:
    level = clamp(level, 1, 11)
    if level <= 3:
        return {
            "level": level,
            "tier_name": "SUBTLE VIBE-CODED MVP",
            "orb_count": 1,
            "announcement_bars": 1,
            "chat_widgets": 0,
            "confetti": False,
            "sections_count": 6,
            "directive": "Keep a thin veneer of plausibility: 1 blurred purple orb, Inter font, 3-col feature cards, and 'Start Free →' buttons.",
        }
    if level <= 7:
        return {
            "level": level,
            "tier_name": "CERTIFIED PRODUCT HUNT #1 LAUNCH 🚀",
            "orb_count": 3,
            "announcement_bars": 1,
            "chat_widgets": 1,
            "confetti": False,
            "sections_count": 9,
            "directive": "Full YC/v0 SaaS energy: 3 floating blur-3xl orbs, pulsing beta pill, gradient noun in H1, 6-card Sparkles feature grid, $0/$29/Custom pricing with 'Save 20% 🔥', Sarah Chen testimonial, and floating '✨ Ask AI' widget.",
        }
    if level <= 10:
        return {
            "level": level,
            "tier_name": "MAXIMUM PURPLE GLASSMORPHISM FEVER DREAM ✨",
            "orb_count": 4,
            "announcement_bars": 1,
            "chat_widgets": 1,
            "confetti": True,
            "sections_count": 12,
            "directive": "Zero human restraint: frosted glass inside frosted glass, conic spinning borders, animated gradient shimmer text, fake live ROI calculator, fake ⌘K bar, cookie popup, and confetti on pricing toggle.",
        }
    return {
        "level": 11,
        "tier_name": "👑 OMEGA LEVEL-11 SINGULARITY SLOP OVERDRIVE 👑",
        "orb_count": 6,
        "announcement_bars": 2,
        "chat_widgets": 2,
        "confetti": True,
        "sections_count": 14,
        "directive": "TRANSCENDENT PARODY MODE: Stack TWO announcement ribbons at the top, 6 drifting rainbow-purple blur-3xl nebulae, wrap 2+ words per heading in animated gradient text, put emojis on EVERY button & nav link, render BOTH a bottom-right '✨ Ask AI Copilot' AND a bottom-left '🔥 Live: Sarah from Acme just upgraded to Pro!' toast, and add $0/$29/$99 AI subscription pricing even if it's a personal resume or bakery.",
    }


def build_design_system(
    query: str,
    project_name: str = "NexusFlow AI",
    slop_level: int = 9,
    era: str = "auto",
    buzzwords_dial: int = 9,
    emoji_density: int = 8,
) -> Dict[str, Any]:
    slop_level = clamp(slop_level, 1, 11)
    buzzwords_dial = clamp(buzzwords_dial, 1, 10)
    emoji_density = clamp(emoji_density, 1, 10)

    styles = load_domain("style")
    palettes = load_domain("palette")
    typographies = load_domain("typography")
    buzzwords = load_domain("buzzwords")
    components = load_domain("components")
    personas = load_domain("personas")
    icons = load_domain("icons")
    motions = load_domain("motion")
    reasonings = load_domain("reasoning")

    # 1. Match reasoning profile
    r_matches = bm25_search(reasonings, query, top_n=1)
    reasoning = r_matches[0] if r_matches else reasonings[0]

    # 2. Resolve Style, Palette, Typography
    if slop_level == 11 and era == "auto":
        style = _find_by_id(styles, "S25") or styles[0]
        palette = _find_by_id(palettes, "P20") or palettes[0]
        typo = _find_by_id(typographies, "T08") or typographies[0]
    elif era != "auto":
        s_matches = bm25_search(styles, query, top_n=1, era_filter=era)
        p_matches = bm25_search(palettes, query, top_n=1, era_filter=era)
        t_matches = bm25_search(typographies, query, top_n=1, era_filter=era)
        style = s_matches[0] if s_matches else next((s for s in styles if s["era"] == era), styles[0])
        palette = p_matches[0] if p_matches else next((p for p in palettes if p["era"] == era), palettes[0])
        typo = t_matches[0] if t_matches else next((t for t in typographies if t["era"] == era), typographies[0])
    else:
        s_matches = bm25_search(styles, query, top_n=1)
        p_matches = bm25_search(palettes, query, top_n=1)
        t_matches = bm25_search(typographies, query, top_n=1)
        style = (
            _find_by_id(styles, reasoning["recommended_style"])
            or (s_matches[0] if s_matches else styles[0])
        )
        palette = (
            _find_by_id(palettes, reasoning["recommended_palette"])
            or (p_matches[0] if p_matches else palettes[0])
        )
        typo = (
            _find_by_id(typographies, reasoning["recommended_typography"])
            or (t_matches[0] if t_matches else typographies[0])
        )

    tier = describe_slop_tier(slop_level)

    # 3. Pick copy formulas
    eyebrows = [b for b in buzzwords if b["category"] == "eyebrow_pill"]
    headlines = [b for b in buzzwords if b["category"] == "hero_headline"]
    subheadlines = [b for b in buzzwords if b["category"] == "hero_subheadline"]
    ctas = [b for b in buzzwords if b["category"] == "cta_primary"]
    micros = [b for b in buzzwords if b["category"] == "cta_microcopy"]

    matched_personas = bm25_search(personas, query, top_n=3)
    if len(matched_personas) < 3:
        for p in personas:
            if p["id"] not in {m["id"] for m in matched_personas}:
                matched_personas.append(p)
            if len(matched_personas) == 3:
                break

    mandatory_components = components[: min(len(components), tier["sections_count"] + 2)]

    emoji_policy = (
        "FULL EMOJI EXPLOSION (🚀 ✨ ⚡ 🧠 🔒 🔥 📈 🤖 on every badge, card icon, pricing toggle, and CTA)"
        if emoji_density >= 8
        else "LUCIDE SACRED SIX + SELECTIVE ✨ (<Sparkles />, <Zap />, <Rocket />, <Brain />, <ShieldCheck />, <TrendingUp /> inside tinted rounded-xl boxes)"
        if emoji_density >= 4
        else "SUBTLE NEO-SLOP CHROME (Tracked ALL-CAPS eyebrows, middle dots '·', em-dashes '—', and trailing '→' arrows)"
    )

    buzzword_policy = (
        "MAXIMUM LLM SYNERGY: Use 'Supercharge', 'Unleash', 'Seamlessly', 'Orchestrate', 'Next-Gen', '10x', em-dashes ('—') in every paragraph, and 'It's not just X — it's Y' at least twice."
        if buzzwords_dial >= 8
        else "STANDARD YC LAUNCH COPY: Promise 'minutes, not months', 'built for modern teams', and 'no credit card required · 14-day free trial'."
        if buzzwords_dial >= 4
        else "FAUX-PROFOUND MANIFESTO: Short pretentious sentences about 'craft', 'velocity', and 'autonomous intelligence'."
    )

    return {
        "project_name": project_name,
        "query": query,
        "tier": tier,
        "dials": {
            "slop_level": slop_level,
            "era": style["era"],
            "buzzwords": buzzwords_dial,
            "emoji_density": emoji_density,
        },
        "reasoning": reasoning,
        "style": style,
        "palette": palette,
        "typography": typo,
        "emoji_policy": emoji_policy,
        "buzzword_policy": buzzword_policy,
        "copy_pack": {
            "eyebrow": eyebrows[0]["example"].replace("NexusFlow", project_name),
            "headline": (
                headlines[4]["example"]
                if style["era"] == "2026-editorial"
                else headlines[0]["example"]
            ),
            "subheadline": subheadlines[0]["example"],
            "cta_primary": ctas[0]["example"],
            "cta_secondary": "▶ Watch 2-Min Demo",
            "microcopy": micros[0]["example"],
        },
        "personas": matched_personas,
        "icons": icons[:6],
        "motions": motions[:5],
        "components": mandatory_components,
    }


def format_design_system_markdown(ds: Dict[str, Any]) -> str:
    p = ds["palette"]
    s = ds["style"]
    t = ds["typography"]
    r = ds["reasoning"]
    tier = ds["tier"]
    dials = ds["dials"]
    cp = ds["copy_pack"]

    personas_md = "\n".join(
        f'- **{u["persona_name"]}**, *{u["role"]} @ {u["company"]}* (`{u["metric_badge"]}`): "{u["quote"]}"'
        for u in ds["personas"]
    )
    icons_md = "\n".join(
        f'- `{ic["emoji"]}` / `<{ic["lucide_icon"]} />` — **{ic["concept"]}** (`{ic["container_tailwind"]}`)'
        for ic in ds["icons"]
    )
    comps_md = "\n".join(
        f'{idx + 1}. **{c["name"]}** (`{c["section"]}`) — `{c["tailwind_recipe"]}`'
        for idx, c in enumerate(ds["components"][:10])
    )
    motions_md = "\n".join(
        f'- **{m["name"]}** (`{m["duration_easing"]}`): `{m["tailwind_or_css"]}`'
        for m in ds["motions"]
    )

    return f"""# ✨ AI-SLOP UI/UX PRO-MAX — MASTER DESIGN SYSTEM: {ds["project_name"]}

> **Slop Tier**: `{tier["tier_name"]}` (Level **{dials["slop_level"]}/11**)
> **Era**: `{dials["era"]}` | **Buzzword Dial**: `{dials["buzzwords"]}/10` | **Emoji Density**: `{dials["emoji_density"]}/10`
> **Matched Archetype**: {r["product_category"]} (`{r["id"]}`)

---

## 1. Prime Directive (Anti-Restraint Mandate)

{tier["directive"]}

- **Signature Aesthetic**: **{s["name"]}** (`{s["id"]}`) — *{s["vibe"]}*
- **Signature Tell (MUST INCLUDE)**: {s["signature_tell"]}
- **Forbidden Human Trait (NEVER DO THIS)**: {s["forbidden_human_trait"]}
- **Mandatory Product Gimmick**: {r["mandatory_gimmick"]}
- **Required Vanity Stat Triad**: `{r["fake_stat_triad"]}`

---

## 2. Color Palette & Nebula Physics (`{p["name"]}`)

```css
:root {{
  --slop-bg: {p["bg_hex"]};
  --slop-surface: {p["surface_hex"]};
  --slop-primary: {p["primary_hex"]};
  --slop-secondary: {p["secondary_hex"]};
  --slop-accent: {p["accent_hex"]};
  --slop-text: {p["text_hex"]};
  --slop-muted: {p["muted_hex"]};
  --slop-gradient: {p["gradient_css"]};
}}
```

- **Tailwind Gradient Utility**: `bg-gradient-to-r {p["tailwind_gradient"]}`
- **Gradient Text Span**: `bg-gradient-to-r {p["tailwind_gradient"]} bg-clip-text text-transparent`
- **Floating Radial Orbs (`{tier["orb_count"]}` required)**: `{p["orb_recipe"]}`
- **Glass Card Recipe**: `{s["card_recipe"]} {s["border_radius"]}`
- **Glow Shadow**: `{s["shadow_recipe"]}`

---

## 3. Typography Monoculture (`{t["name"]}`)

- **Heading Font**: `{t["heading_font"]}` | **Body Font**: `{t["body_font"]}` | **Mono Font**: `{t["mono_font"]}`
- **Google Fonts Import**:
  ```html
  <link rel="stylesheet" href="{t["google_fonts_url"]}" />
  ```
- **Hero Heading Classes**: `{t["hero_classes"]}`
- **Eyebrow Label Rule**: {t["eyebrow_rule"]}
- **Mandatory Headline Gimmick**: {t["headline_gimmick"]}

---

## 4. Instant Buzzword Copy Pack

- **Policy**: {ds["buzzword_policy"]}
- **Eyebrow Pill**: `{cp["eyebrow"]}`
- **Hero H1**: `{cp["headline"]}`
- **Hero Subheadline**: `{cp["subheadline"]}`
- **Primary CTA**: `{cp["cta_primary"]}`
- **Secondary CTA**: `{cp["cta_secondary"]}`
- **Trust Microcopy**: `{cp["microcopy"]}`
- **Fictional Logo Bar**: `Acme Corp · QuantumAI · NexusCloud · HyperScale · Synthetix · VortexMetrics`

---

## 5. Sacred Iconography & Emoji Rules

- **Policy**: {ds["emoji_policy"]}
{icons_md}

---

## 6. Mandatory Page Sections & Slop Components

{comps_md}

- **Announcement Bars at Top**: `{tier["announcement_bars"]}`
- **Unsolicited Floating AI Chat Widgets**: `{tier["chat_widgets"]}`
- **Confetti on Toggle/CTA Click**: `{"ENABLED 🎉" if tier["confetti"] else "Optional"}`

---

## 7. Certified Fake Testimonials (Drop Straight Into Wall-of-Love)

{personas_md}

---

## 8. Gratuitous Motion Choreography

{motions_md}
"""


def persist_design_system(
    ds: Dict[str, Any],
    output_dir: Path,
    page: Optional[str] = None,
    force: bool = False,
) -> Dict[str, Any]:
    slug = slugify(ds["project_name"])
    base_dir = output_dir.resolve() / "slop-system" / slug
    pages_dir = base_dir / "pages"
    base_dir.mkdir(parents=True, exist_ok=True)
    pages_dir.mkdir(parents=True, exist_ok=True)

    master_path = base_dir / "MASTER-SLOP.md"
    written_files: List[str] = []
    skipped_files: List[str] = []

    if master_path.exists() and not force:
        skipped_files.append(str(master_path))
    else:
        master_path.write_text(format_design_system_markdown(ds), encoding="utf-8")
        written_files.append(str(master_path))

    if page:
        page_slug = slugify(page)
        page_path = pages_dir / f"{page_slug}.md"
        if page_path.exists() and not force:
            skipped_files.append(str(page_path))
        else:
            page_content = f"""# ✨ Page-Specific Slop Override: `{page}` ({ds["project_name"]})

Inherits all rules from `../MASTER-SLOP.md` with the following extra slop injections for **{page}**:

1. Add a sticky top banner: `🎉 New in {ds["project_name"]} {page.title()}: Autonomous AI Co-Pilot is now LIVE →`
2. Ensure at least **{ds["tier"]["orb_count"]}** floating `blur-3xl` radial orbs behind the `{page}` container.
3. Add a `✨ Generate AI Insights` glowing purple button in the top-right header of `{page}`.
4. Append `→` to every interactive button and link on `{page}`.
"""
            page_path.write_text(page_content, encoding="utf-8")
            written_files.append(str(page_path))

    return {
        "master_path": str(master_path),
        "written": written_files,
        "skipped": skipped_files,
    }

#!/usr/bin/env python3
"""Multi-format Slop Design Token Exporter (CSS, Tailwind, Shadcn HSL, W3C JSON)."""

from __future__ import annotations

import colorsys
import json
from typing import Any, Dict


def hex_to_hsl_triplet(hex_str: str) -> str:
    clean = hex_str.strip().lstrip("#")
    if len(clean) != 6 or not all(c in "0123456789abcdefABCDEF" for c in clean):
        return "240 10% 3.9%"
    r = int(clean[0:2], 16) / 255.0
    g = int(clean[2:4], 16) / 255.0
    b = int(clean[4:6], 16) / 255.0
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return f"{round(h * 360)} {round(s * 100, 1)}% {round(l * 100, 1)}%"


def export_css_tokens(ds: Dict[str, Any]) -> str:
    p = ds["palette"]
    t = ds["typography"]
    s = ds["style"]
    return f"""/* AI-SLOP UI/UX PRO-MAX — Generated CSS Tokens for {ds["project_name"]} */
/* Style: {s["name"]} ({s["era"]}) | Palette: {p["name"]} */

:root {{
  --slop-bg: {p["bg_hex"]};
  --slop-surface: {p["surface_hex"]};
  --slop-border: {p.get("border_hex", "rgba(255,255,255,0.10)")};
  --slop-primary: {p["primary_hex"]};
  --slop-secondary: {p["secondary_hex"]};
  --slop-accent: {p["accent_hex"]};
  --slop-text: {p["text_hex"]};
  --slop-muted: {p["muted_hex"]};
  --slop-gradient: {p["gradient_css"]};
  --slop-font-heading: '{t["heading_font"]}', system-ui, sans-serif;
  --slop-font-body: '{t["body_font"]}', system-ui, sans-serif;
  --slop-font-mono: '{t["mono_font"]}', monospace;
  --slop-radius-card: 1rem;
  --slop-radius-pill: 9999px;
}}

@keyframes slopBlob {{
  0%, 100% {{ transform: translate(0, 0) scale(1); }}
  50% {{ transform: translate(28px, -24px) scale(1.12); }}
}}

@keyframes slopShimmer {{
  0% {{ background-position: 0% 50%; }}
  100% {{ background-position: 200% 50%; }}
}}

@keyframes slopMarquee {{
  0% {{ transform: translateX(0%); }}
  100% {{ transform: translateX(-50%); }}
}}

.slop-canvas {{
  background-color: var(--slop-bg);
  color: var(--slop-text);
  font-family: var(--slop-font-body);
}}

.slop-glass-card {{
  background: rgba(255, 255, 255, 0.04);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border: 1px solid var(--slop-border);
  border-radius: var(--slop-radius-card);
  transition: all 300ms cubic-bezier(0.4, 0, 0.2, 1);
}}

.slop-glass-card:hover {{
  transform: translateY(-6px) scale(1.01);
  border-color: var(--slop-primary);
  box-shadow: 0 20px 40px -15px rgba(168, 85, 247, 0.35);
}}

.slop-gradient-text {{
  background-image: var(--slop-gradient);
  background-size: 200% auto;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: slopShimmer 4s linear infinite;
}}

.slop-glow-btn {{
  background-image: var(--slop-gradient);
  color: #ffffff;
  border-radius: var(--slop-radius-pill);
  font-weight: 700;
  box-shadow: 0 12px 30px -8px rgba(168, 85, 247, 0.5);
  transition: transform 200ms ease, box-shadow 200ms ease;
}}

.slop-glow-btn:hover {{
  transform: translateY(-2px) scale(1.03);
}}
"""


def export_tailwind_config(ds: Dict[str, Any]) -> str:
    p = ds["palette"]
    t = ds["typography"]
    return f"""// AI-SLOP UI/UX PRO-MAX — tailwind.config.js snippet for {ds["project_name"]}
export default {{
  darkMode: "class",
  theme: {{
    extend: {{
      colors: {{
        slop: {{
          bg: "{p["bg_hex"]}",
          surface: "{p["surface_hex"]}",
          primary: "{p["primary_hex"]}",
          secondary: "{p["secondary_hex"]}",
          accent: "{p["accent_hex"]}",
          text: "{p["text_hex"]}",
          muted: "{p["muted_hex"]}",
        }},
      }},
      fontFamily: {{
        heading: ["{t["heading_font"]}", "sans-serif"],
        sans: ["{t["body_font"]}", "sans-serif"],
        mono: ["{t["mono_font"]}", "monospace"],
      }},
      backgroundImage: {{
        "slop-gradient": "{p["gradient_css"]}",
      }},
      animation: {{
        "slop-blob": "slopBlob 8s ease-in-out infinite",
        "slop-marquee": "slopMarquee 22s linear infinite",
      }},
    }},
  }},
}};
"""


def export_shadcn_globals(ds: Dict[str, Any]) -> str:
    p = ds["palette"]
    return f"""/* AI-SLOP UI/UX PRO-MAX — shadcn/ui globals.css tokens for {ds["project_name"]} */
@layer base {{
  :root {{
    --background: {hex_to_hsl_triplet(p["bg_hex"])};
    --foreground: {hex_to_hsl_triplet(p["text_hex"])};
    --card: {hex_to_hsl_triplet(p["surface_hex"])};
    --card-foreground: {hex_to_hsl_triplet(p["text_hex"])};
    --primary: {hex_to_hsl_triplet(p["primary_hex"])};
    --primary-foreground: 0 0% 100%;
    --secondary: {hex_to_hsl_triplet(p["secondary_hex"])};
    --secondary-foreground: 0 0% 100%;
    --accent: {hex_to_hsl_triplet(p["accent_hex"])};
    --accent-foreground: 0 0% 100%;
    --muted: {hex_to_hsl_triplet(p["surface_hex"])};
    --muted-foreground: {hex_to_hsl_triplet(p["muted_hex"])};
    --radius: 1rem;
  }}
}}
"""


def export_w3c_tokens(ds: Dict[str, Any]) -> str:
    p = ds["palette"]
    t = ds["typography"]
    payload = {
        "$description": f"AI-SLOP UI/UX PRO-MAX Design Tokens for {ds['project_name']}",
        "color": {
            "background": {"$value": p["bg_hex"], "$type": "color"},
            "surface": {"$value": p["surface_hex"], "$type": "color"},
            "primary": {"$value": p["primary_hex"], "$type": "color"},
            "secondary": {"$value": p["secondary_hex"], "$type": "color"},
            "accent": {"$value": p["accent_hex"], "$type": "color"},
            "text": {"$value": p["text_hex"], "$type": "color"},
            "muted": {"$value": p["muted_hex"], "$type": "color"},
        },
        "fontFamily": {
            "heading": {"$value": t["heading_font"], "$type": "fontFamily"},
            "body": {"$value": t["body_font"], "$type": "fontFamily"},
            "mono": {"$value": t["mono_font"], "$type": "fontFamily"},
        },
        "gradient": {
            "hero": {"$value": p["gradient_css"], "$type": "string"},
        },
    }
    return json.dumps(payload, indent=2)


def export_tokens(ds: Dict[str, Any], fmt: str) -> str:
    key = fmt.strip().lower()
    if key == "css":
        return export_css_tokens(ds)
    if key == "tailwind":
        return export_tailwind_config(ds)
    if key == "shadcn":
        return export_shadcn_globals(ds)
    if key in {"w3c", "json"}:
        return export_w3c_tokens(ds)
    raise ValueError(f"Unsupported token format '{fmt}'. Choose: css, tailwind, shadcn, w3c")

#!/usr/bin/env python3
"""Main CLI for AI-SLOP UI/UX PRO-MAX v2.0 Design Intelligence Engine."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from auditor import audit_path, format_audit_report  # noqa: E402
from core import (  # noqa: E402
    AVAILABLE_ERAS,
    AVAILABLE_STACKS,
    CANONICAL_DOMAINS,
    bm25_search,
    catalog_stats,
    load_domain,
    load_stack,
)
from design_system import (  # noqa: E402
    build_design_system,
    format_design_system_markdown,
    persist_design_system,
)
from generator import SCAFFOLD_TEMPLATES, generate_scaffold  # noqa: E402
from tokens import export_tokens  # noqa: E402


def format_rows_markdown(title: str, rows: List[Dict[str, str]]) -> str:
    if not rows:
        return (
            f"## {title}\n\n"
            "No exact keyword hit — default to Classic v0 Indigo-Purple Nebula "
            "(`#6366F1 -> #A855F7 -> #EC4899`) + `Inter` + `✨`!"
        )
    out = [f"# ✨ {title} ({len(rows)} matches)", ""]
    for idx, row in enumerate(rows, 1):
        head = (
            row.get("name")
            or row.get("topic")
            or row.get("persona_name")
            or row.get("concept")
            or row.get("product_category")
            or row.get("category")
            or row.get("id", f"Row {idx}")
        )
        score = row.get("_score", "")
        score_str = f" *(BM25: {score})*" if score else ""
        out.append(f"### {idx}. [{row.get('id', '')}] {head}{score_str}")
        for k, v in row.items():
            if k in {"id", "_score"} or not v:
                continue
            out.append(f"- **{k}**: {v}")
        out.append("")
    return "\n".join(out)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="slop.py",
        description="✨ AI-SLOP UI/UX PRO-MAX v2.0 — Deliberate Cliché AI UI/UX Intelligence Engine",
    )
    parser.add_argument(
        "query",
        nargs="?",
        default="",
        help="Search query or product concept (e.g. 'ai analytics saas dashboard')",
    )
    parser.add_argument(
        "--design-system",
        "-ds",
        action="store_true",
        help="Compile a complete AI-Slop Design System Blueprint",
    )
    parser.add_argument(
        "--domain",
        "-d",
        type=str,
        help=f"Search a specific slop domain ({', '.join(CANONICAL_DOMAINS)})",
    )
    parser.add_argument(
        "--stack",
        "-s",
        type=str,
        help=f"Search stack-specific slop guidelines ({', '.join(AVAILABLE_STACKS)})",
    )
    parser.add_argument(
        "--export-tokens",
        type=str,
        choices=["css", "tailwind", "shadcn", "w3c"],
        help="Export Slop Design Tokens in css, tailwind, shadcn, or w3c JSON format",
    )
    parser.add_argument(
        "--scaffold",
        type=str,
        choices=SCAFFOLD_TEMPLATES,
        help=f"Generate a ready-to-run Grade S+ Slop UI ({', '.join(SCAFFOLD_TEMPLATES)})",
    )
    parser.add_argument(
        "--format",
        type=str,
        default="html",
        choices=["html", "tsx"],
        help="Output format for --scaffold (html or tsx; default: html)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="Write output of --scaffold or --export-tokens to file path",
    )
    parser.add_argument(
        "--audit",
        type=str,
        metavar="PATH",
        help="Audit a file or directory and compute its Official Slop Score™ (0-100)",
    )
    parser.add_argument(
        "--min-score",
        type=int,
        default=0,
        help="Exit non-zero if --audit score falls below this threshold (for CI)",
    )
    parser.add_argument(
        "--copy",
        action="store_true",
        help="Generate an instant SaaS buzzword hero + testimonials copy pack",
    )
    parser.add_argument(
        "-p",
        "--project",
        type=str,
        default="NexusFlow AI",
        help="Project/Startup name (default: 'NexusFlow AI')",
    )
    parser.add_argument(
        "--slop-level",
        type=int,
        default=9,
        help="Slop intensity dial 1-11 (11 = Omega Singularity Slop Overdrive! Default: 9)",
    )
    parser.add_argument(
        "--era",
        type=str,
        default="auto",
        choices=AVAILABLE_ERAS,
        help="Lock aesthetic to a specific AI Slop Era (default: auto)",
    )
    parser.add_argument(
        "--buzzwords",
        type=int,
        default=9,
        help="SaaS buzzword & em-dash density dial 1-10 (default: 9)",
    )
    parser.add_argument(
        "--emoji-density",
        type=int,
        default=8,
        help="Emoji & Sparkles icon density dial 1-10 (default: 8)",
    )
    parser.add_argument(
        "--motion-nausea",
        type=int,
        default=8,
        help="Gratuitous hover/blob/beam/confetti animation dial 1-10 (default: 8)",
    )
    parser.add_argument(
        "--persist",
        action="store_true",
        help="Persist MASTER-SLOP.md + slop-tokens.css to <output-dir>/slop-system/<slug>/",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=".",
        help="Project root for --persist (default: current directory)",
    )
    parser.add_argument(
        "--page",
        type=str,
        default=None,
        help="Optional page override slug when using --persist (e.g. 'pricing')",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing persisted files",
    )
    parser.add_argument(
        "-n",
        "--max-results",
        type=int,
        default=5,
        help="Max search rows to return (default: 5)",
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show local Slop Intelligence database row counts",
    )
    parser.add_argument(
        "--list-domains",
        action="store_true",
        help="List all searchable slop domains, eras, and stacks",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON output",
    )
    return parser


def main(argv: List[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.stats:
        st = catalog_stats()
        if args.json:
            print(json.dumps(st, indent=2))
        else:
            print("# ✨ AI-SLOP UI/UX PRO-MAX v2.0 — Catalog Statistics\n")
            for k, v in st["domains"].items():
                print(f"- **Domain `{k}`**: {v} rows")
            print(f"- **Stacks (`{len(st['stacks'])}`)**: {st['total_stack_rows']} rows")
            print(f"\n**Grand Total Searchable Records**: **{st['grand_total_rows']}**")
        return 0

    if args.list_domains:
        info = {
            "domains": CANONICAL_DOMAINS,
            "eras": AVAILABLE_ERAS,
            "stacks": AVAILABLE_STACKS,
            "scaffolds": SCAFFOLD_TEMPLATES,
        }
        if args.json:
            print(json.dumps(info, indent=2))
        else:
            print("✨ Searchable Domains:  ", ", ".join(CANONICAL_DOMAINS))
            print("🕰️  Supported Slop Eras: ", ", ".join(AVAILABLE_ERAS))
            print("🚀 Supported Stacks:    ", ", ".join(AVAILABLE_STACKS))
            print("🏗️  Scaffold Templates:  ", ", ".join(SCAFFOLD_TEMPLATES))
        return 0

    if args.audit:
        report = audit_path(args.audit)
        if args.json:
            print(json.dumps(report, indent=2, ensure_ascii=False))
        else:
            print(format_audit_report(report))
        if args.min_score and report["slop_score"] < args.min_score:
            return 2
        return 0

    if args.export_tokens:
        ds = build_design_system(
            query=args.query or "ai saas workflow platform",
            project_name=args.project,
            slop_level=args.slop_level,
            era=args.era,
            buzzwords_dial=args.buzzwords,
            emoji_density=args.emoji_density,
            motion_nausea=args.motion_nausea,
        )
        rendered = export_tokens(ds, args.export_tokens)
        if args.output:
            out_path = Path(args.output)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(rendered, encoding="utf-8")
            print(f"💾 Wrote {args.export_tokens} tokens to {out_path}")
        else:
            print(rendered)
        return 0

    if args.scaffold:
        ds = build_design_system(
            query=args.query or f"{args.scaffold} ai saas platform",
            project_name=args.project,
            slop_level=args.slop_level,
            era=args.era,
            buzzwords_dial=args.buzzwords,
            emoji_density=args.emoji_density,
            motion_nausea=args.motion_nausea,
        )
        code = generate_scaffold(ds, args.scaffold, fmt=args.format)
        if args.output:
            out_path = Path(args.output)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(code, encoding="utf-8")
            print(f"🚀 Scaffolded {args.scaffold} ({args.format}) to {out_path}")
        else:
            print(code)
        return 0

    if args.copy:
        ds = build_design_system(
            query=args.query or "ai saas workflow platform",
            project_name=args.project,
            slop_level=args.slop_level,
            era=args.era,
            buzzwords_dial=args.buzzwords,
            emoji_density=args.emoji_density,
            motion_nausea=args.motion_nausea,
        )
        payload = {
            "project": ds["project_name"],
            "copy_pack": ds["copy_pack"],
            "buzzword_policy": ds["buzzword_policy"],
            "personas": ds["personas"],
        }
        if args.json:
            print(json.dumps(payload, indent=2, ensure_ascii=False))
        else:
            cp = ds["copy_pack"]
            print(f"# ✨ Instant AI-Slop Copy Pack for {ds['project_name']}\n")
            print(f"- **Eyebrow Pill**: `{cp['eyebrow']}`")
            print(f"- **Hero H1**: `{cp['headline']}`")
            print(f"- **Subheadline**: {cp['subheadline']}")
            print(f"- **Primary CTA**: `{cp['cta_primary']}`")
            print(f"- **Secondary CTA**: `{cp['cta_secondary']}`")
            print(f"- **Microcopy**: `{cp['microcopy']}`\n")
            print("## Fake Wall-of-Love Quotes")
            for u in ds["personas"]:
                print(
                    f'- **{u["persona_name"]}** ({u["role"]} @ {u["company"]} · `{u["metric_badge"]}`): "{u["quote"]}"'
                )
        return 0

    if args.design_system or (not args.domain and not args.stack and args.query):
        ds = build_design_system(
            query=args.query or "ai saas startup landing page",
            project_name=args.project,
            slop_level=args.slop_level,
            era=args.era,
            buzzwords_dial=args.buzzwords,
            emoji_density=args.emoji_density,
            motion_nausea=args.motion_nausea,
        )
        persist_info = None
        if args.persist:
            persist_info = persist_design_system(
                ds,
                output_dir=Path(args.output_dir),
                page=args.page,
                force=args.force,
            )
            ds["persisted"] = persist_info

        if args.json:
            print(json.dumps(ds, indent=2, ensure_ascii=False))
        else:
            print(format_design_system_markdown(ds))
            if persist_info:
                print("\n---")
                if persist_info["written"]:
                    print("💾 Persisted Slop System artifacts:")
                    for p in persist_info["written"]:
                        print(f"  - {p}")
                if persist_info["skipped"]:
                    print("⏭️  Skipped existing files (pass --force to overwrite):")
                    for p in persist_info["skipped"]:
                        print(f"  - {p}")
        return 0

    if args.stack:
        rows = load_stack(args.stack)
        results = bm25_search(rows, args.query, top_n=args.max_results)
        if not results:
            results = rows[: args.max_results]
        if args.json:
            print(json.dumps(results, indent=2, ensure_ascii=False))
        else:
            print(format_rows_markdown(f"Stack Slop Rules: {args.stack}", results))
        return 0

    if args.domain:
        rows = load_domain(args.domain)
        results = bm25_search(
            rows, args.query, top_n=args.max_results, era_filter=args.era
        )
        if not results:
            results = rows[: args.max_results]
        if args.json:
            print(json.dumps(results, indent=2, ensure_ascii=False))
        else:
            print(format_rows_markdown(f"Domain Slop Rules: {args.domain}", results))
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

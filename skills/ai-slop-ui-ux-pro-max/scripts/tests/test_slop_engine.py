#!/usr/bin/env python3
"""Comprehensive unit, integration, and repository-hygiene tests for AI-SLOP UI/UX PRO-MAX v2.0."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = TESTS_DIR.parent
SKILL_DIR = SCRIPTS_DIR.parent
REPO_ROOT = SKILL_DIR.parent.parent

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from auditor import audit_path  # noqa: E402
from core import (  # noqa: E402
    AVAILABLE_ERAS,
    AVAILABLE_STACKS,
    CANONICAL_DOMAINS,
    bm25_search,
    catalog_stats,
    load_domain,
    load_stack,
)
from design_system import build_design_system, persist_design_system  # noqa: E402
from generator import SCAFFOLD_TEMPLATES, generate_scaffold  # noqa: E402
from tokens import export_tokens  # noqa: E402


class TestSlopDatabasesV2(unittest.TestCase):
    def test_catalog_exceeds_250_records_with_unique_ids(self) -> None:
        stats = catalog_stats()
        self.assertGreaterEqual(stats["grand_total_rows"], 250)
        self.assertEqual(len(CANONICAL_DOMAINS), 11)
        self.assertEqual(len(AVAILABLE_STACKS), 12)

        for domain in CANONICAL_DOMAINS:
            rows = load_domain(domain)
            self.assertGreaterEqual(len(rows), 12, f"Domain {domain} too small")
            ids = [r["id"] for r in rows]
            self.assertEqual(len(ids), len(set(ids)), f"Duplicate IDs in {domain}")

    def test_synonym_bm25_relevance(self) -> None:
        editorial = bm25_search(load_domain("style"), "anthropic warm cream terracotta", top_n=3)
        self.assertEqual(editorial[0]["id"], "S06")

        charts = bm25_search(load_domain("charts"), "hockey stick spline revenue", top_n=3)
        self.assertEqual(charts[0]["id"], "CH01")

        bakery = bm25_search(load_domain("reasoning"), "sourdough bakery plumber", top_n=2)
        self.assertEqual(bakery[0]["id"], "R18")


class TestCompilerTokensAndScaffolder(unittest.TestCase):
    def test_all_7_eras_and_level_11_compile_cleanly(self) -> None:
        ds11 = build_design_system("ai workflow", project_name="OmegaAI", slop_level=11)
        self.assertEqual(ds11["style"]["id"], "S50")
        self.assertEqual(ds11["palette"]["id"], "P30")
        self.assertEqual(ds11["tier"]["orb_count"], 6)

        for era in AVAILABLE_ERAS:
            if era == "auto":
                continue
            ds = build_design_system("platform", era=era, slop_level=8)
            self.assertEqual(ds["style"]["era"], era)

    def test_token_exporters_all_formats(self) -> None:
        ds = build_design_system("fintech card", project_name="VaultAI")
        css_out = export_tokens(ds, "css")
        self.assertIn("--slop-primary:", css_out)
        tw_out = export_tokens(ds, "tailwind")
        self.assertIn("slop-gradient", tw_out)
        sh_out = export_tokens(ds, "shadcn")
        self.assertIn("--background:", sh_out)
        w3c_out = json.loads(export_tokens(ds, "w3c"))
        self.assertIn("color", w3c_out)

    def test_scaffolder_html_and_tsx_pass_high_slop_audit(self) -> None:
        ds = build_design_system("saas analytics", project_name="PulseFlow")
        with tempfile.TemporaryDirectory() as tmp:
            for tpl in SCAFFOLD_TEMPLATES:
                html_file = Path(tmp) / f"{tpl}.html"
                html_file.write_text(generate_scaffold(ds, tpl, fmt="html"), encoding="utf-8")
                rep = audit_path(str(html_file))
                self.assertGreaterEqual(rep["slop_score"], 75, f"HTML scaffold {tpl} scored too low: {rep['slop_score']}")

            tsx_file = Path(tmp) / "App.tsx"
            tsx_file.write_text(generate_scaffold(ds, "landing", fmt="tsx"), encoding="utf-8")
            tsx_rep = audit_path(str(tsx_file))
            self.assertGreaterEqual(tsx_rep["slop_score"], 85)

    def test_persist_writes_master_and_css_tokens(self) -> None:
        ds = build_design_system("devtools cli", project_name="VaporCLI")
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            res = persist_design_system(ds, output_dir=tmp_path, page="pricing", force=False)
            self.assertEqual(len(res["written"]), 3)
            self.assertTrue(Path(res["master_path"]).is_file())
            self.assertTrue(Path(res["tokens_path"]).is_file())


class TestAuditorAndShowcase(unittest.TestCase):
    def test_plain_human_html_scores_grade_f(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            plain = Path(tmp) / "plain.html"
            plain.write_text(
                "<!doctype html><html><body><h1>Corner Hardware</h1><p>Open 8am-5pm. Nails $4/lb.</p><button>Buy</button></body></html>",
                encoding="utf-8",
            )
            rep = audit_path(str(plain))
            self.assertLess(rep["slop_score"], 20)
            self.assertEqual(rep["grade"], "F")

    def test_showcase_scores_grade_s_plus_and_detects_era(self) -> None:
        showcase = REPO_ROOT / "examples" / "nexusflow-ai-showcase.html"
        rep = audit_path(str(showcase))
        self.assertGreaterEqual(rep["slop_score"], 95)
        self.assertEqual(rep["grade"], "S+")
        self.assertIn("2024-nebula", rep["detected_era"])


class TestSkillsManifestsInstallerAndEnglishOnly(unittest.TestCase):
    def test_all_5_skills_have_valid_frontmatter(self) -> None:
        skills_root = REPO_ROOT / "skills"
        skill_dirs = [d for d in sorted(skills_root.iterdir()) if d.is_dir()]
        self.assertEqual(len(skill_dirs), 5)

        seen = set()
        for sdir in skill_dirs:
            skill_md = sdir / "SKILL.md"
            self.assertTrue(skill_md.is_file(), f"Missing SKILL.md in {sdir}")
            content = skill_md.read_text(encoding="utf-8")
            self.assertTrue(content.startswith("---\n"))
            fm = content.split("---\n", 2)[1]
            name_val = next(ln for ln in fm.splitlines() if ln.startswith("name:")).split(":", 1)[1].strip().strip("\"'")
            desc_val = next(ln for ln in fm.splitlines() if ln.startswith("description:")).split(":", 1)[1].strip().strip("\"'")
            self.assertEqual(name_val, sdir.name)
            self.assertGreater(len(desc_val), 40)
            self.assertNotIn(name_val, seen)
            seen.add(name_val)

    def test_cli_installer_all_12_platforms_and_doctor(self) -> None:
        cli = REPO_ROOT / "bin" / "cli.mjs"
        doc = subprocess.run(["node", str(cli), "doctor"], capture_output=True, text=True, check=True)
        self.assertIn("Grand Total Searchable Records", doc.stdout)

        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(["node", str(cli), "init", "--ai", "all", "--dir", tmp], capture_output=True, text=True, check=True)
            tp = Path(tmp)
            self.assertTrue((tp / ".claude/skills/ai-slop-components/SKILL.md").is_file())
            self.assertTrue((tp / ".cursor/skills/ai-slop-pitch-deck/SKILL.md").is_file())
            self.assertTrue((tp / ".gemini/skills/ai-slop-ui-ux-pro-max/SKILL.md").is_file())
            self.assertTrue((tp / ".github/copilot-instructions.md").is_file())

    def test_repository_is_100_percent_english_no_cyrillic(self) -> None:
        cyrillic_re = re.compile(r"[\u0400-\u04FF]")
        skip_parts = {".git", "node_modules", "__pycache__"}
        offending = []
        for path in REPO_ROOT.rglob("*"):
            if any(p in skip_parts for p in path.parts) or not path.is_file():
                continue
            try:
                txt = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if cyrillic_re.search(txt):
                offending.append(str(path.relative_to(REPO_ROOT)))
        self.assertEqual(offending, [], f"Found non-English Cyrillic text in: {offending}")


if __name__ == "__main__":
    unittest.main()

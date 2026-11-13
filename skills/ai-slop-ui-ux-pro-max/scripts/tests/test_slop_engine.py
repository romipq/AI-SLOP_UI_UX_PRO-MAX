#!/usr/bin/env python3
"""Unit and contract tests for AI-SLOP UI/UX PRO-MAX."""

from __future__ import annotations

import json
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
    AVAILABLE_STACKS,
    CANONICAL_DOMAINS,
    bm25_search,
    load_domain,
    load_stack,
)
from design_system import build_design_system, persist_design_system  # noqa: E402


class TestSlopDatabases(unittest.TestCase):
    def test_all_domains_load_non_empty_with_unique_ids(self) -> None:
        for domain in CANONICAL_DOMAINS:
            rows = load_domain(domain)
            self.assertGreaterEqual(len(rows), 10, f"Domain {domain} has too few rows")
            ids = [r["id"] for r in rows]
            self.assertEqual(len(ids), len(set(ids)), f"Duplicate IDs in {domain}")

    def test_all_stacks_load_non_empty(self) -> None:
        for stack in AVAILABLE_STACKS:
            rows = load_stack(stack)
            self.assertGreaterEqual(len(rows), 2, f"Stack {stack} has too few rows")

    def test_bm25_relevance_across_domains(self) -> None:
        fintech_palettes = bm25_search(load_domain("palette"), "fintech emerald bank", top_n=3)
        self.assertTrue(any("Emerald" in r["name"] for r in fintech_palettes))

        editorial_styles = bm25_search(load_domain("style"), "editorial warm cream terracotta", top_n=3)
        self.assertEqual(editorial_styles[0]["id"], "S06")

        bakery_reasoning = bm25_search(load_domain("reasoning"), "sourdough bakery local plumber", top_n=2)
        self.assertEqual(bakery_reasoning[0]["id"], "R12")


class TestDesignSystemAndPersist(unittest.TestCase):
    def test_level_11_activates_omega_singularity(self) -> None:
        ds = build_design_system("ai workflow saas", project_name="HyperSlop", slop_level=11)
        self.assertEqual(ds["dials"]["slop_level"], 11)
        self.assertEqual(ds["style"]["id"], "S25")
        self.assertEqual(ds["palette"]["id"], "P20")
        self.assertEqual(ds["tier"]["orb_count"], 6)
        self.assertEqual(ds["tier"]["announcement_bars"], 2)

    def test_era_override_locks_to_2026_editorial(self) -> None:
        ds = build_design_system("saas platform", era="2026-editorial", slop_level=8)
        self.assertEqual(ds["style"]["era"], "2026-editorial")
        self.assertEqual(ds["palette"]["era"], "2026-editorial")

    def test_persist_respects_force_flag(self) -> None:
        ds = build_design_system("devtools cli", project_name="VaporCLI")
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            first = persist_design_system(ds, output_dir=tmp_path, page="pricing", force=False)
            self.assertEqual(len(first["written"]), 2)
            self.assertEqual(len(first["skipped"]), 0)

            second = persist_design_system(ds, output_dir=tmp_path, page="pricing", force=False)
            self.assertEqual(len(second["written"]), 0)
            self.assertEqual(len(second["skipped"]), 2)

            third = persist_design_system(ds, output_dir=tmp_path, page="pricing", force=True)
            self.assertEqual(len(third["written"]), 2)


class TestAuditor(unittest.TestCase):
    def test_human_html_scores_grade_f(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            plain = Path(tmp) / "plain.html"
            plain.write_text(
                "<!doctype html><html><body><h1> Joe's Hardware Store </h1><p>Open 8am to 5pm Monday through Saturday. Hammers $12.</p><button>Save</button></body></html>",
                encoding="utf-8",
            )
            report = audit_path(str(plain))
            self.assertLess(report["slop_score"], 20)
            self.assertEqual(report["grade"], "F")
            self.assertGreaterEqual(len(report["anti_human_prescriptions"]), 5)

    def test_showcase_html_scores_grade_s_plus(self) -> None:
        showcase = REPO_ROOT / "examples" / "nexusflow-ai-showcase.html"
        report = audit_path(str(showcase))
        self.assertGreaterEqual(report["slop_score"], 95)
        self.assertEqual(report["grade"], "S+")


class TestAgentSkillManifestsAndInstaller(unittest.TestCase):
    def test_skill_frontmatter_and_unique_names(self) -> None:
        skills_root = REPO_ROOT / "skills"
        skill_dirs = [d for d in sorted(skills_root.iterdir()) if d.is_dir()]
        self.assertGreaterEqual(len(skill_dirs), 3)

        seen_names = set()
        for sdir in skill_dirs:
            skill_md = sdir / "SKILL.md"
            self.assertTrue(skill_md.is_file(), f"Missing SKILL.md in {sdir}")
            text = skill_md.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"), f"Invalid frontmatter start in {skill_md}")
            frontmatter = text.split("---\n", 2)[1]
            name_line = next((ln for ln in frontmatter.splitlines() if ln.startswith("name:")), "")
            desc_line = next((ln for ln in frontmatter.splitlines() if ln.startswith("description:")), "")
            name_val = name_line.split(":", 1)[1].strip().strip('"').strip("'")
            desc_val = desc_line.split(":", 1)[1].strip().strip('"').strip("'")
            self.assertEqual(name_val, sdir.name)
            self.assertGreater(len(desc_val), 30)
            self.assertNotIn(name_val, seen_names)
            seen_names.add(name_val)

    def test_json_manifests_valid(self) -> None:
        for rel in [
            ".claude-plugin/plugin.json",
            ".claude-plugin/marketplace.json",
            "skill.json",
            "package.json",
        ]:
            path = REPO_ROOT / rel
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertIsInstance(data, dict)

    def test_node_cli_installer_all_platforms(self) -> None:
        cli = REPO_ROOT / "bin" / "cli.mjs"
        with tempfile.TemporaryDirectory() as tmp:
            proc = subprocess.run(
                ["node", str(cli), "init", "--ai", "all", "--dir", tmp],
                capture_output=True,
                text=True,
                check=True,
            )
            self.assertIn("Installed for Claude Code", proc.stdout)
            tmp_path = Path(tmp)
            self.assertTrue((tmp_path / ".claude/skills/ai-slop-ui-ux-pro-max/SKILL.md").is_file())
            self.assertTrue((tmp_path / ".cursor/rules/ai-slop-ui-ux-pro-max.mdc").is_file())
            self.assertTrue((tmp_path / ".agents/skills/ai-slop-copywriter/SKILL.md").is_file())
            self.assertTrue((tmp_path / ".windsurfrules").is_file())
            self.assertTrue((tmp_path / ".github/copilot-instructions.md").is_file())


if __name__ == "__main__":
    unittest.main()

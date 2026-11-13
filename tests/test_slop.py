"""Tests for AI-SLOP UI/UX PRO-MAX.

Run: python3 -m unittest discover -s tests -v
No dependencies beyond the standard library.
"""
from __future__ import annotations

import io
import json
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import slop_lint  # noqa: E402
import slop_gen  # noqa: E402


class TestRubric(unittest.TestCase):
    def test_signal_count(self):
        self.assertEqual(len(slop_lint.SIGNALS), 90)

    def test_category_budgets_sum_to_100(self):
        self.assertEqual(sum(cap for _, _, cap in slop_lint.CATEGORIES), 100)

    def test_every_signal_has_a_category_budget(self):
        caps = {key for key, _, _ in slop_lint.CATEGORIES}
        for signal in slop_lint.SIGNALS:
            self.assertIn(signal["cat"], caps, signal["id"])

    def test_ids_are_unique(self):
        ids = [s["id"] for s in slop_lint.SIGNALS]
        self.assertEqual(len(ids), len(set(ids)))


class TestLinter(unittest.TestCase):
    def score(self, rel: str) -> int:
        return slop_lint.score_file(ROOT / rel)["score"]

    def test_flagship_landing_is_certified(self):
        self.assertGreaterEqual(self.score("examples/01-max-landing.html"), 90)

    def test_dashboard_is_certified(self):
        self.assertGreaterEqual(self.score("examples/02-dashboard.html"), 90)

    def test_auth_is_certified(self):
        self.assertGreaterEqual(self.score("examples/03-auth.html"), 90)

    def test_tasteful_page_scores_low(self):
        self.assertLess(self.score("examples/00-before.html"), 25)

    def test_slopified_page_gains_at_least_50_points(self):
        before = self.score("examples/00-before.html")
        after = self.score("examples/04-slopified.html")
        self.assertGreaterEqual(after - before, 50)

    def test_json_shape(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = slop_lint.main([
                str(ROOT / "examples/01-max-landing.html"), "--json"
            ])
        self.assertEqual(code, 0)
        data = json.loads(buf.getvalue())
        for key in ("file", "score", "grade", "hits", "categories", "found", "missing", "next_moves"):
            self.assertIn(key, data)
        self.assertEqual(set(data["categories"]), {k for k, _, _ in slop_lint.CATEGORIES})

    def test_min_gate_exits_nonzero(self):
        with redirect_stdout(io.StringIO()):
            code = slop_lint.main([
                str(ROOT / "examples/00-before.html"), "--min", "90", "--quiet"
            ])
        self.assertEqual(code, 1)

    def test_linked_stylesheet_is_scored(self):
        # ledger for the auth page: CSS signals present, content signals honest
        result = slop_lint.score_file(ROOT / "examples/03-auth.html")
        self.assertIn("color.gradient_text", result["found"])
        self.assertIn("glass.blur", result["found"])
        # auth has no pricing section in its HTML
        self.assertIn("struct.pricing", result["missing"])

    def test_list_mode(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = slop_lint.main(["--list"])
        self.assertEqual(code, 0)
        self.assertIn("copy.ai_powered", buf.getvalue())


class TestGenerator(unittest.TestCase):
    def test_deterministic_with_seed(self):
        a = slop_gen.generate(seed=42)
        b = slop_gen.generate(seed=42)
        self.assertEqual(a, b)

    def test_seed_changes_output(self):
        self.assertNotEqual(slop_gen.generate(seed=1), slop_gen.generate(seed=2))

    def test_kit_is_complete(self):
        kit = slop_gen.generate(seed=7)
        self.assertEqual(len(kit["features"]), 6)
        self.assertEqual(len(kit["testimonials"]), 3)
        self.assertEqual(len(kit["stats"]), 4)
        self.assertIn("most popular", kit["pricing"]["pro"]["note"].lower())


if __name__ == "__main__":
    unittest.main()

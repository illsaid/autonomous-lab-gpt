#!/usr/bin/env python3
"""Smoke tests for the salvage_card CLI."""

import csv
import json
import subprocess
import sys
import unittest
from io import StringIO
from pathlib import Path

import salvage_card

ROOT = Path(__file__).parent
SCRIPT = ROOT / "salvage_card.py"


class SalvageCardTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_demo_outputs_ranked_text_cards(self):
        result = self.run_cli("--demo")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("#1", result.stdout)
        self.assertIn("score=", result.stdout)
        self.assertIn("angle:", result.stdout)
        self.assertIn("license:", result.stdout)

    def test_demo_json_is_parseable_and_ranked(self):
        result = self.run_cli("--demo", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        cards = json.loads(result.stdout)
        self.assertGreaterEqual(len(cards), 2)
        scores = [card["score"] for card in cards]
        self.assertEqual(scores, sorted(scores, reverse=True))
        self.assertTrue({"name", "score", "angle", "license_note", "prototype_name"}.issubset(cards[0]))

    def test_demo_csv_has_review_queue_columns(self):
        result = self.run_cli("--demo", "--csv")
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = list(csv.DictReader(StringIO(result.stdout)))
        self.assertGreaterEqual(len(rows), 2)
        self.assertEqual(
            list(rows[0].keys()),
            [
                "rank",
                "name",
                "score",
                "prototype_name",
                "language",
                "stars",
                "age_years",
                "angle",
                "license_note",
                "signals",
                "source_url",
                "research_note",
            ],
        )
        self.assertEqual(rows[0]["rank"], "1")
        self.assertTrue(rows[0]["prototype_name"].endswith("-rebuild"))
        self.assertIn(" | ", rows[0]["signals"])

    def test_topic_filtered_csv_limits_demo_rows(self):
        result = self.run_cli("--demo", "--topic", "simulation", "--csv")
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = list(csv.DictReader(StringIO(result.stdout)))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["name"], "demo/tiny-sim")
        self.assertEqual(rows[0]["prototype_name"], "tiny-sim-rebuild")

    def test_topic_filter_limits_demo_results(self):
        result = self.run_cli("--demo", "--topic", "simulation", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        cards = json.loads(result.stdout)
        self.assertEqual(len(cards), 1)
        self.assertEqual(cards[0]["name"], "demo/tiny-sim")
        self.assertEqual(cards[0]["prototype_name"], "tiny-sim-rebuild")

    def test_brief_outputs_rebuild_guidance(self):
        result = self.run_cli("--demo", "--topic", "simulation", "--brief")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Rebuild brief: demo/tiny-sim", result.stdout)
        self.assertIn("Next prototype name: tiny-sim-rebuild", result.stdout)
        self.assertIn("First build step:", result.stdout)
        self.assertIn("Why this candidate:", result.stdout)

    def test_brief_md_outputs_markdown_rebuild_guidance(self):
        result = self.run_cli("--demo", "--topic", "simulation", "--brief-md")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("# Rebuild brief: demo/tiny-sim", result.stdout)
        self.assertIn("**Next prototype name:** `tiny-sim-rebuild`", result.stdout)
        self.assertIn("## Reusable shape", result.stdout)
        self.assertIn("## First build step", result.stdout)
        self.assertIn("- ", result.stdout)

    def test_ticket_outputs_issue_ready_prototype_task(self):
        result = self.run_cli("--demo", "--topic", "simulation", "--ticket")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Title: Prototype tiny-sim-rebuild", result.stdout)
        self.assertIn("Goal:", result.stdout)
        self.assertIn("Start here:", result.stdout)
        self.assertIn("Acceptance checks:", result.stdout)
        self.assertIn("- Runs locally without external services", result.stdout)
        self.assertIn("- Uses fresh implementation, not copied source code", result.stdout)
        self.assertIn("Context:", result.stdout)
        self.assertIn("- Source candidate: demo/tiny-sim", result.stdout)

    def test_output_modes_are_mutually_exclusive(self):
        result = self.run_cli("--demo", "--ticket", "--json")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("choose only one output mode", result.stderr)

    def test_csv_conflicts_with_other_output_modes(self):
        result = self.run_cli("--demo", "--csv", "--json")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("choose only one output mode", result.stderr)

    def test_license_note_warns_for_unclear_rights(self):
        note = salvage_card.license_note({"license": "unknown"})
        self.assertIn("study the idea only", note)

    def test_prototype_name_falls_back_when_name_is_empty(self):
        self.assertEqual(salvage_card.prototype_name({"name": "///"}), "salvage-candidate-rebuild")


if __name__ == "__main__":
    unittest.main()

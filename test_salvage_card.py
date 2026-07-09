#!/usr/bin/env python3
"""Smoke tests for the salvage_card CLI."""

import json
import subprocess
import sys
import unittest
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
        self.assertTrue({"name", "score", "angle", "license_note"}.issubset(cards[0]))

    def test_license_note_warns_for_unclear_rights(self):
        note = salvage_card.license_note({"license": "NOASSERTION"})
        self.assertIn("study the idea only", note)


if __name__ == "__main__":
    unittest.main()

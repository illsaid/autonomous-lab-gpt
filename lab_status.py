#!/usr/bin/env python3
"""Print a small repository status report.

Usage:
    python lab_status.py
    python lab_status.py --json
"""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REQUIRED = [
    "README.md",
    "MISSION.md",
    "SEED.md",
    "AGENT_RULES.md",
    "JUDGING.md",
    "AGENT_STATE.md",
    "CHANGELOG.md",
    "DECISIONS.md",
    "RESEARCH_LOG.md",
    "THIRD_PARTY_NOTICES.md",
]


def build_report():
    files = [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]
    missing = [name for name in REQUIRED if not (ROOT / name).exists()]
    runnable = [p.relative_to(ROOT).as_posix() for p in files if p.suffix == ".py"]
    return {
        "file_count": len(files),
        "missing_required_files": missing,
        "runnable_files": sorted(runnable),
        "next_action": "Do one focused research pass, then improve the runnable script with a concrete finding.",
    }


def main():
    parser = argparse.ArgumentParser(description="Show repository status.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = build_report()
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print("Lab Status")
        print(f"Files: {report['file_count']}")
        print(f"Missing required files: {len(report['missing_required_files'])}")
        print("Runnable files:")
        for item in report["runnable_files"]:
            print(f"- {item}")
        print(f"Next action: {report['next_action']}")


if __name__ == "__main__":
    main()

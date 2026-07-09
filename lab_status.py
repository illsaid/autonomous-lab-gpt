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

DATA_SUFFIXES = {".csv", ".json", ".jsonl", ".sqlite", ".db", ".txt"}
TEST_PREFIXES = ("test_",)
TEST_SUFFIXES = ("_test.py", ".test.js", ".spec.js", ".test.ts", ".spec.ts")


def is_test_file(path):
    name = path.name
    return name.startswith(TEST_PREFIXES) or any(name.endswith(suffix) for suffix in TEST_SUFFIXES)


def choose_next_action(report):
    if report["missing_required_files"]:
        return "Restore the missing required project memory files."
    if not report["runnable_files"]:
        return "Add the first local runnable artifact."
    if not report["test_files"]:
        return "Add a tiny test or smoke-check for the runnable artifact."
    if not report["machine_readable_run_records"]:
        return "Add a machine-readable run record under RUNS/."
    return "Use research to add one user-visible capability to the runnable artifact."


def build_report():
    files = [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]
    missing = [name for name in REQUIRED if not (ROOT / name).exists()]
    runnable = [p.relative_to(ROOT).as_posix() for p in files if p.suffix == ".py"]
    tests = [p.relative_to(ROOT).as_posix() for p in files if is_test_file(p)]
    data_files = [p.relative_to(ROOT).as_posix() for p in files if p.suffix.lower() in DATA_SUFFIXES]
    run_records = [
        p.relative_to(ROOT).as_posix()
        for p in files
        if len(p.relative_to(ROOT).parts) > 1
        and p.relative_to(ROOT).parts[0] == "RUNS"
        and p.suffix.lower() in {".json", ".jsonl", ".yaml", ".yml"}
    ]
    report = {
        "file_count": len(files),
        "missing_required_files": missing,
        "runnable_files": sorted(runnable),
        "test_files": sorted(tests),
        "data_files": sorted(data_files),
        "machine_readable_run_records": sorted(run_records),
    }
    report["next_action"] = choose_next_action(report)
    return report


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
        print(f"Runnable files: {len(report['runnable_files'])}")
        for item in report["runnable_files"]:
            print(f"- {item}")
        print(f"Test files: {len(report['test_files'])}")
        print(f"Machine-readable run records: {len(report['machine_readable_run_records'])}")
        print(f"Data-like files: {len(report['data_files'])}")
        print(f"Next action: {report['next_action']}")


if __name__ == "__main__":
    main()

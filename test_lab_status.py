#!/usr/bin/env python3
"""Dependency-free smoke checks for lab_status.py.

Run:
    python test_lab_status.py
"""

import json
import subprocess
import sys

import lab_status


def test_build_report_shape():
    report = lab_status.build_report()
    required_keys = {
        "file_count",
        "missing_required_files",
        "runnable_files",
        "test_files",
        "data_files",
        "machine_readable_run_records",
        "next_action",
    }
    missing = required_keys.difference(report)
    assert not missing, f"missing report keys: {sorted(missing)}"
    assert isinstance(report["file_count"], int)
    assert "lab_status.py" in report["runnable_files"]
    assert report["missing_required_files"] == []


def test_json_cli_outputs_parseable_report():
    result = subprocess.run(
        [sys.executable, "lab_status.py", "--json"],
        check=True,
        capture_output=True,
        text=True,
    )
    report = json.loads(result.stdout)
    assert report["missing_required_files"] == []
    assert "lab_status.py" in report["runnable_files"]
    assert "test_lab_status.py" in report["test_files"]


def main():
    test_build_report_shape()
    test_json_cli_outputs_parseable_report()
    print("ok - lab_status smoke checks passed")


if __name__ == "__main__":
    main()

# Changelog

## Run 5

- Added `salvage_card.py`, a dependency-free local CLI for turning abandoned-repo JSONL metadata into ranked salvage cards.
- The CLI supports `--demo`, file input, and `--json`; each card includes a score, language/stars/age signals, a suggested salvage angle, and a license note.
- Updated project state to pivot away from repo-process tooling and toward a non-meta open-source archaeology artifact.
- Did not add a `RUNS/` record this run so the 3-file limit could prioritize the new artifact plus required state/changelog updates.

## Run 4

- Added the first run-history marker under `RUNS/`.
- Updated project state for the next run-history capability.

## Run 3

- Added `test_lab_status.py`, a dependency-free smoke test for the local status script.
- The smoke test checks `lab_status.build_report()` shape and verifies that `python lab_status.py --json` emits parseable JSON with expected repository signals.
- Updated agent state to reflect that the first runnable artifact is now also testable.

## Run 2

- Improved `lab_status.py` from a basic file counter into a slightly more useful local repo-triage script.
- Added detection for test files, data-like files, and machine-readable run records.
- Made the script's recommended next action depend on observed repository state.
- Updated agent state for the next run's executable/testable requirement.

## Run 1

- Added `lab_status.py`, the first runnable local artifact.
- The script reports repository file count, missing required files, runnable Python files, and a recommended next action.
- Updated agent state to move from pure bootstrap into small artifact iteration.

## Bootstrap

- Initialized the autonomous lab repository structure.
- Added mission, seed, rules, judging criteria, and initial agent state.

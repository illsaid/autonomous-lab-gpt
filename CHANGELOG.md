# Changelog

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

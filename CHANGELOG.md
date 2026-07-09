# Changelog

## Run 9

- Added `--min-score` and `--limit` scan controls to `salvage_card.py`.
- Filtering happens after scoring and sorting, so `--limit 5` returns the top five candidates and `--min-score 20` hides weaker candidates.
- The filters apply to both human-readable cards and `--json`, making larger research sets easier to inspect without dumping every entry.
- Did not add a `RUNS/` record so the 3-file limit could prioritize user-facing CLI behavior plus required state/changelog updates.

## Run 8

- Improved `salvage_card.py` so optional `source_url` and `research_note` fields are carried into generated cards.
- Text output now prints source and research context when present; `--json` includes those fields for downstream scripts.
- This makes `data/salvage_examples.jsonl` auditable through the CLI instead of requiring a human to cross-reference the raw JSONL.
- Did not add a `RUNS/` record so the 3-file limit could prioritize user-facing CLI behavior plus required state/changelog updates.

## Run 7

- Added `data/salvage_examples.jsonl`, a metadata-only real sample dataset for `salvage_card.py`.
- Included three archived MIT-licensed public repository candidates discovered through GitHub search: `yuanchuan/game-of-life`, `thebigmunch/gmusicapi-scripts`, and `emilyalbini/reddit-place-2017`.
- Verified README/license context before adding metadata; copied no third-party code.
- Did not add a `RUNS/` record so the 3-file limit could prioritize the real sample dataset plus required state/changelog updates.

## Run 6

- Added `test_salvage_card.py`, a dependency-free smoke test suite for `salvage_card.py`.
- The tests cover demo text output, demo JSON output, score ordering, and license-note behavior.
- This run improves the non-meta salvage artifact with executable test coverage.
- Did not add a `RUNS/` record so the 3-file limit could prioritize test coverage plus required state and changelog updates.

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

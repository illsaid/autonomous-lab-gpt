# Changelog

## Run 20

- Added `--csv` output to `salvage_card.py` for spreadsheet-friendly salvage candidate review.
- CSV output includes rank, name, score, prototype name, language, stars, age, angle, license note, signals, source URL, and research note.
- Updated output-mode conflict handling so `--csv` cannot be combined with `--json`, `--brief`, `--brief-md`, or `--ticket`.
- No `RUNS/` record was added; the 3-file limit was reserved for user-facing CLI behavior plus required state/changelog updates.

## Run 19

- Expanded `test_salvage_card.py` coverage for `--ticket` output.
- Added assertions for issue-ready ticket structure: title, goal, start step, acceptance checks, local/no-copy safeguards, context, and filtered source candidate.
- Updated output-mode conflict coverage to verify `--ticket` cannot be combined with `--json`.
- No `RUNS/` record was added; the 3-file limit was reserved for artifact test coverage plus required state/changelog updates.

## Run 18

- Added `--ticket` mode to `salvage_card.py` for issue-ready prototype tickets.
- Ticket output includes a prototype title, goal, first build step, local acceptance checks, license caution, score, source candidate, and score signals.
- Output modes are now mutually exclusive across `--json`, `--brief`, `--brief-md`, and `--ticket`.
- No `RUNS/` record was added; the 3-file limit was reserved for user-facing CLI behavior plus required state/changelog updates.

## Run 17

- Expanded `test_salvage_card.py` coverage for generated `prototype_name` behavior.
- JSON output tests now verify that cards include `prototype_name` and that the simulation demo produces `tiny-sim-rebuild`.
- Plain-text `--brief` and Markdown `--brief-md` tests now verify that the next prototype name is printed.
- Added a direct fallback test for empty or punctuation-only repository names.
- No `RUNS/` record was added; the 3-file limit was reserved for artifact test coverage plus required state/changelog updates.

## Run 16

- Added deterministic `prototype_name` generation to `salvage_card.py` cards.
- Plain-text `--brief` output now prints `Next prototype name` for the top candidate.
- Markdown `--brief-md` output now includes a backticked `Next prototype name` field for reuse in issues, folders, branches, or build notes.
- No `RUNS/` record was added; the 3-file limit was reserved for user-facing CLI behavior plus required state/changelog updates.

## Run 15

- Expanded `test_salvage_card.py` coverage for the newer Markdown brief behavior.
- Added a `--brief-md` test that verifies Markdown heading structure, first-build-step output, and bullet output for a filtered demo candidate.
- Updated the output-mode conflict test to match the current parser behavior.
- No `RUNS/` record was added; the 3-file limit was reserved for artifact test coverage plus required state/changelog updates.

## Run 14

- Added `--brief-md` to `salvage_card.py` for Markdown-ready rebuild briefs.
- Markdown brief output includes reusable headings, score metadata, problem statement, reusable shape, first build step, license caution, signal bullets, and source/research context when present.
- Output modes are now mutually exclusive across `--json`, `--brief`, and `--brief-md`.
- No `RUNS/` record was added; the 3-file limit was reserved for user-facing CLI behavior plus required state/changelog updates.

## Run 13

- Expanded `test_salvage_card.py` to cover newer user-facing CLI behavior.
- Added coverage for topic-filtered JSON output.
- Added coverage for filtered brief generation.
- Added coverage for the intentional `--brief` and `--json` conflict.
- No `RUNS/` record was added; the 3-file limit was reserved for artifact test coverage plus required state/changelog updates.

## Prior runs

See repository history for earlier changelog entries.

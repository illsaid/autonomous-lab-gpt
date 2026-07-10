# Agent State

## Agent

GPT repo worker.

## Current Phase

Phase 2 - Non-meta artifact direction.

## Current Understanding

The repository has pivoted away from self-audit tooling and toward a user-facing open-source archaeology artifact: `salvage_card.py`, a local CLI that turns neglected public repository metadata into ranked salvage prompts. The tool now has smoke tests, a small real-world metadata sample at `data/salvage_examples.jsonl`, auditable card output that preserves source context, scan controls for larger candidate sets, score signals, topic filtering, plain-text `--brief` output, Markdown-ready `--brief-md` output, issue-ready `--ticket` output, CSV export for spreadsheet/database review, and generated `prototype_name` slugs that make candidates easier to turn into concrete prototype tasks. The test suite covers topic filtering, plain brief output, Markdown brief output, ticket output, prototype-name propagation, fallback slug behavior, and mutual exclusion across prior output modes.

## Run Count

20

## Last Action

Added `--csv` output to `salvage_card.py` so ranked salvage candidates can be exported as a tabular review queue. CSV rows include rank, repository name, score, prototype slug, language, stars, age, angle, license note, signals, source URL, and research note.

## Current Objective

Grow the salvage-card artifact from a scorer into a small practical assistant for inspecting neglected public software ideas: real examples first, then auditable scoring, filtering, rebuild briefs, reusable Markdown output, prototype-ready naming, issue-ready tickets, spreadsheet-friendly exports, and regression coverage that lets the CLI keep improving without breaking existing output modes.

## Constraints To Remember

- Keep changes small.
- Prefer working artifacts over planning.
- Update state and changelog every run.
- Avoid repo-process features unless they directly support the non-meta salvage artifact.
- Do not copy code from public repositories without permissive license review and attribution.
- Treat sample repository metadata as research hints, not as copied third-party material.

## Change Limit Note

This run changed exactly 3 files: `salvage_card.py`, `AGENT_STATE.md`, and `CHANGELOG.md`. No `RUNS/` record was added because the 3-file limit was reserved for user-facing CLI behavior plus required state updates.

## Next Suggested Action

Add focused `--csv` test coverage, including header shape, filtered row count, and mutual exclusion with another output mode.

# Agent State

## Agent

GPT repo worker.

## Current Phase

Phase 2 - Non-meta artifact direction.

## Current Understanding

The repository has pivoted away from self-audit tooling and toward a user-facing open-source archaeology artifact: `salvage_card.py`, a local CLI that turns neglected public repository metadata into ranked salvage prompts. The tool now has smoke tests, a small real-world metadata sample at `data/salvage_examples.jsonl`, auditable card output that preserves source context, scan controls for larger candidate sets, score signals, topic filtering, plain-text `--brief` output, Markdown-ready `--brief-md` output, issue-ready `--ticket` output, CSV export for spreadsheet/database review, and generated `prototype_name` slugs that make candidates easier to turn into concrete prototype tasks. The companion `salvage_brief_file.py` script writes the top matching rebuild brief to a reusable Markdown file.

## Run Count

22

## Last Action

Added `salvage_brief_file.py`, a small companion CLI that imports the salvage-card scoring pipeline, selects the top matching candidate, and writes a Markdown rebuild brief to either `<prototype_name>.md` or a user-supplied `--output` path. This turns a promising candidate into a reusable file artifact instead of requiring copy/paste from stdout.

## Current Objective

Grow the salvage-card artifact from a scorer into a small practical assistant for inspecting neglected public software ideas: real examples first, then auditable scoring, filtering, rebuild briefs, reusable Markdown output, prototype-ready naming, issue-ready tickets, spreadsheet-friendly exports, file-based brief generation, and regression coverage that lets the CLI keep improving without breaking existing output modes.

## Constraints To Remember

- Keep changes small.
- Prefer working artifacts over planning.
- Update state and changelog every run.
- Avoid repo-process features unless they directly support the non-meta salvage artifact.
- Follow the repository license-review rules before reusing outside implementation details.
- Treat sample repository metadata as research hints.

## Change Limit Note

This run changed exactly 3 files: `salvage_brief_file.py`, `AGENT_STATE.md`, and `CHANGELOG.md`. No `RUNS/` record was added because the 3-file limit was reserved for user-facing file-output behavior plus required state updates.

## Next Suggested Action

Add focused tests for `salvage_brief_file.py`, including default output naming, custom `--output`, topic filtering, and no-candidate failure behavior.

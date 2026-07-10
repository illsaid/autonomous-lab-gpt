# Agent State

## Agent

GPT repo worker.

## Current Phase

Phase 2 - Non-meta artifact direction.

## Current Understanding

The repository has pivoted away from self-audit tooling and toward a user-facing open-source archaeology artifact: `salvage_card.py`, a local CLI that turns neglected public repository metadata into ranked salvage prompts. The tool now has smoke tests, a small real-world metadata sample at `data/salvage_examples.jsonl`, auditable card output that preserves source context, scan controls for larger candidate sets, score signals, topic filtering, plain-text `--brief` output, Markdown-ready `--brief-md` output, issue-ready `--ticket` output, CSV export for spreadsheet/database review, and generated `prototype_name` slugs that make candidates easier to turn into concrete prototype tasks. The test suite covers topic filtering, plain brief output, Markdown brief output, ticket output, prototype-name propagation, fallback slug behavior, CSV export shape, filtered CSV rows, and mutual exclusion across output modes.

## Run Count

21

## Last Action

Added focused regression coverage for `--csv` output in `test_salvage_card.py`. The new tests parse CLI CSV output with `csv.DictReader`, verify the review-queue column order, check prototype slug and signal serialization, confirm topic-filtered CSV produces one matching row, and assert that `--csv` conflicts with other output modes.

## Current Objective

Grow the salvage-card artifact from a scorer into a small practical assistant for inspecting neglected public software ideas: real examples first, then auditable scoring, filtering, rebuild briefs, reusable Markdown output, prototype-ready naming, issue-ready tickets, spreadsheet-friendly exports, and regression coverage that lets the CLI keep improving without breaking existing output modes.

## Constraints To Remember

- Keep changes small.
- Prefer working artifacts over planning.
- Update state and changelog every run.
- Avoid repo-process features unless they directly support the non-meta salvage artifact.
- Follow the repository license-review rules before reusing outside implementation details.
- Treat sample repository metadata as research hints.

## Change Limit Note

This run changed exactly 3 files: `test_salvage_card.py`, `AGENT_STATE.md`, and `CHANGELOG.md`. No `RUNS/` record was added because the 3-file limit was reserved for artifact test coverage plus required state updates.

## Next Suggested Action

Add a small user-facing output option that writes the top rebuild brief to a named Markdown file, or improve the sample dataset with one more permissively licensed public repository metadata record after source review.

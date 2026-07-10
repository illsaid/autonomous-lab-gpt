# Agent State

## Agent

GPT repo worker.

## Current Phase

Phase 2 - Non-meta artifact direction.

## Current Understanding

The repository has pivoted away from self-audit tooling and toward a user-facing open-source archaeology artifact: `salvage_card.py`, a local CLI that turns neglected public repository metadata into ranked salvage prompts. The tool now has smoke tests, a small real-world metadata sample at `data/salvage_examples.jsonl`, auditable card output that preserves source context, scan controls for larger candidate sets, score signals, topic filtering, plain-text `--brief` output, and Markdown-ready `--brief-md` output for reuse in issues, notes, or build docs. The test suite now covers topic filtering, plain brief output, Markdown brief output, and mutual exclusion across output modes.

## Run Count

15

## Last Action

Expanded `test_salvage_card.py` coverage for the newest user-facing brief behavior. Added a `--brief-md` test that verifies Markdown headings and bullet output for a filtered demo candidate, and replaced the stale conflict test with a broader output-mode conflict test that matches the current parser behavior shared by `--json`, `--brief`, and `--brief-md`.

## Current Objective

Grow the salvage-card artifact from a scorer into a small practical assistant for inspecting neglected public software ideas: real examples first, then auditable scoring, filtering, rebuild briefs, reusable Markdown output, and tests that help a human decide what to prototype next without breaking existing CLI behavior.

## Constraints To Remember

- Keep changes small.
- Prefer working artifacts over planning.
- Update state and changelog every run.
- Avoid repo-process features unless they directly support the non-meta salvage artifact.
- Do not copy code from public repositories without permissive license review and attribution.
- Treat sample repository metadata as research hints, not as copied third-party material.

## Change Limit Note

This run changed exactly 3 files: `test_salvage_card.py`, `AGENT_STATE.md`, and `CHANGELOG.md`. No `RUNS/` record was added because the 3-file limit was better spent on user-facing test coverage plus required state updates.

## Next Suggested Action

Add one small usability improvement to `salvage_card.py`: include a short "Next prototype name" field in brief output so the result is more directly reusable as a build ticket.

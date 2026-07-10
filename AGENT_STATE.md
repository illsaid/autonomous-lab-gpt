# Agent State

## Agent

GPT repo worker.

## Current Phase

Phase 2 - Non-meta artifact direction.

## Current Understanding

The repository has pivoted away from self-audit tooling and toward a user-facing open-source archaeology artifact: `salvage_card.py`, a local CLI that turns neglected public repository metadata into ranked salvage prompts. The tool now has smoke tests, a small real-world metadata sample at `data/salvage_examples.jsonl`, auditable card output that preserves source context, scan controls for larger candidate sets, score signals, topic filtering, plain-text `--brief` output, and Markdown-ready `--brief-md` output for reuse in issues, notes, or build docs. The test suite covers the newer topic and plain brief modes, including the `--brief`/`--json` conflict; `--brief-md` still needs explicit test coverage.

## Run Count

14

## Last Action

Added `--brief-md` to `salvage_card.py`, a Markdown-ready rebuild brief mode for the top matching candidate. The new mode keeps the same decision content as `--brief` but emits headings, bold metadata, and bullet signals so a human can paste a salvage brief into a GitHub issue, planning note, or handoff document. Output modes are now mutually exclusive across `--json`, `--brief`, and `--brief-md`.

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

This run changed exactly 3 files: `salvage_card.py`, `AGENT_STATE.md`, and `CHANGELOG.md`. No `RUNS/` record was added because the 3-file limit was better spent on user-facing CLI behavior plus required state updates.

## Next Suggested Action

Add explicit test coverage for `--brief-md`, including Markdown headings and the new mutual-exclusion error for incompatible output modes.

# Agent State

## Agent

GPT repo worker.

## Current Phase

Phase 2 - Non-meta artifact direction.

## Current Understanding

The repository has pivoted away from self-audit tooling and toward a user-facing open-source archaeology artifact: `salvage_card.py`, a local CLI that turns neglected public repository metadata into ranked salvage prompts. The tool now has smoke tests, a small real-world metadata sample at `data/salvage_examples.jsonl`, auditable card output that preserves source context, scan controls for larger candidate sets, score signals, topic filtering, and a `--brief` mode that turns the top matching candidate into a compact rebuild brief.

## Run Count

12

## Last Action

Added `--brief` mode to `salvage_card.py`. After existing filtering, the mode selects the top matching candidate and prints a compact rebuild brief with problem, reusable shape, first build step, license note, scoring rationale, and source or research context when available. `--brief` is text-only and cannot be combined with `--json`.

## Current Objective

Grow the salvage-card artifact from a scorer into a small practical assistant for inspecting neglected public software ideas: real examples first, then auditable scoring, filtering, and rebuild briefs that help a human decide what to prototype next.

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

Extend `test_salvage_card.py` to cover `--brief`, `--topic`, and the `--brief`/`--json` conflict.

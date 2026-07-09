# Agent State

## Agent

GPT repo worker.

## Current Phase

Phase 2 - Non-meta artifact direction.

## Current Understanding

The repository has pivoted away from self-audit tooling and toward a user-facing open-source archaeology artifact: `salvage_card.py`, a local CLI that turns neglected public repository metadata into ranked salvage prompts. The tool now has smoke tests, a small real-world metadata sample at `data/salvage_examples.jsonl`, auditable card output that preserves source context, and basic scan controls for larger candidate sets.

## Run Count

9

## Last Action

Added `--min-score` and `--limit` to `salvage_card.py`. Cards are still scored and sorted first; then a user can keep only candidates above a score threshold and/or display the top N. The filters work for both text and `--json` output, making the CLI more usable as the sample dataset grows without adding dependencies or network behavior.

## Current Objective

Grow the salvage-card artifact from a scorer into a small practical assistant for inspecting neglected public software ideas: real examples first, then auditable scoring/explanations, then possibly a lightweight viewer or generator that helps a human choose what to rebuild.

## Constraints To Remember

- Keep changes small.
- Prefer working artifacts over planning.
- Update state and changelog every run.
- Avoid repo-process features unless they directly support the non-meta salvage artifact.
- Do not copy code from public repositories without permissive license review and attribution.
- Treat sample repository metadata as research hints, not as copied third-party material.

## Change Limit Note

This run changed exactly 3 files: `salvage_card.py`, `AGENT_STATE.md`, and `CHANGELOG.md`. No `RUNS/` record was added because the current correction deprioritizes run tracking and the 3-file limit was better spent on user-facing CLI filtering plus required state updates.

## Next Suggested Action

Improve the card explanations rather than adding process machinery: add a small `score_reasons` or `signals` field so humans can see why a repo scored highly. Keep it dependency-free and preserve the existing text/JSON modes.

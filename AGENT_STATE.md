# Agent State

## Agent

GPT repo worker.

## Current Phase

Phase 2 - Non-meta artifact direction.

## Current Understanding

The repository has pivoted away from self-audit tooling and toward a user-facing open-source archaeology artifact: `salvage_card.py`, a local CLI that turns neglected public repository metadata into ranked salvage prompts. The tool now has smoke tests, a small real-world metadata sample at `data/salvage_examples.jsonl`, and card output that preserves source/audit context when those fields are present.

## Run Count

8

## Last Action

Improved `salvage_card.py` so cards carry through optional `source_url` and `research_note` fields from input JSONL. Text output now prints those fields when present, and `--json` includes them as structured fields. This makes the real sample dataset auditable directly from the CLI without network fetching, dependencies, or copied third-party code.

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

This run changed exactly 3 files: `salvage_card.py`, `AGENT_STATE.md`, and `CHANGELOG.md`. No `RUNS/` record was added because the current correction deprioritizes run tracking and the 3-file limit was better spent on user-facing CLI output plus required state updates.

## Next Suggested Action

Add a small `--min-score` or `--limit` filter to `salvage_card.py` so a larger JSONL research set can be scanned without dumping every candidate. Keep it dependency-free and update tests if the 3-file limit can be satisfied by pairing code + tests with required state/changelog updates.

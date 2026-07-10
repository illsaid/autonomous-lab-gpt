# Agent State

## Agent

GPT repo worker.

## Current Phase

Phase 2 - Non-meta artifact direction.

## Current Understanding

The repository has pivoted away from self-audit tooling and toward a user-facing open-source archaeology artifact: `salvage_card.py`, a local CLI that turns neglected public repository metadata into ranked salvage prompts. The tool now has smoke tests, a small real-world metadata sample at `data/salvage_examples.jsonl`, auditable card output that preserves source context, basic scan controls for larger candidate sets, score signals that explain why each candidate ranked where it did, and a topic filter for narrowing the candidate set before scoring.

## Run Count

11

## Last Action

Added a `--topic` filter to `salvage_card.py`. The filter searches candidate name, description, language, and topics before cards are scored, so a human can ask for a focused slice such as `--topic simulation`, `--topic cli`, or `--topic music` instead of scanning the whole metadata file. The existing angle detection now uses the same shared searchable text helper.

## Current Objective

Grow the salvage-card artifact from a scorer into a small practical assistant for inspecting neglected public software ideas: real examples first, then auditable scoring/explanations, now practical filtering, then possibly a lightweight viewer or generator that helps a human choose what to rebuild.

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

Improve practical output rather than process machinery: add a `--brief` mode that turns the top matching salvage card into a compact rebuild brief with problem, reusable shape, first build step, and license caution.

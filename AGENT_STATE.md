# Agent State

## Agent

GPT repo worker.

## Current Phase

Phase 2 - Non-meta artifact direction.

## Current Understanding

The repository has pivoted away from self-audit tooling and toward a user-facing open-source archaeology artifact: `salvage_card.py`, a local CLI that turns neglected public repository metadata into ranked salvage prompts. The tool now has smoke tests, a small real-world metadata sample at `data/salvage_examples.jsonl`, auditable card output that preserves source context, basic scan controls for larger candidate sets, and score signals that explain why each candidate ranked where it did.

## Run Count

10

## Last Action

Added a `score_signals()` explanation layer to `salvage_card.py`. Each generated card now includes a `signals` array in `--json` output and a readable `signals:` line in text output, covering dormancy, prior interest, license posture, archive status, topics, and description availability. This makes the ranking more inspectable for a human choosing what to salvage next.

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

This run changed exactly 3 files: `salvage_card.py`, `AGENT_STATE.md`, and `CHANGELOG.md`. No `RUNS/` record was added because the current correction deprioritizes run tracking and the 3-file limit was better spent on user-facing CLI explanations plus required state updates.

## Next Suggested Action

Improve practical selection rather than process machinery: add a simple `--topic` filter or a `--angle`/`--format` selector so a human can narrow cards by the kind of artifact they want to build next.

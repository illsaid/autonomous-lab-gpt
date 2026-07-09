# Agent State

## Agent

GPT repo worker.

## Current Phase

Phase 2 - Non-meta artifact direction.

## Current Understanding

The repository has pivoted away from self-audit tooling and toward a user-facing open-source archaeology artifact: `salvage_card.py`, a local CLI that turns neglected public repository metadata into ranked salvage prompts. The tool now has both smoke tests and a small real-world metadata sample at `data/salvage_examples.jsonl`.

## Run Count

7

## Last Action

Added `data/salvage_examples.jsonl`, a metadata-only sample set with three live-researched archived MIT-licensed public repositories: `yuanchuan/game-of-life`, `thebigmunch/gmusicapi-scripts`, and `emilyalbini/reddit-place-2017`. No code or repository contents were copied; the file records only compact metadata, source URLs, and research notes. The sample is intended to make `python salvage_card.py data/salvage_examples.jsonl --json` useful beyond the built-in demo.

## Current Objective

Grow the salvage-card artifact from a scorer into a small practical assistant for inspecting neglected public software ideas: real examples first, then better scoring/explanations, then possibly a lightweight viewer or generator that helps a human choose what to rebuild.

## Constraints To Remember

- Keep changes small.
- Prefer working artifacts over planning.
- Update state and changelog every run.
- Avoid repo-process features unless they directly support the non-meta salvage artifact.
- Do not copy code from public repositories without permissive license review and attribution.
- Treat sample repository metadata as research hints, not as copied third-party material.

## Change Limit Note

This run changed exactly 3 files: `data/salvage_examples.jsonl`, `AGENT_STATE.md`, and `CHANGELOG.md`. No `RUNS/` record was added because the current correction explicitly deprioritizes run tracking and the 3-file limit was better spent on a real sample dataset plus required state updates.

## Next Suggested Action

Improve `salvage_card.py` so output includes `source_url` and `research_note` when present. That would make the real sample dataset auditable from the CLI without adding dependencies or copying third-party code.

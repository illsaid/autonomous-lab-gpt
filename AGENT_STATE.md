# Agent State

## Agent

GPT repo worker.

## Current Phase

Phase 2 - Non-meta artifact direction.

## Current Understanding

The repository had drifted into self-audit tooling (`lab_status.py`) and run-history bookkeeping. The current correction is to pivot toward a user-facing artifact inspired by `SEED.md`: salvage-oriented tooling for turning neglected public repository metadata into concrete build prompts.

## Run Count

6

## Last Action

Added `test_salvage_card.py`, a dependency-free smoke test suite for `salvage_card.py`. The tests verify that `python salvage_card.py --demo` emits ranked text cards, that `python salvage_card.py --demo --json` emits parseable score-sorted JSON, and that unclear licenses produce a study-only warning. This satisfies the every-third-run executable/testable rule with a real test improvement to the non-meta salvage artifact.

## Current Objective

Grow `salvage_card.py` into a useful open-source archaeology assistant: first with reliable tests, then with real researched JSONL examples from public repositories, while keeping the project local-first and license-conscious.

## Constraints To Remember

- Keep changes small.
- Prefer working artifacts over planning.
- Update state and changelog every run.
- Avoid repo-process features unless they directly support the non-meta salvage artifact.
- Do not copy code from public repositories without permissive license review and attribution.

## Change Limit Note

This run changed exactly 3 files: `test_salvage_card.py`, `AGENT_STATE.md`, and `CHANGELOG.md`. No `RUNS/` record was added because the current instruction explicitly deprioritizes run tracking as a main content change, and the 3-file limit was better spent on test coverage plus required state updates.

## Next Suggested Action

Add a small `data/salvage_examples.jsonl` file with 2-3 live-verified abandoned repository metadata entries, then ensure `salvage_card.py data/salvage_examples.jsonl --json` works against real examples. Prefer metadata only; do not copy code.
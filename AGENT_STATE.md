# Agent State

## Agent

GPT repo worker.

## Current Phase

Phase 2 - Non-meta artifact direction.

## Current Understanding

The repository had drifted into self-audit tooling (`lab_status.py`) and run-history bookkeeping. The current correction is to pivot toward a user-facing artifact inspired by `SEED.md`: salvage-oriented tooling for turning neglected public repository metadata into concrete build prompts.

## Run Count

5

## Last Action

Added `salvage_card.py`, a dependency-free local CLI that reads abandoned-repo JSONL metadata (or a built-in demo) and emits ranked salvage cards with scores, reuse angles, and license notes. This is the first non-meta artifact direction: a small tool a human could use while exploring old public repos, rather than a tool for auditing this repository.

## Current Objective

Grow `salvage_card.py` into a useful open-source archaeology assistant: first with better scoring/tests, then with real researched JSONL examples from public repositories, while keeping the project local-first and license-conscious.

## Constraints To Remember

- Keep changes small.
- Prefer working artifacts over planning.
- Update state and changelog every run.
- Avoid repo-process features unless they directly support the non-meta salvage artifact.
- Do not copy code from public repositories without permissive license review and attribution.

## Change Limit Note

This run changed exactly 3 files: `salvage_card.py`, `AGENT_STATE.md`, and `CHANGELOG.md`. No `RUNS/` record was added because the current instruction explicitly deprioritizes run tracking as a main content change, and the 3-file limit was better spent on a real artifact plus required state updates.

## Next Suggested Action

Add a tiny smoke test for `salvage_card.py` that verifies `--demo` and `--json` output, or add a small `data/salvage_examples.jsonl` file with 2-3 live-verified abandoned repository metadata entries. Prefer the test first if only one file can be added next run.

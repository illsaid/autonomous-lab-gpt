# Agent State

## Agent

GPT repo worker.

## Current Phase

Phase 2 - Non-meta artifact direction.

## Current Understanding

The repository has pivoted away from self-audit tooling and toward a user-facing open-source archaeology artifact: `salvage_card.py`, a local CLI that turns neglected public repository metadata into ranked salvage prompts. The tool now has smoke tests, a small real-world metadata sample at `data/salvage_examples.jsonl`, auditable card output that preserves source context, scan controls for larger candidate sets, score signals, topic filtering, and a `--brief` mode that turns the top matching candidate into a compact rebuild brief. The test suite now covers the newer topic and brief modes, including the `--brief`/`--json` conflict.

## Run Count

13

## Last Action

Expanded `test_salvage_card.py` to cover the newer user-facing CLI modes: topic-filtered JSON output, brief output for a filtered candidate, and rejection of `--brief` combined with `--json`. This was a test-coverage run rather than a new feature run, following the prior run's suggested action and keeping the salvage-card artifact safer to extend.

## Current Objective

Grow the salvage-card artifact from a scorer into a small practical assistant for inspecting neglected public software ideas: real examples first, then auditable scoring, filtering, rebuild briefs, and tests that help a human decide what to prototype next without breaking existing CLI behavior.

## Constraints To Remember

- Keep changes small.
- Prefer working artifacts over planning.
- Update state and changelog every run.
- Avoid repo-process features unless they directly support the non-meta salvage artifact.
- Do not copy code from public repositories without permissive license review and attribution.
- Treat sample repository metadata as research hints, not as copied third-party material.

## Change Limit Note

This run changed exactly 3 files: `test_salvage_card.py`, `AGENT_STATE.md`, and `CHANGELOG.md`. No `RUNS/` record was added because the 3-file limit was better spent on user-facing CLI test coverage plus required state updates.

## Next Suggested Action

Add one more output mode that makes salvage briefs easier to reuse outside the terminal, such as `--brief-md` for Markdown-ready rebuild briefs, while keeping it mutually exclusive with `--json` and the current plain-text `--brief`.

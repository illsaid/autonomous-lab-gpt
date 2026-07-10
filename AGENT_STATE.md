# Agent State

## Agent

GPT repo worker.

## Current Phase

Phase 2 - Non-meta artifact direction.

## Current Understanding

The repository has pivoted away from self-audit tooling and toward a user-facing open-source archaeology artifact: `salvage_card.py`, a local CLI that turns neglected public repository metadata into ranked salvage prompts. The tool now has smoke tests, a small real-world metadata sample at `data/salvage_examples.jsonl`, auditable card output that preserves source context, scan controls for larger candidate sets, score signals, topic filtering, plain-text `--brief` output, Markdown-ready `--brief-md` output, and generated `prototype_name` slugs that make briefs more directly reusable as build tickets or project notes. The test suite covers topic filtering, plain brief output, Markdown brief output, and mutual exclusion across output modes.

## Run Count

16

## Last Action

Added a small user-facing build-ticket improvement to `salvage_card.py`: each generated card now includes a deterministic `prototype_name` derived from the repository name, and both plain-text and Markdown brief outputs print it as the next prototype name. This gives a human a ready slug to use for an issue, folder, branch, or throwaway prototype without inventing naming by hand.

## Current Objective

Grow the salvage-card artifact from a scorer into a small practical assistant for inspecting neglected public software ideas: real examples first, then auditable scoring, filtering, rebuild briefs, reusable Markdown output, prototype-ready naming, and tests that help a human decide what to prototype next without breaking existing CLI behavior.

## Constraints To Remember

- Keep changes small.
- Prefer working artifacts over planning.
- Update state and changelog every run.
- Avoid repo-process features unless they directly support the non-meta salvage artifact.
- Do not copy code from public repositories without permissive license review and attribution.
- Treat sample repository metadata as research hints, not as copied third-party material.

## Change Limit Note

This run changed exactly 3 files: `salvage_card.py`, `AGENT_STATE.md`, and `CHANGELOG.md`. No `RUNS/` record was added because the 3-file limit was reserved for user-facing CLI behavior plus required state updates.

## Next Suggested Action

Add test coverage for `prototype_name` in JSON, `--brief`, and `--brief-md` output so the new build-ticket field stays stable.

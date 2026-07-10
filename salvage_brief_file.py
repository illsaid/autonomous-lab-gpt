#!/usr/bin/env python3
"""Write a Markdown rebuild brief from salvage-card candidates.

This is a small companion CLI for turning the top matching neglected-repo
candidate into a reusable `.md` artifact that can be opened, shared, edited,
or dropped into an issue tracker.

Usage:
    python salvage_brief_file.py --demo --topic simulation
    python salvage_brief_file.py repos.jsonl --topic maps --output briefs/map.md
"""

import argparse
from pathlib import Path

import salvage_card


def brief_markdown(card):
    lines = [
        f"# Rebuild brief: {card['name']}",
        "",
        f"**Score:** {card['score']} ({card['language']}, {card['stars']} stars, {card['age_years']}y old)",
        "",
        f"**Next prototype name:** `{card['prototype_name']}`",
        "",
        "## Problem",
        card["description"],
        "",
        "## Reusable shape",
        card["angle"],
        "",
        "## First build step",
        salvage_card.first_build_step(card),
        "",
        "## License caution",
        card["license_note"],
        "",
        "## Why this candidate",
    ]
    lines.extend(f"- {signal}" for signal in card["signals"][:3])
    if card.get("source_url"):
        lines.extend(["", f"**Source:** {card['source_url']}"])
    if card.get("research_note"):
        lines.extend(["", f"**Research note:** {card['research_note']}"])
    return "\n".join(lines) + "\n"


def choose_card(args):
    if args.demo:
        items = salvage_card.DEMO_ITEMS
    elif args.input:
        items = salvage_card.load_jsonl(args.input)
    else:
        raise SystemExit("provide a JSONL input file or use --demo")

    cards = salvage_card.filter_cards(
        salvage_card.build_cards(salvage_card.filter_items(items, topic=args.topic)),
        min_score=args.min_score,
        limit=1,
    )
    if not cards:
        raise SystemExit("No salvage candidates found.")
    return cards[0]


def main():
    parser = argparse.ArgumentParser(description="Write the top salvage rebuild brief to Markdown.")
    parser.add_argument("input", nargs="?", help="JSONL file of repository metadata")
    parser.add_argument("--demo", action="store_true", help="run against built-in example metadata")
    parser.add_argument("--topic", help="only use candidates matching this text")
    parser.add_argument("--min-score", type=float, help="only use candidates with this score or higher")
    parser.add_argument("--output", help="Markdown output path; defaults to <prototype_name>.md")
    args = parser.parse_args()

    card = choose_card(args)
    output_path = Path(args.output or f"{card['prototype_name']}.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(brief_markdown(card), encoding="utf-8")
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()

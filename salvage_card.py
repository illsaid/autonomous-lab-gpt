#!/usr/bin/env python3
"""Generate salvage cards from abandoned-repo metadata.

This local-first tool turns JSONL observations about neglected public
repositories into ranked build prompts. It does not fetch the network. It only
reads metadata supplied by a human or future research run.

Usage:
    python salvage_card.py --demo
    python salvage_card.py repos.jsonl
    python salvage_card.py repos.jsonl --json
"""

import argparse
import json
from datetime import date
from pathlib import Path

PERMISSIVE_LICENSES = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC"}

DEMO_ITEMS = [
    {
        "name": "demo/old-map-tool",
        "description": "Archived utility for annotating local walking maps",
        "language": "Python",
        "license": "MIT",
        "stars": 84,
        "archived": True,
        "pushed_at": "2018-04-12",
        "topics": ["maps", "cli", "geojson"],
    },
    {
        "name": "demo/tiny-sim",
        "description": "Old browser simulation experiment with simple moving entities",
        "language": "JavaScript",
        "license": "BSD-3-Clause",
        "stars": 31,
        "archived": True,
        "pushed_at": "2016-09-03",
        "topics": ["simulation", "canvas"],
    },
]


def parse_date(value):
    if not value:
        return None
    try:
        year, month, day = (int(part) for part in value[:10].split("-"))
        return date(year, month, day)
    except (TypeError, ValueError):
        return None


def age_years(item):
    pushed = parse_date(item.get("pushed_at"))
    if not pushed:
        return 0.0
    return max(0.0, (date.today() - pushed).days / 365.25)


def salvage_score(item):
    stars = item.get("stars") or 0
    age_score = min(age_years(item), 12.0)
    star_score = min(stars / 25.0, 6.0)
    license_score = 4.0 if item.get("license") in PERMISSIVE_LICENSES else 0.0
    archive_score = 2.0 if item.get("archived") else 0.0
    topic_score = min(len(item.get("topics") or []), 4)
    description_score = 2.0 if item.get("description") else 0.0
    return round(age_score + star_score + license_score + archive_score + topic_score + description_score, 2)


def salvage_angle(item):
    text = " ".join(
        str(part).lower()
        for part in [item.get("name", ""), item.get("description", ""), item.get("language", ""), " ".join(item.get("topics") or [])]
    )
    if any(word in text for word in ["game", "canvas", "simulation"]):
        return "Extract the loop; rebuild it as a tiny modern playable prototype."
    if any(word in text for word in ["map", "geo", "location", "route"]):
        return "Modernize the spatial workflow as a focused local-data explorer."
    if any(word in text for word in ["bot", "chat", "slack", "discord"]):
        return "Keep the conversation pattern and replace the stale platform glue."
    if any(word in text for word in ["dataset", "list", "catalog", "archive"]):
        return "Make the old structure searchable, ranked, or explorable."
    if any(word in text for word in ["cli", "script", "tool", "utility"]):
        return "Preserve the single-purpose workflow as a dependency-light CLI."
    return "Identify the reusable shape and make one small working version."


def license_note(item):
    license_name = item.get("license") or "unknown"
    if license_name in PERMISSIVE_LICENSES:
        return f"{license_name}: safe for idea study; attribute anything reused."
    return f"{license_name}: study the idea only unless rights are clarified."


def load_jsonl(path):
    items = []
    with Path(path).open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                items.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"{path}:{line_number}: invalid JSONL: {exc}") from exc
    return items


def build_cards(items):
    cards = []
    for item in items:
        cards.append({
            "name": item.get("name", "(unnamed)"),
            "score": salvage_score(item),
            "language": item.get("language") or "unknown",
            "stars": item.get("stars") or 0,
            "age_years": round(age_years(item), 1),
            "angle": salvage_angle(item),
            "license_note": license_note(item),
        })
    return sorted(cards, key=lambda card: card["score"], reverse=True)


def print_cards(cards):
    if not cards:
        print("No salvage candidates found.")
        return
    for index, card in enumerate(cards, start=1):
        print(f"#{index} {card['name']}  score={card['score']}")
        print(f"   language={card['language']} stars={card['stars']} age={card['age_years']}y")
        print(f"   angle: {card['angle']}")
        print(f"   license: {card['license_note']}")


def main():
    parser = argparse.ArgumentParser(description="Generate salvage cards from abandoned-repo JSONL metadata.")
    parser.add_argument("input", nargs="?", help="JSONL file of repository metadata")
    parser.add_argument("--demo", action="store_true", help="run against built-in example metadata")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of text cards")
    args = parser.parse_args()

    if args.demo:
        items = DEMO_ITEMS
    elif args.input:
        items = load_jsonl(args.input)
    else:
        parser.error("provide a JSONL input file or use --demo")

    cards = build_cards(items)
    if args.json:
        print(json.dumps(cards, indent=2, sort_keys=True))
    else:
        print_cards(cards)


if __name__ == "__main__":
    main()

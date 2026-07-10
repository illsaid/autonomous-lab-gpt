#!/usr/bin/env python3
"""Generate salvage cards from abandoned-repo metadata.

This local-first tool turns JSONL observations about neglected public
repositories into ranked build prompts. It does not fetch the network. It only
reads metadata supplied by a human or future research run.

Usage:
    python salvage_card.py --demo
    python salvage_card.py repos.jsonl
    python salvage_card.py repos.jsonl --json
    python salvage_card.py repos.jsonl --min-score 20 --limit 5
    python salvage_card.py repos.jsonl --topic simulation
    python salvage_card.py repos.jsonl --topic simulation --brief
    python salvage_card.py repos.jsonl --topic simulation --brief-md
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


def score_signals(item):
    signals = []
    years = age_years(item)
    if years >= 8:
        signals.append(f"old enough to be neglected ({years:.1f} years since last push)")
    elif years >= 3:
        signals.append(f"some dormancy signal ({years:.1f} years since last push)")
    elif years:
        signals.append(f"recent enough that abandonment is less clear ({years:.1f} years since last push)")
    else:
        signals.append("missing or invalid pushed_at date")

    stars = item.get("stars") or 0
    if stars >= 150:
        signals.append(f"strong prior interest ({stars} stars)")
    elif stars >= 25:
        signals.append(f"some prior interest ({stars} stars)")
    else:
        signals.append(f"low visible demand ({stars} stars)")

    license_name = item.get("license") or "unknown"
    if license_name in PERMISSIVE_LICENSES:
        signals.append(f"permissive license ({license_name})")
    else:
        signals.append(f"license needs caution ({license_name})")

    if item.get("archived"):
        signals.append("explicitly archived")
    else:
        signals.append("not marked archived")

    topics = item.get("topics") or []
    if topics:
        signals.append(f"tagged shape: {', '.join(str(topic) for topic in topics[:4])}")
    else:
        signals.append("no topics supplied")

    if item.get("description"):
        signals.append("has a usable description")
    else:
        signals.append("missing description")

    return signals


def searchable_text(item):
    parts = [
        item.get("name", ""),
        item.get("description", ""),
        item.get("language", ""),
        " ".join(str(topic) for topic in item.get("topics") or []),
    ]
    return " ".join(str(part).lower() for part in parts if part)


def matches_topic(item, topic):
    if not topic:
        return True
    needle = topic.lower()
    return needle in searchable_text(item)


def salvage_angle(item):
    text = searchable_text(item)
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


def first_build_step(card):
    text = " ".join([card.get("name", ""), card.get("description", ""), card.get("angle", "")]).lower()
    if any(word in text for word in ["game", "canvas", "simulation", "playable"]):
        return "Build one tiny loop with placeholder data or shapes before touching the original code."
    if any(word in text for word in ["map", "geo", "location", "route"]):
        return "Create a local sample file and render one searchable or filterable spatial view."
    if any(word in text for word in ["dataset", "list", "catalog", "archive"]):
        return "Convert a handful of records into JSONL and add one query that exposes the hidden pattern."
    if any(word in text for word in ["cli", "script", "tool", "utility"]):
        return "Rebuild the core command with one input, one output, and no external services."
    return "Write the smallest fresh prototype that proves the reusable behavior still matters."


def prototype_name(card):
    raw_name = card.get("name") or "salvage-candidate"
    repo_name = raw_name.rsplit("/", 1)[-1]
    slug = "".join(char.lower() if char.isalnum() else "-" for char in repo_name).strip("-")
    slug = "-".join(part for part in slug.split("-") if part)
    if not slug:
        slug = "salvage-candidate"
    return f"{slug}-rebuild"


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
        card = {
            "name": item.get("name", "(unnamed)"),
            "description": item.get("description") or "No description supplied.",
            "score": salvage_score(item),
            "signals": score_signals(item),
            "language": item.get("language") or "unknown",
            "stars": item.get("stars") or 0,
            "age_years": round(age_years(item), 1),
            "angle": salvage_angle(item),
            "license_note": license_note(item),
        }
        card["prototype_name"] = prototype_name(card)
        if item.get("source_url"):
            card["source_url"] = item["source_url"]
        if item.get("research_note"):
            card["research_note"] = item["research_note"]
        cards.append(card)
    return sorted(cards, key=lambda card: card["score"], reverse=True)


def filter_items(items, topic=None):
    if topic:
        items = [item for item in items if matches_topic(item, topic)]
    return items


def filter_cards(cards, min_score=None, limit=None):
    if min_score is not None:
        cards = [card for card in cards if card["score"] >= min_score]
    if limit is not None:
        cards = cards[:limit]
    return cards


def print_cards(cards):
    if not cards:
        print("No salvage candidates found.")
        return
    for index, card in enumerate(cards, start=1):
        print(f"#{index} {card['name']}  score={card['score']}")
        print(f"   language={card['language']} stars={card['stars']} age={card['age_years']}y")
        print(f"   signals: {'; '.join(card['signals'])}")
        print(f"   angle: {card['angle']}")
        print(f"   license: {card['license_note']}")
        if card.get("source_url"):
            print(f"   source: {card['source_url']}")
        if card.get("research_note"):
            print(f"   research: {card['research_note']}")


def print_brief(cards):
    if not cards:
        print("No salvage candidates found.")
        return
    card = cards[0]
    print(f"Rebuild brief: {card['name']}")
    print(f"Score: {card['score']} ({card['language']}, {card['stars']} stars, {card['age_years']}y old)")
    print(f"Next prototype name: {card['prototype_name']}")
    print(f"Problem: {card['description']}")
    print(f"Reusable shape: {card['angle']}")
    print(f"First build step: {first_build_step(card)}")
    print(f"License caution: {card['license_note']}")
    print(f"Why this candidate: {'; '.join(card['signals'][:3])}")
    if card.get("source_url"):
        print(f"Source: {card['source_url']}")
    if card.get("research_note"):
        print(f"Research note: {card['research_note']}")


def print_brief_markdown(cards):
    if not cards:
        print("No salvage candidates found.")
        return
    card = cards[0]
    print(f"# Rebuild brief: {card['name']}")
    print()
    print(f"**Score:** {card['score']} ({card['language']}, {card['stars']} stars, {card['age_years']}y old)")
    print()
    print(f"**Next prototype name:** `{card['prototype_name']}`")
    print()
    print(f"## Problem")
    print(card["description"])
    print()
    print(f"## Reusable shape")
    print(card["angle"])
    print()
    print(f"## First build step")
    print(first_build_step(card))
    print()
    print(f"## License caution")
    print(card["license_note"])
    print()
    print(f"## Why this candidate")
    for signal in card["signals"][:3]:
        print(f"- {signal}")
    if card.get("source_url"):
        print()
        print(f"**Source:** {card['source_url']}")
    if card.get("research_note"):
        print()
        print(f"**Research note:** {card['research_note']}")


def main():
    parser = argparse.ArgumentParser(description="Generate salvage cards from abandoned-repo JSONL metadata.")
    parser.add_argument("input", nargs="?", help="JSONL file of repository metadata")
    parser.add_argument("--demo", action="store_true", help="run against built-in example metadata")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of text cards")
    parser.add_argument("--brief", action="store_true", help="emit a compact rebuild brief for the top matching candidate")
    parser.add_argument("--brief-md", action="store_true", help="emit a Markdown rebuild brief for the top matching candidate")
    parser.add_argument("--min-score", type=float, help="only show cards with this score or higher")
    parser.add_argument("--limit", type=int, help="only show the top N cards after scoring and filtering")
    parser.add_argument("--topic", help="only score candidates whose name, description, language, or topics match this text")
    args = parser.parse_args()

    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be at least 1")
    if sum(bool(flag) for flag in [args.json, args.brief, args.brief_md]) > 1:
        parser.error("choose only one output mode: --json, --brief, or --brief-md")

    if args.demo:
        items = DEMO_ITEMS
    elif args.input:
        items = load_jsonl(args.input)
    else:
        parser.error("provide a JSONL input file or use --demo")

    cards = filter_cards(build_cards(filter_items(items, topic=args.topic)), min_score=args.min_score, limit=args.limit)
    if args.json:
        print(json.dumps(cards, indent=2, sort_keys=True))
    elif args.brief:
        print_brief(cards)
    elif args.brief_md:
        print_brief_markdown(cards)
    else:
        print_cards(cards)


if __name__ == "__main__":
    main()

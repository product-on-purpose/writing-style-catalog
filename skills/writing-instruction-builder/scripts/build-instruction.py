#!/usr/bin/env python3
"""
Build a composed writing instruction from taxonomy entry IDs.

Usage:
    python build-instruction.py [--voice ID] [--tone ID] [--style ID] [--format ID]
                                 [--topic TEXT] [--audience TEXT] [--list]
"""
import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]  # 3 levels up from skills/writing-instruction-builder/scripts/
TAXONOMY_ROOT = REPO_ROOT / "taxonomy"

AXES = {
    "voice": TAXONOMY_ROOT / "voices",
    "tone": TAXONOMY_ROOT / "tones",
    "style": TAXONOMY_ROOT / "styles",
    "format": TAXONOMY_ROOT / "formats",
}


def load_entry(axis: str, entry_id: str) -> dict | None:
    """Load and parse an ENTRY.md file, returning the frontmatter as a dict."""
    entry_path = AXES[axis] / entry_id / "ENTRY.md"
    if not entry_path.exists():
        return None

    content = entry_path.read_text(encoding="utf-8")
    # Extract YAML frontmatter between --- delimiters
    if not content.startswith("---"):
        return None

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None

    frontmatter_text = parts[1].strip()
    # Parse YAML manually for the fields we need (avoid requiring pyyaml)
    # This is a simple key: value parser sufficient for our frontmatter structure
    return _parse_simple_yaml(frontmatter_text)


def _parse_simple_yaml(text: str) -> dict:
    """Parse simple YAML frontmatter (key: value pairs, no nested objects needed here)."""
    result = {}
    current_key = None
    current_list = None

    for line in text.split("\n"):
        if not line.strip():
            if current_list is not None:
                result[current_key] = current_list
                current_key = None
                current_list = None
            continue

        if line.startswith("  - ") and current_list is not None:
            current_list.append(line[4:].strip())
            continue

        if ":" in line and not line.startswith(" "):
            if current_list is not None:
                result[current_key] = current_list
                current_list = None

            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()

            if value == "":
                current_key = key
                current_list = []
            elif value.startswith("["):
                # Inline array
                items = value.strip("[]").split(",")
                result[key] = [i.strip().strip('"').strip("'") for i in items if i.strip()]
                current_key = None
            else:
                result[key] = value.strip('"').strip("'")
                current_key = None

    if current_list is not None and current_key:
        result[current_key] = current_list

    return result


def list_entries() -> dict[str, list[str]]:
    """Return all available entry IDs grouped by axis."""
    available = {}
    for axis, axis_path in AXES.items():
        if not axis_path.exists():
            available[axis] = []
            continue
        available[axis] = sorted([
            d.name for d in axis_path.iterdir()
            if d.is_dir() and (d / "ENTRY.md").exists()
        ])
    return available


def compose_instruction(
    voice: str | None = None,
    tone: str | None = None,
    style: str | None = None,
    fmt: str | None = None,
    topic: str | None = None,
    audience: str | None = None,
) -> str:
    """Compose a writing instruction from entry IDs."""
    parts = []
    errors = []

    selections = [("voice", voice), ("tone", tone), ("style", style), ("format", fmt)]

    for axis, entry_id in selections:
        if entry_id is None:
            continue
        entry = load_entry(axis, entry_id)
        if entry is None:
            errors.append(f"Entry not found: {axis}/{entry_id}")
            continue
        phrasing = entry.get("llm_instruction_phrasing", "")
        if phrasing:
            parts.append(phrasing)

    if errors:
        return "Errors:\n" + "\n".join(f"  - {e}" for e in errors)

    if not parts:
        return "No entries selected. Use --list to see available entries."

    instruction = "\n\n".join(parts)

    if topic:
        instruction += f"\n\nWrite about: {topic}"
    if audience:
        instruction += f"\n\nAudience: {audience}"

    return instruction


def main():
    parser = argparse.ArgumentParser(
        description="Compose a writing instruction from taxonomy entry IDs."
    )
    parser.add_argument("--voice", help="Voice entry ID")
    parser.add_argument("--tone", help="Tone entry ID")
    parser.add_argument("--style", help="Style entry ID")
    parser.add_argument("--format", dest="fmt", help="Format entry ID")
    parser.add_argument("--topic", help="Topic to write about")
    parser.add_argument("--audience", help="Intended audience")
    parser.add_argument("--list", action="store_true", help="List all available entries")
    parser.add_argument("--json", dest="output_json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.list:
        available = list_entries()
        if args.output_json:
            print(json.dumps(available, indent=2))
        else:
            for axis, entries in available.items():
                print(f"\n{axis.upper()}")
                if entries:
                    for e in entries:
                        print(f"  {e}")
                else:
                    print("  (no entries yet)")
        return

    result = compose_instruction(
        voice=args.voice,
        tone=args.tone,
        style=args.style,
        fmt=args.fmt,
        topic=args.topic,
        audience=args.audience,
    )
    print(result)


if __name__ == "__main__":
    main()

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
    """Parse simple YAML frontmatter sufficient for taxonomy entry files.

    Handles: scalar key-value, multi-line lists (  - item), and YAML
    block scalars (> folded and | literal) for multi-line string fields.
    """
    result = {}
    current_key = None
    current_list = None
    block_key = None
    block_lines = []
    block_style = None  # ">" or "|"

    def flush_block():
        nonlocal block_key, block_lines, block_style
        if block_key is None:
            return
        if block_style == "|":
            result[block_key] = "\n".join(block_lines).strip()
        else:  # ">" folded: join with space, collapse newlines
            result[block_key] = " ".join(line for line in block_lines if line).strip()
        block_key = None
        block_lines = []
        block_style = None

    def flush_list():
        nonlocal current_key, current_list
        if current_list is not None and current_key is not None:
            result[current_key] = current_list
        current_key = None
        current_list = None

    for line in text.split("\n"):
        # Inside a block scalar: collect indented lines
        if block_key is not None:
            if line.startswith("  ") or (line.strip() == "" and block_lines):
                block_lines.append(line.strip())
                continue
            else:
                # Block ended
                flush_block()
                # Fall through to process this line normally

        # Inside a list: collect list items
        if current_list is not None and line.startswith("  - "):
            current_list.append(line[4:].strip())
            continue

        # Blank line: flush pending state
        if not line.strip():
            if current_list is not None:
                flush_list()
            continue

        # Top-level key
        if ":" in line and not line.startswith(" "):
            flush_list()
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()

            if value in (">", "|"):
                block_key = key
                block_style = value
                block_lines = []
            elif value == "":
                current_key = key
                current_list = []
            elif value.startswith("["):
                items = value.strip("[]").split(",")
                result[key] = [i.strip().strip('"').strip("'") for i in items if i.strip()]
            else:
                result[key] = value.strip('"').strip("'")

    # Flush any pending state at end
    flush_block()
    flush_list()

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

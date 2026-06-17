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

    import re
    parts = re.split(r"(?m)^---[ \t]*$", content, maxsplit=2)
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
                str_val = value.strip('"').strip("'")
                # Coerce to numeric types if applicable
                if str_val.lstrip('-').isdigit():
                    result[key] = int(str_val)
                elif str_val.replace('.', '', 1).lstrip('-').isdigit() and str_val.count('.') == 1:
                    result[key] = float(str_val)
                else:
                    result[key] = str_val

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


def analyze_relationships(selections: list[dict]) -> dict:
    """Cross-check the selected entries' relationship fields.

    `selections` is a list of {"axis", "id", "entry"} dicts. Conflicts use a
    symmetric (union) rule per decision B1: a pair is flagged if EITHER entry
    lists the other in `avoid_with`, so a conflict never depends on which
    author recorded the link. Returns {"conflicts": [...], "affirmations": [...]}.
    """
    conflicts = []
    affirmations = []
    items = [(s["axis"], s["id"], s.get("entry") or {}) for s in selections]
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            a_axis, a_id, a_entry = items[i]
            b_axis, b_id, b_entry = items[j]
            pair = {"a": a_id, "a_axis": a_axis, "b": b_id, "b_axis": b_axis}
            a_avoid = a_entry.get("avoid_with") or []
            b_avoid = b_entry.get("avoid_with") or []
            if b_id in a_avoid or a_id in b_avoid:
                conflicts.append(pair)
            a_pairs = a_entry.get("pairs_well_with") or []
            b_pairs = b_entry.get("pairs_well_with") or []
            if b_id in a_pairs or a_id in b_pairs:
                affirmations.append(pair)
    return {"conflicts": conflicts, "affirmations": affirmations}


def resolve_selections(
    voice: str | None = None,
    tone: str | None = None,
    style: str | None = None,
    fmt: str | None = None,
) -> list[dict]:
    """Resolve selected entry IDs into loaded entries, in the canonical
    voice -> tone -> style -> format precedence order regardless of the order
    the arguments were passed. A not-found entry is kept with entry=None so the
    caller can report it.
    """
    spec = [("voice", voice), ("tone", tone), ("style", style), ("format", fmt)]
    resolved = []
    for axis, entry_id in spec:
        if entry_id is None:
            continue
        resolved.append(
            {"axis": axis, "id": entry_id, "entry": load_entry(axis, entry_id)}
        )
    return resolved


def compose_report(
    voice: str | None = None,
    tone: str | None = None,
    style: str | None = None,
    fmt: str | None = None,
    topic: str | None = None,
    audience: str | None = None,
) -> dict:
    """Compose the instruction AND analyze the selected entries' relationships.

    Returns {"instruction", "conflicts", "affirmations", "errors"}. Conflicts
    are surfaced as warnings (decision B2: warn, never block), so the full
    instruction still composes even when a selected pair conflicts.
    """
    resolved = resolve_selections(voice, tone, style, fmt)
    parts = []
    errors = []
    found = []

    for sel in resolved:
        if sel["entry"] is None:
            errors.append(f"Entry not found: {sel['axis']}/{sel['id']}")
            continue
        found.append(sel)
        phrasing = sel["entry"].get("llm_instruction_phrasing", "")
        if phrasing:
            parts.append(phrasing)

    if errors:
        return {
            "instruction": "Errors:\n" + "\n".join(f"  - {e}" for e in errors),
            "conflicts": [],
            "affirmations": [],
            "errors": errors,
        }

    if not parts:
        return {
            "instruction": "No entries selected. Use --list to see available entries.",
            "conflicts": [],
            "affirmations": [],
            "errors": [],
        }

    instruction = "\n\n".join(parts)
    if topic:
        instruction += f"\n\nWrite about: {topic}"
    if audience:
        instruction += f"\n\nAudience: {audience}"

    analysis = analyze_relationships(found)
    return {
        "instruction": instruction,
        "conflicts": analysis["conflicts"],
        "affirmations": analysis["affirmations"],
        "errors": [],
    }


def compose_instruction(
    voice: str | None = None,
    tone: str | None = None,
    style: str | None = None,
    fmt: str | None = None,
    topic: str | None = None,
    audience: str | None = None,
) -> str:
    """Compose a writing instruction from entry IDs (string form).

    Thin wrapper over compose_report for backward compatibility; callers that
    need the conflict / affirmation report should call compose_report directly.
    """
    return compose_report(
        voice=voice, tone=tone, style=style, fmt=fmt, topic=topic, audience=audience
    )["instruction"]


def _print_relationship_notes(report: dict) -> None:
    """Surface conflicts and affirmations to stderr so stdout stays the clean,
    pipeable instruction. Conflicts warn but never block (decision B2)."""
    for c in report.get("conflicts", []):
        print(
            f"warning: conflict - {c['a']} ({c['a_axis']}) and {c['b']} "
            f"({c['b_axis']}) are marked avoid_with. Composing anyway with "
            f"voice -> tone -> style -> format precedence; expect tension.",
            file=sys.stderr,
        )
    for a in report.get("affirmations", []):
        print(
            f"note: {a['a']} ({a['a_axis']}) and {a['b']} ({a['b_axis']}) "
            f"pair well together.",
            file=sys.stderr,
        )


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

    report = compose_report(
        voice=args.voice,
        tone=args.tone,
        style=args.style,
        fmt=args.fmt,
        topic=args.topic,
        audience=args.audience,
    )
    print(report["instruction"])
    _print_relationship_notes(report)


if __name__ == "__main__":
    main()

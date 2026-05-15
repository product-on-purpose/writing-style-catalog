#!/usr/bin/env python3
"""
Generate a diff-pair file from two existing vertical-slice examples.

A diff-pair shows two examples that vary on exactly one axis, holding the
other axes (and topic) constant. The output is a single Markdown file that
places both examples side-by-side with brief commentary on what the swap
teaches.

The generator reads the two source example files, validates that they
match on topic and differ only on the named axis, pulls one-liners from
the corresponding entry frontmatter, and assembles a comparison artifact.

Usage:
    python tools/diff-pair-generator.py --topic <topic-slug> \
        --axis <voice|tone|style|format> --a <id_a> --b <id_b>

Example:
    python tools/diff-pair-generator.py --topic async-standups \
        --axis voice --a pragmatic-architect --b pastoral
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate import _extract_frontmatter, AXES, REPO_ROOT  # noqa: E402

EXAMPLES_DIR = REPO_ROOT / "examples"
DIFF_PAIRS_DIR = EXAMPLES_DIR / "diff-pairs"
VERTICAL_SLICES_DIR = EXAMPLES_DIR / "vertical-slices"


def load_example(topic: str, axis: str, entry_id: str) -> tuple[dict, str]:
    """Return (frontmatter, body) for the vertical-slice example file."""
    path = VERTICAL_SLICES_DIR / topic / f"{axis}-{entry_id}.md"
    if not path.exists():
        raise FileNotFoundError(f"Example not found: {path.relative_to(REPO_ROOT)}")

    text = path.read_text(encoding="utf-8")
    fm = _extract_frontmatter(path)
    if fm is None:
        raise ValueError(f"Could not parse frontmatter: {path.relative_to(REPO_ROOT)}")

    parts = text.split("---", 2)
    body = parts[2].strip() if len(parts) >= 3 else ""
    return fm, body


def load_entry_one_liner(axis: str, entry_id: str) -> str:
    """Return the entry's one_liner field, or an empty string if not found."""
    entry_dir = AXES.get(axis)
    if entry_dir is None:
        return ""
    entry_path = entry_dir / entry_id / "ENTRY.md"
    if not entry_path.exists():
        return ""
    fm = _extract_frontmatter(entry_path)
    if fm is None:
        return ""
    return fm.get("one_liner", "")


def build_diff_pair(topic: str, axis: str, a: str, b: str) -> str:
    fm_a, body_a = load_example(topic, axis, a)
    fm_b, body_b = load_example(topic, axis, b)

    topic_label = fm_a.get("topic_label", topic)
    if fm_b.get("topic_label", "") != topic_label:
        print(
            f"[WARN] topic_label mismatch: '{fm_a.get('topic_label')}' vs '{fm_b.get('topic_label')}'",
            file=sys.stderr,
        )

    one_liner_a = load_entry_one_liner(axis, a)
    one_liner_b = load_entry_one_liner(axis, b)

    axis_label = axis.title()

    lines = [
        "---",
        f"diff_pair_id: {axis}-{a}-vs-{b}-{topic}",
        f"topic_slug: {topic}",
        f"topic_label: {topic_label}",
        f"axis_varied: {axis}",
        f"entry_a: {a}",
        f"entry_b: {b}",
        "generator: tools/diff-pair-generator.py",
        "review_status: reviewed",
        "---",
        "",
        f"# Diff Pair: {axis_label} swap - `{a}` vs `{b}`",
        "",
        f"**Topic:** {topic_label}",
        f"**Axis varied:** {axis}",
        f"**A:** `{a}` - {one_liner_a}",
        f"**B:** `{b}` - {one_liner_b}",
        "",
        "## What to notice",
        "",
        f"Both examples address the same topic and (by default) share every axis other than {axis}. ",
        f"The only deliberate variable is which {axis} the writing was rendered through. Read both ",
        "and ask: where does the framing change? Where does the vocabulary change? What does the ",
        f"reader take away from A that they would not take away from B, and vice versa? The {axis} ",
        "swap is the entire cause of those differences.",
        "",
        "---",
        "",
        f"## A: `{a}`",
        "",
        body_a,
        "",
        "---",
        "",
        f"## B: `{b}`",
        "",
        body_b,
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0])
    parser.add_argument("--topic", required=True, help="Anchor topic slug (e.g., async-standups)")
    parser.add_argument(
        "--axis",
        required=True,
        choices=["voice", "tone", "style", "format"],
        help="The axis that varies between A and B",
    )
    parser.add_argument("--a", required=True, help="Entry ID of the A side")
    parser.add_argument("--b", required=True, help="Entry ID of the B side")
    parser.add_argument(
        "--output",
        help="Output path (default: examples/diff-pairs/<topic>/<axis>-<a>-vs-<b>.md)",
    )
    args = parser.parse_args()

    if args.a == args.b:
        print(f"[ERROR] A and B must differ (got '{args.a}' for both)", file=sys.stderr)
        return 1

    try:
        content = build_diff_pair(args.topic, args.axis, args.a, args.b)
    except (FileNotFoundError, ValueError) as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1

    if args.output:
        out_path = Path(args.output)
    else:
        out_dir = DIFF_PAIRS_DIR / args.topic
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{args.axis}-{args.a}-vs-{args.b}.md"

    out_path.write_text(content, encoding="utf-8")
    print(f"[OK] Wrote {out_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

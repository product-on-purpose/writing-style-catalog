#!/usr/bin/env python3
"""Promote draft catalog entries to stable, safely and atomically.

WHAT
    Flips one or more entries from `review_status: draft` to `review_status: stable`,
    but ONLY when every entry being promoted already renders on all 12 anchor topics.
    If any requested entry is missing samples, it flips NOTHING and reports exactly
    what is missing.

WHY IT MATTERS
    A stable entry must render on all 12 anchor topics - the Gate 2 sample-count rule
    enforced by tools/validate.py. Flip an entry to stable with fewer than 12 samples
    and `validate.py` fails (a red main). Promoting by hand is therefore error-prone:
    you must render first, then flip, and never half-promote. This script makes that
    safe - it is the guardrail that turns "promote a wave" into a one-liner that cannot
    leave the catalog in a red state.

HOW IT WORKS
    For each id it finds taxonomy/<axis>/<id>/ENTRY.md, reads the entry's `axis` and
    `review_status` from frontmatter, and checks that
    examples/vertical-slices/<topic>/<axis>-<id>.md exists for all 12 topics in
    tools/anchor_topics.seed_pool(). It promotes only if ALL requested entries pass;
    otherwise it exits non-zero having changed nothing. The flip preserves the file's
    existing newlines (it does not rewrite line endings).

    Render the missing samples first with the tools/agentic/promote.js workflow, then
    re-run this. See tools/agentic/README.md and
    docs/internal/release-plans/promotion-and-release-runbook.md.

USAGE
    python tools/promote.py rfc postmortem retrospective   # promote these (all must be ready)
    python tools/promote.py --check rfc postmortem         # dry run: report readiness, change nothing
    python tools/promote.py --all-ready                    # promote every draft entry that is fully rendered
    python tools/promote.py --all-ready --check            # report which drafts are promotion-ready

EXIT CODES
    0  promotion applied (or, with --check, all named entries are ready)
    1  nothing promoted: a requested entry was missing samples, not a draft, or not found
"""
from __future__ import annotations

import argparse
import glob
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import anchor_topics  # noqa: E402

VSLICES = ROOT / "examples" / "vertical-slices"

# Frontmatter is the block between the opening and the FIRST closing `---` that
# sits at column 0. A `---` indented inside a block scalar (description: |,
# canonical_template: |) does not match, so fields that come after a block scalar
# - notably review_status, the last field - are read correctly. We parse with
# pyyaml to match the validator (ADR 0012), not a hand-rolled line scan.
_FRONTMATTER = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def find_entry(entry_id: str) -> Path | None:
    """Locate taxonomy/<axis>/<id>/ENTRY.md for an id (unique across axes)."""
    matches = glob.glob(str(ROOT / "taxonomy" / "*" / entry_id / "ENTRY.md"))
    return Path(matches[0]) if matches else None


def parse_frontmatter(path: Path) -> dict:
    """Parse the ENTRY.md frontmatter block into a dict (empty if malformed)."""
    match = _FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        return {}
    data = yaml.safe_load(match.group(1))
    return data if isinstance(data, dict) else {}


def missing_samples(axis: str, entry_id: str) -> list[str]:
    """Anchor topics on which this entry does NOT yet have a vertical-slice sample."""
    return [
        topic
        for topic in anchor_topics.seed_pool()
        if not (VSLICES / topic / f"{axis}-{entry_id}.md").is_file()
    ]


def readiness(entry_id: str) -> tuple[str, str | None, list[str] | None]:
    """(status, axis, missing) where status is one of:
    not_found | not_draft | ready | incomplete."""
    path = find_entry(entry_id)
    if path is None:
        return ("not_found", None, None)
    fm = parse_frontmatter(path)
    axis = fm.get("axis")
    if fm.get("review_status") != "draft":
        return ("not_draft", axis, None)
    missing = missing_samples(axis, entry_id) if axis else None
    return ("ready" if not missing else "incomplete", axis, missing)


def flip_to_stable(entry_id: str) -> None:
    """Flip the first `review_status: draft` to stable, preserving newlines."""
    path = find_entry(entry_id)
    text = path.read_text(encoding="utf-8")
    text = text.replace("review_status: draft", "review_status: stable", 1)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def all_draft_ids() -> list[str]:
    """Every entry id currently at review_status: draft, across all axes."""
    ids = []
    for entry in glob.glob(str(ROOT / "taxonomy" / "*" / "*" / "ENTRY.md")):
        path = Path(entry)
        if parse_frontmatter(path).get("review_status") == "draft":
            ids.append(path.parent.name)
    return sorted(ids)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Promote fully-rendered draft entries to stable, atomically."
    )
    parser.add_argument("ids", nargs="*", help="entry ids to promote")
    parser.add_argument(
        "--all-ready",
        action="store_true",
        help="promote every draft entry that already renders on all 12 anchor topics",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="dry run: report readiness and change nothing",
    )
    args = parser.parse_args()

    if args.all_ready:
        candidates = all_draft_ids()
        ids = [i for i in candidates if readiness(i)[0] == "ready"]
        not_ready = [i for i in candidates if readiness(i)[0] == "incomplete"]
        if not_ready:
            print(f"[skip] {len(not_ready)} draft(s) not yet fully rendered: "
                  f"{', '.join(not_ready)}")
        if not ids:
            print("[promote] no draft entry is fully rendered; nothing to do.")
            return 0
    else:
        ids = args.ids
        if not ids:
            parser.error("give entry ids, or use --all-ready")

    blockers = []
    plan = []
    for entry_id in ids:
        status, axis, missing = readiness(entry_id)
        if status == "not_found":
            blockers.append(f"  [not found] {entry_id}: no taxonomy/*/{entry_id}/ENTRY.md")
        elif status == "not_draft":
            blockers.append(f"  [not draft] {entry_id}: review_status is not 'draft'")
        elif status == "incomplete":
            blockers.append(
                f"  [incomplete] {axis} '{entry_id}': missing {len(missing)}/12 "
                f"sample(s): {', '.join(missing)}"
            )
        else:
            plan.append((entry_id, axis))

    if blockers:
        print("Cannot promote - nothing was changed:")
        print("\n".join(blockers))
        print("\nRender the missing samples first (tools/agentic/promote.js), then re-run.")
        return 1

    if args.check:
        print(f"[check] all {len(plan)} entr{'y' if len(plan) == 1 else 'ies'} "
              f"ready to promote: {', '.join(i for i, _ in plan)}")
        return 0

    for entry_id, axis in plan:
        flip_to_stable(entry_id)
        print(f"[promoted] {axis} '{entry_id}' -> stable")
    print(f"\nPromoted {len(plan)}. Now: rebuild indexes, bump counters + manifests, "
          f"run validate.py (Gate 2 active), build the site, and open a PR.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

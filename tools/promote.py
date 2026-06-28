#!/usr/bin/env python3
"""Promote draft catalog entries to stable, with a transactional, guarded flip.

WHAT
    Flips one or more entries from `review_status: draft` to `review_status: stable`,
    but ONLY when every entry being promoted already renders on all 12 anchor topics.
    If any requested entry is missing samples (or fails any preflight check), it writes
    NOTHING and reports exactly what is wrong.

WHY IT MATTERS
    A stable entry must render on all 12 anchor topics - the Gate 2 sample-count rule
    enforced by tools/validate.py. Flip an entry to stable with fewer than 12 samples
    and `validate.py` fails (a red main). Promoting by hand is therefore error-prone:
    you must render first, then flip, and never half-promote. This script makes that
    safe: it validates everything first, stages every rewrite in memory, then writes
    all files - and if any write fails, it rolls the already-written files back. So a
    promotion either fully applies or leaves the tree exactly as it found it.

HOW IT WORKS
    Preflight, for each id: find the unique taxonomy/<axis>/<id>/ENTRY.md (a duplicate
    id across axes is an error, not a silent first-match); read `axis` and
    `review_status` from frontmatter (parsed with pyyaml, ADR 0012); confirm it is a
    draft; confirm examples/vertical-slices/<topic>/<axis>-<id>.md exists for all 12
    topics in tools/anchor_topics.seed_pool(); and confirm the frontmatter contains
    exactly one column-0 `review_status: draft` line (so the flip cannot hit a lookalike
    inside a block scalar). Only if ALL entries pass does it write - staged content,
    newlines preserved, with rollback on any failure.

    Render the missing samples first with the tools/agentic/promote.js workflow, then
    re-run this. See tools/agentic/README.md and
    docs/internal/release-plans/promotion-and-release-runbook.md.

USAGE
    python tools/promote.py rfc postmortem retrospective   # promote these (all must pass)
    python tools/promote.py --check rfc postmortem         # dry run: report readiness, write nothing
    python tools/promote.py --all-ready                    # promote every draft that is fully rendered
    python tools/promote.py --all-ready --check            # report which drafts are promotion-ready

EXIT CODES
    0  the write succeeded; OR --check ran and every named/ready entry is promotable
       (including the benign --all-ready case where nothing is ready yet)
    1  a requested entry was missing samples, not a draft, not found, a duplicate id, or
       had an ambiguous frontmatter; OR a write failed and was rolled back. Nothing was
       left changed.
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

# Frontmatter is the block between the opening and the FIRST closing `---` at column
# 0. A `---` indented inside a block scalar does not match, so fields after a block
# scalar - notably review_status, the last field - are read correctly. Parsed with
# pyyaml to match the validator (ADR 0012).
_FRONTMATTER = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
# A column-0 `review_status: draft` line (the real field; not an indented lookalike).
# The trailing group preserves a CR so CRLF files are not reflowed to LF.
_DRAFT_LINE = re.compile(r"(?m)^review_status: draft[ \t]*(\r?)$")


def find_paths(entry_id: str) -> list[Path]:
    """All taxonomy/<axis>/<id>/ENTRY.md matching an id (should be exactly one)."""
    return [Path(p) for p in glob.glob(str(ROOT / "taxonomy" / "*" / entry_id / "ENTRY.md"))]


def parse_frontmatter(path: Path) -> dict:
    """Parse the ENTRY.md frontmatter block into a dict (empty if malformed)."""
    match = _FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        return {}
    data = yaml.safe_load(match.group(1))
    return data if isinstance(data, dict) else {}


def missing_samples(axis: str, entry_id: str) -> list[str]:
    """Anchor topics on which this entry has no vertical-slice sample yet."""
    return [
        topic
        for topic in anchor_topics.seed_pool()
        if not (VSLICES / topic / f"{axis}-{entry_id}.md").is_file()
    ]


def flip_text(text: str) -> str:
    """Return `text` with the frontmatter's review_status flipped draft -> stable.

    Raises ValueError unless the frontmatter contains exactly one column-0
    `review_status: draft` line. Newlines (including CRLF) are preserved.
    """
    match = _FRONTMATTER.match(text)
    if not match:
        raise ValueError("no frontmatter block")
    fm_start, fm_end = match.start(1), match.end(1)
    frontmatter = text[fm_start:fm_end]
    hits = _DRAFT_LINE.findall(frontmatter)
    if len(hits) != 1:
        raise ValueError(
            f"expected exactly one column-0 'review_status: draft' line in the "
            f"frontmatter, found {len(hits)}"
        )
    new_fm = _DRAFT_LINE.sub(lambda m: "review_status: stable" + m.group(1), frontmatter)
    return text[:fm_start] + new_fm + text[fm_end:]


def preflight(entry_id: str) -> tuple[str, str | None]:
    """(status, detail) for one id. status is one of:
    not_found | duplicate | not_draft | incomplete | ambiguous | ready.
    detail carries the human-readable reason for the non-ready statuses."""
    paths = find_paths(entry_id)
    if not paths:
        return ("not_found", f"no taxonomy/*/{entry_id}/ENTRY.md")
    if len(paths) > 1:
        return ("duplicate", "id resolves to multiple files: "
                + ", ".join(str(p.relative_to(ROOT)) for p in paths))
    path = paths[0]
    fm = parse_frontmatter(path)
    axis = fm.get("axis")
    if fm.get("review_status") != "draft":
        return ("not_draft", "review_status is not 'draft'")
    if not axis:
        return ("ambiguous", "frontmatter has no 'axis'")
    missing = missing_samples(axis, entry_id)
    if missing:
        return ("incomplete", f"missing {len(missing)}/12 sample(s): {', '.join(missing)}")
    try:
        flip_text(path.read_text(encoding="utf-8"))
    except ValueError as exc:
        return ("ambiguous", str(exc))
    return ("ready", axis)


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
        description="Promote fully-rendered draft entries to stable, transactionally."
    )
    parser.add_argument("ids", nargs="*", help="entry ids to promote")
    parser.add_argument("--all-ready", action="store_true",
                        help="promote every draft entry that already renders on all 12 anchor topics")
    parser.add_argument("--check", action="store_true",
                        help="dry run: report readiness and write nothing")
    args = parser.parse_args()

    if args.all_ready:
        results = {i: preflight(i) for i in all_draft_ids()}
        ids = [i for i, (status, _) in results.items() if status == "ready"]
        not_ready = [i for i, (status, _) in results.items() if status != "ready"]
        if not_ready:
            print(f"[check] {len(not_ready)} draft(s) not yet promotable: {', '.join(not_ready)}")
        if not ids:
            print("[check] no draft entry is fully rendered; nothing to promote.")
            return 0
    else:
        ids = args.ids
        if not ids:
            parser.error("give entry ids, or use --all-ready")

    blockers = []
    plan = []  # (entry_id, axis, path)
    for entry_id in ids:
        status, detail = preflight(entry_id)
        if status == "ready":
            plan.append((entry_id, detail, find_paths(entry_id)[0]))
        else:
            blockers.append(f"  [{status}] {entry_id}: {detail}")

    if blockers:
        print("Cannot promote - nothing was changed:")
        print("\n".join(blockers))
        print("\nRender the missing samples first (tools/agentic/promote.js), then re-run.")
        return 1

    if args.check:
        print(f"[check] all {len(plan)} entr{'y' if len(plan) == 1 else 'ies'} "
              f"ready to promote: {', '.join(i for i, _, _ in plan)}")
        return 0

    # Stage every rewrite in memory before touching disk.
    staged = []  # (path, original_text, new_text, entry_id, axis)
    for entry_id, axis, path in plan:
        original = path.read_text(encoding="utf-8")
        staged.append((path, original, flip_text(original), entry_id, axis))

    # Write all; roll back every written file if any write fails.
    written = []  # (path, original_text)
    try:
        for path, original, new_text, entry_id, axis in staged:
            with open(path, "w", encoding="utf-8", newline="") as handle:
                handle.write(new_text)
            written.append((path, original))
            print(f"[promoted] {axis} '{entry_id}' -> stable")
    except OSError as exc:
        for path, original in reversed(written):
            with open(path, "w", encoding="utf-8", newline="") as handle:
                handle.write(original)
        print(f"\n[error] write failed ({exc}); rolled back {len(written)} file(s). "
              f"Nothing was promoted.")
        return 1

    print(f"\nPromoted {len(plan)}. Now: rebuild indexes, bump counters + manifests, "
          f"run validate.py (Gate 2 active), build the site, and open a PR.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
Build taxonomy.json and coverage.json from all ENTRY.md files.

taxonomy.json is the machine-readable index consumed by skills and the Composer.
coverage.json is the per-cell coverage ledger (ADR 0010 section 6): for every
domain/family cell it reports the target band and the filled count, plus the
count of entries not yet assigned a family (the pre-backfill state). The ledger
is a report, not a gate.

The human-readable reference index (site/src/content/docs/reference/index.md) is
owned by the Starlight generator (scripts/gen-site.mjs); this tool no longer
writes it.

Requirements: none beyond stdlib (shares validate.py's _extract_frontmatter).

Usage:
    python tools/build-indexes.py
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Import shared parser and constants from validate.py in the same directory,
# and the controlled vocabulary (single-sourced in taxonomy.py per ADR 0010).
sys.path.insert(0, str(Path(__file__).parent))
from validate import _extract_frontmatter, AXES, REPO_ROOT  # noqa: E402
import taxonomy  # noqa: E402

TAXONOMY_JSON = REPO_ROOT / "taxonomy.json"
COVERAGE_JSON = REPO_ROOT / "coverage.json"

AXIS_ORDER = ["voice", "tone", "style", "format"]

# Fields written to taxonomy.json. The collector gathers more (domain/family/
# subfamily) for the coverage ledger, but taxonomy.json stays this slim set so
# adding the taxonomy fields does not churn the index.
INDEX_FIELDS = ("id", "name", "axis", "one_liner", "review_status")


def collect_entries() -> list[dict]:
    entries = []
    for axis in AXIS_ORDER:
        axis_path = AXES.get(axis)
        if not axis_path or not axis_path.exists():
            continue
        for entry_dir in sorted(axis_path.iterdir()):
            if not entry_dir.is_dir():
                continue
            entry_md = entry_dir / "ENTRY.md"
            if not entry_md.exists():
                continue
            fm = _extract_frontmatter(entry_md)
            if not fm:
                print(
                    f"[WARN] Could not parse frontmatter: {entry_md.relative_to(REPO_ROOT)}",
                    file=sys.stderr,
                )
                continue
            entries.append(
                {
                    "id": fm.get("id", entry_dir.name),
                    "name": fm.get("name", entry_dir.name),
                    "axis": fm.get("axis", axis),
                    "one_liner": fm.get("one_liner", ""),
                    "review_status": fm.get("review_status", ""),
                    # Taxonomy fields (optional until backfill) - ledger only.
                    "domain": fm.get("domain"),
                    "family": fm.get("family"),
                    "subfamily": fm.get("subfamily"),
                }
            )
    return entries


def build_taxonomy_json(entries: list[dict]) -> None:
    slim = [{k: e.get(k, "") for k in INDEX_FIELDS} for e in entries]

    # Preserve the existing timestamp if entries are unchanged so that CI
    # staleness checks (git diff --exit-code) don't fail on every run.
    preserved_ts = None
    if TAXONOMY_JSON.exists():
        try:
            existing = json.loads(TAXONOMY_JSON.read_text(encoding="utf-8"))
            if existing.get("entries") == slim:
                preserved_ts = existing.get("generated")
        except Exception:
            pass

    payload = {
        "generated": preserved_ts or datetime.now(timezone.utc).isoformat(),
        "entries": slim,
    }
    TAXONOMY_JSON.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"[OK] Wrote {TAXONOMY_JSON.relative_to(REPO_ROOT)} ({len(slim)} entries)")


def build_coverage_ledger(entries: list[dict]) -> dict:
    """Build the per-cell coverage ledger from collected entries.

    Returns format cells (one per domain/family pair) and voice families, each
    with its target band and filled count, plus the count of format/voice
    entries not yet assigned a family.
    """
    format_counts: dict[tuple[str, str], int] = {}
    voice_counts: dict[str, int] = {}
    unassigned = {"format": 0, "voice": 0}

    for e in entries:
        axis = e.get("axis")
        if axis == "format":
            domain, family = e.get("domain"), e.get("family")
            if domain and family:
                format_counts[(domain, family)] = format_counts.get((domain, family), 0) + 1
            else:
                unassigned["format"] += 1
        elif axis == "voice":
            family = e.get("family")
            if family:
                voice_counts[family] = voice_counts.get(family, 0) + 1
            else:
                unassigned["voice"] += 1

    format_cells = []
    for domain in taxonomy.FORMAT_DOMAINS:
        for family in taxonomy.FORMAT_FAMILIES_BY_DOMAIN[domain]:
            lo, hi = taxonomy.coverage_band(family)
            format_cells.append(
                {
                    "domain": domain,
                    "family": family,
                    "target_min": lo,
                    "target_max": hi,
                    "filled": format_counts.get((domain, family), 0),
                }
            )

    voice_families = []
    for family in taxonomy.VOICE_FAMILIES:
        lo, hi = taxonomy.coverage_band(family)
        voice_families.append(
            {
                "family": family,
                "target_min": lo,
                "target_max": hi,
                "filled": voice_counts.get(family, 0),
            }
        )

    return {
        "format_cells": format_cells,
        "voice_families": voice_families,
        "unassigned": unassigned,
    }


def build_coverage_json(entries: list[dict]) -> None:
    """Write the coverage ledger to coverage.json.

    Deterministic (no timestamp): re-runs produce identical output unless the
    entries change, so CI staleness checks stay clean.
    """
    ledger = build_coverage_ledger(entries)
    COVERAGE_JSON.write_text(
        json.dumps(ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    assigned = sum(c["filled"] for c in ledger["format_cells"]) + sum(
        f["filled"] for f in ledger["voice_families"]
    )
    print(
        f"[OK] Wrote {COVERAGE_JSON.relative_to(REPO_ROOT)} "
        f"({assigned} assigned, "
        f"{ledger['unassigned']['format'] + ledger['unassigned']['voice']} unassigned)"
    )


def main() -> int:
    entries = collect_entries()
    if not entries:
        print("[WARN] No entries found - output will be empty", file=sys.stderr)
    build_taxonomy_json(entries)
    build_coverage_json(entries)
    return 0


if __name__ == "__main__":
    sys.exit(main())

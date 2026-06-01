#!/usr/bin/env python3
"""
Build taxonomy.json from all ENTRY.md files.

taxonomy.json is the machine-readable index consumed by skills and the Composer.
The human-readable reference index (docs/reference/index.md) is owned by the
Starlight generator (scripts/generate_site_pages.py); this tool no longer writes it.

Requirements: none beyond stdlib (shares validate.py's _extract_frontmatter).

Usage:
    python tools/build-indexes.py
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Import shared parser and constants from validate.py in the same directory
sys.path.insert(0, str(Path(__file__).parent))
from validate import _extract_frontmatter, AXES, REPO_ROOT  # noqa: E402

TAXONOMY_JSON = REPO_ROOT / "taxonomy.json"

AXIS_ORDER = ["voice", "tone", "style", "format"]


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
                }
            )
    return entries


def build_taxonomy_json(entries: list[dict]) -> None:
    # Preserve the existing timestamp if entries are unchanged so that CI
    # staleness checks (git diff --exit-code) don't fail on every run.
    preserved_ts = None
    if TAXONOMY_JSON.exists():
        try:
            existing = json.loads(TAXONOMY_JSON.read_text(encoding="utf-8"))
            if existing.get("entries") == entries:
                preserved_ts = existing.get("generated")
        except Exception:
            pass

    payload = {
        "generated": preserved_ts or datetime.now(timezone.utc).isoformat(),
        "entries": entries,
    }
    TAXONOMY_JSON.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"[OK] Wrote {TAXONOMY_JSON.relative_to(REPO_ROOT)} ({len(entries)} entries)")


def main() -> int:
    entries = collect_entries()
    if not entries:
        print("[WARN] No entries found - output will be empty", file=sys.stderr)
    build_taxonomy_json(entries)
    return 0


if __name__ == "__main__":
    sys.exit(main())

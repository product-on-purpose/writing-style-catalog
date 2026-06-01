#!/usr/bin/env python3
"""Fail if committed generated docs pages differ from a fresh generation.

Regenerates into a temp dir and compares file-by-file against the committed
docs/ generated trees. Exit 1 on any difference (stale pages) so CI blocks.
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_site_pages as gsp  # noqa: E402


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_root = Path(tmp)
        gsp.generate(tmp_root)
        stale = []
        committed_root = gsp.DOCS
        # Compare fresh -> committed (every freshly generated file must match)
        for fresh in tmp_root.rglob("*"):
            if not fresh.is_file():
                continue
            rel = fresh.relative_to(tmp_root)
            committed = committed_root / rel
            if not committed.exists():
                stale.append(f"missing committed page: docs/{rel}")
            elif committed.read_text(encoding="utf-8").replace("\r\n", "\n") != fresh.read_text(encoding="utf-8").replace("\r\n", "\n"):
                stale.append(f"stale committed page: docs/{rel}")
    if stale:
        print("[FAIL] generated docs are stale - run: python scripts/generate_site_pages.py")
        for s in stale:
            print("  " + s)
        return 1
    print("[OK] generated docs match source")
    return 0


if __name__ == "__main__":
    sys.exit(main())

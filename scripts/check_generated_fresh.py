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
    generated_subdirs = ["reference", "examples", "recipes", "templates"]
    with tempfile.TemporaryDirectory() as tmp:
        tmp_root = Path(tmp)
        gsp.generate(tmp_root)
        committed_root = gsp.DOCS
        stale = []
        fresh_rels = set()
        # fresh -> committed: every freshly generated file must exist and match
        for fresh in tmp_root.rglob("*"):
            if not fresh.is_file():
                continue
            rel = fresh.relative_to(tmp_root)
            fresh_rels.add(rel)
            committed = committed_root / rel
            if not committed.exists():
                stale.append(f"missing committed page: docs/{rel}")
            elif committed.read_text(encoding="utf-8").replace("\r\n", "\n") != fresh.read_text(encoding="utf-8").replace("\r\n", "\n"):
                stale.append(f"stale committed page: docs/{rel}")
        # committed -> fresh: orphaned committed pages in the generated subtrees
        for sub in generated_subdirs:
            base = committed_root / sub
            if not base.exists():
                continue
            for committed in base.rglob("*"):
                if not committed.is_file():
                    continue
                rel = committed.relative_to(committed_root)
                if rel not in fresh_rels:
                    stale.append(f"orphaned committed page: docs/{rel} (source no longer generates it)")
    if stale:
        print("[FAIL] generated docs are out of sync - run: python scripts/generate_site_pages.py")
        for s in stale:
            print("  " + s)
        return 1
    print("[OK] generated docs match source")
    return 0


if __name__ == "__main__":
    sys.exit(main())

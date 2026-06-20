"""E1 adherence gate (Stage 3 of the six-stage factory).

Slice 1: the deterministic neighbor lookup. Given a candidate entry and the
catalog, compute the gate neighbor set the blind distinguishability test
(Gate 1) renders against, per the ratified taxonomy rules:

- Q4 (gate neighbor definition): a candidate is judged against its tree
  siblings AND any entry it declares in `confusable_with`, regardless of where
  that declared entry sits in the tree.
- Gate 1 (adherence-gate-spec.md): tree siblings are same-family, narrowing to
  same-subfamily once a family reaches the 12-member trigger.
- Q5 (flat axes): tone and style have no family, so they render whole-axis
  while each axis stays small (~15-30), with declared `confusable_with` as the
  priority subset.

The neighbor set is same-axis: Gate 1 is a single-axis-varied forced-choice
attribution, so a cross-axis `confusable_with` edge (which the Q6 audit already
removed from the catalog) is not a Gate-1 adversary and is excluded.

This module reuses validate.py's frontmatter parser and AXES map; it never
re-parses entries or duplicates the controlled vocabulary (tools/taxonomy.py).
"""
from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate import _iter_entries, _extract_frontmatter  # noqa: E402

# Mirrors the subfamily trigger enforced in validate.py (decision A2 / A1-Q7):
# once a family reaches this many members, subfamily becomes required and the
# gate narrows neighbors to the same subfamily.
SUBFAMILY_TRIGGER = 12


def load_catalog() -> dict[str, tuple[str, dict]]:
    """Load every entry's frontmatter into an id_map: entry_id -> (axis, fm).

    Quiet counterpart to validate.check_frontmatter_parseable: same shape, but
    no printing and no error collection. Entries whose frontmatter will not
    parse are skipped (validate.py is the place that reports those).
    """
    id_map: dict[str, tuple[str, dict]] = {}
    for axis, entry_dir in _iter_entries():
        entry_md = entry_dir / "ENTRY.md"
        if not entry_md.exists():
            continue
        try:
            fm = _extract_frontmatter(entry_md)
        except Exception:
            continue  # mirror validate.py: skip an entry that will not parse
        if fm is None:
            continue
        entry_id = fm.get("id", entry_dir.name)
        id_map[entry_id] = (axis, fm)
    return id_map


@dataclass(frozen=True)
class NeighborSet:
    """The gate neighbor set for a candidate, split by provenance.

    `siblings` are same-family (or same-subfamily past the trigger, or
    whole-axis for the flat tone/style axes) tree neighbors; `confusable` are
    the candidate's declared same-axis `confusable_with` edges. `neighbors` is
    their sorted union - the adversary set Gate 1 renders against.
    """
    candidate: str
    axis: str
    siblings: tuple[str, ...]
    confusable: tuple[str, ...]

    @property
    def neighbors(self) -> tuple[str, ...]:
        return tuple(sorted(set(self.siblings) | set(self.confusable)))


def _tree_siblings(candidate_id, axis, domain, family, subfamily, id_map):
    """Same-tree-node neighbors for the candidate's axis (Gate 1 + Q5)."""
    # Flat axes (tone, style) have no family: render whole-axis (Q5).
    if axis in ("tone", "style"):
        return {
            oid for oid, (oaxis, _fm) in id_map.items()
            if oid != candidate_id and oaxis == axis
        }

    if not family:
        return set()  # cannot compute a family-scoped set without a family

    # Same axis + same family (+ same domain for format, whose families are
    # domain-scoped). Collect members including the candidate to size the family.
    members = [
        oid for oid, (oaxis, ofm) in id_map.items()
        if oaxis == axis
        and ofm.get("family") == family
        and (axis != "format" or ofm.get("domain") == domain)
    ]

    # The trigger uses this family's full membership. For formats the count is
    # domain-scoped, but format family names are globally unique across domains
    # (enforced by taxonomy._self_check), so it equals the family total and
    # agrees with the (axis, family) count validate.py uses to enforce the same
    # 12-member subfamily rule.
    if len(members) >= SUBFAMILY_TRIGGER:
        if not subfamily:
            # Invalid catalog: validate.py errors when a 12+ member family has
            # an entry with no subfamily. Fail loud rather than render the
            # candidate against a too-broad neighbor set and emit a misleading
            # gate verdict.
            raise ValueError(
                f"{candidate_id}: family '{family}' has {len(members)} members "
                f"(>= {SUBFAMILY_TRIGGER}) but the candidate has no subfamily; "
                f"the catalog violates the subfamily rule (run tools/validate.py)."
            )
        # Past the trigger the family is subfamily-partitioned, so the gate
        # narrows to same-subfamily neighbors (Gate 1 / A2).
        members = [
            m for m in members
            if id_map[m][1].get("subfamily") == subfamily
        ]

    return {m for m in members if m != candidate_id}


def _declared_confusable(candidate_id, axis, fm, id_map):
    """The candidate's declared `confusable_with` edges, same-axis only (Q4).

    Cross-axis edges are excluded because Gate 1 is a single-axis-varied
    forced-choice attribution; the Q6 audit already removed such edges from the
    catalog. Unknown and self references are dropped defensively (validate.py is
    the check that reports unknown references).
    """
    out: set[str] = set()
    for ref in fm.get("confusable_with", []) or []:
        if not ref or ref == candidate_id:
            continue
        target = id_map.get(ref)
        if target is None or target[0] != axis:
            continue
        out.add(ref)
    return out


def gate_neighbors(candidate_id, id_map) -> NeighborSet:
    """Compute the gate neighbor set for a candidate entry."""
    axis, fm = id_map[candidate_id]
    siblings = _tree_siblings(
        candidate_id, axis, fm.get("domain"), fm.get("family"),
        fm.get("subfamily"), id_map,
    )
    confusable = _declared_confusable(candidate_id, axis, fm, id_map)
    return NeighborSet(
        candidate=candidate_id,
        axis=axis,
        siblings=tuple(sorted(siblings)),
        confusable=tuple(sorted(confusable)),
    )


# ---------------------------------------------------------------------------
# CLI - inspect a candidate's gate neighbor set
# ---------------------------------------------------------------------------

def _format_report(ns: NeighborSet) -> str:
    return "\n".join([
        f"candidate: {ns.candidate} (axis: {ns.axis})",
        f"  siblings ({len(ns.siblings)}): {', '.join(ns.siblings) or '(none)'}",
        f"  confusable ({len(ns.confusable)}): {', '.join(ns.confusable) or '(none)'}",
        f"  neighbors ({len(ns.neighbors)}): {', '.join(ns.neighbors) or '(none)'}",
    ])


def main(argv=None) -> int:
    import argparse
    parser = argparse.ArgumentParser(
        description="Inspect a candidate's gate neighbor set."
    )
    parser.add_argument("--entry", required=True, help="Entry ID to look up")
    args = parser.parse_args(argv)

    id_map = load_catalog()
    if args.entry not in id_map:
        print(f"[ERROR] unknown entry id: {args.entry}", file=sys.stderr)
        return 1
    print(_format_report(gate_neighbors(args.entry, id_map)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

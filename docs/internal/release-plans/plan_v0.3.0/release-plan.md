# v0.3.0 Expansion Foundation - Release Plan

> The executing agent OWNS and UPDATES this file. Check a box only after its acceptance check
> passes. Keep the repo green between steps. Spec: [`spec.md`](spec.md). This release builds
> the machinery for scaled expansion; it does not mass-produce content.

**Status:** Proposed - planning. **Version:** 0.3.0 (MINOR).
**Companions:** [`adherence-gate-spec.md`](adherence-gate-spec.md) (E1),
[`anchor-topics.md`](anchor-topics.md) (the 12 topics), ADR
[`0010`](../../adr/0010-domain-and-family-organization.md) (taxonomy).

---

## Phase 0 - Designs + decisions (this folder)

- [ ] ADR 0010, the adherence-gate spec, and the 12-anchor-topics proposal authored and
      internally consistent.
  - Acceptance: all three present, dash-clean, cross-referenced; reflect the v2 taxonomy (not
    the stale v1) and the scaling decision matrix.
- [ ] Maintainer answers the six decisions in `spec.md` Section 6; ADR 0010 and ADR 0009 move
      Proposed -> Accepted; ADR 0006 noted for the topic-set update.
  - Acceptance: no open P0 decision remains; the taxonomy cuts, the 12 topics, and the gate
    thresholds are locked.

## Phase 1 - Codify the taxonomy (ADR 0010)

- [ ] Rewrite `tools/taxonomy.py` to the v2 vocabulary (5 domains, 16 format families, 6 voice
      families) plus the subfamily level and the governed facet-tag enum. Remove the v1 lists.
- [ ] Add `domain` / `family` / `subfamily` enums and the faceted-tag pattern to
      `schemas/format.schema.json`, `schemas/voice.schema.json`,
      `schemas/entry.universal.schema.json` (format requires domain+family; voice requires
      family; tones/styles unchanged).
- [ ] Add `check_taxonomy_membership()` to `tools/validate.py` (family-in-domain; subfamily
      required past 12 family members; facet tags from the governed enum). Ship
      optional-with-warning.
- [ ] Add the per-cell coverage ledger to `tools/build-indexes.py`.
  - Acceptance: `python tools/validate.py` passes with the new check in warning mode;
    `tools/taxonomy.py` matches ADR 0010 exactly.

## Phase 2 - Backfill the 60 entries

- [ ] Backfill `domain` / `family` on the 15 formats and `family` on the 15 voices (+
      `subfamily` where a family already overflows 12); add faceted tags where clear.
- [ ] Tighten the validator from optional-with-warning to required for formats/voices.
  - Acceptance: all 60 entries carry valid taxonomy values; `tools/validate.py` green in
    required mode; `taxonomy.json` regenerates; coverage ledger renders.

## Phase 3 - Conflict-aware composition (S1)

- [ ] Extend `build-instruction.py` to read `avoid_with` / `pairs_well_with`, flag conflicts,
      apply voice -> tone -> style -> format precedence, and implement the locked `avoid_with`
      symmetry rule.
- [ ] Update `SKILL.md`; add tests under `tests/` (including the `pragmatic-architect` +
      `reverent` conflict case).
  - Acceptance: the conflict case warns; precedence is deterministic; tests green; existing
    valid combinations still compose.

## Phase 4 - Lock the anchor topics

- [ ] Finalize `anchor-topics.md` (12 topics, domain assignments, isolation rationale); confirm
      every domain has a native topic.
- [ ] Update ADR 0006 (anchor-topic-selection) to reference the expanded set; keep the existing
      3 topics.
  - Acceptance: topics locked; ADR 0006 amended; no domain left without a home topic.

## Phase 5 - Stand up the adherence gate (E1)

- [ ] Implement `tools/adherence-gate.py` per the spec: neighbor-set selection from the
      taxonomy tree, a cross-family judge, the three pass/fail checks, the per-entry
      distinguishability score output.
- [ ] Freeze the golden set (the 60 plus the 8/8 smoke-test pairs); wire the gate + the new
      validators into CI as a regression check.
- [ ] Finalize ADR 0009 (pedagogical bar); the gate's completeness check reads it.
  - Acceptance: the gate runs the golden set green in CI; a deliberately indistinct entry is
    rejected; the 70 percent first-pass stop floor is documented.

## Phase 6 - Close out

- [ ] Bump to 0.3.0 (plugin.json, self-hosted marketplace, README, CHANGELOG); tag + Release;
      update the agent-plugins registry pin (same flow as v0.2.0).
- [ ] Flip this plan + spec to SHIPPED; update `backlog.md` (S1, E1, the taxonomy, and the
      topics move from backlog to done); refresh memory.
  - Acceptance: v0.3.0 released; the foundation is in place; v0.4.0 (content scale) is unblocked.

---

## Sequencing notes

- **Phase 1 must precede Phase 2** (schema before backfill) and **Phase 4/5** (the gate's
  neighbor sets are defined by the taxonomy tree; loose categories produce loose gates).
- **Phase 3 (S1) is independent** of the taxonomy work and can run in parallel, but should land
  before any combinatorial enumeration in v0.4.0.
- **The gate (Phase 5) is the unlock for v0.4.0**; without it, mass content reintroduces the
  dilution risk this whole effort exists to prevent.
- This is a planning artifact. Execution begins only after the Phase 0 maintainer decisions are
  locked.

## Execution log

- (to be filled during execution)

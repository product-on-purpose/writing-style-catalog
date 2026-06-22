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
- [ ] Maintainer records the decisions in [`decisions.md`](decisions.md) (the consolidated
      decision record; the six in `spec.md` Section 6 are the P0 subset); ADR 0010 and ADR 0009
      move Proposed -> Accepted (ADR 0010 on 2026-06-19; ADR 0009 on 2026-06-20 as a gate-critical
      subset); ADR 0006 noted for the topic-set update (extended by ADR 0017).
  - Acceptance: every P0 row in `decisions.md` has a recorded maintainer call; the taxonomy
    cuts, the 12 topics, the gate thresholds, and the resourcing posture are locked.

## Phase 1 - Codify the taxonomy (ADR 0010)

- [x] Rewrite `tools/taxonomy.py` to the v2 vocabulary (5 domains, 17 format families, 5 voice
      families) plus the subfamily level and the governed facet-tag enum. Remove the v1 lists.
- [x] Add `domain` / `family` / `subfamily` enums and the faceted-tag pattern to
      `schemas/format.schema.json` and `schemas/voice.schema.json` as optional fields (the
      family/domain and facet rules are enforced by `validate.py`; `entry.universal` is
      unchanged; tones/styles unchanged).
- [x] Add `check_taxonomy_membership()` to `tools/validate.py` (family-in-domain; subfamily
      required past 12 family members; facet tags from the governed enum). Ship
      optional-with-warning.
- [x] Add the per-cell coverage ledger to `tools/build-indexes.py`.
  - Acceptance: `python tools/validate.py` passes with the new check in warning mode;
    `tools/taxonomy.py` matches ADR 0010 exactly.

## Phase 2 - Backfill the 60 entries

- [x] Backfill `domain` / `family` on the 15 formats and `family` on the 15 voices (+
      `subfamily` on `pastoral` -> `care` per the A1 fold); faceted tags deferred (none clear yet).
- [x] Tighten the validator from optional-with-warning to required for formats/voices.
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

## Phase 4 - Decide the anchor-topic model (D1) [DONE 2026-06-20, PR #32]

- [x] Finalize `anchor-topics.md` as the two-tier model (a frozen regression core plus a growable,
      optionally randomized seed pool; the 12 are the seed, not a cap); confirm every domain has a
      native topic in the seed.
- [x] Record the architecture in a new ADR (ADR 0017), extending ADR 0006 (the Phase 0 single-topic
      predecessor, kept Accepted and unchanged); keep the existing 3 topics as the frozen core.
  - Acceptance: D1 decided (decisions.md); ADR 0017 Accepted; no domain left without a home topic in
    the seed. (Met: PR #32; all 9 P0 now decided.)

## Phase 5 - Stand up the adherence gate (E1)

- [ ] Implement `tools/adherence-gate.py` per the spec: neighbor-set selection from the
      taxonomy tree, a cross-family judge, the three pass/fail checks, the per-entry
      distinguishability score output.
- [ ] Freeze the golden set (the 60 plus the 8/8 smoke-test pairs); wire the gate + the new
      validators into CI as a regression check.
- [~] Finalize ADR 0009 (pedagogical bar); the gate's completeness check reads it. ADR ratified
      2026-06-20 (gate-critical subset: `failure_modes`, `anti_patterns`, `tells`). Deterministic
      Gate 2 (pedagogical-field subset) DONE 2026-06-22: the three fields are now required in the
      universal schema (presence, count band, shape), and `check_pedagogical_bar` in
      `tools/validate.py` adds the error-level substance check (no empty/whitespace strings) the schema
      cannot express; the full catalog validates clean. Gate 2's sample-count half (12 per entry) and
      the judge-side reading (the C1 restraint check, Gate 1) still ride the model-calling gate build.
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

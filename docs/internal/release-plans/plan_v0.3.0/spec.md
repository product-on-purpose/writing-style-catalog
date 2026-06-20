# v0.3.0 Expansion Foundation - Specification

> The contract for v0.3.0. Companion [`release-plan.md`](release-plan.md) is the ordered
> execution. This release builds the MACHINERY and STRUCTURE that the aspirational ~10x
> expansion (more topics, styles, domains, and a dozen-plus samples of everything) is built
> on. It deliberately ships almost no new catalog content; it makes mass content safe to add
> later. Strategy context: [`../../scaling-the-library-100x.md`](../../scaling-the-library-100x.md)
> and [`../../backlog.md`](../../backlog.md).

**Status:** Proposed - planning (drafts for maintainer review).
**Type:** MINOR (0.2.0 -> 0.3.0).
**Theme:** Lock the taxonomy, make composition a guarantee, lock the worked-sample substrate,
and stand up the adherence gate - the four pieces that let breadth scale without diluting the
proven distinguishability result.

---

## 1. Why this release exists

The maintainer is committing to an aspirational ~10x expansion across topics, styles, and
domains, held to a best-in-class bar. The scaling strategy concluded that comprehensiveness
and quality only coexist if breadth scales BEHIND a gate, and that the binding constraint is
machinery, not appetite. v0.3.0 builds that machinery on the proven 60 entries, so that the
content-scaling releases (v0.4.0 and beyond) can add entries and samples that are provably as
distinguishable as the first 60.

Nothing here mass-produces entries. This is the foundation: a frozen taxonomy to define tight
neighbor sets, conflict-aware composition so the combinatorial space is navigable, a locked
anchor-topic substrate, and the adherence gate that admits or rejects every future candidate.

## 2. The design artifacts this release implements (the contract)

| Artifact | What it fixes | Path |
|---|---|---|
| ADR 0010 | The frozen taxonomy: 5 domains, 17 format families, 5 voice families, a three-level subfamily, and a governed facet-tag enum; the four axes stay frozen | `docs/internal/adr/0010-domain-and-family-organization.md` |
| E1 adherence-gate spec | The automated distinguishability + pedagogical-completeness + cross-model adherence gate | `plan_v0.3.0/adherence-gate-spec.md` |
| Anchor-topic model (ADR 0017) | The two-tier worked-sample substrate: a frozen regression core plus a growable seed pool (extends ADR 0006) | `plan_v0.3.0/anchor-topics.md` |

ADR 0009 (pedagogical-entry-bar, still a draft) is a dependency of the gate's completeness
check; finalizing it is in scope as a sub-item.

## 3. Scope

### In scope (the foundation)
1. **Codify ADR 0010.** Update `tools/taxonomy.py` from the stale v1 vocabulary (6 domains) to
   the v2 vocabulary (5 domains, 17 format families, 5 voice families) plus the subfamily level
   and the governed facet-tag enum. Add `domain` / `family` / `subfamily` and the faceted-tag
   namespace to the JSON schemas (`schemas/format.schema.json`, `schemas/voice.schema.json`,
   `schemas/entry.universal.schema.json`). Add `check_taxonomy_membership()` to
   `tools/validate.py` (family belongs to domain; subfamily required past 12 family members;
   facet tags drawn from the governed enum). Add per-cell coverage counts to
   `tools/build-indexes.py`.
2. **Backfill the 60 existing entries** with `domain` / `family` (and `subfamily` where a
   family already overflows 12), and any faceted tags. Fields ship optional-with-warning first,
   then tighten to required for formats/voices at the end of the release.
3. **S1 conflict-aware composition.** Extend `skills/writing-instruction-builder/scripts/build-instruction.py`
   to read `avoid_with` / `pairs_well_with`, flag conflicting selections, apply the
   voice -> tone -> style -> format precedence, and resolve `avoid_with` symmetry. Update
   `SKILL.md`; add tests. (Backlog item S1.)
4. **Decide the anchor-topic model** per `anchor-topics.md` and ADR 0017: a two-tier set (a frozen
   regression core plus a growable, optionally randomized seed pool; the 12 are the seed, not a
   cap), extending ADR 0006. The existing 3 stay as the frozen core; the 9 new ones are named and
   domain-assigned (not yet rendered at scale). DONE 2026-06-20 (PR #32).
5. **Stand up the E1 adherence gate** per `adherence-gate-spec.md`: `tools/adherence-gate.py`,
   the frozen golden set (the 60 plus the 8/8 smoke-test pairs), the cross-family judge, and CI
   wiring. The gate runs but is not yet the high-volume producer.
6. **Finalize ADR 0009** (pedagogical bar) so the gate's completeness check has a codified bar.

### Out of scope (future releases, behind this foundation)
- Mass entry expansion toward 30/axis and the full inventory (backlog E2) - v0.4.0+.
- Rendering 12+ samples per entry across the new topics (backlog E3) - v0.4.0+.
- The MCP server (backlog S2) and community sourcing (scaling approach d).
- Any change to the four axes (frozen by ADR 0010) or to tone/style flatness.

## 4. Implementation surfaces

| Surface | Change |
|---|---|
| `tools/taxonomy.py` | v1 -> v2 vocabulary; add subfamily + governed facet-tag enum; the single source of truth |
| `schemas/*.schema.json` | add `domain` / `family` / `subfamily` enums + faceted-tag pattern; format requires domain+family, voice requires family |
| `tools/validate.py` | `check_taxonomy_membership()`; optional-with-warning then required |
| `tools/build-indexes.py` | per-cell coverage ledger (target / filled / gated-pass) |
| `taxonomy/**/ENTRY.md` (x60) | backfill domain/family/subfamily/facets |
| `skills/.../build-instruction.py` + `SKILL.md` | conflict-aware composition (S1) |
| `tools/adherence-gate.py` (new) | the E1 harness |
| `.github/workflows/` | wire the gate + the new validators into CI |
| `tests/` | tests for composition conflicts and the gate |

## 5. Acceptance criteria

- [ ] ADR 0010 is Accepted by the maintainer; `tools/taxonomy.py` matches it exactly; the
      stale v1 vocabulary is gone.
- [ ] `python tools/validate.py` enforces taxonomy membership; all 60 entries carry valid
      `domain` / `family` (formats), `family` (voices); tones/styles unchanged.
- [ ] `tools/build-indexes.py` emits the coverage ledger; `taxonomy.json` regenerates cleanly.
- [ ] `compose-instruction` flags an `avoid_with` conflict (e.g. `pragmatic-architect` +
      `reverent`), applies precedence, and is covered by tests; `SKILL.md` documents it.
- [x] The anchor-topic model is decided in `anchor-topics.md` (two-tier: frozen core + seed pool),
      every domain has a native topic in the seed, and ADR 0017 records it (extending ADR 0006).
- [ ] `tools/adherence-gate.py` runs the golden set green in CI, uses a cross-family judge, and
      writes a per-entry distinguishability score; the 70 percent first-pass stop floor is
      documented.
- [ ] ADR 0009 (pedagogical bar) is Accepted and the gate checks against it.
- [ ] The catalog still validates and the site still builds (no regression); house dash rule
      holds across all new docs and code.

## 6. Maintainer decisions to confirm (gates on Accepted)

These come from the design docs' open questions and the scaling decision matrix; the release
cannot move from Proposed to executing until they are answered:

1. **Taxonomy cuts** - accept the v2 5-domain / 17-family / 5-voice-family structure and the
   evocative family names, or request renames/recuts (ADR 0010 open questions). (Ratified 2026-06-19 as A1.)
2. **Anchor topics** - accept the 12 (and the 9 new slugs), or substitute.
3. **Gate thresholds** - accept the proposed distinguishability band, the ~0.92 dedup cosine,
   and the 70 percent first-pass stop floor as pilot-tunable starting numbers.
4. **`avoid_with` symmetry** - confirm the deterministic rule S1 will use.
5. **Scope boundaries** - confirm journalism / plain-language legal-medical admission policy
   and the held-out crafts (fiction, poetry, translation, children's writing).
6. **Resourcing** - confirm this is a funded effort or a consciously capped one (the scaling
   doc's decision 10); it sets how far v0.4.0+ pushes.

## 7. Risks

| Risk | Mitigation |
|---|---|
| Taxonomy churn after backfill | Lock ADR 0010 Accepted before backfilling; vocabulary changes are ADR amendments |
| Gate built on a same-family judge (monoculture) | Cross-family judge mandated by the spec; human spot-audit before any later distillation |
| S1 changes composition output for current users | Conflict handling is additive (warnings + precedence); existing valid combinations still compose |
| Foundation slips into content work prematurely | E2/E3 explicitly out of scope; the gate must exist before mass generation |
| Required-field tightening breaks the build mid-backfill | Optional-with-warning first, tighten only after all 60 carry valid values |

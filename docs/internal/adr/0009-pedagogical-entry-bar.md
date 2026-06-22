---
adr_id: "0009"
title: Adopt a Pedagogical Entry Bar for Taxonomy Entries
date: 2026-06-20
status: Accepted
supersedes: docs/internal/_working/0009-pedagogical-entry-bar.md (the 2026-05-15 Proposed draft)
related:
  - docs/internal/release-plans/plan_v0.3.0/decisions.md
  - docs/internal/release-plans/plan_v0.3.0/adherence-gate-spec.md
  - docs/internal/release-plans/plan_v0.3.0/spec.md
  - docs/internal/adr/0010-domain-and-family-organization.md
  - schemas/entry.universal.schema.json
  - tools/validate.py
---

# 0009 - Adopt a Pedagogical Entry Bar for Taxonomy Entries

## Status

Accepted - 2026-06-20, ratified as a **gate-critical subset** with amendments. The catalog adopts a
pedagogical entry bar: structured frontmatter fields that let an entry teach a reader (and feed the
adherence gate) what it is, how it fails, and how to misuse it. Of the six fields the original draft
proposed, three are adopted now because the E1 adherence gate consumes them (`failure_modes`,
`anti_patterns`, `tells`); the three heavier ones (`before_after_example`, `mini_glossary`, and the
cross-reference `{id, rationale}` object upgrade) are **deferred, not rejected** (see Decision and
Alternatives). The adopted fields landed as **optional** schema properties (2026-06-20) and were
**tightened to required on 2026-06-22**, once all 60 baseline entries were backfilled, via the
deterministic Gate 2 check in `tools/validate.py` (the F2 - migration sequencing optional-then-tighten
path; see Migration below).

This ADR supersedes the Proposed draft at `docs/internal/_working/0009-pedagogical-entry-bar.md`
(2026-05-15), which proposed the full bar against a pre-gate plan ("double the catalog to 120 with
parallel-agent upgrades; 5 hand-crafted exemplars"). That migration never ran, and its context was
overtaken by the agentic-first posture (F3), the adherence-gate design, A1 - taxonomy cuts, and the
freezing of the 60 as held-out ground truth (C3). The draft stays as a frozen historical snapshot
(`_working/` is read-only); this ADR is the living, ratified record. Mark the draft
`Superseded by ADR 0009`.

## Context

The 60 baseline entries were authored to a baseline bar: a one-liner, a description, when-to-use /
when-not-to-use, axis-specific structural fields (`language_patterns`, `markers`,
`structural_conventions`, `canonical_template`), bare-ID cross-reference arrays, an
`llm_instruction_phrasing` string, and tags. Failure-mode and anti-pattern reasoning lives in prose
inside the description, not in structured fields.

Two forces make that bar insufficient for the v0.3.0+ program:

- **The adherence gate needs structured failure data.** The gate's quality half (the C1 restraint
  check, defined in `adherence-gate-spec.md`) judges each rendered sample by asking whether it is the
  genuine register or a caricature - *judged against the entry's own declared failure modes*. That
  question is only answerable if the failure modes are a field the judge can read, not prose buried
  in a paragraph. Gate 2 (pedagogical completeness) is a deterministic schema check that an entry
  carries this structured data before any judge tokens are spent. Both depend on these fields
  existing.
- **The catalog must teach itself at scale.** Past a few dozen entries a reader cannot hold the
  catalog in their head; each entry must name how to recognize it (`tells`), how it is commonly
  misused (`anti_patterns`), and how it breaks in practice (`failure_modes`).

The original draft's framing (programmatic SDK/MCP consumers, doubling to 120 by hand) is no longer
the driver. Under agentic-first (F3) the driver is the gate: these fields are the gate's inputs, so
the bar is adopted in the shape and at the time the gate needs it, not as a speculative full rewrite
of every entry.

## Decision

### Adopted now (the gate-critical subset)

Three axis-neutral fields are added to `schemas/entry.universal.schema.json` as **optional**
properties, enforced in shape when present:

- **`failure_modes`** - array of 2 to 3 objects, each `{mode, mitigation}`: a specific way the entry
  breaks in practice and how the writer recognizes and corrects it. This is the field the C1
  restraint check renders against; it is the single most load-bearing addition.
- **`anti_patterns`** - array of 2 to 4 objects, each `{pattern, why}`: a common misuse and why it
  counts as misapplication. Makes explicit what is implicit in `when_not_to_use` and
  `confusable_with`; consumed by Gate 2.
- **`tells`** - array of 5 to 7 strings, each a spottable phrase, syntactic move, or structural
  marker by which a reader identifies the entry's application in the wild. Largely a reformatting of
  the existing per-axis fields (`language_patterns`, `markers`, `structural_conventions`) where they
  overlap, new content where they do not.

### Deferred, not rejected

- **`before_after_example`** - the draft's `{before, after, commentary}` object. The heaviest field
  (per-entry hand authorship, the draft's own "highest-effort" admission) and not consumed by the
  gate. Deferred to a later pass.
- **`mini_glossary`** - 2 to 3 term-and-definition pairs, where applicable. Useful but not
  gate-blocking.
- **Cross-reference `{id, rationale}` upgrade** - promoting `pairs_well_with` / `avoid_with` /
  `confusable_with` from bare-ID arrays to objects. The most invasive change (it rewrites existing
  *required* fields on all 60 entries and touches `tools/validate.py`'s cross-reference checker and
  the site generator), and the gate needs none of it. Deferred; the bare-ID arrays stay the contract
  for now.

### Migration (optional-then-tighten, per F2)

1. **Now:** the three fields land as optional schema properties. The 60 entries continue to validate
   unchanged; an entry that omits them is valid, an entry that includes a malformed one fails.
2. **Backfill:** the 60 baseline entries are backfilled with real `failure_modes` / `anti_patterns` /
   `tells`, an agentic authoring task (not the draft's "parallel human agents"). Adding this metadata
   to the frozen 60 does **not** violate C3 - held-out reference set: the freeze protects the
   entries' rendered samples and distinguishability ratings from contaminating the generator/judge,
   whereas these fields are metadata the judge *reads*. Carrying them is in fact a precondition for
   calibrating the C1 restraint bar against the 60.
3. **Tighten:** once the backfill is complete and the gate exists, the fields tighten from optional to
   required (a Gate 2 check in `tools/validate.py`), the same optional-then-tighten move A1 used for
   `domain` / `family`. **Executed 2026-06-22:** with all 60 backfilled, the three fields were added to
   the universal schema's `required` array and `check_pedagogical_bar` (Gate 2) landed in
   `tools/validate.py` as an error-level presence/band/substance check (substance = non-empty strings,
   the bar the schema cannot express). The full catalog validates clean under the required bar. The
   model-calling gate stages (Gates 1 and 3, the cross-family judge) remain to be built; the
   deterministic Gate 2 enforcement does not depend on them.

### Versioning

No incremental `plugin.json` bump accompanies this change. Consistent with the A1 schema work (the
`domain` / `family` / `subfamily` / facet fields and their tightening landed across PRs #26-#31 with
`plugin.json` left at 0.2.0), schema changes inside the in-flight v0.3.0 cycle are batched into the
single v0.3.0 release whose version bump rides the release tag. This ADR is the "new ADR" the
schema-change rule (CLAUDE.md) requires; the additive, optional, backward-compatible field set is
v0.3.0 foundation work.

## Consequences

### Positive

- **The gate's quality half becomes buildable.** Gate 2 and the C1 restraint check have the fields
  they consume; the gate's deterministic foundation (neighbor lookup, anchor-topic pool) plus this
  bar covers everything the gate needs except the model calls themselves.
- **Entries become self-teaching** at the recognition / misuse / failure level, the part that matters
  most for disambiguating near neighbors.
- **Least churn for the value.** Adopting only the gate-critical subset avoids the heaviest fields and
  the invasive cross-reference rewrite while still unblocking the gate.

### Negative

- **A backfill was owed (resolved 2026-06-22).** The 60 entries needed real `failure_modes` /
  `anti_patterns` / `tells` before the fields could tighten to required. The backfill completed
  (PRs #39, #41-#44) and the tightening executed on 2026-06-22, so Gate 2 now enforces them.
- **Frontmatter grows.** Entries carrying the new fields are heavier than the lean baseline shape.
- **Partial bar was a visible interim state (resolved 2026-06-22).** During the backfill some entries
  carried the fields and some did not; this was the intended optional-then-tighten interim. With the
  fields now required, the interim is closed.

### Neutral

- **The deferred fields remain on the table.** `before_after_example`, `mini_glossary`, and the
  cross-reference upgrade can be ratified later by amending this ADR if a concrete need (a downstream
  consumer, a gate criterion that needs them) appears. YAGNI until then.
- **The bar is axis-neutral.** The three fields apply uniformly across voice / tone / style / format,
  so they live in the universal base schema, not the per-axis schemas.

## Alternatives considered

### Scope of ratification (the 2026-06-20 decision)

- **Full bar as drafted (all six fields plus the cross-reference object upgrade).** Maximum
  pedagogical and downstream-consumer payoff, but the heaviest authoring and migration cost and more
  than the gate consumes. Rejected for now in favor of the subset; the difference is deferred, not
  refused.
- **Gate-critical subset (chosen).** Adopt `failure_modes` / `anti_patterns` / `tells`; defer the
  rest. Chosen because it is the minimum that unblocks the gate's quality half, costs the least
  churn, and keeps the heavy/invasive changes out until a concrete need justifies them.
- **Defer entirely (leave 0009 Proposed).** Rejected because the gate's quality half is genuinely
  blocked on these fields; deferring the whole ADR would block C1 / Gate 2 indefinitely.

### Field-set shape (carried from the 2026-05-15 draft, preserved as history)

- **Approach 1 (tells + anti-patterns only).** Lighter, but omits `failure_modes`, the field the C1
  restraint check actually renders against.
- **Approach 2 (tells + anti-patterns + failure_modes).** This is, in effect, the gate-critical
  subset now adopted.
- **Approach 3 (everything except before/after).** Adds `mini_glossary` and the cross-reference
  upgrade without the before/after example.
- **Approach 4 (the full bar).** The draft's original selection; now the deferred end-state.

## Related work

- `docs/internal/release-plans/plan_v0.3.0/decisions.md` - C1 (what the gate scores) and F2
  (migration sequencing); the decision context this bar serves.
- `docs/internal/release-plans/plan_v0.3.0/adherence-gate-spec.md` - Gate 2 and the C1 restraint
  check that consume these fields.
- ADR 0010 (domain-and-family-organization) - the precedent for ratifying a `_working` draft into a
  living ADR with amendments, and for the optional-then-tighten schema migration.
- `docs/internal/_working/0009-pedagogical-entry-bar.md` - the superseded 2026-05-15 draft.

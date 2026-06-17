---
adr_id: "0016"
title: Conflict-aware composition semantics
date: 2026-06-16
status: Accepted
---

# 0016 - Conflict-aware composition semantics

## Status

Accepted (2026-06-16) - implements the decided B1 (`avoid_with` symmetry) and B2 (warn, never
block), both now ratified in `docs/internal/release-plans/plan_v0.3.0/decisions.md`. B2 was
ratified by merging the implementing PR (#20).

## Context

The composer (`skills/writing-instruction-builder/scripts/build-instruction.py`,
`compose_instruction`) loaded each selected entry, pulled only its `llm_instruction_phrasing`,
and joined the blocks with blank lines. That was the entire algorithm: string concatenation. It
never read the curated relationship fields (`pairs_well_with`, `avoid_with`, `confusable_with`)
that every entry carries and that `tools/validate.py` already guarantees reference real IDs.

The concrete failure this allowed: composing `voice=pragmatic-architect` with `tone=reverent`
stapled together "lead with the decision, no softening" and "approach the subject with reverence
and weight" - an incoherent instruction - even though `reverent` is literally in
`pragmatic-architect`'s `avoid_with`. No warning was emitted. "Composable" was a claim, not a
checked guarantee.

Two decisions govern the fix. **B1 (decided 2026-06-09): `avoid_with` is symmetric** - a pair is
a conflict if either entry lists the other, because a conflict is a property of the pair, not of
one author's bookkeeping; under agentic-first authoring (F3) cross-references will be incomplete,
so a symmetric union is the only rule robust to that. **B2 (recommended): warn, never block** -
`avoid_with` means "discouraged," not "forbidden," and a user may want a deliberate tension.

## Decision

1. **Detect conflicts with a symmetric union rule.** For the selected entries, flag a pair if
   either lists the other in `avoid_with`. Implemented in a pure `analyze_relationships()`
   function over `{axis, id, entry}` selections, so the rule is independently testable.
2. **Affirm good pairings.** A `pairs_well_with` match between two selections is surfaced as a
   confirming note (same symmetric union).
3. **Warn, never block.** A conflicting selection still composes the full instruction. Conflicts
   and affirmations are written to **stderr**; the composed instruction is written to **stdout**,
   so stdout stays a clean, pipeable prompt.
4. **Deterministic precedence.** `resolve_selections()` orders selections voice -> tone -> style
   -> format regardless of argument order, so the higher-precedence axis leads and the output is
   stable.
5. **Backward compatibility.** `compose_report()` returns `{instruction, conflicts, affirmations,
   errors}`; `compose_instruction()` is kept as a thin wrapper returning the instruction string,
   so existing callers and the CLI's stdout are unchanged.

`confusable_with` is intentionally NOT consumed here: it serves the adherence gate's neighbor
set (the Fable review's R3), not composition.

## Consequences

### Positive

- "Composable" becomes a checked guarantee: incoherent pairings are surfaced at composition time.
- The rule is deterministic and order-independent, and robust to incomplete cross-references,
  which matters under agentic authoring where back-links are unreliable.
- The relationship data the catalog already curates earns its keep instead of sitting unused.
- stdout/stderr separation keeps the instruction pipeable while still informing the user.

### Negative

- Warnings are advisory. The builder orders and annotates conflicting blocks; it does not
  programmatically merge or reconcile the prose (realistically it cannot), so a deliberately
  conflicting composition can still produce tension - by design.
- A hygiene gap remains: an entry may omit a reciprocal `avoid_with`/`pairs_well_with` link. The
  symmetric rule tolerates this for correctness; a future validator warning can nudge the catalog
  toward complete reciprocal links (noted in B1).

---
adr_id: "0009"
title: Adopt Full Pedagogical Bar for Taxonomy Entries
date: 2026-05-15
status: Proposed
related:
  - docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md
  - docs/internal/_working/phase-0-exemplar-candidates_2026-05-15.md
  - schemas/voice.schema.json
  - schemas/tone.schema.json
  - schemas/style.schema.json
  - schemas/format.schema.json
  - schemas/entry.universal.schema.json
---

# 0009 - Adopt Full Pedagogical Bar for Taxonomy Entries

## Status

Proposed - awaiting maintainer approval before Phase 1 schema codification can ship. See `docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md` for the broader plan this ADR supports.

## Context

The Phase 1 catalog (60 entries, 15 per axis) was authored against a baseline quality bar: each entry has a one-liner, description, when_to_use / when_not_to_use, axis-specific structural fields (`language_patterns` for voices, `markers` for tones, `structural_conventions` for styles, `canonical_template` and `typical_voices`/`typical_tones` for formats), bare ID arrays for `pairs_well_with` / `avoid_with` / `confusable_with`, `llm_instruction_phrasing`, and tags. Confusable_with prose explanations live in the body, not frontmatter.

Phase 2 plans to:
1. Double the catalog to 120 entries (30 per axis).
2. Add downstream consumers (SDK, MCP server, Composer SPA) that programmatically read entry frontmatter.

Two consequences of that plan create pressure on the current bar:

- **Programmatic consumption.** Tools that compose writing instructions need structured failure-mode and anti-pattern data, not prose buried in descriptions. The current bar makes the LLM-facing instruction string (`llm_instruction_phrasing`) the only structured-for-consumption field; everything else assumes a human reader.
- **Catalog-as-pedagogy.** At 120 entries, a reader cannot hold the catalog in their head. Each entry must teach itself: what it is, how to recognize it, how it differs from neighbors, when it fails, and what its application produces in concrete terms.

Three approaches were considered (see `docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md` for the full analysis):

1. **Tells + anti-patterns only** - minimal additions; preserves existing structure
2. **Tells + anti-patterns + failure modes** - adds failure-mode reasoning
3. **Full pedagogical entry** - adds tells, anti-patterns, failure modes, dense cross-reference network with rationale, and mini-glossary
4. **Full + before/after example pair** - everything above plus a paired 50-100 word passage showing the same content rendered without and with the entry applied

Approach 4 was selected during brainstorming. The before/after example pair is the heaviest addition but provides the highest per-entry pedagogical payoff: a reader can see the entry's effect concretely, not just read about it.

## Decision

Adopt the full pedagogical bar (Approach 4) for all taxonomy entries.

New required fields, added to entry frontmatter across all four axis schemas:

- **`tells`** - array of 5 to 7 strings, each naming a spottable phrase, syntactic move, or structural marker by which a reader could identify this entry's application in the wild. Reformatting of existing per-axis fields (`language_patterns`, `markers`, `structural_conventions`) where they overlap; new content where they do not.
- **`anti_patterns`** - array of 2 to 4 objects, each with `pattern` (a description of a common misuse) and `why` (a short explanation of why it counts as misapplication). Articulates explicitly what is currently implicit in `when_not_to_use` and `confusable_with`.
- **`failure_modes`** - array of 2 to 3 objects, each with `mode` (a specific way the entry breaks in practice) and `mitigation` (how the writer recognizes and corrects it). Promotes failure discussion out of description prose into a structured field.
- **`before_after_example`** - object with `before` (a 50 to 100 word passage written without the entry applied), `after` (the same passage rewritten with the entry applied), and optional `commentary` (one to three sentences naming what changed). Net-new field.
- **`mini_glossary`** - object or array of 2 to 3 term-and-definition pairs, defining terms the entry uses that a reader might not share.

Cross-reference fields upgrade from bare ID arrays to objects:

- **`pairs_well_with`**, **`avoid_with`**, **`confusable_with`** - each item becomes an object with `id` (the entry ID, as before) and `rationale` (one sentence explaining why this pairing or contrast matters).

Migration strategy:

1. **Phase 1 (schema codification).** Add new fields to schemas as **optional**. Old bare-ID-array shape for cross-references continues to validate alongside new object shape. Existing 55 entries (60 minus the 5 hand-crafted exemplars) continue to pass validation unchanged.
2. **Phase 2 (audit-and-upgrade existing 55).** Parallel agents upgrade entries against exemplar templates. After completion, schema fields tighten from optional to required.
3. **Phase 3 (generate new 60).** New entries authored directly to the full bar; validator now enforces required fields.

The pedagogical bar applies uniformly to all four axes. Some fields (`canonical_template`, `typical_voices`, `typical_tones`) remain format-specific. The new fields are axis-neutral.

## Consequences

### Positive

- **Catalog becomes self-teaching at scale.** A reader can land on any entry and learn what it is, recognize it, avoid common misuses, see its application concretely (before/after), and navigate to compatible, contrasting, or confusable neighbors with explicit rationale.
- **Downstream surfaces gain structured data to consume.** SDK, MCP server, and Composer can present anti-patterns, failure modes, and disambiguation rationale through their own UIs without scraping prose.
- **Diff-pair pedagogy gains a per-entry foundation.** Every entry carries its own mini-diff-pair (before/after) in addition to the catalog-wide diff-pairs in `examples/diff-pairs/`. The per-entry version teaches "what does this entry alone do"; the catalog-wide version teaches "how do two similar entries differ."
- **Curation rigor.** Adding an entry now requires the curator to articulate failure modes, anti-patterns, and a before/after example, which forces the entry to actually earn inclusion.

### Negative

- **Authorship cost rises.** Each entry now requires roughly six additional populated fields, including the highest-effort before/after example. Solo-maintainer sustainability is a real concern; the Phase 0 exemplar work is partly an effort-estimation test.
- **Frontmatter visual weight.** Entries that previously fit on one screen will become multi-screen frontmatter blocks. Some readers may prefer the leaner prior shape.
- **Schema and validator complexity.** Schemas grow new field definitions; validator gains optional-then-required field checks. The hand-rolled YAML parser already used in `tools/validate.py` and `skills/writing-instruction-builder/scripts/build-instruction.py` may need updates to handle the more deeply-nested anti_patterns / failure_modes objects.
- **Migration risk.** Even with optional-then-required staging, the 55 existing entries each need new fields populated correctly. Parallel agents can drift; cf. the `e0fb1d4` precedent in the Phase 1 session log.

### Neutral

- **The bar applies retroactively.** All existing entries must be upgraded; this is by design. Mixed-quality catalogs (some entries at old bar, some at new) are explicitly rejected as a stopping state.
- **Cross-reference rationale prose duplicates some content from confusable_with body prose.** This is acceptable; the body prose is for the human reader, the frontmatter rationale is for programmatic consumption. They serve different audiences.

## Alternatives considered

- **Approach 1 (tells + anti-patterns only).** Lighter touch. Rejected because failure_modes and before/after are the fields with the highest downstream-consumer payoff; deferring them creates schema churn later.
- **Approach 2 (add failure_modes but not before/after).** Rejected for the same reason; before/after is the field that makes entries concretely useful and is the hardest to add later because it requires hand authorship per entry.
- **Approach 3 (everything except before/after).** Rejected during brainstorming in favor of Approach 4.
- **Two-phase rollout (new fields shipped without before/after, before/after added later).** Rejected; before/after is the field most likely to drive schema-shape discoveries during Phase 0, and pulling it out reduces the value of Phase 0 as a discovery exercise.

## Related work

- `docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md` - the design spec this ADR supports.
- `docs/internal/_working/phase-0-exemplar-candidates_2026-05-15.md` - the 5 entries proposed as Phase 0 exemplars under this bar.
- ADR 0001 (three-axis-model) - the bar applies to all four axis families equally.
- ADR 0002 (atomic-folder pattern) - the bar adds fields to ENTRY.md frontmatter; folder structure is unchanged.

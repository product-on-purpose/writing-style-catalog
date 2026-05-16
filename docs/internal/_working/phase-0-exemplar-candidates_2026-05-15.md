---
title: Phase 0 Exemplar Candidates - Analysis and Recommendations
date: 2026-05-15
author: claude (Opus 4.7)
status: draft - awaiting maintainer approval before Phase 0 execution
type: analysis
related:
  - docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md
  - docs/internal/_working/domain-and-family-taxonomy_2026-05-15.md
  - taxonomy/voices/caregiver/ENTRY.md
  - taxonomy/tones/confessional/ENTRY.md
  - taxonomy/styles/socratic-inquiry/ENTRY.md
  - taxonomy/formats/whitepaper/ENTRY.md
  - taxonomy/voices/pragmatic-architect/ENTRY.md
---

# Phase 0 Exemplar Candidates - Analysis and Recommendations

## Purpose

The Phase 2 design spec (`phase-2-catalog-expansion_2026-05-15.md`) opens with Phase 0: hand-craft 5 exemplar entries to the proposed full pedagogical bar before any schema changes ship. The 5 exemplars become the canonical templates that parallel agents reference when upgrading the remaining 55 entries (Phase 2) and generating the 60 new entries (Phase 3).

This document recommends specific entries to pick as exemplars, with rationale for each, and flags one stress case that tests the bar at its hardest boundary.

The recommendations are for maintainer approval before Phase 0 execution starts. They are not yet locked.

## Methodology

I sampled 5 entries across the four axes for evaluation against the proposed bar:

- `caregiver` voice (emotional/care register)
- `confessional` tone (intimate self-disclosure register)
- `socratic-inquiry` style (rhetorical inquiry pattern)
- `whitepaper` format (long-form authoritative structure)
- `dialectic` style (newer entry, sanity check on cross-batch consistency)
- `daily-standup` format (shorter-form structural sanity check)

Evaluation criteria:

1. **Existing richness** - does the entry already have substantial frontmatter and prose, or would the pedagogical upgrade be mostly net-new authoring?
2. **Cross-reference density** - how many pairs_well_with / avoid_with / confusable_with relationships are present, and how non-trivial would adding rationale be?
3. **Distinctiveness** - does the entry sit in a unique part of the catalog (own family, own register), making it a useful pattern for similar future entries?
4. **Stress-test value** - does the entry's shape exercise an edge of the proposed bar (e.g., long canonical_template, dense confusable_with cluster, emotional content that makes "anti-patterns" hard to articulate)?
5. **Taxonomy placement** (per `domain-and-family-taxonomy_2026-05-15.md`) - exemplars should ideally cover multiple families across the catalog so the templates exercise family-membership variations.

## Headline finding

Every existing entry sampled is already at a high baseline. The pedagogical upgrade is mostly **additive** (new fields) rather than **rewriting** (changing existing content). The current entries already include:

- Strong `one_liner`, `description`, `when_to_use`, `when_not_to_use`
- Markers / language_patterns / structural_conventions fields that overlap heavily with the proposed `tells`
- Confusable_with prose explanations that overlap heavily with proposed disambiguation rationale
- Detailed `llm_instruction_phrasing`

What the proposed bar adds, against this baseline:

| Proposed field | Closest existing equivalent | Gap to fill |
|---|---|---|
| `tells` (5-7 spottable strings) | `markers` / `language_patterns` / `structural_conventions` (per-axis named differently) | Mostly reformatting; small content additions |
| `anti_patterns` (explicit "what this is NOT") | Implicit in `when_not_to_use` and `confusable_with` | Mostly explicit articulation of what's currently implicit |
| `failure_modes` (specific failure scenarios) | Some entries discuss failure in description prose | New explicit field; modest content addition |
| `before_after_example` (50-100 word paired passages) | Not present | Net new; the highest-effort field per entry |
| `mini_glossary` (2-3 term definitions) | Not present | Net new; small per-entry content |
| Cross-references with rationale | Bare ID arrays | Reformatting plus 1-sentence rationale per ref |

**Implication for Phase 0:** the exemplar work is meaningful but not a wholesale rewrite. Five entries upgraded by hand should be a one-session task, not a multi-session deep dive.

## Per-axis exemplar recommendations

### Voice exemplar: `caregiver`

**Recommended.** Confidence: high.

- **Why:** Emotional-register stress case. The pedagogical bar's `anti_patterns` and `failure_modes` fields are hardest for entries with high emotional content, because the failure modes are subtler ("the caregiver voice becomes performative compassion" or "the voice becomes preachy"). Getting these articulated well on caregiver sets a template for similar high-emotion entries: pastoral, friendly-mentor, coach.
- **Existing strength:** Already has rich `language_patterns`, explicit `confusable_with` prose for pastoral and coach, and well-articulated `when_not_to_use`.
- **Family placement (per proposed taxonomy):** `people-and-coaching` (one of two with multiple members at current scale).
- **What this exemplar stress-tests:** whether the proposed bar accommodates emotionally-attuned entries without making them feel clinical.

### Tone exemplar: `confessional`

**Recommended.** Confidence: high.

- **Why:** Already has a `markers` field with six entries that map almost directly to the proposed `tells` field. Strong existing confusable_with prose explaining the difference from `empathetic`. The intimate self-disclosure register stress-tests the before/after example field at the hardest boundary - a confessional before/after must show specific personal ownership, which is harder to fake than informational rewriting.
- **Existing strength:** The `description` already articulates failure modes inline ("performative humility uses the form of confession to fish for reassurance"). Refactoring those into an explicit `failure_modes` field is fast.
- **What this exemplar stress-tests:** whether the bar's `failure_modes` field can capture register-specific failures (performance, fishing, preemption of criticism) cleanly.

### Style exemplar: `socratic-inquiry`

**Recommended.** Confidence: high.

- **Why:** Style entries have `structural_conventions` rather than `markers` or `language_patterns`. Socratic-inquiry's structural_conventions are particularly strong (five precise rules including "at least one question must admit a real second answer"). Choosing socratic-inquiry as the style exemplar exercises the bar against a structurally-disciplined rhetorical pattern.
- **Existing strength:** The `description` includes failure modes inline ("fails when it becomes manipulative... or when it becomes lazy"). The confusable_with prose against `diataxis-explanation` and `dialectic` is already disambiguation-quality.
- **What this exemplar stress-tests:** whether the bar accommodates structurally-rigorous styles (where the "tells" are partly about discipline rather than just vocabulary).

### Format exemplar: `whitepaper`

**Recommended.** Confidence: high.

- **Why:** Format entries are uniquely structured: they have `canonical_template` (a multi-line block scalar) and `typical_voices`/`typical_tones` fields that no other axis has. Whitepaper has the most complex canonical_template in the catalog (~30 lines, multiple section headings, optional appendix). Exercising the bar on whitepaper proves that the new fields integrate cleanly with the existing complex canonical_template field.
- **Existing strength:** Multi-paragraph description with explicit failure mode discussion (the executive-summary-as-load-bearing observation). Strong existing confusable_with prose against `blog-post-long-form` and `technical-reference`.
- **Family placement (per proposed taxonomy):** `engineering > decision-documents` - the family with the most members; whitepaper as exemplar provides template for adr, prd, design-doc, rfc.
- **What this exemplar stress-tests:** whether the bar's new fields can coexist with the complex existing format-specific fields without crowding the frontmatter or making validation brittle.

### Stress case: `pragmatic-architect`

**Recommended.** Confidence: medium-high. Open to substitution if a better case surfaces.

- **Why:** The cross-reference-with-rationale field is the proposed change with the highest spread across the catalog. Every existing entry will gain rationale strings for its pairs_well_with / avoid_with / confusable_with lists. `pragmatic-architect` is one of the most heavily cross-referenced entries in the voice axis (anchor of the technical-and-expert family, paired across many tones and formats). Upgrading it tests the bar's cross-reference treatment at its most demanding before that pattern propagates to 55 other entries.
- **Family placement (per proposed taxonomy):** `technical-and-expert` (largest voice family). Pairing this stress case with the `caregiver` exemplar covers two voice families in the exemplar set.
- **What this exemplar stress-tests:** whether the proposed object-shape for cross-references (`{id: x, rationale: "..."}`) is ergonomic when an entry has 5+ entries per cross-ref list, or whether it becomes visually heavy.
- **Alternatives considered:**
  - `pastoral` voice - the unique spiritual family. Stress-tests the bar at a single-member family. Rejected because the stress on pastoral is "minimum density" which is less informative than "maximum density."
  - A horizontal-slice combination - stress-tests the cross-axis composition. Rejected because exemplars are per-entry, not per-combination; horizontal slices live in `examples/` not `taxonomy/`.
  - A newer entry from the 8c50565 batch (e.g., `journalist` or `senior-consultant`) - would test the bar against entries authored under the older lighter conventions. Rejected because the 8c50565 batch entries inspected (e.g., `dialectic`) are already at parity with older entries.

## Family coverage check

Per the proposed domain/family taxonomy:

| Axis | Family covered | Exemplar |
|---|---|---|
| voices | `people-and-coaching` | caregiver |
| voices | `technical-and-expert` | pragmatic-architect (stress case) |
| tones | (no family layer) | confessional |
| styles | (no family layer) | socratic-inquiry |
| formats | `engineering > decision-documents` | whitepaper |

Two voice families covered. Tones and styles get one exemplar each (no family layer for those axes by design). Formats get one exemplar in the largest family. Other format families (workplace, publication, ceremonial, contemplative) and other voice families (authority, narrative-and-media, spiritual) do NOT have exemplars in this set; they will reference the existing exemplars and adapt patterns rather than getting their own dedicated templates.

If any of those uncovered families turn out to need their own exemplar during Phase 2 (e.g., ceremonial entries like eulogy need a fundamentally different pattern), a sixth or seventh exemplar can be added mid-Phase-2 without disrupting the schema.

## Recommended order to craft exemplars

1. **`whitepaper`** first - the format exemplar is the most complex frontmatter shape; getting the bar to fit alongside `canonical_template` and `typical_voices`/`typical_tones` proves the schema can carry the load before less-complex axes are tackled.
2. **`socratic-inquiry`** - style exemplar; cleaner frontmatter than format, exercises rhetorical-pattern entries.
3. **`confessional`** - tone exemplar; simplest frontmatter shape; the `markers` -> `tells` rename happens here.
4. **`caregiver`** - voice exemplar; emotional-content stress; tests anti_patterns articulation at the hardest boundary.
5. **`pragmatic-architect`** - stress case; cross-reference density test; comes last because the cross-ref upgrade pattern depends on having the other exemplars' new field shapes settled.

Sequencing this way means schema decisions front-load on the format exemplar (the hardest case) and the cross-ref decisions back-load on the stress case (after the per-field decisions are stable).

## Expected per-entry effort

Based on the sampled entries' existing richness:

| Exemplar | Existing baseline | Net-new authoring needed | Estimated effort |
|---|---|---|---|
| whitepaper | High; complex canonical_template | tells (refactor), anti_patterns, failure_modes, before/after, mini-glossary, cross-ref rationale | Medium - the before/after example for a whitepaper is the heaviest piece (must be representative without becoming a full whitepaper) |
| socratic-inquiry | High; explicit structural_conventions and failure-mode discussion | tells (refactor of structural_conventions), explicit failure_modes, before/after, mini-glossary, cross-ref rationale | Light-to-medium |
| confessional | High; existing `markers` field | tells (rename), anti_patterns (extract from description), failure_modes (extract from description), before/after, mini-glossary, cross-ref rationale | Light-to-medium |
| caregiver | High; rich language_patterns and confusable_with prose | tells (refactor), anti_patterns (new articulation), failure_modes (new), before/after, mini-glossary, cross-ref rationale | Medium - emotional-content anti_patterns are subtler |
| pragmatic-architect | Not yet inspected in detail; expected to be similarly rich | cross-ref rationale at scale plus the standard new fields | Medium - depends on how dense the cross-refs actually are |

Aggregate estimate: a single concentrated session per exemplar, or one extended session for the full set if dispatched serially with the same field-shape decisions carried forward. Parallel dispatch is possible but not recommended for Phase 0 exemplars - the entire point of doing this by hand is to surface schema-shape questions, which is hard to do in parallel.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| The bar feels different in practice than in spec | Phase 0's whole purpose is exactly this discovery; the spec is explicit that schema codification (Phase 1) happens AFTER exemplar craft |
| One exemplar's field shapes contradict another | Sequencing recommendation above front-loads the hardest case (whitepaper format); shape decisions settle early |
| Before/after example takes longer than estimated | Acceptable; this is the field with the highest pedagogical payoff and the most-novel design surface |
| Exemplar quality varies | Manual hand-craft on 5 entries should produce uniform quality if done sequentially by the same author |
| Pragmatic-architect cross-refs reveal that the object shape is too heavy | This is the stress case's job; if confirmed, fallback options are listed in the taxonomy doc (the object shape can be optional alongside bare ID arrays during migration) |

## Decision needed

Maintainer to confirm:

1. **The 5 picks (caregiver, confessional, socratic-inquiry, whitepaper, pragmatic-architect)** - or substitute specific entries.
2. **The ordering recommendation (format first, stress case last)** - or override.
3. **Sequential rather than parallel craft** - or accept parallel dispatch trade-off.

Once confirmed, Phase 0 can start as soon as the design spec itself is approved.

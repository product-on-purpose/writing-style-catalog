---
adr_id: "0010"
title: Add Domain and Family Organization Layers to Catalog
date: 2026-05-15
status: Proposed
related:
  - docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md
  - docs/internal/_working/domain-and-family-taxonomy_2026-05-15.md
  - docs/internal/adr/0001-three-axis-model.md
  - schemas/format.schema.json
  - schemas/voice.schema.json
---

# 0010 - Add Domain and Family Organization Layers to Catalog

## Status

Proposed - awaiting maintainer approval. See `docs/internal/_working/domain-and-family-taxonomy_2026-05-15.md` for the comprehensive proposal and `docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md` for the broader plan.

## Context

The Phase 1 catalog at 15 entries per axis reads naturally as a flat list. The format axis lineup (adr, blog-post-long-form, devotional-entry, meeting-notes, slack-message, etc.) is heterogeneous but small enough that the heterogeneity does not feel disordered.

Phase 2 targets 30 entries per axis and proposes a candidate format lineup that would include `rfc`, `linkedin-post`, `eulogy`, `wedding-toast`, `error-message`, and `podcast-show-notes` among others. A flat axis presenting these as peer choices is no longer accurate; an `rfc` and a `wedding-toast` do not occupy the same writing-task space.

The same heterogeneity surfaces on the voice axis at scale: `pragmatic-architect`, `pastoral`, `journalist`, and `caregiver` are not really peers, even at 15 entries each. The flat-list framing breaks down faster on voices than tones or styles because voices encode speaker identity (which has natural domain affinity) where tones and styles encode register and rhetorical pattern (which are domain-neutral by nature).

Five alternatives were evaluated (see `docs/internal/_working/domain-and-family-taxonomy_2026-05-15.md` for full analysis):

1. Single-level `category` field per axis
2. Three-level taxonomy (domain > family > subfamily)
3. Tag-based organization only
4. Per-axis fully custom organization
5. A fifth top-level catalog axis

A two-level taxonomy (domain + family) was selected. Two-level is more queryable than single-level, more sustainable than three-level at current scale, more disciplined than tag-only, more consistent than per-axis custom, and preserves the foundational three-axis model from ADR 0001.

## Decision

Add two new fields to entry frontmatter, with per-axis applicability:

- **`domain`** - required on **formats only**. One value from a controlled list of 6: `engineering`, `business`, `workplace`, `publication`, `ceremonial`, `contemplative`. Answers "in what sphere of life does this writing happen?"
- **`family`** - required on **formats and voices**. One value from a per-axis controlled list (scoped to domain for formats). Answers "what structural or functional kind of writing is this?"

Tones and styles receive neither field; their flat structure is preserved by design. Tone is a register that travels across domains by nature; style is a rhetorical pattern with the same property. Imposing a domain or family on them would produce arbitrary groupings.

Controlled vocabulary highlights (see `domain-and-family-taxonomy_2026-05-15.md` for the full enumeration):

**Format domains (6) and families (14):**
- `engineering`: decision-documents, reference-and-onboarding, status
- `business`: briefs-and-proposals, status-and-updates, feedback
- `workplace`: quick-communication, meetings, onboarding
- `publication`: long-form, social-posts, spoken-and-show-notes
- `ceremonial`: toasts-and-tributes
- `contemplative`: devotional-writing

**Voice families (5 at current 15 entries; expected 6-7 at 30 entries):**
- `technical-and-expert`
- `people-and-coaching`
- `authority`
- `narrative-and-media`
- `spiritual`

Schema enforcement uses Option 2 (Python cross-field check) from the proposal: schema files list valid domains and valid families as separate enums; a new `check_taxonomy_membership()` function in `tools/validate.py` enforces that each format entry's family belongs to its declared domain's family list. The controlled vocabulary lives in a single Python module (`tools/taxonomy.py`) for easy evolution.

Migration strategy mirrors ADR 0009:

1. **Phase 1.** Fields added as optional; validator warns rather than errors when fields are missing or family-domain mismatched.
2. **Phase 2.** Existing 60 entries (15 formats, 15 voices, 30 tones-and-styles) backfilled with domain and family values during the audit pass. Phase 0 exemplars populate the fields first as templates.
3. **Phase 2 (end).** Fields tighten from optional to required; validator promotes warnings to errors.

The taxonomy is forward-compatible with future subfamily layer (a third level) if catalog scale eventually warrants it. Subfamily can be added as an optional field without breaking the two-level scheme.

## Consequences

### Positive

- **Catalog heterogeneity becomes structured.** A reader scanning formats sees ADR, RFC, design-doc grouped under engineering/decision-documents and eulogy, wedding-toast grouped under ceremonial/toasts-and-tributes. The distance between them is visible, not hidden in a flat list.
- **Index pages and future composer surfaces gain hierarchical navigation.** Three-click selection (domain > family > entry) becomes possible instead of long flat scrolling.
- **Diff-pair selection criterion sharpens.** Within-family confusables produce the crispest pedagogy. The current 4 seed diff-pairs include `pragmatic-architect` vs `pastoral` (cross-family); within-family pairs become the recommended pattern (Phase 5 design spec section).
- **Per-axis curation rationale becomes tractable.** Curation discussion structures around 6 domains and 14 families instead of 30 individual entries (formats) or 30 individual voices.
- **Future SDK and MCP queries gain natural filters.** `catalog.formats.filter(f => f.domain === 'engineering')` and `catalog.voices.groupBy(v => v.family)` become first-class queries.

### Negative

- **Per-entry curation now includes a placement decision.** Adding a new format requires choosing one of 6 domains and one of N families within it. Choosing well requires holding the taxonomy in working memory. Edge cases (daily-standup, prd, whitepaper, talk-abstract) will produce maintainer judgment calls.
- **Controlled vocabulary becomes a binding contract.** Adding a new domain or a new family is a schema change that requires an ADR amendment or replacement. Adding new entries within an existing family is friction-free; expanding the vocabulary is not.
- **Taxonomy may age poorly.** Some family names (`spoken-and-show-notes`, `social-posts`) reference platform conventions that may shift. The proposal doc carries the rationale so future renames preserve intent.
- **No personal domain at launch.** The catalog has no formats for personal letters, journal entries, etc. If those are added later, `personal` becomes a 7th domain (small schema change).
- **Single-member families exist.** Some families (`toasts-and-tributes` at 2, `devotional-writing` at 1, `meetings` at 1) are deliberately thin. Acceptable as a starting state; not aesthetically pleasing.

### Neutral

- **Tones and styles stay flat.** No organization layer for those axes is a deliberate design choice (their entries are register and rhetorical pattern, domain-neutral by nature). If at 40+ entries either axis develops felt-grouping pressure, a future ADR can revisit.
- **Backward-compatible with three-level future.** Subfamily can be added later as an optional third field. The current two-level scheme is forward-stable.
- **ADR 0001's three-axis model remains foundational.** Domain and family are within-axis organization, not a fifth axis. The three-axis model is preserved.

## Alternatives considered

- **Single-level `category`.** Simpler schema. Loses queryability and forces awkward names. Rejected.
- **Three-level `domain > family > subfamily`.** Maximum expressiveness. Third-level cells too thin at 30 entries per axis. Rejected for now; forward-compatible later.
- **Tag-based only.** No schema change. Organization-by-convention is fragile; new contributors will tag inconsistently. Rejected as primary mechanism; tags remain available for cross-cutting attributes.
- **Per-axis fully custom.** Maximum per-axis appropriateness. Sacrifices schema consistency, complicates downstream consumers. Rejected.
- **Fifth top-level axis.** Maintains pure-axis-only structure. Breaks the three-axis model from ADR 0001. Rejected.

See `docs/internal/_working/domain-and-family-taxonomy_2026-05-15.md` Section "Alternative taxonomies considered" for the full evaluation.

## Open questions deferred to maintainer review

The proposal doc lists six open questions for maintainer answer before this ADR can be promoted from Proposed to Accepted:

1. Whether the 6-domain cut is right, or whether `business` should be split into marketing/leadership/operations or `ceremonial` and `contemplative` merged.
2. Whether voices should also get a `domain` field (recommendation: no).
3. Whether any family names read wrong and need substitution.
4. Whether the edge-case placements (daily-standup, whitepaper, talk-abstract) should be reassigned.
5. Whether the no-organization decision for tones and styles is correct.
6. Whether per-axis curation rationale (Phase 6d) is one doc per axis or one doc per domain.

## Related work

- `docs/internal/_working/domain-and-family-taxonomy_2026-05-15.md` - the comprehensive proposal this ADR codifies.
- `docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md` - the broader Phase 2 plan that integrates this taxonomy at Phase 1 (schema), Phase 2 (backfill), Phase 5 (diff-pair criterion), and Phase 6d (curation rationale).
- ADR 0001 (three-axis-model) - the foundational structure this ADR organizes within, not against.
- ADR 0009 (pedagogical-entry-bar) - parallel schema additions that ship in the same Phase 1 codification window.

---
adr_id: "0010"
title: Domain, Family, and Subfamily Organization plus Governed Facet Tags
date: 2026-06-03
status: Accepted
supersedes: docs/internal/_working/0010-domain-and-family-organization.md (draft v1, 6 domains / 14 families)
related:
  - docs/internal/_working/domain-and-family-taxonomy_2026-05-15.md
  - docs/internal/_working/catalog-inventory-aspirational_2026-05-16.md
  - docs/internal/scaling-the-library-100x.md
  - docs/internal/backlog.md
  - docs/internal/adr/0001-three-axis-model.md
  - docs/internal/adr/0002-atomic-folder-pattern.md
  - schemas/entry.universal.schema.json
  - schemas/format.schema.json
  - schemas/voice.schema.json
  - tools/taxonomy.py
  - tools/validate.py
  - tools/build-indexes.py
---

# 0010 - Domain, Family, and Subfamily Organization plus Governed Facet Tags

## Status

Accepted - 2026-06-19 (ratifies decision A1 - taxonomy cuts). Adopted with the amendments worked out of the independent Fable review (the Q1-Q12 register in `_LOCAL/2026-06-09_a1-taxonomy-evaluation_by-fable.md`, Section 13) and recorded in `docs/internal/release-plans/plan_v0.3.0/decisions.md` under A1. The structure carried into acceptance differs from the originally proposed cut in two ratified ways: the `relational` domain is renamed `personal` and redefined to cover both its families (Q2), and the voice axis carries **5** families, not 6, with the former `pastoral` family folded into `care` as a subfamily (the grounding pass below). Every recorded alternative to the cut (drop-domains, single-level, tags-only, a fifth axis, the v1 cut) was re-examined in the review and rejected for its recorded reason; the review's verdict was "adopt, do not re-cut." Execution of the field migration this ADR specifies (Section 9) proceeds in Phase 1; the entry-level data moves the review also raised (slug reconciliation Q9, the confusable-graph audit Q6, channel-clone collapse Q3) batch into that migration so entries are touched once.

This ADR supersedes the stale draft at `docs/internal/_working/0010-domain-and-family-organization.md`, which encoded a v1 taxonomy (6 domains: engineering, business, workplace, publication, ceremonial, contemplative; 14 functional families) derived from a ~30-entry candidate set. That draft was never promoted. Maintainer feedback rejected its cuts (business/workplace blurred, `authority` carried wrong connotations, family names read as database columns). The canonical structure is the v2 taxonomy in `domain-and-family-taxonomy_2026-05-15.md`, sized against the ~195-format / ~68-voice aspirational inventory and refined by the agreed scaling strategy (`scaling-the-library-100x.md`, decision-matrix rows 6 and 7). This ADR codifies that canonical structure as a binding contract. Mark the draft `Superseded by ADR 0010` and do not copy from it.

## Context

At 60 entries (15 per axis), a flat axis list is scannable and the domain/family scheme is a navigation nicety. The catalog is now committed to an aspirational expansion across more topics, styles, and domains, toward roughly 600 best-in-class entries carrying tens of thousands of worked samples, every one held to the same empirical bar the catalog's value rests on. That bar is the 8/8 blind adherence result (`_LOCAL/audit/2026-05-31_adherence-smoke-test.md`): a blind judge correctly attributed all 8 within-axis confusable pairs against a chance baseline near 0.4 percent. The scaling strategy promotes that one-off audit into a standing CI gate (backlog item E1) that renders each candidate entry blind against its same-`family` neighbors and rejects anything not distinguishable.

That makes taxonomy load-bearing, not cosmetic. The gate is only as sharp as the neighbor set it renders against, and the neighbor set is defined by the category tree. Loose categories produce loose gates. At the target scale the taxonomy must do three jobs at once: keep thousands of entries scannable (domain to family to entry in three clicks, never an 800-row scroll); make coverage measurable (every cell carries a target count and a fill state, so "comprehensive" has a number, not a slogan); and keep neighbor sets tight so the adherence gate stays meaningful. The inventory already overflows the two-level scheme - `instruction` holds ~19 candidate formats and `witness` holds ~18 candidate voices, both past the v2 doc's own "revisit when a family exceeds 12 members" trigger.

A recurring temptation is to add a fifth top-level axis to absorb new dimensions (rhetorical stance, epistemic stance, register/formality, medium/channel, persona-archetype, output modality). ADR 0001 fixes the model at four axes. The correct move is to deepen the existing within-axis structure and demote every candidate fifth axis to a governed facet tag or a subfamily (the demotion table is in Decision section 1).

This ADR therefore codifies four things together, because they are one decision: the v2 controlled vocabulary, its promotion to three levels, a governed faceted-tag namespace that absorbs the rejected fifth axes, and the enforcement that keeps all of it from rotting.

## Decision

### 1. The four axes stay frozen

Voice, Tone, Style, and Format remain the only top-level axes, per ADR 0001. No fifth axis is added now or as part of any expansion. Every floated fifth axis demotes:

| Candidate axis | Demotes to |
|---|---|
| Rhetorical stance (advocate / explain / explore / provoke) | `stance:` facet tag on Style (already encoded by `socratic-inquiry`, `dialectic`, `manifesto`) |
| Epistemic stance (certain / hedged / speculative) | `epistemic:` facet tag (splits across Tone and Voice; not selectable as an axis) |
| Register / formality | `formality:` ordinal facet tag on Tone (formality is the core of Tone already) |
| Medium / channel | Format `family`/`subfamily` plus a `channel:` facet tag |
| Persona-archetype | This is Voice; Voice families are grounded by communicative function and validated by the gate (Section 2a), with brand-archetype clusters kept only as a recognizability cross-reference |
| Output modality (prose / list / dialogue / verse) | `modality:` facet tag riding on Style; verse stays out of scope |

The test a top-level axis must pass: orthogonal to the others, the composer selects exactly one value per instruction, and it changes `llm_instruction_phrasing` independently. None of the six pass cleanly; all are better expressed as cross-cutting facets or subfamilies.

### 2. Controlled vocabulary: 5 format domains, 17 format families, 5 voice families

**Two new organizational fields, per-axis applicability:**

- `domain` - required on **formats only**. One of 5 values. Answers "in what sphere of life does this writing happen?"
- `family` - required on **formats and voices**. For formats, scoped to its domain. Answers "what structural or functional kind of writing is this?"

Tones and Styles receive neither field. They are register and rhetorical-pattern concepts that travel across spheres by nature (a `candid` tone works in Slack and in a eulogy; a `dialectic` style works in an op-ed and a sermon). They stay flat, organized only by the governed facet tags in section 4.

**The 5 format domains:** `professional`, `public`, `personal`, `ceremonial`, `contemplative`. (The domain formerly proposed as `relational` is renamed `personal` per A1/Q2, and its definition is widened to cover both its families - `correspondence`, written to someone the author knows, and `essay`, drawn from the author's lived experience for a wider readership. The unifying thread is the personal/relational source of the writing, not the size of the audience. Near miss for the placement algorithm: a personal essay published to strangers still belongs in `personal` because its subject is the writer's own experience, whereas a how-to guide or explainer addressed to a general audience belongs in `public` because its subject is the reader's task, not the writer's life. The full definition with this near-miss regression sentence is recorded under A1 in `decisions.md` and lands in `tools/taxonomy.py` during the Phase 1 migration.)

**The 17 format families, scoped to domain:**

| Domain | Families |
|---|---|
| `professional` (8) | `deliberation`, `instruction`, `progress`, `brief`, `appraisal`, `messaging`, `outreach`, `response` |
| `public` (4) | `broadcast`, `copy`, `position`, `accountability` |
| `personal` (2) | `correspondence`, `essay` |
| `ceremonial` (1) | `tribute` |
| `contemplative` (2) | `devotion`, `journal` |

(Count correction, 2026-06-19: the per-domain enumeration sums to 8 + 4 + 2 + 1 + 2 = **17**, not the "16" that earlier summary lines in this ADR, the v2 working doc, and the Fable review all carried. The enumeration has always listed 17; "16" was a propagated arithmetic error. Phase 1 codification (`tools/taxonomy.py`) encodes the enumerated 17, which is the binding count.)

**The 5 voice families (no domain):** `expert`, `care`, `principal`, `witness`, `dissident`. Voices carry no `domain` because a speaker travels across spheres: a `witness`-family voice can write a public broadcast, a professional brief, a personal essay, or a ceremonial tribute without ceasing to be that voice. (The originally proposed sixth family `pastoral` is folded into `care` as a subfamily per A1 and the grounding pass in Section 2a: by the functional test a pastoral voice performs the same communicative action as `care` - it accompanies, tends, and forms a reader - in a religious register, so it is a register variant of `care`, not a peer family. The `pastoral` voice entry keeps its slug and takes `family: care, subfamily: pastoral` at Phase 1 backfill.)

Family names are deliberately single-word and evocative of a writerly stance, not a functional-organizational label (the v1 names `decision-documents`, `reference-and-onboarding`, `quick-communication` were rejected for reading like column values). Format `family` is scoped to its `domain`, so a `family` value is unique only when paired with its domain; the validator and any consumer always carry both fields together.

### 2a. What grounds the voice families (and why not a personality typology)

The voice families were first justified loosely as "archetype clusters." A 2026-06-19 survey of established literary and psychological taxonomies (the run is summarized in the A1 record in `decisions.md`) found that no externally-validated framework can ground a discrete five-persona voice cut, because the validated science is the wrong shape:

- The personality frameworks that are empirically validated - Big Five / OCEAN and HEXACO - are **trait models**: continuous dimensions, not discrete persona types. They locate a writer on an axis; they do not partition writers into named families.
- The frameworks that do yield discrete personas - the Jung / Mark-Pearson brand archetypes, DISC, MBTI, Enneagram, Merrill-Reid Social Styles - are **practitioner conventions**, not validated science (MBTI and the Enneagram are actively contested). Adopting one would trade the maintainer's cut for a consultancy's cut: more familiar, not more objective.

So the families are grounded on the two standards the catalog actually owns, in this order:

1. **Communicative function (primary).** Each family names a distinct rhetorical action - the lens of Carolyn Miller's "genre as social action" and Searle's speech-act taxonomy. The catalog already describes families this way: `witness` reports and records what was seen; `dissident` holds a position against prevailing sentiment; `expert` speaks from having done the work; `care` accompanies and tends a reader; `principal` speaks from a defined role. Two families are kept distinct only if they perform distinct actions.
2. **Empirical distinguishability (the proof).** The E1 adherence gate's blind attribution test is the operative objectivity standard. A family is "real" when a blind judge can attribute its renders against its neighbors. This is a stronger warrant than matching any canon, and it is the standard A1's Q12 pilot began to supply.
3. **Archetype cross-reference (recognizability only).** The Jung / Mark-Pearson clusters (`expert` ~ Sage, `care` ~ Caregiver, `principal` ~ Ruler, `dissident` ~ Outlaw; `witness` is a composite Chronicler/Observer type) are retained in docs purely so the families read as familiar, and are cited as practitioner convention, never as scientific warrant.

The `pastoral` fold follows directly from standard 1: `pastoral` is not a distinct communicative function from `care` (both accompany, tend, and form a reader); it is `care` in a religious register, so it is a subfamily of `care`, not a sixth family. The same functional test is how future voice families are admitted or rejected. (A separate finding - that the one cleanly-validated external standard, NN/g's four tone dimensions, grounds the **Tone** axis rather than Voice - is logged for a future Tone pass and is out of scope here.)

### 3. Three levels: promote `subfamily` to a real third level

The v2 doc deferred a third level as premature at 30/axis. At the committed scale it is required, because the inventory already overflows. Promote the optional `subfamily` field to a real level:

- Formats: `domain (5) -> family (16) -> subfamily -> entry`. Example: `professional -> instruction -> reference -> api-doc` (and `professional -> instruction -> tutorial -> onboarding-walkthrough`).
- Voices: `family (5) -> subfamily -> entry`. Example: `witness -> chronicler -> historian`. The `pastoral` fold makes `care -> pastoral` the first named voice subfamily (`care -> pastoral -> {chaplain, spiritual-director, liturgist, ...}`), even though `care` has not yet crossed the 12-member trigger; it is a register-distinct cluster worth naming early.

`subfamily` is **optional until a family reaches 12 members, then required for every entry in that family.** Twelve is the v2 doc's existing "revisit" trigger, now made a hard schema threshold. On the aspirational inventory this immediately binds `instruction` (~19) and `witness` (~18), and will bind `deliberation` (~15), `broadcast` (~15), `correspondence` (~17), `tribute` (~16), and `devotion` (~17) as they fill. A family under 12 members may stay two-level. Minting a subfamily is governed like a tags-level change (cheap); it does not require an ADR, because it refines a neighbor set rather than re-cutting one.

### 4. Governed faceted-tag namespace

Today `tags` is a single open array. At scale that rots: contributors invent overlapping free-text labels and no validator can enforce structure. Split the field's two jobs:

- **`tags`** stays a free-text array, for search only. Unvalidated, unconstrained, never load-bearing.
- A **governed faceted-tag namespace** is introduced: tags of the form `facet:value` drawn from a closed enum. The facets are exactly the demoted fifth-axis concepts:

| Facet | Values (illustrative; the enum in `tools/taxonomy.py` is authoritative) |
|---|---|
| `channel:` | `slack`, `email`, `linkedin`, `op-ed`, `print`, ... |
| `formality:` | ordinal `1`-`5` |
| `modality:` | `prose`, `list`, `dialogue`, `table` |
| `epistemic:` | `certain`, `hedged`, `exploratory` |
| `length:` | `micro`, `standard`, `long` |
| `stance:` | `advocate`, `explain`, `explore`, `provoke` |
| `delivery:` | `spoken`, `written` |

A faceted tag (any string matching `^[a-z]+:`) is validated against the enum; an unknown facet prefix or an out-of-enum value fails validation. Free-text tags (no colon prefix) are never validated. **This is the single highest-leverage anti-rot mechanism in this ADR:** it lets the four axes stay frozen and Tones and Styles stay flat while still capturing every orthogonal dimension people will reach for, with a validator instead of a convention holding the line.

### 5. Enforcement: one vocabulary module, schema enums, one cross-field check

The controlled vocabulary lives in exactly one place: `tools/taxonomy.py`. It exports the domain list, the per-domain family lists, the per-family subfamily lists, and the faceted-tag facet/value enum. Schemas and validators reference it; nothing duplicates it (consistent with ADR 0013's single-source-of-truth doctrine).

Enforcement is the v2 doc's recommended Option 2 (separate enums plus a Python cross-field check), not a `oneOf` block:

1. **JSON Schema enums.** `format.schema.json` lists valid `domain`, `family`, and `subfamily` values as flat enums; `voice.schema.json` lists valid `family` and `subfamily`. JSON Schema alone cannot express "family belongs to domain," so the enums catch typos and the Python check catches membership.
2. **Python cross-field check.** Extend `tools/validate.py` with `check_taxonomy_membership()`: a format entry's `family` must belong to its `domain`; a `subfamily`, if present, must belong to its `family`; and `subfamily` must be present once the entry's family has 12 or more members. A voice entry's `family` and optional `subfamily` are checked the same way (no domain).
3. **Faceted-tag check.** The same validator pass rejects any `facet:value` tag outside the `tools/taxonomy.py` enum, while leaving free-text tags alone.

These join the existing 7 validate.py checks; all must pass before an entry ships.

### 6. Coverage ledger as a drift alarm

`build-indexes.py` emits a per-cell coverage report alongside `taxonomy.json`: for every domain/family/subfamily cell, three numbers - **target**, **filled**, and **gated-pass** (entries that have cleared the E1 adherence gate). Target bands are set by territory width, not a uniform quota: **dense families target 12-20** (`instruction`, `deliberation`, `correspondence`, `witness`); **narrow families target 3-8** (`messaging`, `journal`, `tribute`). The ledger turns "most comprehensive" into a number at every node and surfaces lopsided growth (a family ballooning past its band, a cell going stale) so re-cuts happen on signal, not vibes. It is a report, not a gate; it informs the maintainer, it does not block a build.

### 7. The adherence gate doubles as a de-duplication gate

The E1 gate (defined in the scaling strategy and backlog E1, not built by this ADR) is also the over-splitting police. **If two proposed sibling entries cannot produce blindly distinguishable output, they are not two entries - they are one entry plus a `confusable_with` note.** This prevents the catalog from minting near-synonyms to hit a coverage-ledger count: the ledger says "fill this cell," and the gate refuses to let it be filled with indistinguishable duplicates. Coverage targets create pull toward a number; the gate ensures the number is only ever reached with genuinely distinct entries. Splitting a subfamily is therefore not just a naming act; the resulting siblings must each clear the gate against each other or the split collapses back.

### 8. Scope boundaries

The aspirational inventory scopes out fiction, poetry, translation, children's writing, working journalism, legal/medical/scientific, and government/policy writing. This ADR holds the hard exclusions and admits two boundary cases, gate-arbitrated (per scaling decision-matrix row 6):

- **Hold out, firmly:** fiction, poetry, translation, children's writing. Separate crafts with their own conventions; the gate cannot cleanly judge "distinguishable" against literary intent, and admitting them dilutes the proven wedge.
- **Admit only if it clears the E1 gate and teaches register, not domain knowledge:** journalism (`news-brief`, `feature-lead`, `investigative-nut-graf`) as a `public` subfamily; and plain-language legal/medical (`plain-english-legal-summary`, `patient-instructions`) at the register boundary only. Full legal briefs and clinical notes stay out - they are domain expertise, not writing instruction.

Any admission of a scoped-out territory is a maintainer ADR decision arbitrated by the gate, never a mechanical add.

### 9. Migration: optional, then required

Backward-compatible, mirroring the additive-then-tightening pattern:

1. **Add fields optional.** Add `domain`, `family`, `subfamily` to the schemas as optional. Add `check_taxonomy_membership()` and the faceted-tag check to `validate.py` as **warnings**. Land the `tools/taxonomy.py` vocabulary with the v2 values. Existing entries continue to validate untouched.
2. **Backfill the 60.** Populate `domain` and `family` on every existing format and voice entry. The reviewed `stable` baseline keeps its `review_status` (this ADR does not touch lifecycle). Faceted tags are migrated from any existing free-text tags that map to a facet.
3. **Tighten to required.** Promote `domain` (formats) and `family` (formats and voices) from optional to required; promote validator warnings to errors. `subfamily` tightens per-family: it becomes required for a family the moment that family crosses 12 members, enforced by the cross-field check, not by a global schema flag.

The three-axis model (ADR 0001) and the atomic-folder pattern (ADR 0002) are unchanged: these are within-axis frontmatter fields, not a fifth axis and not a folder restructure.

## Consequences

### Positive

- **The gate's neighbor set is well-defined.** A tight family/subfamily tree gives the E1 adherence gate a sharp same-family render set, which is the precondition for scaling breadth without diluting distinguishability. This is the load-bearing payoff.
- **Heterogeneity becomes structured and scannable.** An RFC and a wedding toast stop looking like peer choices; three-click navigation (domain to family to entry, or to subfamily to entry) replaces an 800-row scroll.
- **Coverage is measurable.** The per-cell ledger attaches a number to "comprehensive" at every node and alarms on drift, replacing aspiration with instrumentation.
- **The four axes stay frozen while orthogonal dimensions are still capturable.** The faceted-tag namespace absorbs all six rejected fifth axes without re-opening ADR 0001 or burdening Tone/Style entries.
- **Anti-rot is deterministic.** One vocabulary module, schema enums, a cross-field check, and a faceted-tag enum mean no entry validates with an invented category or facet. The gate additionally polices over-splitting, so coverage targets cannot be gamed with near-synonyms.

### Negative

- **Per-entry curation now carries placement decisions.** Adding a format requires choosing a domain, a family, and (past 12 members) a subfamily. Edge cases (`whitepaper`, `recommendation-letter`, `meeting-notes`, `personal-essay`) will produce maintainer judgment calls; the v2 doc's edge-case table records the chosen placements and confidence.
- **The vocabulary is a binding contract.** Adding a new domain or family is a schema change requiring an ADR and a version bump, because it re-cuts everyone's nearest-neighbor set and therefore the gate. Adding a subfamily or an entry within a family is friction-free; expanding the top two levels is not.
- **Three levels multiply structure to hold in working memory.** Mitigated by making subfamily required only past 12 members, so most families stay two-level until they genuinely need the third.
- **Faceted-tag enum needs governance.** A new channel or stance value is a `tools/taxonomy.py` edit and should be reviewed, or the namespace re-rots into open free text by another name. This is cheaper than an ADR but is not zero.

### Neutral

- **Tones and Styles stay flat.** A deliberate design choice; they are domain-neutral. If either crosses 40 entries and a clustering emerges from real entries, a future ADR can revisit, preferring facets over a tree.
- **ADR 0001 remains foundational.** Domain, family, subfamily, and facets are all within-axis or cross-cutting; none is a fifth axis.
- **The E1 gate and the coverage ledger are referenced, not built here.** This ADR defines the structure they consume; their implementation is backlog item E1 and the `build-indexes.py` extension.
- **`review_status` lifecycle is untouched.** The gate-to-tier binding lives in the scaling strategy and `CLAUDE.md`, not here.

## Alternatives considered

- **Keep the v1 cut (6 domains, 14 functional families).** Rejected by maintainer feedback: business/workplace blurred under real entries, `authority` carried dominance connotations, and family names read as database columns. The superseded draft 0010 encodes this; this ADR replaces it.
- **Stay two-level (domain to family), defer subfamily again.** This is the v2 doc's own position, correct at 30/axis. Rejected at the committed scale because the inventory already overflows `instruction` and `witness` past 12 members; a flat family of 18 voices gives the gate a 17-way neighbor render that is both expensive and blunt.
- **Add a fifth top-level axis.** Rejected. Breaks ADR 0001, forces Tone/Style entries to declare an inapplicable value, and multiplies the composer's combinatorial space. The faceted-tag namespace delivers the same filterability at a fraction of the cost.
- **Keep `tags` as a single open array.** Rejected. Open tags rot into inconsistent overlapping labels at scale, and a validator cannot enforce structure on free text. The free-text-plus-governed-facet split keeps search flexible while making the orthogonal dimensions enforceable.
- **Encode domain-to-family as a JSON Schema `oneOf`.** Self-documenting but verbose and hard to evolve; it also cannot express the 12-member subfamily threshold. Rejected in favor of separate enums plus a Python cross-field check, with the vocabulary single-sourced in `tools/taxonomy.py`.
- **Drop the domain layer entirely, keep only evocative families.** Seriously considered (v2 Alternative 1). Rejected because domain-level queryability and coarse grouping are real and 5 domains is sustainable; dropping it later is non-breaking if it fails to earn its place.

## Open questions - resolution status at acceptance

Recorded against A1 ratification (2026-06-19). Resolutions live in `decisions.md`; the originals are kept below for context.

1. **Subfamily naming** - resolved by A1/Q7: keep the hard 12-member trigger, pre-design subfamily cuts for the known-fat families with a human naming checkpoint per split. The `care -> pastoral` subfamily is named now (Section 3).
2. **Faceted-tag enum scope** - open as decision A4 (P1, needed during v0.3.0): ship the 7 facet keys as a closed set, values widen on demand. Not blocking acceptance.
3. **Coverage target bands** - open as decision A5 (P1): the dense 12-20 / narrow 3-8 bands are the working proposal, tuned after first fill. Not blocking acceptance.
4. **Journalism placement** - resolved direction by E2: a `public` subfamily, not a sixth domain, admitted only if it clears the gate (E1). 
5. **Migration timing relative to E1** - resolved by F2: land the taxonomy optional, backfill the 60, stand up E1, then tighten to required. This ADR's Section 9 is that sequence.
6. **Twelve as the subfamily threshold** - resolved by A2/Q7: a hard, validator-enforced cutoff at 12, not a soft alarm. Q12's pilot supports 12 as workable; revisit only on gate evidence.

Originals, for context:

1. **Subfamily naming.** This ADR fixes the three levels and the 12-member trigger but does not enumerate subfamilies. The first binding cases are `instruction` (`reference` vs `tutorial` is the v2 doc's worked example) and `witness` (`chronicler` is named; the other ~17 voices need cuts). Approve the subfamily-naming pass as a follow-on working doc, gate-arbitrated, before mass-add into those two families?
2. **Faceted-tag enum scope.** Are the 7 facets (`channel:`, `formality:`, `modality:`, `epistemic:`, `length:`, `stance:`, `delivery:`) the right closed set, and are the illustrative value lists complete enough to seed `tools/taxonomy.py`, or should the initial enum start narrower and widen on demand?
3. **Coverage target bands.** Confirm the dense (12-20) and narrow (3-8) bands, and assign each of the 17 families to a band. The inventory implies the dense set (`instruction`, `deliberation`, `correspondence`, `broadcast`, `tribute`, `devotion`, `witness`); confirm `messaging`, `journal`, `copy`, `outreach`, `response`, `essay` as narrow.
4. **Journalism placement.** If journalism is admitted, is it a `public` subfamily (recommended, widening an existing domain) or its own sixth domain? A new domain is a heavier contract than a subfamily.
5. **Migration timing relative to E1.** This ADR's tighten-to-required step (migration phase 3) and the E1 gate are interdependent: the gate renders against family neighbors, so families should be populated before the gate runs at volume. Confirm the sequence: land this taxonomy (optional, then backfill), stand up E1, then tighten to required behind the gate.
6. **Twelve as the subfamily threshold.** Is 12 the right hard cutoff, or should it be a soft alarm in the coverage ledger with the maintainer deciding each split? A hard cutoff is enforceable; a soft one preserves judgment at the cost of determinism.

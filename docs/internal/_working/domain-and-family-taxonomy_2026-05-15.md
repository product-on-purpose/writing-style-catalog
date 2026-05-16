---
title: Domain and Family Taxonomy - Comprehensive Proposal
date: 2026-05-15
revised: 2026-05-16
version: 2
author: claude (Opus 4.7) in collaboration with jprisant
status: draft - awaiting user review (v2)
type: design-proposal
supersedes: v1 of this doc (same path, prior revision in git history)
related:
  - docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md
  - docs/internal/_working/plan-comparison_2026-05-15.md
  - docs/internal/_working/0010-domain-and-family-organization.md
  - docs/internal/adr/0001-three-axis-model.md
  - docs/internal/adr/0002-atomic-folder-pattern.md
  - schemas/format.schema.json
  - schemas/voice.schema.json
  - tools/taxonomy.py
---

# Domain and Family Taxonomy - Comprehensive Proposal (v2)

## What changed from v1

This is the second revision of this proposal. The first version (in git history under the same path) proposed 6 domains and 14 families derived from the ~30 candidate format entries already in the Phase 2 design spec. Maintainer feedback surfaced five concrete problems with that v1:

1. The candidate set was too narrow; a taxonomy derived from ~30 formats produces either thin families or arbitrary fits.
2. `business` vs `workplace` were too similar; the boundary kept blurring under real entries.
3. The voice family name `authority` carried wrong connotations.
4. The format family name `quick-communication` was descriptively flat.
5. Family naming generally felt functional-organizational rather than writerly-evocative.

This v2 addresses all five:

| v1 | v2 |
|---|---|
| ~30 candidate formats | ~70 candidate formats spanning professional, public, relational, ceremonial, and contemplative scopes |
| ~30 candidate voices | ~40 candidate voices including narrative, witness, dissident, and pastoral voices currently under-represented |
| 6 domains (engineering, business, workplace, publication, ceremonial, contemplative) | 5 domains (professional, public, relational, ceremonial, contemplative) - business and workplace collapsed into a unified `professional` |
| 14 format families with descriptive-functional names (`decision-documents`, `reference-and-onboarding`, `quick-communication`, etc.) | 16 format families with evocative single-word names (`deliberation`, `instruction`, `messaging`, `tribute`, `devotion`, etc.) |
| Voice family `authority` | Voice family `principal` (front-of-room voices that speak from a defined role) |
| Voice family `narrative-and-media` | Voice family `witness` (observational/narrative voices) |
| 5 voice families | 6 voice families (added `dissident` for challenging/contrarian voices, separated from `principal`) |

The aspirational scope expansion is the most important change. The repo's audience explicitly includes pastors, marketers, engineers, designers, and writers covering writing tasks from eulogies to ADRs. The v1 taxonomy was implicitly engineering-centric; v2 corrects that.

## Purpose of this document

The Phase 2 catalog expansion targets 30 entries per axis. At that scale, flat axis lists become noisy. A reader scanning the format axis sees RFC, slack message, eulogy, and wedding toast as peers; nothing in the structure signals that these entries serve fundamentally different writing contexts.

This document proposes a two-level organizational taxonomy (`domain` + `family`) to make heterogeneity *visible and structured* rather than hiding it in a flat list. It covers the full design space, not just the chosen recommendation: alternatives considered, edge cases enumerated, migration path defined, future-scale implications mapped, naming decisions defended.

This is a design proposal, not yet an ADR. If approved, ADR 0010 (draft at `docs/internal/_working/0010-domain-and-family-organization.md`) codifies it and Phase 1 schema codification absorbs the changes.

## Problem statement

The Phase 1 catalog at 15 entries per axis reads naturally. The flat lists are short enough to scan. The heterogeneity present at 15 entries (devotional-entry next to slack-message) is mild enough to feel deliberate rather than chaotic.

The Phase 2 candidate set expanded substantially in this v2. Looking at the expanded format list (~70 candidates), the catalog's intended reach is now visible:

- Engineering decision documents (ADR, RFC, design-doc, postmortem)
- Cross-functional workplace communication (slack-message, email, meeting-notes)
- Internal feedback and personnel writing (performance-review, job-description, recommendation-letter)
- Customer-facing communication (support-response, refund-email, escalation)
- Sales and outreach (sales-email, cold-outreach, proposal-cover-letter)
- Public broadcast posts (blog-post-long-form, linkedin-post, newsletter-issue)
- Marketing copy (landing-page-copy, ad-copy)
- Public position-taking (op-ed, public-statement, advocacy-letter, testimony)
- Public accountability writing (public-apology, security-advisory, status-page-update)
- Personal correspondence (thank-you-note, condolence-note, apology-letter)
- Long-form personal essay and memoir
- Ceremonial speech (eulogy, wedding-toast, retirement-speech, graduation-speech)
- Spiritual writing (devotional-entry, sermon, homily, prayer, lectionary-commentary)
- Private reflection (journal-entry)

A flat axis presenting these as peer choices is now visibly wrong. RFC and wedding-toast are not alternatives a writer considers for the same task. They belong to different spheres of writing entirely. The same heterogeneity surfaces on voices at scale: pragmatic-architect, pastoral, journalist, and caregiver are not peers either.

Tones and styles do not have this problem. They are register and rhetorical-pattern concepts that travel across spheres by nature: a candid tone works in slack and in wedding-toast; a dialectic style works in op-ed and in sermon.

## Design constraints

Any organizational taxonomy added to this catalog must satisfy:

1. **Schema-compatible** with the atomic-folder pattern (ADR 0002): the new fields go in frontmatter; the folder structure does not change.
2. **Backward-compatible** during migration: existing entries must continue to validate while the new fields are populated.
3. **Solo-maintainer-sustainable**: the controlled vocabulary must be small enough that a single person can hold it in their head.
4. **Composer-and-SDK-friendly**: any downstream tool consuming the catalog should be able to filter, group, and recommend using these fields.
5. **Curator-friendly**: when adding a new entry, choosing its domain and family should take seconds.
6. **Reader-friendly**: when browsing, the organization should match the reader's mental model of "what kind of writing am I doing right now?"
7. **Per-axis appropriate**: not all axes need organization; the proposal must justify per-axis decisions individually.
8. **Aspirationally scoped**: the controlled vocabulary should anticipate writing the catalog could plausibly grow into, not just what the catalog has at the next milestone.

The eighth constraint is new in v2 in response to maintainer feedback.

## Proposal summary

Two new optional-then-required fields, added per axis where they make sense:

- **`domain`** (required for formats only): one of 5 controlled values. Answers "in what sphere of life does this writing happen?"
- **`family`** (required for formats and voices): one of N controlled values, scoped to domain for formats. Answers "what structural or functional kind of writing is this?"

Tones and styles receive no organizational layer. Their flat structure is preserved by design.

## Why two-level, not one or three

### Why not one level

A single `category` field could compress domain and family into one (e.g., `professional-deliberation`). Simpler schema. But:

- Loses queryability: composers and SDKs cannot easily filter by domain alone ("show me all professional formats")
- Forces awkward names: `contemplative-devotional-writing` becomes unwieldy
- Conflates two genuinely different organizing questions: where (sphere) vs what-kind (structural pattern)

### Why not three levels

A three-level taxonomy (domain > family > subfamily) would allow finer distinctions: `professional > instruction > tutorial` vs `professional > instruction > reference`. But:

- The catalog at 30/axis does not yet contain enough entries to fill three-level cells without thinness
- Each additional level multiplies the curation decision per entry
- Solo-maintainer-sustainable constraint argues for minimum viable structure
- Future-proofing for a third level can be added later without breaking the two-level scheme (subfamily becomes optional)

### Why two

Two levels (domain + family) provides:

- A coarse axis (domain) for browse-by-context and high-level filtering
- A fine axis (family) for peer-grouping and within-family diff-pair pedagogy
- Schema simplicity: two enums, with family scoped to domain
- Naming clarity: each field has a clear, distinct job

## Field shapes and schema

### Frontmatter examples

Format entry:

```yaml
---
id: adr
axis: format
name: Architecture Decision Record
domain: professional
family: deliberation
version: 1.1.0
review_status: stable
tags: [decision, technical, retrospective-friendly]
---
```

Format entry, ceremonial:

```yaml
---
id: eulogy
axis: format
name: Eulogy
domain: ceremonial
family: tribute
version: 1.0.0
review_status: draft
tags: [spoken, public, occasion-bound]
---
```

Voice entry (family only, no domain):

```yaml
---
id: caregiver
axis: voice
name: Caregiver
family: care
---
```

Tone or style entry: no new fields. Existing frontmatter is unchanged.

### Schema enforcement

Two approaches; either is acceptable. Pick during Phase 1 implementation:

**Option 1: Pure JSON Schema with `oneOf`.** Encode the domain-to-family mapping as a `oneOf` block in `format.schema.json`. Self-documenting; one source of truth. More verbose.

**Option 2: JSON Schema for individual enums, Python validator for the cross-field constraint.** `format.schema.json` lists valid domains and valid families separately. `validate.py` adds a check that the entry's family belongs to its domain. Simpler schemas; the constraint logic lives in Python.

Option 2 is recommended. The controlled vocabulary lives in `tools/taxonomy.py` (already drafted at HEAD).

## The 5 domains, fully defined

### `professional`

**Definition:** Writing produced inside work. Includes engineering, product, design, marketing, sales, leadership, operations, HR, finance, customer-facing communication, internal coordination, and external partnership work. Audience: colleagues, customers, partners, stakeholders, vendors. The defining property is that the writing exists to advance, document, or coordinate paid work.

**Anchor examples:** ADR, slack message, performance review, customer support email, sales pitch.

**Fits when:** the writing happens because someone is doing their job.

**Does not fit when:** the writing addresses a public audience via a channel with its own conventions (that is `public`); is for someone the writer knows personally outside work (that is `relational`); is occasion-bound (that is `ceremonial`); is reflective or spiritual (that is `contemplative`).

**Why this is one domain instead of two:** v1 split this into `business` and `workplace`. The boundary kept blurring (status reports? performance reviews? meeting notes?) and produced edge-case friction that did not pay off in queryability. A unified `professional` domain with families that differentiate by purpose (deliberation, instruction, messaging, etc.) gives the same separation without the false split.

### `public`

**Definition:** Writing addressed to a general or open audience via channels with their own established conventions and reader expectations. The reader is not known personally to the writer; the channel mediates the relationship.

**Anchor examples:** blog post, LinkedIn post, op-ed, press release, public statement.

**Fits when:** the channel has reader-expectations independent of any organization. A LinkedIn post follows LinkedIn norms regardless of who posts.

**Does not fit when:** the writing is internal (that is `professional`); aimed at a known individual (that is `relational`); for an occasion with a defined audience (that is `ceremonial`).

**Why separate from `professional`:** public-channel writing follows external conventions (algorithm-aware length, platform-native form, public-record permanence) that are fundamentally different from internal work writing, even when marketing or comms teams produce the public-facing version.

### `relational`

**Definition:** Writing for a specific person or small group the writer knows personally. The relationship between writer and reader is direct and pre-existing.

**Anchor examples:** thank-you note, condolence note, apology letter, personal essay (when addressed to a specific reader or community of practice), recommendation letter.

**Fits when:** the writer could name the reader and the reader's situation in specific detail.

**Does not fit when:** the writer addresses a role or generic audience (that is `professional` or `public`); the writing is for an occasion with a defined audience (that is `ceremonial`).

**Why this exists as its own domain:** personal correspondence has fundamentally different constraints than work or public writing. The register, length, and conventions of a condolence note do not generalize. Bundling under `personal` (the prior candidate name) is too vague; `relational` names the defining quality - the relationship.

### `ceremonial`

**Definition:** Writing for specific occasions with defined audiences: weddings, funerals, milestones, public tributes, retirements, graduations. Often delivered spoken; often addresses an audience that is not the primary subject.

**Anchor examples:** eulogy, wedding toast, retirement speech, graduation speech, anniversary letter.

**Fits when:** the writing is occasion-bound and the moment of delivery shapes the form.

**Does not fit when:** the writing is *about* ceremonies but not for one (a post about wedding traditions is `public`); for an individual in private (that is `relational`).

**Why this exists as its own domain:** ceremonial writing has distinct constraints (brevity, the room, the moment, the audience's relationship to the subject) that do not generalize to other writing contexts.

### `contemplative`

**Definition:** Spiritual, devotional, meditative, reflective, or pastoral writing. Often first-person; often produced as a discipline rather than for a specific recipient.

**Anchor examples:** devotional entry, sermon, prayer, meditation, journal entry, lectionary commentary.

**Fits when:** the primary purpose is reflection, contemplation, spiritual formation, prayer, or pastoral teaching.

**Does not fit when:** the writing is *about* spirituality but for a public audience (a blog post on prayer practice is `public`); is part of an occasion (a wedding homily is `ceremonial`, even if spiritually framed).

**Why this is separate from `ceremonial`:** ceremonial writing is occasion-bound and outward-facing; contemplative writing is interior or community-of-practice-facing and often produced as a discipline. Distinct constraints.

### Domains *considered and rejected*

- **`academic`** - rejected because the catalog does not currently target academic writing. Could be added later if scope expands.
- **`legal`** - rejected for the same reason.
- **`journalism`** - rejected because journalism writing fits cleanly into `public` (or `professional` for internal-facing journalism work).
- **`government` / `civic`** - rejected; civic writing (advocacy letters, testimony) fits in `public`.
- **`creative` / `literary`** - rejected as a separate domain; long-form essay and memoir fit in `relational` (when addressed to a specific community of practice) or `public` (when broadcast).
- **Split `professional` into engineering / business / workplace** - rejected (this is the v1 cut); the family layer carries the load better.

## Format families - 16 families across 5 domains

The following enumeration places the expanded ~70 candidate format set into domain and family. Current 15 entries are marked with their entry-id slug; candidates from v1 design spec are marked with "v1 candidate"; new in v2 are marked with "new in v2".

### `professional` domain - 8 families

#### `deliberation`

Writing whose purpose is to record, propose, or argue for a substantive decision. The writer is taking a position the reader will weigh.

| Member | Status |
|---|---|
| `adr` | current |
| `prd` | current |
| `design-doc` | v1 candidate |
| `rfc` | v1 candidate |
| `whitepaper` | current |
| `postmortem` | new in v2 |
| `position-paper` | new in v2 |

#### `instruction`

Writing whose purpose is to teach, guide, or document so that a reader can act. Reference, tutorial, runbook, and onboarding shapes all sit here.

| Member | Status |
|---|---|
| `readme` | current |
| `technical-reference` | current |
| `runbook` | new in v2 |
| `api-doc` | new in v2 |
| `error-message` | v1 candidate |
| `microcopy` | v1 candidate |
| `faq` | v1 candidate |
| `onboarding-walkthrough` | v1 candidate |
| `lesson-plan` | new in v2 |
| `syllabus` | new in v2 |
| `curriculum-outline` | new in v2 |

#### `progress`

Writing whose purpose is to communicate ongoing state, change, or completion to a known internal audience.

| Member | Status |
|---|---|
| `changelog-entry` | current |
| `daily-standup` | current |
| `status-report` | current |
| `release-notes` | new in v2 |
| `okr-update` | new in v2 |
| `deprecation-notice` | new in v2 |
| `meeting-notes` | current |

#### `brief`

Writing whose purpose is to compress a proposal, summary, or framing into a small, dense, decision-supporting artifact.

| Member | Status |
|---|---|
| `one-pager` | current |
| `talk-abstract` | v1 candidate |
| `conference-proposal` | v1 candidate |
| `cover-letter` | new in v2 |
| `proposal-cover-letter` | new in v2 |
| `executive-brief` | new in v2 |

#### `appraisal`

Writing whose purpose is to evaluate a person's work, performance, or fit. The writer is rendering judgment.

| Member | Status |
|---|---|
| `performance-review` | v1 candidate |
| `peer-feedback-note` | v1 candidate |
| `360-feedback` | new in v2 |
| `recommendation-letter` | new in v2 |
| `interview-rubric` | new in v2 |
| `exit-summary` | new in v2 |
| `job-description` | new in v2 |

#### `messaging`

Writing that is short, two-way, real-time-adjacent, and assumes a known recipient or channel. The default form of everyday work communication.

| Member | Status |
|---|---|
| `slack-message` | current |
| `email` | current |

#### `outreach`

Writing that initiates contact with a recipient who has no prior relationship, with an intent to inform, persuade, or sell. One-way, sender-initiated.

| Member | Status |
|---|---|
| `sales-email` | new in v2 |
| `cold-outreach` | new in v2 |
| `customer-success-email` | new in v2 |

#### `response`

Writing produced in reply to inbound communication: support tickets, customer queries, escalations. The writer is reacting; the recipient is known to be in some kind of need or complaint state.

| Member | Status |
|---|---|
| `support-response` | new in v2 |
| `refund-email` | new in v2 |
| `escalation-reply` | new in v2 |

### `public` domain - 4 families

#### `broadcast`

Writing for an open audience through a channel that has its own conventions: blog platforms, social, newsletters, podcasts. The reader self-selects in.

| Member | Status |
|---|---|
| `blog-post-long-form` | current |
| `newsletter-issue` | v1 candidate |
| `linkedin-post` | v1 candidate |
| `tweet-thread` | current |
| `podcast-show-notes` | v1 candidate |

#### `copy`

Writing whose purpose is commercial persuasion delivered through marketing channels: landing pages, advertisements, sales pages. The reader is a prospect.

| Member | Status |
|---|---|
| `landing-page-copy` | new in v2 |
| `ad-copy` | new in v2 |
| `tagline` | new in v2 |

#### `position`

Public writing that takes a stance, makes an argument, or addresses a topic where the writer is identified with the position. The reader expects opinion.

| Member | Status |
|---|---|
| `op-ed` | new in v2 |
| `public-statement` | new in v2 |
| `advocacy-letter` | new in v2 |
| `testimony` | new in v2 |
| `press-release` | new in v2 |

#### `accountability`

Writing produced in response to having broken something, caused harm, or fallen short publicly. The form is shaped by needing to be seen taking responsibility.

| Member | Status |
|---|---|
| `public-apology` | new in v2 |
| `security-advisory` | new in v2 |
| `status-page-update` | new in v2 |
| `recall-notice` | new in v2 |

### `relational` domain - 2 families

#### `correspondence`

Personal letters, notes, and cards for someone the writer knows. Short to medium length; the relationship carries weight the writing does not have to manufacture.

| Member | Status |
|---|---|
| `thank-you-note` | new in v2 |
| `condolence-note` | new in v2 |
| `apology-letter` | new in v2 |
| `personal-letter` | new in v2 |
| `birthday-message` | new in v2 |
| `holiday-card` | new in v2 |

#### `essay`

Long-form personal writing addressed to a community of readers (often a community of practice) rather than to a general public. The writer is present in the prose.

| Member | Status |
|---|---|
| `personal-essay` | new in v2 |
| `memoir-excerpt` | new in v2 |
| `profile-piece` | new in v2 |
| `travel-writing` | new in v2 |

### `ceremonial` domain - 1 family

#### `tribute`

Occasion-bound speech, typically delivered aloud, that honors a person or marks a transition. Brief by convention; the moment of delivery shapes the form.

| Member | Status |
|---|---|
| `eulogy` | v1 candidate |
| `wedding-toast` | v1 candidate |
| `retirement-speech` | new in v2 |
| `anniversary-letter` | new in v2 |
| `graduation-speech` | new in v2 |

### `contemplative` domain - 2 families

#### `devotion`

Spiritual, devotional, or pastoral writing produced as a discipline of formation, prayer, or teaching. Often first-person or first-person-plural.

| Member | Status |
|---|---|
| `devotional-entry` | current |
| `sermon` | new in v2 |
| `homily` | new in v2 |
| `prayer` | new in v2 |
| `meditation` | new in v2 |
| `lectionary-commentary` | new in v2 |

#### `journal`

Private or semi-private reflective writing whose primary reader is the writer or a close circle.

| Member | Status |
|---|---|
| `journal-entry` | new in v2 |
| `morning-pages` | new in v2 |

### Format summary at expanded scale

- 5 domains
- 16 families
- ~75 candidate format entries

Family member counts are more balanced than v1: most families have 3-7 members. The thinnest cells (`tribute` at 5, `journal` at 2, `messaging` at 2) are deliberately small because their content territory is narrow.

The catalog will not build all 75 candidate entries in Phase 2. The Phase 2 target remains 30 per axis. The taxonomy is sized to the territory the catalog could plausibly grow into, not to the next milestone count.

## Voice families - 6 families

Voices receive a `family` field but no `domain`. Speakers travel across domains: a `journalist` voice can write a public blog post, a professional brief, a relational essay, or a ceremonial tribute without ceasing to be a journalist voice.

### `expert`

Voices that signal deep practitioner knowledge in a craft or specialized field. The reader trusts the writer because the writer has done the work.

| Member | Status |
|---|---|
| `pragmatic-architect` | current |
| `technical-writer` | current |
| `researcher` | current |
| `senior-consultant` | current |
| `operator` | current |
| `product-thinker` | current |
| `ethicist` | new in v2 |
| `primer-author` | new in v2 (beginner-explainer) |
| `artisan` | new in v2 |
| `curator` | new in v2 |

### `care`

Voices oriented around tending to, developing, or accompanying other people. The reader feels seen.

| Member | Status |
|---|---|
| `coach` | current |
| `friendly-mentor` | current |
| `caregiver` | current |
| `elder` | new in v2 |
| `advocate` | new in v2 |
| `chaplain` | new in v2 |

### `principal`

Voices that speak from a defined role with positional clarity. Not authoritative in the sense of dominating; principal in the sense of "speaking on behalf of," "in front of the room," "publicly accountable for the words." Replaces v1's rejected `authority`.

| Member | Status |
|---|---|
| `executive` | current |
| `direct-communicator` | current |
| `defender` | new in v2 |
| `spokesperson` | new in v2 |

### `witness`

Observational and narrative voices. The writer reports, records, or recounts what was seen. Includes journalistic, documentary, and chronicling voices.

| Member | Status |
|---|---|
| `journalist` | current |
| `storyteller` | current |
| `columnist` | current |
| `satirist` | new in v2 |
| `naturalist` | new in v2 |
| `historian` | new in v2 |
| `profiler` | new in v2 |
| `chronicler` | new in v2 |
| `outsider` | new in v2 |
| `insider-confidant` | new in v2 |

### `dissident`

Voices that challenge, contradict, or hold a position against prevailing sentiment. The writer is taking a stance the reader may resist.

| Member | Status |
|---|---|
| `contrarian` | new in v2 |
| `polemicist` | new in v2 |
| `skeptic` | new in v2 |
| `whistleblower` | new in v2 |

### `pastoral`

Voices oriented around faith, formation, or pastoral care. Speaks from within a tradition.

| Member | Status |
|---|---|
| `pastoral` | current |
| `prophet` | new in v2 |
| `mystic` | new in v2 |

### Voice family summary

- 6 families
- ~40 candidate voice entries
- Most families have 4-10 members

Naming: the v2 names (`expert`, `care`, `principal`, `witness`, `dissident`, `pastoral`) are single-word and evocative of a writerly stance rather than a functional role. They read more like character archetypes than personnel categories.

## Why tones and styles receive no organization layer

Tones are registers: candid, warm, urgent, empathetic, resolute, playful. Their defining property is that they are *not* tied to a context or sphere. A `candid` tone works in a slack message, a wedding toast, a sermon, and a P0 incident report.

Imposing a domain or family on tones would either produce arbitrary groupings or force entries into multiple families (defeating the point of single-membership organization). Existing implicit grouping for tones (warm/empathetic/caring cluster vs candid/direct/resolute cluster) is observable in cross-references and does not need to be schematized.

Styles are rhetorical patterns. Like tones, they are domain-neutral; a `dialectic` style works in academic writing, engineering decisions, pastoral teaching, and ceremonial reflection. Informal style clusters exist (expository styles, argumentative styles, narrative styles) but the boundaries are fuzzy.

**Recommendation: leave tones and styles flat.** Revisit if either count crosses 40 *and* a coherent clustering emerges from actual entries; even then, prefer tags over schema fields.

## Edge cases and judgment calls

These are the placements where reasonable curators could disagree.

### `meeting-notes`

- **Chosen:** professional/progress
- **Alternative considered:** own family `meetings`
- **Reasoning:** at v1's 14-family structure, `meetings` was its own family with one member, which was thin. v2 folds meeting-notes into `progress` because the dominant purpose is reporting what happened in the meeting forward to non-attendees. If `meeting-agenda` and `meeting-brief` are later added, a `meetings` family can split out.
- **Confidence:** medium.

### `daily-standup`

- **Chosen:** professional/progress
- **Reasoning:** standups are short-cycle progress reports. v1 placed this in engineering/status; v2 maintains the progress family but now under unified `professional`. Use across non-engineering teams is real, so the engineering-domain framing in v1 was constraining.
- **Confidence:** high.

### `prd`

- **Chosen:** professional/deliberation
- **Alternative considered:** own family `product-specs`
- **Reasoning:** PRDs are decision-supporting artifacts that argue for a product direction. Family `deliberation` already covers this shape; a product-specs family is not worth the split.
- **Confidence:** high.

### `whitepaper`

- **Chosen:** professional/deliberation
- **Alternative considered:** public/broadcast
- **Reasoning:** Whitepapers are decision-influencing artifacts published to a public audience that the author wants to be cited by. v2 places them in `professional/deliberation` because the form is decision-document-shaped and the publication context is incidental. If marketing-whitepapers become distinct (more sales-oriented), they can move to public/copy.
- **Confidence:** medium.

### `op-ed`

- **Chosen:** public/position
- **Alternative considered:** professional/deliberation
- **Reasoning:** an op-ed is public position-taking, not internal decision recording. The audience is general; the writer is identified with the position.
- **Confidence:** high.

### `personal-essay`

- **Chosen:** relational/essay
- **Alternative considered:** public/broadcast
- **Reasoning:** the canonical personal essay is addressed to a community of practice (other writers, readers of a specific magazine), not to a general public. When personal essay is published broadly (a long Substack post), it can also fit public/broadcast. The placement reflects the dominant convention.
- **Confidence:** medium.

### `recommendation-letter`

- **Chosen:** professional/appraisal
- **Alternative considered:** relational/correspondence
- **Reasoning:** recommendation letters are evaluative judgments produced in a professional context, even when written about a friend. The appraisal family captures the judgment-rendering shape.
- **Confidence:** medium.

### `condolence-note`

- **Chosen:** relational/correspondence
- **Alternative considered:** ceremonial/tribute
- **Reasoning:** condolence notes are addressed privately to a known individual at a hard moment; they are not occasion-bound speech for an audience. Distinct from a eulogy.
- **Confidence:** high.

### `prayer` and `meditation`

- **Chosen:** contemplative/devotion
- **Alternative considered:** contemplative/journal
- **Reasoning:** prayers and meditations may be written privately but are typically composed as a discipline of formation, often shared, often used liturgically. Distinct from journal-entry which is more loosely reflective.
- **Confidence:** medium.

### `eulogy` and `wedding-toast`

- **Chosen:** ceremonial/tribute
- **Reasoning:** core members of the tribute family; both are occasion-bound speeches that honor a person or transition.
- **Confidence:** high.

### Edge cases that disappear vs v1

In v1, several edge cases existed because of the business/workplace split:
- "Is performance-review business or workplace?" - in v2, both are simply professional/appraisal.
- "Is status-report business or workplace?" - in v2, professional/progress.
- "Is slack-message workplace, and is performance-review business?" - in v2, both are professional with different families.

The business/workplace split caused friction without payoff. Collapsing it into `professional` resolves these.

## Alternative taxonomies considered

### Alternative 1: Drop the domain layer entirely

Use only `family` with evocative names. No `domain` field.

- **Pro:** simpler schema; family names are evocative enough to navigate directly
- **Pro:** removes the v1 business/workplace problem entirely
- **Con:** loses queryability ("show me all professional writing" requires multi-family selection)
- **Con:** index pages and composer UI lose a useful coarse-level grouping

**Verdict:** seriously considered. Rejected because the queryability and grouping benefits are real, and 5 domains is a small enough vocabulary to be sustainable. If practice shows domain is not earning its place, dropping it later is non-breaking (mark optional, then remove).

### Alternative 2: Single-level `category`

A flat `category` field per axis, with values like `professional-deliberation`, `ceremonial-tribute`.

- **Pro:** simplest schema
- **Con:** loses queryability; awkward names; conflates two questions

**Verdict:** rejected (same reasoning as v1).

### Alternative 3: Three-level `domain > family > subfamily`

Add a third level for finer distinctions.

- **Pro:** maximum expressiveness
- **Con:** thin cells at current scale; over-engineering for solo maintenance

**Verdict:** rejected for now; forward-compatible with subfamily added later as optional.

### Alternative 4: v1's 6-domain cut (business/workplace split)

The v1 proposal with `engineering`, `business`, `workplace`, `publication`, `ceremonial`, `contemplative` and 14 functional families.

- **Pro:** more queryable at the domain level (engineering vs business vs workplace)
- **Con:** business/workplace boundary blurred under real entries; maintainer rejected the cut
- **Con:** functional family names felt organizational rather than writerly

**Verdict:** rejected after maintainer feedback. v2 collapses business/workplace into `professional` and renames families.

### Alternative 5: Tag-based organization only

Use the existing `tags` array rigorously, with conventions for domain-like and family-like attributes.

- **Pro:** no schema change
- **Con:** organization-by-convention is fragile; contributors will tag inconsistently
- **Con:** validators cannot enforce taxonomic structure on free-form tags

**Verdict:** rejected as the primary mechanism. Tags remain available for cross-cutting attributes (`spoken`, `external`, `occasion-bound`).

### Alternative 6: A fifth top-level catalog axis

Add a new top-level axis ("domain" or "context") to the existing four.

- **Pro:** maintains axis-only structure
- **Con:** breaks the three-axis model (ADR 0001)
- **Con:** every entry on every axis must declare a domain, even tones/styles where it does not apply

**Verdict:** rejected. The three-axis model is foundational.

## How browsing and picking change

### Current state (flat axes)

`docs/reference/index.md` renders four flat axis tables. A reader scrolls each table.

### After taxonomy (hierarchical formats and voices)

`docs/reference/index.md` renders:

```
Formats
├── professional
│   ├── deliberation (7): adr, prd, design-doc, rfc, whitepaper, postmortem, position-paper
│   ├── instruction (11): readme, technical-reference, runbook, api-doc, ...
│   ├── progress (7): changelog-entry, daily-standup, ...
│   ├── brief (6): one-pager, talk-abstract, ...
│   ├── appraisal (7): performance-review, ...
│   ├── messaging (2): slack-message, email
│   ├── outreach (3): sales-email, cold-outreach, customer-success-email
│   └── response (3): support-response, refund-email, escalation-reply
├── public
│   ├── broadcast (5): blog-post-long-form, newsletter-issue, ...
│   ├── copy (3): landing-page-copy, ad-copy, tagline
│   ├── position (5): op-ed, public-statement, ...
│   └── accountability (4): public-apology, ...
├── relational
│   ├── correspondence (6): thank-you-note, condolence-note, ...
│   └── essay (4): personal-essay, memoir-excerpt, ...
├── ceremonial
│   └── tribute (5): eulogy, wedding-toast, ...
└── contemplative
    ├── devotion (6): devotional-entry, sermon, ...
    └── journal (2): journal-entry, morning-pages

Voices
├── expert (10): pragmatic-architect, technical-writer, researcher, ...
├── care (6): coach, friendly-mentor, caregiver, ...
├── principal (4): executive, direct-communicator, ...
├── witness (10): journalist, storyteller, columnist, ...
├── dissident (4): contrarian, polemicist, ...
└── pastoral (3): pastoral, prophet, mystic

Tones (15)
├── (flat list)

Styles (15)
├── (flat list)
```

That nested structure makes RFC and eulogy feel like distant cousins (which they are) rather than peers in a flat list (which they aren't).

For the future composer SPA, a domain selector becomes the first format picker filter, then family, then specific entry. Three clicks instead of one long scroll.

For SDK and MCP queries:

```typescript
// All professional formats
catalog.formats.filter(f => f.domain === 'professional');

// All deliberation formats (across domains - in practice all in professional)
catalog.formats.filter(f => f.family === 'deliberation');

// Voices grouped by family
catalog.voices.groupBy(v => v.family);
```

## Cross-reference relationship

The proposed taxonomy strengthens cross-reference semantics:

- **Within-family cross-references become more powerful.** Diff-pairs that contrast two members of the same family (`adr` vs `rfc` within deliberation, `coach` vs `friendly-mentor` within care) produce the sharpest pedagogical contrasts.
- **Cross-family cross-references remain valuable.** `pairs_well_with` continues to capture good combinations across axes; family membership does not constrain this.
- **The `confusable_with` field becomes most semantically tight.** Confusable entries are typically same-family.

**Recommendation in Phase 5 (diff-pairs):** prefer within-family diff-pairs as the sharpest pedagogical contrast.

## Migration plan

The taxonomy fits the design spec's existing 8-phase plan without restructuring it. Revisions per phase:

### Phase 0 (exemplar craft) - light revision

The 5 exemplars (whitepaper, socratic-inquiry, confessional, caregiver, pragmatic-architect) each get domain and family populated. With v2 names:
- whitepaper → professional/deliberation
- caregiver → voice family `care`
- pragmatic-architect → voice family `expert`

Stress-tests the taxonomy at 5 entries before broader rollout.

### Phase 1 (schema codification) - additive

- Add `domain` (formats only) and `family` (formats and voices) to schemas as optional initially
- Add `check_taxonomy_membership()` to `validate.py` as warnings initially
- Controlled vocabularies live in `tools/taxonomy.py` (already drafted; will need update to v2 values before Phase 1 ships)
- Update `build-indexes.py` to render `docs/reference/index.md` hierarchically
- Write ADR 0010 (already drafted at `_working/0010-domain-and-family-organization.md`; will need update to v2 values before promotion)

### Phase 2 (audit-and-upgrade existing 55) - includes backfill

The audit pass populates domain and family on every existing format and voice entry. Exemplars from Phase 0 are templates. After Phase 2, fields tighten from optional to required.

### Phase 3 (generate 60 new entries) - taxonomy-aware curation

The 60 new entries are selected with family balance as a criterion, not just axis balance. Implication: the per-axis curation rationale (Phase 6d) becomes a per-domain-and-family rationale for formats.

### Phase 5 (diff-pair expansion) - within-family focus

Diff-pair selection criterion: prefer within-family confusables for sharpest pedagogy.

### Phase 6d (per-axis curation rationale) - restructured around taxonomy

Format curation doc structures around 5 domains and 16 families. Voice curation doc structures around 6 families. Tone and style curation docs remain flat.

## Future scale considerations

### At 60 entries per axis (next-next milestone)

- Format families approach 5 average members; some families may split (e.g., `instruction` could bifurcate into `reference` and `tutorial`)
- Voice families approach 10 average members; clearer subdivisions emerge
- New domains may become warranted (e.g., `academic` or `civic`)
- Subfamily layer may pay off

### At 200 entries per axis (aspirational)

- Two-level taxonomy becomes insufficient; subfamily needed
- Composer UX needs progressive disclosure: domain > family > subfamily > entry

The current proposal does not preclude any of this. Adding a third level later requires only making `subfamily` optional in the schema.

### Triggers to revisit

- Format axis reaches 50 entries
- Any single family exceeds 12 members
- A new domain becomes warranted (entry list shows clear cluster not fitting existing 5)
- Composer or SDK users report navigation friction

## Naming decisions defended (v2)

### Why `domain` and not `sphere` / `context` / `area` / `realm`

Standard taxonomy term; clear meaning; no overload with existing repo concepts.

### Why `family` and not `cluster` / `archetype` / `kind` / `category`

`family` implies bounded membership and peer relationship; matches the goal.

### Why family names are single-word and evocative in v2

The v1 family names (`decision-documents`, `reference-and-onboarding`, `quick-communication`) were descriptive-functional. Maintainer feedback: they read like database column values, not like categories a writer would orient themselves with.

The v2 family names (`deliberation`, `instruction`, `messaging`, `tribute`, `devotion`, `witness`, `dissident`) are mostly single-word and evoke a writerly stance or shape:

- `deliberation` evokes weighing and choosing, the actual cognitive work of decision documents
- `instruction` evokes teaching and guiding, broader than "reference and onboarding"
- `messaging` evokes the back-and-forth of slack and email naturally
- `tribute` evokes honor and occasion, more apt than "toasts and tributes"
- `devotion` evokes a discipline of formation, broader than "devotional writing"
- `witness` evokes the journalistic stance of seeing and recording
- `dissident` evokes the act of holding a position against prevailing sentiment
- `principal` evokes "speaking from a position" without the dominance baggage of "authority"

A few names remain compound where the concept is genuinely two-part: `messaging` works alone, but if a single-word alternative does not improve clarity, compound is acceptable.

### Why `principal` instead of `authority`

`authority` carries connotations of dominance and hierarchy. The voices in this family (executive, direct-communicator, defender, spokesperson) are not really about authority; they are about positional clarity, decisiveness without hedging, and speaking on behalf of a role.

`principal` evokes "speaking in front of the room" or "principal investigator" or "first speaker" - someone in a defining position without the dominance valence.

Alternatives considered:
- `decisive` - too narrow (other voices can be decisive too)
- `positional` - clinical
- `command` - even more hierarchical than authority
- `front-of-room` - evocative but compound
- `office-holder` - too tied to formal organizations

`principal` won.

### Why `messaging` instead of `quick-communication`

`quick-communication` is functionally accurate but flat. `messaging` is the noun-form of the everyday practice: people *message* each other. Slack, email, and adjacent forms are messaging. The name evokes the genre directly.

### Why family is scoped to domain (for formats) rather than global

Global family names would collide across domains (e.g., `essay` in `relational` is a different shape than `whitepaper` in `professional/deliberation`). Scoping family to domain allows shorter, clearer family names within each domain context.

Trade-off accepted: an entry's family value alone is not globally unique without the domain qualifier. The validator and composer always carry both fields together.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Curators disagree on placements for edge cases | Edge-cases table in this doc documents chosen placements; ADR 0010 captures rationale |
| Taxonomy feels arbitrary to a reader | Per-axis curation rationale (Phase 6d) makes the logic explicit |
| New formats do not fit existing families | Adding a new family is a small schema change; adding a new domain is bigger. Process documented in `schema-evolution-policy.md` (Phase 6c) |
| Solo maintainer drifts on family assignments over time | Validator enforces controlled vocabulary; new entries cannot pass with non-existent family |
| Two-level scheme insufficient at 60+ entries | Subfamily can be added later as optional |
| v2 family names age poorly | Names are revisable; ADR 0010 captures the rationale so future renames preserve intent |
| Schema changes regress existing validators | Phase 1 adds fields as optional warnings first; tighten only after Phase 2 backfill |
| The expanded candidate list misrepresents scope | Maintainer review of v2 expanded list (this doc) catches this before Phase 3 selects 60 new entries to build |

## Open questions for jprisant

1. **Domain count: 5 acceptable?** Or do you want to keep `professional` split somehow? Or merge `ceremonial` and `contemplative` into one `sacred` or `ritual` domain?
2. **Family naming - any v2 names still read wrong?** `messaging`, `outreach`, `response`, `accountability`, `tribute`, `devotion`, `witness`, `dissident`, `principal`, `correspondence`, `essay` are the most negotiable. Suggest alternatives if any feel off.
3. **The expanded format list - is the scope right?** Anything missing that the catalog should aspirationally cover (e.g., medical writing, legal briefs, government memos, parenting writing)? Anything that should not be in scope?
4. **The expanded voice list - is the scope right?** Voices currently missing that should be added or aspirationally noted?
5. **Edge cases - reassign any?** Especially `whitepaper`, `personal-essay`, `recommendation-letter`, `meeting-notes` where confidence is medium.
6. **Drop domain entirely (Alternative 1)?** Seriously considered but rejected; if you'd prefer the simpler one-layer-only structure with just family, the change is mechanical.
7. **Per-axis curation rationale (Phase 6d) - one doc per axis, or one doc per domain for formats?** Per-domain may be more readable (5 small docs) but produces more files.

## Recommended next steps

1. Read this v2 and answer the 7 open questions.
2. If approved: update ADR 0010 draft (`_working/0010-domain-and-family-organization.md`) to v2 domain and family values; update `tools/taxonomy.py` to v2 controlled vocabularies; update Phase 0 exemplar candidates doc to v2 family names where they reference family membership.
3. If revisions: I update this doc, re-circulate, and only then update downstream artifacts.
4. Once design spec + this proposal are both approved: invoke writing-plans skill to produce the task-level implementation plan, with v2 taxonomy integrated.

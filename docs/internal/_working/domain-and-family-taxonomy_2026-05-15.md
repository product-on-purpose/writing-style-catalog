---
title: Domain and Family Taxonomy - Comprehensive Proposal
date: 2026-05-15
author: claude (Opus 4.7) in collaboration with jprisant
status: draft - awaiting user review
type: design-proposal
supersedes: none
related:
  - docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md
  - docs/internal/_working/plan-comparison_2026-05-15.md
  - docs/internal/adr/0001-three-axis-model.md
  - docs/internal/adr/0002-atomic-folder-pattern.md
  - AGENTS.md
  - schemas/format.schema.json
  - schemas/voice.schema.json
  - schemas/tone.schema.json
  - schemas/style.schema.json
---

# Domain and Family Taxonomy - Comprehensive Proposal

## Purpose of this document

The Phase 2 catalog expansion (see `phase-2-catalog-expansion_2026-05-15.md`) targets 30 entries per axis. At that scale, flat lists become noisy. A reader scanning the format axis sees RFC, slack-message, eulogy, and wedding-toast as peers; nothing in the structure signals that these entries serve fundamentally different writing contexts.

This document proposes a two-level organizational taxonomy (`domain` + `family`) to make heterogeneity *visible and structured* rather than hiding it inside a flat axis list. It covers the full design space, not just the chosen recommendation: alternatives considered, edge cases enumerated, migration path defined, future-scale implications mapped, naming decisions defended.

This is a design proposal, not yet an ADR. If approved, an ADR follows (likely `0010-domain-and-family-organization.md`) and the design spec's Phase 1 (schema codification) absorbs the schema changes.

## Problem statement

At 15 entries per axis, the catalog reads naturally. The 15 formats currently in the catalog mostly cohere around workplace and engineering use cases, with `devotional-entry` as a deliberate outlier per ADR 0006 (anchor topic selection).

At 30 entries per axis, the proposed additions widen the catalog significantly. The format axis would span:

- Engineering decision documents (ADR, design-doc, RFC, whitepaper)
- Cross-functional workplace communication (slack-message, email, meeting-notes)
- Public/external publishing (blog-post-long-form, linkedin-post, podcast-show-notes)
- Personal feedback (performance-review, peer-feedback-note)
- Ceremonial speech (eulogy, wedding-toast)
- Contemplative writing (devotional-entry)

A flat axis presenting these as peer choices is not just visually noisy; it misrepresents the catalog's structure. RFC and wedding-toast are not alternatives a writer considers for the same task. They belong to different *spheres* of writing entirely.

The same heterogeneity will surface on the voice axis at 30 entries: pragmatic-architect, pastoral, journalist, and caregiver are not really peers either.

Tones and styles do not have this problem; they are register and rhetorical-pattern concepts that travel across spheres by nature.

## Design constraints

Any organizational taxonomy added to this catalog must satisfy:

1. **Schema-compatible** with the atomic-folder pattern (ADR 0002): the new fields go in frontmatter; the folder structure itself does not change.
2. **Backward-compatible** during migration: existing entries must continue to validate while the new fields are being populated.
3. **Solo-maintainer-sustainable**: the controlled vocabulary must be small enough that a single person can hold it in their head and apply it consistently.
4. **Composer-and-SDK-friendly**: any downstream tool that consumes the catalog should be able to filter, group, and recommend using these fields without complex traversal.
5. **Curator-friendly**: when adding a new entry, choosing its domain and family should take seconds, not require committee discussion.
6. **Reader-friendly**: when browsing the catalog, the organization should match the reader's mental model of "what kind of writing am I doing right now?"
7. **Per-axis appropriate**: not all axes need organization; the proposal must justify per-axis decisions individually.

## Proposal summary

Two new optional-then-required fields, added per axis where they make sense:

- **`domain`** (required for formats only): one of 6 controlled values. Answers "in what sphere of life does this writing happen?"
- **`family`** (required for formats and voices): one of N controlled values, scoped to domain for formats. Answers "what structural or functional kind of writing is this?"

Tones and styles receive no organizational layer. Their flat structure is preserved with deliberate reasoning (see below).

## Why two-level, not one or three

### Why not one level

A single `category` field could compress domain and family into one (e.g., `engineering-decision-documents`). Simpler schema. But:

- Loses queryability: composers and SDKs cannot easily filter by domain alone (e.g., "show me all engineering formats")
- Forces awkward names: `contemplative-and-ceremonial-tributes` is unwieldy
- Conflates two genuinely different organizing questions: where and what-kind

### Why not three levels

A three-level taxonomy (domain > family > subfamily) would allow finer distinctions: `engineering > decision-documents > forward-looking` vs. `engineering > decision-documents > retrospective`. But:

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

Format entry (new fields shown):

```yaml
---
id: adr
axis: format
name: Architecture Decision Record
domain: engineering
family: decision-documents
version: 1.1.0
review_status: stable
tags: [decision, technical, retrospective-friendly]
created: 2026-05-10
author: jprisant
# ... existing pedagogical fields ...
---
```

Format entry, ceremonial:

```yaml
---
id: eulogy
axis: format
name: Eulogy
domain: ceremonial
family: toasts-and-tributes
version: 1.0.0
review_status: draft
tags: [spoken, public, occasion-bound]
# ...
---
```

Voice entry (family only, no domain):

```yaml
---
id: caregiver
axis: voice
name: Caregiver
family: people-and-coaching
# ...
---
```

Tone or style entry: no new fields. Existing frontmatter is unchanged.

### Schema enforcement

Two approaches; either is acceptable. Pick during Phase 1 implementation:

**Option 1: Pure JSON Schema with `oneOf`.** Encode the domain-to-family mapping as a `oneOf` block in `format.schema.json`. Self-documenting; one source of truth. More verbose.

**Option 2: JSON Schema for individual enums, Python validator for the cross-field constraint.** `format.schema.json` lists valid domains and valid families separately. `validate.py` adds a check that the entry's family belongs to its domain. Simpler schemas; the constraint logic lives in Python.

Option 2 is recommended because the `validate.py` cross-check pattern is already established (see `check_cross_references()`), the schema files stay readable, and the controlled vocabulary lives in one Python dict that is easy to evolve.

### Validator additions

`validate.py` gains two checks:

- `check_domain_valid()`: every format entry has a `domain` value in the controlled list; every voice entry has a `family` value in the controlled list
- `check_family_scoped_to_domain()`: every format entry's `family` belongs to the family list valid for its `domain`

Both checks are optional during Phase 1 (warn) and required after Phase 2's audit completes (error).

## Domain - the 6 values, fully defined

### `engineering`

**Definition:** Writing produced inside or about software engineering, product management, and design technical work. The audience is technical practitioners or stakeholders to technical work.

**Anchor examples:** ADR, RFC, design doc, technical reference, error message.

**Fits when:** the writing exists to advance, document, or align around a technical artifact, decision, or operational concern.

**Does not fit when:** the writing is about engineering work but framed for a general business audience (that is `business`), or aimed at customers in a marketing register (that is `publication`).

### `business`

**Definition:** Writing produced inside marketing, sales, leadership, operations, HR, or finance functions. Cross-functional in the sense that it crosses these business sub-functions, but does *not* primarily serve engineering work.

**Anchor examples:** one-pager, talk abstract, performance review, executive briefing memo.

**Fits when:** the writing exists to inform a business decision, align stakeholders outside engineering, or document a non-technical commitment.

**Does not fit when:** the writing is engineering-decision-focused (that is `engineering`), or aimed at a public audience (that is `publication`).

**Note on bundling:** marketing, leadership, ops, HR, and finance are deliberately bundled. Splitting them is tempting but produces thin families. Revisit if the catalog crosses ~60 business-domain entries.

### `workplace`

**Definition:** Cross-functional work communication that genuinely crosses the engineering / business divide. Conversational, fast-cycle, applies to everyone in a knowledge-work organization.

**Anchor examples:** slack message, email, meeting notes, onboarding walkthrough.

**Fits when:** the format is used identically by an engineer, a marketer, a designer, and an executive.

**Does not fit when:** the format is functionally specific (PRD is `engineering`; sales-call notes is `business`).

**Why this exists as its own domain:** email and slack are formats whose conventions cross all work disciplines. Forcing them into engineering or business would be arbitrary and misleading.

### `publication`

**Definition:** Writing intended for public or external audiences via channels with their own established conventions and reader expectations.

**Anchor examples:** blog post, newsletter, LinkedIn post, tweet thread, podcast show notes.

**Fits when:** the channel has reader-expectations independent of any organization (a LinkedIn post follows LinkedIn norms regardless of who posts it).

**Does not fit when:** the writing is internal (that is `business` or `workplace`), or for a private occasion (that is `ceremonial`).

**Why this is separate from `business`:** public-channel writing follows external conventions (algorithm-aware length, platform-native form). It is a fundamentally different writing job than internal business communication, even though marketing teams produce a lot of it.

### `ceremonial`

**Definition:** Writing for specific occasions: weddings, funerals, milestones, public tributes, retirement parties, anniversary letters.

**Anchor examples:** eulogy, wedding toast.

**Fits when:** the writing is occasion-bound, often delivered spoken, often addresses an audience that is not the primary subject.

**Does not fit when:** the writing is about ceremonies but not for one (a *post* about wedding traditions is `publication`).

**Why this exists as its own domain:** ceremonial writing has distinct constraints (brevity, the room, the moment) that do not generalize to other writing contexts. Bundling it with `personal` would obscure this.

### `contemplative`

**Definition:** Spiritual, devotional, meditative, or reflective writing. Typically first-person or pastoral, oriented around interior life.

**Anchor examples:** devotional entry.

**Fits when:** the primary purpose is reflection, contemplation, spiritual formation, or prayer.

**Does not fit when:** the writing is *about* spirituality but for a public audience (a blog post on prayer is `publication`).

**Why this is separate from `ceremonial`:** ceremonial writing is occasion-bound and audience-facing; contemplative writing is interior and often private or semi-private. Distinct constraints.

### Why not 7 (no `personal`)

The catalog currently has no formats for personal letters, journal entries, family correspondence, etc. If those are added later, `personal` becomes a 7th domain. Keeping the domain list aligned to actually-present entries avoids empty buckets.

### Domains *considered and rejected*

- **`academic`** - rejected because the catalog does not currently target academic writing. Could be added later if scope expands.
- **`legal`** - rejected for the same reason.
- **`journalism`** - rejected because journalism writing fits cleanly into `publication`.
- **`government` / `civic`** - rejected; speculative scope.
- **`creative` / `literary`** - rejected; speculative scope.

These exist as future expansion possibilities, not present scope.

## Format families - per domain, fully fleshed out

The following enumeration places every current format (15) and every candidate format proposed in the Phase 2 design spec (15) into a domain and family.

### `engineering` domain - 3 families

#### `decision-documents`

Formats whose purpose is to record a technical decision, propose one, or argue for one.

| Member | Current/candidate | Notes |
|---|---|---|
| `adr` | current | Architecture Decision Record |
| `prd` | current | Product Requirements Document - debatable; see edge cases |
| `design-doc` | candidate | Technical design document |
| `rfc` | candidate | Request for Comments |
| `whitepaper` | current | Technical white paper - debatable; see edge cases |

#### `reference-and-onboarding`

Formats whose purpose is to instruct, document, or onboard a user, developer, or operator.

| Member | Current/candidate | Notes |
|---|---|---|
| `readme` | current | Repository README |
| `technical-reference` | current | API or system reference doc |
| `error-message` | candidate | User-facing error string |
| `microcopy` | candidate | UI string design |
| `faq` | candidate | Frequently asked questions |

#### `status`

Formats whose purpose is to communicate ongoing state, progress, or change.

| Member | Current/candidate | Notes |
|---|---|---|
| `changelog-entry` | current | Release notes entry |
| `daily-standup` | current | Standup update - debatable; see edge cases |

### `business` domain - 3 families

#### `briefs-and-proposals`

Short documents that frame an idea, opportunity, or request for a decision.

| Member | Current/candidate | Notes |
|---|---|---|
| `one-pager` | current | Single-page brief |
| `talk-abstract` | candidate | Talk or session description |
| `conference-proposal` | candidate | CFP submission |

#### `status-and-updates`

Recurring or periodic communication about progress or state.

| Member | Current/candidate | Notes |
|---|---|---|
| `status-report` | current | Project or team status |

#### `feedback`

Written feedback to or about another person.

| Member | Current/candidate | Notes |
|---|---|---|
| `performance-review` | candidate | Periodic performance review |
| `peer-feedback-note` | candidate | Peer-to-peer feedback |

### `workplace` domain - 3 families

#### `quick-communication`

Short-form, fast-cycle messages.

| Member | Current/candidate | Notes |
|---|---|---|
| `slack-message` | current | Slack post or thread reply |
| `email` | current | Internal or external work email |

#### `meetings`

Documentation produced for or from meetings.

| Member | Current/candidate | Notes |
|---|---|---|
| `meeting-notes` | current | Meeting summary or transcript |

#### `onboarding`

Documents that orient a new person to a process, tool, or team.

| Member | Current/candidate | Notes |
|---|---|---|
| `onboarding-walkthrough` | candidate | New-hire or new-user walkthrough |

### `publication` domain - 3 families

#### `long-form`

Sustained, structured writing for an external audience.

| Member | Current/candidate | Notes |
|---|---|---|
| `blog-post-long-form` | current | Long blog post or essay |
| `newsletter-issue` | candidate | Single newsletter issue |

#### `social-posts`

Channel-native short or medium posts.

| Member | Current/candidate | Notes |
|---|---|---|
| `linkedin-post` | candidate | LinkedIn-native post |
| `tweet-thread` | current | Twitter/X thread |

#### `spoken-and-show-notes`

Companion writing for spoken or audio formats.

| Member | Current/candidate | Notes |
|---|---|---|
| `podcast-show-notes` | candidate | Podcast episode show notes |

### `ceremonial` domain - 1 family

#### `toasts-and-tributes`

Occasion-bound speech, typically delivered aloud.

| Member | Current/candidate | Notes |
|---|---|---|
| `eulogy` | candidate | Funeral or memorial address |
| `wedding-toast` | candidate | Wedding or anniversary toast |

### `contemplative` domain - 1 family

#### `devotional-writing`

First-person or pastoral reflective writing.

| Member | Current/candidate | Notes |
|---|---|---|
| `devotional-entry` | current | Daily or thematic devotional |

### Format summary at 30 entries

- 6 domains
- 14 families
- ~2.1 average family members at 30 entries
- Family member counts: 5, 5, 5 (engineering); 3, 1, 2 (business); 2, 1, 1 (workplace); 2, 2, 1 (publication); 2 (ceremonial); 1 (contemplative)

Thinnest cells: `business/status-and-updates` (1), `workplace/meetings` (1), `workplace/onboarding` (1), `publication/spoken-and-show-notes` (1), `contemplative/devotional-writing` (1). These are acceptable starting states; they may grow as the catalog evolves.

## Voice families - one level, fully fleshed out

Voices receive a `family` field but no `domain`. Speakers travel across domains: a `journalist` voice can write for engineering or business audiences without ceasing to be a journalist voice.

### `technical-and-expert`

Voices that signal deep practitioner knowledge, often in a technical or specialized field.

| Member | Notes |
|---|---|
| `pragmatic-architect` | The grounded, opinionated engineer |
| `technical-writer` | The clarifying documentarian |
| `researcher` | The curious investigator |
| `senior-consultant` | The seasoned outside advisor |
| `operator` | The runbook-and-on-call voice |
| `product-thinker` | The customer-and-tradeoffs voice |

### `people-and-coaching`

Voices oriented around developing, supporting, or caring for other people.

| Member | Notes |
|---|---|
| `coach` | The asking-questions-to-unlock-the-learner voice |
| `friendly-mentor` | The warm-and-experienced guide |
| `caregiver` | The tending-with-attention voice |

### `authority`

Voices that speak with positional or credentialed weight.

| Member | Notes |
|---|---|
| `executive` | The senior-leader voice |
| `direct-communicator` | The plainspoken-and-decisive voice |

### `narrative-and-media`

Voices oriented around story, observation, or commentary.

| Member | Notes |
|---|---|
| `journalist` | The reporting-and-sourcing voice |
| `storyteller` | The narrative-arc-and-character voice |
| `columnist` | The recurring-opinion-and-perspective voice |

### `spiritual`

Voices oriented around faith, formation, or pastoral care.

| Member | Notes |
|---|---|
| `pastoral` | The shepherding voice |

### Voice family summary at 15 entries

- 5 families
- Average 3 members per family
- Healthy density even at current size

### At 30 voices (Phase 2 target)

Expected family expansion based on candidate voices in the design spec:

| Family | At 15 | Projected at 30 | Likely additions |
|---|---|---|---|
| `technical-and-expert` | 6 | 9 | ethicist, primer-author, beginner-explainer |
| `people-and-coaching` | 3 | 7 | elder, peer, advocate, witness |
| `authority` | 2 | 4 | contrarian, polemicist |
| `narrative-and-media` | 3 | 6 | satirist, naturalist, historian |
| `spiritual` | 1 | 1 | (likely no additions) |
| `insider-and-outsider` (new family?) | 0 | 3 | insider-confidant, outsider, witness |

The candidate list may produce 5-6 families at 30 voices. Families remain meaningful (each holds 3+ members on average); the taxonomy scales.

## Why tones receive no organization layer

Tones are registers: candid, warm, urgent, empathetic, resolute, playful, etc. Their defining property is that they are *not* tied to a context or sphere. A `candid` tone works in a slack message, a wedding toast, a sermon, and a P0 incident report.

Imposing a domain or family on tones would either:
- Produce arbitrary groupings (e.g., grouping `urgent` with operational tones when urgency applies to ceremonial writing too), or
- Force entries into multiple families (defeating the point of single-membership organization)

Existing implicit grouping for tones (warm/empathetic/caring cluster vs candid/direct/resolute cluster vs playful/celebratory/urgent cluster) is observable in `pairs_well_with` and `confusable_with` relationships and does not need to be schematized.

**Recommendation: leave tones flat.** Revisit if tone count crosses 40 and the flat list becomes hard to scan; even then, prefer informal clustering via cross-references over hard schema fields.

## Why styles receive no organization layer

Styles are rhetorical and cognitive patterns: how-to-tutorial, narrative-case-study, dialectic, executive-summary, decision-log, frequently-asked-questions, etc. Like tones, they are domain-neutral; a `dialectic` style works in academic writing, engineering decisions, pastoral teaching, and ceremonial reflection.

Informal style clusters exist (expository styles, argumentative styles, narrative styles) but the boundaries are fuzzy: is `frequently-asked-questions` expository or instructional? Is `decision-log` argumentative or narrative? Forcing a controlled vocabulary on these would create more disagreement than insight.

**Recommendation: leave styles flat.** Revisit if style count crosses 40 *and* a coherent clustering emerges from actual entries; even then, prefer tags over schema fields.

## Edge cases and judgment calls

These are the placements where reasonable curators could disagree. Each has a chosen placement and the alternative considered.

### `daily-standup`

- **Chosen:** `engineering > status`
- **Alternative considered:** `workplace > meetings`
- **Reasoning:** Standups originated in agile software practice and remain most dense in engineering teams. Other functions use them but typically via engineering-adjacent practice.
- **Confidence:** medium. If catalog grows toward non-technical functions, may move to workplace.

### `prd`

- **Chosen:** `engineering > decision-documents`
- **Alternative considered:** Own domain `product`
- **Reasoning:** PRDs are technical-adjacent; their primary readers are engineering and design. A separate product domain with one member is overdone.
- **Confidence:** high.

### `whitepaper`

- **Chosen:** `engineering > decision-documents`
- **Alternative considered:** `publication > long-form`
- **Reasoning:** The catalog's likely whitepaper use is technical or technical-marketing. Marketing whitepapers tend to follow long-form publication conventions; technical whitepapers tend to follow decision-document conventions. Default placement reflects current entry's emphasis.
- **Confidence:** low. May benefit from being two entries (`technical-whitepaper`, `marketing-whitepaper`) at scale.

### `one-pager`

- **Chosen:** `business > briefs-and-proposals`
- **Alternative considered:** `engineering > decision-documents`
- **Reasoning:** One-pagers are most often business-decision-framing artifacts (a single page summarizing an opportunity, request, or recommendation). Engineering one-pagers exist but are less canonical.
- **Confidence:** high.

### `tweet-thread`

- **Chosen:** `publication > social-posts`
- **Alternative considered:** `publication > long-form` (since some tweet threads are long)
- **Reasoning:** Threads follow social-post conventions (replies, sequential structure, platform-native length); long-form publication is a different writing job.
- **Confidence:** high.

### `linkedin-post`

- **Chosen:** `publication > social-posts`
- **Alternative considered:** `business > briefs-and-proposals`
- **Reasoning:** LinkedIn is a public platform with public-channel conventions, regardless of who posts. Business-context posts on LinkedIn still follow LinkedIn conventions.
- **Confidence:** high.

### `talk-abstract`

- **Chosen:** `business > briefs-and-proposals`
- **Alternative considered:** `publication > spoken-and-show-notes`
- **Reasoning:** Talk abstracts function as proposals for selection (to a conference, an audience). The abstract itself is a brief, not the spoken artifact.
- **Confidence:** medium.

### `peer-feedback-note`

- **Chosen:** `business > feedback`
- **Alternative considered:** `workplace > quick-communication`
- **Reasoning:** Peer feedback notes are explicitly evaluative and tied to professional development context, which lives in business/HR practice.
- **Confidence:** medium.

### `eulogy` and `wedding-toast`

- **Chosen:** `ceremonial > toasts-and-tributes`
- **Alternative considered:** Two separate families (`tributes`, `toasts`)
- **Reasoning:** At 2 members total, splitting into two single-member families is over-categorization. Bundle now; split later if catalog grows.
- **Confidence:** high for now.

## Alternative taxonomies considered

This section documents alternatives evaluated before recommending domain+family.

### Alternative 1: Single-level `category`

A flat `category` field per axis, with values like `engineering-decision-documents`, `ceremonial-tributes`, `social-posts`.

- **Pro:** simplest schema (one new field, one enum)
- **Pro:** easier validator
- **Con:** loses queryability ("show me all engineering formats" requires substring matching)
- **Con:** awkward names (`contemplative-and-ceremonial-tributes` becomes unwieldy)
- **Con:** conflates two real questions (where vs. what-kind) into one field

**Verdict:** rejected. The queryability loss is significant for future composer/SDK use cases.

### Alternative 2: Three-level `domain > family > subfamily`

Add a third level for finer distinctions (e.g., `engineering > decision-documents > forward-looking`).

- **Pro:** maximum expressiveness
- **Con:** at 30 entries per axis, third-level cells are too thin to be meaningful
- **Con:** triples the per-entry curation decision
- **Con:** future-proof for adding a third level later if needed (subfamily becomes optional)

**Verdict:** rejected for now. Two-level is sufficient at current and projected scale. Subfamily can be added in a future cycle without breaking the two-level structure.

### Alternative 3: Tag-based organization only

Use the existing `tags` array more rigorously, with conventions ensuring consistent tagging for domain-like and family-like attributes.

- **Pro:** no schema change
- **Pro:** flexible (entries can carry multiple tags)
- **Con:** organization-by-convention is fragile; new contributors may tag inconsistently
- **Con:** validators cannot enforce taxonomic structure on free-form tags without conventions becoming de facto schema
- **Con:** no canonical grouping for indexes and browsing

**Verdict:** rejected as the *primary* organization mechanism. Tags remain available for cross-cutting attributes (e.g., `spoken`, `external`, `occasion-bound`) that span domains and families.

### Alternative 4: Per-axis fully custom organization

Let each axis define its own organizing structure based on what makes sense for that axis.

- **Pro:** maximum per-axis appropriateness
- **Con:** zero schema consistency across axes
- **Con:** every downstream consumer (composer, SDK, MCP server) needs per-axis handling
- **Con:** harder to reason about as a maintainer

**Verdict:** rejected. The proposed scheme is already per-axis appropriate (formats get domain+family, voices get family only, tones and styles get nothing) without sacrificing consistency where it applies.

### Alternative 5: A fifth taxonomy axis

Add a new top-level axis ("domain" or "context") to the existing four. Each entry on each axis then has a relationship to the domain axis.

- **Pro:** maintains axis-only structure (ADR 0001's three-axis model)
- **Con:** breaks the three-axis model (now four)
- **Con:** every entry must declare a domain, even on tones and styles where it does not apply
- **Con:** combinatorial explosion in the composer UI

**Verdict:** rejected. The three-axis model is foundational. Domain belongs as an organizing attribute *within* axes that need it, not as a new axis.

## How browsing and picking change

### Current state (flat axes)

`docs/reference/index.md` renders four flat axis tables. A reader scrolls each table looking for an entry that matches their need.

### After taxonomy (hierarchical formats and voices)

`docs/reference/index.md` renders:

- Formats grouped by domain, then by family
- Voices grouped by family
- Tones flat
- Styles flat

A reader scanning formats sees clearly that RFC and eulogy live in different sections, not as adjacent flat entries.

For the future composer SPA, a domain selector becomes the first format picker filter, then family, then specific entry. Three clicks instead of one long scroll.

For the SDK and MCP server, query patterns become natural:

```typescript
// Get all engineering formats
catalog.formats.filter(f => f.domain === 'engineering');

// Get all decision-document formats across domains
catalog.formats.filter(f => f.family === 'decision-documents');

// Get the canonical voice family
catalog.voices.groupBy(v => v.family);
```

## Cross-reference relationship

The existing cross-reference fields (`pairs_well_with`, `avoid_with`, `confusable_with`) currently bear all the burden of expressing relationships between entries. After the proposed taxonomy:

- **Within-family cross-references become more powerful.** Diff-pairs that contrast two members of the same family (`narrative-case-study` vs `chronological-narrative` within styles, or `coach` vs `friendly-mentor` within `people-and-coaching`) become the sharpest pedagogical move.
- **Cross-family cross-references remain valuable.** `pairs_well_with` continues to capture "good combinations" across axes; family membership does not constrain this.
- **The `confusable_with` field becomes the most semantically tight.** Confusable entries are typically same-family. The taxonomy validates that intuition.

**Recommendation in Phase 5 (diff-pairs):** prefer within-family diff-pairs as the sharpest pedagogical contrast. Cross-family diff-pairs are valid but produce less crisp lessons.

## Migration plan

The taxonomy fits into the design spec's existing 8-phase plan without restructuring it. Specific revisions:

### Phase 0 (exemplar craft) - light revision

Five exemplar entries each get domain and family populated. This stress-tests the taxonomy at 5 entries before broader rollout.

### Phase 1 (schema codification) - additive

- Add `domain` (formats only) and `family` (formats and voices) to schemas as optional initially
- Add `check_domain_valid()` and `check_family_scoped_to_domain()` to `validate.py` as warnings initially
- Write controlled vocabularies into a single Python module (e.g., `tools/taxonomy.py`) or into schema files
- Write a new ADR (`0010-domain-and-family-organization.md`) documenting the rationale
- Update `build-indexes.py` to render `docs/reference/index.md` hierarchically

### Phase 2 (audit-and-upgrade existing 55) - includes backfill

The audit pass now also populates domain and family on every existing format and voice entry. Exemplars from Phase 0 are the templates.

After Phase 2 completes, schema fields tighten from optional to required, and validator checks promote from warnings to errors.

### Phase 3 (generate 60 new entries) - taxonomy-aware curation

The 60 new entries are selected with family balance as a criterion, not just axis balance. Specific implication: the per-axis curation rationale (Phase 6d) becomes a per-domain-and-family rationale for formats.

### Phase 5 (diff-pair expansion) - within-family focus

Diff-pair selection criterion changes from "within-axis confusables" to "within-family confusables" for sharper pedagogy. The current 4 seed diff-pairs already mostly satisfy this (the voice diff-pair `pragmatic-architect` vs `pastoral` is cross-family and could be supplemented by within-family pairs in the same axis).

### Phase 6d (per-axis curation rationale) - restructured around taxonomy

Format curation doc structures around 6 domains and 14 families. Voice curation doc structures around 5-7 families. Tone and style curation docs remain flat.

### New ADR

`docs/internal/adr/0010-domain-and-family-organization.md` documents:

- The problem (heterogeneity at 30/axis)
- The proposed two-level taxonomy
- The alternatives considered
- Per-axis decisions (formats yes, voices yes, tones no, styles no)
- Migration path

## Future scale considerations

### At 60 entries per axis (next-next milestone)

- Format families approach 4 average members; some families likely split (e.g., `decision-documents` may bifurcate into `forward-looking` and `retrospective`)
- Voice families approach 12 average members; clearer subdivisions emerge
- New domains may become warranted (e.g., `academic` or `creative` if scope expands)
- Subfamily layer may finally pay off

### At 200 entries per axis (aspirational scale)

- Two-level taxonomy becomes insufficient; subfamily or third-level needed
- May warrant a separate taxonomy doc per axis
- Composer UX needs progressive disclosure: domain > family > subfamily > entry

The current proposal does not preclude any of this. Adding a third level later requires only making `subfamily` optional in the schema; existing two-level entries continue to validate.

### Triggers to revisit

- Format axis reaches 50 entries
- Any single family exceeds 8 members
- A new domain becomes warranted (entry list shows clear cluster not fitting existing 6)
- Composer or SDK users report navigation friction at 30/axis

## Naming decisions defended

### Why `domain` and not `sphere` / `context` / `area` / `realm`

- `sphere`: slightly precious; reads more like academic philosophy than catalog metadata
- `context`: ambiguous with the writing's *usage* context (audience, occasion); could be confused with prompt context
- `area`: vague and overused in software jargon
- `realm`: precious in a different direction; feels fantasy-novel
- `domain`: standard taxonomy term, clear meaning, no overload with existing repo concepts

### Why `family` and not `cluster` / `archetype` / `kind` / `category`

- `cluster`: implies emergent grouping (statistical); the taxonomy is curated, not emergent
- `archetype`: voice-axis-specific connotation; awkward for formats
- `kind`: too informal; tonally weak as a schema field name
- `category`: works but tends to compete with `tags` and `axis` semantically
- `family`: implies bounded membership and peer relationship; matches the goal

### Why family is scoped to domain (for formats) rather than global

Global family names would collide across domains (`status` in engineering vs `status-and-updates` in business). Scoping family to domain allows shorter, clearer family names within each domain context.

Trade-off accepted: an entry's family value alone is not globally unique without the domain qualifier. The validator and composer always carry both fields together.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Curators disagree on placements for edge cases | Edge-cases table in this doc documents chosen placements; ADR 0010 captures rationale |
| Taxonomy feels arbitrary to a reader | Per-axis curation rationale (Phase 6d) makes the logic explicit |
| New formats do not fit existing families | Adding a new family is a small schema change; adding a new domain is a slightly bigger one. Process documented in `schema-evolution-policy.md` (Phase 6c) |
| Solo maintainer drifts on family assignments over time | Validator enforces controlled vocabulary; new entries cannot pass with a non-existent family |
| Two-level scheme insufficient at 60+ entries | Subfamily layer can be added later as optional; current scheme is forward-compatible |
| The proposed family names age poorly (e.g., LinkedIn evolves, "social-posts" feels dated) | Names are revisable; ADR 0010 captures the *rationale* so future renames preserve intent |
| Schema changes regress existing validators | Phase 1 adds fields as optional warnings first; tighten only after Phase 2 backfill |

## Open questions for jprisant

1. **Domain count: 6 acceptable?** Or do you want to split `business` further (`marketing`, `leadership`, `operations`)? Or merge `ceremonial` and `contemplative` into one `personal-and-spiritual` domain?
2. **Domain on voices: yes or no?** I argued no; voices travel across domains. If you have strong examples of voices that are essentially domain-locked (`pastoral` may be one), it could change the call.
3. **Family naming - any reads wrong?** `quick-communication`, `toasts-and-tributes`, `spoken-and-show-notes`, `feedback`, `briefs-and-proposals` are the most negotiable. Suggest alternatives if any feel off.
4. **Edge cases - reassign any?** Especially `daily-standup`, `whitepaper`, `talk-abstract` where confidence is medium.
5. **Tone/style flat decision - agree?** If you see implicit groupings in tones or styles that would benefit from schematization, I want to hear them before locking the no-organization call.
6. **Curation rationale structure (Phase 6d) - one doc per axis still, or one doc per domain for formats?** Per-domain may be more readable but produces 6 docs for formats instead of 1.

## Recommended next steps

1. Read this proposal and answer the 6 open questions above.
2. If approved as recommended: I draft ADR 0010 and update the design spec's Phase 1 / Phase 2 / Phase 5 / Phase 6d sections to reflect taxonomy integration.
3. If revisions: I update this doc, re-circulate, and only then update the design spec.
4. Once design spec + this proposal are both approved: invoke writing-plans skill to produce the task-level implementation plan, with taxonomy work integrated.

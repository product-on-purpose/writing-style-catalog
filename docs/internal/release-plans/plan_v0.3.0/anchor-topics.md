---
title: The 12 Anchor Topics (the worked-sample substrate)
status: proposal (internal, for maintainer decision)
date: 2026-06-03
type: design-proposal
related:
  - docs/internal/scaling-the-library-100x.md
  - docs/internal/backlog.md
  - docs/internal/_working/domain-and-family-taxonomy_2026-05-15.md
  - docs/internal/_working/catalog-inventory-aspirational_2026-05-16.md
  - _LOCAL/audit/2026-05-31_adherence-smoke-test.md
supersedes_context: this resolves decision-matrix item 8 ("lock the 12 anchor topics")
---

# The 12 Anchor Topics (the worked-sample substrate)

## What this decides

The catalog renders every entry as worked samples on a shared set of anchor topics. Holding the topic constant is what makes a sample teach: a reader sees one entry across real contexts, and a diff-pair can vary exactly one axis because the topic is pinned. Today there are 3 topics (`async-standups`, `morning-routine`, `service-database-choice`), about 3 renders per entry. The vision target is 12+ samples per entry, which mechanically means expanding the anchor-topic set toward ~12 chosen so that every domain and ideally every family has a native home topic to be rendered on honestly.

This document locks the 12. It is the single highest-leverage unresolved input in the scaling program: the sample matrix, the diff-pair generator, the per-entry distinguishability test-bed, and the E1 gate's neighbor-rendering all key off this list (scaling doc, decision-matrix item 8). It supersedes the instinct-picked 3-and-improvise approach with a designed, domain-balanced slice.

## Selection criteria

Three criteria, taken straight from the backlog and the scaling doc, plus one derived check. A candidate topic must clear all three.

### 1. Isolation (the load-bearing criterion)

A topic must let exactly one axis vary while the other three axes and the topic stay fixed, with no confound. The topic itself must not smuggle in a domain or a register of its own. `service-database-choice` is the exemplar: Postgres-vs-DynamoDB is a clean decision substrate that does not itself drag in a tone or a format, so swapping the voice axis on it isolates the voice. The smoke-test evidence confirms this - on that topic an `adr` render produced the `## Context / ## Decision / ## Consequences` skeleton while a `whitepaper` render opened "Executive Summary", and the only thing that changed was the format entry.

**A topic that fails it:** `eulogy-for-my-father`. It bakes in the `ceremonial` domain and a grief-laden reverent register before any axis is selected. Render `playful` tone or a `slack-message` format on it and the topic fights the instruction; the sample teaches "the topic is a eulogy", not "this is what the tone entry does". A topic that is itself a genre cannot be the constant-topic control for a genre-bearing axis. The rule: the topic supplies a *situation*, the axes supply the *writing*.

### 2. Spread across the five domains

The set must reach all five domains (professional, public, relational, ceremonial, contemplative) so every entry has a natural home topic. A `contemplative` `devotional-entry` rendered only on `async-standups` is being tested off its home turf and will read as strained; it needs a topic where reflection is the native mode. Spread is what lets a family be shown flattered (on its home topic) and stretched (on a neighbor's), which is exactly the contrast the diff-pair pedagogy needs.

**A topic that fails it:** a fourth professional-engineering decision such as `monolith-vs-microservices`. It is well-isolated and real, but it adds zero spread - it sits in the same cell as `service-database-choice`, leaving `ceremonial` and `contemplative` with no native substrate at all. Failing this criterion is not about the topic being bad; it is about the *set* being lopsided.

### 3. Real-worldness

A topic must be something a real writer actually faces, not a synthetic prompt. The current three pass: teams really debate async standups, people really design a morning routine, engineers really choose a datastore. Synthetic topics ("describe a fictional widget") produce samples that read as exercises, which violates the best-in-class constraint by construction - a sample that reads as homework cannot demonstrate that an entry steers real writing.

**A topic that fails it:** `the-color-blue` or `a-day-in-the-life-of-a-photon`. Isolated and domain-neutral, yes, but no writer is ever handed it as a live task, so every render is a creative-writing stunt rather than evidence the entry works in the wild.

### 4 (derived). Cross-topic contrast

Beyond passing individually, the 12 must collectively exercise the full register range - decision, instruction, reflection, celebration, accountability, advocacy - so no entry is starved of a flattering substrate and none is only ever shown flattered. The Phase 2 spec reasoned this way when it added `service-database-choice` precisely because it "pulls hardest on parts of the catalog the first two topics undersell". This is a property of the slate, used to break ties among otherwise-qualifying candidates, not a per-topic gate.

## The 12 topics

Distribution: 4 professional, 2 public, 2 relational, 2 ceremonial, 2 contemplative. The existing 3 are slotted in unchanged (rows marked *existing*). Family names below are from the v2 taxonomy (canonical: `domain-and-family-taxonomy_2026-05-15.md`).

| # | Topic slug | One-line label | Domain | Families it best exercises | Isolation rationale |
|---|---|---|---|---|---|
| 1 | `service-database-choice` *(existing)* | Choosing Postgres vs DynamoDB for a new service | professional | deliberation, instruction; expert voices; analytic styles | A bounded technical decision with named constraints; supplies a situation, not a genre or register. The proven best-isolated anchor. |
| 2 | `async-standups` *(existing)* | Whether the team should move to async-first standups | professional | progress, messaging, brief; principal + expert voices | A team-practice change with real tradeoffs; carries no inherent tone, so candid/confident/diplomatic all attach cleanly. |
| 3 | `roadmap-deprioritization` | Telling stakeholders a committed feature is being cut this quarter | professional | progress, response, accountability-adjacent; principal voices; persuasive styles | A status-and-consequence situation; the bad-news content is fixed while register (apologetic vs resolute vs diplomatic) is free to vary. |
| 4 | `onboarding-a-new-hire` | Getting a new engineer productive in their first two weeks | professional | instruction, appraisal, messaging; care + expert voices | A teach-someone-to-act situation; isolates instruction vs reference vs encouragement without presupposing any one form. |
| 5 | `remote-work-policy` | Arguing a public position on return-to-office | public | position, broadcast; dissident + principal + witness voices | A contestable public issue; the stance is the topic's content, but advocacy vs reportage vs satire are axis choices, not baked in. |
| 6 | `product-launch-announcement` | Announcing a new product to an outside audience | public | broadcast, copy; witness + principal voices; expository styles | A there-is-news situation routed through public channels; hype vs plain vs reverent is supplied by the axes, not the event. |
| 7 | `morning-routine` *(existing)* | Designing a sustainable morning routine | relational | essay, correspondence-adjacent; care + expert voices; reflective + how-to styles | A personal-life design problem addressed to self or a known reader; a situation, not a register - it renders as systems-design, coaching, or confession depending only on the axis. |
| 8 | `thanking-a-mentor` | Writing to thank a mentor who shaped your career | relational | correspondence, essay; care voices; warm + confessional registers | A gratitude-bearing but register-open situation; the relationship is fixed, the form (note vs essay vs toast-draft) and tone vary freely. |
| 9 | `retirement-send-off` | Marking a long-serving colleague's departure | ceremonial | tribute; principal + witness + care voices; narrative + celebratory styles | An occasion with a defined audience but no fixed words; honor is the situation, the register and form are open - unlike a eulogy it does not force grief. |
| 10 | `team-milestone-celebration` | Marking the team shipping a hard, long project | ceremonial | tribute, progress-adjacent; care + principal voices; celebratory + narrative styles | A mark-the-moment situation that admits celebratory, sober-grateful, or playful registers; the milestone is fixed, the tone is the variable. |
| 11 | `daily-rest-practice` | Reflecting on keeping a discipline of rest | contemplative | devotion, journal; pastoral + care voices; reflective + devotional styles | A formation/reflection situation with no occasion and no audience-of-record; isolates devotional vs journal vs meditative voice without dragging in a ceremony. |
| 12 | `a-hard-year-in-review` | A personal year-end reckoning with a difficult year | contemplative | journal, essay; pastoral + witness voices; confessional + narrative styles | A private-reflection situation; the difficulty is content, while confessional vs measured-witness vs devotional framing is entirely an axis choice. |

### Honest domain assessment of the existing three

- `service-database-choice` and `async-standups` are unambiguously **professional**.
- `morning-routine` is assigned **relational**. It is a personal-life matter addressed to oneself or a close reader, which is the relational definition (writer could name the reader and their situation). It has genuine **contemplative** reach - the existing `pragmatic-architect` render treats it as systems design while a `confessional` or `devotional` render would treat it reflectively - but its native home is relational, because the dominant frame is a person designing their own daily life, not a discipline of formation. Topics 11 and 12 carry the contemplative load it only gestures at.

## Coverage check

Every domain has at least one native topic; the dense professional surface gets four. Family-level coverage below maps each major family group to its strongest native substrate among the 12.

| Domain | Native topics | Families with a strong home topic |
|---|---|---|
| professional | 1, 2, 3, 4 | deliberation (1), instruction (4), progress (2,3), messaging (2,4), appraisal (4), response (3), brief (2) |
| public | 5, 6 | position (5), broadcast (5,6), copy (6), accountability (3 carries the boundary case) |
| relational | 7, 8 | essay (7,8), correspondence (8) |
| ceremonial | 9, 10 | tribute (9,10) |
| contemplative | 11, 12 | devotion (11), journal (11,12) |

Voice families (which carry no domain) all find a flattering substrate: `expert` on 1/4, `care` on 4/7/8/10, `principal` on 3/5/9, `witness` on 5/6/9/12, `dissident` on 5, `pastoral` on 11/12. Tones and styles are domain-neutral by design and travel across all 12, so they need no native cell - they are exercised hardest where stakes vary (3, 5, 9, 12).

**Families left without a strong home topic, flagged honestly:**

- **`outreach`** (cold sales/partnership initiation) and **`copy`** (ad/landing-page) are only partially served. Topic 6 exercises announcement-style copy but not cold-open persuasion to a stranger. This is acceptable: these are narrow commercial families, and a render of an `outreach` format on topic 5 or 6 is a legitimate stretch test. If the gate later shows `outreach` entries cannot be distinguished off-home, add a 13th topic (`cold-pitch-to-a-stranger`) rather than weaken the slate of 12.
- **`accountability`** (public apology, security advisory) has no fully native home; topic 3 (a hard internal cut) is its closest substrate but is professional, not public. This is a deliberate trade. A `public-apology` topic fails the isolation criterion the same way a eulogy does - it bakes in contrition - so accountability is intentionally tested on its boundary (topic 3) rather than handed a register-bearing native topic.

The pattern is intentional: the 12 cover the five domains and the great majority of families, and the two thin spots are exactly the families whose native topics would themselves fail isolation. That is the criterion doing its job, not a gap to paper over.

## Why 12 and not the full Cartesian product

The 12 is a *designed slice*, not topic x entry exhaustion. Two reasons it is not 12 trivial paraphrases of one render:

1. **The slice is chosen for spread, so the 12 topics already differ in register-range.** A `confessional` tone on `a-hard-year-in-review` and the same tone on `service-database-choice` are not paraphrases; they are the same instruction proving it holds across reflection and decision. The cross-topic-contrast criterion guarantees the topics are far apart in the very space the samples are meant to probe.

2. **Per entry, the 12 samples vary other dimensions too - not just topic.** The scaling doc's sample matrix has six dimensions (topic, length, audience, stakes, medium, difficulty), and the per-entry slice deliberately moves more than one. A defensible default slice (scaling doc, "the sample matrix" section) is: the home topic rendered at three lengths (3 samples), four additional spread topics at standard length (4), three edge renders that push one dimension to a strained setting - a `slack-message` forced long, a `lay` audience for an entry that claims to trust expert readers, a `crisis`-stakes render of a routine tone (3), and two reserved for the novel example types - a before/after pair and a multi-model render (2). That is 12, and no two are reachable from each other by a trivial paraphrase. Topic is the spine of the slice; length, audience, stakes, and difficulty are the ribs.

So 12 anchor topics is the *vocabulary* of substrates, not the *count* of samples per entry. The samples-at-100x design varies several dimensions through that vocabulary; the topics exist to give every entry honest home ground and to keep diff-pairs topic-constant, not to be the only thing that changes.

The 12 is also a designed slice, not topic-x-entry exhaustion, for a hard economic reason. Full Cartesian (every entry on every topic at every matrix coordinate) is tens of thousands of near-redundant renders that the diversity mechanisms (matrix-cell uniqueness, embedding dedup, lexical-overlap guard) would mostly reject anyway. Twelve substrates, sliced deliberately, buys the teaching value the Cartesian would and skips the redundancy tax.

## Migration

- **The existing 3 stay, unchanged.** `async-standups`, `morning-routine`, and `service-database-choice` are already rendered across the current 60 entries and carry diff-pairs (async-standups and morning-routine do; `service-database-choice` is the C2 backlog item to add them). They are grandfathered as anchor topics; no re-render is needed. Their domain assignments are now recorded (2x professional, 1x relational) so the slate balance is explicit.
- **The 9 new topics are generated behind the E1 gate, never hand-improvised.** Each new topic's renders are produced by the E1 generation pipeline (the extended `diff-pair-generator.py`) and cleared by the automated adherence gate before publish. A render earns its place on a new topic the same way an entry earns its slot: by producing measurably distinguishable output against its same-family neighbors on that topic. This is the non-negotiable order from the backlog - gate first, then generate at volume - applied to topic expansion: no new anchor topic ships renders until E1 exists.
- **Sequencing.** Lock these 12 now (this resolves decision-matrix item 8). Add `service-database-choice` diff-pairs (C2) on the existing slate. Then, once E1 lands, generate the 9 new topics' renders family by family, prioritizing the home topics of families that today have no native substrate (ceremonial and contemplative first, since those are the entries currently tested most off-home).
- **Schema touch.** Each sample's frontmatter already carries `topic_slug` and `topic_label`; the new topics need only their slugs registered wherever the anchor-topic set is enumerated (the generator and the site's vertical-slice index). The six-dimension matrix coordinates (`length`, `audience`, `stakes`, `medium`, `difficulty`) are a separate, later frontmatter extension tracked under the sample-depth work (E3), not blocked on locking the 12.

## Open questions for the maintainer

1. **Slate balance.** Is 4/2/2/2/2 the right weighting, or should professional drop to 3 (freeing a slot for an `outreach`/`copy` home topic) given the commercial-family gap flagged above?
2. **`morning-routine` domain.** Confirm the relational assignment, or reassign to contemplative if you read its dominant frame as formation rather than personal-life design.
3. **The accountability boundary.** Accept testing `accountability` on its boundary (topic 3, professional) rather than minting a register-bearing native topic, or admit one deliberately and accept the isolation cost?
4. **Slugs.** The 9 new slugs are first-draft names; confirm or rename before they are written into the generator and the route manifest.

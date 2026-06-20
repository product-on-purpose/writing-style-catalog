---
title: Anchor Topics - a frozen regression core and a growable seed pool (the worked-sample substrate)
status: decided (D1 - anchor topics, 2026-06-20; ADR 0017)
date: 2026-06-03
updated: 2026-06-20
type: design-proposal
related:
  - docs/internal/scaling-the-library-100x.md
  - docs/internal/backlog.md
  - docs/internal/adr/0006-anchor-topic-selection.md
  - docs/internal/adr/0017-anchor-topic-architecture.md
  - docs/internal/release-plans/plan_v0.3.0/adherence-gate-spec.md
  - docs/internal/release-plans/plan_v0.3.0/decisions.md
  - docs/internal/_working/domain-and-family-taxonomy_2026-05-15.md
  - docs/internal/_working/catalog-inventory-aspirational_2026-05-16.md
  - _LOCAL/audit/2026-05-31_adherence-smoke-test.md
supersedes_context: resolves decision-matrix item 8 ("lock the 12 anchor topics") and decision D1 - anchor topics
---

# Anchor Topics: a frozen regression core and a growable seed pool

> **Status note (2026-06-20).** D1 - anchor topics is **DECIDED**. This document is no longer a
> proposal awaiting a maintainer call; it records the decided **two-tier anchor-topic model** and
> the designed seed slate. The architectural decision is [ADR 0017](../../adr/0017-anchor-topic-architecture.md);
> the decision-state record is [`decisions.md`](decisions.md) under D1. The original Phase 0
> single-topic decision ([ADR 0006](../../adr/0006-anchor-topic-selection.md)) is the predecessor
> this supersedes for the scaling era, not a conflict.

## What this decides

The catalog renders every entry as worked samples on a shared set of anchor topics. Holding the
topic constant is what makes a sample teach: a reader sees one entry across real contexts, and a
diff-pair can vary exactly one axis because the topic is pinned. Today there are 3 topics
(`async-standups`, `morning-routine`, `service-database-choice`), about 3 renders per entry. The
vision target is 12+ samples per entry, which mechanically means expanding the anchor-topic set so
that every domain and ideally every family has a native home topic to be rendered on honestly.

D1 settles the **shape** of that set. Rather than locking a single flat slate of 12 forever, the
anchor topics are split into two tiers (the reconciliation the D1 deferral sketched, and the shape
the gate spec already implies for its golden set):

1. A small **frozen regression core**: a fixed set of topics that the C3 - held-out reference set
   renders on every CI as the distinguishability regression. The core never changes silently; it is
   the immovable yardstick.
2. A larger **growable, optionally randomized seed pool**: the set the E1 adherence gate draws home
   topics from for admission and breadth. The 12 designed topics below are the **seed** of this
   pool, not a hard cap. New topics join only after the gate clears their renders, and the pool may
   be drawn from randomly per gate run for breadth.

This is the single highest-leverage substrate input in the scaling program: the sample matrix, the
diff-pair generator, the per-entry distinguishability test-bed, and the E1 gate's neighbor-rendering
all key off these topics (scaling doc, decision-matrix item 8). The two-tier shape keeps the C3
frozen-regression guarantee deterministic (regression always runs on the fixed core) while giving
the program the expansion and randomness a single locked slate could not (admission draws from the
growable pool).

## Why two tiers (and not a flat fixed 12)

The deferral that opened D1 named a real tension: C3 - held-out reference set needs a **fixed** topic
set so a sharpening edit that blurs a previously crisp pair fails the build, but a small fixed slate
overfits the catalog to a dozen prompts and forces a premature commitment to which topics best
exercise each family. The two tiers resolve both at once, and they are not a compromise against the
gate design - they are the gate design. The gate spec's golden-set-staleness mitigation already
prescribes treating the frozen set as "versioned, not eternal: add (never silently replace) new
frozen pairs per new family as it matures, each promoted by a maintainer ADR." A frozen-but-growable
core is exactly that rule applied to topics.

Concretely:

- **Regression is deterministic.** The frozen core is rendered every CI; if a frozen pair drops
  below its recorded band, the build fails. Randomness never touches this tier.
- **Breadth is empirical.** Admission and breadth renders draw from the seed pool, optionally
  randomized per run, with each draw logged together with its seed so any run is reproducible. A
  topic earns its place in the pool the same way an entry earns its slot: by producing measurably
  distinguishable output against its same-family neighbors on that topic.
- **No premature commitment.** Because the pool is gate-arbitrated and growable, the slate below
  does not have to be perfect on day one. Topics that fail to isolate or to flatter a family are
  caught by the gate rather than by a maintainer guessing in advance.

## Selection criteria

Three criteria, taken straight from the backlog and the scaling doc, plus one derived check. A
candidate topic must clear all three to enter the pool.

### 1. Isolation (the load-bearing criterion)

A topic must let exactly one axis vary while the other three axes and the topic stay fixed, with no
confound. The topic itself must not smuggle in a domain or a register of its own.
`service-database-choice` is the exemplar: Postgres-vs-DynamoDB is a clean decision substrate that
does not itself drag in a tone or a format, so swapping the voice axis on it isolates the voice. The
smoke-test evidence confirms this - on that topic an `adr` render produced the
`## Context / ## Decision / ## Consequences` skeleton while a `whitepaper` render opened "Executive
Summary", and the only thing that changed was the format entry.

**A topic that fails it:** `eulogy-for-my-father`. It bakes in the `ceremonial` domain and a
grief-laden reverent register before any axis is selected. Render `playful` tone or a
`slack-message` format on it and the topic fights the instruction; the sample teaches "the topic is
a eulogy", not "this is what the tone entry does". A topic that is itself a genre cannot be the
constant-topic control for a genre-bearing axis. The rule: the topic supplies a *situation*, the
axes supply the *writing*.

### 2. Spread across the five domains

The set must reach all five domains (professional, public, personal, ceremonial, contemplative) so
every entry has a natural home topic. A `contemplative` `devotional-entry` rendered only on
`async-standups` is being tested off its home turf and will read as strained; it needs a topic where
reflection is the native mode. Spread is what lets a family be shown flattered (on its home topic)
and stretched (on a neighbor's), which is exactly the contrast the diff-pair pedagogy needs.

**A topic that fails it:** a fourth professional-engineering decision such as
`monolith-vs-microservices`. It is well-isolated and real, but it adds zero spread - it sits in the
same cell as `service-database-choice`, leaving `ceremonial` and `contemplative` with no native
substrate at all. Failing this criterion is not about the topic being bad; it is about the *set*
being lopsided.

### 3. Real-worldness

A topic must be something a real writer actually faces, not a synthetic prompt. The current three
pass: teams really debate async standups, people really design a morning routine, engineers really
choose a datastore. Synthetic topics ("describe a fictional widget") produce samples that read as
exercises, which violates the best-in-class constraint by construction - a sample that reads as
homework cannot demonstrate that an entry steers real writing.

**A topic that fails it:** `the-color-blue` or `a-day-in-the-life-of-a-photon`. Isolated and
domain-neutral, yes, but no writer is ever handed it as a live task, so every render is a
creative-writing stunt rather than evidence the entry works in the wild.

### 4 (derived). Cross-topic contrast

Beyond passing individually, the pool must collectively exercise the full register range - decision,
instruction, reflection, celebration, accountability, advocacy - so no entry is starved of a
flattering substrate and none is only ever shown flattered. The Phase 2 spec reasoned this way when
it added `service-database-choice` precisely because it "pulls hardest on parts of the catalog the
first two topics undersell". This is a property of the slate, used to break ties among
otherwise-qualifying candidates, not a per-topic gate.

## The seed slate (12 topics)

These 12 are the designed **seed** of the breadth pool. Distribution: 4 professional, 2 public,
2 personal, 2 ceremonial, 2 contemplative. The existing 3 are slotted in unchanged (rows marked
*existing*) and double as the initial frozen regression core. Family names below are from the v2
taxonomy (canonical: `tools/taxonomy.py`; the voice axis carries 5 families, with `pastoral` a
subfamily of `care`).

| # | Topic slug | One-line label | Domain | Families it best exercises | Isolation rationale |
|---|---|---|---|---|---|
| 1 | `service-database-choice` *(existing, core)* | Choosing Postgres vs DynamoDB for a new service | professional | deliberation, instruction; expert voices; analytic styles | A bounded technical decision with named constraints; supplies a situation, not a genre or register. The proven best-isolated anchor. |
| 2 | `async-standups` *(existing, core)* | Whether the team should move to async-first standups | professional | progress, messaging, brief; principal + expert voices | A team-practice change with real tradeoffs; carries no inherent tone, so candid/confident/diplomatic all attach cleanly. |
| 3 | `roadmap-deprioritization` | Telling stakeholders a committed feature is being cut this quarter | professional | progress, response, accountability-adjacent; principal voices; persuasive styles | A status-and-consequence situation; the bad-news content is fixed while register (apologetic vs resolute vs diplomatic) is free to vary. |
| 4 | `onboarding-a-new-hire` | Getting a new engineer productive in their first two weeks | professional | instruction, appraisal, messaging; care + expert voices | A teach-someone-to-act situation; isolates instruction vs reference vs encouragement without presupposing any one form. |
| 5 | `remote-work-policy` | Arguing a public position on return-to-office | public | position, broadcast; dissident + principal + witness voices | A contestable public issue; the stance is the topic's content, but advocacy vs reportage vs satire are axis choices, not baked in. |
| 6 | `product-launch-announcement` | Announcing a new product to an outside audience | public | broadcast, copy; witness + principal voices; expository styles | A there-is-news situation routed through public channels; hype vs plain vs reverent is supplied by the axes, not the event. |
| 7 | `morning-routine` *(existing, core)* | Designing a sustainable morning routine | personal | essay, correspondence-adjacent; care + expert voices; reflective + how-to styles | A personal-life design problem addressed to self or a known reader; a situation, not a register - it renders as systems-design, coaching, or confession depending only on the axis. |
| 8 | `thanking-a-mentor` | Writing to thank a mentor who shaped your career | personal | correspondence, essay; care voices; warm + confessional registers | A gratitude-bearing but register-open situation; the relationship is fixed, the form (note vs essay vs toast-draft) and tone vary freely. |
| 9 | `retirement-send-off` | Marking a long-serving colleague's departure | ceremonial | tribute; principal + witness + care voices; narrative + celebratory styles | An occasion with a defined audience but no fixed words; honor is the situation, the register and form are open - unlike a eulogy it does not force grief. |
| 10 | `team-milestone-celebration` | Marking the team shipping a hard, long project | ceremonial | tribute, progress-adjacent; care + principal voices; celebratory + narrative styles | A mark-the-moment situation that admits celebratory, sober-grateful, or playful registers; the milestone is fixed, the tone is the variable. |
| 11 | `daily-rest-practice` | Reflecting on keeping a discipline of rest | contemplative | devotion, journal; care voices (pastoral subfamily); reflective + devotional styles | A formation/reflection situation with no occasion and no audience-of-record; isolates devotional vs journal vs meditative voice without dragging in a ceremony. |
| 12 | `a-hard-year-in-review` | A personal year-end reckoning with a difficult year | contemplative | journal, essay; care (pastoral subfamily) + witness voices; confessional + narrative styles | A private-reflection situation; the difficulty is content, while confessional vs measured-witness vs devotional framing is entirely an axis choice. |

### Honest domain assessment of the existing three

- `service-database-choice` and `async-standups` are unambiguously **professional**.
- `morning-routine` is assigned **personal** (the renamed `relational` domain, per A1/Q2). It is a
  personal-life matter addressed to oneself or a close reader, which is the personal definition (the
  writer could name the reader and their situation). It has genuine **contemplative** reach - the
  existing `pragmatic-architect` render treats it as systems design while a `confessional` or
  `devotional` render would treat it reflectively - but its native home is personal, because the
  dominant frame is a person designing their own daily life, not a discipline of formation. Topics
  11 and 12 carry the contemplative load it only gestures at. (D2 - morning-routine domain confirms
  this assignment as its recommendation; it remains a P1 row formally, but the slate uses `personal`.)

## Coverage check

Every domain has at least one native topic in the seed; the dense professional surface gets four.
Family-level coverage below maps each major family group to its strongest native substrate among the
12.

| Domain | Native topics | Families with a strong home topic |
|---|---|---|
| professional | 1, 2, 3, 4 | deliberation (1), instruction (4), progress (2,3), messaging (2,4), appraisal (4), response (3), brief (2) |
| public | 5, 6 | position (5), broadcast (5,6), copy (6), accountability (3 carries the boundary case) |
| personal | 7, 8 | essay (7,8), correspondence (8) |
| ceremonial | 9, 10 | tribute (9,10) |
| contemplative | 11, 12 | devotion (11), journal (11,12) |

Voice families (which carry no domain) all find a flattering substrate: `expert` on 1/4, `care` on
4/7/8/10 and its `pastoral` subfamily on 11/12, `principal` on 3/5/9, `witness` on 5/6/9/12,
`dissident` on 5. Tones and styles are domain-neutral by design and travel across all 12, so they
need no native cell - they are exercised hardest where stakes vary (3, 5, 9, 12).

**Families left without a strong home topic, flagged honestly:**

- **`outreach`** (cold sales/partnership initiation) and **`copy`** (ad/landing-page) are only
  partially served. Topic 6 exercises announcement-style copy but not cold-open persuasion to a
  stranger. This is acceptable: these are narrow commercial families, and a render of an `outreach`
  format on topic 5 or 6 is a legitimate stretch test. If the gate later shows `outreach` entries
  cannot be distinguished off-home, add a `cold-pitch-to-a-stranger` topic to the pool rather than
  weaken the seed. The growable pool makes this a low-cost, gate-arbitrated addition.
- **`accountability`** (public apology, security advisory) has no fully native home; topic 3 (a hard
  internal cut) is its closest substrate but is professional, not public. This is a deliberate trade
  (D3 - accountability family home recommends testing on the boundary). A `public-apology` topic
  fails the isolation criterion the same way a eulogy does - it bakes in contrition - so
  accountability is intentionally tested on its boundary (topic 3) rather than handed a
  register-bearing native topic.

The pattern is intentional: the seed covers the five domains and the great majority of families, and
the two thin spots are exactly the families whose native topics would themselves fail isolation.
That is the criterion doing its job, not a gap to paper over - and the pool can absorb a remedy
later if the gate proves one is needed.

## Why 12 and not the full Cartesian product

The 12 is a *designed slice* seeding the pool, not topic-x-entry exhaustion and not a hard cap. Two
reasons it is not 12 trivial paraphrases of one render:

1. **The slice is chosen for spread, so the 12 topics already differ in register-range.** A
   `confessional` tone on `a-hard-year-in-review` and the same tone on `service-database-choice` are
   not paraphrases; they are the same instruction proving it holds across reflection and decision.
   The cross-topic-contrast criterion guarantees the topics are far apart in the very space the
   samples are meant to probe.
2. **Per entry, the 12 samples vary other dimensions too - not just topic.** The scaling doc's
   sample matrix has six dimensions (topic, length, audience, stakes, medium, difficulty), and the
   per-entry slice deliberately moves more than one. A defensible default slice (scaling doc, "the
   sample matrix" section) is: the home topic rendered at three lengths (3 samples), four additional
   spread topics at standard length (4), three edge renders that push one dimension to a strained
   setting - a `slack-message` forced long, a `lay` audience for an entry that claims to trust
   expert readers, a `crisis`-stakes render of a routine tone (3), and two reserved for the novel
   example types - a before/after pair and a multi-model render (2). That is 12, and no two are
   reachable from each other by a trivial paraphrase. Topic is the spine of the slice; length,
   audience, stakes, and difficulty are the ribs.

So the seed slate is the *vocabulary* of substrates, not the *count* of samples per entry. The
samples-at-100x design varies several dimensions through that vocabulary; the topics exist to give
every entry honest home ground and to keep diff-pairs topic-constant, not to be the only thing that
changes.

The slice is a designed seed, not topic-x-entry exhaustion, for a hard economic reason too. Full
Cartesian (every entry on every topic at every matrix coordinate) is tens of thousands of
near-redundant renders that the diversity mechanisms (matrix-cell uniqueness, embedding dedup,
lexical-overlap guard) would mostly reject anyway. A deliberate seed, drawn from as the pool grows,
buys the teaching value the Cartesian would and skips the redundancy tax.

## Migration (the two tiers in practice)

- **The existing 3 are the frozen regression core, unchanged.** `async-standups`, `morning-routine`,
  and `service-database-choice` are already rendered across the current 60 entries and carry
  diff-pairs (async-standups and morning-routine do; `service-database-choice` is the C2 backlog item
  to add them). They are grandfathered as anchor topics and frozen into the C3 regression set; no
  re-render is needed. Their domain assignments are recorded (2x professional, 1x personal) so the
  core's balance is explicit. The core covers professional and personal today; it grows toward one
  topic per domain as E1 renders and clears the ceremonial and contemplative topics, each added by a
  maintainer ADR (the gate spec's "versioned, not eternal" rule).
- **The 9 new topics seed the breadth pool and are generated behind the E1 gate, never
  hand-improvised.** Each new topic's renders are produced by the E1 generation pipeline (the
  extended `diff-pair-generator.py`) and cleared by the automated adherence gate before publish. A
  render earns its place on a new topic the same way an entry earns its slot: by producing measurably
  distinguishable output against its same-family neighbors on that topic. This is the non-negotiable
  order from the backlog - gate first, then generate at volume - applied to topic expansion: no new
  anchor topic ships renders until E1 exists.
- **Randomization is a pool-draw property, not a core property.** Once E1 exists, breadth and
  admission renders may draw topics randomly from the pool per gate run, with the draw (and its
  seed) logged for reproducibility. Regression always renders on the frozen core, so randomization
  never threatens the C3 invariant.
- **Sequencing.** The two-tier model is decided now (D1 / ADR 0017). Add `service-database-choice`
  diff-pairs (C2) on the existing core. Then, once E1 lands, generate the 9 seed topics' renders
  family by family, prioritizing the home topics of families that today have no native substrate
  (ceremonial and contemplative first, since those are the entries currently tested most off-home),
  promoting each cleared topic into the frozen core by ADR as it matures.
- **Schema touch.** Each sample's frontmatter already carries `topic_slug` and `topic_label`; the
  new topics need only their slugs registered wherever the anchor-topic set is enumerated (the
  generator and the site's vertical-slice index), with a flag marking core vs pool membership. The
  six-dimension matrix coordinates (`length`, `audience`, `stakes`, `medium`, `difficulty`) are a
  separate, later frontmatter extension tracked under the sample-depth work (E3), not blocked on this
  decision.

## Resolved questions

The four questions this document originally left open for the maintainer are now resolved as part of
D1 (see [`decisions.md`](decisions.md)):

1. **Slate balance.** Keep 4/2/2/2/2 for the seed (D1, original option A). Professional is the
   deepest domain and warrants four; the `outreach`/`copy` commercial gap is exercised on the public
   topics for now and remedied by a pool addition if the gate shows it under-served, rather than by
   re-weighting the seed.
2. **`morning-routine` domain.** `personal` (D2 recommendation; the renamed `relational` domain).
   Its dominant frame is personal-life design, not formation; topics 11 and 12 carry the
   contemplative load.
3. **The accountability boundary.** Test `accountability` on its boundary (topic 3), not on a
   minted register-bearing native topic (D3 recommendation), accepting the isolation discipline.
4. **Slugs.** The 9 first-draft slugs are accepted as the pool seed (D4) and stay renameable until
   they enter the generator and the route manifest. Because the pool is growable and gate-arbitrated,
   a slug that jars in use is cheap to change before generation.

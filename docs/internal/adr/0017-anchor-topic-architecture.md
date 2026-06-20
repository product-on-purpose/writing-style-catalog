---
adr_id: "0017"
title: "Anchor-Topic Architecture: a frozen regression core and a growable seed pool"
date: 2026-06-20
status: Accepted
supersedes_context: extends ADR 0006 (Phase 0 single anchor topic) for the scaling era; decides D1 - anchor topics
related:
  - docs/internal/adr/0006-anchor-topic-selection.md
  - docs/internal/adr/0010-domain-and-family-organization.md
  - docs/internal/release-plans/plan_v0.3.0/anchor-topics.md
  - docs/internal/release-plans/plan_v0.3.0/adherence-gate-spec.md
  - docs/internal/release-plans/plan_v0.3.0/decisions.md
  - docs/internal/scaling-the-library-100x.md
---

# 0017 - Anchor-Topic Architecture: a frozen regression core and a growable seed pool

## Status

Accepted - 2026-06-20 (decides D1 - anchor topics, the last open P0 in the v0.3.0 / expansion
decision record at `decisions.md`). This ADR extends ADR 0006 (the Phase 0 single anchor topic) for
the scaling era. ADR 0006 is not superseded; it is the predecessor this generalizes from one topic
to a structured set. The detailed design and the seed slate live in
`docs/internal/release-plans/plan_v0.3.0/anchor-topics.md`, which this ADR ratifies.

## Context

The catalog renders every entry as worked samples on a shared set of anchor topics. Holding the
topic constant is what makes a sample teach (a reader sees one entry across real contexts) and what
lets a diff-pair vary exactly one axis. Scaling toward 12+ samples per entry mechanically requires a
larger anchor-topic set, chosen so every domain and ideally every family has a native home topic to
be rendered on honestly. The set is the highest-leverage substrate input in the scaling program: the
sample matrix, the diff-pair generator, the per-entry distinguishability test-bed, and the E1
adherence gate's neighbor-rendering all key off it.

D1 - anchor topics was deferred 2026-06-09 for three reasons: (a) the slate's domain balance derives
from the taxonomy, which was under independent external review (A1 - taxonomy cuts); (b) the
maintainer wanted to see more worked examples before committing which topics best exercise each
family; and (c) the maintainer wanted to explore expanding or randomizing the topic set rather than
locking a small fixed slate.

The design tension behind (c): C3 - held-out reference set freezes the reviewed 60 (plus the 8
smoke-test pairs) as uncontaminated ground truth that re-runs every CI as a distinguishability
regression. That regression needs a **fixed** topic set, because a frozen pair can only be checked
against a recorded band if it is rendered on the same topic each time. Randomized or expanding
topics improve breadth and reduce overfitting to a dozen prompts, but they complicate the
frozen-regression guarantee. The deferral itself sketched the reconciliation: freeze a small fixed
core for regression while drawing additional gate renders from a larger randomized pool for breadth.

By 2026-06-20, reason (a) is resolved: A1 is ratified and ADR 0010 is Accepted, so the five-domain
structure the slate keys off (with the `relational` domain renamed `personal`) is settled. That
makes D1 decidable.

## Decision

Adopt a two-tier anchor-topic architecture.

### 1. Two tiers

- **Frozen regression core.** A small fixed set of anchor topics that the C3 held-out reference set
  renders on every CI as the distinguishability regression. It never changes silently and is the
  immovable yardstick: if a frozen pair drops below its recorded band after an edit, the build
  fails. Randomization never touches this tier.
- **Growable, optionally randomized seed pool.** The set the E1 gate draws home topics from for
  admission and breadth. The 12 designed topics in `anchor-topics.md` are the **seed** of this pool,
  not a hard cap. A new topic joins only after the gate clears its renders against same-family
  neighbors. Admission and breadth renders may draw topics randomly from the pool per gate run, with
  each draw and its seed logged for reproducibility.

### 2. Membership and growth

- The frozen core today is the existing 3 topics (`service-database-choice`, `async-standups`,
  `morning-routine`), which are already rendered across the 60 entries and already inside the C3 set.
  The core covers the `professional` and `personal` domains now.
- The core grows toward roughly one topic per domain (adding `ceremonial` and `contemplative`
  coverage) as E1 renders and clears the seed topics, each promoted into the core by a maintainer
  ADR. This is the gate spec's golden-set-staleness rule ("versioned, not eternal: add, never
  silently replace") applied to topics.
- The seed slate keeps the 4/2/2/2/2 balance over
  `professional/public/personal/ceremonial/contemplative`. New pool topics are admitted by the same
  isolation, domain-spread, and real-worldness criteria documented in `anchor-topics.md`,
  gate-arbitrated rather than hand-picked.

### 3. Folded sub-decisions

- `morning-routine` is assigned the `personal` domain (D2 - morning-routine domain recommendation).
- `accountability` is tested on its boundary (topic 3, professional) rather than given a
  register-bearing native topic, which would fail the isolation criterion (D3 - accountability
  family home recommendation).
- The 9 first-draft topic slugs are accepted as the pool seed (D4 - the 9 new topic slugs) and stay
  renameable until they enter the generator and the route manifest.

## Consequences

### Positive

- Closes the last open P0; v0.3.0's execution-blocking decision gate is fully cleared.
- Keeps C3's frozen-regression guarantee deterministic while delivering the expansion and randomness
  the deferral wanted. The two goals the maintainer thought were in tension are both met, because
  regression renders on the fixed core and only breadth draws from the (optionally randomized) pool.
- Removes premature commitment: because the pool is gate-arbitrated and growable, the slate need not
  be perfect up front. Topics earn their place empirically, which directly answers deferral reason
  (b) without a manual example-review gate.
- Reuses existing machinery rather than inventing new: the frozen core is the C3 set that already
  exists, and the growth rule is the gate spec's existing staleness mitigation.

### Negative / accepted costs

- The frozen regression core is thin at v0.3.0 (3 topics, covering only `professional` and
  `personal`). `Ceremonial` and `contemplative` entries have no frozen-core home topic until E1
  renders and clears them. Mitigation: the core grows by ADR as E1 lands; until then those entries
  regress on their nearest core topic, which is the same off-home test the gate already tolerates.
- Randomized pool draws add nondeterminism to admission and breadth runs. Mitigation: every draw
  logs its seed, so any run is reproducible, and regression (the part that must be stable) never
  randomizes.
- Two tiers are more machinery than a flat slate. Accepted, because the only alternative that avoids
  the machinery (a flat fixed 12) reintroduces the exact problems D1 was opened to avoid.

### Neutral

- The anchor-topic choice does not constrain catalog content; any topic works with any entry. The
  architecture is scaffolding for the sample set and the gate, not a taxonomy constraint.
- ADR 0006 stays Accepted and unchanged as the Phase 0 record; this ADR is its scaling-era successor.

## Alternatives considered

- **Flat fixed 12-topic slate (original D1 option A).** Simplest C3 regression, but it commits the
  slate and the per-family fit up front and gives up expansion and randomness, the two reasons D1 was
  deferred. It closes D1 by undoing the reasons D1 was opened. Rejected.
- **Pure growable / randomized pool, no special core.** Maximal breadth and least overfitting, but a
  rotating regression set is not a stable invariant: a sharpening edit could blur a previously crisp
  pair and slip through between draws, with no humans in the loop to catch it. That defeats C3, which
  the gate spec calls the single cheapest insurance against model collapse under the agentic-first
  posture (F3 - resourcing posture). Rejected.

---
adr_id: "0021"
title: "Add a machine-verified review_status so every entry carries a claim it has earned"
date: 2026-08-21
status: Proposed
supersedes_context: >
  Does not supersede an existing ADR. Proposes the second of three written paths past GATE 1
  (reviewed catalog) of the v1.0 readiness gates, which sits at 0 of 97 ledger rows decided.
  Governed by ADR 0019's change-class policy; classified there as class B (a widened enum),
  which corrects the class C assumption carried in the 2026-08-07 session handoff.
related:
  - docs/internal/adr/0019-schema-freeze-and-change-policy.md
  - docs/internal/adr/0020-versioned-schema-ids.md
  - docs/internal/adr/0009-pedagogical-entry-bar.md
  - docs/internal/review-ledger.md
  - docs/internal/backlog.md
---

# 0021 - Add a `machine-verified` review_status so every entry carries a claim it has earned

## Status

**Proposed (2026-08-21).** Not accepted. This is a product claim about how the catalog
describes itself, so it is drafted for maintainer ratification rather than adopted by an agent.
ADR 0019 set the precedent: it was drafted as Proposed, put as a decision with alternatives, and
ratified explicitly before any schema file moved. Nothing in this document is applied until it is
accepted.

**Why a class B change carries an ADR at all.** ADR 0019 requires one for class B "only if it
introduces a new concept rather than a field". A new lifecycle state, with its own admission
semantics and its own public claim, is a new concept. The process here is proportionate to what is
being decided, not to the size of the schema diff.

## Context

### The gate, and what is actually false

GATE 1 of the v1.0 readiness gates requires that `review_status` be honestly promoted. It sits
at **0 of 97 rows decided** in [`review-ledger.md`](../review-ledger.md), untouched since the
packets were generated. It is the only open blocker on the v1.0 launch.

The repository's own rule, stated in `CLAUDE.md`, `AGENTS.md`, and the ledger header, is:

> An entry may only be `stable` after a maintainer has reviewed it.

97 entries carry `review_status: stable` (15 Voice, 15 Tone, 15 Style, 52 Format). No maintainer
has read them one by one. By the repo's own rule, the label is false on all 97.

Note a second, smaller inconsistency this surfaces. The schema's own description string says
`stable = in active use`, which *is* true of the 97 and does not mention review at all. So the
contract and the governance rule disagree about what the word means, and the entries are
compliant under one reading and false under the other. Whichever path is chosen, that
disagreement should not survive.

### What the 97 have actually passed

They are not unvetted. Every one of them clears these checks on every CI run, and all of them
were green at the v0.13.0 tag. This list is deliberately restricted to checks that are
**enforced mechanically on every entry**, because that is what the new label will mean:

| Check | Where it lives |
|---|---|
| Conformance to the frozen axis schema | `check_schema_validation` |
| Cross-references resolve to entries that exist, and `confusable_with` is symmetric | `check_cross_references`, plus the symmetry test |
| Taxonomy membership: `domain` / `family` / `subfamily` per ADR 0010 | `check_taxonomy_membership` |
| Pedagogical substance: `tells`, `anti_patterns`, `failure_modes` present and non-trivial | ADR 0009, enforced by schema (shape) and `check_pedagogical_bar` (substance) |
| Gate 2 depth: renders on all 12 anchor topics | `check_sample_count` |
| Every worked example parses and validates | `check_examples` |

**What is deliberately not on that list, and why.** The adherence gate's blind-judge
distinguishability result is the catalog's strongest evidence, and it does **not** cover these 97.
`_agent-context/gate-pilot/CALIBRATION.md` records **9 unique entries across 6 packets and 18
judged slots, on one anchor topic**. That run validated the *instrument* (18/18 attribution, and a
negative control in which caricatures flip pass to fail); it was never a sweep over the catalog.
The de-duplication work was likewise an audit performed during the Stream-B waves, not a
per-entry gate that re-runs.

This matters more here than anywhere else in the repo. An ADR whose entire purpose is to stop the
catalog claiming more than it has earned cannot itself define the new label by evidence that does
not cover the entries receiving it. `machine-verified` is therefore scoped to the enforced list
above, and the distinguishability evidence keeps being cited for what it actually is: a pilot that
validated the measurement, at its own stated scope.

What the 97 have not had is a human reading them. `review_status` has no value that says that, so
`stable` overstates and `draft` understates. The catalog is forced to lie in one direction or the
other.

### Correction to the inherited framing: this is class B, not class C

The 2026-08-07 session handoff recorded this path as a class C change costing a minor bump today
and a major bump from 1.0.0, and recommended it partly *because* that made it the only option
with a deadline. **That classification is wrong**, and the argument built on it should not be
relied on.

ADR 0019 defines class B as, verbatim, "a new **optional** property, or a widened `enum`,
`pattern`, or numeric bound. Every document that validates today still validates, and the
accepted set only grows." Adding a value to the `review_status` enum is a widened `enum`. No
document that validates today stops validating; a document carrying the new value fails today
and would start passing. That is exactly and only the additive direction.

The test suite already encodes this asymmetry rather than leaving it to reading:
`tests/test_schema_change_policy.py::test_narrowing_an_enum_is_a_real_break` asserts that
*shrinking* an enum is a compatibility event. There is no companion test for widening one,
because under the policy there is nothing to catch. No test pins the contents of the
`review_status` enum, so nothing in the suite blocks the addition.

One counter-reading exists and is worth answering rather than leaving for a reader to raise.
Class C says "A change to a shared `$def` or to `entry.universal` is class C for *every* schema
that composes it." That sentence sits inside the class C keyword list and does two jobs: it names
`$defs` and shared definitions as class C keywords, and it scopes migration blast radius for a
change that is already class C. It does not promote an explicitly allowlisted class B edit to
class C because of which file it lives in. Read the other way, class B would be unreachable for
this catalog, since every entry-facing property lives in `entry.universal`.

**Practical consequence: the cost is a minor bump either way while the project is at `0.y.z`, so
the classification does not change what happens now.** What it changes is the argument for
urgency. Class B is a minor bump before *and* after 1.0.0, so this change does **not** get four
times more expensive at 1.0.0 and it is **not** the only option with a deadline. It should be
chosen on its merits or not at all.

### Is this the relabel the marketing plan forbids?

It has to be asked directly, because the prohibition is explicit. The plan says: "If a gate
cannot be met in a reasonable window (most likely GATE 1, since review is human-bottlenecked),
the honest move is to slip the launch, not to relabel." The ledger repeats it: "entries are not
relabelled to make a gate go green."

That rule forbids relabeling **upward**: moving entries toward a stronger claim they have not
earned so a gate reads green. This proposal moves 97 entries **downward**, from a claim they have
not earned to a weaker one they have. It reduces what the catalog asserts.

The plan also already contemplates a non-review outcome in the same breath: R1's condition is "an
honest promotion (or an honest 'still draft' on the ones not ready)". Its two options are
review-then-promote, or demote to `draft`. This proposal is a third member of that family: for
entries whose true state is neither, add the value that states it. The prohibited move and this
one point in opposite directions.

What must not follow from acceptance is the thing the last session refused: an agent pass that
manufactures 97 per-entry verdicts for bulk approval. That would be relabeling with extra steps.
This ADR changes what the label *claims*; it does not claim the reading happened.

## Decision

### 1. Add exactly one value, to exactly one schema

`machine-verified` is added to the `review_status` enum in
`schemas/entry.universal.schema.json` **only**.

`example.schema.json` and `schemas/experimental/diff-pair.schema.json` carry their own
`review_status` enums and are **not** touched. The 1,179 example files and 158 diff-pairs that
carry `reviewed` do so with tool-emitted semantics; widening those enums would invite the same
overloading this ADR exists to prevent. Stated here so a later reader does not mistake the
asymmetry for an oversight.

### 2. Name, and why not the values already there

**Recommended value: `machine-verified`.** It is self-describing, states the agent of
verification, and cannot be read as involving a person.

Two existing values were considered and rejected as the honest middle:

- **`reviewed`** is the obvious candidate and the wrong one. Its schema meaning is "editorially
  checked", which is precisely what has not happened. It is also already in service across 1,179
  example files and 158 diff-pairs with a generator-emitted meaning. Reusing it would recreate the
  ambiguity being fixed, and would make one word mean two different things depending on which
  file it appears in.
- **`draft`** understates, and it is not cost-free: `check_sample_count` exempts non-admitted
  entries from the 12-render bar, the site stamps a "may change or be withdrawn before promotion"
  caution on drafts, and the recommender refuses to recommend them. Applying that to 97 entries
  that pass every automated gate would make the catalog describe itself as less finished than it
  is, and would empty the recommender (see decision 4).

Alternative names, if the maintainer prefers: `gate-verified` (ties to the repo's own gate
vocabulary, but requires knowing what the gates are) or `machine-checked` (softer on what
"verified" implies). `machine-verified` is recommended; the choice is the maintainer's, and
changing it is a search and replace inside this same change.

### 3. The ladder, and who may set each value

| Value | Means | Who may set it | Admitted to the shipped catalog |
|---|---|---|---|
| `draft` | Initial content. Candidate, not shipped. | Anyone, including tooling | No |
| `machine-verified` | Passes every enforced check in the Context table, and nothing beyond them. **No maintainer has read it.** | Tooling, when those checks pass | **Yes** |
| `stable` | A maintainer read this entry and approved it. | **Maintainer only** | Yes |
| `reference-quality` | Exemplary; maintainer-reviewed. | **Maintainer only** | Yes |
| `deprecated` | Superseded by another entry. | Maintainer | No |
| `reviewed` | Unused for taxonomy entries. Retained because removing an enum value is class C; in active use in the example and diff-pair schemas. | Tooling, in those schemas | n/a |

The existing governance rule is unchanged and unweakened: `stable` and `reference-quality` still
require maintainer review. This adds a rung below them; it does not lower them.

### 4. Admission semantics - the load-bearing decision

`machine-verified` **is admitted**. Two hardcoded sets must be updated in the same change:

- `tools/validate.py::check_sample_count`, `admitted = ("stable", "reference-quality")`
- `skills/entry-recommender/scripts/recommend.py`, `STABLE_STATUSES = {"stable", "reference-quality"}`

**If either is missed, the recommender's candidate pool silently drops to zero.** All 97 movers
are currently `stable`, and no entry anywhere carries `reference-quality`, so after the migration
those sets would match nothing at all. The failure is silent in the sense that `validate.py`
would still pass; the recommender would simply return empty axes.

Two consequences follow, both deliberate:

- Gate 2's 12-render bar **continues to bind** these entries. They keep the renders they have;
  none need generating. An entry does not get to shed its depth obligation by being honest about
  its review state.
- The recommender's AC-6, "never recommend a draft", is untouched and still holds.
  `machine-verified` is not a draft.

Rename `STABLE_STATUSES` to `ADMITTED_STATUSES` in the same change, since after this it no longer
describes a set containing `stable` alone.

### 5. The status must be visible, or the change is cosmetic

`scripts/gen-site.mjs` special-cases `draft` only. It gains a distinct notice for
`machine-verified`, worded to say what was and was not done. Suggested text, for the maintainer
to edit:

> **Machine-verified.** This entry passes the catalog's automated checks: it conforms to the
> frozen schema, its cross-references resolve, it carries worked examples on all twelve anchor
> topics, and it meets the pedagogical bar (`tells`, `anti_patterns`, `failure_modes`). It has not
> yet been read line by line by the maintainer.

It must read as a factual statement of what was checked, not as an apology and not as a
credential. Note what it does **not** say: nothing about distinguishability or non-duplication,
per the scope limit set in Context. If that notice ever grows a claim, the claim needs a check
behind it that runs on every entry. An honest status no reader can see is not honesty, it is
bookkeeping; an honest status that quietly inflates is worse than the label it replaced.

### 6. The recommender should pass the status through

`recommend.py` emits `id`, `score`, `one_liner`, and match data per recommendation, but not
`review_status`. It should include it, so a consuming skill can surface "not yet maintainer-read"
alongside a recommendation. Low cost, and it keeps the honesty at the surface where an entry is
actually chosen. Lower priority than decisions 1 through 5; drop it if it complicates the change.

### 7. Tighten `stable`'s description in the same PR (class A, free)

The enum's `description` string currently reads `stable = in active use`, which is the
disagreement noted above. It is corrected to say maintainer-reviewed, and the new value is
described. `description` is on ADR 0019's class A allowlist, so this rides along at no additional
cost. Doing it in this PR is what keeps the contract and the governance rule from continuing to
disagree.

### 8. Version, and what this does *not* touch

- **Plugin version: minor bump, `0.13.0` to `0.14.0`**, per ADR 0019 class B. A `CHANGELOG.md`
  note is required.
- **`SCHEMA_CONTRACT_VERSION` does not move, and no snapshot is created.** ADR 0020 states that
  the contract version "bumps only when the contract itself breaks". A widened enum does not
  break it: every document valid under the published `v1` stays valid. The schema at
  `/schemas/v1/entry.universal.schema.json` is updated in place, which is what a class B change
  under a versioned contract path means. `test_contract_version_bump_requires_a_snapshot` is not
  triggered, because the constant does not move.
- Consumers pinning `v1` see a schema that accepts strictly more than before. That is the
  additive guarantee working as designed.

### 9. What GATE 1 becomes

GATE 1 is **not** closed by this change, and the ledger is not marked done.

- **Before:** "read 97 entries before launch", with the launch blocked until then.
- **After:** "every entry carries a status that is true", which acceptance of this ADR plus the
  migration satisfies. The reading continues afterward as background work, and each entry that
  gets read moves `machine-verified` to `stable` and gains its ledger row.

The ledger survives unchanged in purpose: it becomes the record of the 97 promotions still to
come, rather than the record of a blocking sweep. Its scope line and its "may only be `stable`"
header need rewording only to reflect the new starting status.

## Migration checklist

Everything below lands in one PR. The count of 97 is a file count taken 2026-08-21 and must be
re-derived at migration time, never copied from this document.

| # | Surface | Change |
|---|---|---|
| 1 | `schemas/entry.universal.schema.json` | Add the enum value; rewrite the `description` per decision 7 |
| 2 | 97 `taxonomy/*/*/ENTRY.md` | `review_status: stable` to `review_status: machine-verified` |
| 3 | `tools/validate.py` | `admitted` tuple in `check_sample_count` |
| 4 | `skills/entry-recommender/scripts/recommend.py` | `STABLE_STATUSES` to `ADMITTED_STATUSES`, plus the new member; decision 6 if kept |
| 5 | `tools/promote.py` | Currently flips `draft` to `stable` only. The ladder now has two rungs: `draft` to `machine-verified` (tooling) and `machine-verified` to `stable` (maintainer). Its `_DRAFT_LINE` regex and single-match guard generalize accordingly |
| 6 | `tools/review_packet.py` | `--status` default is `stable`; becomes the awaiting-review status. Also line 173, which flags `stable` entries lacking `confusable_with` |
| 7 | `tools/agentic/promote.js` | Emits `review_status: reviewed`; reconcile with the ladder |
| 8 | `taxonomy.json` | Regenerate via `python tools/build-indexes.py` (no code change; `review_status` is already an index field) |
| 9 | `scripts/gen-site.mjs` | The notice from decision 5, in both the entry page and format-template paths |
| 10 | `tests/test_gate2_sample_count.py`, `tests/test_review_packet.py` | Hardcoded statuses. Grep the repo, not just `tests/`, for `stable` before assuming these are the only two. `tests/test_schema_change_policy.py` pins no enum contents and needs no change |
| 10b | `skills/entry-recommender/SKILL.md`, `skills/entry-recommender/README.md`, `skills/writing-instruction-builder/scripts/build-instruction.py` | Prose and docstrings that say "the stable catalog" or "scores the stable catalog". Wording only, but it is user-facing in the skill docs |
| 11 | `docs/internal/review-ledger.md` | Header rule and scope line per decision 9 |
| 12 | `docs/internal/backlog.md` | GATE 1 row |
| 13 | `AGENTS.md`, `CONTRIBUTING.md`, `CLAUDE.md` | The promotion rule gains its middle rung. The existing "never `stable` without review" sentences stay true and are kept |
| 14 | `README.md` | "97 stable taxonomy entries" and "the 97 stable entries" (two places) |
| 15 | `library.json`, `.claude-plugin/plugin.json` | "Ships 97 curated entries". Kept byte-identical to each other, enforced by `validate-plugin-manifest.mjs` |
| 16 | `agent-plugins` registry listing | The third copy of the same sentence. Separate repo, separate PR, per the re-pin checklist |
| 17 | `CHANGELOG.md` | Class B note under `[Unreleased]`, at merge time, not at open time |

**Verification before merge:** `python tools/validate.py` green with the same entry, diff-pair,
and example counts; `python tests/eval/run_eval.py --verbose` still 10/10, which is the only
automatic catch if item 4 is missed; `node --test tests/gen-site.test.mjs`; the full pytest
suite; `node scripts/validate-plugin-manifest.mjs`; the dash sweep.

**Expected behavioral delta: none.** The same 97 entries are admitted before and after, so the
recommender should score identically and the eval should not drift. A changed eval result means
an admission set was missed, not that the catalog changed.

### On the word "curated"

Items 14 through 16 are launch copy, and the maintainer owns the wording. "97 curated entries" is
close to the overstatement this ADR exists to remove, since "curated" implies a curator. "97
entries" with the status made visible on the site is the safe version. Flagged rather than
decided.

## Alternatives considered

**A. Path 1 - review the 45 Voice/Tone/Style entries, return the 52 Formats to `draft`.** Roughly
two hours in batches of ten. Keeps the enum untouched and the standard intact, and yields a
genuinely maintainer-reviewed core. Costs: the headline drops from 97 to 45, 52 site pages gain a
caution badge, and the recommender's Format axis loses all 52 of its admitted entries, which is a
functional regression rather than a cosmetic one. Still available, and still the shortest
defensible launch. Not mutually exclusive with this ADR: accepting this and then reviewing at
leisure reaches the same end state without the interim regression.

**B. Path 3 - slip and keep building depth.** The plan's stated default and the honest baseline.
Costs nothing and claims nothing. Its only weakness is that it leaves 97 entries carrying a false
label for as long as the slip lasts, which is the specific thing GATE 1 exists to prevent.
Choosing B means accepting that the label stays false in the meantime.

**C. Redefine `stable` as "in active use" and drop the review requirement.** The schema's own
description already says this, so it is the smallest possible edit. Rejected: it resolves the
contradiction by deleting the standard rather than meeting it, and the review requirement is the
credibility mechanism the whole launch plan is built on.

**D. Do nothing to the schema; record the true state only in the ledger.** The ledger is internal
and gitignored packets back it; a user reading the site or installing the plugin would still see
`stable`. Fixes the record for maintainers and for no one else.

## Consequences

### Positive

- Every entry carries a claim it has earned, which is what GATE 1 was actually for. The gate is
  met by making the label true, not by making the number look done.
- It costs less than the handoff recorded: class B, minor bump, no contract-version bump, no
  snapshot obligation, no migration for external consumers.
- Zero functional regression. The admitted set is unchanged in membership, so the recommender,
  the renders, and the depth bar all behave exactly as they do today. Alternative A cannot say
  that.
- The catalog gains a vocabulary for a state it has been in all along and could not express:
  machine-checked but unread. Every future Stream-B batch lands there naturally instead of jumping
  from `draft` to a maintainer-only status.
- The `stable` = "in active use" versus "maintainer-reviewed" contradiction gets closed as a free
  rider.

### Negative

- **A third status can read as hedging.** A reader who does not care about the distinction sees a
  project that would not commit. The mitigation is decision 5's wording: state what was checked,
  plainly and specifically, and let it read as precision rather than as a disclaimer. This is a
  product-voice risk and it is the main reason this is a maintainer decision.
- **The headline weakens.** "97 curated entries" becomes something more careful. The honest
  version is less impressive than the current version, which is the point, but it is still a real
  cost to launch copy.
- **The enum grows and cannot easily shrink.** Removing a value later is class C. If the full
  review completes and every entry reaches `stable`, `machine-verified` stays in the schema
  unused, next to `reviewed`, which is already in exactly that position for entries. Two vestigial
  values is a smell, and the honest answer is that the enum would benefit from a class C cleanup
  someday, ideally before 1.0.0 while class C is still a minor bump.
- **Seventeen surfaces move at once**, three of them published (README, the two manifests, the
  registry listing). Counter drift across exactly these surfaces was the whole diagnosis of the
  v0.13.0 release. Every count in this change must come from a file count.
- The migration touches 97 files mechanically. A regex flip across `ENTRY.md` frontmatter is the
  same operation `promote.py` already does carefully, for the same reason: a naive replace can hit
  an indented lookalike.

### Neutral

- The reading still has to happen for the catalog to reach `stable`. This ADR buys an honest
  interim state, not a shortcut to a reviewed catalog. Anyone reading it as "GATE 1 solved" has
  misread it.
- The `reviewed` value stays in the entry enum, unused. Removing it is class C and is not worth a
  separate migration on its own; it belongs in the cleanup named above.
- ADR 0020 contains a stale sentence: its decision 2 moves `diff-pair.schema.json` to
  `schemas/experimental/`, while its Consequences note still says diff-pair is "published under
  `v1` alongside the frozen five". The file is at `schemas/experimental/` and decision 2 is
  operative. Noted here because it was found while establishing that this change does not touch
  the contract version; correcting it is a class A documentation fix outside this ADR's scope.

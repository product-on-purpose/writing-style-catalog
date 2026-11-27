---
adr_id: "0022"
title: "Record a per-entry distinguishability measurement in entry frontmatter"
date: 2026-11-26
status: Proposed
supersedes_context: >
  Does not supersede an existing ADR. It writes the data contract for the per-entry
  `distinguishability` score that `adherence-gate-spec.md` already specifies as a Gate 1 output
  ("a recomputed per-entry distinguishability score written to frontmatter") and that frontier
  idea 1 of scaling-the-library-100x.md ranks first among the unbuilt ideas. Governed by ADR
  0019's change-class policy; classified below as class B, with the one place that classification
  is arguable stated and tested rather than assumed.
related:
  - docs/internal/adr/0019-schema-freeze-and-change-policy.md
  - docs/internal/adr/0020-versioned-schema-ids.md
  - docs/internal/adr/0021-honest-middle-review-status.md
  - docs/internal/adr/0017-anchor-topic-architecture.md
  - docs/internal/scaling-the-library-100x.md
  - docs/internal/agentic-generation-spec.md
  - docs/internal/release-plans/plan_v0.3.0/adherence-gate-spec.md
---

# 0022 - Record a per-entry distinguishability measurement in entry frontmatter

## Status

**Proposed (2026-11-26).** Not in effect. The schema is frozen by ADR 0019, so the field it
describes exists nowhere yet: no schema and no `ENTRY.md` was changed in the change that added
this document. Ratification is the maintainer's, and decision 4 and decision 6 are the two that
genuinely need a person rather than a reading.

## Context

### The catalog's value rests on one measurement, taken once

The 2026-05-31 adherence smoke test judged eight within-axis confusable pairs blind and attributed
8 of 8 correctly, chance being about 0.4 percent. That result is why the project is a measured
instrument rather than a well-written list, and it is cited in launch copy, in the strategy
documents, and in the README's claim that the distinctions are real.

It is also a photograph. It was taken at 60 entries, with strong models at both ends, on eight
pairs. Today the catalog holds 118 entries. **No individual entry carries a number.** Nothing
recomputes when an entry is edited. If a future edit to `senior-consultant` collapsed it toward
`pragmatic-architect`, every automated check in the repository would still pass: `validate.py`
checks shape, substance of the pedagogical fields, referential integrity, and sample counts, and
none of those can see a collapsed distinction.

### What already exists, and what is therefore missing

Four pieces of the measurement are built and in the tree:

- **The neighbor graph.** `confusable_with` is curated, referentially enforced, and symmetric
  (guarded by tests). `tools/adherence_gate.py` computes the Gate 1 adversary set from it.
- **A fixed topic set.** ADR 0017 froze the twelve anchor topics; `tools/anchor_topics.py` is the
  module.
- **A validated judge, on free infrastructure.** The gate pilot (`tools/gate_pilot.py`, PR #46)
  proved the architecture cross-vendor: a Codex-companion judge, fed a blind packet, re-attributed
  18 of 18 slots, detected caricature when given one, and bent its band scale correctly on a
  near-duplicate probe. The calibration record is `_agent-context/gate-pilot/CALIBRATION.md`.
- **A producer in the field's own shape.** `tools/distinguishability.py` computes a band for one
  entry against one declared neighbor on a named topic, from the renders already committed under
  `examples/vertical-slices/`. Its first run attributed 10 of 10 trials correctly across four
  pairs on all four axes.

What is missing is the one piece that turns a run into a property of an entry: **somewhere to put
the answer.** A measurement that lives in a gitignored working file is an audit. A measurement
that lives on the entry is a contract.

### This is not a new idea, and that matters for the scope

`adherence-gate-spec.md` already specifies the field as a Gate 1 output, in those words, and
assigns it two jobs: the internal trust signal that drives the `review_status` tier, and the
public proof. Frontier idea 1 names the same object and the same sub-fields. So this ADR is not
proposing the measurement. It is doing the narrower thing those documents left undone: fixing the
shape, the semantics, who may write it, and what it does **not** mean, before any of it ships.

Decision 4 departs from the gate spec on one of those two jobs, deliberately and with the
conflict named.

## Decision

### 1. One optional object on the shared entry schema

Add `distinguishability` as an **optional** property of
`schemas/entry.universal.schema.json`, so it is available on all four axes. When present it is an
object, and these sub-fields are then required:

| Sub-field | Type | What it records |
|---|---|---|
| `score` | number, 0 to 1 | Attribution accuracy over the trials: the fraction of blind trials in which the judge assigned both passages to the right entry |
| `trials` | integer, 1 or more | How many blind trials the score is over |
| `band` | one of `identical`, `subtle`, `clear`, `dramatic` | The **worst** band the judge reported across those trials |
| `neighbor` | entry id | The declared `confusable_with` entry it was tested against |
| `topic` | anchor-topic slug | The anchor topic both passages were written on |
| `judge_model` | string | The judge that returned the verdicts |
| `generator_model` | string | The model that wrote both passages |
| `measured_on` | date, `YYYY-MM-DD` | When the measurement was taken |

`harness` (string) is optional and records the producing tool, so a reader can reproduce the
number.

The proposed sub-schema is in the appendix. It is **not applied** by the change that adds this
ADR.

Three choices inside that table are the substance, not formatting:

- **`trials` is required, not optional.** A pairwise forced choice over two slots is right or
  wrong as a whole, so one trial scores 0 or 1 and a score of 1.0 at N=1 is a coin flip that
  landed. A score without its N is not a measurement.
- **`band` is a floor, not a mean.** The first harness run found the band moves with presentation
  order: `pragmatic-architect` vs `senior-consultant` rated `dramatic` in one order and `clear`
  in the other, on the same two passages, with attribution correct both times. A mean would hide
  the worse reading, and Gate 1's own rule auto-fails on a single `identical`. The field therefore
  claims "at least this distinguishable".
- **`topic` is required because the band is conditional on it.** The same style pair rated `clear`
  on `a-hard-year-in-review` and `dramatic` on `service-database-choice`. A field that recorded no
  topic would be recording an average over conditions it never measured.

### 2. The field is absent until measured, and absence is not a failure

No entry gets a placeholder, an empty object, or a `null`. 118 entries carry nothing today and
most will carry nothing for a long time; the field appears on an entry when a run has produced a
number for it. `validate.py` gains no check that requires the field. This follows the review-ledger
precedent from ADR 0021: 97 entries sat at `machine-verified` with 0 read, and the honest record of
that was an empty ledger, not a fabricated one.

### 3. ADR 0019 class: **class B**, and here is the part that is arguable

Class B is "a new optional property", which this is. The classification was nonetheless checked
against ADR 0019's own text in the three places it could fail, because a wrong answer here is
expensive: a class C change to a frozen schema does not merely cost an ADR and a version bump, it
breaks the `v1` contract and forces a `schemas/v2` path plus a retained snapshot under ADR 0020.
That is the cost that got the vestigial-enum cleanup declined: ADR 0021's Neutral section
records that on 2026-10-28 the maintainer declined removing the unused `reviewed` value before
1.0.0, precisely because narrowing the enum would bump `SCHEMA_CONTRACT_VERSION` to `v2` and
serve `v1` alongside it.

**Check 1 - the `entry.universal` sentence. Already settled, by ADR 0021.** Class C says "A
change to a shared `$def` or to `entry.universal` is class C for *every* schema that composes
it". Read as "any change to `entry.universal` is class C", that sentence would make class B
unreachable on the shared schema. ADR 0021 answered this directly when it classified the
`machine-verified` enum widening, in its section "Correction to the inherited framing": the
sentence "sits inside the class C keyword list and does two jobs: it names `$defs` and shared
definitions as class C keywords, and it scopes migration blast radius for a change that is
already class C. It does not promote an explicitly allowlisted class B edit to class C because
of which file it lives in." This ADR follows that reading rather than re-deriving it, and the
same corroboration applies: decision 3 of ADR 0019 names "`family` on styles and tones" - a new
optional property on a per-axis schema - as "a class B change followed later by a class C
tightening".

**Check 2 - keywords used inside the new object.** The sub-schema uses `type`, `enum`, `minimum`,
`maximum`, `required`, `properties` and `pattern`, all introducing assertions on a property that
does not exist yet rather than narrowing one that does. It deliberately avoids `format`, which ADR
0019 names class C by keyword; the date is a `pattern` instead, which also makes it assertive
across drafts rather than optional-by-convention. It adds no `$ref`, no `$defs`, and no
`additionalProperties`.

**Check 3 - the open-schema edge, which is real.** No schema in this repository sets
`additionalProperties: false` or `unevaluatedProperties`, which was verified by grep and then by
validating synthetic documents through the registry `validate.py` actually builds. The result:

| Document | Today | After declaring the typed optional property |
|---|---|---|
| A real entry with no `distinguishability` | validates | validates |
| A well-formed `distinguishability` object | validates | validates |
| `distinguishability: "a string"` | **validates** | **rejected** |
| `distinguishability: {score: 1.0}` | **validates** | **rejected** (missing required sub-fields) |

So the second clause of class B's rationale - "the accepted set only grows" - is literally false
here. A document that squats the key with a junk value validates today and would stop. ADR 0019's
compatibility test says either direction is a compatibility event, and its tie-breaker says the
default is C.

**Recommended ruling: class B anyway, for a reason that generalises.** Every schema in this
repository is open, so on the strict reading *no* new property could ever be class B, and class B
would be dead law in the only repository it governs - which contradicts ADR 0019's own worked
example. The documents the edit removes from the accepted set are documents that use a key the
contract never defined, with a shape that never meant anything. Treating those as protected
compatibility would freeze the namespace, not the contract.

**So the ruling needs a one-sentence amendment to ADR 0019 rather than a silent reading**, and
this ADR proposes it as part of ratification:

> Class B also covers declaring a new optional property on a schema that does not restrict
> additional properties, even though a document that already used that key with an undeclared
> shape may stop validating. Only documents that squatted the key are affected, and they relied on
> no contract.

`tests/test_schema_change_policy.py` gains a synthetic test pinning that premise, in the same
style as the tests that pin class A, so the reasoning is auditable rather than remembered.

**Cost if ratified as class B:** a minor version bump and a `CHANGELOG` note. No entry migration
and no contract-version bump.

### 4. The field does not gate `review_status`, and this contradicts the gate spec

`adherence-gate-spec.md` says the score "is both the internal trust signal that drives the
`review_status` tier and the public proof that is the moat". **This ADR proposes it drive
neither tier transition, in v1:**

- `machine-verified` keeps exactly the enforced checks ADR 0021 enumerated. A measured band is not
  added to them.
- `stable` keeps meaning a maintainer read the entry. A good band is not a substitute for reading,
  and the whole point of ADR 0021 was to stop one word carrying a claim nobody had earned.

Three reasons, the first two of which are new information since the gate spec was written:

1. **The instrument is not yet stable enough to gate on.** The band flips with presentation order
   and with topic, and two independent later runs disagree with the May smoke test about whether
   `narrative-case-study` vs `chronological-narrative` is `subtle`. A signal that moves under
   re-presentation can inform a maintainer; it should not block a merge until its variance is
   characterised.
2. **Gating requires recomputation, and recomputation is the part that is not free.** A gate that
   fires on a stored number rewards whoever last ran the harness, not whoever is correct now. The
   honest version of gating is the CI ratchet of frontier idea 2, which needs a judge CI can call
   and therefore fires a paid-automation trigger. See the costed note alongside this ADR.
3. **It keeps the ladder single-meaning.** ADR 0021's value is that each rung states who
   verified what. Adding a second axis of trust to the same enum re-creates the overloading it
   removed.

What the field does instead is **inform**: a `subtle` band is a maintenance signal and a review
priority, which is exactly the use frontier idea 1 claims for it ("a maintenance signal rather
than a buried footnote"). Promoting it to a gate is a later ADR, and should be written after the
ratchet exists and the variance is known.

### 5. Who may write it, and the anti-gaming rule

- **Tooling writes it, from a run record.** Hand-editing the object is prohibited by the same logic
  that made the gate spec say the score is "recomputed, never hand-set, so it cannot be gamed by
  editing a YAML field".
- **One generator for both passages.** `generator_model` is a single string, so a measurement whose
  two passages came from different generators may not be recorded. This is a live constraint, not
  a hypothetical: in the first harness run one pair, `adr` against `design-doc` on
  `service-database-choice`, drew one passage from a `claude-opus-4-7` render and the other from
  a `claude-sonnet-4-6` render, because the committed renders were made in different waves. That
  pair could not populate the field until one side were re-rendered. The other four pairs were
  single-generator. The alternative - letting `generator_model` be an array - is cheaper now and
  makes every cross-model comparison in frontier idea 3 ambiguous later, so the single string is
  recommended.
- **One topic per measurement, and a trial is one presentation.** A pairwise forced choice is
  right or wrong as a whole, so one trial scores 0 or 1, and the two presentation orders of one
  passage pair are not independent samples: they test order sensitivity on the same prose. A
  measurement that spans several topics is therefore several measurements, not one with a larger
  N. Where a pair has been judged on more than one topic, the field records the topic whose
  trials produced the recorded floor band, and the other topics live in the run records. Letting
  `topic` be a list would average over conditions the measurement never pooled.
- **The measurement must be blind, and blindness is checked, not promised.** Many committed renders
  open with a heading naming the entry; the harness strips it and then refuses to emit a packet
  whose passages still name either entry.

### 6. Publishing the field fires one of the factory spec's three paid triggers

`agentic-generation-spec.md` fences paid automation behind three triggers, none of which has ever
fired. The third is "publishing provenance-pinned distinguishability scores". This ADR is that
trigger's subject, so it has to answer it rather than inherit it.

The answer splits the thing the trigger names:

- **Producing a band, by hand, per entry, stays free.** The harness generates nothing and the judge
  is an in-session subagent. The first run cost zero. Populating all 118 entries once is on the
  order of 118 to 236 subagent judge calls, hand-driven in batches - large, but the same kind of
  work the breadth waves already did for free.
- **Keeping every band current does not stay free.** Recomputing on edit, on a neighbor's edit, and
  on a model release is CI work, and CI cannot call an in-session subagent. That is the ratchet,
  and it fires the trigger.

**Recommendation: ratify the field now and leave the trigger unfired.** The field is useful as a
hand-produced, dated record; it is strictly more useful once CI maintains it; and the second thing
is a spending decision that should be made against the costed note, not implied by accepting a
schema shape.

### 7. What the number means, stated on the entry

Any surface that shows the field shows it as a dated, conditional floor, not a grade. The claim the
object supports is: *on this topic, against this neighbor, with this generator and this judge, on
this date, over N blind trials, a judge attributed the pair correctly `score` of the time and rated
the distinction at least `band`.* It does not support "this entry is better than that one", a
comparison across different topics or judges, or any claim about an entry whose phrasing changed
after `measured_on`.

## Alternatives considered

**A sidecar file instead of frontmatter** - for example `_measurements/<axis>/<id>.json`, or one
catalog-wide `distinguishability.json`. Genuinely attractive: it needs no schema change at all, so
it is a class-free change under ADR 0019; it can hold full run records rather than a summary; and
it cannot be hand-edited into an entry's provenance. Rejected for the reason the frontmatter won
everywhere else in this repository: the atomic-folder pattern of ADR 0002 keeps everything about an
entry in the entry, consumers already read frontmatter and would need a second loader, and a
measurement in a sidecar is an audit artifact that drifts out of sync with the thing it describes.
The run records stay as files regardless - the field is a summary of them, not a replacement, and
nothing stops a later ADR from publishing the records too.

**A bare `band` string with no object** - cheapest possible field. Rejected: without `trials`,
`topic`, `judge_model`, `generator_model` and `measured_on`, the band is unfalsifiable and cannot
be re-derived, which removes the one property that makes it defensible against a competitor's
prose description.

**Store the score only in the public site build** - a leaderboard page generated from run records,
nothing in the catalog source. Rejected as the primary home because an entry installed from the
marketplace would carry no evidence, which is where consumers actually read the catalog. It remains
a good secondary surface.

**Do nothing until the ratchet is funded.** This is the status quo and it is not unreasonable: the
field is strictly more useful when maintained automatically. Rejected because the shape is the part
that is expensive to change later. Fixing the contract while a class B change is still cheap, and
before 1.0.0 makes class C a major bump, is the same reasoning ADR 0020 used to pull its own
change forward.

## Consequences

### Positive

- An entry can carry its own evidence. The claim "a blind judge distinguishes this from its
  nearest neighbor" becomes per-entry, dated and reproducible rather than a single 2026-05 footnote
  about eight pairs.
- The `subtle` band becomes a queryable maintenance signal, which gives the long-standing C1
  backlog item ("sharpen the two subtle pairs") a definition of done that a tool can check.
- It is the prerequisite every other frontier idea names. Ideas 2, 3 and 6 all depend on score
  storage, so the contract has to exist before any of them is worth costing.
- The classification work is reusable. Whatever the maintainer rules, the open-schema edge is now
  tested rather than argued, and the next additive field inherits the answer.

### Negative

- **It introduces a field that is empty almost everywhere,** on purpose. A reader who meets the
  schema before the data will reasonably ask why. Decision 2 says so out loud, and the ADR 0021
  ledger is the precedent for preferring a visible gap to a fabricated one.
- **It publishes a number that can be read as more precise than it is.** A score of 1.0 over 2
  trials looks like certainty and is not. Decision 1 forces `trials` into the object and decision 7
  forces the conditional framing onto every surface, but a number on a page invites misreading in a
  way prose does not.
- **The band is the softest part of the measurement.** It moved under presentation order in the
  first run. Recording the floor is a mitigation, not a fix; characterising that variance is
  genuinely unfinished work.
- **Measuring from committed renders measures the phrasing as it stood when the render was made.**
  One pair in the first run drew its passages from generator waves months apart, and every render
  used predates the run by months. `measured_on` and `generator_model` make the staleness
  visible; they do not remove it.
- **The field cannot be produced for every entry from the renders in the repository.** Under the
  leak check as corrected by PR #198, 89 of the 118 entries have at least one anchor topic on
  which their declared pair can be judged blind; the other 29 are almost all ceremonial,
  contemplative and document formats whose prose names the format, `eulogy` and `adr` among them.
  For those, the field waits on renders that do not name themselves, or on a protocol that masks
  the term instead of refusing the packet.
- **Nothing invalidates a stale field in v1.** An entry whose `llm_instruction_phrasing` is edited
  after `measured_on` keeps a number that no longer describes it. That is exactly the hole the
  ratchet fills, and until it is funded the date is the only defence.

### Neutral

- **The band scale is only partly calibrated at both ends.** The gate pilot's near-duplicate probe
  produced `subtle` deliberately, and the first band-harness run produced `clear` and `dramatic`
  but no `subtle` and no `identical`. So the top of the scale is now observed, the bottom is
  observed only under a probe designed to force it, and no production run has yet produced the
  band that would matter most.
- `tools/gate_pilot.py` stays as it is. Its judge prompt offers three bands and cannot emit
  `dramatic`; it remains the calibrated instrument for N-way admission, and the field's producer is
  a separate module.
- This ADR does not touch `example.schema.json` or `schemas/experimental/diff-pair.schema.json`.
  Worked samples and diff-pairs carry their own `review_status` enums with tool-emitted semantics,
  and nothing here changes them.

## Appendix: the proposed sub-schema

Not applied. Shown so that ratification is a decision about concrete text.

```json
"distinguishability": {
  "type": "object",
  "title": "A blind distinguishability measurement against one declared neighbor",
  "description": "Produced by tools/distinguishability.py from a run record; never hand-set. A dated, conditional floor: on this topic, against this neighbor, with this generator and judge, a blind judge attributed the pair correctly `score` of `trials` times and rated the distinction at least `band`.",
  "required": ["score", "trials", "band", "neighbor", "topic", "judge_model", "generator_model", "measured_on"],
  "properties": {
    "score": { "type": "number", "minimum": 0, "maximum": 1 },
    "trials": { "type": "integer", "minimum": 1 },
    "band": { "type": "string", "enum": ["identical", "subtle", "clear", "dramatic"] },
    "neighbor": { "type": "string", "pattern": "^[a-z][a-z0-9-]*[a-z0-9]$" },
    "topic": { "type": "string", "pattern": "^[a-z][a-z0-9-]*[a-z0-9]$" },
    "judge_model": { "type": "string", "minLength": 1 },
    "generator_model": { "type": "string", "minLength": 1 },
    "measured_on": { "type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$" },
    "harness": { "type": "string", "minLength": 1 }
  }
}
```

Two deliberate details. `neighbor` and `topic` carry the repository's slug pattern rather than a
`$ref` to a shared definition, because `$ref` and `$defs` are class C keywords and no shared
definition exists to point at. `measured_on` is a `pattern` rather than `"format": "date"` for the
same reason, and because `format` is advisory in several JSON Schema drafts while a pattern asserts
in all of them.

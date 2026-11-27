---
title: Stream-C Axis Rebalance - the candidate slate for Voice, Tone, and Style
date: 2026-11-26
status: slate proposed; 3 exemplars authored; 41 candidates not started
owner: maintainer (admission decisions); agent (generation + gating)
related:
  - docs/internal/agentic-generation-spec.md (the factory design and the canonical gate prompts)
  - tools/agentic/README.md (how to run each harness, now axis-parameterized)
  - docs/internal/adr/0009-pedagogical-entry-bar.md (the bar every new entry must meet)
  - docs/internal/adr/0010-domain-and-family-organization.md (families, the 12-member trigger, scope boundaries)
  - docs/internal/_working/catalog-inventory-aspirational_2026-05-16.md (frozen; the Voice territory)
  - docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md (frozen; the 30-per-axis target and the Tone and Style sketches)
  - docs/internal/release-plans/stream-b-breadth-status.md (the Format precedent this program mirrors)
---

# Stream-C Axis Rebalance: the candidate slate for Voice, Tone, and Style

## The answer first

This document proposes **44 new entries**: 14 Voice, 15 Tone, and 15 Style. Admitting all
44 takes the three thin axes from 16, 15, and 15 to 30 each, which is the Phase 2 target
set in `phase-2-catalog-expansion_2026-05-15.md` and never executed. The Format axis
reached 72 through Stream-B and is not touched here.

Three of the 44 are authored as exemplars in the companion pull request: the `elder`
voice, the `grateful` tone, and the `first-principles-derivation` style. The remaining 41
are proposed and not started.

Fifteen further candidates were considered and **rejected as too close to an existing
entry to pass a distinguishability gate**. They are listed in section 6.1 with the entry
each one collides with. The count was not padded to 15 per axis by admitting them.

## 1. Why the catalog is lopsided, and what the rebalance must protect

The catalog holds 72 Format entries against 16 Voice, 15 Tone, and 15 Style. That
imbalance has one cause. A breadth program called Stream-B generated 57 Format candidates
across 10 gated batches during 2026, and no equivalent program was ever run for the other
three axes. The Format axis grew by its program; the other three stayed at their Phase 1
baseline.

The catalog's whole value rests on a single empirical result. A blind judge attributed 8
of 8 confusable composition pairs correctly, against a chance baseline near 0.4 percent.
That result is what licenses the claim that an entry's `llm_instruction_phrasing` genuinely
steers model output. Breadth must never dilute it. An entry earns its place only by
producing output measurably distinguishable from its nearest neighbor, and ADR 0010
section 7 states the consequence plainly: two candidates that cannot produce blindly
distinguishable output are not two entries, they are one entry plus a `confusable_with`
note.

Every candidate below therefore carries the existing entry it will be gated against. That
neighbor is the gate's render partner, not a decoration.

## 2. The constraints this slate respects

### 2.1 No family may reach 12 members

ADR 0010 section 3 makes `subfamily` required for **every** entry in a family once that
family reaches 12 members. `tools/validate.py:check_taxonomy_membership` enforces the
threshold as a literal 12 and counts every entry in the family, drafts included. Crossing
12 therefore forces a subfamily naming pass plus a backfill of every existing member in
that family, which is a migration this slate is not authorized to trigger.

The slate holds every Voice family at or below 8. The post-slate counts are below.

| Voice family | Now | New | After |
|---|---|---|---|
| `expert` | 6 | 2 | 8 |
| `care` | 4 | 3 | 7 |
| `principal` | 3 | 3 | 6 |
| `witness` | 3 | 3 | 6 |
| `dissident` | 0 | 3 | 3 |
| **total** | **16** | **14** | **30** |

The `dissident` family is empty today. ADR 0010 section 2 names it as one of the five
voice families, so an empty family is a real coverage hole, and the slate fills it with
three entries rather than leaving it at zero.

### 2.2 Tone and Style carry no `family` field, and this slate adds none

ADR 0010 section 2 is explicit: tones and styles receive neither `domain` nor `family`,
because register and rhetorical pattern travel across spheres by nature. The schemas
match. `schemas/tone.schema.json` and `schemas/style.schema.json` declare no `family`
property, and `schemas/entry.universal.schema.json` sets `additionalProperties: false`, so
writing one would fail validation.

The task that produced this slate asked for an ADR 0010 family per candidate. For Voice
that is the real `family` field. For Tone and Style **there is no such field, and
inventing one would be a schema change requiring a version bump and a new ADR**. This
slate does not propose one. Instead each Tone and Style candidate is placed in a
**planning cluster**, which is a grouping used for review and for the de-dup audit only
and is written to no file.

The clusters are not invented. They reuse the keys the catalog already carries:
`spectrum` on tones and `frame` on styles. `tools/adherence_gate.py` already treats the
two flat axes this way, rendering a candidate against the whole axis rather than against
a family, so the cluster is a reading aid for the maintainer and a `GROUPS` key for
`tools/agentic/dedup.js`. It is never a validated field.

### 2.3 The out-of-scope list stands

ADR 0010 section 8 holds fiction, poetry, translation, and children's writing out firmly,
and admits journalism and plain-language legal or medical writing only at the register
boundary and only on a maintainer ADR. The frozen inventory adds working journalism,
government and policy writing, legal briefs, clinical notes, scientific papers, and
academic monographs.

Nine inventory voices were rejected on scope rather than on closeness. They are recorded
in section 6.2 so the ruling is legible and does not have to be made again.

### 2.4 One further filter: every entry must render on all 12 anchor topics

Gate 2, in `tools/validate.py:check_sample_count`, requires an entry at
`machine-verified` or above to render on all 12 anchor topics. Four of those topics are
ceremonial or contemplative: `thanking-a-mentor`, `retirement-send-off`,
`daily-rest-practice`, and `a-hard-year-in-review`. A candidate that can only be written
in a professional register will eventually fail Gate 2, or will pass it with four forced
and worthless samples.

This filter is why the `satirist` voice is held in reserve rather than slated. It is also
the main reason the three exemplars were chosen as they were.

## 3. The Voice slate: 14 candidates

All 14 are drawn from the frozen aspirational inventory. The neighbor column is the
existing entry the candidate will declare in `confusable_with` and be gated against.

### 3.1 `expert` family, 2 new, reaching 8

| Candidate | Rationale | Neighbor | Risk |
|---|---|---|---|
| `ethicist` | Reasons from a stated principle to an obligation, where the rest of the family reasons from evidence or experience to a recommendation. The catalog has no voice that can say an option is available and still wrong. | `senior-consultant` | low |
| `artisan` | Judges work by the standard of the craft rather than by its outcome, and treats quality as its own justification. Fills the making-practice register that `pragmatic-architect` leaves empty, because that voice reasons in bets and tradeoffs. | `pragmatic-architect` | low |

### 3.2 `care` family, 3 new, reaching 7

| Candidate | Rationale | Neighbor | Risk |
|---|---|---|---|
| `elder` | Speaks from having outlived the situation, so its authority is elapsed time rather than expertise, and it is comfortable offering no advice at all. **Authored as the Voice exemplar.** | `friendly-mentor` | low |
| `advocate` | Addresses the party holding power on behalf of someone else, where every other `care` voice addresses the person being cared for. The change of addressee changes every sentence. | `caregiver` | low |
| `chaplain` | Stays present with suffering without claiming shared belief, which is the institutional register `pastoral` cannot occupy, because that voice preaches from scripture to a congregation. Populates the one named voice subfamily, `care` to `pastoral`. | `pastoral` | medium |

### 3.3 `principal` family, 3 new, reaching 6

| Candidate | Rationale | Neighbor | Risk |
|---|---|---|---|
| `spokesperson` | Speaks for an institution under the constraint that the writer's own view is off the table, which no existing voice carries. The `executive` holds a position and may say so. | `executive` | low |
| `founder` | Draws authority from having originated the thing and is personally identified with it, where the `executive` draws authority from a role and can be replaced in it. | `executive` | medium |
| `defender` | Accepts fault in the first person and in public. It is the accountability register the catalog has formats for, such as `apology` and `public-statement`, and no voice for. | `spokesperson` | medium |

### 3.4 `witness` family, 3 new, reaching 6

| Candidate | Rationale | Neighbor | Risk |
|---|---|---|---|
| `historian` | Writes about what has settled, with hindsight as the instrument, where the `journalist` writes about what is still moving and must attribute every claim. | `journalist` | low |
| `naturalist` | Records close observation with no narrative arc, so attention itself is the content. The `storyteller` needs a scene that turns. One of the few voices that reads naturally on the contemplative topics. | `storyteller` | low |
| `profiler` | Renders one person through the accounts of others, which is a different instrument from the `storyteller`, whose subject is an event. Strong on `retirement-send-off` and `thanking-a-mentor`. | `storyteller` | medium |

### 3.5 `dissident` family, 3 new, reaching 3

This family is empty, so none of the three has a same-family neighbor. Each is gated
against a cross-family voice instead, and the real distinguishability risk is **collision
among themselves**. The de-dup audit must read the three together as one cluster, which is
exactly the cross-batch collision `tools/agentic/dedup.js` exists to catch.

| Candidate | Rationale | Neighbor | Risk |
|---|---|---|---|
| `whistleblower` | Has standing from having been inside, and accepts a personal cost by writing. No other voice carries risk to the writer as a structural feature. | `journalist` | low |
| `contrarian` | Takes the unpopular side because the consensus is unexamined, and argues against a position rather than for one. The `columnist` holds a recurring stance that may well be the majority view. | `columnist` | medium |
| `polemicist` | Prosecutes one target at sustained length, where the `contrarian` takes the opposite side of whatever is in front of it. This is the weakest distinction in the Voice slate. | `contrarian` | **high** |

The `polemicist` and `contrarian` pair is the one Voice admission this document is not
confident in. If the gate cannot separate them, keep `polemicist`, which has the sharper
definition, and drop `contrarian` back to a `confusable_with` note. That leaves Voice at
29, and the maintainer can promote a reserve candidate from section 6.3.

## 4. The Tone slate: 15 candidates

The frozen aspirational inventory covers Format and Voice only. It has **no Tone or Style
section**, so the only prior source is the 15-item sketch in Phase 3 of
`phase-2-catalog-expansion_2026-05-15.md`, and that sketch is stale. One of its 15,
`reverent`, has since been built. Ten of its 15 survive vetting here. The remaining five
slots are filled from registers the catalog demonstrably lacks, each named below with the
gap it closes.

The cluster column is the planning cluster described in section 2.2. It reuses existing
`spectrum` values where one fits, and is written to no file.

| Candidate | Cluster | Rationale | Neighbor | Risk |
|---|---|---|---|---|
| `grateful` | warmth | Credits the person who made a thing possible, where `celebratory` marks the thing itself. **Authored as the Tone exemplar.** | `celebratory` | low |
| `weary` | depletion | Honest fatigue stated without complaint. The catalog can be `candid` about a problem, but has no register for the cost of carrying it. | `candid` | low |
| `exasperated` | depletion | Irritation at a problem that should have been fixed already. It differs from `weary` in energy: exasperated still pushes, weary has stopped. | `candid` | medium |
| `defiant` | commitment | Positioned against someone who wants otherwise, where `resolute` has merely stopped deliberating and faces no opposition. | `resolute` | low |
| `vigilant` | urgency | Sustained attention with no crisis present, which is the on-call and monitoring register. `urgent` cannot be sustained, because it spends the reader's attention at once. | `urgent` | low |
| `cautious` | certainty | Commits to a course and hedges the downside, where `skeptical` declines to commit until the evidence arrives. | `skeptical` | medium |
| `restrained` | neutral-expressive | Deliberate under-expression where more was available, so the omission carries the weight. `matter-of-fact` is not holding anything back. | `matter-of-fact` | low |
| `contemplative` | solemnity | Turns something over slowly without resolving it, where `reverent` stands before something already settled as weighty. | `reverent` | medium |
| `apologetic` | self-disclosure | Addresses the person harmed and names what is owed. `confessional` admits something about the writer, to anyone. This closes the gap under the existing `apology` format. | `confessional` | low |
| `ceremonial` | solemnity | Heightened form appropriate to a gathered occasion. The catalog has an entire ceremonial format domain, including `toast`, `eulogy`, `blessing`, and `wedding-vows`, and no tone for public occasion. | `reverent` | medium |
| `curious` | certainty | Open inquiry with no doubt attached, where `skeptical` doubts and `instructional` already knows. Pairs with `socratic-inquiry`. | `skeptical` | low |
| `stern` | transparency | Names a standard that was not met and expects correction. `candid` names a hard truth and asks nothing. This closes the gap under `performance-review`. | `candid` | low |
| `hopeful` | motivation | Addresses what a situation could still become, where `encouraging` addresses what the reader is capable of. Hopeful works where nothing is in the reader's control. | `encouraging` | medium |
| `wistful` | warmth | Longing toward something now past, which neither `grateful` nor `contemplative` carries. Strong on `retirement-send-off` and `a-hard-year-in-review`. | `grateful` | medium |
| `bemused` | levity | The writer's own amused puzzlement at something unresolved, where `playful` is an invitation extended to the reader. This is the thinnest distinction in the Tone slate. | `playful` | **high** |

Four Tone candidates from the Phase 2 sketch were rejected outright. They are
`deferential`, `sober`, `tender`, and `exuberant`, with reasons in section 6.1.

## 5. The Style slate: 15 candidates

Phase 3 of the frozen Phase 2 document sketched 15 styles. That sketch has aged worse than
the Tone one. One already exists as a Style, `comparison-contrast`. Two would collide with
existing **Format** ids, `manifesto` and `postmortem`, and entry ids are global across all
four axes, because `tools/validate.py:check_frontmatter_parseable` builds one flat
`id_map` keyed by id alone. Four more duplicate an existing Style or Format closely enough
to reject. Seven survive. Eight slots are filled with cognitive and rhetorical patterns the
catalog lacks, each named with the move that makes it distinct.

The cluster column reuses the existing `frame` values.

| Candidate | Cluster | Rationale | Neighbor | Risk |
|---|---|---|---|---|
| `first-principles-derivation` | argumentative | Starts from premises nobody disputes and builds up, refusing to borrow a conclusion from authority or precedent. **Authored as the Style exemplar.** | `classical-argument` | low |
| `taxonomy` | expository | Partitions a space into exhaustive and mutually exclusive categories, then defends the cut itself. `definitional` defines one thing, and `comparison-contrast` holds two side by side. | `definitional` | low |
| `debunking` | argumentative | States the claim it intends to dismantle fairly and at full strength, then removes its support. `dialectic` seeks a synthesis that honors both sides. | `dialectic` | low |
| `inversion` | argumentative | Asks what would have to be true for the opposite, or how one would guarantee failure, and reasons from the answer. This is a distinct cognitive move, not a distinct subject. | `dialectic` | low |
| `analogy-driven` | expository-conceptual | Carries the whole explanation on one sustained analogy, and names where that analogy breaks. `diataxis-explanation` builds a direct conceptual model instead. | `diataxis-explanation` | low |
| `cause-effect` | expository | Traces a mechanism from cause to consequence and stops there. `problem-solution` must prescribe a remedy, and this style is under no obligation to. | `problem-solution` | low |
| `prediction-and-rationale` | argumentative | Commits to a falsifiable claim about the future and states what would disconfirm it. No existing Style puts its own falsifier on the page. | `classical-argument` | low |
| `hypothesis-and-test` | expository-analytical | Reports a hypothesis, the test run against it, and the result, including a result that went the other way. It is backward-looking where `prediction-and-rationale` is forward-looking. | `prediction-and-rationale` | medium |
| `constraint-first` | expository | States the binding constraints before any option, so the constraints do the deciding and options are filtered rather than argued. `decision-log` records how a choice was reached, criteria included. | `decision-log` | medium |
| `inductive-build` | argumentative | Builds from particulars and withholds the claim until the end, which is the exact inverse of `executive-summary` and its claim-first contract. | `executive-summary` | low |
| `quantitative-narrative` | expository-analytical | Builds the argument out of a few numbers, each carrying its source and its uncertainty, with the prose in service of the figures. | `executive-summary` | medium |
| `objection-handling` | argumentative | Organized by the reader's anticipated resistance, conceding before answering. `question-and-answer` is organized by curiosity and concedes nothing. | `question-and-answer` | medium |
| `parable` | reflective-personal | A short illustrative story whose lesson is deliberately withheld for the reader to supply. `narrative-case-study` tells a real story and states the principle. | `narrative-case-study` | medium |
| `premortem` | expository-analytical | Assumes the failure has already happened and reasons backward to its causes. The prospective-hindsight framing is what distinguishes it from the `postmortem` format, which reports a failure that did occur. | `decision-log` | medium |
| `aphoristic` | expository | A sequence of compressed, freestanding propositions, each complete on its own, with no connective argument between them. | `layered-disclosure` | **high** |

`parable` carries one scope caution. ADR 0010 section 8 holds fiction out firmly. A parable
is admissible here only as a teaching device inside in-scope writing, such as the existing
`sermon` and `devotional-entry` formats. If its renders start reading as short fiction, it
should be withdrawn rather than defended.

`aphoristic` is the weakest Style admission. Its risk is not a neighbor collision but a
category one: a sequence of standalone propositions may be a format, or a `modality:`
facet, rather than a rhetorical pattern. Gate it last, and withdraw it rather than argue
for it.

## 6. What was rejected, and why

### 6.1 Rejected as too close to an existing entry

These 15 candidates are **not slated**. Each is listed with the entry it collides with.
The count per axis was left short rather than filled with these.

| Candidate | Axis | Collides with | Why it fails a distinguishability gate |
|---|---|---|---|
| `primer-author` | voice | `friendly-mentor` and `technical-writer` | It sits between two existing voices and takes its whole definition from both. Friendly-mentor already assumes a capable but new reader, and technical-writer already optimizes for task completion. |
| `strategist` | voice | `senior-consultant` | Senior-consultant already diagnoses against a named framework before recommending action, which is what a strategist does. The difference is time horizon, and a time horizon is a subject, not a register. |
| `skeptic` | voice | the `skeptical` **tone** | This is a cross-axis collision. ADR 0010's test for a dimension is that it changes `llm_instruction_phrasing` independently. A skeptic voice and a skeptical tone would not. It is the clearest reject in the set. |
| `iconoclast` | voice | `contrarian`, itself a slate candidate | Breaking a cherished assumption is what the contrarian move already does. Admitting both would mint a near-synonym inside an otherwise empty family. |
| `gadfly` | voice | `contrarian` | Persistence is a frequency, not a register. |
| `prophet-of-doom` | voice | `polemicist` and the `defiant` tone | The warning is carried by tone, and the sustained prosecution is carried by `polemicist`. Nothing is left over. |
| `dissenting-opinion` | voice | `defender`, plus the out-of-scope legal boundary | Formal disagreement from within is close to `defender`, and the formal-opinion genre is legal writing. |
| `deferential` | tone | `diplomatic` | Diplomatic's own one-liner claims the power-differential register explicitly. Deferential yields the position rather than protecting face, which is too thin a difference to render. |
| `sober` | tone | `matter-of-fact` and `reverent` | It reads as matter-of-fact with weight added, and the weight is what `reverent` already supplies. |
| `tender` | tone | `warm` and `empathetic` | Both existing tones cover care toward a fragile reader. Tender is the overlap of the two, not a third thing. |
| `exuberant` | tone | `celebratory` | Celebratory already owns the high-energy register and anchors it to a specific achievement. Exuberant is the same affect with the anchor removed, which is likely to render identically. |
| `anecdote-then-principle` | style | `narrative-case-study` | The existing entry is defined as a story used to make a general principle concrete. The candidate is a restatement of it. |
| `retrospective-analysis` | style | `decision-log`, plus the `postmortem` and `retrospective` formats | It collides on two axes at once. |
| `position-paper` | style | `classical-argument`, plus the `whitepaper` and `op-ed` formats | The argument pattern is `classical-argument` and the artifact is a Format. Nothing is left over. |
| `primer` | style | `diataxis-explanation` and `definitional` | Beginner orientation is a reader contract already carried by both. |

Two further Phase 2 Style candidates, `manifesto` and `postmortem`, are rejected on a
harder ground than closeness. Entry ids are global, so either id would collide outright
with an existing Format entry and leave `validate.py` resolving one id to two entries.

One Style candidate, `dialogue`, is rejected on ADR grounds rather than on closeness. ADR
0010 section 1 demotes output modality to a `modality:` facet tag riding on Style, and
`modality: dialogue` is already in the governed enum. Minting it as an entry would
re-litigate a ratified decision.

### 6.2 Rejected on scope

ADR 0010 section 8 and the frozen inventory's scope rules exclude these. Each needs a
maintainer ADR to reopen, not a slate decision.

| Candidate | Axis | Scope ruling |
|---|---|---|
| `clinician` | voice | Medical writing. Out per the inventory's exclusion of clinical notes, and out per ADR 0010 except at the plain-language register boundary, which a whole voice is not. |
| `healer` | voice | The same medical boundary, and vaguer. |
| `scholar` | voice | Academic monographs and scientific papers are out per the inventory. It is also close to `researcher`. |
| `judge` | voice | Legal writing. Rendering decisions in a formal opinion is the excluded genre. |
| `arbitrator` | voice | Dispute resolution reads as legal-adjacent. A workplace-mediation register may be admissible later, but it needs the ADR first. |
| `travel-writer` | voice | This names a subject, not a register. The inventory scopes in long-form creative non-fiction, which `storyteller` and the proposed `naturalist` already carry. |
| `food-writer` | voice | The same reason as `travel-writer`. |
| `cultural-critic` | voice | This is `columnist` plus a beat, and a beat is a subject. |
| `tech-critic` | voice | The same reason as `cultural-critic`. |

### 6.3 Held in reserve

These are defensible, and were cut only because the slate is capped at 30 per axis. Promote
one from here if a slated candidate fails its gate.

| Candidate | Axis | Why it is held |
|---|---|---|
| `analyst` | voice | Genuinely distinct from `researcher`, whose loyalty is to the method, where the analyst's is to the read. Held because the `expert` family is already the largest. |
| `curator` | voice | Selection and juxtaposition as the writer's instrument. Held for family balance. |
| `peer-supporter` | voice | First-person parity, and a refusal to advise from above. Held because `care` would otherwise reach 8. |
| `satirist` | voice | Argues by exaggeration rather than assertion. Held on the Gate 2 filter in section 2.4, because satire on `retirement-send-off` or `thanking-a-mentor` is tonally hazardous and Gate 2 forces all 12. |
| `ethnographer` | voice | Participant observation. Held as close to `naturalist` plus `researcher`. |
| `field-notes` | style | Present-tense observation without interpretation. Held because it overlaps the `journal-entry` format. |
| `principle-then-exception` | style | A rule followed by the exceptions that bound it. Held as close to `definitional`, which already covers edge cases. |
| `before-after-bridge` | style | Held as close to `problem-solution`. |

## 7. The three exemplars, and why these three

The companion pull request authors one entry per axis at the full ADR 0009 bar, each
rendered on all 12 anchor topics. The selection criterion was the same for all three: the
clearest case on its axis, measured by whether the distinction from the neighbor can be
stated in one sentence, and whether the entry reads naturally on the ceremonial and
contemplative topics that Gate 2 forces.

| Exemplar | Axis | Neighbor | The distinction in one sentence |
|---|---|---|---|
| `elder` | voice, `care` family | `friendly-mentor` | The elder's authority is elapsed time rather than expertise, so it can decline to advise, which a mentor cannot. |
| `grateful` | tone | `celebratory` | Celebratory marks the achievement, and grateful credits the person who made it possible. |
| `first-principles-derivation` | style | `classical-argument` | Classical argument may cite an authority as a warrant, and this style may not, because every step must be built from premises the reader already grants. |

Each starts at `review_status: draft`. Promotion to `machine-verified` happens only through
`python tools/promote.py`, which refuses to flip an entry that is not rendered on all 12
topics. Promotion to `stable` is the maintainer's decision alone, made after reading the
entry, per ADR 0021.

## 8. How the remaining 41 get built

The harnesses in `tools/agentic/` are axis-parameterized as of the companion pull request,
so loop A in `tools/agentic/README.md` runs unchanged for Voice, Tone, and Style. The
sequence per batch is the Stream-B sequence.

1. Set `AXIS` and `CANDIDATES` in `tools/agentic/generate.js`. Pre-validate every
   cross-reference id against the live catalog, because the deterministic gate rejects a
   dangling reference.
2. Run the generate harness, then `python tools/validate.py` and
   `python tools/build-indexes.py`.
3. Dispatch the distinguishability gate from section 4a of the generation spec, reworded
   off Format. The two recurring catch types are neighbor mischaracterization and a
   `pairs_well_with` id the entry's own anti-pattern forbids.
4. Add the reciprocal `confusable_with` edge on every neighbor, because the symmetry is
   enforced by `tests/test_review_packet.py`.
5. Run `tools/agentic/dedup.js` over the cluster, not over the single declared neighbor.
   For `dissident` and for the two flat axes this is the step that matters most, because
   the per-entry gate never compares two new entries to each other.
6. Render on all 12 topics with `tools/agentic/promote.js`, then promote with
   `python tools/promote.py`.

Batch size should stay at five or six candidates. Stream-B's gated batches ran at that
size, and the constraint on this program is maintainer review capacity, not generation
capacity.

The recommended batch order puts the highest confidence first.

1. **Style, the six remaining low-risk entries.** `first-principles-derivation` is already
   authored, so the batch is `taxonomy`, `debunking`, `inversion`, `analogy-driven`,
   `cause-effect`, and `prediction-and-rationale`. All six are low-risk, and all six
   render across the topic span.
2. **Voice, the six remaining low-risk entries.** `elder` is already authored, so the batch
   is `ethicist`, `artisan`, `advocate`, `spokesperson`, `historian`, and `naturalist`.
3. **Tone, the seven remaining low-risk entries.** `grateful` is already authored, so the
   batch is `weary`, `defiant`, `vigilant`, `restrained`, `apologetic`, `curious`, and
   `stern`.
4. **The `dissident` three as one batch**, gated against each other before anything else.
5. **The medium-risk remainder**, in axis batches.
6. **The three high-risk entries last**: `polemicist`, `bemused`, and `aphoristic`. Each
   should be withdrawn rather than defended if its gate fails.

## 9. What this slate does not decide

- **No schema change is proposed.** Section 2.2 is the one place the slate could have
  needed one, and it does not.
- **No promotion is proposed.** All 44 are draft work. The Gate 1 blind attribution for
  the three exemplars was not run as part of this slate, so the empirical distinguishability
  claim for them is argued but unverified.
- **No counter updates are proposed.** `README.md`, `library.json`, and
  `.claude-plugin/plugin.json` carry curated counts that move only on promotion, and the
  exemplars stay at `draft`.
- **The reserve list is not ranked.** If a gate fails, which reserve candidate replaces the
  failed one is a maintainer call.

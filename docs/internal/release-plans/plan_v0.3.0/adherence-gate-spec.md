---
title: "E1: The Adherence Gate (automated distinguishability + quality harness)"
status: design spec (draft for maintainer review)
date: 2026-06-03
type: design-spec
supersedes: docs/internal/_working/0010-domain-and-family-organization.md (the stale v1 draft ADR, on its overlapping scope only)
related:
  - docs/internal/scaling-the-library-100x.md
  - docs/internal/backlog.md
  - docs/internal/_working/domain-and-family-taxonomy_2026-05-15.md
  - docs/internal/_working/catalog-inventory-aspirational_2026-05-16.md
  - _LOCAL/audit/2026-05-31_adherence-smoke-test.md
  - schemas/entry.universal.schema.json
  - skills/writing-instruction-builder/scripts/build-instruction.py
---

# E1: The Adherence Gate (automated distinguishability + quality harness)

## Purpose, and why it is the unlock

The catalog's whole value rests on one empirical fact, not on its entry count: on 2026-05-31 a blind judge attributed 8 of 8 within-axis confusable pairs correctly, against a chance baseline near 0.4 percent (`_LOCAL/audit/2026-05-31_adherence-smoke-test.md`). That result is the asset. The aspirational ~10x expansion - toward roughly 600 entries and tens of thousands of worked samples drawn from the ~195-format / ~68-voice inventory - is only legitimate if the 1,441st entry is as provably distinguishable as the first 60. Scale that dilutes distinguishability does not grow the moat; it destroys it. A catalog where a third of entries produce indistinguishable mush is worth strictly less than the 60 we already trust.

The unlock is to stop trusting that new entries steer a model and start *refusing* the ones that cannot prove it. E1 turns the one-off smoke-test audit into a standing, automated gate that admits or rejects every candidate entry and sample at volume. This is the load-bearing machinery the entire expansion depends on. It is simultaneously four things:

- **The admission test.** No entry reaches `reviewed` or `stable` without passing.
- **The regression test.** A frozen golden set re-runs every CI; a sharpening edit that accidentally blurs a previously crisp pair fails the build.
- **The de-duplication test.** Two entries that cannot produce distinguishable output are not two entries; they are one entry plus a `confusable_with` note. The gate refuses to mint near-synonyms to hit a vanity count.
- **The public moat.** Each passing entry carries a recomputed per-entry `distinguishability` score written to frontmatter - a proof of quality no competitor catalog can fake, because faking it requires actually producing steerable instructions.

The discipline this spec encodes: scale only behind a gate that refuses what it cannot tell apart, and treat a falling pass-rate as a stop signal rather than a knob to loosen.

## What it measures: three pass/fail gates

"Best-in-class" is lethal as a vibe and unusable as an aspiration. E1 defines it as three measurements a candidate must clear before it ships. All three must pass.

### Gate 1 - Blind same-neighbor distinguishability

Render the candidate and its 2-3 nearest same-family / same-subfamily neighbors on a fixed anchor topic that is native to the entry's domain. A blind judge receives the unlabeled renders, the axis under test, and the candidate descriptions, then (a) rates how distinguishable they are and (b) attributes each render to an entry as a forced choice. This is the smoke-test method generalized: hold three axes and the topic constant, vary one axis, judge blind with presentation order alternated.

Pass condition, both required:

- **Forced-choice attribution correct** against the hidden mapping.
- **Distinguishability band `subtle` or better.** `identical` is an automatic fail. The smoke test produced exactly two `subtle` results (`pragmatic-architect` vs `senior-consultant`; `narrative-case-study` vs `chronological-narrative`) - entries living closest to the failure line. `subtle` passes; it is the floor, and `subtle`-rated passers route to mandatory human review (see Stage 5).

Same-family neighbors are the right adversary because the taxonomy (v2, the canonical proposal) defines tight neighbor sets: an `expert`-family voice is judged against other `expert` voices, never against `pastoral`. Loose categories produce loose gates, which is why the taxonomy tree must be tight before the gate can be sharp.

### Gate 2 - Pedagogical completeness

Schema-checked, deterministic, no judge needed. Every required field is present and substantive: the universal schema's `pairs_well_with`, `avoid_with`, `confusable_with`, `when_to_use`, `when_not_to_use`, `llm_instruction_phrasing` (all already required and ID-validated by `tools/validate.py`), plus the pedagogical fields the draft ADR 0009 bar names - `tells`, `anti_patterns`, `failure_modes`, a `before_after_example` (before, after, commentary), a `mini_glossary` where applicable, and the minimum sample count (12 per entry across the anchor set). This gate is cheap and runs first, because there is no point paying for judge tokens on a candidate that is structurally incomplete.

### Gate 3 - Cross-model adherence

The smoke test's first caveat is the exact gap: "strong model on both ends." It proved a capable model renders the distinctions, not that a mid-tier model does. Gate 3 converts that caveat into a demonstrated property. The instruction must hold its distinction on **at least two model tiers** - a strong generator (Opus-class) AND a mid-tier generator (Sonnet/Haiku-class). An entry that only separates when a frontier model writes it is not a robust instruction; it is a lucky one, and it will fail silently the moment a consumer points a cheaper model at it.

| Gate | What it proves | Mechanism | Cost |
|---|---|---|---|
| 1. Blind distinguishability | Output is perceivably different and correctly attributable vs nearest neighbors | Blind cross-family judge, forced choice + band | Judge tokens |
| 2. Pedagogical completeness | The entry teaches, not just steers | Deterministic schema + field checks in `validate.py` | Compute (negligible) |
| 3. Cross-model adherence | The distinction is robust, not model-luck | Re-run Gate 1 on a second model tier | Generator tokens x2 |

### The restraint check (resolving C1)

> Added 2026-06-17. This closes the quality-measurement sub-problem that decision C1
> (`decisions.md`) left open: the gate scores distinguishability AND quality, but HOW to measure
> "good" was undefined. The design below is parked, not yet calibrated. It is gate-blocking for E1
> (Phase 5 / v0.4.0+), not for v0.3.0, and gets calibrated when the gate it rides is built, not
> before. The decision NOT to build a fuller rubric speculatively is itself part of the design.

**Why a quality check at all.** Gates 1-3 all push toward distinctness, and distinctness has one
perverse failure: a generator optimized to pass blind attribution learns that exaggeration is the
cheapest way to be distinguishable, and produces distinct-but-bad caricature (the first row of the
failure-modes table below). Distinguishability is necessary, not sufficient. So the gate needs a
second measurement that pulls in the opposite direction: not "is it distinct?" but "is it the
genuine register a skilled writer would produce, or a costume?"

**The whole check is one judge question, because the catalog supplies its own answer key.**
Measuring "good" is usually hard because it imports external taste, which is subjective and
gameable. This catalog sidesteps that. Every entry already carries its own `failure_modes` /
`anti_patterns` / `when_not_to_use` (required and substance-checked by Gate 2 / ADR 0009), and the
prose entries name their caricature explicitly: `confident` says "distinct from arrogance," `warm`
says it "tips into saccharine," `resolute` warns that "performative resoluteness ... reads as
bluster." So restraint is not an outside aesthetic judgment; it is a check against each entry's own
published failure mode. The cross-family judge (already running for Gate 1) answers, per rendered
sample, in the same pass:

> Is this the genuine register, or a caricature of it - judged against this entry's own declared
> failure modes? (pass / weak / fail)

- **pass** admits; **weak** routes to the existing `subtle` / near-collision human spot-audit
  bucket (Stage 5), not a new queue; **fail** rejects.
- It rides the Gate 1 judge call, so it costs rubric tokens, not a second render.

**Why this is non-circular and non-gameable.** Fidelity and distinguishability ask "does it hit
the instruction?"; restraint asks "does it avoid the instruction's own failure mode?" Those point
in opposite directions, so a caricature fails restraint precisely because it over-hits fidelity: a
maximally "confident" render that is all unhedged assertion and no substance is MORE
distinguishable and fails restraint on `confident`'s own "distinct from arrogance" line. And
because the bound is the entry's published failure mode rather than the judge's taste, the
generator cannot move the goalposts by being more stylish.

**Thresholds are calibration outputs, not decisions.** How strict the bar is, and whether "good
enough" means "in the quality class of the frozen 60," are not set by judgment - they are read off
a calibration run. Score the frozen 60 (C3, the trusted uncontaminated reference) first: the anchor
is "as restrained and well-crafted as the 60." A baseline that fails is signal (the bar is
miscalibrated, or that baseline is genuinely weak), never a target to beat. This is the same
discipline the distinguishability gate already uses against the same reference set.

**Deliberately kept to one question.** A richer rubric (separate craft and task-fitness criteria,
or an explicit anti-AI-tell criterion given the house no-dash rule) can be split out of the single
restraint question later, but only if a calibration run shows one question is too coarse. The
default is the single restraint check plus the judge's general prose competence, adding criteria
only when evidence demands them rather than building a multi-part rubric on speculation.

## The harness design

### Pipeline position

E1 is **Stage 3 of the six-stage factory** (scaffold, generate, **adherence gate**, diversity check, spot-review, publish). Stages 1, 2, 4, and 6 already have working precedent in the repo: `diff-pair-generator.py` for scaffolding and generation, `validate.py` for structure, `build-indexes.py` for publishing, and the site route/link guards. Stage 3 is the single new piece of machinery, and the one everything downstream depends on. Nothing reaches `reviewed` or `stable` without passing it.

### Inputs

- The **candidate** entry plus its rendered samples.
- The **neighbor set**, looked up mechanically from the taxonomy tree: the candidate's same-family (and, past 12 family members, same-subfamily) siblings. The taxonomy is what makes neighbor selection deterministic; this is why the three-level tree and governed facet enum must land (as the new ADR 0010, superseding the stale v1 draft of that number) before mass generation.
- The **home anchor topic** for the entry's domain, drawn from the locked ~12-topic set (~4 professional, 2 public, 2 relational, 2 ceremonial, 2 contemplative), so every family is rendered on native substrate rather than tested off its home turf.

### The judge

The judge **must be a different model family from the generator.** An Opus-class judge scoring Opus-class output is precisely the monoculture the smoke test flagged, and the slow path by which the gate lies to itself (the model collapse failure mode). Cross-family judging is the cheapest defense against a gate that drifts toward rewarding its own generator's habits.

The judge's clean passes are not taken on faith. A **15 percent human spot-audit of clean passers is mandatory before any distillation** (force-multiplier (f) in the scaling strategy) is turned on. Distillation trains a generator on gate-passing output; if the gate has a blind spot, distillation amplifies it into the generator and the judge simultaneously, and the metric still says "pass." The spot-audit is the human check that keeps the gate honest enough to trust as a training signal.

### The frozen golden set

A held-out reference the generator and judge **never** see as training data or few-shot exemplars: the reviewed baseline 60 (the v0.1.0 seed catalog; LLM-generated and maintainer-curated, not human-authored) plus the 8 smoke-test pairs (including the two known-`subtle` pairs), frozen with their recorded ratings. It runs every CI as regression. The catalog's content is its product, and product regresses: someone sharpens `senior-consultant`'s `confusable_with` block to fix one `subtle` pair and accidentally blurs it against `executive`. If a frozen pair drops below its recorded band, the build fails. This is what makes the 8/8 result a continuously enforced invariant rather than a historical fact. Without an uncontaminated reference, model collapse is invisible: there is nothing clean left to measure drift against.

### The output

For each candidate: **ADMIT or REJECT, plus the judge rationale**, and on admit, a **recomputed per-entry `distinguishability` score written to frontmatter** (band plus the attribution result and the model tiers it held on). The score is both the internal trust signal that drives the `review_status` tier and the public proof that is the moat. It is recomputed, never hand-set, so it cannot be gamed by editing a YAML field.

## Thresholds (concrete, pilot-tunable)

Pick numbers so the gate is executable on the first batch, then tune. A falling pass-rate is a signal, not a license to loosen.

| Threshold | Pilot value | Meaning | If breached |
|---|---|---|---|
| Distinguishability band | forced-choice correct AND `subtle`-or-better | `identical` auto-fails; `subtle` passes but routes to mandatory human review | Reject candidate |
| De-dup cosine | ~0.92 | Embed `llm_instruction_phrasing` + samples; flag any pair above this as a near-duplicate | Mandatory human collision review (Stage 4/5) |
| First-pass-rate STOP FLOOR | ~70 percent | Fraction of candidates in a territory that clear Gate 1 on first attempt | **STOP**: do not lower the floor |

The stop floor is the load-bearing threshold and the most easily misread. A first-pass rate below ~70 percent in some territory means **the model cannot reliably differentiate that territory** - the family is saturated, the subfamily is too fine, or the candidates are near-synonyms. The correct response is to stop adding entries there, not to relax the gate so the failures pass. Loosening the floor to hit a count is exactly how the catalog fills with distinct-but-mediocre entries, which is the failure the whole gate exists to prevent. The roadmap keeps an explicit license to stop the expansion before its target if distinguishability stops scaling.

The cosine threshold is the de-dup test made numeric. Two entries can each pass Gate 1 against their listed neighbors yet be near-duplicates of *each other* if the taxonomy placed them in different families; the embedding check catches that, and ~0.92 is a standard near-duplicate starting point to tune on the first corpus.

## Implementation

Build on the repo's existing generate-and-guard machinery; do not start fresh.

- **Extend `tools/diff-pair-generator.py`** into the Stage 1-2 scaffolder/generator. It already imports `_extract_frontmatter`, `AXES`, and `REPO_ROOT` from `validate.py` and already renders one-axis-varied comparisons holding topic constant - the exact shape the gate consumes. Generalize it from "two existing slices" to "candidate plus its taxonomy-derived neighbor set, rendered on the home topic across two model tiers."
- **New `tools/adherence-gate.py`.** The Stage 3 harness proper: take a candidate, look up neighbors from `tools/taxonomy.py`, render via the generator, run the cross-family blind judge, score forced-choice + band, run the embedding de-dup, and emit ADMIT/REJECT + rationale + the recomputed `distinguishability` score. It reuses `validate.py`'s frontmatter parser and `AXES` map rather than re-parsing.
- **Extend `tools/build-instruction.py`.** Land S1 (conflict-aware composition) first: today `compose_instruction` (line 180, `"\n\n".join(parts)`) concatenates `llm_instruction_phrasing` blocks and never reads `avoid_with` / `pairs_well_with`, so composing `pragmatic-architect` + `reverent` silently staples together a pairing that is literally in `pragmatic-architect`'s `avoid_with`. The gate renders compositions; if composition is incoherent, the gate measures noise. Conflict-aware composition (and a deterministic `avoid_with` symmetry decision) must precede any combinatorial enumeration the gate scores.
- **Extend `tools/validate.py`** for Gate 2: check presence and substance of `tells`, `anti_patterns`, `failure_modes`, `before_after_example`, `mini_glossary`, and the minimum sample count, deterministically. The relationship-ID existence checks already in `validate.py` stay; Gate 2 adds the pedagogical bar on top.
- **Wire into CI alongside `validate.py`.** `validate.py` (structure) and `adherence-gate.py` (empirical, including the frozen golden-set regression) run together. Structural failures short-circuit before judge tokens are spent.

## Reviewer economics, and where humans are irreplaceable

The gate exists to spend scarce human judgment only where machines cannot substitute. Stages 1-4 and 6 are fully automated; most rejections happen there at zero human cost. Stage 5 is the human cost: review a sampled ~15 percent of clean passers, plus **100 percent of two high-risk buckets** - entries the judge rated `subtle`, and entries the de-dup check flagged as near-collisions. At roughly 20-25 minutes of senior editorial time per reviewed entry, that lands near **250-300 reviewer hours per 1,000 entries** - on the order of 6-8 focused weeks for one editor, against the multiple person-years hand-authoring 1,000 entries at this bar would take.

Humans are irreplaceable for exactly three things, and only these:

- **Margin adjudication.** Deciding whether a `subtle`-but-passing entry is a genuinely distinct writing instruction or a judge artifact. The forced-choice attribution can be right for the wrong reason; a human catches that.
- **Collision resolution.** When two entries trip the cosine threshold, choosing which to keep, merge, or kill. The gate flags the collision; only judgment resolves it.
- **Exemplar curation.** Selecting the `reference-quality` entries that seed generation. A bad exemplar propagates its flaws into every entry generated against it, so this is the highest-leverage human act in the whole pipeline.

Everything else - the bulk of the labor - the gate absorbs. Machines manufacture and measure; humans adjudicate the margin. API tokens are a rounding error; this reviewer budget is the binding constraint, and it does not parallelize cleanly. The honest consequence: fund 2-4 reviewers for the program or consciously cap the expansion below its target. Solo evenings at 10x is just 10x of the distinct-but-mediocre failure.

> **Update (2026-06-09, decision F3 - resourcing posture).** The maintainer chose neither funded reviewers nor a hard cap, but an agentic-first posture: the cross-family gate carries quality automatically, the maintainer provides only a capacity-bounded spot-audit (100 percent of the `subtle` and near-collision buckets, plus a sustainable sample of clean passers), and distillation - with its mandatory 15-percent audit - is deferred until that rigor is worth funding in maintainer time. See `decisions.md` (C2 - judge policy, F3 - resourcing posture). The 250-300 reviewer-hour figure above is the cost of the human-heavy model this decision avoids; it now bounds how much spot-audit is sustainable solo (and therefore the scale target, F1 - breadth vs depth weighting), not a hiring plan.

## Failure modes of the gate itself, and mitigations

The gate is machinery, and machinery can be wrong in ways that are invisible precisely because the metric still reads "pass." Three named failure modes, each a variant of "the signal degraded and nobody noticed."

| Failure mode | How it happens | Mitigation |
|---|---|---|
| **Gate-gaming into caricature** | A generator optimized to pass attribution learns that exaggeration is distinguishable, so it produces distinct-but-bad prose. Distinguishable is necessary, not sufficient. | Gate 1 scores distinguishability; the restraint check (resolving C1, defined above) is the second pass/fail measurement - it asks whether the render is the genuine register or a caricature, judged against the entry's own declared failure modes. The capacity-bounded human spot-audit catches caricature the judge still rewards. |
| **Judge drift / monoculture** | A same-lineage judge slowly co-adapts to the generator and stops noticing collapsing distinctions; with distillation it co-drifts faster. | Cross-family judge by construction. Rotate judge models periodically. The frozen golden set is the external anchor: if the judge has drifted, golden-set pairs regress and the build fails. |
| **Golden-set staleness** | The frozen 60 + 8 pairs stop representing the catalog's hard cases as the inventory grows into new families the golden set never covered; regression passes while new territory rots. | Treat the golden set as versioned, not eternal: add (never silently replace) new frozen pairs per new family as it matures, each promoted by a maintainer ADR, so coverage tracks the territory while the original anchors stay immovable. |

The through-line is the same at every rung of the expansion: machines provide throughput, the gate provides a floor, humans provide the ceiling and periodically re-verify the gate against prose they wrote themselves. The value was never the entry count. It was the proof - and E1 is the machine that keeps the proof true at scale.

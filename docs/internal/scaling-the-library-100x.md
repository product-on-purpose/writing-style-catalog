---
title: Scaling the Writing Style Catalog 100x
status: strategy (draft for maintainer review)
date: 2026-06-02
type: strategy
related:
  - docs/internal/backlog.md
  - docs/internal/_working/catalog-inventory-aspirational_2026-05-16.md
  - docs/internal/_working/domain-and-family-taxonomy_2026-05-15.md
  - docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md
---

# Scaling the Writing Style Catalog 100x

> Long-form strategy for taking the catalog from roughly 60 entries / 195 samples to about
> 100x scale (thousands of entries, tens of thousands of worked samples) while holding a
> best-in-class quality bar as a hard constraint, not an aspiration. Companion to the backlog
> ([`backlog.md`](backlog.md)), which carries the near-term work and the staged Expansion
> Program this document deepens. Produced by a multi-agent deep-dive: six facet specialists
> developed one section each, a synthesis pass wrote the executive frame and decision matrix,
> and the result was assembled and dash-sanitized here. Treat it as a menu and a map, not a
> commitment; the decision matrix in the frame is where the maintainer chooses.

## Executive frame

### The 100x thesis

100x does not mean 6,000 entries. It means roughly 600 best-in-class entries carrying tens of thousands of worked samples (12+ each across ~12 anchor topics), where every single one clears the same empirical bar the catalog's whole value rests on: the 8/8 blind adherence result in `_LOCAL/audit/2026-05-31_adherence-smoke-test.md`, where a blind judge attributed every within-axis confusable pair correctly against a chance baseline near 0.4 percent. That result is the asset, not the entry count. Best-in-class is therefore a hard constraint and not an aspiration, because the failure is asymmetric: a catalog of 3,000 entries where a third produce indistinguishable mush is worth strictly less than the 60 we already trust. Scale that dilutes distinguishability does not grow the moat, it destroys it. The only legitimate version of 100x is one where the 1,441st entry is as provably distinguishable as the first 60.

### The unifying model

All six sections describe one machine: a gated generation factory feeding a taxonomy-structured catalog, measured by an adherence eval that is itself the product. Machines manufacture and measure at volume; humans adjudicate only the margin; and one piece of new machinery - backlog item E1, the automated adherence gate - sits underneath everything as the load-bearing substrate. The factory has six stages with a hard gate at Stage 3 (scaffold, generate, adherence gate, diversity check, spot-review, publish). The gate renders each candidate blind against its same-`family` neighbors on a fixed anchor topic and rejects anything not distinguishable, which is the smoke test promoted from a one-off audit to standing CI. That gate is only sharp if the category tree defines tight neighbor sets, so the four axes (Voice, Tone, Style, Format) freeze and the existing domain/family scheme deepens to three levels with governed facet tags instead of a fifth axis. It only stays honest if a frozen golden set and an independent judge keep it from lying to itself. And the same harness run that admits an entry also produces its public proof: a per-entry, recomputed `distinguishability` score that no competitor catalog can fake. Generation gives throughput, the gate gives a floor, humans give the ceiling, and the eval is simultaneously the admission test, the regression test, the de-duplication test, and the moat.

### How to read this document

- **10 - Scaling approaches: the strategy menu.** The seven production methods (a artisanal through g licensed corpora), each scored first on whether it clears the gate at volume and only then on throughput and cost, resolving to a sequenced blend: humans set the reference, (c) generate-then-curate is the workhorse, (e) combinatorial enumeration feeds it post-S1, and (d)/(f) are force-multipliers gated on a trustworthy judge.
- **20 - The production model and the quality system.** The six-stage factory and the operational definition of best-in-class as three measurable pass/fail gates (blind distinguishability, pedagogical completeness, cross-model adherence) plus a frozen golden set, bound to the existing `review_status` enum, holding reviewer cost near 250-300 hours per 1,000 entries.
- **30 - Categories and taxonomy at 100x.** Why the four axes freeze, why every candidate fifth axis demotes to a facet or subfamily, and how the two-level domain/family scheme becomes a three-level, coverage-instrumented tree with a governed faceted-tag enum and a per-cell coverage ledger.
- **40 - Samples and examples at 100x.** The six-dimension sample matrix sliced to a fixed 12 per entry, selection criteria for the ~12 anchor topics, the three generation-side diversity mechanisms that kill near-duplicates, and novel example types (before/after, failure galleries, anti-examples, multi-model renders).
- **50 - Frontier ideas.** The six moves that convert the 8/8 result into structural advantage - the per-entry distinguishability score, the gate as a one-directional quality ratchet, per-model phrasing variants plus a public leaderboard, confidence-graded composition over MCP, auto-generated diff-pairs, and versioned phrasings tracked against model releases - all sitting on the E1 substrate.
- **60 - Risks, economics, and the roadmap.** The eight failure modes (all variants of "the signal degraded and nobody noticed"), the honest economics (API cost is the cheap part; human review is the binding constraint), and the staged 1x to 3x to 10x to 30x to 100x roadmap with a pass-rate stop floor and an explicit license to stop before 100x.

### Cross-cutting decision matrix

These are the strategic calls the maintainer must make to pursue 100x, deduplicated and sharpened from the open decisions raised across all six sections. Each is a fork the rest of the program keys off.

| # | Decision | Options | Recommendation |
|---|---|---|---|
| 1 | What does the E1 gate score? | (a) distinguishability only; (b) distinguishability plus a taste/quality rubric | **(b).** Distinguishability is necessary, not sufficient - a generator optimized to pass attribution produces distinct-but-bad caricature. Add a second pass/fail quality rubric so prose stays good while becoming distinct. This is what keeps the gate from rewarding exaggeration. |
| 2 | Independent-judge policy | (a) same Opus-class model judges everything; (b) cross-family judge plus human spot-audits before distillation | **(b).** The smoke test's caveat 1 ("strong model on both ends") is the exact gap. Require a judge from a different model family and 15 percent human spot-audit of clean passers, mandatory before turning on distillation (f), or the gate slowly lies to itself (failure mode 4). |
| 3 | Held-out reference set | (a) reuse the 60 freely as few-shot exemplars; (b) freeze the 60 (or a curated subset) as ground truth never used for training/few-shot | **(b).** The whole blend depends on having uncontaminated ground truth to audit against. Formally designate and freeze the reviewed baseline 60 (the v0.1.0 seed catalog; LLM-generated and maintainer-curated, not human-authored) as the reference the generator never sees; model collapse (f) is invisible without it. |
| 4 | Breadth vs depth weighting | (a) grow toward ~600 entries; (b) hold entries lower and let 12+ samples per entry carry the "100x" | **Blend, depth-weighted.** Target ~600 entries (the format surface concentrates breadth; voices/tones saturate faster), but the bulk of "100x" is sample depth - 600 x 12 is already ~120x today's ~195. Let the gate reject near-duplicate entries so breadth never inflates past distinguishability. |
| 5 | Numeric thresholds: gate pass, dedup cosine, first-pass stop floor | (a) leave illustrative; (b) commit numbers: forced-choice correct AND `subtle`-or-better band; cosine ~0.92 dedup; 70 percent first-pass-rate stop floor | **(b), pilot-tuned.** Pick concrete numbers so the gate is executable, then tune on the first batch. A first-pass rate falling below the floor is a stop signal (model can't differentiate that territory), not a knob to loosen. |
| 6 | Scope-out boundaries | (a) hold the full out-of-scope list (fiction/poetry/legal/medical/journalism); (b) admit selectively at the register boundary | **(b), gate-arbitrated.** Admit journalism (news-brief, feature-lead, investigative-nut-graf) and plain-language legal/medical (`plain-english-legal-summary`, `patient-instructions`) only if they clear E1 and teach register not domain knowledge. Hold fiction, poetry, translation, children's writing. Any reopening is a maintainer ADR, never a mechanical add. |
| 7 | Taxonomy depth and ADR sequencing | (a) keep flat axis lists; (b) codify the three-level tree + faceted-tag enum as ADR 0010 before mass-add | **(b).** The gate's neighbor set is defined by the tree, so loose categories produce loose gates. Promote `subfamily` now, make it required past 12 family members, govern the facet enum (`channel:`, `formality:`, `modality:`, `epistemic:`, `length:`, `stance:`, `delivery:`) in `tools/taxonomy.py`, and land ADR 0010 before 3x->10x breadth. |
| 8 | Lock the ~12 anchor topics | (a) keep instinct-picked 3 and improvise; (b) lock 12 with explicit domain assignment before any mass generation | **(b), urgently.** This is the highest-leverage unresolved input; the sample matrix, diff-pairs, and per-entry distinguishability test-bed all key off it. Select by isolation, five-domain spread, and real-worldness (~4 professional / 2 public / 2 personal / 2 ceremonial / 2 contemplative) so every family has a native substrate. |
| 9 | Land S1 and resolve `avoid_with` symmetry before scoring | (a) keep `compose_instruction` concatenating (line 180 `"\n\n".join(parts)`, never reads conflict fields); (b) make composition conflict-aware and decide symmetry | **(b).** Today composing `pragmatic-architect` + `reverent` silently staples together a pairing that is in `avoid_with`. Land S1 before anyone enumerates the combinatorial grid, and resolve `avoid_with` symmetry deterministically so composition-confidence (frontier idea 4) and nearest-neighbor selection are well-defined. |
| 10 | Resourcing commitment | (a) solo evenings; (b) 2-4 people for 18-24 months with a real budget; (c) consciously cap at 10x/30x | **(b) or (c), never (a).** API tokens are a rounding error; human review is the binding constraint and does not parallelize cleanly. Either fund the team or consciously cap the target. Solo evenings at 100x is just 100x of failure mode 8 (distinct-but-mediocre). The roadmap must keep the right to stop at 10x/30x if distinguishability stops scaling. |

The discipline is identical at every rung: scale only behind a gate that refuses what it cannot tell apart, treat a falling pass-rate as a stop signal rather than a tuning problem, and remember the value was never the count - it was the proof.

## Scaling approaches: the strategy menu

The question is not "how do we make more entries." It is "how do we make tens of thousands of best-in-class worked samples without breaking the one empirical result the catalog is built on" - the 8/8 blind adherence test where a judge attributed every confusable pair correctly at a chance baseline of about 0.4 percent (`_LOCAL/audit/2026-05-31_adherence-smoke-test.md`). Best-in-class is a hard constraint here. An entry that does not produce measurably distinguishable output is not a low-quality entry, it is a non-entry: it dilutes the signal that gives every other entry its value. So each approach below is judged on one axis above all others - can it clear the adherence gate at volume - and only then on throughput and cost.

The arithmetic that forces this conversation: 120 entries at 12 samples each is ~1,440 samples; the comprehensive inventory (`_working/catalog-inventory-aspirational_2026-05-16.md`, ~195 formats and ~68 voices) plus proportional tone/style growth lands near 400-500 entries, and at 12+ samples each that is on the order of 5,000-10,000 samples - before we even reach the "thousands of entries" framing. We have ~195 today. Every approach is really a proposal for the ratio of human judgment to machine output per sample.

### (a) Artisanal human authoring

**Mechanism.** A skilled writer hand-crafts each entry (`tells`, `anti_patterns`, `failure_modes`, `llm_instruction_phrasing`, cross-refs) and hand-writes each worked sample. This is how the proven 60 were made.

**Throughput.** Brutally low. The Phase 2 spec budgets a full pedagogical entry as hours of expert work, and a worked sample at the bar is 30-60 minutes once you include the "what to notice" reasoning. Call it 2-4 quality samples per expert-hour. Tens of thousands of samples is tens of thousands of expert-hours - years of one person, or a payroll the project does not have.

**Cost shape.** Linear and steep. No fixed-cost lever; cost scales 1:1 with output forever.

**Quality risk.** Lowest of any approach - this is the bar everything else is measured against. The risk is the opposite one: it never reaches 100x, so the catalog stays small and "best-in-class" is achieved on a footprint too narrow to matter.

**Best-in-class reachable?** Yes, by definition. At 100x scale, no.

### (b) LLM generation behind an automated adherence gate

**Mechanism.** Extend `tools/diff-pair-generator.py` into a full generator (backlog item E1): scaffold an entry from the schema, render its samples across the anchor-topic set using `build-instruction.py`, then run every candidate through an *automated* version of the smoke test - render against nearest neighbors on a fixed topic, have a blind judge attribute them, reject anything not distinguishable. The gate is the quality definition made executable.

**Throughput.** Very high. Generation is compute-bound; a batch of 1,440 samples is a job that runs overnight, not a quarter of writing. The gate is the rate limiter, not the generator.

**Cost shape.** High fixed cost (build the gate harness, the judge rubric, the bar-checking validator) then near-zero marginal cost per sample, plus the unavoidable generate-and-reject waste: if 30 percent of candidates fail the gate, you pay for 1.4x the tokens you keep.

**Quality risk.** Two specific failure modes. First, **gate gaming**: a generator optimized to pass attribution can produce caricature - output so exaggerated it is distinguishable but no longer good writing (distinguishable is necessary, not sufficient). Second, **judge monoculture**: an Opus-class judge scoring Opus-class output is the exact caveat the smoke test flagged (strong model on both ends). A gate is only as honest as its judge.

**Best-in-class reachable?** This is the only approach that *can* reach best-in-class at 100x, but only if the gate measures more than distinguishability. The smoke test proves the gate concept works on the hard within-axis pairs (`pragmatic-architect` vs `senior-consultant` rated "subtle" but still attributed correctly). It does not yet prove a gate keeps prose *good* while making it *distinct*.

### (c) Expert-in-the-loop hybrid: generate then curate

**Mechanism.** (b) produces candidates; the gate filters the clearly-failing ones; a human expert reviews what survives, edits the near-misses, and accepts or rejects on the qualities a judge cannot score (taste, the "rings true" test, whether `tells` are real tells). Generation does the volume; the human does the judgment.

**Throughput.** High and tunable. A reviewer clears candidates far faster than they author from scratch - reviewing a generated sample against its entry is minutes, not an hour. Realistic: 15-40 reviewed samples per expert-hour, an order of magnitude over (a), with the gate having already discarded the obvious failures so the human only sees plausible work.

**Cost shape.** Fixed gate cost plus a *sub-linear* human cost: review time per sample falls as the generator improves (fewer near-misses to fix). This is the cost curve that actually bends.

**Quality risk.** Reviewer fatigue and rubber-stamping at volume - approving "good enough" because the queue is long is exactly how the bar drifts. Mitigated by keeping the human on judgment, not production, and by spot-auditing accepted samples through the same blind gate.

**Best-in-class reachable?** Yes, and most defensibly. It is the only approach that pairs machine volume with the human taste that defined the bar. This is the workhorse.

### (d) Community / contributor sourcing with the gate as the admission test

**Mechanism.** Open contribution, but make the automated adherence gate (E1) the price of admission: a proposed entry is merged only if its rendered output is blindly attributable against its nearest neighbors. The gate converts "do we like this contributor's entry" (subjective, unscalable, contentious) into "does it pass" (objective, automatable). `tools/validate.py` already enforces structural correctness and that every `pairs_well_with`/`avoid_with`/`confusable_with` ID exists; the gate adds the empirical check on top.

**Throughput.** Potentially unbounded and not on the maintainer's payroll - the one approach whose ceiling is community size, not budget. But latency is high and unpredictable; contributors arrive on their own schedule.

**Cost shape.** Low marginal cost to the project, high fixed cost in contributor on-ramp (the E4 meta-layer: governance docs, review rubric, a runnable gate contributors can self-test against before submitting).

**Quality risk.** The gate's blind spot becomes the catalog's blind spot at the worst possible scale, because now adversarial-ish contributors are pushing against it. Also coverage skew: contributors write what they know (more engineering voices, fewer `contemplative`-domain formats), warping the inventory away from the balanced family targets in the domain taxonomy.

**Best-in-class reachable?** Yes *if and only if* the gate is trustworthy, which makes (d) entirely downstream of (b)/(c) succeeding first. This is a force-multiplier, not a foundation.

### (e) Programmatic combinatorial expansion (axis x axis x topic)

**Mechanism.** The catalog is combinatorial by construction: voice x tone x style x format x topic. With even 30 entries per axis and 12 topics, the composition space is 30^4 x 12 ~ 9.7 million instructions. "Generate samples" can mean "enumerate compositions and render each."

**Throughput.** Effectively infinite - this is the only approach that *over*-produces.

**Cost shape.** Pure compute; trivial to generate, expensive to store and curate.

**Quality risk.** This is the trap, and the repo already knows why. Composition today is naive concatenation (`compose_instruction` in `build-instruction.py`, lines ~149-187, joins `llm_instruction_phrasing` blocks with `\n\n` and never reads the conflict fields). So enumerating the grid blindly produces incoherent samples like `pragmatic-architect` + `reverent` - and `reverent` is literally in pragmatic-architect's `avoid_with`. Most of a 9.7M-cell grid is noise: contradictory pairings, genre violations, redundant near-duplicates. Combinatorial expansion without **conflict-aware composition (backlog S1)** is a sample-quality disaster generator.

**Best-in-class reachable?** Only as a *candidate enumerator* feeding (b)/(c), and only after S1 prunes the incoherent cells. On its own, no. It is a firehose, not a faucet.

### (f) Model distillation / self-improving generator

**Mechanism.** Use the proven catalog as training/few-shot signal. Near-term: assemble the best worked samples per entry as few-shot exemplars so the generator in (b) writes in-distribution from the start. Longer-term: fine-tune a specialized "catalog renderer" on the corpus of gate-passing samples, so the generator internalizes what distinguishability looks like.

**Throughput.** Highest sustained rate, because pass-rate climbs - the generator stops producing gate failures, so generate-and-reject waste falls toward zero.

**Cost shape.** Highest fixed cost (corpus assembly, fine-tune, eval) and lowest long-run marginal cost. Pays off only at genuinely large N.

**Quality risk.** **Model collapse / inbreeding** is the named danger: a generator trained on its own gate-passing output drifts toward the catalog's average and loses the edges, and because the judge shares the lineage, the gate stops noticing. Distinctions narrow while the metric still says "pass." This is the most dangerous failure because it is invisible to the very gate meant to catch it.

**Best-in-class reachable?** Risky. Reachable only with an *independent* judge (different model family, periodic human audit) and a held-out reference set (the reviewed baseline 60) the generator never trains on. Treat as an efficiency layer under (c), never as the sole pipeline.

### (g) Licensed / imported corpora

**Mechanism.** Acquire existing high-quality writing (a publisher's archive, a licensed essay corpus) and back-fill samples or mine `tells` from real exemplars rather than generating them.

**Throughput.** Step-function: large drop on acquisition, then nothing until the next deal.

**Cost shape.** Lumpy and legal: licensing fees, rights review, attribution obligations.

**Quality risk.** **Provenance and fit.** Imported prose was not written to instantiate a specific composition on a fixed anchor topic, so it cannot serve as a single-variable worked sample (the whole pedagogical point - hold topic constant, vary one axis). It also cannot pass the adherence gate, which compares *renders of the catalog's own instructions*. Licensed corpora are useful as *reference material for human authors* mining real `tells` and `anti_patterns`, not as samples.

**Best-in-class reachable?** Not for samples. Possibly valuable as ground-truth input to (a)/(c). Out of scope for the core scaling problem; the aspirational inventory also explicitly scopes out fiction, poetry, journalism, and legal/medical/scientific writing, which is where most licensable corpora live.

### Comparison

| Approach | Throughput | Cost shape | Specific quality risk | Best-in-class at 100x? |
|---|---|---|---|---|
| (a) Artisanal | ~2-4 samples/expert-hr | Linear, steep, no lever | None (this is the bar) | Yes on quality, no on scale |
| (b) LLM + gate | Very high (compute-bound) | High fixed, ~0 marginal + reject waste | Gate gaming -> caricature; judge monoculture | Yes, only if gate scores more than distinctness |
| (c) Generate + curate | High, tunable (15-40/hr) | Fixed gate + sub-linear human | Reviewer rubber-stamping at volume | Yes - most defensible |
| (d) Community + gate | Unbounded, high latency | Low marginal, high on-ramp cost | Gate blind spots exploited; coverage skew | Yes, iff gate is trustworthy (downstream of b/c) |
| (e) Combinatorial | Infinite (over-produces) | Pure compute; storage/curation cost | Incoherent cells without S1 conflict-awareness | No alone; candidate enumerator only |
| (f) Distillation | Highest sustained | Highest fixed, lowest marginal | Model collapse invisible to a same-lineage gate | Risky; needs independent judge + human anchor |
| (g) Licensed corpora | Step-function | Lumpy, legal | Provenance; cannot be single-variable samples | No for samples; reference input only |

### The recommended blend, and why no single approach gets there

No single approach reaches 100x-at-best-in-class. (a) hits the bar but not the scale. (b), (e), and (f) hit the scale but each has a quality failure mode that the gate alone cannot catch (caricature, incoherence, collapse). (d) and (g) are real leverage but strictly downstream of a trustworthy gate and a proven generator. The constraint is not appetite, it is the gate's credibility - which is exactly the sequencing the backlog already commits to ("build the machinery on the proven 60 first, then scale breadth and sample-depth behind the gate").

**The blend, sequenced:**

1. **Foundation - (a) sets the reference, then build the gate.** Keep the reviewed baseline 60 as the held-out reference set the generator never trains on. Land S1 (conflict-aware composition) so the composition space is coherent before anyone enumerates it, and stand up the E1 automated gate with that reviewed baseline as ground truth.
2. **Core engine - (c) as the workhorse, (b) underneath.** LLM generation produces candidates; the gate discards obvious failures; experts curate the survivors on taste the judge cannot score. This is the only combination that pairs machine volume with the judgment that defined "best-in-class."
3. **Enumerator - (e) feeds the engine, post-S1.** Use the (now-pruned) combinatorial grid to propose which compositions to render, so coverage is deliberate against the domain/family targets, not skewed by whoever happens to be authoring.
4. **Force-multipliers, once the gate is trusted - (d) and (f).** Open community contribution with the gate as admission, and introduce distillation to cut generate-and-reject waste - both guarded by an *independent* judge (different model family) plus periodic human audit against the held-out reference, the only defense against the gate slowly lying to itself.
5. **(g) as reference input only**, mined by human authors for real `tells`, never used as samples.

The through-line: machines provide throughput, the gate provides a floor, and humans provide the ceiling. Best-in-class survives 100x only if every layer that adds volume sits behind a gate that humans periodically re-verify against prose they wrote themselves.

## The production model and the quality system

The catalog's entire value sits on one empirical fact: composing a voice + tone + style + format produces output a blind reader can tell apart and correctly attribute. The smoke test in `_LOCAL/audit/2026-05-31_adherence-smoke-test.md` measured this directly - 8 of 8 within-axis confusable pairs attributed correctly, blind, against a chance baseline of about 0.4 percent. That result is the asset. Scale that dilutes it does not grow the asset, it destroys it, because a catalog of 3,000 entries where a third produce indistinguishable mush is worth less than 60 entries that all clearly steer a model. So the production model is not "how do we make a lot of entries." It is "how do we make the 1,441st entry as provably distinguishable as the 60 we already trust." Everything below is built backwards from that constraint.

### Best-in-class, operationalized as three measurable gates

"Best-in-class" is unusable as an aspiration and lethal as a vibe. We define it as three pass/fail measurements an entry must clear before it ships. An entry is gold only if all three pass.

1. **Blind distinguishability from nearest neighbors.** The entry, rendered on a fixed anchor topic, must be correctly attributed by a blind Opus-class judge against its 2-3 nearest neighbors - which, post-taxonomy, are its same-`family` siblings (an `expert`-family voice is judged against other `expert` voices, not against `pastoral`). This is the smoke test promoted from a one-off audit to a per-entry CI gate. Pass condition: correct forced-choice attribution AND a distinguishability rating of `subtle` or better (`identical` is an automatic fail). The smoke test already produced exactly two `subtle` results (`pragmatic-architect` vs `senior-consultant`; `narrative-case-study` vs `chronological-narrative`), which is why those are the C1 sharpening targets - they are the entries living closest to the failure line.

2. **Full pedagogical completeness.** Every required field is present and substantive: the universal schema's `pairs_well_with`, `avoid_with`, `confusable_with`, `when_to_use`, `when_not_to_use`, `llm_instruction_phrasing`, plus the Phase 2 pedagogical fields (`tells`, `anti_patterns`, `failure_modes`, `before_after_example`, `mini_glossary`). This is structural, so `tools/validate.py` checks it deterministically - no judge needed.

3. **Cross-model adherence.** Distinguishability must hold on at least two model tiers, not just the Opus-class generator both ends of the smoke test used. The audit's own caveat 1 names this gap directly: it did not prove a Haiku-class model renders the distinctions as crisply. A gold entry passes the blind gate with a strong generator AND a mid-tier generator (Haiku/Sonnet-class). An entry that only works when a frontier model writes it is not a robust instruction, it is a lucky one.

### The pipeline: six stages, one gate

The factory is a linear pipeline where the third stage is a hard gate. Nothing reaches `reviewed` or `gold` without passing it.

| Stage | What runs | Human or machine | Output |
|---|---|---|---|
| 1. Scaffold | Generate entry skeleton from the axis schema + assigned `domain`/`family` | Machine (extend `diff-pair-generator.py` into a scaffolder) | Draft `ENTRY.md`, all required fields stubbed |
| 2. Generate | Render `llm_instruction_phrasing` and N worked samples across the anchor-topic set | Machine | Candidate entry + samples |
| 3. Adherence gate | Blind distinguishability vs same-family neighbors, on 2 model tiers | Machine (the harness) | PASS / FAIL + judge rationale |
| 4. Diversity check | Embed phrasing + samples; flag near-duplicate of an existing entry | Machine | Redundancy score, collision flags |
| 5. Spot-review | Human reads a sampled fraction of passers; reads 100 percent of `subtle`-rated and near-collision entries | Human | Promote / revise / reject |
| 6. Publish | `build-indexes.py`, route/link guards, regenerate `taxonomy.json` and site | Machine | Live entry |

Stage 3 is the load-bearing one. Stages 1, 2, 4, and 6 already have working precedent in the repo (`diff-pair-generator.py`, `validate.py`, `build-indexes.py`, the site route guards). The single new piece of machinery the whole program depends on - backlog item E1 - is turning the audit into the Stage 3 harness.

### Why the gate is what lets breadth scale without dilution

The naive scaling failure - the "120 mixed-quality entries" risk the ROADMAP explicitly guarded against - happens when you add entries and *hope* they steer the model. The gate inverts that. An entry earns its slot only by producing measurably distinguishable output; one that does not is rejected before it pollutes the catalog. This decouples breadth from quality risk. You can attempt the full ~195-format / ~68-voice aspirational inventory precisely because attempting is cheap and only passers survive. The gate also catches the specific scaling pathology this catalog is prone to: at 30+ entries per `family`, new entries crowd their neighbors and distinctions collapse. A flat list hides that; the same-family blind judge surfaces it as a FAIL on exactly the entry that got too close. The gate is not bureaucracy bolted onto generation - it is the thing that makes generation safe to run at volume.

### The diversity check is a distinct failure mode

Stage 4 exists because Stage 3 has a blind spot. Two entries can each be individually distinguishable from their listed neighbors yet be near-duplicates of *each other* if the taxonomy added them in different families. As we push toward 68 voices, the real risk is not incoherence, it is redundancy: a `clinician` voice and a `senior-consultant` voice that converge in practice. We embed each new entry's `llm_instruction_phrasing` and its worked samples, compute cosine similarity against the existing corpus, and flag anything above a threshold for mandatory human review. A redundant entry is a quality failure even when it passes adherence, because it makes the catalog harder to navigate and the `confusable_with` graph noisier.

### Quality tiers, mapped to the existing `review_status`

The schema already has the lifecycle field; we bind it to the gate rather than inventing a parallel scheme. This mirrors the sibling agent-skills-toolkit's Bronze/Silver/Gold but reuses our `review_status` enum so no schema change is needed.

| Tier | `review_status` | Gate requirement | Trust |
|---|---|---|---|
| Draft (Bronze) | `draft` | Schema-valid, scaffolded, samples generated. No adherence proof. | Visible internally; not a published claim |
| Reviewed (Silver) | `reviewed` | Passed Stage 3 adherence on one model tier + Stage 4 diversity | Listed; "distinguishable, single-tier" |
| Gold | `stable` | Passed adherence on **2 tiers** + diversity + human spot-review | The trustworthy public catalog |
| Reference | `reference-quality` | Gold + chosen as a teaching exemplar (canonical for its family) | Used as the template other entries are generated against |

This is exactly why `CLAUDE.md` forbids setting `review_status` to `stable` without review: `stable` is the gold claim, and the gate is what backs the claim. The current 60 entries are the grandfathered gold baseline (they passed the original smoke test on the hardest pairs); every new entry must earn the tier the same way.

### The adherence harness as repeatable eval, plus a golden set

The harness generalizes the smoke test's exact method: hold three axes and the topic constant, generate blind and independently, judge blind with presentation order alternated, score forced-choice attribution against the hidden mapping. The reusable form takes a candidate entry, looks up its same-family neighbors, renders all of them on the entry's home anchor topic, and runs the blind judge.

Beyond the per-entry gate, we keep a **golden set**: the original 8 smoke-test pairs (2 per axis) plus the two known-`subtle` pairs, frozen with their expected ratings. This is regression coverage. The catalog's content is its product, and product can regress - someone sharpens `senior-consultant`'s `confusable_with` block to fix the `subtle` pair and accidentally blurs it against `executive`. The golden set runs in CI on every entry edit. If a frozen pair drops below its recorded distinguishability, the build fails. This is the difference between a one-time audit and a quality *system*: the 8/8 result stops being a historical fact and becomes a continuously enforced invariant.

### Reviewer economics: where humans are irreplaceable

The whole point of the gate is to spend scarce human judgment only where machines cannot substitute. Concretely, per 1,000 new entries:

- **Stages 1-4 and 6 are fully automated.** Scaffolding, generation, the blind adherence gate, the diversity embed, and publishing cost compute, not hours. Most rejections happen here with zero human time.
- **Stage 5 spot-review is the human cost.** We do not review every passer. We review a sampled ~15 percent of clean passers (catching judge-model blind spots and tone-deafness the forced-choice attribution misses) plus 100 percent of two high-risk buckets: entries the judge rated `subtle`, and entries the diversity check flagged as near-collisions. Budget roughly 20-25 minutes of senior editorial time per reviewed entry. With clean-pass sampling plus full review of the risky buckets, that lands near **250-300 reviewer hours per 1,000 entries** - on the order of 6-8 focused weeks for one editor, versus the multiple person-years hand-authoring 1,000 entries at this bar would take.

Humans are irreplaceable for exactly three things, and only these: judging whether a `subtle`-but-passing entry is *genuinely* a distinct writing instruction or a judge artifact; resolving diversity collisions (which of two near-duplicates to keep, merge, or kill); and curating the `reference-quality` exemplars that seed generation, because a bad exemplar propagates its flaws into every entry generated against it. Everything else - the bulk of the labor - the gate absorbs. That asymmetry is the production model: machines manufacture and measure, humans adjudicate the margin. It is what makes "the world's most comprehensive catalog" compatible with "every entry as provably distinguishable as the first 60."

## Categories and taxonomy at 100x

At 60 entries, a flat axis list is scannable and the domain/family taxonomy is a nicety. At 100x - on the order of thousands of entries - taxonomy stops being a navigation convenience and becomes the load-bearing structure that decides whether the catalog is a coherent map of writing or a junk drawer of plausible-sounding labels. The thesis of this section: legibility at scale comes from a fixed, small set of organizing axes plus a deep, governed category tree underneath them, not from inventing new top-level axes. The four axes (Voice, Tone, Style, Format) are correct and should be frozen; everything that tempts us toward a fifth axis is better modeled as a cross-cutting tag or a subfamily. The real work is deepening the existing two-level domain/family scheme into three levels, defining the territory so coverage is measurable, and building anti-rot machinery so the tree stays sharp as it grows.

### The taxonomy must do three jobs at scale

1. **Keep thousands of entries scannable.** A reader doing "Postgres vs DynamoDB" should reach the relevant 5-8 formats in three clicks (domain -> family -> entry), never scroll a list of 800.
2. **Make coverage measurable.** "Most comprehensive catalog" is meaningless unless every cell in the tree has a defined target count and a fill state. The taxonomy is the coverage ledger.
3. **Keep neighbors tight so the quality gate stays sharp.** The 8/8 adherence result rests on near-neighbor confusables (`pragmatic-architect` vs `senior-consultant` inside the `expert` family). The category tree is what defines "nearest neighbors", and the E1 gate renders a candidate against its same-family siblings. Bad categories produce loose gates.

### Do NOT add a fifth top-level axis

ADR 0001 fixes the three-axis model (Voice/Tone are two dimensions of one axis; Style and Format are the other two). Six candidate new axes have been floated. Each is real, but each is better expressed inside the existing structure than as a peer of Voice/Tone/Style/Format. The test: a top-level axis must be (a) orthogonal to the others, (b) something a composer selects exactly one value of per instruction, and (c) something that changes `llm_instruction_phrasing` independently. None of the six pass cleanly.

| Candidate axis | Verdict | Where it actually lives |
|---|---|---|
| Rhetorical Stance (advocate / explain / explore / provoke) | Reject as axis | It is the defining property of Style. `socratic-inquiry`, `dialectic`, `manifesto` already encode stance. Add as a `stance:` tag on styles for filtering. |
| Epistemic Stance (certain / hedged / speculative) | Reject as axis | Splits across Tone (`confident` vs `candid`) and Voice (`skeptic`, `researcher`). Model as a cross-cutting tag `epistemic:hedged|certain|exploratory`, not a selectable axis. |
| Register / Formality | Reject as axis | This is the core of Tone. A formality scale collapses into the tone cluster (`reverent`/`sober` high, `playful`/`candid` low). Add an ordinal `formality: 1-5` tag to tones for sorting, not a new axis. |
| Medium / Channel | Reject as axis | Already baked into Format. `slack-message`, `linkedin-post`, `op-ed` are channel-shaped formats. Channel belongs as Format `family`/`subfamily` plus a `channel:` tag, not a parallel selection. |
| Persona-Archetype | Reject as axis | This IS Voice. Voice families (`expert`, `care`, `witness`, `dissident`, `pastoral`, `principal`) are archetype clusters already. Adding an archetype axis double-counts Voice. |
| Modality (prose / list / dialogue / verse) | Partial - reject as axis, adopt as Style subfamily | Output shape is real but narrow. Add a `modality:` tag and let it ride on Style. Verse stays out of scope (poetry exclusion holds). |

Why this matters beyond tidiness: a fifth axis multiplies the combinatorial space the composer must reason about (Voice x Tone x Style x Format is already a 4-way product, ~thousands of entries makes it astronomical) and forces every Tone and Style entry to declare a value it does not need. The cross-cutting tag pattern gives the same filterability without the cost. Frozen axes, deep tree.

### The structure at 100x: three levels, governed tags, explicit coverage cells

**Level up from two to three.** The current scheme is `domain -> family` for formats and `family` for voices. At thousands of entries, families overflow. The taxonomy doc already anticipates this: it flags `instruction` (19 candidate formats) bifurcating into `reference` vs `tutorial`, and `witness` (18 voices) needing subdivision. Promote the optional `subfamily` field now and make it required once any family passes 12 members (the existing "revisit" trigger). Concretely:

- Formats: `domain (5-7) -> family (~20) -> subfamily (~60) -> entry`. Example: `professional -> instruction -> reference -> api-doc`.
- Voices: `family (6-8) -> subfamily (~18) -> entry`. Example: `witness -> chronicler -> historian`.
- Tones and Styles stay flat with **governed cross-cutting tags** instead of a tree, because they are domain-neutral by nature (a `candid` tone travels from Slack to eulogy). The tag namespace is the structure for these two axes.

**Cross-cutting tags become a controlled vocabulary, not free text.** Today `tags` is an open array. At 100x that rots immediately. Split it: keep free `tags` for search, but add a small set of governed faceted tags validated against an enum in `tools/taxonomy.py` - `channel:`, `formality:`, `modality:`, `epistemic:`, `length:`, `stance:`, `delivery:spoken|written`. These are exactly the rejected-axis concepts, demoted to facets. A validator check (extend `validate.py`) rejects any faceted tag outside the enum. This is the single highest-leverage anti-rot mechanism: it lets the four axes stay frozen while still capturing the orthogonal dimensions people will reach for.

### Mapping the actual territory (and what counts per cell)

The aspirational inventory already sizes the territory: ~195 format candidates across 5 domains / 17 families, and ~68 voice candidates across 5 families. That is the comprehensive *surface*; 100x reaches it AND deepens it. Target counts:

| Axis | Today | Families (target) | Comprehensive entries | Per-entry samples | Total samples |
|---|---|---|---|---|---|
| Format | 15 | 20-24 (5-7 domains) | ~280 | 12+ | ~3,400 |
| Voice | 15 | 8 | ~110 | 12+ | ~1,300 |
| Tone | 15 | flat + facets | ~90 | 12+ | ~1,100 |
| Style | 15 | flat + facets | ~120 | 12+ | ~1,400 |
| **Total** | **60** | | **~600** | | **~7,200** |

So 100x is roughly 600 best-in-class entries and ~7,200 worked samples (not literally 6,000 entries - "100x" is the sample-and-coverage volume, since 600 entries x 12 samples is already ~120x today's ~195). The format surface is where breadth concentrates because writing tasks are format-shaped; voices and tones saturate faster (there are only so many human stances and registers worth distinguishing before the adherence gate starts rejecting near-duplicates - and that rejection is the feature, not a failure).

**Per-cell coverage targets** turn the tree into a ledger. Each family carries a target band: dense families (`instruction`, `deliberation`, `correspondence`) target 12-20 entries; narrow families (`messaging`, `journal`, `tribute`) target 3-8; the band is set by territory width, not uniform quota. `build-indexes.py` should emit a coverage report per cell: target, filled, gated-pass, so "comprehensive" has a number attached at every node.

### Revisiting the scope-outs - selectively, with the gate as the arbiter

The inventory deliberately scopes out fiction, poetry, legal/medical/scientific, working journalism, government/policy, children's writing, and translation. "World's most comprehensive" pressures these, but the decision rule should be empirical, not aspirational: **admit a scoped-out territory only if its entries clear the same E1 adherence gate and the entries are about the writing-instruction layer, not field-specific domain knowledge.** That rule sorts the list cleanly:

- **Revisit (admit as a sixth/seventh domain):** **journalism** as a `public` subfamily or its own `journalism` domain - news-brief, feature-lead, investigative-nut-graf are genuinely format-distinct and pass the "instruction not domain-expertise" test. **Civic/government** advocacy and testimony already live in `public/position`; widen rather than admit a new domain.
- **Admit narrowly:** **legal** and **medical** only at the *plain-language* boundary (the `plain-english-legal-summary`, `patient-instructions` formats) where the catalog teaches register, not law or medicine. Full legal briefs and clinical notes stay out - they are domain knowledge, not writing instruction.
- **Hold out:** **fiction, poetry, translation, children's writing.** These are separate crafts with their own conventions; admitting them dilutes the proven wedge and the gate cannot cleanly judge "distinguishable" against literary intent. Keep the exclusion; flag it as a maintainer decision, not a mechanical one.

### Preventing taxonomy rot at scale

Five mechanisms, each cheap and tied to existing tooling:

1. **Single source of truth.** The controlled vocabulary (domains, families, subfamilies, faceted-tag enums) lives only in `tools/taxonomy.py`; schemas reference it; `validate.py` enforces family-belongs-to-domain and subfamily-belongs-to-family. No entry validates with an invented category.
2. **No orphan families.** A family with one member is a smell. The existing "unfit" bucket pattern in the inventory stays: entries that fit no family accumulate visibly, and a family is only minted when 3+ orphans cluster (this is how `messaging` and `meetings` were reasoned about in v2).
3. **Splits are governed like schema changes.** Adding a subfamily is a tags-level change (cheap). Adding a family or domain requires an ADR and a version bump, same as the schema-evolution policy - because it re-cuts everyone's nearest-neighbor set and therefore the gate.
4. **The gate polices over-splitting.** If two proposed sibling entries cannot produce distinguishable output (the 8/8 test fails for that pair), they are not two entries - they are one entry with a confusable note. The adherence gate is also a *de-duplication* gate; it stops the catalog from minting 6,000 near-synonyms to hit a vanity count.
5. **Coverage report as drift alarm.** The per-cell ledger surfaces lopsided growth (a family ballooning past its band, a domain going stale) so re-cuts happen on signal, not vibes.

The through-line: freeze the four axes, deepen the tree to three levels, demote every tempting "new axis" to a governed facet, attach a coverage number to every node, and let the adherence gate double as the rot-and-duplication police. That keeps thousands of entries as legible as sixty, and ties "comprehensive" to a measurable ledger rather than a slogan.

## Samples and examples at 100x (a dozen-plus of everything, maximized)

The sample layer is where 100x stops being a content-writing project and becomes a generation-and-gate pipeline. The math is brutal and clarifying: today we have roughly 195 worked examples across 60 entries and 3 anchor topics (`async-standups`, `morning-routine`, `service-database-choice`), about 3 renders per entry. The backlog's own arithmetic, 120 entries times 12 samples, already lands at about 1,440. Push entries toward the aspirational inventory (roughly 195 formats, 68 voices, plus proportional tone/style growth, low-thousands of entries) and hold the 12-plus bar, and the corpus is **tens of thousands of best-in-class worked samples**. No one hand-authors that at a uniform bar. So the design question is: what do we vary, how do we avoid generating 30,000 near-duplicates, and how does each sample still clear the same empirical bar that gave the 8/8 blind adherence result its meaning?

### The sample matrix: dimensions worth varying

A "sample" today is one `(entry_id, topic_slug)` render with thin frontmatter (`entry_id`, `axis`, `topic_slug`, `topic_label`, `author_type`, `llm_model`, `review_status`). At 100x the sample is a point in a parameter space. The matrix has six dimensions; not all are free, and that constraint is the point.

| Dimension | Range | Free or coupled | Why it earns a slot |
|---|---|---|---|
| Topic | expanded anchor set (~12) | free, but domain-coupled to entry | The original adherence control: hold topic constant, vary one axis |
| Length | micro (~80w), standard (~300w), long (~800w) | semi-free; some formats cap it | A `slack-message` at 800w is a genre violation; length tests whether the entry survives compression and expansion |
| Audience | expert / mixed / lay | free | `pragmatic-architect` says it "trusts the reader to handle tradeoff information"; the lay-audience render is where that claim is falsifiable |
| Stakes | routine / consequential / crisis | free | Tones especially (`urgent`, `candid`, `confident`) only separate under load; a crisis render of `candid` vs `confident` is sharper than a routine one |
| Medium | prose / threaded / spoken-aloud | format-coupled | Forces the format axis to actually shape structure, not just word choice |
| Difficulty | natural-fit / strained / near-violation | free | The diagnostic dimension: a sample where the entry barely holds is more instructive than ten comfortable ones |

The discipline is **not** full Cartesian product. Six dimensions at 3 levels is 729 cells per entry, absurd and mostly redundant. The 12-plus per entry is a *designed slice* through this space, weighted so each sample buys distinct teaching value. A defensible default slice per entry: one render at the home topic at each of three lengths (3), one render at each of four additional spread topics at standard length (4), three "edge" renders that push one dimension to its strained setting (3), and two reserved for the novel example types below (2). That is 12, and no two are reachable from each other by a trivial paraphrase.

### Choosing the expanded anchor-topic set (3 to ~12)

Topics are the load-bearing variable because the original empirical result depended on holding topic constant while swapping one axis. The current three were chosen by instinct; the next nine need selection criteria, and the backlog already names them: **isolation**, **spread across the five domains**, and **real-worldness**.

1. **Isolation.** A topic must let exactly one axis vary while the other three and the topic stay fixed, with no confound. `service-database-choice` is called out in the backlog as "the best-isolated anchor topic" precisely because Postgres-vs-DynamoDB is a clean decision substrate: the topic does not itself drag in a tone or a format. A topic like "writing a eulogy for my father" fails isolation, it smuggles the `ceremonial` domain and a register into the substrate, so it cannot be the constant-topic control for a voice swap.
2. **Domain spread.** The expanded set must reach all five domains (professional, public, personal, ceremonial, contemplative) so every entry has a natural home topic. A contemplative `devotional-entry` rendered only on `async-standups` is being tested off its home turf; it needs a topic like "a discipline of daily rest" to render honestly. Target roughly: 4 professional, 2 public, 2 personal, 2 ceremonial, 2 contemplative topics, which gives every family at least one native substrate.
3. **Real-worldness.** Topics must be things a real writer actually faces, not synthetic prompts. The three current topics pass: a team really does debate async standups; a person really does design a morning routine. Synthetic topics produce samples that read as exercises, which violates the best-in-class constraint by construction.

A fourth, derived criterion: **cross-topic contrast**. The Phase 2 spec already reasoned this way when it picked `service-database-choice` because it "pulls hardest on parts of the catalog the first two topics undersell." The 12 topics should collectively exercise the full register range, decision vs reflection vs celebration vs instruction, so that no entry is starved of a flattering substrate and none is only ever shown flattered.

### Diversity sampling: the anti-duplication machinery

The failure mode at scale is 30,000 samples that are 80 percent the same paragraph. Best-in-class and non-redundant are the same constraint viewed twice. Three mechanisms keep the corpus diverse, and they are generation-side, not review-side, because review cannot catch redundancy it never sees.

- **Matrix-cell uniqueness.** Each sample carries its full coordinate (`length`, `audience`, `stakes`, `medium`, `difficulty`) in frontmatter, extending today's thin schema. The generator refuses to emit two samples for one entry at the same coordinate. This alone kills accidental duplication.
- **Embedding-distance dedup.** After generation, embed every sample and reject any new sample whose cosine similarity to an existing same-entry sample exceeds a threshold (start near 0.92, tune empirically). This is cheap, it is the standard near-duplicate filter, and it catches the case where two different coordinates collapsed to the same prose because the model defaulted.
- **Lexical-overlap guard.** A fast n-gram check on opening sentences, because LLMs notoriously reuse openers. The `pragmatic-architect` sample opens "We should move to async-first standups"; the generator should flag if eight of its twelve samples open with "We should."

### Diff-pairs at scale

Diff-pairs are the catalog's sharpest teaching tool, the backlog calls them exactly that, because they hold topic constant and vary one axis, mirroring the adherence-test method itself. Today there are 12, with a fixed structure: frontmatter (`entry_a`, `entry_b`, `axis_varied`, `generator`), a "What to notice" block, then the A and B renders. At 100x, do **not** generate all O(n squared) pairs; that is millions and most are uninstructive. Generate diff-pairs only for **within-family confusables**, which the domain/family taxonomy makes mechanical to enumerate (the `expert` voice family, the `deliberation` format family, the narrative styles); the taxonomy doc explicitly recommends "prefer within-family diff-pairs as the sharpest pedagogical contrast." Per family, generate the pairwise diff-pairs among its members on each member's shared home topic. That is O(family-size squared) per family, summed: a few thousand pairs, not millions, and every one teaches a distinction a learner would actually confuse. The two "subtle" pairs from the adherence test (`pragmatic-architect` vs `senior-consultant`, `narrative-case-study` vs `chronological-narrative`) are the priority template: the close pairs are where diff-pairs earn their keep.

### Novel example types beyond the single render

The single `(entry, topic)` render is one teaching mode. Four more, each a distinct artifact type with its own frontmatter and its own generation recipe:

1. **Before/after pairs.** The Phase 2 spec already mandates one per entry (`before_after_example` with `before`, `after`, `commentary`): a 50-100 word passage written *without* the entry, then *with* it. This isolates the entry's marginal effect better than any single render, because the reader sees the delta directly. At scale, generate one before/after per entry per home topic, so the "before" is a plausible neutral baseline, not a strawman. Non-redundant by construction: there is exactly one per entry-topic, and the "before" is generated by deliberately omitting the entry's `llm_instruction_phrasing`.

2. **Failure galleries.** Each entry's `anti_patterns`, `when_not_to_use`, and `failure_modes` fields are currently prose assertions. A failure gallery *renders* them: short samples that show the entry misapplied, labeled with which failure mode they instantiate. `pragmatic-architect` lists `when_not_to_use: condolence notes`; the gallery shows the architect voice writing a condolence note, and it is visibly wrong, which teaches the boundary far better than the prose warning. These stay best-in-class by being best-in-class *examples of a named failure*, not sloppy writing, the badness is the lesson, and it is deliberate and annotated.

3. **Adversarial / anti-examples.** Distinct from failure galleries: these target the confusables directly. An anti-example for `confident` is a passage that a naive reader would attribute to `confident` but actually fails the entry's own tells (it asserts but hedges, or claims a track record it does not show). The adherence test's judge "keyed on" `confident` asserting "I have run this on two prior teams" with no self-doubt; an anti-example is the near-miss that omits exactly that tell. These are the generated form of the `confusable_with` field and feed directly back into sharpening it (backlog item C1).

4. **Multi-model adherence renders.** The single biggest caveat in the adherence smoke test was "strong model on both ends": it proved a capable model renders the distinctions, not that a Haiku-class model does. A multi-model render takes one composed instruction and renders it across several models (the frontmatter already has an `llm_model` field, currently always `claude-sonnet-4-6`). Showing the same `socratic-inquiry` instruction holding its interrogative structure across three model tiers is *robustness evidence*, it converts a caveat into a demonstrated property, and it is the corpus form of the "vary the generator model" fix the audit itself asked for.

### How this stays a generation-and-gate output, not a writing project

Every sample type above is produced by extending `tools/diff-pair-generator.py` into the fuller generator the backlog's E1 item describes, then cleared by the automated adherence gate. The gate is the quality guarantee: a sample (or the entry behind it) earns its place only by producing measurably distinguishable output, the 8/8 result turned into a standing rule. Generation makes tens of thousands of samples *possible*; the gate plus the three diversity mechanisms make them *non-redundant and best-in-class*. Volume without the gate reintroduces the exact "many mixed-quality entries dilute the one proven signal" risk the ROADMAP named. The order is fixed and non-negotiable: gate first, then generate at volume behind it.

### Open decisions for the maintainer

- **Lock the 12 anchor topics**, with explicit domain assignment, before mass generation. This is the highest-leverage unresolved input; everything keys off it.
- **Set the per-entry slice** (the specific 12 matrix coordinates) as a template, or allow per-family variation (a `slack-message` cannot honor the long-length coordinate).
- **Pick the embedding model and similarity threshold** for dedup, and decide whether dedup is a hard reject or a human-review flag.
- **Decide the multi-model render set** (which models, how many tiers) and whether multi-model renders are mandatory per entry or reserved for the subtle/confusable pairs where robustness matters most.
- **Decide whether failure galleries and anti-examples are required per entry** or generated on demand for the confusable clusters only, which is cheaper and arguably sufficient.

## Frontier ideas: what makes it best-in-class, not merely big

A catalog of 60 entries on `pairs_well_with` and `llm_instruction_phrasing` is a content artifact. A catalog of thousands is a database. Neither is automatically best-in-class. What makes this project defensible at 100x is the one thing no competitor catalog has bothered to build: a *measurement* tying each entry to a proven empirical result. The 2026-05-31 smoke test (8/8 blind attribution, chance about 0.4 percent) is not a marketing line - it is the seed of a moat. The frontier ideas below all extend that seed. They are ranked by how directly they convert the proven result into a structural advantage, and every one of them depends on E1 (the automated adherence gate) actually existing, because measurement is the substrate the rest sits on.

### 1. The per-entry distinguishability score (the measurable moat)

**What it is.** Every entry carries a new frontmatter field - call it `distinguishability` - holding the output of running that entry through the adherence harness against its nearest confusable neighbor on a fixed anchor topic. Concretely: a score (judge attribution accuracy over N blind trials), a band (`dramatic` / `clear` / `subtle` / `identical`, the exact four the smoke test already produced), the neighbor it was tested against, the topic, the judge and generator models, and a date. The smoke-test table already produces this shape per pair; this idea promotes it from a one-off audit row to a first-class, per-entry, recomputed-on-change field.

**Why it is best-in-class.** No other writing-style resource can say "this voice produces output a blind reader distinguishes from its nearest neighbor 94 percent of the time." Competitors ship prose descriptions and trust the reader. This ships a number with a reproducible method behind it. It also turns the catalog's worst weakness into a managed metric: the smoke test found exactly two `subtle` pairs (`pragmatic-architect` vs `senior-consultant`; `narrative-case-study` vs `chronological-narrative`). A per-entry score makes those visible as a maintenance signal rather than a buried footnote, and it gives the C1 backlog item a definition of done ("move both out of the `subtle` band").

**What it depends on.** E1 automated gate; a fixed `confusable_with` neighbor per entry (already a curated field); a stable anchor-topic-per-entry mapping. It does not depend on schema upheaval - it is one additive object on the existing `entry.universal.schema.json`.

### 2. The gate as a one-directional ratchet, not a checkpoint

**What it is.** The adherence gate (E1) is usually framed as admission control: a new entry must produce distinguishable output to earn its place. The frontier move is to make it a *ratchet* on the whole catalog. Every entry stores its score; CI re-runs the gate not only on new entries but on the neighbors of any edited entry, and **fails the build if an existing entry's band regresses** (e.g., editing `senior-consultant` accidentally collapses it toward `pragmatic-architect`). At 60 entries you can eyeball quality. At thousands, the only thing standing between "best-in-class" and "big pile" is a test that refuses to let quality silently erode. This is what converts the quality-as-hard-constraint framing from an aspiration into machinery.

**Why it is best-in-class.** It makes quality monotonic. A 5,000-entry catalog where every entry has *ever* passed and *still* passes the distinguishability gate is a categorically different asset than 5,000 entries someone wrote carefully once.

**What it depends on.** Score storage (idea 1); a neighbor graph from `confusable_with`; an affordable judge (cost discussed below).

### 3. Per-model phrasing variants and a public adherence leaderboard

**What it is.** `llm_instruction_phrasing` is currently one string per entry, implicitly tuned for an Opus-class model (caveat 1 of the smoke test: "strong model on both ends"). Split it into a small map keyed by model family - `llm_instruction_phrasing: { default: ..., haiku: ..., gpt: ..., gemini: ... }` - and publish a leaderboard: for each model, what fraction of the catalog's entries clear the `clear`-or-better band. This is the public benchmark the audit gestured at and the smoke test explicitly deferred.

**Why it is best-in-class.** It reframes the catalog from "a list of instructions" to "the benchmark for whether a model can be steered into a named writing style." That is a durable, citable artifact - the kind of thing model labs reference. It also directly attacks the honest weakness of the proven result: prove it on Haiku-class and cross-vendor models, in public, and the moat widens from "works on one strong model" to "works, measurably, across the frontier."

**What it depends on.** Multi-model access in the harness (the smoke test recommends varying the generator); versioned phrasings (idea 6); a non-trivial eval budget.

### 4. Conflict-aware composition surfaced as a confidence-graded product, via MCP

**What it is.** Today `compose_instruction` in `build-instruction.py` (lines 149-187) does exactly one thing: load each selected entry, pull `llm_instruction_phrasing`, and `"\n\n".join(parts)`. It never reads `avoid_with`, `pairs_well_with`, or `confusable_with`, even though `_parse_simple_yaml` already parses them. So composing `voice=pragmatic-architect` with `tone=reverent` silently staples "lead with tradeoffs, no softening" to "approach with reverence and weight" - and `reverent` is *literally in* pragmatic-architect's `avoid_with: [reverent, pastoral]`. The frontier version (building on S1) does not just warn; it returns a **composition confidence** computed from the relationship graph: green when the selections appear in each other's `pairs_well_with`, yellow on no relationship, red on an `avoid_with` hit. Exposed through the MCP server (S2), this confidence becomes a product surface: an agent composing an instruction gets back not just the concatenated text but a machine-readable "this combination is coherent / unproven / contradictory" signal.

**Why it is best-in-class.** Programmatic composition with a coherence score is something no static catalog or prompt library offers. It turns the relationship fields - currently inert curation - into runtime guardrails. At 100x scale the combinatorial space is astronomically large (thousands of entries across four axes); a confidence signal is the only thing that keeps that space navigable rather than a field of footguns.

**What it depends on.** S1 (conflict-aware composition) first, explicitly before S2 - the backlog is firm that the MCP server must expose the guaranteed behavior, not the naive concatenation. Also a decision the backlog flags as open: is `avoid_with` symmetric? The composer needs that resolved to compute confidence deterministically.

### 5. Auto-generated diff-pairs and interactive side-by-side as the teaching surface at scale

**What it is.** Diff-pairs hold the topic constant and vary one axis - the catalog's sharpest teaching tool. They are hand-authored today and coverage is uneven (`service-database-choice` has zero pairs despite being the best-isolated topic). The frontier move chains two existing assets: the single-entry renders already sitting under `examples/vertical-slices/` and `tools/diff-pair-generator.py`. For any two same-family neighbors, auto-emit the A/B render pair; the only human-authored part is the "What to notice" prose, and even that can be seeded from what the adherence judge *keyed on* (the smoke test already recorded judge rationale per pair: "candid admitted the downside of its own proposal ... confident asserted with track-record proof"). Surface these as an interactive side-by-side in the docs site with the axis toggle live.

**Why it is best-in-class.** The diff-pair and the distinguishability score are the same measurement viewed two ways: the score is the quantitative claim, the diff-pair is the qualitative evidence a human can read. Generating both from one harness run means every entry ships with proof *and* a demonstration, automatically, at any scale. Competitors show you a description; this shows you the measured difference and lets you flip the variable yourself.

**What it depends on.** The E1 generator extending `diff-pair-generator.py`; the domain/family taxonomy (ADR 0010) so "same-family neighbor" is well-defined and pairs stay within-family for sharpest contrast.

### 6. Versioned phrasings tracked against model releases

**What it is.** Treat `llm_instruction_phrasing` as code that decays. Each phrasing variant records the model version it was last validated against and its band at that time. When a new model ships, CI re-runs the gate; entries whose band drops get flagged `needs-rephrasing`. This is a changelog of *steerability* over model generations.

**Why it is best-in-class.** Every prompt library on the internet rots silently as models change. This one knows when it has rotted, per entry, with a number. That is the difference between a maintained instrument and a dead document.

**What it depends on.** Per-model variants (idea 3) and score storage (idea 1); a cadence for re-running the gate on model releases.

### How the ideas stack

| Idea | Core artifact | Defensibility | Hard dependency |
|---|---|---|---|
| 1. Distinguishability score | `distinguishability` field per entry | A reproducible number competitors cannot fake | E1 gate; fixed neighbor + topic |
| 2. Quality ratchet | CI fails on band regression | Quality becomes monotonic at scale | Idea 1; neighbor graph |
| 3. Per-model variants + leaderboard | phrasing map + public benchmark | Becomes the steerability benchmark labs cite | Multi-model harness; budget |
| 4. Confidence-graded composition (MCP) | green/yellow/red on compose | Runtime guardrails from relationship data | S1 then S2; `avoid_with` symmetry call |
| 5. Auto diff-pairs + side-by-side | generated A/B + "what to notice" | Proof and demonstration, free, at scale | E1 generator; family taxonomy |
| 6. Versioned phrasings | per-model validation dates + bands | Knows when it has rotted | Ideas 1 and 3 |

### The one hard constraint underneath all six

Every idea here converts compute into quality assurance, which means the binding limit is judge cost, not authoring effort. At 120 entries times one neighbor times N blind trials the gate is cheap; at thousands of entries re-run on every model release it is not. The defensible design is a tiered judge: a cheap model screens for the `identical` / `subtle` band where regressions hide, and an Opus-class judge confirms only the borderline cases - mirroring the smoke test's own setup, where strong models on both ends were the point. Get that economics right and "most comprehensive" and "best-in-class" stop trading against each other, because the same harness run that admits an entry is the proof, the demo, and the regression test all at once. That is the difference no competitor catalog has: not size, but a per-entry, recomputed, public claim that the distinction is real.

## Risks, economics, and the 1x to 100x roadmap

The catalog's entire value is one empirical fact: composing entries from `llm_instruction_phrasing` produces output a blind judge can attribute (8/8 pairs, p ~0.4 percent, per `_LOCAL/audit/2026-05-31_adherence-smoke-test.md`). That fact is fragile. It was measured at 60 entries with strong models on both ends, and two of the eight pairs - `pragmatic-architect` vs `senior-consultant` and `narrative-case-study` vs `chronological-narrative` - already rated only "subtle". 100x means thousands of entries and tens of thousands of samples. Every failure mode below is a way that the next 10,000 entries quietly stop being distinguishable while the README still says they are. This section is the skeptic's brief, then the operator's plan.

### The failure modes (and the one mitigation that matters per mode)

| # | Failure mode | What it looks like in THIS repo | Concrete mitigation |
|---|---|---|---|
| 1 | Quality dilution below the gate | Entry 800 produces output a judge can't tell from its nearest `confusable_with` neighbor; the 8/8 becomes 6/8, then 3/4 | Automated adherence gate (E1) is a hard merge-blocker: render candidate vs its declared nearest neighbor on a fixed topic, blind-attribute, reject below threshold. No gate, no entry. |
| 2 | Sample sameness / LLM monoculture | All 1,440+ samples generated by one Opus prompt template converge to the same cadence; entries look distinct but samples rhyme | Generator-model and prompt-template diversity as a *measured* property: rotate generator models, and add a sameness check (n-gram / embedding-distance) to `validate.py` that flags clustered samples |
| 3 | Taxonomy rot | 17 families bloat; `instruction` (already 19 candidates) swallows everything; `confusable_with` graphs go stale as neighbors multiply | Codify the domain/family taxonomy as ADR 0010 *before* mass-add (backlog E2 sequencing); cap family size (the taxonomy doc already names "any single family exceeds 12 members" as a split trigger) |
| 4 | Eval / judge drift | The gate judge gets more lenient (or stricter) over 18 months; "pass" in month 1 != "pass" in month 12 | Pin a frozen golden set: the original 8 pairs become permanent regression anchors, re-run every batch; if the judge re-scores them differently, the judge drifted, not the entries |
| 5 | Maintenance collapse | One solo maintainer cannot hold thousands of entries + cross-ref graph in their head (constraint 3 in the taxonomy doc) | Make the graph machine-maintained: `validate.py` already enforces referential integrity on `pairs_well_with`/`avoid_with`/`confusable_with`; extend it to flag orphaned and stale edges so the human curates exceptions, not the whole graph |
| 6 | Redundancy | `chat-message`, `dm`, `slack-message` are three near-identical messaging entries; `observer`/`eyewitness`/`chronicler` blur | The gate IS the redundancy test: if a new entry can't be told apart from an existing one, it fails. Redundancy and indistinguishability are the same failure, caught by the same machine. |
| 7 | Scope creep into fiction / legal / medical | "World's most comprehensive" pressures the maintainer to add legal briefs, clinical notes, screenplays - each a field with its own conventions the catalog can't validate | Hold the inventory's explicit out-of-scope list (fiction, poetry, legal/medical/scientific, journalism, government, children's, translation). Reopening any boundary is a maintainer ADR, never a mechanical add. |
| 8 | Over-automation losing human taste | The gate proves *distinguishable*, not *good*. A pipeline can mass-produce 10,000 distinct-but-mediocre entries that all pass | The gate is necessary, not sufficient. Keep a human "reference-quality" tier: `review_status` stays `draft` on generated entries; only maintainer review promotes to `stable`. The 60-entry seed remains the taste anchor. |

The through-line: failure modes 1, 2, 6, and 8 are all "the signal degraded and nobody noticed." The defense is the same in each case - a measurement that runs on every batch and refuses to merge what it can't distinguish. The catalog already has the cheap version of this (the smoke test) and the data it needs (`avoid_with`, `confusable_with`, declared neighbors). Scaling is mostly the work of turning that one-off audit into a standing gate.

### Economics, honest and order-of-magnitude

The unit costs are grounded in the repo as it stands today. A typical entry (`pragmatic-architect/ENTRY.md`) is ~780 words; a vertical-slice sample is ~480 words (28,952 words across ~60 slice files for `service-database-choice`). The Phase 2 milestone is 120 entries x 12 samples = ~1,440 samples. "Comprehensive" per the aspirational inventory is ~195 formats + ~68 voices, plus proportional tone/style growth, call it ~600-1,000 entries; at 12 samples each that is ~7,000-12,000 samples. True 100x (thousands of entries, 12+ samples) lands at tens of thousands of samples. Costs below are per generation pass; the gate adds a second judged pass on top.

| Scale | Entries | Samples (~12/entry) | Gen tokens (rough) | API gen cost | Human review hours | Honest read |
|---|---|---|---|---|---|---|
| 1x (today) | 60 | 180 (3/entry) | done | sunk | the seed review | proven, taste-anchored |
| 3x | ~120 | ~1,440 | ~30-60M | low hundreds USD | ~80-150 hrs | a weekend of compute, a month of review |
| 10x | ~600 | ~7,200 | ~150-300M | low thousands USD | ~400-700 hrs | needs the pipeline + gate to exist |
| 30x | ~1,800 | ~21,600 | ~0.5-1B | ~5-15K USD | 1,000+ hrs | unworkable without judge automation and 2+ curators |
| 100x | ~6,000 | ~72,000 | ~2-4B | ~15-50K USD | small team-year | a funded project, not a side repo |

Three honest points about these numbers. First, **API token cost is the cheap part**. Even at 100x the generation spend is tens of thousands of dollars - a rounding error against the human cost. Second, **the gate roughly doubles compute**: every sample is generated once and judged at least once, and rejected entries are pure waste (regenerate-and-rejudge), so budget a 1.5-2x multiplier on the naive number. Third, **human review is the true constraint and it does not parallelize cleanly**. At 30x, 1,000+ review hours is more than one person delivers in a year at sustainable quality; "best-in-class as a hard constraint" means a human must still taste-check promotions to `stable`, and that human is the bottleneck the whole roadmap must respect. The realistic resourcing for 100x is on the order of 2-4 people for 18-24 months, with infra (eval harness, sample store, CI judge runs) being the smallest line item. Anyone promising 100x on solo evenings is promising 100x of failure mode 8.

### The staged roadmap: 1x -> 3x -> 10x -> 30x -> 100x

Each stage names what unlocks it, the gate it must clear, and the stop/go signal that authorizes the next. Do not skip a stage to chase a count - that is the "120 mixed-quality entries" risk the ROADMAP was built to prevent.

**1x -> 3x (60 -> 120 entries, the proven core hardened).**
- *Unlocks:* the near-term P1 work in `backlog.md` - sharpen the two subtle pairs (C1), build `service-database-choice` diff-pairs (C2, currently zero), and make `compose_instruction` conflict-aware (S1, which today just concatenates and ignores `avoid_with`). This is foundation, not scale.
- *Gate:* the existing 8/8 smoke test, re-run by hand. The two subtle pairs must hold or improve; if sharpening `confusable_with` makes them worse, stop.
- *Stop/go to advance:* the adherence test is *automated* (E1 exists as a script, not a memory of one audit) AND at least one real consumer is using composition. No usage signal, no breadth expansion - that was the deliberate ROADMAP defer.

**3x -> 10x (120 -> ~600 entries, breadth behind the machine).**
- *Unlocks:* E1 fully built - generation pipeline (extend `tools/diff-pair-generator.py`), automated judge, and bar-checking in `validate.py` (presence of tells, anti-patterns, failure modes, min sample count). ADR 0010 taxonomy codified so entries are born categorized.
- *Gate:* every new entry passes the automated adherence gate against its declared nearest neighbor AND the frozen golden-8 regression set still scores 8/8. Sameness check below threshold on its samples.
- *Stop/go to advance:* batch pass-rate (entries clearing the gate on first generation) stays above a set floor - say 70 percent. A collapsing first-pass rate means the catalog is entering territory the model can't differentiate (failure mode 1), and breadth should stop, not push.

**10x -> 30x (~600 -> ~1,800 entries, the human-cost wall).**
- *Unlocks:* a second curator and the meta-layer (E4) - navigation, family diagrams, contributor on-ramp - so review is no longer single-threaded. Judge-diversity and model-rotation are live (failure mode 2).
- *Gate:* the gate, plus a *promotion* gate - generated entries stay `draft`; a human must taste-check before `stable`. The CLAUDE.md rule ("never set `review_status` to `stable` without maintainer review") becomes the load-bearing quality wall.
- *Stop/go to advance:* the `draft`-to-`stable` promotion queue is not growing unboundedly. If review can't keep pace with generation, the catalog is becoming a pile of unvetted drafts; pause generation until review catches up.

**30x -> 100x (~1,800 -> ~6,000+ entries, a funded program).**
- *Unlocks:* sustained team + budget (the table above), external contributors clearing the same automated gate, and likely a subfamily layer (the taxonomy doc already anticipates this at 200+/axis).
- *Gate:* everything above, continuously, in CI. The golden set has grown from 8 pairs to a standing regression suite that any model or judge change is validated against.
- *Stop/go (this is the terminal honesty check):* if measured distinguishability across the *whole* catalog is trending down, 100x is the wrong goal - a smaller, sharper catalog beats a vast indistinct one, because the value was never the count, it was the proof. The roadmap must be willing to stop at 10x or 30x if that is where best-in-class quality stops scaling.

The discipline is identical at every rung: scale only behind a gate that refuses what it can't distinguish, and treat a falling pass-rate as a stop signal, not a tuning problem. Comprehensiveness is the destination; the gate is the road; and the road is allowed to end before the destination if quality says so.

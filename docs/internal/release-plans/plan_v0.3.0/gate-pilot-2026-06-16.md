# Adherence Gate Pilot - near-neighbor distinguishability (2026-06-16)

> Runs decision register item **Q12 - gate pilot before freezing A1** from the Fable taxonomy
> evaluation (`_LOCAL/2026-06-09_a1-taxonomy-evaluation_by-fable.md`, Section 13). It is the
> cheapest empirical answer to the one question the whole agentic-first bet (F3 - resourcing
> posture) rests on: can a blind judge tell apart entries that are *near neighbors*, not just the
> far contrasts the original 8-of-8 smoke test used? Feeds A1 (taxonomy ratification), C4 (gate
> thresholds), and the ROADMAP "sharpen the subtle pairs" item.

## Why this pilot exists

The catalog's credibility rests on one result: a blind judge attributed 8 of 8 confusable
composition pairs correctly (chance about 0.4 percent). But those pairs were *far contrasts*. The
adherence gate (E1) does not judge far contrasts - it renders each candidate against its
**nearest same-category neighbors** and rejects anything indistinguishable. So the load-bearing
question was never tested: is the gate's bar even *achievable* on hard, same-cluster pairs? If
near neighbors blur, the agentic-first quality mechanism fails silently at scale. This pilot
tests exactly that, on 8 deliberately hard pairs spanning all four axes.

## Method

- **8 near-neighbor pairs**, two entries each that vary on a single axis and sit in the same
  conceptual cluster (e.g. two "expert" voices, two narrative styles, two caring tones).
- **Single-axis isolation, fixed topic.** Each render applied only that one axis's
  `llm_instruction_phrasing` on a topic held identical within the pair, mirroring how the gate
  renders. The other three axes were unset.
- **Generator:** Claude Opus 4.8 (the catalog's default generation model).
- **Judge:** Claude Sonnet 4.6, blind. The judge saw only the two anonymized, shuffled renders
  and the two candidate profiles, and made a forced binary attribution plus a distinguishability
  band (dramatic / clear / subtle / identical). It never saw the ground-truth mapping.
- **Cross-model, not yet cross-vendor.** Decision C2 - judge policy requires a judge from a
  different model *family* than the generator. Fable 5 (the intended cross-line judge, and the
  model that reviewed A1) was unavailable at run time, so Sonnet 4.6 served as an available
  cross-*model* proxy against the Opus generator. This is stronger than Opus-judging-Opus (the
  monoculture C2 warns about) but weaker than a cross-*vendor* judge (GPT / Codex), which remains
  the standard for the production gate. See Caveats.

## Result: 8 of 8 correct on near neighbors

Forced binary choice per pair, so the chance of 8 of 8 by guessing is 0.5^8 ~ 0.39 percent - the
same baseline as the original far-contrast test, now established on hard pairs.

| Pair | Axis | The near-neighbor pair | Judge correct? | Band | Confidence |
|---|---|---|---|---|---|
| P1 | voice | pragmatic-architect vs senior-consultant | yes | clear | high |
| P2 | voice | researcher vs technical-writer | yes | dramatic | high |
| P3 | style | narrative-case-study vs chronological-narrative | yes | **subtle** | high |
| P4 | style | diataxis-explanation vs how-to-tutorial | yes | dramatic | high |
| P5 | tone | confident vs resolute | yes | **subtle** | medium |
| P6 | tone | warm vs empathetic | yes | **subtle** | medium |
| P7 | format | adr vs prd | yes | dramatic | high |
| P8 | format | readme vs technical-reference | yes | dramatic | high |

Band distribution: dramatic 4, clear 1, subtle 3, identical 0. The judge's rationale on every
pair named a real, entry-specific cue (e.g. P3: "Render uses strict time markers with no
principle stated vs names a turning point and closes with a lesson"), not a surface tell.

## Cross-vendor confirmation (2026-06-16)

The single biggest weakness of the first run was that Sonnet and Opus are the same vendor, so
C2 - judge policy was only partially satisfied. The identical blind packet was therefore
re-judged by **Codex (OpenAI GPT)**, a genuinely different vendor.

**Codex also scored 8 of 8 correct.** Two independent vendors now agree: **16 of 16 attributions
across Anthropic Sonnet and OpenAI GPT**. This retires the same-vendor / monoculture caveat and
satisfies C2's cross-family-judge intent for this pilot.

The two judges also disagree about *difficulty* in a useful way:

| Pair | Sonnet band | Codex band |
|---|---|---|
| P1 pragmatic-architect / senior-consultant | clear | clear |
| P3 narrative-case-study / chronological-narrative | subtle | clear |
| P5 confident / resolute | subtle | clear |
| P6 warm / empathetic | **subtle** | **subtle** |
| P2, P4, P7, P8 | dramatic | dramatic |

Codex found P3 and P5 easy where Sonnet found them subtle, but **both vendors flagged
`warm` / `empathetic` (P6) as subtle**. A cross-vendor consensus on a single hardest seam is
stronger sharpening signal than one judge's band: it separates "genuinely thin distinction"
(warm/empathetic) from "thin to one model only" (the two narrative/assertive pairs).

## Findings

1. **The gate's premise holds on hard cases.** Near neighbors are distinguishable, not just far
   contrasts. This is the first direct evidence that the E1 gate's bar is achievable on the
   comparison it actually makes, which is the precondition for the agentic-first bet paying off.
2. **The genuinely close seams cluster at "subtle" - and they are nameable.** Three pairs landed
   subtle: `narrative-case-study` / `chronological-narrative` (already flagged in the ROADMAP),
   plus two newly surfaced tone seams, `warm` / `empathetic` and `confident` / `resolute`, both
   judged correctly but at only medium confidence. These are the four weakest seams to sharpen
   first (the ROADMAP item now has concrete targets beyond the original two).
3. **Formats are trivially distinguishable** (all dramatic) because their structure is the
   signal. The real distinguishability work lives in voice, tone, and style - exactly where the
   gate's threshold discipline will matter and where the subtle band showed up.
4. **Distinguishability is validated; quality is not.** This pilot measures only "distinct," which
   is C1's settled half. C1's open sub-problem (a judge-applicable *quality* rubric) is untouched
   and remains a gate-blocking item before E1 ships.

## What it feeds

- **A1 - taxonomy cuts:** the gate the taxonomy renders against is viable on near neighbors, so
  ratifying the structure does not rest on an untested mechanism. (Ratification is still the
  maintainer's call via the Q1-Q12 register.)
- **C4 - gate thresholds:** the proposed "subtle-or-better" band with forced-choice-correct is
  achievable, and an 8/8 first-pass rate clears the proposed 70 percent first-pass stop floor
  comfortably on these pairs. Real thresholds still want a larger sample.
- **Q7 - subfamily trigger / Q8 - placements:** confirms the pilot method can settle these
  empirically; a larger run can decide the borderline placements Fable flagged.
- **ROADMAP:** the "sharpen the two subtle pairs" item expands to four named subtle seams.

## Caveats (do not over-read an n=8 pilot)

- **Cross-vendor confirmation done (was the main caveat).** The first run's judge (Sonnet) shared
  a vendor with the generator (Opus). The identical packet was re-judged by Codex (OpenAI GPT) and
  also scored 8/8 (see the cross-vendor section above), so this caveat is addressed. The residual
  limit is that both vendors are strong models, so an adversarial production gate should still
  spot-audit clean passers.
- **n = 8.** Directional, not definitive. A production gate calibration wants tens of pairs per
  axis.
- **Fresh renders, not the frozen 60's own samples.** The renders were generated by Opus for this
  pilot; the gate will eventually render real candidates. And the judge was given the candidate
  descriptors (faithful to the original test, but a harder variant would withhold them).
- **Generator and judge are both capable models.** The smoke-test caveat ("strong model on both
  ends") still applies; the cross-vendor confirmation is what retires it.

## Recommended next steps

1. **Cross-vendor confirmation - DONE (2026-06-16):** the exact blind packet was re-judged by
   Codex (OpenAI GPT) and also scored 8/8, retiring the same-vendor caveat (see the cross-vendor
   section). Raw renders and the key are in `_agent-context/gate-pilot/` (local).
2. **Sharpen the four subtle seams** (`narrative-case-study`/`chronological-narrative`,
   `warm`/`empathetic`, `confident`/`resolute`) by tightening their `confusable_with` distinctions
   from both sides - higher leverage than new entries.
3. **Define the C1 quality rubric** before E1 ships; distinguishability alone is validated, quality
   is not.

## Reproducibility

- Method, pairs, topics, and the shuffled-slot key are recorded here.
- Raw labeled renders: `_agent-context/gate-pilot/2026-06-16_renders_labeled.md` (local-only,
  gitignored).
- Generator: Claude Opus 4.8. Judge: Claude Sonnet 4.6 (Fable 5 attempted, unavailable).

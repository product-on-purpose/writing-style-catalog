# Recommender scorer quality: investigation, design, and deferral

- **Status:** designed, then deferred by maintainer decision (2026-07-17). Not implemented. Pick up from "If resumed" below.
- **Source finding:** the 2026-07-10 audit's `recommender-quality-probe.md` (findings P-2 through P-6), now backed by the `tests/eval/` regression corpus (shipped 2026-07-16, PR #115).
- **Scope of this doc:** what a brainstorming session on 2026-07-17 established about fixing the scorer's quality findings, the design it converged on, the empirical measurements that de-risk it, and why it was set aside rather than built.

## Why this exists

The probe found five scorer-quality issues (P-2 negation blindness, P-3 the distinct-match gate rejecting gold singletons, P-4 vocabulary gaps, P-5 length dilution, P-6 stopword gaps). It opened with a caveat worth repeating: **"Nothing here is a defect in shipped behavior. The scorer behaves exactly as documented and as adversarially reviewed."** These are refinements, not bugs.

A session set out to fix them, starting with negation (the highest-value finding). The investigation changed the picture enough that the maintainer chose to document and defer rather than build. This doc preserves what was learned so the deferral is informed, not lost.

## What the investigation proved (the load-bearing part)

These are measured facts against the current scorer (`skills/entry-recommender/scripts/recommend.py`) and the 10-case corpus in `tests/eval/situations.jsonl`. A future session should not re-derive them.

### 1. Negation rank inversion is NOT fixable at the scorer layer

On `negation-casual` ("absolutely not corporate or formal, no business jargon, just casual"), `reverent` ranks #1 (score 22.63). Its matched tokens are `formal` and `casual` in `when_to_use`, `tells`, and `facets` - **not** `no`/`not`. The bad match is on legitimate topical words used in an *exclusion*, which keyword overlap scores positively because it cannot see polarity.

Consequence: no stopword change and no reweighting fixes this. The only lever at the deterministic layer is a SKILL.md instruction telling Step 2 to treat excluded-register words as evidence against a candidate. Step 2's read is where the actual recovery happens. This upgrades the probe's "read-before-pick is load-bearing" from caution to proven.

### 2. The "recoverable right answer" on the negation case was a junk artifact

The probe noted `playful` (the human-correct tone for a casual note) was present in the shortlist, so Step 2 could recover it. Measured: `playful` qualifies **only** on `no` and `not` (matched_tokens = `{tells: [no, not], facets: [no, not]}`, score 3.29, distinct_matches 2, zero real signal). It was surfaced by accident, matching the negation words, not any casual/informal vocabulary.

Consequence: stripping `no`/`not` correctly drops `playful`, and that is not a lost genuine match - it exposes a real vocabulary gap (no tone entry cleanly carries casual/informal language). That gap is a P-4 target, not a reason to keep junk tokens.

### 3. Per-token stopword measurement (each token added to STOPWORDS individually, qualifying sets diffed across all 10 cases)

| token | cases changed | qualifiers removed | qualifiers added | verdict |
|---|---|---|---|---|
| `no` | 2 (negation-casual, conflict-bait) | 26 | 0 | adopt (per decision 5) |
| `not` | 2 (headline-feature-cut, negation-casual) | 53 | 0 | adopt (per decision 5) |
| `all` | 1 (layoff) | 1 (`tone:resolute`) | 0 | adopt: probe-named junk |
| `off` | 1 (layoff) | 1 (`tone:resolute`) | 0 | adopt: probe-named junk |
| `something` | 1 (noisy-rambling) | 2 (`tone:celebratory`, `format:devotional-entry`) | 0 | adopt: dilution noise |
| `took` | 0 | 0 | 0 | **reject**: no-op (the distinct-match gate already blocks it) |
| strip-pure-numbers | 0 | 0 | 0 | **reject**: no-op on this corpus |
| `how` | n/a | n/a | n/a | **exclude (hard constraint)**: load-bearing for `diataxis-explanation` via facet text (`audience-vs-topic` case) |

None of the removed qualifiers is a probe-named genuine pick, with the single exception of `playful` (decision 5 below). The `took` and strip-numbers results apply the evidence gate literally: a token that removes zero junk on the corpus fails the "removes at least one junk match" bar, so it is not adopted as untestable insurance.

## The design that was converged on (phase A)

If built, phase A is one PR with these parts:

1. **SKILL.md Step 2 negation caution (text).** One or two sentences: when the situation excludes a register ("not formal", "no hype"), treat matches on the excluded words as evidence against a candidate, not for it. This is the only thing that addresses the rank inversion (finding 1).
2. **`STOPWORDS += {no, not, all, off, something}`** in `recommend.py`. Evidence-gated per the table above. `took`, strip-numbers, and `how` are deliberately excluded.
3. **Regenerate `tests/eval/` baselines as intentional drift.** The runbook (step 12) already prescribes this: update `baseline` and `baseline_date` in `situations.jsonl` in the same PR, each delta confirmed as junk-removal. The probe-named genuine picks (pragmatic-architect, resolute-on-headline, decision-log, postmortem, diataxis-explanation) MUST survive - that is the regression check.
4. **Route the exposed gaps to P-4.** Stripping junk makes `layoff` tone and `negation-casual` tone honestly low-confidence, exposing that no tone entry carries casual/informal or HR/layoff vocabulary. Record as P-4 enrichment targets; do not fix here.
5. **Version bump** entry-recommender 0.2.0 -> 0.2.1 (scoring refinement), in both SKILL.md `metadata.version` and `library.json` (the manifest validator requires agreement).

Measured behavior changes to expect: `layoff` tone to 0 qualifying; `negation-casual` tone drops `playful`; `headline-feature-cut` format sheds `celebratory` plus the `not`-inflated tail (genuine leaders survive); `noisy-rambling` sheds two dilution matches.

## Maintainer decisions taken interactively (2026-07-17)

1. **Sequenced ("both"):** do the cheap deterministic-layer work now, keep the door open to a heavier fix later, decide later based on real use.
2. **Scope:** phase A = P-2a (SKILL.md caution) + P-2b/P-6 (stopwords). P-3 (gold-singleton gate exception) and P-4 (vocabulary enrichment) split out as separate follow-ups.
3. **Approach:** token-by-token, evidence-gated stopword calibration (adopt only tokens that provably remove junk and cost no genuine pick), not all-at-once.
4. **Strip `no`/`not`:** precision over serendipity. Junk tokens surface wrong answers (`celebratory` on `headline-feature-cut`) as readily as the accidental right one (`playful`); the serendipity is not selective, so keeping them is not justified.
5. **Then deferred the whole thing** (see below).

## Why it was deferred

The investigation weakened the case for doing scorer work first:

- The headline finding (negation blindness) is unfixable at the scorer layer (finding 1). The scorer already feeds Step 2 a shortlist that contains the recoverable answer where the catalog vocabulary allows; the probe itself says this is by design, not a defect.
- Phase A's visible result is mostly "three cases now report low-confidence." The wins (cleaner shortlists, smaller payloads, honest reporting) are real but invisible.
- The actual coverage lever is **P-4 vocabulary enrichment** - teaching existing entries the casual/informal, HR/layoff, and marketing-adjacent language they lack. That is what the newly-honest low-confidence cases are crying out for, and it expands what the tool can match rather than polishing what it already does. It was explicitly scoped out of phase A.

## The B / C framing (do not put phase B on a timer)

- **Phase A** (above): the full deterministic-layer fix. Small, low-risk, ready to implement from this doc.
- **Phase B** (deferred, may never be needed): polarity detection or the embedding index that the entry-recommender spec's Open Question 2 already defers. Justified **only** if the SKILL.md read layer proves insufficient in *real use*. The deterministic corpus cannot trigger this - after phase A, negation rank stays inverted (inherent), and the corpus only confirms that residual persists. Do not read "the inversion is still there" as a signal to build B; that inversion is expected and is what Step 2 exists to absorb.
- **Adjacent, separate:** P-3 (gold-singleton gate exception - the probe's `pragmatic-architect`-on-`postmortem` case) and P-4 (vocabulary enrichment, likely the higher-value thread of the two).

## If resumed

Phase A is fully specified above and implementable without re-investigation. Steps:

1. Add the negation caution to `skills/entry-recommender/SKILL.md` Step 2.
2. `STOPWORDS += {"no", "not", "all", "off", "something"}` in `recommend.py`. Do NOT add `took`, a strip-numbers rule, or `how`.
3. `python tests/eval/run_eval.py --verbose` -> inspect the drift -> confirm every delta matches the "measured behavior changes" list above and that the probe-named genuine picks survive -> update `baseline` and `baseline_date` in `tests/eval/situations.jsonl`.
4. Bump entry-recommender 0.2.0 -> 0.2.1 in SKILL.md `metadata.version` and `library.json`.
5. Add a CHANGELOG `[Unreleased]` entry; record the exposed P-4 gaps somewhere durable (here, or the backlog).
6. Full gate: `pytest`, `validate.py`, `validate-plugin-manifest.mjs`, `check-no-dashes.mjs`, `markdownlint-cli2`. Branch + PR (main is protected; rebase-merge).

Before starting, re-read finding 1 and 2: they are the reason phase A is modest, and the reason P-4 may be the better use of the same effort.

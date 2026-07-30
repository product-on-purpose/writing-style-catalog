---
title: Does it actually work?
description: The evidence that composed instructions produce output a blind reader can tell apart, including what the tests do not show.
---

Most prompt libraries assert that their named styles produce different writing. This one has
measured it, twice, with a negative control. This page is the record: what was run, what came
back, and what it does not prove.

## The claim, stated precisely

**Given two near-neighbour entries from the same axis, the catalog's per-entry instruction
phrasing steers a capable model into output that a blind judge can correctly attribute.**

That is narrower than "the catalog makes writing better," and deliberately so. It is the
claim the project rests on, and it is the one that was testable.

## Test 1: eight confusable pairs, blind (2026-05-31)

The hardest possible case was chosen on purpose: **within-axis near neighbours**, two per
axis, the pairs a learner would mix up. Not `sermon` against `changelog`, which anyone can
tell apart.

**Method.** For each pair, a real instruction was composed with the actual builder, holding
the other three axes and the topic constant, so the only variable is the entry under test.
Each output was generated **blind and independently**: a fresh agent received only its own
composed instruction and the topic, wrote about 300 words, and never saw its partner. A
separate agent then received the two unlabelled outputs in alternating order, the axis under
test, and the two candidate descriptions, and had to rate how distinguishable they were and
attribute each one. 24 agents in total, 16 generating and 8 judging.

**Result: 8 of 8 attributed correctly.** Chance is 1 in 256, about 0.4 percent.

| Pair | Axis | Distinguishability | Attribution |
| --- | --- | --- | --- |
| `coach` vs `friendly-mentor` | voice | clear | correct |
| `pragmatic-architect` vs `senior-consultant` | voice | **subtle** | correct |
| `candid` vs `confident` | tone | clear | correct |
| `warm` vs `empathetic` | tone | clear | correct |
| `socratic-inquiry` vs `dialectic` | style | dramatic | correct |
| `narrative-case-study` vs `chronological-narrative` | style | **subtle** | correct |
| `adr` vs `whitepaper` | format | dramatic | correct |
| `readme` vs `technical-reference` | format | clear | correct |

Bands: 2 dramatic, 4 clear, 2 subtle, **0 identical**.

The distinguishability rating matters independently of the attribution. Even if you discount
forced-choice attribution entirely, no pair was rated identical.

## Test 2: cross-vendor, a different judge (2026-06-23)

Test 1 used one model family at both ends, which leaves an obvious objection: a model can
recognise its own output conventions. So the second test changed the judge's vendor.

**Method.** Six expert-voice candidates, each rendered against its two nearest declared
confusables on one anchor topic. Generation by Claude Sonnet in isolated subagents, blind to
siblings. Judging by a **GPT-family** model, blind, one call per packet. Nine unique entries,
six packets, 18 judged slots.

**Result: 18 of 18 slots attributed correctly**, all six bands rated `clear`, no `subtle` and
no `identical`.

If the judge were guessing, matching all three samples within a packet has about a 1 in 6
chance; doing that in all six packets is roughly 1 in 46,000.

One detail is worth pulling out. `pragmatic-architect` vs `senior-consultant` was rated
**subtle** in Test 1. Under a different vendor's judge, with the entries now carrying explicit
`tells` and `failure_modes`, that same pair came back **clear**. The weakest seam got stronger
when the entries got more specific.

## The negative control: what makes this a test

A measurement that can only come back positive is a demonstration, not an experiment. So the
judge was also given work it *should* reject.

Deliberately caricatured renders were produced, each one over-hitting its own entry's register
past the point of usefulness. The judge flipped those from pass to **fail**, and named the
specific failure mode the entry itself documents.

This is the single most important result on this page. It establishes that the judge is
discriminating rather than agreeable, which is what licenses reading the positive results as
evidence at all.

A follow-up near-duplicate probe (2026-06-24) confirmed the bands are calibrated in the other
direction too: two renders of the *same* entry come back `subtle`/`same`, two genuinely
distinct entries come back `clear`/`different`.

## What this does not show

Stated plainly, because a proof asset that hides its limits is worth less than one that does
not.

1. **Attribution was description-assisted.** In both tests the judge saw each option's
   one-liner, and in Test 2 its `failure_modes` too. That is the gate as designed, but it
   makes attribution easier than a cold read. Read the results as *"given the descriptions,
   the judge matched every sample,"* not *"the prose alone is unmistakable."* The
   distinguishability bands do not depend on the forced choice and corroborate independently.
2. **Forced choice is easier than open identification.** A stronger test would ask the judge
   to name the entry from the full axis list rather than choose among two or three.
3. **Generation was single-tier.** Both tests generated with capable models. Nothing here
   shows a smaller model renders these distinctions as crisply. **This is the one measurement
   property still open**, and confirming it needs a second, cheaper generator tier.
4. **These are smoke tests, not a published eval.** Eight pairs and eighteen slots. Enough to
   retire the question of whether the premise holds; not enough to publish.
5. **No human raters.** Every judge was a model. Nothing here shows a non-expert human
   perceives the same differences.

## What changed after these tests

One caveat from the 2026-05-31 write-up has since been overtaken and should not be quoted
against the current build. It noted that composition was "literally string concatenation" that
ignored the `avoid_with` conflict data, and concluded the result credited individual entry
phrasings rather than the compositional layer.

The first half is no longer true: conflict-aware composition shipped in v0.3.0
([ADR 0016](https://github.com/product-on-purpose/writing-style-catalog/blob/main/docs/internal/adr/0016-conflict-aware-composition.md)),
and the builder now cross-checks selections and applies a voice, tone, style, format
precedence.

The second half still stands, and is the honest reading: **these results credit the per-entry
instruction phrasings.** The compositional layer is upside on top of a working base, and has
not itself been measured this way.

## Reproducing it

The harness is in the repository, and every run kept its records.

- `tools/gate_pilot.py` runs the render, present-blind, forced-choice-attribute loop.
- Per-run records carry the samples, the hidden mapping, the judge verdict, and the score, so
  any individual result can be re-checked rather than taken on trust.
- The blindness check and a seeded shuffle make runs reproducible; the judge never saw an
  entry id in a sample body.

Both tests ran on free infrastructure. No paid API and no embedding model were required.

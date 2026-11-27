---
title: What the paid half of the measurement layer would cost at 118 entries
status: decision note for the maintainer; nothing in it has been spent
date: 2026-11-26
owner: maintainer
audience: the maintainer, and any agent asked to build one of these three
related:
  - docs/internal/scaling-the-library-100x.md (frontier ideas 2, 3 and 6)
  - docs/internal/adr/0022-per-entry-distinguishability.md (the field all three write to)
  - docs/internal/agentic-generation-spec.md (the three paid-automation triggers)
  - docs/internal/release-plans/plan_v0.3.0/adherence-gate-spec.md (the gate these extend)
  - tools/distinguishability.py (the free harness, and where the measured token counts come from)
---

# What the paid half of the measurement layer would cost at 118 entries

**The answer, first: money is not the constraint.** A full-catalog distinguishability sweep costs
between **8 cents and $3.26** depending on the judge, or up to about **$14** on the pessimistic
reasoning-token assumption in section 2, and running all three ideas continuously for a year lands
between **$10 and a few hundred dollars**. The strategy document's cost table reads in the
thousands because it was written for a 6,000-entry endpoint with 72,000 samples; at 118 entries
and 1,176 samples the arithmetic is two orders of magnitude smaller, and this note derives it from
measurement rather than reusing those figures.

What the three ideas actually cost is **maintainer time and one unsolved measurement problem.**
Nothing below should be funded before the variance study in section 6, which costs under a dollar.

No API was called in producing this note, and no spend is authorized by it.

## 1. What is already free, and the baseline to beat

The judge architecture runs at zero marginal cost today and is validated:

- `tools/gate_pilot.py` plus the Codex companion judged 18 of 18 slots correctly, detected
  caricature, and bent its band scale correctly on a near-duplicate probe
  (`_agent-context/gate-pilot/CALIBRATION.md`).
- `tools/distinguishability.py` computes a per-entry band against a declared neighbor from the
  renders already committed under `examples/vertical-slices/`. Its first run judged 10 trials
  across four pairs, 10 of 10 attributed correctly, **for nothing**.

**So the baseline is not "no measurement". The baseline is a hand-driven sweep at $0.** Populating
the `distinguishability` field on all 118 entries once, at two trials each, is 236 in-session
subagent judge calls. That is large for one sitting and it is the same kind of work the breadth
waves already did free, in batches. Every priced option below has to beat $0-plus-attention, not
beat nothing.

**What the free path cannot do** is the thing all three ideas need: run inside CI. An in-session
subagent exists only while an agent session is open. A GitHub Actions job cannot summon one. That
single fact, not cost, is what makes these three ideas paid.

## 2. The measured unit: one judged comparison

| Quantity | Value | Measured or estimated |
|---|---|---|
| Judge prompt, per comparison | 5,002 to 14,818 characters, mean 8,542 | **Measured**, over the 10 real prompts of the 2026-11-26 run |
| Judge prompt in tokens | about 1,250 to 3,700, mean about 2,100 | Estimated from the characters at 4 characters per token; not a tokenizer count |
| Judge output, visible | the four-field JSON, 700 to 1,200 characters, so about 170 to 300 tokens | **Measured** character count, converted at the same ratio. **A floor, not the billed output** - see the reasoning-token note below |
| Render body, one passage | mean 2,997 characters, p90 5,297 | **Measured**, over all 1,176 committed renders |
| Render body in tokens | mean about 750, p90 about 1,320 | Estimated at the same ratio |
| Render prompt (`llm_instruction_phrasing` plus the task) | mean 696 characters of phrasing, so about 250 tokens in | **Measured** phrasing length; the task framing is estimated |

**For costing, one judged comparison is 2,200 input tokens and 250 output tokens.** The long tail
is real: a format pair, where both passages are full structured documents, runs nearly twice the
mean, so expect format-axis sweeps at about 1.7x.

**The output figure is the weakest number here, and it is a floor.** The judge ran at Codex's
`high` reasoning effort, and frontier APIs bill reasoning tokens as output. Reasoning does not
appear in the transcript, so it was not measured. The Codex CLI reported **1,757 to 36,810 total
tokens** across the twelve calls - a range too wide and too contaminated by the CLI's own system
prompt and hooks to decompose, which is why it is quoted rather than used.

So treat every output-side figure below as a floor and read it with a sensitivity range: at 10x
the visible output, 2,500 reasoning-plus-output tokens per comparison, a frontier judged
comparison costs about **$0.059** rather than $0.0138, and a 236-comparison field sweep costs
about **$14** rather than $3.26. That is the pessimistic end, and it does not change the
conclusion: a full sweep is still tens of dollars at worst. A `count_tokens` pass plus one real
API call with usage reporting would replace this range with a number, and that is the first
thing to do if a budget ever turns on it.

### Prices used

| Tier | Model | Input $/MTok | Output $/MTok | Source |
|---|---|---|---|---|
| Cheap | Claude Haiku 5.5 | 0.10 | 0.50 | Anthropic first-party, as of 2026-11-03 |
| Cheap, cross-vendor | `gpt-5-nano` | 0.05 | 0.40 | OpenAI pricing page, fetched 2026-11-26 |
| Cheap, cross-vendor | `gpt-5.6-luna` | 0.20 | 1.20 | OpenAI pricing page, fetched 2026-11-26 |
| Mid, cross-vendor | Gemini 3.8 Flash | 0.75 | 3.75 | Google pricing page, fetched 2026-11-26; rises to 1.50 / 7.50 on 2027-01-01 |
| Mid | Claude Sonnet 5.5 | 2.00 | 10.00 | Anthropic first-party, as of 2026-11-03 |
| Mid, cross-vendor | `gpt-5.6-terra` | 2.00 | 12.00 | OpenAI pricing page, fetched 2026-11-26 |
| Frontier | Claude Opus 5.5 | 4.00 | 20.00 | Anthropic first-party, as of 2026-11-03 |
| Frontier, cross-vendor | `gpt-5.6-sol` | 4.00 | 20.00 | OpenAI pricing page, fetched 2026-11-26 |

All three vendors price batch at 50 percent of standard. Batch is a good fit for a sweep and a bad
fit for a merge gate, which needs an answer in minutes.

**Cost of one judged comparison**, at 2,200 in and 250 out:

| Judge | Per comparison |
|---|---|
| `gpt-5-nano` | $0.00021 |
| Claude Haiku 5.5 | $0.00035 |
| `gpt-5.6-luna` | $0.00074 |
| Gemini 3.8 Flash | $0.0026 |
| Claude Sonnet 5.5 | $0.0069 |
| `gpt-5.6-terra` | $0.0074 |
| Claude Opus 5.5 / `gpt-5.6-sol` | $0.0138 |

**Cross-vendor is a design requirement, not a preference.** Every committed render was written by a
Claude-family model, and the gate's validity rests on the judge not sharing the generator's family.
That rules the Anthropic column out for judging today's renders and makes `gpt-5.6-luna` the
cheapest defensible screen and `gpt-5.6-sol` the frontier confirm. The Anthropic prices stay in the
table because they are the right column once generation moves to another vendor.

### The graph, measured

Sweep sizes come from the real `confusable_with` graph, not from 118 times one:

- **118** entries, every one of which declares at least one same-axis confusable neighbor. Only
  **89** of them, though, have an anchor topic on which that pair can be judged blind from the
  committed renders: 972 of the 1,416 (pair, topic) cells survive the leak check, and the 29
  entries with no usable cell are mostly formats whose prose names the format. A sweep priced
  below at 118 is therefore an upper bound on what today's renders can actually produce.
- **132** undirected confusable pairs; **264** directed edges.
- Mean degree **2.24**, median 2, max 9.
- The wider Gate 1 adversary set (tree siblings plus confusables) averages **6.95** and peaks at 14.

Two sweep definitions follow, and they differ by only 12 percent:

- **Field sweep** - what ADR 0022's field needs: one comparison per entry against its recorded
  neighbor. 118 pairs, 236 comparisons at two trials.
- **Graph sweep** - every declared edge measured: 132 pairs, 264 comparisons at two trials.

| Sweep | Comparisons | `gpt-5.6-luna` | Gemini 3.8 Flash | `gpt-5.6-terra` | `gpt-5.6-sol` |
|---|---|---|---|---|---|
| Field sweep, 2 trials | 236 | $0.17 | $0.61 | $1.75 | $3.26 |
| Graph sweep, 2 trials | 264 | $0.20 | $0.68 | $1.95 | $3.64 |
| Graph sweep, 6 trials | 792 | $0.59 | $2.05 | $5.86 | $10.93 |
| Tiered: luna screen, sol on 20 percent | 264 + 53 | - | - | - | **$0.93** |

**A full-catalog sweep is a rounding error at every tier.** That is the single most important number
in this note, and it is why "is it affordable" is the wrong question for all three ideas.

## 3. Idea 2 - the gate as a one-directional ratchet

**What it needs.** Three things, in dependency order: the `distinguishability` field (ADR 0022,
proposed, unratified); a CI-callable judge, which means `tools/adherence-gate.py` actually calling
an API, a vendor key in GitHub Actions secrets, and retry and timeout handling; and a stored
baseline per edge so "regressed" has a referent. The ratchet re-judges on every PR that touches an
entry, so it also needs path filters, or Dependabot PRs will spend money judging nothing.

**What a run costs.** Not a sweep. Editing entry X invalidates X's own measurement plus the
measurement of every entry that records X as its neighbor, which is the reverse-edge count: mean
2.24. So a one-entry PR is about 3.2 pairs, and at two trials about 7 comparisons. Add the frozen
golden-set regression that failure mode 4 calls for (the original 8 pairs, 16 comparisons) and a
typical PR run is **about 23 comparisons**.

| Scenario | Comparisons | `gpt-5.6-luna` | `gpt-5.6-sol` |
|---|---|---|---|
| One-entry PR, with golden-set regression | 23 | $0.017 | $0.32 |
| A breadth batch touching 10 entries | 80 | $0.06 | $1.10 |
| 100 such PRs in a year | about 2,300 | $1.70 | $32 |

**Cadence.** On every PR that touches `taxonomy/`, plus the golden set on every run. Nightly or
weekly is the wrong cadence: a ratchet that reports a regression three days after the merge that
caused it is a report, not a ratchet.

**What the maintainer gets.** The one thing no amount of care substitutes for: quality becomes
monotonic. A solo maintainer cannot hold 118 entries and a 132-edge neighbor graph in their head,
and the specific accident this prevents is concrete and already named in the backlog - sharpening
one entry's `confusable_with` block and blurring it against a different neighbor. Today nothing in
the repository would notice.

**Trigger fired.** Publishing provenance-pinned distinguishability scores, the third of the
factory spec's three. Arguably the first as well, if the ratchet is what makes a batch
hand-undrivable.

**The honest blocker, and it is not money.** The band moved under presentation order in the first
harness run: `dramatic` in one order, `clear` in the other, on identical passages. A ratchet that
fails the build on a band drop would fail builds for that reason. **Do not build this before the
variance study in section 6.** The study is under a dollar; the ratchet built on an unstable
instrument costs credibility, which is the asset this whole layer exists to protect.

## 4. Idea 3 - per-model phrasing variants and a public leaderboard

**What it needs.** More than the other two, and the generation half is the part the strategy
document understates. A leaderboard claims "model M can be steered into this catalog's styles",
which requires **M to write the passages**. In-session subagents can only be Claude-family, so
cross-vendor renders are paid generation - the one remaining paid item the gate-pilot calibration
note already identified. It also needs per-model phrasings, and the shape of that
change decides its cost. **Literally as the strategy document writes it** - turning
`llm_instruction_phrasing` from a string into a map - it narrows an existing type, which is
class C: an ADR, a migration of all 118 entries, and a `schemas/v2` contract path under ADR
0020. **An additive variant field instead** - keeping `llm_instruction_phrasing` as the
default string and adding an optional `llm_instruction_variants` object beside it - is class B
by the same reasoning ADR 0022 uses, needs no migration, and leaves every existing consumer
working. The additive shape is the one to pick, and it removes most of what made idea 3 look
structurally expensive. What remains expensive is the public commitment, not the schema.

**What a run costs.** Per model family: render 118 entries on one anchor topic, then judge each
against its neighbor at two trials.

| Per model family | Quantity | Cost |
|---|---|---|
| Renders (250 in, 750 out, x118) | 118 | $0.11 at luna, $0.95 at Sonnet-class, $1.89 at Opus-class |
| Judging (236 comparisons, frontier cross-vendor judge) | 236 | $3.26 |
| **One family, one topic** | | **about $3.40 to $5.20** |
| Four families, one topic | | **about $14 to $21** |
| Four families, all 12 anchor topics | about 5,700 renders, 11,300 comparisons | **about $200** |

**Cadence.** On a published leaderboard, quarterly, plus a re-run when a listed family ships a new
flagship. Monthly invites readers to treat judge noise as a model difference.

**What the maintainer gets.** The strongest version of the catalog's claim, and the one that
answers the smoke test's own first caveat ("strong model on both ends"). It converts the project
from a list of instructions into a citable benchmark for steerability. That is a genuine
positioning asset and the only one of the three ideas with outside-audience value rather than
internal-hygiene value.

**Trigger fired.** All three. It publishes scores, it is a batch too large to hand-drive, and a
public leaderboard invites outside contributions against it.

**The honest risk.** A leaderboard is a public commitment to re-run. A stale leaderboard is worse
than none, because it dates the project in the one place it claims to be current. Nothing here
should ship until the cadence is something a solo maintainer will still be doing in a year.

## 5. Idea 6 - versioned phrasings tracked against model releases

**What it needs.** Ideas 1 and 3 first - there is nothing to version until phrasings are per-family
and scores are stored. Then: a per-variant `last_validated_against` field, a trigger on model
release, and a `needs-rephrasing` flag when a band drops.

**What a run costs.** One field sweep per release, plus renders on the new model if it is a listed
family.

| Scenario | Cost |
|---|---|
| One release, judge-only re-sweep (236 comparisons, frontier cross-vendor) | $3.26 |
| One release, including 118 renders on the new model | about $4 to $5 |
| 10 releases in a year | **$33 to $50** |
| Same, on a tiered judge (luna screen, sol on 20 percent) | **about $10** |

**Cadence.** Event-driven, on release, not calendar-driven. A calendar sweep re-measures nothing
between releases; the whole premise is that phrasings decay against *models*, not against time.

**What the maintainer gets.** The answer to the question every prompt library on the internet
cannot answer: has this rotted? A dated per-entry band against a named model version turns silent
decay into a flagged entry. It is also the cheapest of the three to operate once ideas 1 and 3
exist, and the only one with a natural stopping condition, since it does nothing until a model
ships.

**Trigger fired.** The same third trigger, continuously.

## 6. Recommendation

**Spend nothing yet. Do the variance study first, and it is free.**

The first harness run showed the band is not order-invariant. Until the number of trials that
stabilises a band is known, every priced option above is building on an instrument whose precision
is unmeasured. The study:

- 10 pairs spanning all four axes, 10 trials each (5 presentation orders x 2 topics): **100
  comparisons**.
- On free in-session subagents: **$0**, a few batches of hand-driven work with the harness that
  already exists.
- On a paid cross-vendor judge, if a judge-variance arm is wanted too: **$0.07 at luna, $1.38 at
  sol**.
- Output: the trial count at which a pair's floor band stops moving, per axis. That number is the
  missing input to every table above, because it multiplies all of them.

**Then, in this order:**

1. **Ratify ADR 0022 and populate the field by hand**, free, on the pairs that matter - the
   historically `subtle` ones and anything the de-dup audit flagged. This gets the value of idea 1
   with no spend and no CI.
2. **Build the ratchet (idea 2) on a tiered cross-vendor judge**, once the variance study says how
   many trials a stable verdict needs. Budget **under $50 a year** at a hundred PRs, screened on
   `gpt-5.6-luna` and confirmed on `gpt-5.6-sol`. This is the highest value per dollar of the
   three by a wide margin, because it protects the asset rather than advertising it.
3. **Treat idea 6 as a small addition to the ratchet**, not a project: once CI can judge, a
   release-triggered sweep is another workflow trigger and **$33 to $50 a year**.
4. **Hold idea 3 until there is an audience for it, and if it is built, build it additively.**
   Its tokens are cheap, and the class C schema change is avoidable: an optional
   `llm_instruction_variants` field beside the existing string is class B and needs no
   migration. What is not avoidable is the public commitment to keep re-running a leaderboard,
   and a stale leaderboard dates the project in the one place it claims to be current. That is a
   launch project, and it should follow a usage signal rather than precede one - the same
   reasoning the roadmap used to defer the 120-entry expansion.

**The number worth carrying out of this note:** every judged comparison in this catalog costs
between two hundredths of a cent and about six cents, and the whole catalog sweeps for less than
the price of a lunch even on the pessimistic assumption. So the decision was never a budget decision. It is a decision about whether to
accept CI that calls a vendor API, and about whether the instrument is steady enough to block a
merge on. The first is a preference. The second is a question with a free experiment attached, and
that experiment should run before any card is added to any secret store.

## 7. What is measured and what is estimated

**Measured in this repository, on 2026-11-26:** the catalog size (118 entries), the confusable
graph (132 undirected pairs, 264 directed edges, mean degree 2.24, max 9), the Gate 1 adversary set
size (mean 6.95, max 14), judge prompt lengths over 10 real prompts (5,002 to 14,818 characters), the leak-check coverage
(89 of 118 entries, 972 of 1,416 cells),
render body lengths over all 1,176 committed renders (mean 2,997 characters, p90 5,297),
`llm_instruction_phrasing` lengths (mean 696 characters), the 10-of-10 attribution result, and the
band's instability under presentation order.

**Fetched on 2026-11-26:** the OpenAI and Google per-token prices, from their pricing pages. The
Anthropic prices are from the bundled API reference, dated 2026-11-03; they are the oldest input
here and worth re-checking before anyone commits a budget.

**Estimated, and load-bearing:** the 4-characters-per-token conversion, which is an approximation
and not a tokenizer count - a `count_tokens` pass over the real prompts would tighten every dollar
figure by some tens of percent, in either direction. **Output tokens are the weakest input**: the
measured figure is visible JSON only, reasoning tokens are billed as output and were not measured,
and section 2 carries a 10x sensitivity range for that reason. Also estimated: the 20 percent escalation rate
in the tiered judge, the 100-PRs-per-year and 10-releases-per-year cadences, and the number of
trials a stable band needs, which is **unknown** and is the one estimate section 6 exists to
replace.

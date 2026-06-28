---
title: Agentic Generation Factory - spec and implementation plan
status: implemented and in use (Stream-B breadth done; Wave-1 promotion done; v0.4.0 released)
owner: maintainer
audience: humans and agents extending or operating the factory
related:
  - tools/agentic/README.md (how to run each harness)
  - docs/internal/release-plans/promotion-and-release-runbook.md (the operational steps)
  - docs/internal/release-plans/stream-b-breadth-status.md (the breadth inventory + gate record)
  - AGENTS.md (the repo-wide agent reference)
---

# Agentic Generation Factory: spec and implementation plan

This is the design-of-record for how the catalog produces and gates content with
subagents. It complements the runnable harnesses in `tools/agentic/` (the "how")
with the "what, why, and the contracts" (this document). It is tracked, so the
production method is legible from a clean clone - not only from the agent's
gitignored working notes.

## 1. Purpose and principles

The catalog's value is a set of writing instructions that are **distinguishable**
(each named value produces visibly different output) and **composable**. Growth must
preserve both. Three standing principles:

1. **Gated, not trusted.** No content is published un-gated. Generation is cheap;
   the moat is the gate. Every stage has an explicit, reproducible check.
2. **Free by default.** Generation (isolated subagents) and gating (a cross-vendor
   judge) both run in-session at zero marginal API cost. The paid-automation decision
   is fenced to three triggers and has never fired: a batch too large to hand-drive,
   admitting unattended outside-contributor PRs, or publishing provenance-pinned
   distinguishability scores.
3. **Drafts are reversible; stable is earned.** New entries start `review_status:
   draft`. Promotion to `stable` is a maintainer decision and carries a hard cost
   (Gate 2: render on all 12 anchor topics). Nothing is advertised as curated until
   it is stable.

## 2. The stages and their harnesses

The factory is six stages. Demonstration content (samples, diff-pairs) skips the
distinguishability stages; new entries pass through all of them.

| Stage | Purpose | Harness | Gate |
|---|---|---|---|
| 1. Scaffold | place the unit in the tree with valid frontmatter | (deterministic; folder + schema) | `validate.py` |
| 2. Generate | write the prose | `tools/agentic/generate.js` (new entries); `tools/agentic/promote.js` (worked samples) | - |
| 3. Distinguishability | each new entry is distinct from its neighbor | distinguishability gate prompt (section 4) | cross-vendor (Codex) |
| 4. De-dup / diversity | no cross-batch collisions | `tools/agentic/dedup.js` | high-effort family-cluster audit |
| 5. Spot-review / calendar | human judgment; dated-content consistency | date gate prompt (section 4) + maintainer review | per-format calendar check |
| 6. Publish | validate, index, render, manifest, commit | `validate.py`, `build-indexes.py`, `gen-site.mjs`, `promote.py` | deterministic + CI |

Remediation of any flag is applied with `tools/agentic/remediate.js` (a precise
per-file fix-applier), then re-validated, and genuine quality findings are re-gated.

## 3. Harness contracts

Each harness is a parameterized template. Inputs are an array at the top of the file;
the orchestrator returns a compact summary.

### `generate.js` - new draft entries

- **Input:** `CANDIDATES[]`, each `{ id, name, domain, family, dp, one_liner, concept,
  pairs_well_with, avoid_with, confusable_with, typical_voices, typical_tones }`.
- **Invariant:** every cross-reference id MUST already exist (the deterministic gate
  rejects dangling refs). `pairs_well_with` must fit the format's nature - never an id
  the format's own anti-patterns will forbid (the author supplies the fixed list, so a
  conflict is an authoring error, not the agent's).
- **Output:** one `taxonomy/formats/<id>/ENTRY.md` per candidate, `review_status:
  draft`, mirroring the `adr` template. The agent reads each confusable neighbor's
  ENTRY.md before describing it.
- **Post:** `validate.py` + `build-indexes.py`, then the distinguishability gate.

### `dedup.js` - whole-corpus audit

- **Input:** `GROUPS[]`, one or more family clusters with members tagged (S)/(D).
  Regenerate from the live family map (read ENTRY.md frontmatter, not taxonomy.json).
- **Output:** `{ flagged_pairs, quality_notes }` (structured, severity-sorted).
- **Why by family:** the per-entry gate only compares an entry to its one declared
  neighbor; same-family collisions between entries are invisible to it. The family
  cluster is the slot competitors share, so it is the right audit granularity.

### `remediate.js` - precise fix-applier

- **Input:** `FIXES[]`, each `{ id, instruction }` where the instruction quotes the
  exact text to change and states the replacement. One file (or one reciprocal pair)
  per fix. Used for de-dup fixes, date fixes, or any surgical batch.
- **Output:** the edits applied, one isolated agent per file. Always re-validate after.

### `promote.js` - render across anchor topics

- **Input:** `FORMATS[]`, the draft format ids to render. `TOPICS` is the fixed 12
  (mirrors `anchor_topics.py`).
- **Output:** `examples/vertical-slices/<topic>/format-<fmt>.md` for all 12 topics per
  format. Each cell inherits the topic's shared scenario by reading three existing
  samples on that topic. Forced combos (eng format on a contemplative topic) apply the
  format's structure to the topic's situation.
- **Invariant:** run while the formats are still `draft` (Gate 2 exemption keeps
  validate green during the render).

### `promote.py` - guarded flip (runnable CLI)

- **Input:** entry ids (or `--all-ready`). `--check` for a dry run.
- **Invariant (the whole point):** flips to stable ONLY if every named entry already
  renders on all 12 topics; otherwise it changes nothing and reports what is missing.
  It is **transactional** - it stages every rewrite in memory and writes the files
  together, rolling back any written file if a later write fails - so a promotion
  either fully applies or leaves the tree unchanged, and never leaves main red on
  Gate 2. It also flips only the single column-0 `review_status: draft` line in the
  frontmatter (not a lookalike inside a block scalar) and aborts on a duplicate id.

## 4. The two gate prompts (canonical text)

These dispatch a subagent per unit and return findings. They are prompts, not scripts,
because the judgment is the model's.

### 4a. Distinguishability gate (one `codex:codex-rescue` agent per generation batch)

> You are an adversarial cross-vendor reviewer. N new DRAFT format entries were
> generated. For EACH, read the entry AND its declared `confusable_with` neighbor's
> own ENTRY.md, then check:
> - **A Neighbor accuracy:** the "Often confused with" section (and any anti_pattern
>   naming the neighbor) describes the neighbor consistently with how that neighbor's
>   ENTRY.md describes itself, and states crisply how THIS format differs.
> - **B failure_mode discipline:** each failure_mode is THIS format over-hitting its
>   own register, never a generic misuse, a rule violation, or a neighbor move (those
>   belong in anti_patterns), and never names a neighbor format.
> - **C pairs consistency:** nothing in `pairs_well_with` is something the entry's own
>   description or anti_patterns forbid.
> - **D intra-batch collisions:** entries in the batch that share a neighbor or a slot
>   are distinguishable from each other.
> - **E integrity:** no fabricated statistics, no invented named authority/firm/person
>   presented as real.
> - **F dashes:** no U+2014 or U+2013.
> Return, per entry, PASS or REVISE with a numbered list of concrete minimal fixes
> (quote the offending text, state the exact correction). Do not edit files.

The two recurring catch types are **neighbor mischaracterization** (the agent guessed
the neighbor instead of reading it) and **pairs-consistency** (a pair the entry's own
anti-pattern forbids). Both are designed against in `generate.js` (read-neighbor step;
author-supplied fitting pairs), which drove the revise-rate from 6/6 to about 1/6.

### 4b. Date gate (one `general-purpose` agent per dated format)

> Read these 12 files (one format across 12 topics). For EACH, check ONLY internal
> consistency: (1) any stated weekday matches its calendar date (verify 2025/2026
> against the real calendar); (2) any stated duration / week-count / period matches its
> own start and end; (3) no em/en-dashes; (4) no fabricated statistic attributed to a
> real named entity. Be conservative - flag only genuine internal contradictions, not
> stylistic choices or forced topic-format pairings. For each flagged file: the path,
> the conflicting quote, and the exact correction. Report only.

Apply to any format whose samples carry dates or timelines (incident-report,
release-notes, postmortem, retrospective, status-report-like, decision-log-like).
About 30% of dated samples carry a slip; this is the single persistent quality risk in
rendered content and is worth a dedicated calendar pass every promotion.

## 5. Invariants and counters

- **Gate 2 atomicity.** `validate.py` requires every `stable`/`reference-quality`
  entry to render on all 12 anchor topics. Promotion = render (while draft, exempt) ->
  flip (`promote.py`, guarded). Never flip first.
- **Counter locations** (update together in the promoting PR):
  - `README.md`: four lines - the "every one of the N stable entries" worked-examples
    line; the "M format templates (plus K draft...)" line; the "N stable taxonomy
    entries (15 Voice, 15 Tone, 15 Style, X Format)" line (the "15 each" framing breaks
    once Format > 15); and the "Y worked examples ... 130 diff-pairs and 14 recipes"
    line. README counts vertical-slice samples only.
  - `library.json` + `.claude-plugin/plugin.json`: "Ships N curated entries, T worked
    examples ...". T counts vertical + horizontal; the manifest validator enforces
    `plugin.json` == `library.json`.
- **`taxonomy.json` is a slim index** (no `confusable_with`; nested domain/family).
  Read frontmatter from ENTRY.md when scripting an inventory; use pyyaml, and note that
  `review_status` is the last frontmatter field (after block scalars that may contain a
  `---` line - parse by the column-0 `---`, as `tools/promote.py` does).

## 6. Implementation plan and extension

- **Adding a harness:** mirror an existing template's header contract, take its input
  as a top-of-file array, return a compact summary, and document it in the README +
  this spec. Keep prose fields double-quoted or backtick (the apostrophe gotcha).
- **A deterministic date lint** (future, optional): a heuristic `validate.py` check
  could flag weekday-vs-date mismatches in samples it can parse, reducing reliance on
  the date-gate agent. Natural-language date extraction makes a perfect deterministic
  check hard; treat it as a lint, not a gate.
- **Other axes:** `promote.py` is already axis-general - it reads each entry's `axis`
  from frontmatter and keys samples as `<axis>-<id>.md`, so it promotes Voice/Tone/Style
  entries too. `promote.js` as committed is **format-oriented** (it hardcodes
  `taxonomy/formats`, `format-<id>.md`, and `axis: format`); extend it to another axis
  by parameterizing the axis in its paths and the sample frontmatter.

## 7. Status (2026-06-28)

- **Breadth:** Stream-B produced 57 draft format candidates (batches 1-10), each
  gated. Format axis 15 -> 72.
- **De-dup:** whole-corpus audit run; corpus clean apart from a few fixed items.
- **Promotion:** Wave 1 (14 PM/builder-core formats) promoted to stable, each rendered
  across 12 topics and date-gated. Format axis 15 -> 29 stable; catalog 60 -> 74
  curated entries. Released as **v0.4.0**.
- **Next:** Wave 2 (23 professional/public drafts), then Hold-20
  (personal/ceremonial/contemplative). See the promotion proposal under
  `docs/internal/release-plans/`.

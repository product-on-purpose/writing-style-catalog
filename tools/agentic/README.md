# `tools/agentic/` - the agentic generation factory

This directory is the catalog's **production engine**: the harnesses that generate,
gate, de-duplicate, render, and promote catalog content using subagents, for free,
under deterministic and cross-vendor gates. It is the executable form of the
hand-driven generation plan; the design rationale and contracts live in
[`docs/internal/agentic-generation-spec.md`](../../docs/internal/agentic-generation-spec.md),
and the step-by-step operational runbook lives in
[`docs/internal/release-plans/promotion-and-release-runbook.md`](../../docs/internal/release-plans/promotion-and-release-runbook.md).

## Why this exists

The catalog grows by adding worked content (examples, diff-pairs, vertical slices)
and, more carefully, new entries. Doing that at any scale by hand is slow and
inconsistent; doing it with one ungated LLM call is unsafe (a bad entry dilutes the
catalog's whole reason to exist). The factory threads that needle: **isolated
subagents do the writing** (keeping prose out of the orchestrator's context and
letting each unit be blind to its siblings), and **layered gates do the checking**
(a deterministic schema gate, a cross-vendor distinguishability gate, a whole-corpus
de-dup gate, and - for dated content - a calendar gate). Every stage runs on
in-session subagents at zero marginal API cost; no paid CI is required.

## Two kinds of artifact here

1. **Runnable tooling** - `../promote.py` is a normal Python CLI (guarded, atomic
   draft -> stable promotion). Run it directly.
2. **Workflow templates** - the `*.js` files are **not** standalone scripts. They run
   only through the Claude Code **Workflow tool**: an agent invokes
   `Workflow({ scriptPath: "tools/agentic/<file>.js" })`. They are parameterized
   templates: edit the input array at the top, then invoke. Each has a documented
   header explaining its contract.

## The harnesses

| Harness | Stage | What it does |
|---|---|---|
| [`generate.js`](generate.js) | Generate | Writes N new draft format `ENTRY.md` files, one read-its-neighbor agent per candidate, mirroring the `adr` template. |
| [`dedup.js`](dedup.js) | Audit | Whole-corpus distinguishability + quality audit, one auditor per **family cluster**. Returns structured flags. |
| [`remediate.js`](remediate.js) | Remediate | Applies a precise per-file fix-list, one agent per file. General-purpose (de-dup fixes, date fixes, any surgical batch). |
| [`promote.js`](promote.js) | Render | Renders N formats across all 12 anchor topics (12*N worked samples), each inheriting its topic's shared scenario. |
| [`../promote.py`](../promote.py) | Promote | Flips fully-rendered drafts to stable, atomically and guarded against the Gate 2 sample-count rule. |

Two gates are **agent prompts, not scripts** (they dispatch a subagent per unit and
return findings you feed to `remediate.js`). The canonical prompt text is in the spec;
short forms below.

## The loops

### A. Add new entries (breadth)

```
edit generate.js CANDIDATES (pre-validate every cross-ref id; pick neighbor-fitting pairs)
-> Workflow(generate.js)
-> python tools/validate.py && python tools/build-indexes.py
-> dispatch the DISTINGUISHABILITY GATE (one codex:codex-rescue agent per batch; prompt below)
-> apply fixes with remediate.js (or targeted edits)
-> node scripts/gen-site.mjs && (cd site && npm run build)
-> bump the two README draft-count lines -> commit -> PR -> green -> merge
```

New entries always start `review_status: draft`. They are never promoted by this loop.

### B. De-duplicate the corpus (run after breadth, before promotion)

```
regenerate dedup.js GROUPS from the current family map
-> Workflow(dedup.js)
-> feed flagged_pairs + quality_notes into remediate.js -> Workflow(remediate.js)
-> python tools/validate.py
-> RE-GATE the medium/high pairs with a focused cross-vendor check (confirm RESOLVED)
-> build -> commit -> PR
```

### C. Promote a wave (draft -> stable)

```
edit promote.js FORMATS (the approved wave)
-> Workflow(promote.js)                                  # render 12 samples per format
-> python tools/validate.py                              # green: drafts are Gate-2-exempt
-> DATE GATE the dated formats (incident-report, release-notes, postmortem, retrospective,
   and any with timelines): one date-checker agent per format (prompt below)
-> feed the date flags into remediate.js -> Workflow(remediate.js)
-> python tools/promote.py rfc postmortem ...            # atomic flip, guarded
-> python tools/build-indexes.py
-> update counters: README (x4) + library.json/plugin.json curated counts
-> python tools/validate.py                              # Gate 2 now ACTIVE for the wave
-> node scripts/validate-plugin-manifest.mjs && (cd site && npm run build)
-> commit -> PR -> green -> merge
```

See the runbook for the exact counter edits and the release tag.

## The two gate prompts (dispatch a subagent per unit)

**Distinguishability gate** (one `codex:codex-rescue` agent per generation batch).
For each new entry, the agent reads the entry AND its declared `confusable_with`
neighbor's `ENTRY.md`, then checks: (A) neighbor accuracy - the disambiguation
describes the neighbor as the neighbor describes itself; (B) failure_mode discipline -
each is the format over-hitting its own register, never a misuse or a neighbor move;
(C) pairs consistency - no `pairs_well_with` id the entry's own anti_pattern forbids;
(D) intra-batch collisions; (E) integrity - no fabricated stats or invented
authorities; (F) no em/en-dashes. It returns PASS or REVISE with concrete fixes. Full
prompt: the spec.

**Date gate** (one `general-purpose` agent per dated format). The agent reads that
format's 12 samples and verifies, against the **real calendar**, that every stated
weekday matches its date, every duration/week-count matches its own start and end,
no em/en-dashes, no fabrication. It returns flagged files with the exact correction.
Roughly 30% of dated samples have a slip; this is the one persistent quality risk in
rendered content. Full prompt: the spec.

## Gotchas (read before editing a template)

- **JS apostrophes:** prose fields (concept, one_liner, instructions) with apostrophes
  MUST be double-quoted JS strings or backtick template literals. YAML-style `''`
  doubling inside a single-quoted JS string is a parse error - the most common
  self-inflicted failure.
- **Gate 2 is atomic:** a format flipped to stable with fewer than 12 samples reds
  `validate.py`. Always render first (drafts are exempt), then flip with `promote.py`.
- **Don't read `taxonomy.json` for inventories:** it is a slim index that omits
  `confusable_with` and nests `domain`/`family`. Read frontmatter from `ENTRY.md`.
- **Preserve newlines** when editing files programmatically: PowerShell `Set-Content`
  CRLF-converts the whole file. `promote.py` and the agents preserve line endings.
- **Anchor topics** are defined once in `tools/anchor_topics.py`. The 12 in
  `promote.js` mirror it; keep them in sync.
- **No paid CI:** the whole factory runs on in-session subagents + the cross-vendor
  judge, for free. The paid-automation decision is fenced to three triggers (a batch
  too large to hand-drive, unattended contributor-PR admission, or published
  provenance-pinned distinguishability scores); none have fired.

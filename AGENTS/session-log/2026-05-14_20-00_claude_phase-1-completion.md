---
session_id: 2026-05-14_20-00_claude_phase-1-completion
date: 2026-05-14
time_range: "intermittent across the day"
model: claude-sonnet-4-6
mode: dispatch (heavy use of parallel subagents)
branch: main
base_commit: 8c58e88
head_commit: 9f5c7de
commits_authored: 14
files_changed: 203
insertions: 19152
deletions: 21
status: complete
pushed_to_remote: true
---

# Session Log: Phase 1 Completion

## Summary

Carried the Writing Style Library from the Phase 0 foundation (20 entries, 20 examples, 8 stub docs, ADRs in the root) to a Phase 1 structurally complete state (60 entries, 135 examples spanning two anchor topics, 5 horizontal-slice recipes, 4 diff-pairs, fully fleshed public docs, repo-level CLAUDE.md, CODE_OF_CONDUCT.md, SECURITY.md).

Heavy use of parallel subagents: four-axis dispatching for content generation, with the main thread coordinating, validating, fixing, and committing. The validator gained a new example-schema check that caught a real bug on its first run.

Branch `feat/milestone-1-foundation` was fast-forward-merged into `main` partway through the session. All 14 session commits are now on `origin/main`.

---

## Work Completed (commits in chronological order)

### dff6d12: Move adr/ to docs/internal/adr/

The ADR directory was reorganized under `docs/internal/`. Used `git mv` to preserve history. Updated AGENTS.md and README.md path references.

### a657401: Track internal docs, session log, UI mockups

Brought six previously-untracked files in `docs/internal/` plus the prior session log under `AGENTS/` into version control. These were reference materials marked read-only in AGENTS.md but had never been committed.

### f468b3a: Add build-indexes.py

New script walks every `ENTRY.md` under `taxonomy/` and writes `taxonomy.json` (machine-readable index) plus `docs/reference/index.md` (Markdown table grouped by axis). Wired into `.github/workflows/validate.yml` with a `git diff --exit-code` staleness check and into `.pre-commit-config.yaml` for local runs.

### d54834b: Preserve taxonomy.json timestamp

Quick fix for the staleness check: without timestamp preservation, the CI diff would false-positive on every push because `generated` changed every run. Modified the script to reuse the prior timestamp when entries are unchanged.

### a4a71d4: Add CLAUDE.md, CODE_OF_CONDUCT.md, SECURITY.md

Repo-level Claude Code instructions (brief, points to AGENTS.md for full reference), Contributor Covenant 2.1 code of conduct, and a vulnerability reporting policy.

### efd2780: 20 new taxonomy entries (catalog reaches 40)

Dispatched 4 parallel subagents (one per axis), each writing 5 entries:

- Voices: executive, product-thinker, technical-writer, coach, direct-communicator
- Tones: instructional, empathetic, playful, urgent, celebratory
- Styles: how-to-tutorial, executive-summary, narrative-case-study, layered-disclosure, decision-log
- Formats: email, meeting-notes, one-pager, daily-standup, technical-reference

**Bug surfaced and fixed in this commit:** the `technical-reference` format entry has a Markdown table inside its `canonical_template` block scalar. The table separator row `|------|...|` contains `---` as a substring, which the `_extract_frontmatter` function was matching via `content.split("---", 2)`, truncating the frontmatter before `pairs_well_with`. Replaced with `re.split(r"(?m)^---[ \t]*$", ...)` in both `validate.py` and the duplicate parser in `skills/writing-instruction-builder/scripts/build-instruction.py`.

### 4124337: 20 examples for the new entries on async-standups

Dispatched 4 parallel agents to render the new 20 entries on the existing `async-standups` anchor topic. Each agent reused the established scenario (11 engineers, 4 timezones, Priya's 401 incident, 14-minute standup with about 4 minutes of signal).

### MERGE: feat/milestone-1-foundation into main

Fast-forward merge of 18 commits into `main`, which had been at just the initial commit. Preserved every commit's identity in history.

### fcc7ccb: Replace 8 stub docs with real content

Replaced one-paragraph placeholders in eight public docs with full pages (400-800 words each), authored sequentially for cross-document coherence:

- docs/concepts/composition.md
- docs/concepts/glossary.md
- docs/how-to/pick-voice.md
- docs/how-to/add-entry.md
- docs/design-standards/voice-and-tone.md
- docs/design-standards/naming-conventions.md
- docs/design-standards/style-tells.md
- docs/governance/contribution-process.md

### 0550460: Second anchor topic, 40 morning-routine examples

Dispatched 4 parallel agents (10 examples per agent) to render all 40 existing entries on a second anchor topic: "How to start a morning routine." Chosen to exercise parts of the catalog the workplace-decision topic does not flatter (pastoral, reverent, devotional-reflection, warm, coach, empathetic).

### e0fb1d4: Example schema validation + 20 entry_id fixes

Added `check_examples()` to `validate.py` as the eighth check. It walks every `.md` file under `examples/`, parses frontmatter, validates against `schemas/example.schema.json`, and cross-checks that `entry_id` resolves to a known entry and that the declared `axis` matches the entry's actual axis.

The check immediately caught a real bug: 20 of the morning-routine examples had axis-prefixed `entry_id` values (e.g., `tone-candid` instead of `candid`). Two of the four agents had prepended the axis. Fixed all 20 via a PowerShell one-liner and committed alongside the validator change.

### 8c50565: 20 more entries (catalog reaches 60, Phase 1 target hit)

Dispatched 4 parallel agents to write 5 more entries per axis:

- Voices: researcher, journalist, storyteller, senior-consultant, caregiver
- Tones: skeptical, confident, diplomatic, confessional, resolute
- Styles: socratic-inquiry, frequently-asked-questions, chronological-narrative, dialectic, definitional
- Formats: readme, changelog-entry, status-report, tweet-thread, whitepaper

### 9cf81c0: 5 horizontal-slice recipes

Dispatched 5 parallel agents (one per recipe), each authoring 1 README plus 3 worked example files:

1. architect-candid-adr (rest-to-graphql, kubernetes-staging, sunset-legacy-auth)
2. pastoral-warm-devotional (discipline-of-rest, forgiveness-daily-practice, hearing-god-in-silence)
3. columnist-candid-blog (one-on-one-agendas, against-quarterly-okrs, managers-should-code)
4. mentor-encouraging-tutorial (first-pull-request, development-environment-setup, writing-your-first-test)
5. operator-direct-runbook (restart-auth-service, investigate-p99-latency, database-failover)

Modified `validate.py` to skip `README.md` files in the example-schema check. Example files use the recipe's voice as `entry_id` and capture the full combination in the optional voice_id / tone_id / style_id / format_id fields the schema already exposes.

### 6b325c1: Vertical-slice examples for the newer 20 entries (both topics)

Closed the demonstration gap: dispatched 4 parallel agents (10 examples per agent: 5 entries times 2 topics) to render the new 20 entries on both `async-standups` and `morning-routine`. Prompts explicitly called out the entry_id bug from the e0fb1d4 batch to head off repetition. No mis-prefixed IDs this time.

After this commit: every entry in the catalog has at least one worked example on each anchor topic.

### 9f5c7de: Diff-pair generator and 4 seed diff-pairs

Built `tools/diff-pair-generator.py`. The tool reads two existing vertical-slice example files that share a topic and differ on exactly one axis, then composes a comparison artifact: frontmatter naming the pair and the axis varied, a "What to notice" framing section, and both example bodies rendered in full.

Generated 4 seed diff-pairs (one per axis, two per topic):

- async-standups/voice-pragmatic-architect-vs-pastoral.md
- async-standups/tone-candid-vs-warm.md
- morning-routine/style-how-to-tutorial-vs-narrative-case-study.md
- morning-routine/format-devotional-entry-vs-technical-reference.md

Also: `validate.py` now skips files under `examples/diff-pairs/` in the example-schema check, because diff-pair files use a different frontmatter shape (entry_a / entry_b rather than a single entry_id).

---

## Decisions Made

**Move ADRs under docs/internal/ rather than keep them at root.** The mkdocs site already excludes `docs/internal/` from the public build. ADRs in this project are governance artifacts, not public docs.

**Repo-level CLAUDE.md is brief and points to AGENTS.md.** AGENTS.md remains the canonical reference. The repo-level CLAUDE.md adds Claude Code-specific quick commands and hard rules without duplicating content.

**Two anchor topics, not one.** Second anchor "How to start a morning routine" was chosen to exercise voices, tones, and formats that the workplace-decision topic does not flatter.

**Horizontal-slice example files use voice as entry_id, full combination in optional fields.** The example schema requires `entry_id` (singular). Resolved by using voice as the canonical entry_id and capturing the full combination in the optional voice_id, tone_id, style_id, format_id fields.

**Diff-pair files are skipped by example-schema validation.** Diff-pair frontmatter has `entry_a` and `entry_b` rather than a single `entry_id`. Rather than retrofit the example schema, `validate.py` skips files under `examples/diff-pairs/`.

**Validate.py skips README.md files in examples/.** Horizontal-slice recipe READMEs are documentation, not examples.

**Preserve `generated` timestamp in taxonomy.json when entries are unchanged.** Without this, the CI staleness check would false-positive on every push.

---

## Verification

| Check | Method | Result |
|-------|--------|--------|
| All 8 validate.py checks pass | `python tools/validate.py` on HEAD | PASS |
| Slug format | check 1 | 0 errors |
| ENTRY.md presence | check 2 | 0 errors |
| Frontmatter parseable | check 3 | 0 errors |
| JSON Schema validation | check 4 | 0 errors (60 entries) |
| Cross-reference integrity | check 5 | 0 errors |
| No em-dash, no en-dash | check 6 | 0 errors |
| Example schema (new this session) | check 7 | 0 errors (135 examples) |
| No draft entries | check 8 | 0 warnings |
| `taxonomy.json` is current | `build-indexes.py` then `git diff --exit-code` | clean |
| Commit history | `git log --oneline 8c58e88..HEAD` | 14 commits, conventional |
| Branch pushed to remote | `git push origin main` | success |

---

## Catalog Final State

| | Voices | Tones | Styles | Formats | Total |
|---|---|---|---|---|---|
| Entries | 15 | 15 | 15 | 15 | 60 |
| Examples on async-standups | 15 | 15 | 15 | 15 | 60 |
| Examples on morning-routine | 15 | 15 | 15 | 15 | 60 |
| Horizontal-slice examples | | | | | 15 |
| Diff-pair files | | | | | 4 |

Plus 8 ADRs, 11 fully authored public docs, 11 root files, 5 recipe READMEs. Total substantive documents: about 240.

---

## Outstanding Items

### Known non-blockers

- Pre-existing internal UI mockup contains em-dashes. `docs/internal/ui-mockups/04-brand-voice-builder.html` is internal/read-only per AGENTS.md and not in validate.py's scan scope. Deferred.
- `jsonschema.RefResolver` is deprecated. Migration to the `referencing` library is convenient but not urgent.
- Hand-rolled YAML parser cannot handle nested objects. Only affects `typical_length` in format entries, which is omitted by convention.
- No diff-pair schema check. Diff-pair files are skipped by validate.py rather than checked against their own schema.

### Phase 2 territory (out of scope for this session)

- TypeScript SDK (`packages/ts-sdk/`)
- Python SDK (`packages/py-sdk/`)
- MCP server (`packages/mcp-server/`)
- Composer SPA (`packages/composer-app/`)
- Eval harness using Promptfoo

---

## Evidence Index

| Claim | Evidence |
|---|---|
| All 8 validate.py checks pass | `python tools/validate.py` from repo root |
| 60 entries indexed correctly | `docs/reference/index.md` and `taxonomy.json` |
| 135 examples present | `validate.py` output: "135 examples checked" |
| Both anchor topics have full vertical slices | `examples/vertical-slices/async-standups/` and `morning-routine/` directory listings |
| 5 horizontal-slice recipes | `examples/horizontal-slices/` directory listing |
| 4 diff-pairs cover all four axes | `examples/diff-pairs/` directory listings |
| Parser bug fix | `tools/validate.py` and `skills/writing-instruction-builder/scripts/build-instruction.py` |
| Example schema bug surfaced and fixed | Commit `e0fb1d4` |
| Branch pushed to remote | `git push origin main` output: `875c00e..9f5c7de  main -> main` |

---

## Continuation Prompt

```
Context: Writing Style Library is on branch `main` at HEAD `9f5c7de`, pushed to
origin. Phase 1 catalog work is structurally complete: 60 entries (15 per axis),
135 examples spanning two anchor topics (async-standups and morning-routine), 5
horizontal-slice recipes with worked examples, and 4 diff-pairs covering all four
axes. All 8 validate.py checks pass. Public docs are fully authored. Repo-level
CLAUDE.md, CODE_OF_CONDUCT.md, SECURITY.md are in place.

Next-session candidate work, in rough priority order:

1. PHASE 2 TOOLING. The catalog is now rich enough to consume programmatically.
   Phase 2 deliverables from the strategy brief are: TypeScript SDK, Python SDK,
   MCP server, Composer SPA. Each lives under `packages/`. Pick one to start.

2. EXTEND THE NO-EM-DASH CHECK TO DOCS. `validate.py` currently scans only
   `taxonomy/` and `examples/`. Extending to `docs/` would require cleaning the
   one pre-existing internal mockup first.

3. ADD A DIFF-PAIR SCHEMA AND CHECK. Currently check_examples skips diff-pairs.
   A separate `diff-pair.schema.json` and `check_diff_pairs()` would close that gap.

4. EXPAND DIFF-PAIRS LIBRARY. 4 seed pairs is enough to demonstrate the format.
   The pedagogical value compounds with more, especially within-axis pairs that
   contrast similar entries (candid vs confident, narrative-case-study vs
   chronological-narrative).

5. THIRD ANCHOR TOPIC. Strategy brief allows for one. Candidates: "The discipline
   of rest" or "Choosing between Postgres and DynamoDB for a new service".

6. MIGRATE jsonschema.RefResolver TO referencing. Convenient but not urgent.

Before starting any of these: read this session log and AGENTS.md for the current
state and conventions.
```

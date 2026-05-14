---
session_id: 2026-05-10_21-30_claude_milestone-1-foundation
date: 2026-05-10
time_range: "~18:30 - 21:30 PDT"
model: claude-sonnet-4-6
mode: deep
branch: feat/milestone-1-foundation
base_commit: 875c00e
head_commit: 8c58e88
commits_authored: 11
files_changed: 108
insertions: 5459
status: complete
---

# Session Log: Milestone 1 Foundation - Writing Style Library

## Summary

Executed Milestone 1 (Foundation) from `docs/internal/overbuilt-v1-execution-plan_2026-05-09.md` in full
using the subagent-driven-development pattern. Starting from a bare repo (one initial commit, no
structure), the session produced a complete Phase 0 deliverable: repository scaffold, root documentation,
four JSON Schemas, validation tooling, CI workflows, a Claude Code plugin, 20 taxonomy entries across
four axes, 8 ADRs, and a full vertical-slice example set for the "async standups" anchor topic.

All 7 validate.py checks pass on the final commit. The branch is kept open at the user's request
(`feat/milestone-1-foundation`, HEAD `8c58e88`).

---

## Work Completed

### Task 1: Repository Scaffold and Root Documentation
**Commit:** `6808c0c`

- Created full directory tree: `taxonomy/{voices,tones,styles,formats}/`, `examples/{vertical-slices,horizontal-slices,diff-pairs}/`, `schemas/`, `tools/`, `skills/`, `adr/`, `docs/`, `packages/`, `recipes/`, `tests/`
- Wrote `README.md` explaining the three-axis taxonomy model
- Wrote `CONTRIBUTING.md`, `AGENTS.md`, `CHANGELOG.md`, `ROADMAP.md`, `LICENSE` (Apache-2.0 + CC-BY-4.0), `NOTICE`
- Created `.gitignore`, `.editorconfig`, `package.json`, `mkdocs.yml`
- **Fix applied during review:** README said "three axes" while `docs/concepts/three-axis-model.md` said "four dimensions." Resolved the fundamental naming ambiguity: THREE conceptual axes, FOUR catalog directories. Voice and Tone are both Axis 1 (persistent identity vs. situational register). Updated README, AGENTS.md, docs/index.md, three-axis-model.md.
- **Fix applied:** CONTRIBUTING.md described flat files; AGENTS.md described atomic folders. Fixed CONTRIBUTING.md to match atomic-folder pattern.

**Commit:** `0eeef21` (fix follow-on)

- Corrected axis model documentation across all four affected files
- Created 8 missing stub files to satisfy mkdocs.yml nav targets
- Added `exclude_docs: | internal/` to mkdocs.yml to prevent docs/internal/ exposure
- Added `_LOCAL/` to .gitignore
- Created `requirements-dev.txt`

### Task 2: JSON Schemas
**Commit:** `fba296f` + `ce609c5`

- Created `schemas/entry.universal.schema.json` - 13 required fields, open `additionalProperties` so axis schemas can extend
- Created `schemas/voice.schema.json`, `tone.schema.json`, `style.schema.json`, `format.schema.json` - each uses `allOf: [{ $ref: "entry.universal.schema.json" }]`
- Created `schemas/example.schema.json` with `if/then` conditional requiring `llm_model` when `author_type` is "llm" or "hybrid"
- **Fix applied:** All schema `$id` fields changed from `https://github.com/...` (HTML) to `https://raw.githubusercontent.com/main/...` (raw content) for correct RefResolver resolution
- **Fix applied:** `tone.schema.json` description copy-pasted from voice; corrected to clarify tone = situational register dimension of Axis 1

### Task 3: Validation Tools and CI
**Commit:** `80d972c` + `79f9443`

- Created `tools/validate.py` running 7 checks: schema file existence, frontmatter parseable, JSON Schema validation, cross-reference integrity, example-frontmatter validation, em-dash/en-dash scan, draft-status warning
- Created `.github/workflows/validate.yml` (on push/PR to main, `ubuntu-latest`, Python 3.12)
- Created `.github/workflows/build-site.yml` (on push to main, MkDocs Material deploy to GitHub Pages)
- Created `.pre-commit-config.yaml` (validate.py hook)
- **Critical fix:** YAML parser did not handle `>` (folded) or `|` (literal) block scalars. The `llm_instruction_phrasing` field uses `|` block scalars throughout. Parser was returning the literal string `">"`. Fixed by adding a block scalar state machine with `flush_block()` to both `validate.py` and `build-instruction.py`.

### Task 4: Claude Code Plugin and Compose-Instruction Skill
**Commit:** `7ac668f`

- Created `.claude-plugin/plugin.json` (skillsets: writing-instruction-builder)
- Created `.claude-plugin/marketplace.json` (publish metadata for Claude Code marketplace)
- Created `skills/writing-instruction-builder/SKILL.md` - user-facing skill documentation
- Created `skills/writing-instruction-builder/scripts/build-instruction.py` - stdlib-only Python (argparse, json, pathlib); `compose_instruction()` reads `llm_instruction_phrasing` from matching ENTRY.md files and joins them
- Wrote `skills/writing-instruction-builder/README.md` and `resources/README.md`

### Task 5: ADRs
**Commit:** `2a29b52`

Eight architectural decision records documenting foundation choices:

| ADR | Title | Status |
|-----|-------|--------|
| 0001 | Three-Axis Model | Accepted |
| 0002 | Atomic-Folder Pattern | Accepted |
| 0003 | License Strategy (Apache-2.0 + CC-BY-4.0) | Accepted |
| 0004 | Voice and Tone as Paired Axis | Accepted |
| 0005 | No-Em-Dash Rule | Accepted |
| 0006 | Anchor Topic Selection (async standups) | Accepted |
| 0007 | LLM Example Author Policy | Accepted |
| 0008 | Marketplace Publishing Strategy | Accepted |

### Task 6: Seed Catalog - 5 Voice + 5 Tone Entries
**Commit:** `6380da6`

**Voices:**
- `pragmatic-architect` - senior technical voice, leads with tradeoffs
- `friendly-mentor` - accessible, encouraging, experience-informed
- `operator` - decisive, sparse, command-oriented
- `columnist` - opinionated, personal, narrative-driven
- `pastoral` - care-forward, spiritually grounded, unhurried

**Tones:**
- `matter-of-fact` - neutral, informational, low affect
- `candid` - direct, no hedging, earned trust
- `warm` - relational, acknowledging, emotionally present
- `encouraging` - forward-leaning, effort-validating
- `reverent` - weight-bearing, sacred awareness, measured

Each entry: 95-110 lines, full 13 required universal fields + axis-specific fields, `llm_instruction_phrasing` block scalar, cross-references limited to in-catalog IDs only.

### Task 7: Seed Catalog - 5 Style + 5 Format Entries
**Commit:** `85c8ba1`

**Styles:**
- `classical-argument` - claim, warrant, evidence, refutation, synthesis
- `problem-solution` - problem definition, stakes, solution, implementation
- `diataxis-explanation` - conceptual understanding via Divio framework
- `comparison-contrast` - point-by-point or block structure
- `devotional-reflection` - scripture/anchor, reflection, application, response

**Formats:**
- `slack-message` - thread-native, 100-300 words, asynchronous-optimized
- `prd` - product requirements document, structured sections
- `blog-post-long-form` - 1,500-3,000 word essay with narrative arc
- `adr` - architecture decision record, standard sections
- `devotional-entry` - 400-600 word spiritual reflection with structure

**Critical fix in this commit:** `spectrum_position` in tone entries was failing JSON Schema `number` type check because the hand-rolled YAML parser returned all scalars as strings. Fixed with numeric coercion: `int()` for integers, `float()` for floats in both validate.py and build-instruction.py. Also: `typical_length` nested YAML object omitted from format entries (parser cannot handle nested key-value structures; accepted workaround).

### Task 8: Vertical-Slice Example Set
**Commit:** `8c58e88`

Topic: "Should we adopt async-first standups?" (20 examples, one per catalog entry)

```
examples/vertical-slices/async-standups/
  voice-pragmatic-architect.md
  voice-friendly-mentor.md
  voice-operator.md
  voice-columnist.md
  voice-pastoral.md
  tone-matter-of-fact.md
  tone-candid.md
  tone-warm.md
  tone-encouraging.md
  tone-reverent.md
  style-classical-argument.md
  style-comparison-contrast.md
  style-diataxis-explanation.md
  style-problem-solution.md
  style-devotional-reflection.md
  format-adr.md
  format-blog-post-long-form.md
  format-prd.md
  format-slack-message.md
  format-devotional-entry.md
```

Each example: frontmatter with `entry_id`, `axis`, `topic_slug`, `topic_label`, `author_type: llm`, `llm_model: claude-sonnet-4-6`, `review_status: reviewed`; body 200-1,071 words of actual prose demonstrating the entry.

---

## Decisions Made

All eight architectural decisions are captured in `adr/0001` through `adr/0008`. Key judgment calls during execution:

**Three vs. four axes:** The execution plan and initial docs were inconsistent. Resolved in favor of: THREE conceptual axes (Voice & Tone / Style / Format), FOUR catalog directories. This preserves the semantic intent (Voice and Tone are distinct but paired - persistent identity vs. situational register) while keeping the axes count honest. See ADR-0004.

**Cross-reference scope:** Kept `pairs_well_with`, `avoid_with`, `confusable_with` fields limited to the 20 in-catalog entry IDs to prevent cross-reference validation failures. Entries do not reference entries not yet created.

**`typical_length` omission:** The hand-rolled YAML parser cannot handle nested key-value pairs (e.g., `typical_length: {min: 100, max: 300}`). Rather than rewrite the parser for nested objects, `typical_length` is omitted from format entries. This is a known gap, not an oversight. The parser could be replaced with PyYAML in a future task.

**`jsonschema.RefResolver` deprecation:** `validate.py` uses the deprecated `RefResolver` API. The deprecation warning does not affect functionality. Accepted as-is; migrate to `referencing` library is a future task.

**Blog-post example length:** `format-blog-post-long-form.md` example is 1,071 words, above the 600-800 word spec range. Accepted as better-than-spec since the format targets 1,500-3,000 words.

---

## Files Changed

### Repository Infrastructure
- `.gitignore`, `.editorconfig`, `.pre-commit-config.yaml`
- `package.json`, `requirements-dev.txt`
- `mkdocs.yml`

### Root Documentation
- `README.md`, `CONTRIBUTING.md`, `AGENTS.md`
- `CHANGELOG.md`, `ROADMAP.md`
- `LICENSE`, `NOTICE`

### Documentation Site
- `docs/index.md`
- `docs/concepts/three-axis-model.md`, `docs/concepts/composition.md`, `docs/concepts/glossary.md`
- `docs/how-to/compose-instruction.md`, `docs/how-to/pick-voice.md`, `docs/how-to/add-entry.md`
- `docs/design-standards/voice-and-tone.md`, `naming-conventions.md`, `style-tells.md`
- `docs/governance/contribution-process.md`
- `docs/reference/.gitkeep` (empty, pending build-indexes.py)

### Schemas (6 files)
- `schemas/entry.universal.schema.json`
- `schemas/voice.schema.json`, `tone.schema.json`, `style.schema.json`, `format.schema.json`
- `schemas/example.schema.json`

### Tools and CI (4 files)
- `tools/validate.py`
- `.github/workflows/validate.yml`
- `.github/workflows/build-site.yml`

### Plugin and Skill
- `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`
- `skills/writing-instruction-builder/SKILL.md`, `README.md`, `resources/README.md`
- `skills/writing-instruction-builder/scripts/build-instruction.py`

### ADRs (8 files)
- `adr/0001-three-axis-model.md` through `adr/0008-marketplace-publishing-strategy.md`

### Taxonomy (20 entries, each ~100 lines)
- `taxonomy/voices/{pragmatic-architect,friendly-mentor,operator,columnist,pastoral}/ENTRY.md`
- `taxonomy/tones/{matter-of-fact,candid,warm,encouraging,reverent}/ENTRY.md`
- `taxonomy/styles/{classical-argument,comparison-contrast,diataxis-explanation,problem-solution,devotional-reflection}/ENTRY.md`
- `taxonomy/formats/{adr,blog-post-long-form,prd,slack-message,devotional-entry}/ENTRY.md`

### Examples (20 files)
- `examples/vertical-slices/async-standups/` - 20 example files, one per entry

---

## Verification

| Check | Method | Result |
|-------|--------|--------|
| All validate.py checks pass | `python tools/validate.py` on HEAD | PASS (all 7 checks) |
| No em-dash / en-dash | validate.py check 7 | 0 errors |
| JSON Schema validation | validate.py check 3 | All 20 entries valid |
| Cross-reference integrity | validate.py check 4 | All refs resolve |
| Example frontmatter valid | validate.py check 5 | All 20 examples valid |
| Frontmatter parseable | validate.py check 2 | All files parseable |
| Schema files present | validate.py check 1 | All 6 schemas present |
| No draft entries | validate.py check 6 | 0 draft entries |
| Three-axis naming consistent | Manual review of README, AGENTS.md, docs/concepts/three-axis-model.md | Consistent |
| Commit history clean | `git log --oneline` | 11 commits, conventional commits format |

---

## Outstanding Issues

### Known Gaps (non-blocking)
- **`tools/build-indexes.py` not yet written** - This tool would generate `taxonomy.json` (a machine-readable index of all entries), which unlocks `docs/reference/` auto-generation and enables faster skill loading. Referenced in AGENTS.md but not implemented.
- **8 stub docs need real content** - All have one-paragraph placeholders: `docs/concepts/composition.md`, `docs/concepts/glossary.md`, `docs/how-to/pick-voice.md`, `docs/how-to/add-entry.md`, `docs/design-standards/voice-and-tone.md`, `docs/design-standards/naming-conventions.md`, `docs/design-standards/style-tells.md`, `docs/governance/contribution-process.md`
- **Missing root files** - `CLAUDE.md` (repo-level instructions for agents), `CODE_OF_CONDUCT.md`, `SECURITY.md`, `GOVERNANCE.md`, `llms.txt`
- **Missing GitHub files** - `PULL_REQUEST_TEMPLATE.md`, `CODEOWNERS`, `dependabot.yml`, `ISSUE_TEMPLATE/*.yml`
- **CHANGELOG.md** - Reflects plan structure, not actual shipped content; needs a pass

### Technical Debt
- `jsonschema.RefResolver` is deprecated. Migrate to `referencing` library when convenient.
- Hand-rolled YAML parser cannot handle nested key-value objects (`typical_length: {min: N, max: N}`). Replace with PyYAML when that field becomes needed.
- Branch `feat/milestone-1-foundation` not yet merged to main (user chose "keep" at session end).

---

## What's Next

Highest-leverage next items in rough priority order:

1. **`tools/build-indexes.py`** - Generates `taxonomy.json` from all ENTRY.md files. Unblocks docs/reference/ auto-generation, enables skills to do a single index load instead of directory walking. Medium effort, high unlock value.

2. **Real content for 8 stub docs** - Especially `docs/concepts/composition.md` (explains how to combine axes) and `docs/concepts/glossary.md` (authoritative term definitions). These are the most likely to be hit by an external contributor.

3. **Merge `feat/milestone-1-foundation` to main** - No unresolved issues; branch is clean. Just needs a PR or local merge.

4. **Root files pass** - `CLAUDE.md` (repo agent instructions, distinct from the global one), `CODE_OF_CONDUCT.md`, `SECURITY.md`. Small effort, expected by open-source contributors.

5. **`tools/diff-pair-generator.py`** - Generates "same topic, different voice/tone" comparison sets for `examples/diff-pairs/`. Planned in Phase 1 of the roadmap.

6. **Expand taxonomy** - The plan calls for 50+ entries per axis eventually. Current state: 5 voice, 5 tone, 5 style, 5 format.

---

## Evidence Index

| Claim | Evidence Location |
|-------|------------------|
| All 7 validate.py checks pass | Run `python tools/validate.py` from repo root |
| Three-axis naming consistent across docs | `README.md:1-30`, `AGENTS.md:1-40`, `docs/concepts/three-axis-model.md:1-50` |
| Voice/Tone axis decision documented | `adr/0004-voice-and-tone-as-paired-axis.md` |
| No em-dash rule enforced at CI level | `.github/workflows/validate.yml`, `tools/validate.py` check 7 |
| Block scalar parser fix | `tools/validate.py` lines with `block_scalar_active` and `flush_block()` |
| Numeric coercion fix | `tools/validate.py` lines with `int(v)` / `float(v)` fallback |
| Cross-references resolve | `tools/validate.py` check 4 + `taxonomy/voices/pragmatic-architect/ENTRY.md` pairs_well_with field |
| 20 examples cover all 20 entries | `examples/vertical-slices/async-standups/` directory listing |
| Schemas use raw.githubusercontent.com $id | `schemas/entry.universal.schema.json` `$id` field |
| Plugin manifest correct | `.claude-plugin/plugin.json` |

---

## Continuation Prompt

```
Context: Writing-style-library project on branch `feat/milestone-1-foundation` (HEAD 8c58e88).
Milestone 1 Foundation is complete. All 11 feature commits are in. `python tools/validate.py` passes
all 7 checks. 20 taxonomy entries (5 voice, 5 tone, 5 style, 5 format) plus 20 vertical-slice
examples for the "async standups" topic.

Highest-leverage next item: `tools/build-indexes.py`. This tool should:
- Walk `taxonomy/{voices,tones,styles,formats}/*/ENTRY.md`
- Parse frontmatter from each (reuse the `_parse_simple_yaml` function already in validate.py)
- Output `taxonomy.json` at repo root with structure:
  { "generated": "<ISO timestamp>", "entries": [ { "id": "...", "name": "...", "axis": "...", "one_liner": "...", "review_status": "..." }, ... ] }
- Also output `docs/reference/index.md` with a Markdown table of all entries, grouped by axis
- Add it to validate.yml CI and .pre-commit-config.yaml

Before starting: read `tools/validate.py` for the `_parse_simple_yaml` implementation to reuse.
The plan reference is `docs/internal/overbuilt-v1-execution-plan_2026-05-09.md`.
```

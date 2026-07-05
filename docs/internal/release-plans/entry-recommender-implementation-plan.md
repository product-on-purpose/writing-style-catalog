---
title: Entry Recommender Skill - implementation plan
status: complete - all 8 phases built and smoke-tested 2026-07-03; spec revised across eight rounds of Codex adversarial review before build started, plus a ninth revision from smoke-test findings
owner: maintainer (approval given 2026-07-03); agent (execution and smoke test, 2026-07-03)
audience: whichever agent or human picks up a phase
related:
  - docs/internal/entry-recommender-spec.md (the committed spec this decomposes - AC live there, not here; see its Revisions section for what changed and why)
  - docs/internal/release-plans/entry-recommender-release-plan.md (when and how this ships)
---

# Entry Recommender Skill - Implementation Plan

Decomposes `docs/internal/entry-recommender-spec.md` into buildable phases. Acceptance criteria live in the spec; this plan maps every AC to at least one phase and describes how to build, not what "done" means.

**The spec's `status` is `fulfilled` as of 2026-07-03.** All 8 phases built, smoke-tested, and hardened - see the spec's Revision 9.

## Completion Status

| Phase | Goal | Fulfills AC | Owner | Status |
|---|---|---|---|---|
| 1 | Candidate-pool loader (stable-only, axis-specific facets) | AC-1, AC-6 | LLM | Done - `skills/entry-recommender/scripts/recommend.py` (`load_stable_ids`, `load_full_entry`, `load_all_stable_entries`) |
| 2 | Deterministic pre-filter (per-axis scoring) | AC-1, AC-7 | LLM | Done - IDF-weighted scoring (`build_idf_table`, `score_entry`), not the simple keyword count originally planned; calibrated and fixed twice against real smoke-test data (see spec Revisions 5 and 9) |
| 3 | LLM pick + justification | AC-1, AC-3, AC-7, AC-8 | LLM | Done except AC-8 (`SKILL.md` Step 2) - AC-8's runner-up disclosure correctly deferred as nice-to-have, not built |
| 4 | Partial-axis / fixed-value handling | AC-2 | LLM | Done - `recommend.py`'s `fixed` handling + `SKILL.md` Step 1 |
| 5 | Conflict detection and resolution (reuse, not reimplement) | AC-4, AC-5 | LLM | Done - `SKILL.md` Step 3, calling `build-instruction.py --json` via subprocess (the packaging question this phase flagged - resolved by following `style-profile`'s existing cross-skill subprocess pattern, not a new import mechanism) |
| 6 | Compose-or-recommend-only output | AC-5 | LLM | Done - `SKILL.md` Step 4 |
| 7 | SKILL.md + manifest registration | packaging (no direct AC) | LLM | Done - `skills/entry-recommender/SKILL.md`, `library.json`/`plugin.json` updated, `validate-plugin-manifest.mjs` passes |
| 8 | Smoke test against the spec examples | AC-1 through AC-7 (verification) | human or LLM | Done - independent fresh-context agent ran all 7 examples that existed at the time (4/6/7 as directly-constructed traces, per the spec's Revision 9); found and both of us fixed 2 real bugs and 2 SKILL.md clarity gaps. Examples 6 and 7 were later collapsed into a single Example 6 by Revision 19, once Revision 17 made the scenario Example 6 originally tested (widening beyond an exhausted short list) impossible by construction - the smoke test's findings and fixes remain valid; only the example count changed afterward |

## Phase 1: Candidate-pool loader

**Addresses:** AC-1, AC-6

**Goal:** A function that returns every `stable`/`reference-quality` entry per axis, with no `draft` entry ever included, using the same frontmatter-reading discipline the rest of the repo's tooling already follows.

**Steps:**
1. Add `skills/entry-recommender/scripts/load_candidates.py` (or extend `build-instruction.py` directly if the maintainer prefers one file over two - flag as an implementation-time choice, not pinned here).
2. Read entries via `taxonomy.json` for speed where possible, falling back to direct `ENTRY.md` frontmatter parsing for fields `taxonomy.json` does not carry (`confusable_with`, `avoid_with`, `pairs_well_with` - the documented "taxonomy.json is a slim index" gotcha).
3. Filter: `review_status in ("stable", "reference-quality")` only. No flag, no override - AC-6 is a hard constraint, not configurable.
4. Return one list per axis, and load axis-specific fields, not a universal set - verified against `schemas/{voice,tone,style,format}.schema.json` that `domain`/`family` are not universal (see the spec's Requirements section, Revision 1). Every entry regardless of axis carries `id`, `one_liner`, `when_to_use`, `tells`, `avoid_with`, `pairs_well_with` (required by `entry.universal.schema.json`). Per axis, only one additional field is actually guaranteed by that axis's own `required` list - verified directly against each schema, not assumed: Format guarantees `domain`+`family` (both required); Voice guarantees `family` only (`subfamily` is required only once a family reaches 12 members - confirmed absent on the real `pragmatic-architect` entry, since no voice family is anywhere near that size in the current 15-voice, 5-family catalog); Tone guarantees `markers` only (`spectrum`, `spectrum_position`, `nn_g_profile` are all optional); Style guarantees `structural_conventions` only (`frame`, `evidence_types`, `reader_contract`, `classical_mode` are all optional). Load every field, guaranteed or optional, when present - but Phase 2's scorer must treat the optional ones as bonus signal, never as a required input, since most stable entries today omit most of them.

**Verification:** Unit test asserting the returned Format list has exactly the current live count of `review_status: stable` entries (52 as of v0.5.1 - assert against a live count, not a hardcoded literal, so the test does not silently go stale) and contains zero ids from the current Hold-20 list. A second test loads `pragmatic-architect` specifically (a real stable voice confirmed to lack `subfamily`) plus a real tone and style entry, and confirms the loader neither raises nor silently substitutes an empty string for any absent optional field.

**Decision Gate:** N/A.

**Output Artifacts:** `skills/entry-recommender/scripts/load_candidates.py` (or equivalent), a passing unit test.

**Suggested Owner:** LLM.

## Phase 2: Deterministic pre-filter

**Addresses:** AC-1, AC-7

**Goal:** Score each axis's ENTIRE stable candidate pool in one pass - not just a top-N slice - using each axis's guaranteed facet field plus any optional facets present (Phase 1 Step 4), plus keyword overlap against `when_to_use`/`tells`. Scoring is cheap deterministic string/set matching, not an LLM call, so scoring 52 Format entries costs nothing meaningfully different from scoring 8. The short list is NOT a fixed-size top-N slice of this ranked result: it is every candidate that clears `above_threshold` (the relevance bar), however many there are, padded with a few non-qualifying candidates only when there are fewer than `short_list_size` qualifying ones (Revision 17 - an earlier top-N-only design silently hid genuinely qualifying candidates behind non-qualifying high scorers, confirmed common in practice, not a rare edge case). Because the short list already contains every qualifying candidate, Phase 5's conflict resolution never needs a separate widened search beyond it (Revision 19) - anything outside the short list is, by construction, below the relevance bar.

**Steps:**
1. Add one scoring function per axis, not one shared function - the facets differ per Phase 1's Step 4. Each axis's guaranteed field anchors its score: Format on `domain`+`family` keyword/enum match against the situation description; Voice on `family`; Tone on `markers`; Style on `structural_conventions`. When an optional facet is present on a given entry (`subfamily`, `spectrum`, `frame`, `classical_mode`, etc.), fold it in as a bonus signal - never require it, and never let its absence lower a score below what the guaranteed field plus `when_to_use`/`tells` overlap alone would produce, since most stable entries today omit most optional facets (confirmed: no current voice has `subfamily`). Every axis's score also adds keyword overlap against `when_to_use`/`tells` (the two universal fields), so the four scoring functions share that half but not the facet half.
2. No embeddings, no external API calls, per the spec's Non-Functional Requirements - pure string/set operations, unchanged by scoring the full pool instead of a slice.
3. Return the full ranked list per axis with every stable candidate's score, marking the top-N slice as the short list. Phase 3's LLM-read step still only reads full `ENTRY.md` content for the short-list slice, keeping the expensive step scoped small - only the cheap scoring pass covers the whole pool.
4. Define the AC-7 "minimum relevance bar" as a concrete threshold against this same score - this is the one place in the plan where a real number needs picking; document the chosen threshold and the reasoning for it in this file once decided, since the spec deliberately left the exact mechanism to implementation. Because the four scoring functions are not identical (different facet weight per axis), the threshold may need to be axis-specific too - do not assume one number works for all four without checking.

**Verification:** Feed the three spec Behavior/Examples situations through the scorer; confirm Example 1 and Example 2's expected-direction candidates (for example `problem-solution`-family styles for Example 1) appear in the short list, and Example 3's houseplant-Instagram situation produces low scores across the board. A fourth test scores a real tone entry that has no `spectrum` field and confirms its score reflects `markers` plus `when_to_use`/`tells` overlap alone, not a crash or an artificially depressed score from a missing optional field.

**Decision Gate:** The relevance-bar threshold (Step 4) blocks Phase 3's AC-7 path until picked - do not defer this into Phase 3, since Phase 3's prompt design depends on knowing what "low confidence" means numerically.

**Output Artifacts:** The scoring function returning the full ranked list per axis; the documented threshold value and rationale.

**Suggested Owner:** LLM, with the threshold choice flagged for a human sanity-check given it is the one real judgment call with no external source to cite.

## Phase 3: LLM pick + justification

**Addresses:** AC-1, AC-3, AC-7, AC-8

**Goal:** Given each axis's short list from Phase 2, the skill (running as the current assistant turn, not a dispatched subagent, per the spec's Non-Functional Requirements) picks the single best fit per axis and writes a one-line justification quoting or closely paraphrasing that entry's own field language.

**Steps:**
1. This phase is a prompt-design task, not a script - the matching happens in the skill's own reasoning per `SKILL.md`'s instructions, using the short-listed candidates' full field content as context.
2. Write the `SKILL.md` instruction block for this step: read each short-listed candidate's `when_to_use` and `tells` in full; pick the one whose language most specifically matches the described situation; write a one-line justification that names the specific phrase or concept that matched (AC-3's requirement to cite the entry's own field language).
3. Low confidence (AC-7) has two triggers, not one - the spec's own AC-7 text already says "the deterministic pre-filter AND the model's own read," but this phase must actually implement the second half, not just the first: (a) Phase 2's score never crossed the threshold for that axis (the case already covered); (b) Phase 2's score DID cross the threshold - the short list is topically relevant by keyword/facet overlap - but on actually reading the short-listed candidates' full `when_to_use`/`tells` language, none of them are genuinely supported by that language for this specific situation. Keyword overlap is a heuristic and can clear the bar by coincidence (shared vocabulary without shared meaning); the model's own read is the check that catches what the heuristic cannot. Either trigger produces the same AC-7 output: say so explicitly, name the closest near-miss, do not force-pick.
4. (AC-8, optional) If the top two short-listed scores are within a defined closeness margin, name the runner-up and the one-line reason it lost. Build this only after AC-1 through AC-7 are solid - it is explicitly lower priority in the spec.

**Verification:** Manually run the three spec Behavior/Examples through the full skill and confirm each justification actually quotes real field language from the picked entry (spot-check against the entry's live `ENTRY.md`, not the skill's own claim about what it read). A fourth case specifically exercises Step 3's second trigger: construct a situation description that shares enough vocabulary with a short-listed candidate's `when_to_use`/`tells` to clear Phase 2's threshold, but where that candidate's actual field language does not genuinely support the situation on a close read - confirm the skill reports low confidence for that axis rather than force-picking the coincidentally-scored candidate.

**Decision Gate:** N/A.

**Output Artifacts:** The relevant `SKILL.md` instruction section.

**Suggested Owner:** LLM.

## Phase 4: Partial-axis / fixed-value handling

**Addresses:** AC-2

**Goal:** A user can pass one or more axis values as already-fixed; the skill recommends only the rest and never touches the fixed ones.

**Steps:**
1. Define the input shape: situation description (required) plus optional `voice=`/`tone=`/`style=`/`format=` (mirroring `writing-instruction-builder`'s own existing argument shape, so the two skills feel consistent to a user who has used one and picks up the other).
2. Skip Phase 1-3's candidate generation entirely for any axis with a fixed value; pass it through unchanged into Phase 5 and Phase 6.
3. Validate that a fixed value is real (exists in the stable catalog) before proceeding; if not, fail clearly rather than silently ignoring it.

**Verification:** Feed Example 2 (voice fixed, three axes open) through the skill; confirm the output's voice field is exactly what was passed in, untouched and unjustified (no recommendation text generated for an axis the user already decided).

**Decision Gate:** N/A.

**Output Artifacts:** Input-parsing logic in `SKILL.md` / supporting script.

**Suggested Owner:** LLM.

## Phase 5: Conflict detection and resolution (reuse, not reimplement)

**Addresses:** AC-4, AC-5

**Goal:** The complete final four-axis set - every value that will be composed, whether it came from Phase 3's recommendation or Phase 4's fixed input - is cross-checked for `avoid_with` conflicts on every invocation, using the exact logic `writing-instruction-builder` already exposes. This runs unconditionally, not only when Phase 4 found a fixed value. When a conflict is found and at least one side is recommender-controlled (a Phase 3 pick, not a Phase 4 fixed value), the skill tries to resolve it by re-picking that axis from its own short list, excluding the candidate that caused the conflict - see the spec's Revisions 2 through 19. There is no separate "widen to the full pool" stage (an earlier design had one; Revision 19 removed it as dead, self-contradictory logic once it does): Phase 2's short list is, by construction, every candidate that clears AC-7's relevance bar for that axis, however many there are, so nothing outside the short list could ever be a valid resolution - it would fail the relevance bar the short list is defined by. Warn-and-compose is the fallback only for conflicts the skill genuinely cannot avoid (both values user-fixed, or every short-listed candidate on every controlled axis still conflicts), not the default response to one it created itself and could have avoided.

**Steps:**
1. Import or otherwise call `build-instruction.py`'s existing conflict-analysis function directly (per the spec's explicit reuse-not-reimplement requirement) - do not port or duplicate the `avoid_with`/`pairs_well_with` symmetric-check logic into a second file.
2. If `skills/entry-recommender/` and `skills/writing-instruction-builder/` need to share code across skill boundaries, resolve the import path during this phase - this is a real Claude Code skill-packaging question the implementation needs to answer, not assumed away here. Flag if skills cannot practically import each other's scripts, and fall back to extracting the shared function into a common location both skills reference, still without duplicating the logic.
3. Call the conflict analysis once, after both Phase 3 (recommended values) and Phase 4 (fixed values) have run, passing all four final values together - not per-pair, not conditionally gated on "if something was fixed."
4. If a conflict is found, classify it: does it involve a Phase-3-recommended (non-fixed) axis, or is it strictly between two Phase-4-fixed values?
   - **At least one side recommender-controlled:** re-pick that axis from Phase 2's short list, excluding the candidate that caused the conflict (no new pre-filter run - walk down the same already-computed list). Re-run the conflict check against the new candidate. Repeat until resolved or the short list is exhausted. If BOTH conflicting axes are recommender-controlled, try the lower-precedence axis first (format before style before tone before voice, the reverse of the compose precedence order in `build-instruction.py`, on the reasoning that it is less likely to be the axis the user cares most about matching exactly) - but if that axis's short list is exhausted with no resolution, do not fall through to warning yet: try the SAME walk on the other (higher-precedence) controlled axis before giving up. Warning is only correct once every recommender-controlled axis actually involved in the conflict has had its entire short list searched and none of them yielded a compatible alternative - stopping after only one side, when the other might have resolved it, is the same class of premature fallback an earlier revision already fixed once for a different search stage.
   - **Both sides user-fixed:** no re-pick is possible - the skill has no agency over either value. Fall through to the warning path directly.
   - **Every short-listed candidate on every recommender-controlled axis involved still conflicts:** only now fall through to the warning path, using the best-scoring (most relevant) candidate from whichever side was originally recommended - the same one that triggered the conflict in the first place. This presents the genuinely best-fitting option with the conflict named, rather than silently swapping in a poor-fitting entry (one that never cleared the relevance bar in the first place) just because it avoids the conflict. This should be rare - it means no short-listed entry on either conflicting axis is conflict-free - but the design does not assume it cannot happen.
5. For the warning path (only reached when resolution was not possible): `writing-instruction-builder` itself composes and warns on the same rule (verified against its code - "the instruction still composes even when a selected pair conflicts"); this skill matches that behavior for this fallback case. Surface the conflict alongside the composed output, not instead of it.
6. When resolution succeeds (Step 4's first branch), the newly-selected candidate still needs a real justification, not a silent id swap: re-run Phase 3's justification step (Phase 3 Step 2) for the new candidate alone, then append the conflict-avoidance reason - for example "picked over the higher-scoring candidate X because X conflicts with the fixed voice." AC-3 applies to every final recommendation, including one chosen during conflict resolution.

**Verification:** Four cases: (a) feed a variant of Example 2 (voice fixed, Tone's top candidate conflicts, a compatible second-best Tone candidate exists in the short list) through the skill and confirm it silently re-picks Tone rather than warning; (b) feed Example 4 (all-recommended, Voice and Tone conflict, a compatible alternate Tone exists in the short list) and confirm the same resolve-not-warn behavior when nothing is fixed; (c) feed Example 5 (both voice and tone fixed, conflicting) and confirm the skill falls back to warn-and-compose exactly as `writing-instruction-builder` would, since no resolution is possible; (d) feed Example 6 (every short-listed Tone candidate conflicts - a synthetic worst case) and confirm the warn-and-compose fallback fires only once the entire short list has genuinely been exhausted, not before.

**Decision Gate:** The Step 2 packaging question (can skills share scripts) blocks this phase's completion - resolve before Phase 6.

**Output Artifacts:** The conflict-check-and-resolve call site; resolution of the cross-skill import question, documented here once settled.

**Suggested Owner:** LLM, with the packaging question flagged for a human call if Claude Code's skill isolation model turns out to make script-sharing awkward.

## Phase 6: Compose-or-recommend-only output

**Addresses:** AC-5

**Goal:** By default, the skill's output is the composed prompt prefix (reusing `writing-instruction-builder`'s own compose path on the now-complete axis set from Phases 1-5), with any AC-7 low-confidence axis omitted from composition rather than filled with a near-miss; `--recommend-only` returns just the four picks and justifications without composing.

**Steps:**
1. Call the same `compose_instruction`/`compose_report` function `writing-instruction-builder` uses (same reuse discipline as Phase 5), passing the final axis set after Phases 3-5 have run. This set has at most four values, not always exactly four: any axis where Phase 3 hit its AC-7 low-confidence trigger (Phase 3 Step 3) is passed as blank, the same way a user of `writing-instruction-builder` itself can already leave an axis unspecified - the compose function already supports this, so Phase 6 does not need new logic for it, only to pass a blank instead of a value for that axis. Composition always happens (never blocked entirely); Phases 3 and 5 change which values are being composed and how many axes are filled, never whether composition happens at all.
2. Attach a conflict warning alongside the composed prompt only when Phase 5 actually reached its warning fallback - both sides fixed, or every short-listed candidate on every recommender-controlled axis involved in the conflict still conflicts. This must match Phase 5's real trigger condition exactly: if Phase 5 resolved the conflict by re-picking any axis from its short list, there is nothing to attach - the composed prompt already reflects the clean, resolved set.
3. Attach an AC-7 low-confidence note alongside the composed prompt for any axis passed as blank in Step 1, naming the near-miss Phase 3 identified - the same "surface it alongside the output, don't hide it" treatment as an AC-4 conflict.
4. Add the `--recommend-only` flag; when set, skip the compose call and return the structured recommendation (axis, value or blank, justification, any resolution notes from Phase 5 Step 6, any unresolved-conflict flags from the fallback case, any AC-7 low-confidence flags, any AC-8 runner-up notes) instead.

**Verification:** Feed Example 1 through the skill twice - once default, once with `--recommend-only` - and confirm the default run's output is byte-for-byte what `writing-instruction-builder` would produce given the same four axis values directly, and the flagged run produces no composed prompt at all. Feed Example 3 (houseplant Instagram, low confidence) through the default path and confirm the low-confidence axes are blank in the composed prompt, not filled with the near-miss, with the low-confidence report attached alongside. Feed Example 4 (all-recommended, short-list-resolvable conflict) through the default path and confirm it composes the resolved set with no warning attached. Feed Example 5 (both axes fixed, unresolvable) and Example 6 (every short-listed candidate on a recommender-controlled axis still conflicts) through the default path and confirm both DO produce a composed prompt with the conflict attached alongside it - not withheld.

**Decision Gate:** N/A.

**Output Artifacts:** The output-assembly logic; the `--recommend-only` flag handling.

**Suggested Owner:** LLM.

## Phase 7: SKILL.md + manifest registration

**Addresses:** packaging only - no AC maps here directly, but this phase is required before Phase 8 can run as a real invoked skill rather than standalone scripts.

**Goal:** The skill is installable and discoverable exactly like the two existing skills.

**Steps:**
1. Write `skills/entry-recommender/SKILL.md` with `name`, `description`, and `metadata.version: "0.1.0"` frontmatter, following the exact shape `scripts/validate-plugin-manifest.mjs` enforces (`frontmatter.name == directory name`, `metadata.version` present and SemVer).
2. Add the component entry to `library.json`'s `components.skills` array and mirror it in `.claude-plugin/plugin.json` if that manifest tracks skills separately - confirm against how the two existing skills are currently registered and copy the pattern exactly.
3. Update `library.json`'s / `plugin.json`'s top-level `description` field's "Ships N curated entries..." sentence if it should also name the new skill. Confirm current wording; the sentence already names `style-profile` explicitly - decide during implementation whether a third skill needs a mention there too, or whether the component list alone is sufficient.

**Verification:** `node scripts/validate-plugin-manifest.mjs` passes with the new component present.

**Decision Gate:** N/A.

**Output Artifacts:** `skills/entry-recommender/SKILL.md`; updated `library.json` / `plugin.json`.

**Suggested Owner:** LLM.

## Phase 8: Smoke test against the spec examples

**Addresses:** AC-1 through AC-7 (end-to-end verification; AC-8 if built)

**Goal:** Confirm the assembled skill, invoked the way a real user would invoke it, produces the behavior the spec's six Behavior/Examples describe.

**Steps:**
1. Invoke the skill six times, once per spec example: full recommendation; partial with voice fixed and a short-list-resolvable conflict; low-confidence houseplant case; all-recommended short-list-resolvable conflict (Example 4); both-axes-fixed unresolvable conflict (Example 5); every short-listed candidate on a recommender-controlled axis still conflicts, a synthetic worst case (Example 6). Examples 2, 4, 5, and 6 together cover all of Phase 5's classification branches.
2. Compare each run's output against the spec's stated expectations.
3. Run the release plan's full hygiene-gate checklist (`docs/internal/release-plans/entry-recommender-release-plan.md`).

**Verification:** All six examples behave as specified; every hygiene gate passes.

**Decision Gate:** This phase's pass/fail is the gate for marking the spec `fulfilled` and proceeding to the release plan's version-bump step.

**Output Artifacts:** None (verification only) - update this plan's Completion Status table and the spec's Task Summary AC checklist with evidence (commit hash or PR number) per both documents' own update rules.

**Suggested Owner:** human or LLM (either can run the smoke test; a human sign-off before tagging is recommended given this is a new user-facing surface, not a content fix).

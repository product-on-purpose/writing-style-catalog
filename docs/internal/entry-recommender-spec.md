---
title: Entry Recommender Skill - spec
status: draft - proposed, not yet reviewed by the maintainer
owner: maintainer (approval); agent (drafted this spec 2026-07-02)
audience: humans and agents building or reviewing this skill
related:
  - docs/internal/release-plans/entry-recommender-release-plan.md (what ships, when)
  - docs/internal/release-plans/entry-recommender-implementation-plan.md (how to build it)
  - docs/internal/backlog.md (S4 entry, the backlog slot this fills)
  - skills/writing-instruction-builder/SKILL.md (the skill this recommends into)
  - skills/style-profile/SKILL.md (the sibling personalization skill; different problem - see Non-Goals)
  - site/src/content/docs/guides/pick-voice.md (the existing manual, voice-only method this complements)
---

# Spec: Entry Recommender Skill

## Task Summary

**Status:** draft
**Last updated:** 2026-07-03 by agent (Claude Opus 4.8), revised after a fifth Codex adversarial review
**Linked plan:** `docs/internal/release-plans/entry-recommender-implementation-plan.md`
**Open questions:** 3 (see Open Questions)
**Revisions:** 5 (see Revisions)

### Acceptance Criteria Fulfillment

- [ ] **AC-1** - Full-recommendation path: no fixed axes, all four recommended from stable entries only
- [ ] **AC-2** - Partial-recommendation path: fixed axes are respected, not overridden
- [ ] **AC-3** - Every recommendation cites the entry's own field language, not invented reasoning
- [ ] **AC-4** - Conflicts anywhere in the final four-axis set are resolved by re-picking a recommender-controlled axis with a candidate that is both non-conflicting and relevant enough (AC-7's bar), and named when not (both fixed, or no such candidate anywhere in the stable pool)
- [ ] **AC-5** - Default output is a composed prompt using the resolved set; warn-and-compose is the fallback only when no compatible-and-relevant candidate exists anywhere in the stable pool; `--recommend-only` suppresses composition
- [ ] **AC-6** - Draft-status entries (including all of Hold-20) are never recommended
- [ ] **AC-7** - Low-confidence situations are named as such, not force-picked
- [ ] **AC-8** - Runner-up disclosure when the top two scores are close (nice-to-have)

### Currently In Progress

None.

## Purpose

`writing-instruction-builder` composes a prompt prefix from four axis values the user already knows they want. `style-profile` captures a user's own default style once, for reuse. Neither skill helps a user who has a writing situation but does not yet know which catalog entries fit it - and at 97 stable entries (52 of them Format alone), manually browsing the reference site to find a fit is real friction that did not exist when the catalog had 15 formats. This spec defines a new skill that takes a described writing situation and recommends a voice/tone/style/format combination from the stable catalog, with a defensible reason per axis, optionally composing the final prompt in the same step.

## Scope

- A new Claude Code skill (proposed name: `entry-recommender`; final name is the maintainer's call - see Open Questions) invoked with a natural-language situation description.
- Recommends a value for each of the four axes (Voice, Tone, Style, Format), drawn only from `stable`/`reference-quality` entries.
- Accepts optional pre-fixed axis values so a user who already knows one or two axes only gets recommendations for the rest.
- Reuses the existing conflict-detection and composition logic in `skills/writing-instruction-builder/scripts/build-instruction.py` rather than reimplementing either [S2].
- Ships as a third component in `library.json` / `.claude-plugin/plugin.json`, following the same manifest pattern as the two existing skills.

## Non-Goals

- Does not generate new catalog entries or modify `taxonomy/`.
- Does not recommend or reference any `draft`-status entry, including any of the Hold-20 formats - see AC-6.
- Does not replace `site/src/content/docs/guides/pick-voice.md`. That guide stays as the manual, voice-only, teach-the-reasoning method; this skill is the fast interactive path across all four axes. See Open Questions for whether the guide should link back to this skill once built.
- Does not persist a saved profile - that is `style-profile`'s job. This skill's recommendation is scoped to one situation, not a durable default.
- Is not the MCP server considered and deprioritized in the backlog (S2) - that item exposes composition to external MCP-compatible agents and remains "reach, not commitment" per `ROADMAP.md`'s own framing, with no waiting consumer [S6]. This skill solves a different, live problem: browsing friction inside a Claude Code session, today.
- Does not add a new anchor topic, diff-pair, or recipe. Purely a skill-layer addition.

## Users / Actors

- **Primary: a Claude Code user with a writing situation but no fixed axis picks.** They know what they need to write and for whom, but have not browsed the 52-format reference to find the right structural container, or the 15-voice reference to find the right persistent identity.
- **Secondary: a user who has fixed one or two axes and wants help with the rest.** For example, they know they want `pragmatic-architect` voice but are unsure whether `problem-solution` or `layered-disclosure` style fits a specific message.
- **Tertiary: another skill or agent operating on the user's behalf** that wants a defensible axis pick without hardcoding one.

## Requirements

The skill reads only `stable` and `reference-quality` entries when building its candidate pool. `AGENTS.md`'s review-status governance is explicit that promotion to `stable` is a maintainer decision earning "a hard cost" (Gate 2 rendering); a `draft` entry has not cleared that bar and is not "curated" in the sense the catalog's own manifest advertises [S1]. Recommending a draft would silently promote it in effect, without the maintainer's decision.

The skill's matching mechanism is hybrid, mirroring the catalog's own established "gated, not trusted" pattern - a deterministic pre-check followed by an LLM judgment, used throughout the agentic generation factory for distinguishability and de-dup gating [S7] - applied here to recommendation rather than generation:
1. A deterministic scorer ranks each axis's ENTIRE stable candidate pool in one pass - not just a short list - since this is cheap keyword/facet matching (string/set operations), not an LLM call; scoring all 52 Format entries costs nothing meaningfully different from scoring 8. The facet field each axis's score anchors on is axis-specific, not universal - verified directly against every axis schema's own `required` list [S4], not merely which fields exist: Format guarantees `domain`+`family` (both required, ADR 0010 enums) [S3]; Voice guarantees `family` only (`subfamily` is optional, required only once a family reaches 12 members - confirmed absent on the real `pragmatic-architect` entry, since no voice family is near that size today); Tone guarantees `markers` only (`spectrum` and the other tone facets are optional); Style guarantees `structural_conventions` only (`frame`, `classical_mode`, and the other style facets are optional). Optional facets, when present on a given entry, fold in as bonus signal; their absence is never an error and never depresses a score below what the guaranteed field plus `when_to_use`/`tells` overlap would produce, since most stable entries today omit most optional facets. Every axis additionally scores on keyword overlap against `when_to_use` and `tells`, the two fields genuinely required on all four axes [S4]. The top-N of this ranked list is the short list; the rest of the ranked list stays available (already scored, no re-computation) for AC-4's conflict-resolution fallback.
2. The skill itself (running in the current turn, not a dispatched subagent - see Non-Functional Requirements) reads the short list's full `ENTRY.md` content and picks the best fit per axis, citing the entry's own language.

This two-stage design keeps the EXPENSIVE part small (full-corpus LLM reasoning over 97 entries per call is unnecessary and slower than it needs to be - only the short list gets a full `ENTRY.md` read) while keeping the final judgment call - which requires real reading comprehension of nuanced `when_to_use`/`tells` prose - with the model rather than a keyword score alone. The CHEAP part (the deterministic score) covers the full pool from the start, which is what makes AC-4's relevance-respecting conflict resolution possible without a second pre-filter pass.

Conflict detection reuses `build-instruction.py`'s existing `avoid_with`/`pairs_well_with` cross-check (the symmetric rule already implemented under ADR 0016) rather than a second implementation of the same rule [S2]. This check runs against the complete final four-axis set on every invocation - not only when one or more axes are user-fixed. The all-recommended path (AC-1) has no fixed value to check against, but its four independently-picked entries can still conflict with each other (for example, recommending `pragmatic-architect` voice alongside `reverent` tone, an explicit `avoid_with` pair cited elsewhere in this repo's own backlog), so the check has to cover every pair in the final set, regardless of which values came from a fixed input versus a fresh recommendation. Divergent conflict logic between the two skills would be a real correctness risk - if the two skills disagreed on what counts as a conflict, `writing-instruction-builder`'s own warning could contradict a recommendation this skill had just made.

## Acceptance Criteria

**AC-1**: Given a situation description with no pre-fixed axis values, the skill returns a recommended value for all four axes (voice, tone, style, format), each drawn only from entries with `review_status: stable` or `reference-quality`. [model-inference, grounded in Purpose/Scope above]

**AC-2**: Given a situation description plus one or more pre-fixed axis values, the skill recommends only the remaining axes and does not override or second-guess the ones already fixed. [model-inference]

**AC-3**: Every recommended axis value's justification quotes or closely paraphrases language from that entry's own `when_to_use`, `tells`, or `one_liner` field - not invented reasoning disconnected from the entry's actual documented scope. [S4, model-inference on the exact field list]

**AC-4**: Before finalizing, the skill validates the complete final four-axis set - every value that will be composed, whether user-fixed (AC-2) or freshly recommended (AC-1) - for `avoid_with` conflicts, using the same detection logic `build-instruction.py` already exposes (`compose_report`'s conflict analysis) rather than a new implementation. This check runs on every invocation, including the all-recommended path where no axis is fixed at all, since two independently-recommended entries can conflict with each other exactly as a fixed-and-recommended pair can. If a conflict involves at least one recommender-controlled axis (a value the skill itself picked in AC-1, not a value the user fixed in AC-2), the skill attempts to resolve it: first by re-picking that axis from its own short list, excluding the candidate that caused the conflict, and if the short list is exhausted, by widening the search to the axis's full stable candidate pool (the short list is a relevance heuristic, orthogonal to conflict status - a compatible candidate can rank below the cutoff for reasons unrelated to whether it conflicts). The widened search must not bypass AC-7's relevance bar: only a candidate that is both non-conflicting AND relevant enough counts as a resolution - a technically-compatible but irrelevant candidate is not an acceptable substitute, since silently picking one would smuggle a poor fit past the exact low-confidence guard AC-7 exists to enforce. A recommender that already knows two of its own picks conflict should not present that combination as its answer when a compatible AND relevant stable alternative exists anywhere on that axis. Only if no candidate anywhere in the stable pool is both compatible and sufficiently relevant, or if the conflict is between two user-fixed values (where the skill has no agency over either side), does it name both conflicting entries in its output instead - see AC-5 for how this interacts with the default compose step. [S2]

**AC-5**: By default, the skill's final output is the assembled prompt prefix, produced by calling the same compose path `writing-instruction-builder` uses. When AC-4 resolves a conflict by re-picking a recommender-controlled axis with a candidate that is both non-conflicting and relevant enough, the resolved set is what gets composed - no warning needed, since no conflict survives to compose time. When AC-4 cannot resolve a conflict - no candidate anywhere in the stable pool (not merely the short list) is both compatible and sufficiently relevant, or the conflict is between two user-fixed values the skill has no agency over - the skill composes AND surfaces the conflict alongside the output, matching `writing-instruction-builder`'s own verified behavior of warning without blocking on the same `avoid_with` rule [S2] - but only as the fallback for a conflict the skill genuinely could not avoid, not as the default response to a self-inflicted, avoidable one, and never by silently substituting an irrelevant-but-compatible candidate instead of naming the conflict honestly. A `--recommend-only` flag suppresses composition unconditionally and returns just the four axis picks with justifications (plus any AC-4 conflict or resolution notes), for a user who wants to review before composing. [model-inference]

**AC-6**: No entry with `review_status: draft` - including every current Hold-20 format - is ever recommended, regardless of textual relevance to the situation description. [S1]

**AC-7**: When the deterministic pre-filter and the model's own read both surface no stable candidate clearing a minimum relevance bar for a given axis (for example, a situation genuinely outside the catalog's scope), the skill says so explicitly for that axis rather than force-picking the least-bad option, and names the closest near-miss candidate so the user can judge it themselves. [model-inference]

**AC-8** (nice-to-have, not required for v1): When the top two candidates for an axis score within a defined closeness margin of each other, the recommendation optionally names the runner-up and the one-line reason it lost. Deferred to the implementation plan's judgment on effort/value; not blocking. [model-inference]

## Behavior / Examples

**Example 1 - full recommendation, no fixed axes.**
Input: "I need to tell my engineering team that a feature we committed to is getting cut this quarter, and I want them to trust the reasoning, not just accept the decision."
Expected: the pre-filter surfaces `professional`/`progress` and `professional`/`deliberation` family candidates for Format, a Voice favoring transparency-under-pressure archetypes (for example `pragmatic-architect` or `direct-communicator`), a Tone favoring candor over reassurance (for example `candid`), and a Style favoring reasoning-forward sequencing (for example `problem-solution`). Each pick's justification names the specific `when_to_use`/`tells` language that matched. Default output composes the full prompt.

**Example 2 - partial recommendation, one axis fixed, conflict resolved.**
Input: voice=`pragmatic-architect` (fixed), situation: "explaining a database migration decision to the team."
Expected: the skill does not touch or re-justify the voice pick. It recommends tone/style/format. If Tone's best-scoring candidate is `reverent` (in `pragmatic-architect`'s `avoid_with`), the skill re-picks Tone from the remaining short list first - Tone is recommender-controlled, so a compatible alternative should be tried before presenting a known conflict. A warning appears only if no candidate anywhere in the entire stable Tone pool is both compatible and relevant enough to clear AC-7's bar - not merely when the short list runs out.

**Example 3 - low-confidence situation.**
Input: "Write something for my houseplant's Instagram account."
Expected: the skill does not force a stable pick that technically clears the pre-filter by keyword coincidence. It reports low confidence for the axes that do not genuinely fit and names the closest near-miss, letting the user decide whether to proceed anyway.

**Example 4 - conflict in an all-recommended set, resolved (AC-4, no fixed axes).**
Input: a situation description whose keyword/facet signals independently favor `pragmatic-architect` for Voice and `reverent` for Tone - a real `avoid_with` pair in the catalog today - and whose Tone short list also contains a compatible second-best candidate.
Expected: AC-4's conflict check catches the pair (it runs against the complete final four-axis set on every invocation, not only when something is fixed). Because both Voice and Tone are recommender-controlled in this all-recommended path, the skill re-picks Tone from the remaining short list rather than presenting the known-conflicting pair as its answer. The composed output uses the resolved combination; no conflict warning is needed because none survives to compose time.

**Example 5 - conflict that cannot be resolved (AC-4 fallback, both axes fixed).**
Input: voice=`pragmatic-architect` AND tone=`reverent`, both explicitly fixed by the user, on any situation.
Expected: AC-4 detects the conflict but cannot resolve it - neither conflicting value is recommender-controlled, so there is no alternative to try. The skill falls back to `writing-instruction-builder`'s own verified behavior: compose anyway, with the conflict surfaced alongside the output. This is the one case where warn-and-compose is the right default, because it is the only option - not a shortcut taken when a fix was available.

**Example 6 - short list exhausted, resolved from the wider pool.**
Input: a situation description where every Tone candidate in the short list conflicts with the recommended (or fixed) Voice, but a compatible Tone that also clears AC-7's relevance bar exists elsewhere in the full stable Tone pool - it simply scored below the pre-filter's cutoff on topical relevance (a heuristic ranking artifact), not because it is genuinely a poor fit.
Expected: the skill does not give up at the short list's edge and warn. It widens the search to the full stable Tone pool, filtered to candidates that are both non-conflicting and relevant enough, finds the compatible-and-relevant candidate, and composes the resolved set - the same as Example 4, just one search stage further.

**Example 7 - widened pool has a compatible match, but it is not relevant enough.**
Input: a situation description where every short-listed Tone candidate conflicts, and the only technically non-conflicting Tone anywhere in the stable pool falls well below AC-7's relevance bar for this situation - no real fit exists among the compatible options.
Expected: the skill does not silently substitute the irrelevant-but-compatible candidate as if it were a clean recommendation - doing so would defeat AC-7's low-confidence guard rather than honor it. It falls back to warn-and-compose using the best-scoring (most relevant) Tone candidate - the one that conflicts - surfacing the conflict rather than hiding a poor fit behind a false sense of resolution. Warning is reserved for this case (nothing both fits and avoids the conflict) and the both-fixed case (Example 5), not for a short list that merely ran out.

## Non-Functional Requirements

- **Interactive latency.** The skill runs in the current conversational turn - it does not dispatch an isolated subagent or a `Workflow` run for the matching step. The agentic factory's subagent-isolation pattern exists to keep prose out of the orchestrator's context and to parallelize batch work (rendering 12 samples across a format, auditing a whole corpus) [S7]; neither benefit applies to a single interactive recommendation a user might invoke several times while iterating on a description, where a multi-minute round trip would be a worse experience than the browsing friction this skill exists to remove.
- **No new dependencies.** The deterministic scorer is pure keyword/facet matching over data already in `taxonomy/**/ENTRY.md` frontmatter - no embedding model, no vector store, no new Python package - even though it scores each axis's entire stable pool rather than stopping at a short list (Revision 5); this stays cheap because it is string/set matching, not an LLM call. Consistent with the catalog's "free by default" posture; see Open Questions for whether this proves precise enough at scale.
- **No catalog mutation.** The skill only reads `taxonomy/` and `examples/`; it never writes to either.

## Revisions

**Revision 1 (2026-07-02):** A Codex adversarial review of the initial draft (spec + implementation plan, working-tree diff) surfaced two high-severity findings, both confirmed against the codebase before fixing:
1. AC-4 originally scoped conflict detection to "a fixed axis value's `avoid_with` list," which never fires in the AC-1 all-recommended path (the default, most common invocation) - two independently-recommended entries could conflict with nothing catching it. AC-4 and AC-5 revised to validate the complete final four-axis set on every invocation; Example 4 added to make the fix concrete. AC-5 also corrected to warn-and-still-compose (matching `writing-instruction-builder`'s verified real behavior) rather than an initially-drafted withhold-composition version that would have made the two skills disagree on the same rule - caught while writing this revision, before it reached the plan.
2. The pre-filter design originally assumed every axis carries `domain`/`family`. Verified directly against `schemas/{tone,style,voice,format}.schema.json`: those fields exist only on Format (both required) and partially on Voice (`family` only, no `domain`). Tone and Style have neither. Requirements section and Sources & Evidence corrected to the real per-axis facets (Tone: `spectrum`/`markers`; Style: `frame`/`classical_mode`/`structural_conventions`; Voice: `family`/`subfamily`); as originally specified, implementation would have crashed or produced meaningless scores for two of the four axes.

**Revision 2 (2026-07-03):** A second Codex adversarial review (of the committed working tree, this time including the still-uncommitted spec) surfaced one finding worth acting on and one worth declining, both evaluated on their technical merits rather than applied by default:
1. **Accepted.** Revision 1's warn-and-compose fix for AC-5 was itself incomplete: it made the recommender match `writing-instruction-builder`'s behavior exactly, but the two skills are not actually in the same position. `writing-instruction-builder` validates a user's explicit, fixed choice - warn-and-compose is the right call because refusing would be unhelpful when the user asked for exactly that pairing, and there is no alternative to offer. The recommender, in the all-recommended path, chose both conflicting values itself from a short list it already generated - it has an alternative sitting right there. AC-4 and AC-5 revised again: when a conflict involves at least one recommender-controlled (non-fixed) axis, the skill now tries a compatible alternative from that axis's short list before falling back to warn-and-compose. Warn-and-compose is now the fallback for conflicts the skill genuinely cannot avoid (both values user-fixed, or the short list exhausted), not the default response to a self-inflicted one. Examples 2 and 4 revised to show resolution as the primary path; Example 5 added for the true fallback case (both axes fixed).
2. **Declined as originally framed, addressed at the root cause.** The review flagged that this spec and its companion planning docs live under `docs/internal/`, which `AGENTS.md` and the root `CLAUDE.md` marked read-only at the time. The specific request - move this proposal elsewhere, or get separate maintainer sign-off before committing - was declined: the exception for `docs/internal/adr/` and `docs/internal/release-plans/` as living, maintainer-directed documents is real and repeatedly exercised (`docs/internal/agentic-generation-spec.md`, the promotion-and-release runbook, every `stream-b-*` tracker), and this spec's own creation and commit were direct maintainer instructions in this session. But the underlying documentation gap the review kept pointing at was real: that exception lived only in agent memory, not in the repo's own governing files, so a future agent or contributor reading only `AGENTS.md`/`CLAUDE.md` would get contradictory guidance. Fixed at the source in Revision 3 below, rather than worked around in this one document.

**Revision 3 (2026-07-03):** A third Codex adversarial review (branch diff against `main`, fetched via GitHub) surfaced two more findings, both accepted:
1. Revision 2's conflict-resolution fix stopped too early: it searched only the Phase 2 short list before falling back to warn-and-compose, but the short list is a relevance heuristic (topical keyword/facet score) that has nothing to do with conflict status - a compatible candidate can easily rank just below the cutoff. AC-4 and the implementation plan's Phase 5 revised again: when the short list is exhausted and at least one conflicting axis is recommender-controlled, the search widens to that axis's full stable pool (already loaded by Phase 1, no new pre-filter run needed) before falling back to warning. Warn-and-compose is now reserved for the case where the entire stable pool conflicts, not merely the short list - a much rarer, more defensible last resort. Example 6 added to make this concrete.
2. The review's `docs/internal/` finding, raised in Revision 2 and declined there, came back sharper: the living-docs exception this proposal (and this session's whole body of `docs/internal/release-plans/` work) relies on was never written into the repo's own `AGENTS.md` or `CLAUDE.md` - only carried in agent memory, invisible to any future agent or human without it. That is a real, structural gap independent of whether this specific commit was fine, and it does not fix itself by declining the finding a second time. Corrected at the source: `AGENTS.md`'s "Paths to Know" table and the project `CLAUDE.md`'s hard rules now state the actual rule - `docs/internal/` is a living planning area maintained under maintainer direction, with `docs/internal/_working/` (added as an explicit row) and `_LOCAL/` as the genuinely frozen exceptions - rather than the blanket "read-only" statement that never matched this repo's own demonstrated practice.

**Revision 4 (2026-07-03):** A fourth Codex adversarial review found that Revision 3's own fix was incomplete in two ways, both accepted:
1. The widened-pool search introduced in Revision 3 fixed the conflict problem by creating a relevance problem: "the first candidate that does not conflict, not necessarily the highest-scoring one" could surface a nearly-irrelevant entry from the bottom of a 52-candidate axis, silently smuggling a poor fit past AC-7's low-confidence guard instead of honoring it. AC-4, AC-5, Phase 5, and Example 6 all revised so the widened search filters by AC-7's relevance bar first - only a candidate that is both non-conflicting AND relevant enough counts as a resolution. Example 7 added specifically for the negative case (a compatible-but-irrelevant candidate exists, and the skill must not use it).
2. A cross-reference miss: Revision 3 updated AC-4 and Phase 5 to widen from the short list to the full stable pool, but never propagated that same fix into AC-5's fallback condition or Example 2, both still written in Revision 2's short-list-only terms - a reader following AC-5 or Example 2 alone could implement a narrower, AC-4-violating fallback. Both corrected to state the real condition (no compatible-and-relevant candidate anywhere in the stable pool, not merely the short list).

**Revision 5 (2026-07-03):** A fifth Codex adversarial review found two more gaps, both accepted and both verified directly against the schemas before fixing:
1. A mechanical hole in Revision 4's own fix: the widened search is required to check AC-7's relevance bar, but the original Phase 2 design only ever scored the short list (top-N) - candidates beyond it had no score to check a bar against. Fixed by having Phase 2 score the axis's entire stable pool in one pass instead of just the short list. This is not a performance compromise: the scoring step is cheap deterministic string/set matching, not an LLM call, so scoring 52 entries costs about the same as scoring 8. The short list is now simply the top-N slice of a list that was always fully computed; Phase 5's widened search became a lookup against existing data, not a second pre-filter run. Only Phase 3's LLM read (the genuinely expensive step) stays scoped to the short list.
2. The scoring design assumed every axis's non-universal facet fields were reliably present - `subfamily` for Voice, `spectrum` for Tone, `frame`/`classical_mode` for Style - when in fact each axis schema's own `required` list guarantees only one such field: Voice requires `family` alone, Tone requires `markers` alone, Style requires `structural_conventions` alone. Verified directly against `schemas/{voice,tone,style}.schema.json` and the real `pragmatic-architect` entry, confirmed to have zero `subfamily` occurrences (no voice family in the current 15-voice, 5-family catalog is close to the 12-member threshold that would require it). Phase 1 and Phase 2 revised so optional facets are loaded and used as bonus signal when present, never as a required input whose absence errors or silently depresses a score.

## Sources & Evidence

- **[S1]** `AGENTS.md`, "Review Status Progression" section - draft entries require maintainer promotion; the 60-entry (now 97) `stable` set is the curated baseline. Class A (repo file, verified current 2026-07-02).
- **[S2]** `skills/writing-instruction-builder/scripts/build-instruction.py` - existing `avoid_with`/`pairs_well_with` symmetric conflict-detection and voice-to-tone-to-style-to-format precedence (ADR 0016). Class A (repo file, verified current).
- **[S3]** `docs/internal/adr/0010-domain-and-family-organization.md` and `schemas/format.schema.json` - `domain`/`family` are Format-only facets (both in `format.schema.json`'s `required` list, ADR 0010 enums); Voice's `schemas/voice.schema.json` requires `family` (a different enum: expert/care/principal/witness/dissident) but not `domain` and not `subfamily`. Class A (repo files, verified current 2026-07-02 against an adversarial review finding that the original draft over-generalized this to all four axes).
- **[S4]** `schemas/entry.universal.schema.json` (confirms `when_to_use` and `tells` are required on every axis), `schemas/tone.schema.json` (`"required": ["markers"]` only - `spectrum`/`spectrum_position`/`nn_g_profile` are optional), `schemas/style.schema.json` (`"required": ["structural_conventions"]` only - `frame`/`classical_mode`/`evidence_types`/`reader_contract` are optional), `taxonomy/voices/pragmatic-architect/ENTRY.md` (confirmed to contain zero `subfamily` occurrences, verifying the optional-field claim against real data, not just schema text). Class A (repo files, verified current 2026-07-03 against a second adversarial review finding that optional facets were being treated as guaranteed).
- **[S5]** `site/src/content/docs/guides/pick-voice.md` - the existing manual, voice-only picking method; establishes the confirm-with-example and confusable_with-fallback patterns this skill's design draws on. Class A (repo file).
- **[S6]** `ROADMAP.md`, "Later - reach, not commitment" section - the MCP server (backlog S2) is explicitly gated on "a real consumer signal" that has not appeared. Class A (repo file).
- **[S7]** `docs/internal/agentic-generation-spec.md` and `tools/agentic/README.md` - the "gated, not trusted" deterministic-check-plus-LLM-judge pattern this spec's matching design is modeled on. Class A (repo file).

## Open Questions

1. **Skill name.** This spec uses `entry-recommender` as a working name (parallels `writing-instruction-builder`'s naming pattern; avoids colliding with any axis name like "style"). Final naming is the maintainer's call.
2. **Pre-filter precision at scale.** Keyword/facet matching (no embeddings) is proposed for v1 as the zero-dependency, "free by default" option. If real usage shows the pre-filter missing genuinely good matches (a semantic match with no keyword overlap), the next lever is a lightweight embedding index - deliberately deferred, not designed here, per the same discipline the backlog applies to E1's generation-gate machinery.
3. **Should `pick-voice.md` cross-link to this skill once built?** The guide teaches the manual method; once an interactive fast-path exists, a "or let the skill do this for you" pointer near the top would probably help readers, but changing an existing hand-authored doc is outside this spec's scope - flagged for the implementation plan's judgment or a small follow-up.

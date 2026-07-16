---
name: entry-recommender
description: Recommend a voice, tone, style, and format combination from the catalog's stable entries for a described writing situation, then compose the prompt in the same step. Use when a user has a writing situation but does not yet know which catalog entries fit it - they describe what they need to write, not which entry ids to use. Accepts optional pre-fixed axis values so a user who already knows one or two axes only gets recommendations for the rest. Never recommends a draft-status entry. Reports low confidence rather than force-picking when nothing genuinely fits.
metadata:
  version: "0.1.0"
---

# Entry Recommender

Take a described writing situation and recommend a voice/tone/style/format combination from the catalog's stable entries, with a defensible reason per axis quoting the entry's own language, then compose the final prompt in the same step. This is the fast interactive path for a user who does not yet know which of the 97 stable entries (52 of them Format) fits their situation - `writing-instruction-builder` composes from axis values you already know you want; this skill finds them first.

Full spec: `docs/internal/entry-recommender-spec.md`. Implementation plan (this file implements Phases 3-6; Phases 1-2 are `scripts/recommend.py`): `docs/internal/release-plans/entry-recommender-implementation-plan.md`.

## Prerequisites

- The `writing-style-catalog` plugin is present: `taxonomy/` (the entries), `skills/entry-recommender/scripts/recommend.py` (the scorer), and `skills/writing-instruction-builder/scripts/build-instruction.py` (the composer, reused here rather than reimplemented) all exist at the plugin root.
- If a prerequisite is missing, say so and stop. Do not invent entries, scores, or field language.

## Usage

```
/writing-style-catalog:entry-recommender <situation description> [voice=<id>] [tone=<id>] [style=<id>] [format=<id>] [--recommend-only]
```

The situation description is free text - what you need to write and for whom. Any `axis=id` tokens in the input are pre-fixed axis values; strip them out. Everything else in the input is the situation description, and it reaches the script only through Step 1's temp-file mechanism - never as a `--situation` shell argument (that is Step 1's first failure mode).

- `voice=`, `tone=`, `style=`, `format=` - optional. An axis with a fixed value is never recommended, re-justified, or second-guessed (AC-2).
- `--recommend-only` - optional. Suppresses composition; returns just the four picks, justifications, and any conflict/low-confidence notes, for a user who wants to review before composing (AC-5).

## The Process

Order is load-bearing: score before reading full fields (Step 1 before Step 2), pick before conflict-checking (Step 2 before Step 3), resolve before composing (Step 3 before Step 4).

**Step 1 - Score the candidate pool.** The situation description is arbitrary user text - it can and will contain quotes, apostrophes, backslashes, or newlines ("explaining my team's Q3 numbers" already has one) - and it can be sensitive (HR matters, incident details, customer or product information). Four failure modes to avoid, not one, two, or three:

- Never build a shell command by embedding that text directly into a `--situation "..."` string - real command injection, not theoretical; an ordinary apostrophe is enough to break it with no ill intent.
- Never hand-substitute it into a JSON template without properly escaping it first ("explaining why \"quality\" matters" breaks `{"situation": "<text>"}` the instant you paste it in unescaped - confirmed, this produces invalid JSON from completely ordinary text, no attacker required).
- Never pipe it through a shell heredoc, even a quoted one - the delimiter that closes a heredoc is plain text matched against the body; if the situation text itself contains that exact line (a fixed, predictable delimiter is guessable by anyone who has read this file, since it is public), the heredoc ends early and whatever follows is interpreted as a new, separate shell command, silently reintroducing the exact injection this is supposed to prevent. The script's `--stdin` flag is this same trap by another name when fed via a heredoc or here-string - do not use `--stdin` for situation text either.
- Never rely on yourself to remember a separate delete-the-file step afterward as the only cleanup - if this run is interrupted, errors out earlier than expected, or the step is simply skipped, sensitive situation text is left sitting on disk. Use `--ephemeral-input-file` (below), which deletes the file as part of the script's own execution, not as a separate instruction you have to remember and successfully reach.

Do all of this correctly, in order:

1. Apply real JSON string escaping to the situation text (and to `topic`/`audience` if given): replace `\` with `\\`, `"` with `\"`, newline with `\n`, carriage return with `\r`, tab with `\t`. This is a mechanical, well-defined transformation, not a judgment call - do not skip it or assume the text happens to be simple enough not to need it.
2. Use the Write tool (never a shell command, `echo`, or heredoc) to write the escaped JSON payload to a new file. The location MUST be inside the OS/system temp directory specifically (Python's `tempfile.gettempdir()` - on this session, that is the same root your scratchpad directory is nested under) - NOT merely "somewhere that feels temporary," and NEVER inside this project's working directory. Step 3's flag checks this exact condition and refuses to touch (read OR delete) a path outside it, so if you write somewhere else, the file will be left behind with an error telling you to delete it yourself - avoid that by writing to the right place the first time. The filename MUST end in `.entry-recommender-input.json` (any prefix is fine, for example `situation-<something>.entry-recommender-input.json`) - Step 3's flag also refuses to touch a file that is not named this way, on purpose, so a path mistake fails loudly instead of silently deleting the wrong file:

   ```json
   {"situation": "<the escaped situation text>", "voice": "<id, if fixed>", "tone": "<id, if fixed>"}
   ```

   Omit any key for an axis that is not fixed. The Write tool writes file content directly - it does not involve a shell at all, so nothing here is a quoting or injection concern; the only remaining requirement is that the JSON string itself is valid, which step 1 above ensures.
3. Run the scorer against that file with `--ephemeral-input-file`, not `--input-file` - the path is short, assistant-chosen, and safe to put in a shell command, unlike the situation text itself. This flag deletes the file itself, guaranteed, as soon as it has been read (you do not need a separate cleanup step, and the file is gone even if the JSON turns out to be malformed or scoring fails), but only if the path is outside this repo, inside the system temp directory, AND correctly named per step 2 - otherwise it raises an error instead of reading or deleting anything:

   ```bash
   python "${CLAUDE_SKILL_DIR}/scripts/recommend.py" --ephemeral-input-file <path-to-the-temp-file> --json
   ```

This returns, per non-fixed axis: `short_list` - EVERY candidate that clears `above_threshold`, however many there are, padded with a few non-qualifying candidates only if there are fewer than `short_list_size` qualifying ones - with `score`, `distinct_matches`, `matched_tokens` (which situation words actually matched, broken out by field), `one_liner`, `when_to_use`, `tells`, `when_not_to_use` - everything Step 2 needs to read, positive and negative fields alike. Also `full_ranked` (everyone else - always non-qualifying, since every qualifying candidate is already in `short_list` by construction - kept only for transparency/debugging, not part of the documented workflow below) and `candidate_count`. A fixed axis reports `{"fixed": id, "valid": true/false}` instead - if `valid` is `false`, stop and tell the user the fixed value does not exist in the stable catalog rather than silently ignoring it (Phase 4 Step 3).

From this point on, every id this skill puts into a shell command (in Step 3 and Step 4 below) is either one this step's JSON output already validated (a `fixed` axis reported `valid: true`) or one this skill itself picked from `short_list` (which only ever contains real stable catalog ids, matching the strict kebab-case id pattern every entry is validated against). Never interpolate the raw, not-yet-validated situation text or an unvalidated fixed-axis claim into any later shell command either - route it through Step 1's temp-file mechanism first.

**Step 2 - Read, pick, and justify each non-fixed axis (AC-1, AC-3, AC-7).**

**The score decides who makes the short list. It does not decide who wins.** The score is a cheap keyword/facet heuristic - it tells you who is worth reading, not who is right. Read every short-listed candidate's `when_to_use` and `tells` in full, then pick based on which one is genuinely, specifically supported by that language for THIS situation. Confirmed repeatedly in testing: the top-scoring candidate is very often not the best actual pick - a lower-scoring candidate can describe the situation almost verbatim while the top score turns out to be pulling in the wrong direction (for example, scoring high on "the reasoning is settled, not relitigated" language when the situation explicitly asks the reader to trust the reasoning) or coincidentally matching a word used in an unrelated sense (a candidate's `one_liner` using "account" to mean a written narrative, when the situation means a social-media account). Compare the WHOLE short list's language against the situation before picking - do not default to the top score and use your read only as a rubber stamp or a veto of one obviously-wrong option.

**Also read `when_not_to_use` before picking, not just `when_to_use`/`tells` - a positive-only read is not the full read.** Every candidate carries both fields; scoring only ever looks at the positive ones, so a candidate can clear the short list on `when_to_use`/`tells` overlap while its own `when_not_to_use` explicitly names the situation you are looking at as a poor fit. Treat a genuine match there as disqualifying for that candidate, the same weight as a positive match is treated as supporting - then move to the next short-listed candidate rather than picking the disqualified one anyway.

Low confidence (AC-7) has two independent triggers, and either one alone is enough:

1. **No candidate clears the score threshold** (`above_threshold` is `false` for every short-listed candidate) - the deterministic side of AC-7.
2. **A candidate clears the score threshold, but does not survive your own read.** If nothing in the short list is genuinely supported by its own `when_to_use`/`tells` language for this specific situation, that is low confidence too, even though the score cleared the bar. This is the check the deterministic score cannot make; do not skip it by treating an `above_threshold: true` candidate as automatically good enough.

If low confidence applies to an axis, do not force-pick: record a near-miss id and a one-line reason it does not genuinely fit, and move on - this axis will be blank in the composed output (Step 4). If every short-listed candidate scores identically (including a tie at zero, which happens when nothing matches at all), there is no genuine "closest" one to single out - say so plainly ("nothing in the short list showed a real signal") rather than presenting an arbitrary tie-broken id as if it were meaningfully closer.

Otherwise, pick the short-listed candidate whose `when_to_use`/`tells` language most specifically matches the situation, and write a one-line justification that names the actual phrase or concept that matched - quote or closely paraphrase the entry's own field, never invented reasoning disconnected from what the entry actually says (AC-3). This is true for every axis, including a candidate selected later during conflict resolution (Step 3) - a re-pick still needs a real justification, not a silent id swap.

**Step 3 - Check and resolve conflicts across the complete final set (AC-4).** This runs on every invocation, including when every axis was freshly recommended and nothing is fixed - two independently-picked entries can conflict with each other exactly as a fixed-and-recommended pair can.

1. Call the composer's conflict check on the complete final four-axis set (whatever Step 2 picked, plus any fixed values, plus a blank for any low-confidence axis) - this is the same call as Step 4's compose, so in practice you will often do this and Step 4 together in one call and inspect the `conflicts` field first:

   ```bash
   python "${CLAUDE_SKILL_DIR}/../writing-instruction-builder/scripts/build-instruction.py" --voice <id-or-omit> --tone <id-or-omit> --style <id-or-omit> --format <id-or-omit> --json
   ```

   A blank axis (from Step 2's low-confidence path) is simply omitted from the flags - `writing-instruction-builder` already supports composing with a blank axis, and this skill reuses that rather than inventing new behavior.
2. If `conflicts` is empty, there is nothing to resolve - proceed to Step 4.
3. If a conflict is found, classify it: does it involve at least one axis you recommended in Step 2 (recommender-controlled), or is it strictly between two axes the user fixed?
   - **At least one side recommender-controlled:** re-pick that axis, excluding the conflicting candidate - walk the rest of that axis's `short_list` (you already have full fields for every entry in it). There is no separate "widen to `full_ranked`" step: `short_list` already contains every candidate that clears `above_threshold` for that axis, however many there are (see Step 1) - nothing in `full_ranked` can ever qualify, since anything that did would already be in `short_list` by construction. A replacement must clear TWO conditions, not one - it is easy to stop at the first and skip the second, which is the one that actually matters: (1) non-conflicting; AND (2) genuinely relevant on your own read of its `when_to_use`/`tells`/`when_not_to_use`, exactly the Step 2 judgment call, applied again here - `above_threshold: true` is necessary (every short-listed candidate already has it) but not sufficient by itself, since the score is still just the keyword heuristic and a candidate can clear it while being a real-world non-fit (an institutional-editorial voice matching on one generic word, a how-to-guide format matching on unrelated vocabulary). A candidate that fails condition 2 is not an acceptable resolution; skip it and keep walking the short list. If BOTH conflicting axes are recommender-controlled, try the lower-precedence one first (format, then style, then tone, then voice - the reverse of the compose precedence order) but if its short list is exhausted with no resolution, try the same walk on the other axis before giving up.
   - **Both sides user-fixed:** you have no agency over either value. Skip straight to the warning path below.
   - **Every recommender-controlled axis involved has had its entire short list searched with no compatible-and-relevant candidate found:** only now is this the warning path. This should be rare - it means every candidate that genuinely clears the relevance bar on that axis also conflicts.
4. When a re-pick resolves the conflict, re-run Step 2's justification for the new candidate alone, then append the reason it was chosen over the higher-scoring original (for example "picked over X because X conflicts with the fixed voice"). Re-run the Step 3 conflict check against the updated set before moving on - a resolution can only be trusted once the check comes back clean.
5. When resolution was not possible (both fallback cases above), proceed to compose anyway with the conflict named alongside the output - this is `writing-instruction-builder`'s own verified behavior (warn, never block), reused here as the fallback for a conflict this skill genuinely could not avoid, not the default response to one it created and could have fixed itself.

**Step 4 - Compose or recommend-only (AC-5).** By default, call the composer on the final set (recommended + fixed values, any low-confidence axis passed as blank) exactly as in Step 3's call, and use its `instruction` as the output. Attach two kinds of notes alongside the composed prompt, never instead of it:

- A conflict note, only if Step 3 ended in the warning path (both-fixed, or no compatible-and-relevant candidate found after exhausting every recommender-controlled axis involved).
- A low-confidence note for every axis Step 2 left blank, naming the near-miss and why it did not genuinely fit.

If `--recommend-only` was passed, skip the compose call entirely and return the structured picks instead: axis, value (or blank), justification, any resolution note from Step 3, any conflict or low-confidence note.

## Constraints

Non-negotiable.

- **Never recommend a draft entry (AC-6).** `recommend.py` already filters to `stable`/`reference-quality` before scoring - do not work around this with a manual override, and do not recommend an entry by name from memory instead of from the script's output.
- **Every justification cites the entry's own field language (AC-3).** Quote or closely paraphrase `when_to_use`, `tells`, or `one_liner` - never invent a reason disconnected from what the entry's own fields say, including for a candidate picked during conflict resolution.
- **Report low confidence honestly, on either trigger (AC-7).** A score clearing the threshold is not sufficient on its own if your own read of the field language does not support it. Do not force-pick the least-bad option to avoid an empty axis.
- **Reuse the composer and its conflict check; never reimplement them.** Both live in `skills/writing-instruction-builder/scripts/build-instruction.py` and are called via subprocess with `--json`, the same cross-skill pattern `style-profile` already uses. Do not hand-roll the `avoid_with`/`pairs_well_with` symmetric-conflict rule or the voice-tone-style-format compose precedence a second time.
- **No catalog mutation.** This skill only reads `taxonomy/`, `taxonomy.json`, and `examples/`; it never writes to any of them.
- **No em-dashes or en-dashes** in any output, prose, or file you write. Use " - ". A pre-commit hook enforces this on committed files.

## Examples

Full recommendation, nothing fixed:

```
/writing-style-catalog:entry-recommender I need to tell my engineering team that a feature we committed to is getting cut this quarter, and I want them to trust the reasoning, not just accept the decision.
```

Partial recommendation, voice already decided:

```
/writing-style-catalog:entry-recommender explaining a database migration decision to the team voice=pragmatic-architect
```

Recommendation only, no composed prompt:

```
/writing-style-catalog:entry-recommender a public apology for a service outage --recommend-only
```

See `site/src/content/docs/guides/recommend-entries.md` for a detailed walkthrough with real example outputs, including the low-confidence and conflict-resolution paths.

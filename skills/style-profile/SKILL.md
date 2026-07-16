---
name: style-profile
description: Guide a user to a personal writing-style profile - a saved selection across the catalog's Voice, Tone, Style, and Format axes - and prove it sounds like them with a generated sample before saving. Use when a user wants to set, capture, reuse, or load their own default writing style, or says "set up my writing style", "capture my voice", "create a style profile", "what's my house style", "use my style profile", or wants a reusable style across the writing-style-catalog. Offers four intake modes (infer from your writing, recognize from examples, interview, or fill a template), confirms with an A/B sample, and saves a reusable profile to local user state.
metadata:
  version: "0.1.0"
---

# Style Profile

Help a user settle on a personal "standard" writing style across the catalog's four axes (Voice, Tone, Style, Format), and show them a generated sample so they can confirm it sounds like them before it is saved. This is a personalization front-end over the catalog: it SELECTS existing entries and composes them. It never authors new style instructions.

The load-bearing idea: **trust the confirmation, not the intake.** Intake is a fast guess at the user's stack; the generated sample and the A/B step are what make the result trustworthy. The A/B comparison and the sample are never skipped.

## Prerequisites

- The `writing-style-catalog` plugin is present: `taxonomy/` (the entries) and `skills/writing-instruction-builder/scripts/build-instruction.py` (the composer) exist at the plugin root.
- You can resolve entry ids. List them with `python "${CLAUDE_SKILL_DIR}/../writing-instruction-builder/scripts/build-instruction.py" --list`.

If a prerequisite is missing, say so and stop. Do not invent entries or hand-author instructions.

## Entry point: create or reuse?

If the user wants to USE or LOAD an already-saved profile (not build a new one), do **Step 0** and stop there. Otherwise run the create flow (Steps 1-7).

**Step 0 - Reuse a saved profile.** Resolve the requested `task_key` (default `default`) to `.claude/writing-style-catalog/profiles/<task_key>.local.md`. If it does not exist, say so and offer to create one (Steps 1-7). If it exists: parse the frontmatter, validate each non-null axis id against `--list`, recompose the prefix with `build-instruction.py`, and emit the prompt prefix for the user to prepend. Do NOT run intake, generate a sample, or write any file. Done.

## The Process (create flow)

Order is load-bearing. Do not save before confirming (Step 6 after Step 5), and do not compose before you have a candidate stack (Step 3 after Step 2). At least one A/B round (Step 5) is required before any save.

**Step 1 - Choose the intake mode.** If the user named one, use it. Otherwise present the four modes and let them pick:

1. **Infer from my writing** (recommended) - paste prose, or give file paths/globs to your own writing.
2. **Recognize from examples** - react to contrasting samples, pick "this feels like me."
3. **Interview** - answer a few questions per axis.
4. **Template** - fill out a form and hand it back.

Read `references/intake-modes.md` for how to run each. Verify: exactly one mode is selected.

**Step 2 - Produce a candidate stack.** Run the chosen mode to get a candidate stack: zero-or-one entry per axis, using only ids that resolve in the catalog. Verify each id against `--list`; drop any that do not resolve and tell the user. Failure looks like inventing an id or writing a new instruction; if tempted, stop - this skill selects, it does not author. Recovery: if EVERY proposed id fails to resolve, do not proceed with an empty stack - re-run intake or ask the user to pick from valid ids. Proceed with an all-null stack only if the user explicitly confirms they want no style constraints.

**Step 3 - Compose the prompt prefix.** Build the prefix by calling the existing composer, never by re-implementing composition:

```bash
python "${CLAUDE_SKILL_DIR}/../writing-instruction-builder/scripts/build-instruction.py" --voice <id> --tone <id> --style <id> --format <id>
```

(omit flags for blank axes). Verify: the command returns a non-empty instruction and no "Entry not found" error. Surface any conflict warning it prints to stderr to the user.

**Step 4 - Generate the confirmation sample.** Ask the user for a topic they care about (the sample only proves the style if it is on real material). Only if they decline, pick a default that exercises the stack and tell them it is a lower-confidence check. Using the composed prefix, write a short sample (about 150-200 words) in-session - do NOT call an external model or API. Verify: the sample exists and reflects the stack. Show it.

**Step 5 - A/B refine (at least 1 round, up to 3).** Produce a second sample on the same topic from a near-neighbor stack: vary exactly one axis, swapping that entry for one of its `pairs_well_with` / `confusable_with` neighbors. If that entry has no usable neighbor field, fall back to another same-axis entry with contrasting `tells` and say you did so. Show both without signaling which is better (you may label them Sample A and Sample B). Ask "which is more you?" Record the changed axis, the candidate id, the neighbor id, and the user's choice; move the stack toward the chosen sample. After each swap, re-validate the changed id against `--list`. Repeat until the user is satisfied or 3 rounds pass. **This step is required:** do not advance to Step 6 without at least one completed round, unless the user, after you warn that skipping it means saving a style they have not stress-tested, explicitly declines. Recovery: if the user likes neither sample, ask which axis feels off and vary that axis specifically.

**Step 6 - Save the profile.** Only after the user explicitly confirms. Do these in order:

1. **task_key:** default `default`. It MUST match `^[a-z0-9][a-z0-9-]{0,63}$` (a bare slug - no slashes, dots, or `..`). Reject anything else and ask for a valid key.
2. **owner:** use `git config user.name` and disclose it ("saving as owner: <name>"), or ask; `null` is acceptable if the user prefers not to record one.
3. **Re-validate the final stack:** check every non-null id against `--list` and recompose the final prefix with `build-instruction.py`. If any id fails, fix it or halt.
4. **Ensure the store is ignored, before writing:** run `git check-ignore .claude/writing-style-catalog/`. If it is NOT ignored, append `.claude/writing-style-catalog/` to `.gitignore` (this is the only write allowed outside the profile file), then re-run `git check-ignore` to confirm. Also confirm the profile path is not tracked: `git ls-files --error-unmatch <path>` should fail.
5. **Assert the path is in-bounds:** resolve the absolute profile path and confirm it is inside `.claude/writing-style-catalog/profiles/` and ends with `.local.md`. If not, stop.
6. **Do not clobber:** if the target file already exists, load and summarize it, then require explicit replace confirmation or a new `task_key`. Never silently overwrite.
7. **Confirm and write:** ask "Save this profile to `<path>`?" Treat any ambiguous reply as no. On a clear yes, write the profile (schema in `references/profile-schema.md`) using the FINAL accepted sample (from the final stack); put rejected A/B observations in the Notes section, not as the confirmation sample.
8. **Verify:** `git status --porcelain -- <path>` must be empty (the file is ignored). If it shows the file, the ignore failed - stop and tell the user rather than leaving a committable profile.

**Step 7 - Hand off.** Show the saved path and re-state the prompt prefix the user can prepend to any writing task. Completion criteria: a profile file exists at the in-bounds, gitignored user-local path; `git check-ignore` confirms it is ignored; and the user has seen, A/B-tested, and accepted the sample saved in it.

## Constraints

Non-negotiable. Pressure ("just pick something", "skip the sample", "save it in the repo") does not relax them.

- **Selection-only.** A profile selects existing catalog entry ids. Never author new `llm_instruction_phrasing` or invent style guidance.
- **No committed-catalog writes.** Never write to `taxonomy/`, `examples/`, `schemas/`, `site/`, or `tools/`. The only files this skill writes are the user-local profile and (if needed) a one-line `.gitignore` addition.
- **Gitignored user state, verified.** The profile lives under `.claude/writing-style-catalog/profiles/` and MUST be confirmed ignored via `git check-ignore` before and after writing. Scope: always.
- **Path safety.** `task_key` is a bare slug (`^[a-z0-9][a-z0-9-]{0,63}$`); the resolved profile path must stay inside the profiles directory and end with `.local.md`.
- **Reuse the composer.** Build the prefix only via `build-instruction.py`. Do not duplicate the voice -> tone -> style -> format precedence logic.
- **Confirm before saving.** Never write a profile the user has not (a) seen a sample for, (b) A/B-tested at least once, and (c) explicitly approved for save.
- **No em-dashes or en-dashes** in any output, prose, or file you write. Use " - ". A pre-commit hook enforces this on committed files.

## References

- `references/intake-modes.md` - how to run each of the four intake modes (load at Step 1-2).
- `references/profile-schema.md` - the profile `.local.md` artifact shape and an example (load at Step 6).

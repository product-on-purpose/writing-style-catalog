# style-profile

Guide a user to a personal writing-style profile - a saved selection across the catalog's Voice, Tone, Style, and Format axes - and prove it sounds like them with a generated sample before saving.

## What it does

`style-profile` is a personalization front-end over the catalog. It does not author new style instructions; it SELECTS existing entries, composes them via the `writing-instruction-builder`, and confirms the result with a sample the user reacts to. The output is a reusable personal profile (a personal recipe) saved to local user state.

## The loop

1. Pick an intake mode (infer from your writing, recognize from examples, interview, or fill a template).
2. Reach a candidate stack (one entry per axis, blanks allowed).
3. Compose the prompt prefix with `build-instruction.py`.
4. Generate a confirmation sample in-session.
5. A/B refine against a near-neighbor stack (up to 3 rounds).
6. Save the profile to `.claude/writing-style-catalog/profiles/<task_key>.local.md` (gitignored).
7. Hand off the saved path and the reusable prompt prefix.

## Intake modes

The recommended mode is "infer from my writing": point the skill at files/globs of your own writing (or paste a sample), and it attributes the nearest stack. The other modes (recognize, interview, template) suit users without a corpus. See `references/intake-modes.md`.

## Storage

Profiles are gitignored user-local state, one `.local.md` file per task (`default` first). They never enter the public catalog. See `references/profile-schema.md`.

## Design principle

Trust the confirmation, not the intake. The intake is a fast guess; the generated sample and the A/B choice are what make the profile trustworthy. The sample is never skipped.

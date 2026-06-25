# Intake Modes

Four ways to reach a candidate stack. All four converge on the same thing: zero-or-one existing entry id per axis (Voice, Tone, Style, Format). The stack is a starting guess; the confirmation sample and A/B step (SKILL.md steps 4-5) are what make it trustworthy. Lead with mode 1 when the user has writing to point at; it is the highest-signal.

Record which mode produced the stack as the profile's `provenance`, using exactly these values:

| Mode | provenance value |
|------|------------------|
| Infer from my writing | `infer-from-writing` |
| Recognize from examples | `recognize` |
| Interview | `interview` |
| Template | `template` |

## Mode 1 - Infer from my writing (recommended)

The user supplies their own writing; you attribute it to the nearest stack. Two input methods, same mode:

- **File paths or globs (preferred when available).** The user names files or a folder of their writing, e.g. `./posts/*.md` or `~/notes/essay.txt`. Read guards: first preview the matched files and their sizes; read at most 1-3 text files (or a few thousand words) - enough to attribute, not a whole archive. Skip binary, hidden, and non-text files. If a glob would read material outside the current workspace, or matches more than a handful of files, ask the user to confirm or narrow before reading. Prefer this method when a corpus exists: it is zero-friction and more representative than a paste.
- **Pasted text (universal fallback).** The user pastes 1-3 samples into the chat. Use this when there is no filesystem access or no corpus on disk.

How to attribute (v1 - in-session reasoning):
1. Read 1-3 representative samples (a few hundred words total is plenty).
2. For each axis, pick the entry whose `tells` and description best match what you observe. Read candidate entries from `taxonomy/<axis>/<id>/ENTRY.md`; the `tells` field lists spottable markers.
3. Output the stack with a one-line rationale per axis tying the choice to a specific observed marker (e.g. "you open by naming a framework before recommending -> senior-consultant").
4. Present it as a STARTING candidate, not a verdict. Say so. The A/B loop will correct it.

Hardening path (later, not v1): the same cross-vendor forced-choice attribution validated in the adherence-gate pilot can replace in-session reasoning for higher rigor. Until then, the confirmation loop is the safety net - do not present attribution as certain.

Recovery: if the corpus is tiny or mixed (multiple styles), say what you see, pick the dominant style, and lean harder on the A/B step.

## Mode 2 - Recognize from examples

People recognize their style better than they describe it. Show contrasts and let them pick.

1. Pick an axis to disambiguate (start with Voice, usually the most load-bearing).
2. Show two short contrasting samples on one shared topic that differ only on that axis - draw from `examples/diff-pairs/` if a relevant pair exists, otherwise generate a one-axis-varied pair in-session.
3. Ask "which feels more like you?" Record the pick; that narrows the axis.
4. Run at most ONE forced-choice pair per axis during intake (not every axis needs one). Further refinement of an axis belongs to the A/B step (SKILL.md Step 5), not here, so an axis is touched at most once in this mode.

Recovery: if neither sample fits, ask what is off about both; offer one alternative on that axis, still counting as that axis's single intake pass.

## Mode 3 - Interview

For users with no corpus and no patience for A/B clicking.

1. Ask at most ~2 questions per axis, phrased in plain language, not jargon:
   - Voice: "Who should the reader feel they are hearing from?" (an expert peer, a mentor, a reporter, ...)
   - Tone: "Should it feel warm and encouraging, or matter-of-fact and direct?"
   - Style: "Lead with the decision, walk through reasoning, tell a story, or compare options?"
   - Format: "What are you usually writing - a decision doc, a post, a short message, a reflection?"
2. Map the answers to the closest entry per axis. Confirm your mapping in one line before composing.

Recovery: if an answer maps to two entries, name both and let the A/B step decide.

## Mode 4 - Template

A long-form form the user fills in their own time.

1. Emit a fillable template covering the four axes, each with a short prompt and 2-3 example entry ids to react to. Keep it copy-pasteable.
2. When the user returns the filled template, parse each axis answer into an existing entry id (map free text to the nearest id; do not invent).
3. Confirm the parsed stack in one line before composing.

Recovery: if a filled field matches no entry, surface the closest 2-3 ids and ask the user to pick.

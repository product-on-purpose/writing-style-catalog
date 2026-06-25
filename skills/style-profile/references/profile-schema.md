# Profile Artifact Schema

A saved profile is one gitignored, user-local Markdown file with YAML frontmatter (the selection) and a body (notes plus the confirmation sample). It reuses the catalog's recipe shape: a profile is a personal recipe.

## Location

```
.claude/writing-style-catalog/profiles/<task_key>.local.md
```

- `<task_key>` is `default` unless the user is building a task-specific profile (e.g. `adr`, `marketing`). It MUST be a bare slug matching `^[a-z0-9][a-z0-9-]{0,63}$` - no slashes, dots, or `..`. Reject anything else (it could escape the profiles directory). Before writing, resolve the absolute path and confirm it is inside `.claude/writing-style-catalog/profiles/` and ends with `.local.md`.
- The whole `.claude/writing-style-catalog/` path MUST be gitignored. Verify with `git check-ignore .claude/writing-style-catalog/` before writing; if it is not ignored, add the line `.claude/writing-style-catalog/` to `.gitignore` and re-check. After writing, confirm with `git status --porcelain -- <path>` returning empty. The `.local.md` suffix marks it as local user state, matching the plugin-settings convention.
- One file per `task_key`. A new task creates a new file. If the target `task_key` file already exists, do NOT silently overwrite: load and summarize it, then require an explicit replace confirmation or a different `task_key`.

## Frontmatter (required fields)

```yaml
---
voice: pragmatic-architect      # entry id or null
tone: candid                    # entry id or null
style: decision-log             # entry id or null
format: adr                     # entry id or null
owner: <user name or handle, or null>
task_key: default
created: 2026-06-25
provenance: infer-from-writing  # exactly one of: infer-from-writing | recognize | interview | template
---
```

- Each axis is an existing entry id or `null` (a blank axis is allowed).
- All four axis keys are present even when null, so the file is a complete record of the stack.
- `owner`: default to `git config user.name` (disclose which value you used) or ask the user. `null` is acceptable if the user prefers not to record one - do not invent a handle.
- `provenance` records how the stack was reached, for later auditing and re-runs. Use exactly one of the four values above (the mapping table is in `intake-modes.md`).
- `created` is today's date in YYYY-MM-DD.

## Body

```markdown
# Style profile: default

## Composition

| Axis | Entry |
|------|-------|
| Voice  | pragmatic-architect |
| Tone   | candid |
| Style  | decision-log |
| Format | adr |

## Prompt prefix

<the composed instruction from build-instruction.py, ready to prepend>

## Confirmation sample

<the ~150-200 word sample the user accepted, on its topic>

## Notes

<optional: what the user liked, what was rejected in A/B, any caveats>
```

## Reusing a saved profile

To reuse a profile later: read the file, re-run `build-instruction.py` with its axis ids to regenerate the prompt prefix (or use the stored prefix), and prepend it to the writing task. No re-intake needed.

## Example

`.claude/writing-style-catalog/profiles/default.local.md`:

```markdown
---
voice: senior-consultant
tone: diplomatic
style: problem-solution
format: executive-summary
owner: jp
task_key: default
created: 2026-06-25
provenance: infer-from-writing
---

# Style profile: default

## Composition

| Axis | Entry |
|------|-------|
| Voice  | senior-consultant |
| Tone   | diplomatic |
| Style  | problem-solution |
| Format | executive-summary |

## Prompt prefix

Write in a senior-consultant voice... (diplomatic)... (problem-solution)... (executive-summary)...

## Confirmation sample

(the accepted ~180-word sample)

## Notes

Chose diplomatic over candid in round 2 - the candid sample read too blunt for stakeholder memos.
```

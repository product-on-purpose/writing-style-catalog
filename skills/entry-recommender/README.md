# entry-recommender

Recommendation skill for the writing-style-catalog plugin.

## Skills

- `entry-recommender` - Recommend a voice/tone/style/format combination from the stable catalog for a described writing situation, and compose the prompt in the same step.

## How it Works

`scripts/recommend.py` loads every `stable`/`reference-quality` entry per axis (draft entries, including Hold-20, are never even read - see AC-6 in `docs/internal/entry-recommender-spec.md`) and scores the entire pool against the described situation, weighted by field (`when_to_use` counts most) and by each matching word's rarity across the stable corpus (an IDF-style weighting - a word common to most entries contributes little; a word distinctive to a few is a real signal). It returns a short list with full field content plus the rest of the ranked pool for conflict-resolution fallback.

The actual pick, justification, conflict resolution, and composition (Phases 3-6 of the implementation plan) run in the skill's own reasoning per `SKILL.md`, reusing `skills/writing-instruction-builder/scripts/build-instruction.py` (via subprocess, its `--json` flag) for conflict detection and composition rather than reimplementing either.

## Scripts

- `scripts/recommend.py --ephemeral-input-file PATH --json` (JSON payload `{"situation": "...", "voice": "...", ...}`, properly JSON-string-escaped, written by a file-write tool - never a shell command - to a scratchpad/temp location, filename ending in `.entry-recommender-input.json`) - score the catalog against a situation. This is the path `SKILL.md` requires: situation text is arbitrary, sometimes sensitive user prose, so it must never be interpolated directly into a shell command (shell-injection risk), hand-substituted into JSON without escaping (malformed-JSON risk, triggered by completely ordinary text like an embedded quote), or piped through a shell heredoc (a heredoc's closing delimiter can itself appear in the text, terminating it early and reintroducing shell execution). This flag deletes the file itself, guaranteed, immediately after reading it - success or failure - so cleanup does not depend on a separate step being remembered. Deletion only happens if the path is outside the repo, inside the system temp directory, AND correctly named - otherwise it raises instead of touching anything, so a caller path mistake fails loudly rather than deleting the wrong file.
- `scripts/recommend.py --input-file PATH --json` - same payload, but the file is NOT deleted. For a deliberately-kept test fixture reused across runs, not real situation text.
- `scripts/recommend.py --stdin --json` - same payload, from stdin. Not recommended for untrusted situation text via a shell heredoc (see above).
- `scripts/recommend.py --situation TEXT [--voice ID] [--tone ID] [--style ID] [--format ID] [--json]` - the same, for direct manual/terminal use where the caller controls their own shell escaping.
- `scripts/recommend.py --fetch AXIS ID --json` - full field content for one stable candidate (used when conflict resolution selects a candidate beyond the initial short list; rejects any non-stable id or id outside the requested axis).
- `scripts/recommend.py --list` - list all stable/reference-quality ids per axis.

## See Also

- `docs/internal/entry-recommender-spec.md` - the full spec (8 acceptance criteria).
- `docs/internal/release-plans/entry-recommender-implementation-plan.md` - the phase-by-phase build plan this skill implements.
- `site/src/content/docs/guides/recommend-entries.md` - detailed usage guide with real example outputs.

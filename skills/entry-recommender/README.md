# entry-recommender

Recommendation skill for the writing-style-catalog plugin.

## Skills

- `entry-recommender` - Recommend a voice/tone/style/format combination from the stable catalog for a described writing situation, and compose the prompt in the same step.

## How it Works

`scripts/recommend.py` loads every `stable`/`reference-quality` entry per axis (draft entries, including Hold-20, are never even read - see AC-6 in `docs/internal/entry-recommender-spec.md`) and scores the entire pool against the described situation, weighted by field (`when_to_use` counts most) and by each matching word's rarity across the stable corpus (an IDF-style weighting - a word common to most entries contributes little; a word distinctive to a few is a real signal). It returns a short list with full field content plus the rest of the ranked pool for conflict-resolution fallback.

The actual pick, justification, conflict resolution, and composition (Phases 3-6 of the implementation plan) run in the skill's own reasoning per `SKILL.md`, reusing `skills/writing-instruction-builder/scripts/build-instruction.py` (via subprocess, its `--json` flag) for conflict detection and composition rather than reimplementing either.

## Scripts

- `scripts/recommend.py --input-file PATH --json` - score the catalog against a situation described in a JSON file (`{"situation": "...", "voice": "...", ...}`). This is the path `SKILL.md` requires: situation text is arbitrary user prose that can contain quotes, dollar signs, or other shell metacharacters, so it must never be interpolated directly into a shell command - the JSON file avoids that entirely.
- `scripts/recommend.py --situation TEXT [--voice ID] [--tone ID] [--style ID] [--format ID] [--json]` - the same, for direct manual/terminal use where the caller controls their own shell escaping.
- `scripts/recommend.py --fetch AXIS ID --json` - full field content for one stable candidate (used when conflict resolution selects a candidate beyond the initial short list; rejects any non-stable id).
- `scripts/recommend.py --list` - list all stable/reference-quality ids per axis.

## See Also

- `docs/internal/entry-recommender-spec.md` - the full spec (8 acceptance criteria).
- `docs/internal/release-plans/entry-recommender-implementation-plan.md` - the phase-by-phase build plan this skill implements.
- `site/src/content/docs/guides/recommend-entries.md` - detailed usage guide with real example outputs.

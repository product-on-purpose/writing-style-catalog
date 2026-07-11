# writing-instruction-builder

Core skill for the writing-style-catalog plugin.

## Skills

- `writing-instruction-builder` - Compose a writing instruction from axis entries (formerly `compose-instruction`; renamed in ADR 0015 so the skill name matches its directory)

## How it Works

The skill reads taxonomy entry files directly from `taxonomy/` at the plugin root and builds a composed instruction string from the `llm_instruction_phrasing` field of each selected entry, using a dependency-free frontmatter parser (Python standard library only). It needs no pre-built index or other build artifact.

## Entry IDs

List every available entry ID with `python skills/writing-instruction-builder/scripts/build-instruction.py --list` (run from a repo checkout root), or browse `taxonomy/voices/`, `taxonomy/tones/`, `taxonomy/styles/`, `taxonomy/formats/`.

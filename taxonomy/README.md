# taxonomy/

The catalog. This is the source of truth for the Writing Style Library.

It holds 60 entries across four axis directories, 15 each:

- `voices/` - persistent writer identity (worldview, archetype). Stable across contexts.
- `tones/` - situational register layered on top of voice.
- `styles/` - cognitive and rhetorical pattern (how ideas are sequenced).
- `formats/` - visual and structural container (headings, tables, section templates).

Each entry follows the atomic-folder pattern: `taxonomy/<axis>/<entry-id>/ENTRY.md` (frontmatter + body), with an `examples/` subdirectory alongside. Every `ENTRY.md` carries an `llm_instruction_phrasing` block, which is what the `writing-instruction-builder` skill assembles into a prompt prefix.

`taxonomy.json` at the repo root is the generated machine index of this tree (built by `tools/build-indexes.py`).

To add or edit an entry, follow `AGENTS.md` (How to Add an Entry), validate against the axis schema in `schemas/`, and run `python tools/validate.py`. See `REPOSITORY.md` for how this folder fits the whole repo.

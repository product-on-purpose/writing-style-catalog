# schemas/

The catalog's data contract: JSON Schema definitions that every entry and example must satisfy.

- `entry.universal.schema.json` - the shared entry shape, plus the per-axis schemas `voice`, `tone`, `style`, and `format` that extend it.
- `example.schema.json` - worked example files under `examples/`.
- `diff-pair.schema.json` - the side-by-side comparison files.

`tools/validate.py` checks every `ENTRY.md` and example against these schemas; a file that does not conform fails the build. The schemas also document the required frontmatter fields, so they double as the authoritative reference for what an entry must contain.

Changing a schema is a governed action: it requires a version bump and a new ADR in `docs/internal/adr/`, and every existing file that references the changed schema must be updated in the same change. See the Schema Safety section in `AGENTS.md`.

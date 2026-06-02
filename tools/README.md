# tools/

Catalog integrity and indexing: the source-side tooling. These operate on the catalog source (`taxonomy/` and `examples/`) and produce the machine index. Mental model: `tools/` validate and index the catalog; `scripts/` publish it.

- `validate.py` - the integrity gate. Checks slug format, `ENTRY.md` presence, frontmatter validity (PyYAML), JSON Schema conformance, the no-em-dash/en-dash rule, `review_status` values, and that cross-references resolve. All checks must pass before committing.
- `build-indexes.py` - generates `taxonomy.json` (the machine-readable catalog index) from entry frontmatter.
- `diff-pair-generator.py` - a CLI for authoring diff-pair files from vertical-slice examples (`--topic`, `--axis`, `--a`, `--b`).
- `taxonomy.py` - a controlled-vocabulary module (format domains/families, voice families). Drafted for a future phase; imported by the tools when wired in.

`validate.py` and `build-indexes.py` are wired into the pre-commit hook and CI. See `REPOSITORY.md` for how `tools/` relates to `scripts/`.

# schemas/

The catalog's data contract: JSON Schema definitions that every entry and example must satisfy.

- `entry.universal.schema.json` - the shared entry shape, plus the per-axis schemas `voice`, `tone`, `style`, and `format` that extend it.
- `example.schema.json` - worked example files under `examples/`.
- `diff-pair.schema.json` - the side-by-side comparison files.

`tools/validate.py` checks every `ENTRY.md` and example against these schemas; a file that does not conform fails the build. The schemas also document the required frontmatter fields, so they double as the authoritative reference for what an entry must contain.

## Changing a schema

Six schemas are **frozen** as of [ADR 0019](../docs/internal/adr/0019-schema-freeze-and-change-policy.md): `entry.universal`, `voice`, `tone`, `style`, `format`, and `example`. `example` is included because contributors author example files by hand (CONTRIBUTING requires one with every new entry), so it is a contributor contract, not a generated-artifact schema. `diff-pair` is **not** frozen, since its generator is still evolving, but the classes below still govern it in full.

What a change costs depends on its class. The test: **would this edit change the verdict on any conceivable document, not just the files in this repo?** Checking only the current corpus is not enough: setting `additionalProperties: false` or narrowing a `$ref` can leave all 117 entries passing while rejecting documents the published schema previously accepted.

- **Class A, annotation.** An allowlist and nothing else: `title`, `description`, `$comment`, `examples`, plus reordering a parser cannot observe. A normal PR, no ADR, no version bump, no entry migration. Note "annotation-only, class A" in the PR body.
- **Class B, additive optional.** A new **optional** property, or a widened `enum`, `pattern`, or bound. Minor version bump plus a `CHANGELOG.md` note.
- **Class C, breaking or unclear.** New required property, removal, rename, narrowing, optional to required, **and every keyword not named in A or B** - including `$id`, `$schema`, `$ref`, `$defs`, `additionalProperties`, `unevaluatedProperties`, `format`, and the combinators. An ADR, a **major** version bump, and every affected file migrated in the same change with `validate.py` green before merge.

**The default is C.** Unclear resolves to the most expensive class. A change to `entry.universal` or a shared `$def` is class C for every schema that `$ref`s it, since the per-axis schemas compose it.

Note that the freeze is currently an internal discipline rather than an external guarantee: every `$id` resolves to `main` and the per-axis schemas `$ref` the shared schema relatively, so there is no versioned artifact to pin yet. See ADR 0019 decision 3.

ADR 0019 is the authority; the Schema Safety section in `AGENTS.md` carries the same summary table.

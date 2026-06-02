# examples/

Worked output examples: the proof that each catalog entry produces what it claims. Source material for the generated example, recipe, and diff-pair pages on the docs site.

Three kinds:

- `vertical-slices/` - examples grouped by anchor topic. A vertical slice shows one entry applied to a shared writing task, so entries can be compared on the same subject.
- `horizontal-slices/` - recipes: complete multi-axis combinations (a voice, tone, style, and format together) for a common writing task.
- `diff-pairs/` - side-by-side before/after comparisons that hold a topic fixed and vary a single axis, isolating exactly what that axis changes.

The site generator (`scripts/gen-site.mjs`) reads this tree and renders it into `site/src/content/docs/examples/`, `.../recipes/`, and the diff-pair pages (gitignored, rebuilt each build). Every example validates against `schemas/example.schema.json` (or `schemas/diff-pair.schema.json`) via `python tools/validate.py`. See `REPOSITORY.md` for the full picture.

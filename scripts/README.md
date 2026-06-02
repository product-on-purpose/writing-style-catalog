# scripts/

Documentation-site generation: the output-side tooling. These transform the catalog source into the Markdown and MDX pages the Astro Starlight site builds. Mental model: `tools/` validate and index the catalog; `scripts/` publish it.

- `generate_site_pages.py` - reads `taxonomy/` and `examples/` and renders the catalog into `docs/` (entry/reference pages, diff-pair pages, recipe pages, template pages, and indexes), emitting Starlight-correct links.
- `check_generated_fresh.py` - the freshness guard. Regenerates the pages into a temporary directory and compares them against the committed `docs/` tree, failing if anything drifted. This is what keeps the committed generated pages honest.

Both are wired into the pre-commit hook and CI. Regenerate after any edit to `taxonomy/` or `examples/` (`python scripts/generate_site_pages.py`), then run the freshness check. See `REPOSITORY.md` for the full build pipeline.

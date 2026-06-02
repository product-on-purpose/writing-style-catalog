# scripts/

Documentation-site generation: the output-side tooling. `gen-site.mjs` transforms the catalog source into the Markdown and MDX pages the Astro Starlight site builds. Mental model: `tools/` validate and index the catalog; `scripts/` publish it.

- `gen-site.mjs` - a zero-dependency Node generator. Reads `taxonomy/` and `examples/` and renders the catalog into `site/src/content/docs/` (entry/reference pages, diff-pair pages, recipe pages, template pages, and indexes), emitting relative, Starlight-correct links. Run it directly with `node scripts/gen-site.mjs`, or via the site build (`cd site && npm run build`, which runs the generator then `astro build`).

The generated catalog under `site/src/content/docs/{reference,examples,recipes,templates}/` is gitignored and rebuilt on every build (Pattern S), so there is no committed copy and no drift guard. Regenerate after any edit to `taxonomy/` or `examples/`. See `REPOSITORY.md` for the full build pipeline.

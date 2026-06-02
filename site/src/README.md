# src/

The Astro site source. The documentation site is Astro + Starlight; this folder holds the app code that renders the catalog into the published site (Pattern S: the app lives under `site/`).

- `content.config.ts` - declares the `docs` content collection with the stock Starlight `docsLoader()` over `src/content/docs/`.
- `content/docs/` - the Starlight content root. Hand-authored narrative pages (`index.mdx`, `concepts/`, `guides/`, `design-standards/`, `governance/`) are committed; the generated catalog (`reference/`, `examples/`, `recipes/`, `templates/`) is emitted here by `scripts/gen-site.mjs` and gitignored.
- `components/DiffPair.astro` - the side-by-side diff-pair component the generated diff-pair pages import.
- `styles/custom.css` - Starlight theme overrides (accent color and tweaks).

The site is configured in `site/astro.config.mjs` and built with `cd site && npm run build` (which runs the generator first, then `astro build`). See `REPOSITORY.md` for the full pipeline.

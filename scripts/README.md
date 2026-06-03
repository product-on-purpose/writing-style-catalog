# scripts/

Documentation-site generation: the output-side tooling. `gen-site.mjs` transforms the catalog source into the Markdown and MDX pages the Astro Starlight site builds. Mental model: `tools/` validate and index the catalog; `scripts/` publish it.

- `gen-site.mjs` - a zero-dependency Node generator. Reads `taxonomy/` and `examples/` and renders the catalog into `site/src/content/docs/` (entry/reference pages, diff-pair pages, recipe pages, template pages, and indexes), emitting relative, Starlight-correct links. Run it directly with `node scripts/gen-site.mjs`, or via the site build (`cd site && npm run build`, which runs the generator then `astro build`).

The generated catalog under `site/src/content/docs/{reference,examples,recipes,templates}/` is gitignored and rebuilt on every build (Pattern S), so there is no committed copy and no drift guard. Regenerate after any edit to `taxonomy/` or `examples/`. See `REPOSITORY.md` for the full build pipeline.

## Conformance checks (family Astro site standard)

These run in CI (`.github/workflows/validate.yml`) and can be run locally after `cd site && npm run build`:

- `check-no-dashes.mjs` - fails if any tracked authored or source file (`.md`/`.mdx`/`.mjs`/`.ts`/`.astro`/`.css`/`.yml`/`.yaml`/`.py`) contains an em-dash (U+2014) or en-dash (U+2013). The CI enforcement of the `.pre-commit-config.yaml` `no-em-dashes` hook (a contributor who bypasses pre-commit can otherwise land a dash). Excludes `docs/internal/` (whose markdown is already dash-scanned by `tools/validate.py`, so this avoids redundant coverage and the imported-artifact modification trap) and `_LOCAL/`. Runs in the `validate` job.
- `check-rendered-links.mjs` - walks the built `dist/*.html` and fails on any browser-broken internal link; with `STRICT_ANCHORS=1` it also enforces `#anchor` resolution. Covers `.md`- and `.mdx`-derived pages alike (it reads rendered HTML). Runs in both the PR `build-site` job (`validate.yml`) and the deploy build (`build-site.yml`), so the deployed artifact is guarded too. Clause 14.11.
- `check-route-parity.mjs` - compares the built route set against the committed `route-manifest.txt` and fails if a published route disappears without a redirect. Regenerate the baseline after an intentional route change: `node scripts/check-route-parity.mjs --update`. Runs in both the PR `build-site` job and the deploy build. Clause 14.11.
- `site-base.mjs` - the single source for the Pages base path, read from `site/astro.config.mjs` so link validators never redeclare the base literal (clause 14.7).

Ported from pm-skills (the family donor of the build-aware validators). The build-time link resolver `remark-resolve-links` (pm-skills' 4th validator, which rewrites `.md` links to Starlight slugs at build time, in both the markdown and `@astrojs/mdx` pipelines) is a documented follow-up; until it lands, author internal cross-page links as relative slug URLs (e.g. `../../guides/compose-instruction/`), not file-relative `.md` paths.

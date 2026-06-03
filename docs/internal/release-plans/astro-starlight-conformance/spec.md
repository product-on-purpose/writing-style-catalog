# Astro Starlight conformance: spec

> Conformance target and acceptance criteria for bringing this repo's Astro +
> Starlight docs site to full compliance with the Product on Purpose family Astro
> site standard (`agent-plugins/standards/domains/astro-sites/SITE-STANDARD.md`,
> clauses 14.1 to 14.11). Source of truth for this effort:
> `agent-plugins/standards/domains/astro-sites/rollout/writing-style-catalog.md`
> (the conformance packet) and the 2026-06-02 implementation audit.

## Context

The Pattern S migration already shipped to `main` (PR #11, `197c426`): the app
lives under `site/`, content is read by the stock Starlight `docsLoader()`, the
site generator is a zero-dependency Node `scripts/gen-site.mjs` (the Python
generator is gone), `robots.txt` and the `#5C7CFA` accent are in place. This
effort is conformance polish against `main`, not a migration. The baseline build
is green (111 pages).

## Verified scorecard (against `main @ 197c426`, re-confirmed this effort)

| Clause | Status | Note |
|---|---|---|
| 14.1 Pattern S | PASS | `site/`, stock `docsLoader()`, `docsSchema()`. |
| 14.2 Framework | PASS (branding gap) | Astro + Starlight; `site` set; mermaid before starlight; mdx after starlight. Mermaid unbranded. |
| 14.3 Generate from source | PASS | Node `scripts/gen-site.mjs`; surviving `tools/*.py` are taxonomy tooling, not a site generator. |
| 14.4 Drift guard | PASS | `taxonomy.json` diff guard in CI; generated catalog gitignored and rebuilt. |
| 14.5 No committed build output | PASS | `dist/`, `.astro/` gitignored; nothing tracked. |
| 14.6 Deploy + PR build + pins | PASS | `@v5` action set; `node-version-file: .nvmrc`; deploy in `build-site.yml`, PR `build-site` job in `validate.yml`. |
| 14.7 Base single source | PASS | `base` once in `site/astro.config.mjs`; generator emits relative links. |
| 14.8 Versions + Node | PASS (minor) | `engines.node >=22.12.0`; `.nvmrc=24`; CI reads `node-version-file`. No `.node-version` companion. |
| 14.9 Search + SEO | PASS | Pagefind + sitemap; `robots.txt` + favicon present; no `og:image` (preset-owned). |
| 14.10 No config sidecars | PASS | None present. |
| 14.11 Link/route integrity | FAIL | None of the build-aware validators present (shared family gap). |
| Carry-over | - | Starlight `title` still "Writing Style Library" after the rename; em/en-dash check only in pre-commit, not CI. |

One packet imprecision corrected during verification: the deploy action chain
(`upload-pages-artifact` / `deploy-pages` / `environment`) lives in
`.github/workflows/build-site.yml`; the PR non-deploying `build-site` job lives in
`.github/workflows/validate.yml`. The packet described both as in `validate.yml`.
Evidence is split across the two workflow files; 14.6 still PASSes.

## Corrections in scope

1. P2 (branding) Brand mermaid: add `themeVariables` (lineColor `#5C7CFA`,
   system-ui, 14px) to the `mermaid()` call in `site/astro.config.mjs`.
2. ~~P2 (identity) Fix the Starlight `title` to "Writing Style Catalog".~~
   **REJECTED - packet conflicts with repo reality.** ADR 0014 (and the CHANGELOG)
   record that the 2026-06-02 rename changed only the slug/identifiers and
   deliberately RETAINED the display title "Writing Style Library" (39 authored
   references use it; the packet's title item was the only "Catalog" display name
   in the repo). The Starlight title is intentional, not stale. Left as-is, with a
   config comment citing ADR 0014.
3. P2 (family rule) Add the em/en-dash check to CI (currently pre-commit only, so
   a contributor who bypasses pre-commit can land a dash).
4. P1/P2 (14.11) Add link/route guards: port `check-rendered-links` (anchors
   enforced) and `check-route-parity` from pm-skills, wired into the PR
   `build-site` job. Derive the base from the single source
   (`site/astro.config.mjs`) rather than redeclaring the literal, so the port does
   not import pm-skills' one live 14.7 violation (its hardcoded `BASE`).
5. (optional) Add `.node-version=24` companion alongside `.nvmrc`.

## Out of scope

- Building the shared reusable CI workflow or the `@product-on-purpose/astro-docs-preset`
  (family infrastructure that lives in other repos; "adopt the shared workflow" is
  blocked on infra that does not exist yet, so 14.11 is satisfied by an in-repo
  port now, which the packet sanctions as the fallback).
- `verify-edit-links` and `remark-resolve-links` (the other two of the four
  validators): not named in the packet's correction. The generator already emits
  relative links (14.7) and the rendered-link check is the regression guard, so
  the named pair is the in-scope set.
- Any change to other repos.

## Acceptance criteria (done = all true)

- Mermaid renders with `#5C7CFA`. (The Starlight `title` stays "Writing Style
  Library" per ADR 0014; the packet's title-change item is rejected as conflicting
  with that decision.)
- The em/en-dash check runs in CI; a rendered-link check (with anchors enforced)
  and a route-parity check run against `dist` in the PR build and are green
  (mdx-derived pages included, since the check walks rendered `dist/*.html`).
- `cd site && npm run build` green; `git ls-files` shows no tracked build output.
- The ported validators derive the base from `site/astro.config.mjs` (no second
  base literal introduced).
- PR(s) prepared, not pushed or merged without maintainer confirmation.

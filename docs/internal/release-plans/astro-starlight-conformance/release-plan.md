# Astro Starlight conformance: release plan

> The executing agent OWNS and UPDATES this file. Check a box only after its
> acceptance check passes. Keep the repo buildable and CI green between steps.
> Spec: [`spec.md`](spec.md).

Branch: `chore/astro-starlight-conformance` (off `main @ 197c426`).

## Checklist

- [x] Confirm `main` is Pattern S and builds green; create this release-plan
      folder with `spec.md` + `release-plan.md`.
      - Acceptance: `cd site && npm run build` green (111 pages). Done at baseline.
- [x] **P2** Brand mermaid (`themeVariables`: lineColor `#5C7CFA`, system-ui, 14px)
      in `site/astro.config.mjs`.
      - Acceptance: build green; mermaid config carries `themeVariables`. Mirrors
        the pm-skills / thinking-framework-skills block.
- [x] **P2** ~~Fix Starlight `title` to "Writing Style Catalog".~~ REJECTED: the
      packet conflicts with ADR 0014, which retained the display title "Writing
      Style Library" in the rename (only the slug changed). Title left as-is with a
      config comment citing ADR 0014.
      - Acceptance: title stays "Writing Style Library"; discrepancy flagged.
- [x] **P2** Add the em/en-dash check to CI: `scripts/check-no-dashes.mjs` wired
      into `validate.yml`'s `validate` job (runs on push + PR).
      - Acceptance: `node scripts/check-no-dashes.mjs` exits 0; the check is a CI step.
- [x] **P1/P2** Add link/route guards (14.11): `scripts/site-base.mjs` (single
      source for the base), `scripts/check-rendered-links.mjs` (anchors enforced),
      `scripts/check-route-parity.mjs` + `scripts/route-manifest.txt`; wired into
      the `build-site` job in `validate.yml` after `npm run build`.
      - Acceptance: build green; both validators exit 0 against `dist`; base
        derived from `site/astro.config.mjs` (no second literal). Done.
- [x] Fix the 16 pre-existing broken internal links the rendered-link guard
      surfaced (file-relative `.md` links in hand-authored pages -> relative-slug
      URLs). Required to land the guard green.
      - Acceptance: rendered-link check PASS (0 broken); no residual `.md` cross-links.
- [x] (optional) Add `.node-version=24` companion alongside `.nvmrc`.
      - Acceptance: file present, content `24`. Done.
- [x] Final: `cd site && npm run build` green; `git ls-files` shows no build
      output; dash check + link check + route parity all green.
- [x] Adversarial review of the diff (6-dimension multi-agent workflow, each finding
      adversarially verified); wrote the findings doc; applied the actionable fixes.
- [ ] Open PR(s); CI green; await maintainer review. (Do NOT push or merge without
      maintainer confirmation.)

## Execution log

- (baseline) `chore/astro-starlight-conformance` cut from `main @ 197c426`; site
  build green at 111 pages; release-plan folder created.
- Branded mermaid in `site/astro.config.mjs`; added `.node-version=24`.
- C2 (fix the Starlight title) REJECTED after verification: ADR 0014 + CHANGELOG
  retain the display title "Writing Style Library" (only the slug was renamed); 39
  authored references use it. Reverted the title to "Writing Style Library" with a
  config comment citing ADR 0014, and flagged the packet/repo conflict.
- Added `scripts/check-no-dashes.mjs` (dash check, built from code points) and
  wired it into the `validate` job. Tree is clean (and `docs/internal/` is clean
  too, 0 of 25 files).
- Ported the 14.11 link/route guards from pm-skills: `scripts/site-base.mjs`
  (base from `site/astro.config.mjs`, NOT a hardcoded literal - avoids importing
  pm-skills' one live 14.7 violation), `check-rendered-links.mjs`,
  `check-route-parity.mjs` + a 111-route `route-manifest.txt`. Wired both into the
  PR `build-site` job.
- The rendered-link guard caught 16 pre-existing browser-broken internal links
  (file-relative `.md` links in 7 hand-authored pages). Fixed all 16 to
  relative-slug URLs (decision: fix-now, keep validators donor-faithful;
  `remark-resolve-links` is the documented follow-up). Re-ran: build green (111),
  rendered-link 0 broken / 0 broken anchors, route parity 111/111, dash check
  clean, no tracked build output.
- Adversarial review (workflow `wsl-astro-conformance-review`, 17 agents): 6
  findings survived verification, 5 refuted (the refuted set confirmed the title
  revert, the link fixes, scope, and the route-manifest are all correct). Applied:
  (1) wired the two 14.11 guards into the deploy build `build-site.yml` too, not
  just the PR build (P2: the guards now run on the artifact that actually deploys);
  (2) extended `check-no-dashes.mjs` to scan `.py` and de-literalized
  `tools/validate.py`'s own detector via `chr(0x2014/0x2013)` so it stays dash-free
  (P2 coverage gap); (3) corrected the `docs/internal/` exclusion rationale (it is
  excluded because `validate.py` already dash-scans `docs/`, not because it is
  "read-only"); (4) documented the bare-relative-link skip limitation in
  `check-rendered-links.mjs` (P3); (5) fixed the README extension list (P3).
  Accepted without change: `.node-version` drift (P3) - kept as the packet's
  optional local-dev companion; `.nvmrc` remains the CI source of truth (both pin
  24). Full findings doc:
  `agent-plugins/standards/domains/astro-sites/rollout/2026-06-02_astro-standard_writing-style-catalog_review-findings.md`.
  Re-verified after fixes: build green, all guards green, `validate.py` green.

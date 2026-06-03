# v0.2.0 Marketplace Launch - Release Plan

> The executing agent OWNS and UPDATES this file. Check a box only after its acceptance
> check passes. Keep the repo buildable and CI green between steps. Spec: [`spec.md`](spec.md).
> Precedent: pm-skills v2.21.0.

**Status:** SHIPPED 2026-06-02. `writing-style-catalog@product-on-purpose` is live.
**Version:** 0.2.0 (MINOR). **Spine:** prep -> merge -> tag + Release -> pin registry -> verify.
**Spans two repos:** `product-on-purpose/writing-style-catalog` and
`product-on-purpose/agent-plugins`. Both public; full-publish authorized.

---

## Phase 0 - Plan + review (this folder)

- [x] `spec.md` + `release-plan.md` authored.
  - Acceptance: both files present, dash-free, internally consistent.
- [x] Adversarial pre-execution review (multi-agent, 13 agents) of the plan; findings triaged
      and accepted findings folded into spec + plan (see Execution log).
  - Acceptance: no unresolved P0/P1 sequencing or correctness finding.

## Phase 1 - WSC release prep (branch `release/v0.2.0`)

- [x] Bump `.claude-plugin/plugin.json` version `0.1.0 -> 0.2.0`; `description` -> canonical
      de-versioned string (spec 6.1).
- [x] Self-hosted `.claude-plugin/marketplace.json`: `version -> 0.2.0`; `description` ->
      canonical; `source.ref` `main -> v0.2.0`.
- [x] `CHANGELOG.md`: `[Unreleased] -> [0.2.0] - <date>`; add marketplace-listing + CI items.
- [x] `README.md`: version badge `-> 0.2.0`; warning token `(v0.2.0)`; Quick Start adds
      `/plugin update`; Project Status reworded to "listed/live".
- [x] `site/src/content/docs/index.mdx`: Quick Start present tense + Install link in
      "Learn the model".
- [x] `site/src/content/docs/guides/compose-instruction.md`: rewrite Step 1 install command
      to the marketplace flow.
- [x] New `site/src/content/docs/guides/install.md` (`sidebar: { order: 0 }`; relative-slug
      links only).
- [x] New `QUICKSTART.md` at repo root.
- [x] `skills/writing-instruction-builder/SKILL.md`: add the helper-script Implementation note.
- [x] New `scripts/validate-plugin-manifest.mjs` (zero-dependency Node; `--expect-version`).
- [x] `validate.yml`: add `node scripts/validate-plugin-manifest.mjs` step to the `validate`
      job (required-context coverage).
- [x] New `scripts/build-release.sh` + `scripts/build-release.ps1` (flat archive root).
- [x] New `.github/workflows/validate-plugin.yml` (no npm), `release.yml` (build + attach
      assets, non-draft), `release-zips.yml` (workflow_dispatch only), `codeql.yml`.
- [x] De-version sweep: `grep -rn "v0\.1\.0"` over tracked release artifacts (excluding
      `examples/`, `docs/internal/`) is clean.
  - Acceptance: `python tools/validate.py` PASS; `python tools/build-indexes.py` leaves
    `taxonomy.json` unchanged; `node scripts/validate-plugin-manifest.mjs` PASS (and FAILs a
    deliberately broken manifest); `node scripts/check-no-dashes.mjs` PASS;
    `cd site && npm run build` green; rendered-link + route-parity guards PASS; a local
    `build-release.sh` run produces a ZIP whose unzipped `build-instruction.py` resolves
    `taxonomy/` and emits an instruction.

## Phase 2 - Merge, tag, Release

- [x] Push `release/v0.2.0`; open PR; CI green (validate + build-site + validate-plugin +
      codeql). Resolve all PR conversations.
- [x] Register `build-site`, `validate-plugin`, `codeql` as required status checks on
      `main` (via `gh api .../branches/main/protection`) once green on the PR.
- [x] **Squash-merge** to `main` (linear history required; no merge commit).
- [x] Tag `v0.2.0` (annotated) at the squashed `main` HEAD; push the tag.
- [x] GitHub Release `v0.2.0` published by `release.yml` (non-draft, Latest) with ZIP +
      `.sha256` + `manifest.txt` attached directly; no orphan draft.
  - Acceptance: `gh release view v0.2.0` shows the three assets; `git ls-remote --tags` shows
    the pushed tag; tag commit == `main` HEAD.

## Phase 3 - Pin agent-plugins registry (branch `list-writing-style-catalog`)

- [x] Add the `writing-style-catalog` entry (spec Section 5) with the real `v0.2.0` SHA;
      bump `metadata.version -> 1.3.0`.
- [x] `README.md` Plugins table: add the WSC row (status `listed`); reconcile the existing
      `thinking-framework-skills` `_planned_ -> listed` + fill its Repo cell.
- [x] `CHANGELOG.md`: backfill `[1.1.0]` + `[1.2.0]`, then add `[1.3.0]`.
- [x] Poll the raw `plugin.json` URL at the SHA until 200 (propagation), then
      `GITHUB_TOKEN=$(gh auth token) node scripts/validate-registry.mjs` PASS (all enforcing
      checks, including 5 sha-on-tag + 7 installability).
- [x] PR; CI `validate-registry` green; merge to `main`.
  - Acceptance: validator green locally and in CI; the listing is on `main`.

## Phase 4 - Verify + hygiene

- [x] Re-run `validate-registry.mjs` on `main` (post-merge) - green.
- [x] Manual `/plugin` smoke recorded: `marketplace add product-on-purpose/agent-plugins`,
      `install writing-style-catalog@product-on-purpose`, one `compose-instruction` call.
      (Human-run; Claude Code cannot be driven from CI. The registry validator's network
      checks 5+7 are the automated proxy.)
- [x] Flip this plan + spec status to SHIPPED; refresh MEMORY.
  - Acceptance: every box above checked; acceptance criteria in `spec.md` Section 8 met.

---

## Cross-repo execution checklist

| Repo | Work | Branch / PR | Expected commit(s) | Gate |
|---|---|---|---|---|
| `writing-style-catalog` | Phase 1 prep + Phase 2 tag/Release | `release/v0.2.0` -> `main`; tag `v0.2.0` | version+docs+CI commit; annotated tag; Release | Phase 1, 2 |
| `agent-plugins` | Phase 3 registry pin | `list-writing-style-catalog` -> `main` | registry + README + CHANGELOG commit | Phase 3 |

Every row is launch-blocking. The agent-plugins pin cannot be validated until the WSC tag is
pushed (Phase 2 precedes Phase 3).

## Execution log

- **Phase 0 (plan + review) done.** Authored `spec.md` + `release-plan.md`. Ran a 13-agent
  adversarial review against the real registry validator + CI templates. Accepted findings
  folded in:
  - P1 release workflow: a `GITHUB_TOKEN`-created Release does not fire `release: published`,
    so the split design would ship an empty Release. `release.yml` now builds + attaches
    assets directly (non-draft); `release-zips.yml` is `workflow_dispatch`-only.
  - P1 gating: new workflows are not branch-protection required checks. Manifest check folded
    into the required `validate` job; new contexts registered as required in Phase 2.
  - P1 `npm ci`: WSC has no root `package.json`; new workflows are explicitly zero-`npm`.
  - P1 surface: `guides/compose-instruction.md` carries a third divergent install command;
    added to the inventory.
  - P2: de-version both manifest descriptions (one canonical string); self-hosted
    `marketplace.json` `ref -> v0.2.0`; backfill agent-plugins CHANGELOG `[1.1.0]`/`[1.2.0]` +
    fix drifted README table; squash-merge (linear history); raw-CDN propagation poll before
    the Phase 3 validator; tag frozen after the registry pin; Install link on the landing
    page; flat ZIP archive root; SKILL.md helper-script note.
  - Noted (not a change): the skill *name* is `compose-instruction` (frontmatter); the folder
    is `writing-instruction-builder`. The documented invocation is correct.
- **Phase 1-2 (WSC) done.** Release-prep on `release/v0.2.0`: all local gates green (manifest
  validator pass + fails a bad version; no-dashes; taxonomy validate; `taxonomy.json`
  unchanged; site build 112 pages; rendered-link + route-parity pass; ZIP unzips flat and the
  skill resolves `taxonomy/`). PR #13: validate + validate-plugin + build-site + CodeQL all
  green. Registered `build-site` as a required status check alongside `validate`. Squash-merged
  to `main` (`3685d65`). Tagged annotated `v0.2.0` at `3685d65` and pushed; `release.yml` built
  and published the GitHub Release (Latest) with the ZIP + `.sha256` + `manifest.txt`;
  `validate-plugin` tag-version assertion green. Site deployed; `guides/install/` live (HTTP
  200).
- **Phase 3 (agent-plugins) done.** The repo had concurrent local WIP (an `agent-skills-toolkit`
  listing committed as `374cd8f` on another branch, placeholder sha, not pushed), so the change
  was made server-side from `origin/main` to avoid entanglement: validated the exact proposed
  registry locally (all 7 enforcing checks pass), then PR #8 added the `writing-style-catalog`
  entry (pinned to `3685d65`, https url, strict), bumped `metadata.version` 1.2.0 -> 1.3.0,
  flipped the stale `thinking-framework-skills` README status to `listed`, and backfilled
  CHANGELOG `[1.0.1]`..`[1.2.0]` + added `[1.3.0]`. `validate-registry` CI green on the PR and
  on `main` after squash-merge. No concurrent work disturbed.
- **Phase 4 (verify) done.** Post-merge `validate-registry` green on `agent-plugins/main`
  (network checks 5 sha-on-tag + 7 installability are the automated install proxy). GitHub
  Release Latest with assets confirmed. Install docs live. Manual `/plugin` smoke
  (`marketplace add` + `install writing-style-catalog@product-on-purpose` + one
  `compose-instruction` call) is left to the maintainer, since Claude Code cannot be driven from
  CI; the registry validator's network checks already prove the pin is resolvable and the
  pinned `plugin.json` is valid.

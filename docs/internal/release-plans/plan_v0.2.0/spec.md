# v0.2.0 Marketplace Launch - Specification

> The contract for v0.2.0. The companion [`release-plan.md`](release-plan.md) is the
> ordered, checkbox-owned execution; this file is the "what" and "why" it answers to.
> Reference precedent: pm-skills v2.21.0 (`pm-skills/docs/internal/release-plans/v2.21.0/`),
> the marketplace launch this mirrors.

**Status:** SHIPPED 2026-06-02. `writing-style-catalog@product-on-purpose` is installable.
**Type:** MINOR (0.1.0 -> 0.2.0).
**Theme:** Make `writing-style-catalog` genuinely installable through the `product-on-purpose`
marketplace, make every install/getting-started surface tell the truth, and add the
standardized plugin CI (validation, release, release ZIPs, CodeQL) the listing depends on.

---

## 1. Problem statement

The repository already *documents* a marketplace install that does not work yet:

- `README.md` (Quick Start) and `site/src/content/docs/index.mdx` instruct users to run
  `/plugin marketplace add product-on-purpose/agent-plugins` then
  `/plugin install writing-style-catalog@product-on-purpose`.
- The `product-on-purpose/agent-plugins` registry (`.claude-plugin/marketplace.json`)
  lists only `pm-skills` and `thinking-framework-skills`. **`writing-style-catalog` is
  absent**, so the install command resolves to nothing.
- The only existing tag, `v0.1.0`, predates the ADR-0014 rename. At that commit the plugin
  `name` is `writing-style-library` and the self-hosted marketplace identity is
  `writing-style-library-marketplace`. The registry CI requires the pinned `sha` to be the
  target of a release tag whose `plugin.json` carries the correct `name` (checks 5 + 7), so
  `v0.1.0` cannot serve as the pin.

The gap is therefore not "write new install docs" but "make the existing docs true": list the
plugin in the registry, pinned to a fresh tag that reflects the renamed, Astro-migrated
`main`.

A secondary gap: WSC ships only `validate.yml` (taxonomy) and `build-site.yml` (Pages deploy).
It has no plugin-manifest validation, no release automation, and no security scan. The
registry's integrity model assumes a plugin repo that tags releases and keeps `plugin.json`
valid; WSC needs the CI to hold up its end of that contract.

## 2. Version decision (why v0.2.0, why MINOR)

- **Fresh tag is mandatory.** A published tag is immutable in practice; `v0.1.0` already
  points at the pre-rename commit and is the wrong plugin identity. The next tag is the only
  viable pin.
- **0.2.0, not 0.1.1.** Everything merged since `v0.1.0` is substantial: the repository
  rename (ADR 0014), the full docs-site migration from MkDocs to Astro Starlight (Pattern S),
  and the 14.11 build-aware link/route guards. v0.2.0 formally releases that accumulated work
  *and* adds the marketplace listing. A patch would understate it.
- **MINOR, not MAJOR.** The project is pre-1.0 and explicitly experimental; the catalog is
  unchanged (60 entries, same `compose-instruction` interface). The rename does change the
  install identity, but `v0.1.0` was never actually distributed through the registry (the
  registry never listed it), so there is no existing marketplace install to break. Under
  pre-1.0 SemVer, the minor is the unit of change. v0.2.0 is correct and conventional.

## 3. Goals

1. `writing-style-catalog` is listed in the `product-on-purpose/agent-plugins` registry,
   pinned to the `v0.2.0` tag commit, `strict: true`, via an https `url` source.
2. The two install commands documented in the README and the site work end to end against a
   public Claude Code client.
3. Every install / getting-started surface (repo `README.md`, repo `QUICKSTART.md`, site
   landing page, a new site install guide) states the live, accurate install path in
   present tense, with the `/plugin update` path noted.
4. WSC carries standardized plugin CI: manifest validation, a tag-driven GitHub Release, a
   release-ZIP attach step, and CodeQL.
5. A reproducible release artifact (`scripts/build-release.{sh,ps1}`) that bundles the
   installable plugin (the `.claude-plugin/` manifest, `skills/`, and the `taxonomy/` data
   the skill reads at runtime) for the Claude.ai / Claude Desktop upload path.

## 4. Non-goals

- No catalog content changes (no new entries, examples, diff-pairs, or recipes).
- No schema change (so no ADR or schema version bump is triggered by this release).
- No retirement of the self-hosted single-plugin `marketplace.json`; it stays as the direct
  fallback, version-bumped (mirrors the pm-skills additive dual-home decision D-V3-1).
- No change to the Astro site generation pipeline or the existing taxonomy validators.
- No second-language packaging (Codex `.codex-plugin`); WSC ships a single Claude plugin.

## 5. The registry entry (executable target)

Added to `product-on-purpose/agent-plugins/.claude-plugin/marketplace.json` in the `plugins`
array. The `sha` is filled at execution after the `v0.2.0` tag is pushed (Section 9 ordering).

```jsonc
{
  "name": "writing-style-catalog",
  "source": {
    "source": "url",
    "url": "https://github.com/product-on-purpose/writing-style-catalog.git",
    "sha": "<v0.2.0 tag commit SHA>"
  },
  "description": "<the canonical de-versioned description - identical to plugin.json, Section 6.1>",
  "version": "0.2.0",
  "strict": true
}
```

The `description` is the single canonical, de-versioned string defined in Section 6.1 and
reused verbatim in `plugin.json`, the self-hosted `marketplace.json`, and here, so the three
never drift and no per-release description edit is needed.

- **`source: url` (https), not `github` shorthand.** The registry's own
  `registry-maintenance.md` documents that a `github` shorthand source clones over SSH and
  breaks HTTPS-only users; https `url` is the launch standard. This was a real pm-skills
  v2.21.0 smoke finding.
- **`strict: true`.** The plugin passes strict validation; this exercises the real launch
  configuration through the registry CI.
- The registry's own version line bumps: `metadata.version` `1.2.0 -> 1.3.0`. The validator
  does **not** check monotonicity (it only type-checks `metadata.version` as a string); the
  bump is a maintenance convention, not a validator requirement.

The entry must satisfy all seven enforcing checks in
`agent-plugins/scripts/validate-registry.mjs`:

| # | Check | How v0.2.0 satisfies it |
|---|---|---|
| 1 | JSON parses | hand-validated + `node scripts/validate-registry.mjs` |
| 2 | Top-level schema | unchanged registry header |
| 3 | Per-entry required fields | `name`, `source`, `version`, `description` all present |
| 4 | `source` shape + 40-char `sha` | https `url` + the pushed tag commit hash |
| 5 | `sha` is a release-tag target | the `v0.2.0` annotated tag is pushed before validation |
| 6 | No placeholder; strict needs a real pin | real description + valid pinned sha |
| 7 | Installability (pinned `plugin.json` has name/version/description/license) | WSC `plugin.json` carries all four |

## 6. WSC repository deliverables

### 6.1 Version + manifest surfaces
- **Canonical description (de-versioned).** Both `plugin.json` and the self-hosted
  `marketplace.json` currently embed a `v0.1.0 ships 60 curated entries...` clause in their
  `description`. Bumping only the numeric `version` field leaves that stale token behind. Fix
  the whole class once: replace the embedded `v0.1.0 ships...` with a version-free `Ships 60
  curated entries...`, and use the *same* string in `plugin.json`, the self-hosted
  `marketplace.json`, and the registry entry (Section 5). Canonical string:
  > Composable writing instructions on four orthogonal axes (Voice, Tone, Style, Format).
  > Select one entry per axis and the compose-instruction skill assembles a ready-to-paste
  > prompt prefix that steers any LLM toward a precise register, reasoning pattern, and
  > layout. Ships 60 curated entries (15 per axis), 195 worked examples across three anchor
  > topics, 12 diff-pairs, and 5 horizontal-slice recipes. Follows the agentskills.io
  > specification.
- `.claude-plugin/plugin.json`: `version` `0.1.0 -> 0.2.0`; `description` -> canonical.
- `.claude-plugin/marketplace.json` (self-hosted): plugin entry `version` `0.1.0 -> 0.2.0`;
  `description` -> canonical; **`source.ref` `main -> v0.2.0`** so the direct fallback is
  pinned to the released tag rather than tracking a moving `main` (it then matches its own
  declared version; re-pin one line per release). The `v0.2.0` ref is self-consistent inside
  the commit that gets tagged `v0.2.0`.
- `README.md` version badge `0.1.0 -> 0.2.0`; the experimental-warning `(v0.1.0)` token;
  the Project Status heading.
- `CHANGELOG.md`: convert `[Unreleased]` to `[0.2.0] - <date>`; add the marketplace-listing
  and CI items under Added; keep the existing astro/rename entries.
- After all edits, `grep -rn "v0\.1\.0" --include` over tracked release artifacts (excluding
  `examples/` worked-example content and `docs/internal/`) returns no stale token.

### 6.2 Install / getting-started surfaces
- `README.md` Quick Start: keep the (now-correct) two commands; add the `/plugin update
  writing-style-catalog` line; drop any wording that implies the listing is hypothetical;
  ensure the "Distributed through..." status line is accurate.
- `site/src/content/docs/index.mdx`: rewrite the "Once it is published..." Quick Start to
  present tense; add an **Install** link to the "Learn the model" list so the new guide is
  reachable from the landing page.
- `site/src/content/docs/guides/compose-instruction.md`: **Step 1 currently shows a third,
  divergent install command** (`claude plugin install product-on-purpose/writing-style-catalog`).
  Rewrite it to the canonical two-line marketplace flow (or link `install.md`) so no
  site-linked page contradicts the standard.
- `site/src/content/docs/guides/install.md`: new authored guide - prerequisites, add +
  install + update, the direct-from-repo fallback, and the Claude.ai/Desktop ZIP path. The
  Guides sidebar group is `autogenerate` (`site/astro.config.mjs:63`), so the page appears
  automatically; set `sidebar: { order: 0 }` in its frontmatter to sort it first. No
  `astro.config.mjs` edit is needed. Author all internal links as relative-slug URLs
  (`../../guides/...`), never `.md` paths, so `check-rendered-links.mjs` (STRICT_ANCHORS)
  stays green.
- `QUICKSTART.md` (new, repo root): concise install + first-compose, mirroring the
  pm-skills QUICKSTART shape.
- `skills/writing-instruction-builder/SKILL.md`: add a one-line Implementation note pointing
  at the `scripts/build-instruction.py` helper, so the runtime `taxonomy/` read is real and
  the ZIP's `taxonomy/` inclusion is load-bearing (not merely defensive).

### 6.3 Standardized CI (modeled on pm-skills, adapted)
All workflow files are dash-free (the `check-no-dashes.mjs` gate covers `.yml`). Two
adaptations are load-bearing and diverge from the pm-skills donor on purpose:

- **No `npm ci` anywhere in the new workflows.** WSC has no root `package.json`/lockfile
  (only `site/` has Node deps), so the donor's unconditional `npm ci` would hard-fail. The
  manifest validator imports only `node:` built-ins (matching `scripts/check-no-dashes.mjs`).
- **Gating coverage.** Branch protection on `main` requires only the `validate` context, so a
  standalone `validate-plugin` job would be advisory at merge. Therefore the manifest check is
  **also added as a step inside the existing `validate` job** (`validate.yml`), so the
  required context actually covers it; and Phase 2 registers `build-site`, `validate-plugin`,
  and `codeql` as required contexts via `gh api .../branches/main/protection` once they have
  run green on the PR.

1. **`scripts/validate-plugin-manifest.mjs`** (new, zero-dependency Node): asserts
   `plugin.json` required string fields (`name`, `version`, `description`, `homepage`,
   `repository`, `license`), `name === "writing-style-catalog"`, SemVer `version`, non-empty
   `keywords`, `author.name`; asserts the self-hosted `marketplace.json` plugin entry `name` +
   `version` agree with `plugin.json`; asserts each `skills/*/SKILL.md` has `name` +
   `description` frontmatter. Accepts an optional `--expect-version X.Y.Z` for the tag check.
2. **Existing `validate.yml`**: add one step to the `validate` job ->
   `node scripts/validate-plugin-manifest.mjs` (so the required context covers manifests).
3. **`.github/workflows/validate-plugin.yml`** (new) - on PR/push touching `scripts/**`,
   `.claude-plugin/**`, `skills/**`, or the workflow file: checkout -> `setup-node`
   (`node-version-file: .nvmrc`) -> `node scripts/validate-plugin-manifest.mjs`. On a `v*`
   tag push, also run it with `--expect-version "${tag#v}"` (tag-equals-manifest). The path
   filter uses `scripts/**` so an edit to the validator triggers its own gate. **No `npm`.**
4. **`.github/workflows/release.yml`** (new) - on `v*` tag push: derive the version, build the
   artifact (`scripts/build-release.sh`), generate notes, and create the GitHub Release as a
   **non-draft** with the ZIP + `.sha256` + `manifest.txt` attached directly (this is the sole
   asset path; relying on a `release: published` handoff would not fire, because a Release
   created with the default `GITHUB_TOKEN` does not trigger further workflow runs). Re-uploads
   are idempotent (`softprops/action-gh-release` overwrites same-named assets), so there is no
   "race".
5. **`.github/workflows/release-zips.yml`** (new) - `workflow_dispatch` only (a tag input):
   rebuild and upload the ZIPs for an existing Release. This is the manual re-pack helper;
   it does **not** depend on the suppressed `release: published` event.
6. **`.github/workflows/codeql.yml`** (new) - CodeQL for `javascript-typescript` and `python`
   (the `.mjs` site/tooling scripts and the Python tools/skill), on push/PR to `main` +
   weekly schedule.

### 6.4 Release packaging
- `scripts/build-release.sh` + `scripts/build-release.ps1`: produce
  `dist/writing-style-catalog-v<version>.zip` staging `.claude-plugin/`, `skills/`,
  `taxonomy/`, `README.md`, `LICENSE`, `NOTICE`, `CHANGELOG.md` **at the archive root (no
  wrapper directory)**; plus a `.sha256` and a `manifest.txt` file listing. The flat root is
  required so that, after unzip, `build-instruction.py`'s `REPO_ROOT =
  Path(__file__).resolve().parents[3]` lands on the unzip directory where `taxonomy/` sits.
  `taxonomy/` is included because the skill reads `REPO_ROOT/taxonomy` at runtime; a ZIP
  without it (or with an extra wrapper dir) produces a broken skill on the upload path.
- Pre-release verification (hard gate): unzip the artifact and run
  `python skills/writing-instruction-builder/scripts/build-instruction.py voice=pragmatic-architect`
  from the unzip root; it must resolve `taxonomy/` and emit an instruction.

## 7. agent-plugins repository deliverables
- `.claude-plugin/marketplace.json`: add the Section 5 entry; bump `metadata.version` to
  `1.3.0`.
- `README.md`: add a `writing-style-catalog` row to the Plugins table, status `listed`.
  **Also reconcile the existing drift:** the `thinking-framework-skills` row reads `_planned_`
  but it is a live `strict: true` pinned entry in the registry; flip it to `listed` and fill
  its Repo cell, so the table matches the registry.
- `CHANGELOG.md`: the file's last released heading is `[1.0.0]` while `metadata.version` is
  already `1.2.0` (two bumps went unrecorded). **Backfill** brief `[1.1.0]` (add
  thinking-framework-skills; re-pin pm-skills to 2.24.0) and `[1.2.0]` (re-pin
  thinking-framework-skills to 0.2.0) from the git log, then add `[1.3.0]` (add
  writing-style-catalog) so the line is honest.
- Validation: `node scripts/validate-registry.mjs` passes with `GITHUB_TOKEN` set
  (`gh auth token`), after the WSC `v0.2.0` tag is pushed.

## 8. Acceptance criteria (release-level)

- [ ] WSC `plugin.json`, self-hosted `marketplace.json`, README badge, and CHANGELOG all read
      `0.2.0`; `python tools/validate.py` and `python tools/build-indexes.py` leave
      `taxonomy.json` unchanged; `cd site && npm run build` is green; the dash, rendered-link,
      and route-parity guards pass.
- [ ] `validate-plugin.yml` passes on the PR and on the tag; the manifest validator fails a
      deliberately broken manifest (smoke-tested locally).
- [ ] `v0.2.0` is tagged at the CI-green commit and pushed; a GitHub Release `v0.2.0` exists
      with the ZIP, `.sha256`, and `manifest.txt` attached and is marked Latest.
- [ ] The agent-plugins registry lists `writing-style-catalog` pinned to the `v0.2.0` SHA at
      `version 0.2.0`, `strict: true`, https `url`; `metadata.version` is `1.3.0`;
      `validate-registry.mjs` passes all enforcing checks on `main`.
- [ ] The README, QUICKSTART, site landing page, and the new install guide state the live
      install path in present tense; no "once published" or hypothetical wording remains.
- [ ] The self-hosted single-plugin marketplace still resolves as the direct fallback at
      `0.2.0`.
- [ ] A documented manual `/plugin` smoke (add + install + compose) is recorded as the
      human-run verification, since Claude Code cannot be driven from CI.

## 9. Cross-repo sequencing (hard constraints)

The registry pin cannot be validated until the tag it points at exists on GitHub. Therefore:

1. WSC release-prep branch green (all validators + site build) -> open PR -> **squash-merge**
   to `main` (`main` requires linear history + conversation resolution, so a merge commit is
   rejected; resolve all PR conversations first; under `strict` status checks the branch may
   need an update + `validate` re-run before merge).
2. Tag `v0.2.0` (annotated) at the squashed `main` HEAD; **push the tag** (check 5 now
   resolves). The release workflow fires on the tag and builds + publishes the Release with
   assets.
3. Confirm the Release: `gh release view v0.2.0` shows the ZIP + `.sha256` + `manifest.txt`
   and Latest; no orphan draft.
4. agent-plugins branch: fill the `sha`. Before running the validator, **wait for raw-CDN
   propagation**: poll `https://raw.githubusercontent.com/product-on-purpose/writing-style-catalog/<sha>/.claude-plugin/plugin.json`
   until it returns 200 (check 7 fetches this raw URL and treats a 404 as a non-retryable hard
   failure; immediately after tagging this can 404 from propagation lag, not a defect; the
   `REGISTRY_CHECK7=advisory` env var is the documented escape hatch if lag persists). Then
   `node scripts/validate-registry.mjs` green -> PR -> merge to `main`. The listing is live.
5. Verify: re-run the registry validator on `main`; run the manual `/plugin` smoke.

A failed validator at any gate halts the chain at that gate; nothing downstream proceeds.

**Tag immutability.** Once Phase 3 merges the registry pin, the `v0.2.0` tag is frozen:
deleting or moving it makes the registry's check 5 fail on the next push or the weekly cron,
turning the public registry CI red. Any later retag must update the registry `sha` in the same
change. The "safe to delete + re-push the tag" rollback note applies **only before** the
registry pin is merged.

## 10. Risks + rollback

| Risk | Mitigation / rollback |
|---|---|
| Registry validator red after merge (sha/tag/installability) | Caught pre-merge by running `validate-registry.mjs` locally against the pushed tag; never merge the registry entry red. |
| Tag pushed at a non-green commit | Tag only the commit whose full CI is green; if wrong, the tag is safe to delete + re-push while the registry entry is not yet merged. |
| Release ZIP missing `taxonomy/` -> broken upload-path skill | Build script explicitly includes `taxonomy/`; a local unzip + run of `build-instruction.py` confirms before release. |
| New route (install guide) trips route-parity | Adding a route does not fail parity (only removals do); regenerate `route-manifest.txt` baseline to keep it current. |
| Self-hosted marketplace identity rename strands a v0.1.0 self-hosted install | None known to exist (experimental, pre-distribution); documented in CHANGELOG. The direct repo path keeps working. |
| em/en-dash slips into a tracked file | Global PreToolUse hook + `check-no-dashes.mjs` CI gate both block it. |

## 11. Reference precedent

This launch is a single-plugin instance of pm-skills v2.21.0. Differences: WSC's registry is
already public (the go-public flip happened at the pm-skills launch), so there is no
visibility flip; and WSC adds a fuller CI suite (the pm-skills launch added only the
registry-side CI, the plugin-side CI already existed there).

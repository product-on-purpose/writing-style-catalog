---
title: Promotion and Release Runbook
status: in use (validated by the Wave-1 promotion and the v0.4.0 release)
audience: maintainer + operating agent
related:
  - tools/agentic/README.md (the harnesses)
  - tools/promote.py (the guarded flip)
  - docs/internal/agentic-generation-spec.md (the design + contracts)
  - docs/internal/release-plans/stream-b-promotion-proposal.md (which drafts, in which wave)
---

# Promotion and Release Runbook

The repeatable steps to promote a wave of draft format entries to stable and to cut
a release. This is the operational checklist; the design is in the spec. It was
walked end to end for Wave 1 / v0.4.0 and is the template for Wave 2 / v0.5.0.

Everything here runs on free in-session subagents plus deterministic tooling. The
only outward-facing, maintainer-reserved step is cutting the release tag (step 13).

## Preconditions

- The drafts to promote already passed the per-entry distinguishability gate (at
  generation) and the whole-corpus de-dup audit. If not, run those first
  (`tools/agentic/README.md`, loops A and B).
- A wave is chosen (see the promotion proposal). Each promoted format costs 12
  anchor-topic renders, so a wave is a deliberate, sized batch.

## Promote a wave

1. **Branch.** `git checkout -b feat/promote-<wave>`.

2. **Render.** Edit `tools/agentic/promote.js` `FORMATS` to the wave's draft ids.
   Invoke it with the Workflow tool. It writes
   `examples/vertical-slices/<topic>/format-<id>.md` for all 12 topics per format.
   (The entries are still `draft`, so they are Gate-2-exempt and validate stays green.)

3. **Validate the render.** `python tools/validate.py` - expect green (the new sample
   files are well-formed; no dashes; example count rises by 12 x wave-size).

4. **Date gate.** For every dated format in the wave (incident-report, release-notes,
   postmortem, retrospective, and any with timelines), dispatch one date-checker agent
   per format (prompt in the spec, section 4b). Collect the flagged files + corrections.

5. **Apply date fixes.** Put the corrections into `tools/agentic/remediate.js` `FIXES`
   (one entry per file, quoting the exact change), invoke it, then `python
   tools/validate.py` again. Expect roughly a third of dated samples to need a fix.

6. **Flip - guarded.** `python tools/promote.py <id> <id> ...` (or `--all-ready`). It
   promotes only if every named entry renders on all 12 topics; otherwise it changes
   nothing and tells you what is missing. `--check` first if you want a dry run.

7. **Rebuild the index.** `python tools/build-indexes.py`.

8. **Update counters.** In the same PR:
   - `README.md` (four lines): bump the stable-entry count and the worked-example
     count ("every one of the N stable entries ... = N x 12"), the "M format
     templates (plus K draft ...)" line, the "N stable taxonomy entries (15 Voice, 15
     Tone, 15 Style, X Format)" line, and the "Y worked examples ... 130 diff-pairs and
     14 recipes" line. README worked-examples = vertical-slice samples only.
   - `library.json` and `.claude-plugin/plugin.json`: "Ships N curated entries, T
     worked examples ...". T = vertical + horizontal (currently vertical + 29). Update
     BOTH identically.

9. **Validate with Gate 2 active.** `python tools/validate.py` - now the promoted
   entries are stable, so Gate 2 sample-count applies to them; it must pass.
   `node scripts/validate-plugin-manifest.mjs` - confirms `plugin.json` == `library.json`.

10. **Build the site.** `node scripts/gen-site.mjs && (cd site && npm run build)`. The
    promoted entries lose the "Draft - under review" badge automatically.

11. **PR -> green -> squash-merge.** Conventional commit; no dashes.

## Cut the release

12. **Release-prep PR.** Branch `release/vX.Y.0`. Bump `"version"` in `library.json`
    and `.claude-plugin/plugin.json` (line 3) to the new version. Roll the CHANGELOG
    `[Unreleased]` block into a `## [X.Y.0] - <date>` section with a summary line and
    Added / Changed / Fixed entries describing the wave. Leave a fresh empty
    `[Unreleased]`. Validate (`validate.py` + the manifest validator), PR, green, merge.

13. **Tag (maintainer-reserved, outward-facing).** On `main` at the release commit:
    ```
    git tag -a vX.Y.0 -m "vX.Y.0 - <summary>"
    git push origin vX.Y.0
    ```
    `.github/workflows/release.yml` triggers on the `v*` tag push, builds the plugin
    ZIP, and publishes the GitHub Release with the ZIP + sha256 + manifest. Confirm
    with `gh release view vX.Y.0`.

14. **Marketplace registry re-pin (separate repo, manual).** The listing in
    `product-on-purpose/agent-plugins` tracks the released tag, not `main`, so the
    install surface updates only when that registry re-pins to the new tag. Bump the
    registry `metadata.version` on a new listing. This is NOT done by the release here.

## Notes

- The whole sequence kept the catalog schema-valid at every step in the Wave-1 run.
  If `validate.py` ever reds mid-flip, it is the Gate 2 sample-count: an entry was
  flipped before all 12 samples existed. Render the missing ones and re-run.
- Wave sizing: Wave 1 was 14 formats = 168 renders, run as a 2-format pilot (to prove
  the pipeline) then the remaining 12. Wave 2 is ~23 formats = ~276 renders; consider
  splitting if a single render run is too large to review in one pass.

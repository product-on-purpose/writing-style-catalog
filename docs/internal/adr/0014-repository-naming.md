---
adr_id: "0014"
title: Repository name vs the family grade-word "library"
date: 2026-06-01
status: Proposed
---

# 0014 - Repository name vs the family grade-word "library"

## Status

Proposed (awaiting maintainer decision)

## Context

The repository is named `writing-style-library`. The product-on-purpose family standard (`agent-skills-toolkit/STANDARD.md`, Section 0) reserves "library" as a quality grade, not an artifact type: "'Library' is a grade, not a thing", the designation for a plugin that conforms to the Standard and is graded Bronze, Silver, or Gold. By that vocabulary, naming a repository `...-library` claims a grade rather than describing what the repository is.

The family's repository names are not currently consistent. There are tooling and standards repos named `...-toolkit` (`agent-skills-toolkit`, `agent-config-toolkit`), catalog repos named `...-skills` (`pm-skills`, `thinking-framework-skills`, `utility-skills`), and this one named `...-library`. The maintainer raised `writing-styles-toolkit` as a candidate.

Two separate naming questions are in play: the suffix (`library` vs `toolkit` vs `skills` vs none), and singular vs plural (`style` vs `styles`).

This is an outward-facing decision. The name appears in:

- the GitHub repository URL (`product-on-purpose/writing-style-library`),
- the live documentation site URL (`product-on-purpose.github.io/writing-style-library/`) and the Astro `base` path,
- the package name (`@product-on-purpose/writing-style-library`) and the plugin and marketplace identifiers,
- internal cross-references across `README.md`, `AGENTS.md`, `CLAUDE.md`, and the docs.

Renaming is therefore not a local edit; it is a migration with redirect and link-rot considerations.

## Decision

Proposed, pending maintainer choice.

The `-skills` suffix is rejected on inspection. The repository currently contains exactly one skill (`compose-instruction`); its product is the catalog of writing instructions, examples, diff-pairs, recipes, and templates. Naming it `...-skills`, a suffix the family uses for multi-skill collections like `pm-skills`, misrepresents it.

The options:

- **Option A - keep `writing-style-library`.** Zero migration cost. "Library" in its ordinary sense, a curated and growing collection, describes the repository accurately and is the maintainer's preferred connotation. The only cost is a soft collision with the standard's grade-word "library", which is a vocabulary-precision issue internal to the standard and can be resolved with a clarifying sentence there rather than a repository rename.
- **Option B - rename to `writing-style-catalog`.** "Catalog" is the word the repository already uses to describe itself (`package.json`: "A composable catalog of writing instructions"). It avoids the grade-word collision and keeps the collection connotation. This is the only rename strictly more accurate than the current name.
- **Option C - rename to `writing-styles-toolkit`.** The maintainer's earlier candidate. Rejected: this repository is content, not tooling.

Timing: the repository was just made public, the marketplace listing is deferred, and the install path is still aspirational, so a rename is at its cheapest right now. GitHub auto-redirects the old URL; only the Astro `base` path, the package and plugin identifiers, and internal references change. The cost rises once the listing is broadcast and external users install.

Recommendation: keep `writing-style-library` (Option A) and clarify the grade-word in the standard, unless eliminating the collision outright is preferred, in which case `writing-style-catalog` (Option B) is the one rename worth making while it is cheap. Do not adopt `-skills` or `-toolkit`.

A rename, if accepted, MUST be executed as a sequenced migration, not a side effect. At minimum: rename the GitHub repo (GitHub auto-redirects the old URL), update the Astro site `base` and redeploy, update the package, plugin, and marketplace identifiers, sweep internal references, and note the change in `CHANGELOG.md` and the release notes.

## Consequences

### Positive

- Resolving the name removes a contradiction with the family's own controlled vocabulary and improves cross-repo consistency.

### Negative

- Any rename breaks existing URLs and the published plugin identifier. GitHub redirects soften repository-URL breakage but not the package or marketplace identifier.

### Neutral

- This ADR records the decision space; it does not itself rename anything. No action is taken until the maintainer accepts an option.

---
adr_id: "0020"
title: "Serve schemas at a contract-versioned URL so the freeze is externally real"
date: 2026-07-30
status: Accepted
supersedes_context: >
  Resolves the known gap recorded in ADR 0019 decision 3, which froze the schemas but could
  not offer an external guarantee because every $id resolved to raw.githubusercontent on
  main. This is a class C change under ADR 0019's own policy.
related:
  - docs/internal/adr/0019-schema-freeze-and-change-policy.md
  - docs/internal/adr/0011-site-generation-architecture.md
  - docs/internal/backlog.md
---

# 0020 - Serve schemas at a contract-versioned URL so the freeze is externally real

## Status

Accepted (2026-07-30).

## Context

ADR 0019 froze the entry schema and then had to admit, in decision 3, that the freeze bought
nothing for anyone outside this repository:

> Every `$id` resolves to a raw GitHub URL on `main`, so the published schema tracks the tip
> of the branch. There is no `1.x`-identified artifact to pin.

Two concrete defects sat behind that.

**1. The published contract tracked a moving branch.** Every `$id` was
`https://raw.githubusercontent.com/.../main/schemas/<name>.schema.json`. Anyone resolving it
got whatever `main` said at that moment. "Frozen" and "resolves to a branch tip" cannot both
be true.

**2. Relative `$ref`s could silently mix versions.** The four per-axis schemas compose the
shared one with `{ "$ref": "entry.universal.schema.json" }`. A relative `$ref` resolves
against the *base URI of the document that contains it*, which is its `$id`. With every `$id`
on `main`, a consumer who fetched `voice.schema.json` from a git tag would still resolve
`entry.universal` from `main`. The axis schema would be pinned and its own parent would not.

There was also a third problem inside the repo, unmentioned by ADR 0019.
`tools/validate.py::_build_schema_registry` rebuilt each schema's URI from a **hardcoded base
string** rather than reading the file's `$id`:

```python
uri = f"https://raw.githubusercontent.com/.../main/schemas/{f.name}"
```

That is a second copy of the base URL, in a different file from the one that declares it. Any
move of the `$id` would leave the registry mapping documents under URIs that no longer matched
their declared identity, and `$ref` resolution would fail, or half-resolve, with nothing
pointing at the cause.

### Why now, specifically

Under ADR 0019 a change to `$id` is **class C**: ADR, version bump, migrate every affected
file. ADR 0019 originally said "major bump" without addressing what that means at `0.y.z`, so
it was amended (2026-07-30) to state that class C bumps the minor component pre-1.0 and the
major component from 1.0.0 onward. That amendment was made as its own decision rather than
asserted here, because reinterpreting a policy inside the first change it governs is how
policies quietly stop meaning anything.

The consequence is that this fix is **cheapest right now and permanently more expensive after
1.0.0**, and the v1.0 launch copy cannot honestly advertise a stable schema contract until it
lands. Both point the same way: pull it forward.

## Decision

**Schemas are served from a contract-versioned path on the documentation site:**

```
https://product-on-purpose.github.io/writing-style-catalog/schemas/v1/<name>.schema.json
```

1. **The contract version is `v1`, and it is not the plugin version.** The data contract
   changes far less often than the catalog does. Tying them would make every catalog release
   rewrite every `$id`, which is a class C change by ADR 0019, so routine releases would
   become breaking ones. `v1` bumps only when the contract itself breaks. This is the same
   shape JSON Schema itself uses for drafts.

   **Superseded versions keep being served, and that is enforced rather than promised.** The
   published tree is gitignored and regenerated on every build, so a version that is not
   emitted from a committed source disappears on the next deploy and every pinned consumer
   gets a 404. A promise alone would therefore have been false the first time it mattered.
   Instead: when the contract breaks, the outgoing version is snapshotted to
   `schemas/contracts/<version>/` **in the same PR** that bumps the constant, and the
   publisher emits every snapshot alongside the current contract.
   `test_contract_version_bump_requires_a_snapshot` fails the build if the constant moves
   without its snapshot, so the retention obligation cannot be forgotten at the one moment it
   becomes real.

2. **The unfrozen schema does not sit in the frozen namespace.** ADR 0019 permits a class C
   change to `diff-pair.schema.json` without a major bump. Publishing it at `/schemas/v1/`
   would mean the document behind a "pinned" URL could change under a consumer, with nothing
   in the URL distinguishing it from the frozen ones. It moves to
   `schemas/experimental/diff-pair.schema.json` and is served at `/schemas/experimental/`, so
   **the URL carries the guarantee level.**

3. **Publishing is generated, not duplicated.** `scripts/gen-site.mjs` copies the schema tree
   into `site/public/schemas/` on every build; the copies are gitignored. The single source of
   truth stays `schemas/` at the repo root. A committed second copy would drift.

4. **The generator verifies `$id` against the path it publishes to** and throws if they
   disagree, so a moved schema fails the build instead of silently serving a document whose
   declared identity contradicts its own URL.

5. **`_build_schema_registry` now reads each file's own `$id`** instead of rebuilding the URI
   from a constant, and raises if a schema has none. The base URL now exists in exactly one
   place per schema: the schema.

6. **Relative `$ref`s are kept as-is.** They are the mechanism that makes this work: once the
   base URI is version-scoped, `{ "$ref": "entry.universal.schema.json" }` resolves *within
   v1* automatically. Rewriting them to absolute URLs would reintroduce the duplication this
   ADR removes.

### Class C obligations, discharged

| Obligation (ADR 0019) | How it is met |
|---|---|
| ADR | This document |
| Version bump | v0.8.0 -> **v0.9.0**, the minor component, per the ADR 0019 amendment that defines the pre-1.0 class C increment. The amendment was made separately and first; this is not a reinterpretation made to fit. |
| Migrate every affected file | All 7 schemas (6 under `v1`, `diff-pair` under `experimental`), the registry builder and diff-pair path in `validate.py`, and the publisher. No `ENTRY.md` references a schema by URI, so no catalog entry needed migration; `validate.py` green confirms it. |
| `validate.py` green before merge | Yes, plus 117 entries and 1,207 examples still validating through the rewritten registry. |

## Consequences

### Positive

- The freeze becomes a real external guarantee. A consumer can pin the `v1` URL and know the
  shape will not change under them, which is what ADR 0019 wanted to promise and could not.
- The version-skew bug is fixed structurally rather than by convention: a version-scoped base
  URI makes it impossible for a per-axis schema to resolve its parent from a different version.
- The duplicated base URL is gone. The registry cannot disagree with the schemas, because it
  no longer holds an opinion about where they live.
- v1.0 launch copy can now honestly describe a stable, retrievable data contract.

### Negative

- **The canonical URI is not portable across a rename or transfer.** Schema identity is now
  tied to the `product-on-purpose` org and the `writing-style-catalog` Pages path. GitHub does
  not redirect a Pages site after a repository transfer, so a move would 404 every `$id` and
  every relative `$ref` under it. The honest fix is a project-controlled custom domain, which
  is an infrastructure decision with real cost and is not made here.

  Worth being precise about the delta: the previous `raw.githubusercontent.com/.../main/` URLs
  carried the **same** org and repo coupling *plus* branch mutability, so this is strictly
  better rather than a new exposure. But "strictly better" is not "durable", and a v1.0 launch
  claim of a permanent contract should wait for the domain. Logged in the backlog.
- The published contract now depends on the docs site being deployed. If Pages is down or the
  deploy fails, the `$id` URL does not resolve, whereas raw.githubusercontent tracked the repo
  directly. Mitigated by the URL being a stable identifier regardless: local validation never
  fetches it, and the repo remains the source of truth.
- Anyone who already resolved the old raw.githubusercontent URLs is broken by this. That is
  the definition of a class C change and the reason to do it before 1.0 rather than after. The
  old URLs were never advertised as stable, and ADR 0019 said in writing that they were not.
- Two version numbers now exist in the project (plugin version, schema contract version). That
  is the point, but it is a thing to explain, so `schemas/README.md` states it.

### Neutral

- `example.schema.json` and `diff-pair.schema.json` are published under `v1` alongside the
  frozen five. Publishing is not the same as freezing: `diff-pair` remains unfrozen per ADR
  0019 decision 1. Serving it at a stable URL costs nothing and keeps the tree uniform.
- The schemas are served as static JSON with no `Content-Type: application/schema+json`, since
  GitHub Pages serves `.json` as `application/json`. No consumer requires the former.

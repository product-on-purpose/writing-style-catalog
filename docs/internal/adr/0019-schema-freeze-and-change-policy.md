---
adr_id: "0019"
title: "Freeze the entry schema at v1.0 and define a change policy with explicit change classes"
date: 2026-07-29
status: Accepted
supersedes_context: >
  Replaces the single blanket rule in AGENTS.md "Schema Safety" and schemas/README.md, which
  requires a version bump, a new ADR, and updates to every referencing file for ANY change to
  schemas/. Closes GATE 2 (schema frozen) of the v1.0 readiness gates. Unblocks the schema
  annotation cleanup deferred by ADR 0018 decision 5.
related:
  - docs/internal/adr/0010-domain-and-family-organization.md
  - docs/internal/adr/0009-pedagogical-entry-bar.md
  - docs/internal/adr/0018-four-axis-framing.md
  - docs/internal/backlog.md
---

# 0019 - Freeze the entry schema at v1.0 and define a change policy with explicit change classes

## Status

**Accepted (2026-07-29).** Ratified by the maintainer. Declaring the data contract stable is
a decision with a long tail, so it was drafted as Proposed and accepted explicitly rather
than assumed. The freeze is in effect as of this ADR.

## Context

The catalog's data contract is seven JSON Schemas under `schemas/`. Consumers today are
in-repo (`tools/validate.py`, `scripts/gen-site.mjs`, three skills) but the contract is
published: `entry.universal.schema.json` carries a `$id` pointing at a raw GitHub URL on
`main`, which means anyone can and may already reference it.

**The v1.0 launch is gated on this.** The marketing plan holds the public launch until
`review_status` is honestly promoted and the schema is frozen. Of the six readiness gates,
this is the one that constrains future engineering rather than documentation, so it deserves
a policy and not just a declaration.

### The current rule is unworkable as written

`AGENTS.md` and `schemas/README.md` both say the same thing:

> Changing a schema is a governed action: it requires a version bump and a new ADR in
> `docs/internal/adr/`, and every existing file that references the changed schema must be
> updated in the same change.

Read literally, correcting a typo in a `description` string requires an ADR and an update to
all 117 entry files. That is not a rule anyone can follow, so in practice it gets either
ignored or worked around. ADR 0018 hit this directly: it needed to fix "Axis 1 / Axis 2 /
Axis 3" wording in five schema `description` annotations, correctly declined to invent an
exception on its own authority, and deferred the cleanup here.

A rule that cannot be followed for its cheapest case does not protect the expensive case. It
just teaches people that schema governance is theatre.

### What the schema state actually is

The contract is more settled than the pre-1.0 version number suggests. Two rounds of
deliberate tightening have already landed and completed:

- **ADR 0009 (pedagogical bar):** `tells`, `anti_patterns`, and `failure_modes` are required
  on every entry, enforced by both the schema (shape) and `validate.py` (substance).
- **ADR 0010 (domain and family), all three phases:** `domain` and `family` are required on
  formats, `family` on voices, with `subfamily` tightening per-family by cross-field check.
  Styles and tones carry neither, which is the intended scope, not an omission.

All 117 entries validate. There is no pending structural work queued against these schemas.

## Decision

### 1. Freeze scope

**Frozen** (the contributor-facing contract): `entry.universal`, `voice`, `tone`, `style`,
`format`, and `example`. `example.schema.json` is included because contributors author
example files by hand: CONTRIBUTING requires that "every new taxonomy entry should be
accompanied by at least one example file." Calling it a generated-artifact schema would be
wrong, and would let a breaking frontmatter change invalidate authored source with no
migration.

**Not frozen:** `diff-pair.schema.json`. The diff-pair generator is actively changing (it
gained commentary preservation this cycle), and diff-pairs are produced by tooling rather
than hand-authored from scratch. **Classes A, B, and C below still apply to it in full.**
Unfrozen means only that a class C change to it does not force a major version bump; it does
not exempt it from ADR review or entry migration.

Frozen means: no change to the **validated shape** without the class C process.

### 2. Change classes

Every `schemas/` edit falls into exactly one class.

#### The test

**Would this edit change the verdict on *any conceivable document*, not just the 117 in this
repository?** Two documents matter: one that validates today and might stop, and one that
fails today and might start passing. Either direction is a compatibility event.

Evaluating against the current corpus is **not** sufficient and is the trap this policy
exists to avoid. Setting `additionalProperties: false`, narrowing a `$ref`, or adding a
`format` assertion can leave all 117 entries passing while rejecting documents the published
schema previously accepted. That is a class C change even though nothing in the repo moves.

#### Class A - Annotation

Class A is defined by an **allowlist**, not by observed behaviour. Only these keywords, and
only where they carry no assertion:

`title`, `description`, `$comment`, `examples`

plus reordering that a JSON parser cannot observe (key order within an object; the order of
the `required` array, which is a set).

Nothing else is class A, however harmless it looks.

**Requires:** a normal PR, stating "annotation-only, class A" in the body. No ADR, no version
bump, no entry migration.

#### Class B - Additive optional

A new **optional** property, or a widened `enum`, `pattern`, or numeric bound. Every document
that validates today still validates, and the accepted set only grows.

**Requires:** a minor version bump and a `CHANGELOG.md` note. An ADR only if it introduces a
new concept rather than a field.

#### Class C - Breaking, or unclear

A new required property; removing or renaming a property; narrowing a type, `enum`, `pattern`,
or bound; promoting optional to required; **and every keyword not named in class A or B**,
explicitly including:

`$id`, `$schema`, `$ref`, `$defs` and any shared definition, `additionalProperties`,
`unevaluatedProperties`, `format`, and the combinators `allOf`, `anyOf`, `oneOf`, `not`,
`if`/`then`/`else`, `dependentRequired`, `dependentSchemas`.

Two of those deserve naming. A change to a **shared `$def` or to `entry.universal`** is class
C for *every* schema that composes it, because the per-axis schemas pull it in by `$ref`;
scope the migration accordingly. A **`$schema` draft change** is class C by default, since
draft revisions have altered keyword semantics.

**Requires:** an ADR, a **major** version bump, every affected file migrated in the same
change, and `validate.py` green before merge.

##### Amendment (2026-07-30): what "major bump" means before 1.0

This policy was written assuming post-1.0 versions and did not say what class C costs while
the project is at `0.y.z`. Left unstated, the first class C change had to either ship as
`1.0.0` (claiming a v1.0 readiness the open GATE 1 does not support) or reinterpret "major"
on the fly, which would weaken the policy one release after adopting it.

Deciding it explicitly instead: **while the version is `0.y.z`, a class C change bumps the
MINOR component** (`0.8.0` -> `0.9.0`). SemVer treats the whole `0.y.z` range as unstable and
makes no compatibility promise across it, so the minor is where breaking changes already
live pre-1.0. This is a stated exception with a defined end: **at `1.0.0` and after, class C
means the major component, with no exceptions.**

The practical consequence is worth naming, because it cuts the other way from most policy:
any class C change is *cheapest right now* and gets permanently more expensive at 1.0.0.
Contract fixes should be pulled forward, not deferred.

**The default is C.** If an edit is not obviously A or B, it is C. Unclear is not a fourth
class; it resolves to the most expensive one.

### 3. What the freeze does and does not guarantee

**Inside this repository, it guarantees:** no class C change lands without an ADR, a major
bump, and a migration that keeps `validate.py` green. That is enforceable today and is the
substance of the freeze.

**It does not yet guarantee anything to an external consumer, and this ADR does not claim
that it does.** An earlier draft promised that a consumer pinning `1.x` could not have a
document invalidated. That promise is not currently deliverable, for two concrete reasons:

1. Every `$id` resolves to a raw GitHub URL on `main`, so the published schema tracks the tip
   of the branch. There is no `1.x`-identified artifact to pin.
2. The per-axis schemas reference the shared one **relatively**
   (`{ "$ref": "entry.universal.schema.json" }`). A consumer who fetches `voice.schema.json`
   from a tag can still resolve the shared schema from wherever the base URI points, so even
   a tagged fetch can mix versions.

**Versioned schema IDs and version-consistent `$ref`s are therefore a prerequisite for
advertising external schema stability.**

**Resolved by [ADR 0020](0020-versioned-schema-ids.md) (2026-07-30).** Schemas are now served
from `.../schemas/v1/`, a contract-versioned path independent of the plugin version, and the
relative `$ref`s resolve within that version automatically. The freeze is an external
guarantee as of v0.9.0, and launch copy may describe a pinnable contract.

**Additive-optional stays available after the freeze.** Freezing must not mean the catalog
cannot grow: the planned breadth expansion may want `family` on styles and tones once those
axes pass ADR 0010's 12-member threshold. That is a class B change followed later by a class
C tightening, and the policy is designed to permit exactly that sequence.

### 4. Immediate consequence

The annotation cleanup deferred by ADR 0018 decision 5 is a **class A** change (it touches
`description` only) and was applied on ratification: the stale "Axis 1 / Axis 2 / Axis 3" wording in the five schema
`description` fields is corrected to the four-axis framing, with no version bump and no entry
migration.

### 5. Documentation updated on ratification

`AGENTS.md` "Schema Safety" and `schemas/README.md` both stated the blanket rule.
Both now carry a summary table pointing at this ADR, so there is one authority instead of
three restatements that can drift.

## Consequences

### Positive

- The cheapest case becomes followable, which is what makes the expensive case credible. A
  typo fix is a normal PR; a new required field still needs an ADR, a major bump, and a
  migration. The previous blanket rule made both cost the same, so in practice neither was
  paid.
- Class A is an allowlist rather than a behavioural test, so it cannot silently widen. An
  edit is annotation-only because of which keyword it touches, not because the current corpus
  happened not to notice.
- The compatibility test is stated against all conceivable documents rather than the 117 in
  the repo, which closes the hole where `additionalProperties: false` or a narrowed `$ref`
  reads as harmless because nothing local breaks.
- The freeze is compatible with the catalog's own growth plans, because class B survives it.
  A freeze that blocked additive fields would be abandoned the first time breadth expansion
  needed one.
- Unblocks a known-stale surface that ADR 0018 deliberately left rather than papering over.

### Negative

- Three classes plus an explicit keyword list is materially more to absorb than one sentence.
  The mitigation is that the expensive path is the default: anything not on the class A
  allowlist or squarely class B is class C, so misremembering the policy costs time, not
  compatibility.
- Freezing before v1.0 ships means any contract change discovered during launch preparation
  now costs an ADR and a major bump. That is the intended cost of a freeze; the bill arrives
  before the launch does, not after.
- The freeze delivers **less than a reader might assume from the word "frozen."** It is an
  internal discipline, not yet an external guarantee, because the published `$id` still
  tracks `main`. Decision 3 says so explicitly rather than letting the word carry an implied
  promise.
- `diff-pair.schema.json` is unfrozen, which is an asymmetry a future reader could mistake
  for an oversight. Decision 1 states it, and states that classes A/B/C still govern it.

### Neutral

- **Prerequisite for external stability, resolved the next day:** versioned schema IDs and
  version-consistent `$ref`s, delivered by [ADR 0020](0020-versioned-schema-ids.md). It was
  done immediately rather than deferred because a `$id` change is class C under this very
  policy, and pre-1.0 that bill is a minor bump while post-1.0 it is a real major plus every
  pinned consumer. This was the last cheap moment.
- **On applying the annotation cleanup under a class defined in the same change.** This ADR
  defines class A and then immediately uses it, which is a shape worth naming rather than
  glossing. What makes it a sequence rather than a circle is that the policy was drafted as
  Proposed, put to the maintainer as a decision with alternatives, and ratified explicitly
  before any schema file was touched. Had the annotations been edited first and the class
  written afterwards to cover them, that would be the smell.
- The schemas carry no internal `version` field. Version means the repository and plugin
  version throughout this ADR, which is what "version bump" has always meant here. That is
  also part of why the external guarantee is not yet available.
- This ADR does not touch `review_status` lifecycle (GATE 1), which is a separate and
  human-bottlenecked gate.

---
adr_id: "0018"
title: "Name the model four-axis: align the label with the implementation"
date: 2026-07-29
status: Accepted
supersedes_context: >
  supersedes the LABELLING decisions in ADR 0001 (three-axis taxonomy) and ADR 0004
  (Voice and Tone as paired dimensions within one axis). Preserves every structural
  decision both ADRs made. Closes the "three axes vs four directories" reconciliation
  tracked in ROADMAP.md and as backlog item S3.
related:
  - docs/internal/adr/0001-three-axis-model.md
  - docs/internal/adr/0004-voice-and-tone-as-paired-axis.md
  - docs/internal/backlog.md
---

# 0018 - Name the model four-axis: align the label with the implementation

## Status

Accepted (2026-07-29). Supersedes the labelling decisions in ADR 0001 and ADR 0004; both
remain in force on everything structural.

## Context

The catalog has been described two ways since v0.1.0, and the two contradict each other in
published documentation.

**What every mechanical surface says: four.**

- Four catalog directories: `taxonomy/voices/`, `tones/`, `styles/`, `formats/`
- Four per-axis JSON Schemas: `voice.schema.json`, `tone.schema.json`, `style.schema.json`, `format.schema.json`
- Four values in the `axis` enum in `schemas/entry.universal.schema.json`
- Four entries in `AXES` in `tools/validate.py`, which drives every validation pass
- Four separate parameters on the composer, applied in a voice -> tone -> style -> format precedence order (ADR 0016)
- Four separate selections in the `entry-recommender` and `style-profile` skills

**What the outward-facing copy says: four.**

`.claude-plugin/plugin.json` (the marketplace listing), `QUICKSTART.md`,
`.github/workflows/release.yml` (release notes), `ROADMAP.md`, and the `README.md` subtitle
all say "four orthogonal axes."

**What the design documentation says: three.**

`README.md` carries a "The Three-Axis Model" section with `Axis 1 - Voice and Tone`,
`Axis 2 - Style`, `Axis 3 - Format`. `AGENTS.md` carries the same. The published site has a
page at `/concepts/three-axis-model/`. The glossary defines an axis as "one of the three
orthogonal dimensions."

So a reader meeting this project through the marketplace is told four, and a reader who
follows the link to understand the design is told three.

### Both founding ADRs predicted this exact failure

This is not a discovered inconsistency; it is a known cost that was accepted and then not
paid down.

ADR 0001, Negative consequences:

> The "three-axis" label requires explanation because there are four catalog directories.
> First-time readers may count four and expect the model to be called four-axis.

ADR 0004, Negative consequences (emphasis added):

> The "three-axis" name requires explanation since there are four catalog directories and
> four frontmatter parameters (`voice`, `tone`, `style`, `format`). **Every piece of
> documentation that mentions "three-axis" needs a parenthetical explaining the Voice/Tone
> pairing.**

That parenthetical was the mitigation. It was never applied consistently, and the resulting
drift became a tracked roadmap item. A mitigation that requires perpetual discipline across
every document, applied by many hands over time, is not a mitigation; it is a recurring bill.

### ADR 0001's own reasoning already argued four

ADR 0001's Context establishes orthogonality over four things, not three:

> The core insight is that Voice (who is speaking), Tone (how they feel right now), Style
> (what kind of writing), and Format (the structural container) are orthogonal. You can hold
> any three constant and vary the fourth to produce meaningfully different results.

"Hold any three constant and vary the fourth" is a four-dimensional claim. The Decision
section then grouped two of those four for presentational reasons, leaving the label at odds
with the argument that justified it.

### What the three-axis label was actually buying

ADR 0004 is explicit that the reason was terminological convention, not structure:

> The AP Stylebook, the Mailchimp content guide, and most brand style guides use "voice and
> tone" as a single compound noun without drawing a distinction.

That is a real consideration, and it is worth less here than it would be in a brand guide.
This catalog's audience selects voice and tone as two independent runtime parameters. The
compound noun is a convention for humans reading a style guide once; this is an instruction
set composed per task. ADR 0004 itself made the same point when arguing for separation: the
persistent-versus-situational distinction "is the distinction that makes the catalog useful
for programmatic composition, not just human reading."

## Decision

**The model is named and documented as four axes: Voice, Tone, Style, Format.**

1. "Four axes" is the canonical framing in all documentation, prose, and outward-facing copy.
2. The Voice/Tone relationship is still documented, because it is genuinely the most
   confusable pair in the catalog. It is described as **two closely related axes that are
   modelled and validated separately**, not as two halves of one axis. The
   persistent-versus-situational rule (voice is stable across contexts; tone varies per
   piece) remains the guidance for deciding which directory an entry belongs in.
3. The published page moves from `/concepts/three-axis-model/` to
   `/concepts/four-axis-model/`. The old route is kept as an Astro redirect, so external
   links continue to resolve and the route-parity guard still sees the route present.
4. `CHANGELOG.md` is not rewritten. It is a historical record, and entries describing the
   three-axis model were accurate when written. The same applies to the frozen research and
   planning snapshots under `docs/internal/_working/` and the dated strategy documents: they
   record what was believed at the time.
5. **The `schemas/` annotations are deliberately not changed here.** All five schema files
   (`entry.universal`, plus `voice`, `tone`, `style`, `format`) carry "Axis 1 / Axis 2 /
   Axis 3" wording in `description` fields. Fixing them is correct but is blocked on a
   governance question this ADR should not answer by fiat: `AGENTS.md` requires "a version
   bump and an ADR entry" for any change to `schemas/`, a rule written for structural changes
   that can invalidate existing entries. A `description` string cannot. Rather than
   silently invent an annotation-only exception, this is sequenced into the schema-freeze
   work, whose post-1.0 change policy is the right place to define that class of edit. Until
   then the schema annotations are the one known-stale surface, recorded in the backlog.
6. ADR 0001 and ADR 0004 keep their status as Accepted for everything structural. Only their
   labelling decisions are superseded. Specifically, these decisions from 0004 remain in
   force and are unaffected: separate entry directories, separate JSON Schemas with different
   required fields, separate composer parameters, and `confusable_with` as the
   cross-axis disambiguation hook.

## Consequences

### Positive

- The marketplace description, the QUICKSTART, the README, `AGENTS.md`, and every published
  site page now agree. A reader who counts four directories and is told "four axes" needs no
  reconciliation. The `schemas/` annotations are the one exception, deliberately deferred per
  decision 5 above and guarded by a test so the gap stays visible rather than forgotten.
- The documentation tax ADR 0004 named is retired. No parenthetical is required, so nothing
  degrades when the next document is written by someone who has not read this ADR.
- The label now matches the reasoning in ADR 0001's Context and the mechanics in `validate.py`.
- No code changes. The `axis` enum, the directories, the schemas, and the composer precedence
  were already four-valued; this ADR changes only what they are collectively called.

### Negative

- Readers arriving from a brand-writing background, where "voice and tone" is one compound
  noun, now meet a model that splits them. The Voice/Tone section is retained specifically to
  absorb that, and it has a job it did not have before: it must earn the split rather than
  explain away a grouping.
- Two ADRs are partially superseded, which is a heavier bookkeeping state than either fully
  standing or fully replaced. Anyone reading 0001 or 0004 needs this ADR to know which parts
  still hold. Both files carry a pointer here to make that unavoidable.
- One published URL changes. Mitigated by the redirect, but any external copy of the old link
  now takes an extra hop.

### Neutral

- The count is not a claim that writing has exactly four orthogonal dimensions. As ADR 0001's
  own Neutral section noted about three, it is a claim that these are sufficient for the
  catalog's use cases. Audience remains a metadata constraint (`target_audience`, `use_for`),
  not a fifth axis.
- Entry counts stay uneven across the four axes (Format has 52; Voice, Tone, and Style have 15
  each). Naming them peers does not imply they are equally developed, and the breadth gap is
  tracked separately in the backlog.

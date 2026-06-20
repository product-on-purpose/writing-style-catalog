# Working Backlog - Content + Skill

> Internal working tracker. The public, distilled version is [`ROADMAP.md`](../../ROADMAP.md)
> at the repo root; this file is the detailed companion: priorities, rationale, the source
> that justifies each item, the editable surface to change, and a rough effort. Living doc -
> update the snapshot date and check items off as they ship.

**Last updated:** 2026-06-03 (after the v0.2.0 marketplace launch and the comprehensive-catalog
vision; the foundation - taxonomy, adherence gate, anchor topics, conflict-aware composition -
is now designed in [`release-plans/plan_v0.3.0/`](release-plans/plan_v0.3.0/release-plan.md)).
**Priority key:** P1 = highest leverage, do next; P2 = valuable, after P1; P3 = hygiene / opportunistic.

This doc holds two horizons: the **near-term, evidence-led work** (sharpen the proven core,
make composition a guarantee) and the **long-term ambition** (the world's most comprehensive
catalog, with a dozen-plus samples of everything). The Vision section below reconciles them so
the second does not erode the first.

---

## North star (why the near-term priorities are what they are)

The whole catalog rests on **one proven result**: a blind adherence test attributed 8 of 8
confusable composition pairs correctly (chance about 0.4 percent), which means the per-entry
`llm_instruction_phrasing` genuinely steers model output. Everything near-term either
**strengthens that result** (content) or **turns "composable" from a claim into a guarantee**
(skill). That proven core is also the *foundation* the comprehensive catalog gets built on:
you scale from a thing that demonstrably works, behind a gate that keeps every addition working.

---

## Vision: the world's most comprehensive catalog (and the tension to manage)

**The ambition (maintainer-stated, 2026-06-02):** the world's most comprehensive catalog of
voices, tones, styles, and formats, with **a dozen or more worked samples of every entry**.

**This is not new territory; it was designed and then parked.** Prior working docs already map
it: an aspirational inventory of roughly **180 format candidates and 70 voice candidates**
([`_working/catalog-inventory-aspirational_2026-05-16.md`](_working/catalog-inventory-aspirational_2026-05-16.md)),
a Phase 2 expansion spec targeting **120 entries (30 per axis) at a full pedagogical bar**
([`_working/phase-2-catalog-expansion_2026-05-15.md`](_working/phase-2-catalog-expansion_2026-05-15.md)),
and a **domain/family taxonomy** (5 domains: professional, public, personal, ceremonial,
contemplative; 17 format families; 5 voice families) to keep that breadth navigable
([`_working/domain-and-family-taxonomy_2026-05-15.md`](_working/domain-and-family-taxonomy_2026-05-15.md)).
After the adherence test passed, the ROADMAP deliberately deferred all of it ("ship it; do not
expand breadth to chase quality; defer Phase 2 behind a usage signal").

**The real tension.** "Most comprehensive" and "depth over breadth" look opposed, but they only
truly conflict under one failure mode: scaling breadth on a thin foundation, producing many
mixed-quality entries that dilute the one proven signal and pile on maintenance with no usage
validation. That is exactly the risk the ROADMAP was guarding against. It is avoidable.

**The reconciliation: comprehensiveness is the destination; a quality gate is the road.** The
first 60 entries work because each produces *measurably distinguishable* output. If every new
entry must clear that same bar, breadth stops trading against quality. The binding constraint
then is not ambition, it is **machinery**: 120 entries times 12 samples is about **1,440
samples** (versus roughly 195 today), which no one hand-authors at a uniform bar. So the path
to "most comprehensive" runs *through tooling*:

1. a **generation pipeline** (extend the existing `tools/diff-pair-generator.py` pattern) that
   produces samples and entry scaffolds at scale,
2. the **adherence test as an automated contributor gate** (an entry earns its place only by
   producing distinguishable output - the empirical wedge the project already validated),
3. the **domain/family taxonomy** codified (draft ADR 0010) so 180 formats stay legible, and
4. **conflict-aware composition** (S1) so the exploding combinatorial space is actually usable.

**Therefore the sequencing is:** build the machinery on the proven 60 first (the near-term
P1 items below are precisely that foundation), then scale breadth and sample-depth behind the
gate (the Expansion Program section). Done in that order, "most comprehensive" and "proven
quality" reinforce each other instead of fighting.

**One open scope decision for the maintainer.** The aspirational inventory deliberately scopes
*out* fiction, poetry, legal/medical/scientific writing, working journalism, government/policy,
children's writing, and translation (each a field with its own conventions). "World's most
comprehensive" may mean revisiting some of those boundaries. That is a maintainer call, not a
mechanical one; flagged here, not assumed.

---

## Status snapshot

| Area | State (verified 2026-06-02) |
|---|---|
| Catalog size | 60 entries, 15 per axis (Voice, Tone, Style, Format) |
| Adherence result | 8/8 blind; 2 "dramatic", 4 "clear", **2 "subtle"**, 0 "identical" |
| Composition | **Not conflict-aware** - `compose_instruction` concatenates phrasings; never reads `avoid_with`/`pairs_well_with` |
| Diff-pair coverage | async-standups + morning-routine have pairs; **`service-database-choice` has zero** |
| Sample depth | ~195 worked examples across **3 anchor topics** (~3 per entry); vision target is **12+ per entry** |
| Expansion design | Already drafted and parked: ~180 format / 70 voice aspirational inventory; Phase 2 = 120 entries; domain/family taxonomy (ADR 0010 draft) |
| Adherence gate | Run once as an audit; **not yet automated** (E1 prerequisite for scale) |
| Marketplace | v0.2.0 listed in `product-on-purpose/agent-plugins`; install live |
| Repository legibility | Done (REPOSITORY.md, folder READMEs, ADR 0013) |
| CI | Node 24; validate + validate-plugin + build-site + CodeQL; release automation |

---

## Near-term content backlog (sharpen the proven core)

> Phase A. Strengthen the proven result and raise the per-entry bar on the existing 60. This
> is the quality reference the Expansion Program then scales against.

### C1 (P1) - Sharpen the two "subtle" confusable pairs
The adherence test rated exactly two pairs only "subtle" (the genuinely-close confusables):
- `pragmatic-architect` vs `senior-consultant` (voice; within the "expert voice" cluster)
- `narrative-case-study` vs `chronological-narrative` (style; within the narrative styles)

These are the **weakest seams in the one result the whole library rests on**, so tightening
their `confusable_with` distinctions from both sides is worth more than ten new entries.
- **Source:** `_LOCAL/audit/2026-05-31_adherence-smoke-test.md` (the distinguishability table +
  the "Where the signal points" section). Note: `_LOCAL/` is local-only / gitignored, not in
  the published repo; the committed distillation is `ROADMAP.md` line 9.
- **Editable surface:** the `confusable_with` blocks (and the surrounding language patterns) in
  - `taxonomy/voices/pragmatic-architect/ENTRY.md`
  - `taxonomy/voices/senior-consultant/ENTRY.md`
  - `taxonomy/styles/narrative-case-study/ENTRY.md`
  - `taxonomy/styles/chronological-narrative/ENTRY.md`
- **Effort:** small-medium. After edits run `python tools/validate.py` then
  `python tools/build-indexes.py`.

### C2 (P1) - Diff-pairs for the `service-database-choice` topic
It currently has **zero** diff-pairs, despite being the best-isolated anchor topic; the other
two topics have several. Diff-pairs are the catalog's sharpest teaching tool because they hold
the topic constant and vary exactly one axis.
- **Why this is partly mechanical:** the single-entry renders already exist under
  `examples/vertical-slices/service-database-choice/` (every `style-*`, `tone-*`, `format-*`,
  and voice file), and diff-pairs are produced by `tools/diff-pair-generator.py` (named in each
  diff-pair's `generator:` frontmatter). Drafting a pair is: generate from the two existing
  renders, then author the "What to notice" prose.
- **Draft first (this doubles as C1):** the two subtle pairs *on this topic* -
  `style-narrative-case-study` vs `chronological-narrative` and
  `voice-pragmatic-architect` vs `senior-consultant`. Then a couple of dramatic/clear pairs
  (e.g. `format-adr` vs `whitepaper`) for teaching range.
- **Editable surface / model:** mirror `examples/diff-pairs/async-standups/voice-pragmatic-architect-vs-senior-consultant.md`
  (frontmatter -> "What to notice" -> "A:" render -> "B:" render). New pages are picked up by
  the site generator; rebuild with `cd site && npm run build` and the route/link guards.
- **Effort:** small per pair (generator + prose).

### C3 (P2) - Deepen high-weight entries
Add tells, anti-patterns, failure modes, and before/after micro-examples to the entries that
carry the most composition weight, instead of adding new entries to chase coverage.
- **Editable surface:** the heaviest-used `taxonomy/**/ENTRY.md` files (start with the four in
  C1, then the entries that appear most in recipes).
- **Effort:** ongoing; size to appetite.

---

## Near-term skill / tooling backlog (build the foundation)

> Phase A. The machinery the comprehensive catalog is built on. S1 in particular is a
> prerequisite for scale, not just a feature.

### S1 (P1) - Make `compose-instruction` conflict-aware
**The single highest-leverage item in the roadmap.** It hardens the core promise and is the
stated gate before any MCP server (S2).

- **What it does today:** `skills/writing-instruction-builder/scripts/build-instruction.py`,
  function `compose_instruction` (lines 163-180), loads each selected entry, pulls only its
  `llm_instruction_phrasing`, and joins the blocks with `\n\n`. That is the whole algorithm -
  string concatenation. It never reads the relationship fields.
- **The data already there, unused:** every entry's frontmatter carries
  `pairs_well_with`, `avoid_with`, and `confusable_with` (e.g. `pragmatic-architect` has
  `avoid_with: [reverent, pastoral]`). The data is curated and `tools/validate.py` already
  enforces that every referenced ID exists. `_parse_simple_yaml` already parses these lists;
  the composer simply ignores them.
- **The concrete failure this allows:** composing `voice=pragmatic-architect` + `tone=reverent`
  staples together "lead with tradeoffs, no softening" and "approach with reverence and weight"
  - an incoherent instruction - even though `reverent` is literally in pragmatic-architect's
  `avoid_with`. No warning is emitted.
- **The change (three layers, increasing ambition):**
  1. **Detect + warn** - cross-check each selection against the others' `avoid_with` (decide:
     is `avoid_with` symmetric?), flag conflicts, and affirm `pairs_well_with` matches.
  2. **Precedence** - apply the order voice -> tone -> style -> format (already the iteration
     order at `build-instruction.py:161`, just not used to resolve anything) so the
     higher-precedence axis leads and a contradiction is annotated, not silently doubled.
  3. **(Optional) suggest** - recommend a compatible substitute from `pairs_well_with`.
- **Touches:** `build-instruction.py` (surface two already-parsed fields + a conflict pass),
  `skills/writing-instruction-builder/SKILL.md` (document the behavior), likely a new ADR for
  composition semantics, and tests under `tests/`.
- **Open design decisions (worth a short brainstorm before coding):** warn vs hard-block;
  `avoid_with` symmetry; how literally to "resolve" prose blocks (realistically: order +
  annotate, not programmatic merge).
- **Effort:** medium. Bounded - the data and parser exist.

### S2 (P2) - MCP server
Expose composition to any MCP-compatible agent, reusing the proven `pm-skills-mcp` pattern
rather than starting fresh. Explicitly **after** S1 (conflict-aware composition) lands, so the
server exposes the guaranteed behavior, not the naive concatenation.
- **Effort:** medium-large; new machinery, so gate it behind a real consumer signal.

### S3 (P3) - Tooling hygiene
- **`remark-resolve-links`** - the 4th pm-skills site validator (rewrites `.md` links to
  Starlight slugs at build time), deferred during the Astro conformance work. Until it lands,
  author internal cross-page links as relative-slug URLs. Source:
  `docs/internal/release-plans/astro-starlight-conformance/` + `scripts/README.md`.
- **Reconcile the "three axes vs four directories" framing** so the model is described
  consistently across `README.md`, the taxonomy, and the contributor docs (Voice and Tone are
  two dimensions of one axis, but live in separate directories).
- **`review_status` governance** - new entries must start at `draft`, not `stable`; the
  60-entry seed set is the reviewed `stable` baseline (already documented in `CLAUDE.md` /
  `AGENTS.md`). Keep enforcing this on new contributions.

---

## Expansion Program (Phase B: the comprehensive catalog, sequenced behind the gate)

> The scale phase. Do **not** start the breadth/depth tracks (E2, E3) until the gate and
> generation machinery (E1) exist and the near-term P1 foundation has landed; otherwise this
> reintroduces the exact "120 mixed-quality entries" risk the ROADMAP named. E1 is the unlock.

> **Foundation designed (2026-06-03).** The machinery below is specified in the v0.3.0
> release plan: ADR [`0010`](adr/0010-domain-and-family-organization.md) (the frozen taxonomy
> for E2), [`adherence-gate-spec.md`](release-plans/plan_v0.3.0/adherence-gate-spec.md) (E1),
> [`anchor-topics.md`](release-plans/plan_v0.3.0/anchor-topics.md) (the 12-topic substrate for
> E3), and S1 conflict-aware composition. v0.3.0 builds the machinery on the proven 60; E2/E3
> content scale follow in v0.4.0+. See [`release-plans/plan_v0.3.0/`](release-plans/plan_v0.3.0/release-plan.md).

### E1 (P1 for scale) - The quality gate + generation machinery
Comprehensiveness is rate-limited by tooling, not appetite. Build this first; everything else
in Phase B depends on it.
- **Automate the adherence test as a contributor gate.** Today it is a one-off audit
  (`_LOCAL/audit/2026-05-31_adherence-smoke-test.md`). Turn it into a repeatable harness: render
  a candidate entry against its nearest neighbors on a fixed topic, have a blind judge attribute
  them, and **reject any entry whose output is not measurably distinguishable**. This is the
  rule that lets breadth scale without diluting the proven signal. Reuse the sibling
  family's eval patterns rather than build fresh.
- **Generation pipeline.** Extend `tools/diff-pair-generator.py` into a fuller generator:
  scaffold an entry from the schema, render its samples across the topic set, and emit the
  cross-reference and diff-pair stubs. Hand-authoring 1,440 samples is not viable; generation
  plus the gate is.
- **Validation at scale.** Extend `tools/validate.py` so the per-entry pedagogical bar is
  *checked*, not just hoped for (presence of tells, anti-patterns, failure modes, cross-refs,
  before/after pair, and the minimum sample count).
- **Effort:** medium-large. This is the highest-leverage Phase B item because it gates the rest.

### E2 (P2) - Breadth: toward the full inventory
Grow the catalog toward the aspirational inventory, organized so it stays legible.
- **Concrete next milestone (already designed):** Phase 2 target of **30 entries per axis
  (120 total)**, each at the full pedagogical bar. Source spec:
  [`_working/phase-2-catalog-expansion_2026-05-15.md`](_working/phase-2-catalog-expansion_2026-05-15.md).
- **Stretch toward "comprehensive":** the aspirational inventory of roughly **180 formats and
  70 voices** (plus proportional tone/style growth), drawn from
  [`_working/catalog-inventory-aspirational_2026-05-16.md`](_working/catalog-inventory-aspirational_2026-05-16.md).
- **Prerequisite - codify the organizing taxonomy.** At 30+ entries per axis a flat list gets
  noisy (an RFC next to a eulogy next to a wedding toast). Promote the draft domain/family
  taxonomy (5 domains, 17 format families, 5 voice families) to ADR 0010 and absorb it into the
  schema *before* mass-adding entries, so entries are born categorized. Source:
  [`_working/domain-and-family-taxonomy_2026-05-15.md`](_working/domain-and-family-taxonomy_2026-05-15.md)
  and the draft `_working/0010-domain-and-family-organization.md`.
- **Order within E2:** taxonomy codified -> exemplar entries per new family (catch bar drift
  early) -> fill out each family behind the E1 gate.
- **Effort:** large; the bulk of the program. Size by family, not all at once.

### E3 (P3 until E1 lands) - Sample-depth: a dozen-plus of everything
Take per-entry worked samples from ~3 to **12 or more**.
- **Today:** roughly 195 worked examples across **3 anchor topics** (async-standups,
  morning-routine, service-database-choice), about 3 renders per entry.
- **Target:** 12+ samples per entry. Mechanically this means expanding the **anchor-topic set**
  (from 3 toward ~12, chosen for spread across the domains so every entry has a natural home
  topic) and/or multiple samples per topic, all produced by the E1 generator and cleared by the
  E1 gate. At 120 entries this is on the order of **1,440 samples** - a tooling output, not a
  writing project.
- **Topic selection matters:** pick anchor topics that are well-isolated (like
  service-database-choice) so the single-variable teaching stays sharp at volume.
- **Effort:** large, but mostly compute + review once E1 exists.

### E4 (P3) - Meta-layer for scale
What a 120-to-180-entry catalog needs to stay usable: navigation aids, visual taxonomy
diagrams (per the family standard), per-axis curation rationale, and richer governance/
contributor docs (so external contributions can clear the E1 gate). Source: the meta-layer
scope in the Phase 2 spec.

### Definition of done (the comprehensive catalog)
- Every axis is filled out to its taxonomy (target 30/axis near-term; toward the full inventory
  long-term), organized by domain/family.
- Every entry meets the full pedagogical bar (tells, anti-patterns, failure modes, dense
  cross-references, mini-glossary, before/after pair).
- Every entry carries **12 or more** worked samples spanning multiple anchor topics.
- Every entry has **passed the automated adherence gate** (measurably distinguishable output).
- Composition across the whole space is conflict-aware (S1), so the catalog is navigable, not
  just large.

### Suggested sequencing (milestones, not dates)
1. **Foundation (Phase A):** C1 + C2 (sharpen + service-database-choice diff-pairs), S1
   (conflict-aware composition). Locks the quality reference and makes composition a guarantee.
2. **Unlock (E1):** automated adherence gate + generation pipeline + bar-checking validation.
3. **Structure (E2 prerequisite):** codify the domain/family taxonomy (ADR 0010) + schema.
4. **Scale (E2 + E3):** grow to 30/axis behind the gate, each entry with 12+ generated samples;
   then extend toward the full inventory family by family.
5. **Polish (E4):** meta-layer and contributor on-ramp so the catalog scales beyond one author.

---

## Deliberately deferred (not a backlog - a "no for now" with reasons)

From `ROADMAP.md` "Deliberately deferred":
- **Composer single-page app** - the docs site already lets people browse and compose; a
  separate app duplicates it.
- **TypeScript / Python SDKs** - no consumer yet; the empty `packages/` stubs were removed
  (recoverable from git if a real need appears).
- **Community quality-scoring / authoring machinery** - provided by sibling projects in the
  same family; consume those rather than rebuild.

What stays unique to this project is the catalog itself: a proven, (soon) conflict-aware,
composable set of writing instructions no sibling or external tool provides.

---

## Source map

| Topic | Where |
|---|---|
| Distilled public roadmap | [`ROADMAP.md`](../../ROADMAP.md) |
| Adherence test (the 8/8, the two subtle pairs) | `_LOCAL/audit/2026-05-31_adherence-smoke-test.md` (local-only / gitignored) |
| Content growth options | `_LOCAL/audit/2026-05-31_content-growth-strategy.md` (local-only) |
| Aspirational inventory (~180 formats / 70 voices) | `docs/internal/_working/catalog-inventory-aspirational_2026-05-16.md` |
| Phase 2 expansion spec (120 entries, pedagogical bar) | `docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md` |
| Domain/family taxonomy (5 domains, families) | `docs/internal/_working/domain-and-family-taxonomy_2026-05-15.md`; draft ADR `_working/0010-domain-and-family-organization.md` |
| Composition code | `skills/writing-instruction-builder/scripts/build-instruction.py` |
| Skill contract | `skills/writing-instruction-builder/SKILL.md` |
| Entry schema + relationship fields | `schemas/*.schema.json`; any `taxonomy/**/ENTRY.md` |
| Diff-pair model | `examples/diff-pairs/async-standups/*.md`; generator `tools/diff-pair-generator.py` |
| Site generation architecture | ADR 0011; `scripts/gen-site.mjs`; `scripts/README.md` |
| Repository map / conventions | `REPOSITORY.md`; ADR 0013 |
| v0.2.0 marketplace launch | `docs/internal/release-plans/plan_v0.2.0/` |

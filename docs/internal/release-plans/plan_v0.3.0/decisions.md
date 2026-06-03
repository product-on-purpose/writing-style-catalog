# v0.3.0 / Expansion Decision Record

> The consolidated decision log for the expansion-foundation effort. It dedupes the open
> decisions raised across four sources: the scaling strategy's decision matrix
> ([`../../scaling-the-library-100x.md`](../../scaling-the-library-100x.md)), ADR
> [`0010`](../../adr/0010-domain-and-family-organization.md), the
> [`adherence-gate-spec.md`](adherence-gate-spec.md), and [`anchor-topics.md`](anchor-topics.md),
> plus [`spec.md`](spec.md) Section 6. Each decision has context, options, and a recommendation;
> the maintainer slot is where the call gets recorded. Until a P0 row is decided, v0.3.0 stays
> Proposed and execution does not begin.

**Status:** OPEN - awaiting maintainer decisions.
**Priority key:** P0 = blocks v0.3.0 execution; P1 = needed during v0.3.0; P2 = can defer past v0.3.0.

---

## Summary table

| # | Decision | Recommendation | Priority | Maintainer call |
|---|---|---|---|---|
| A1 | Accept the v2 taxonomy cuts | Accept as-is | P0 | _pending_ |
| A2 | Subfamily 12-member trigger: hard vs soft | Hard cutoff | P1 | _pending_ |
| A3 | Subfamily naming pass | Defer to a gate-arbitrated follow-on | P2 | _pending_ |
| A4 | Facet-tag enum scope | Ship the 7, values widen on demand | P1 | _pending_ |
| A5 | Coverage target bands | Accept dense 12-20 / narrow 3-8 | P1 | _pending_ |
| A6 | Freeze the four axes | Freeze (ratify ADR 0010 sec. 1) | P0 | _pending_ |
| B1 | `avoid_with` symmetry | Symmetric (union both directions) | P0 | _pending_ |
| B2 | Conflict handling: warn vs block | Warn + precedence, never block | P1 | _pending_ |
| C1 | What the gate scores | Distinguishability AND a quality rubric | P0 | _pending_ |
| C2 | Judge policy | Cross-family judge + 15% human audit | P0 | _pending_ |
| C3 | Held-out reference set | Freeze the 60 as ground truth | P0 | _pending_ |
| C4 | Gate thresholds | Commit pilot numbers, then tune | P1 | _pending_ |
| D1 | The 12 topics + slate balance | Accept 4/2/2/2/2 | P0 | _pending_ |
| D2 | `morning-routine` domain | Relational | P1 | _pending_ |
| D3 | `accountability` family home | Test on the boundary (topic 3) | P2 | _pending_ |
| D4 | The 9 new topic slugs | Accept first-draft, rename now if any jar | P1 | _pending_ |
| E1 | Scope boundaries | Admit journalism + plain-language legal/medical, gate-arbitrated; hold fiction/poetry/translation/children's | P1 | _pending_ |
| E2 | Journalism placement | A `public` subfamily, not a 6th domain | P2 | _pending_ |
| F1 | Breadth vs depth weighting | ~600 entries, depth-weighted | P1 | _pending_ |
| F2 | Migration sequencing vs E1 | Taxonomy -> backfill -> gate -> tighten to required | P0 | _pending_ |
| F3 | Resourcing posture | Fund 2-4 people, or consciously cap | P0 | _pending_ |

---

## Group A - Taxonomy and structure (ADR 0010)

### A1 - Accept the v2 taxonomy cuts (P0)
**Context.** ADR 0010 codifies 5 domains (professional, public, relational, ceremonial, contemplative), 16 format families, and 6 voice families (expert, care, principal, witness, dissident, pastoral), with evocative family names. This supersedes a stale v1 (6 domains, 14 functional-sounding families). The taxonomy is load-bearing: the adherence gate's neighbor sets are defined by the tree, so loose categories make loose gates.
**Options.** A) Accept the v2 cuts and names as-is. B) Accept the cuts but rename specific families. C) Re-cut the domains/families. D) Drop the domain layer, families only. E) Stay flat, no taxonomy.
**Recommendation.** **A.** The v2 cuts were already iterated once against maintainer feedback and stress-tested against the ~195-format inventory; they are sound and naming is evocative rather than database-flat. Renames (B) are cheap to apply later if a name jars in use; do not block on them.
**Source.** spec #1; scaling matrix #7; ADR 0010.
**Maintainer decision:** _pending_

### A2 - Subfamily 12-member trigger: hard cutoff vs soft alarm (P1)
**Context.** The third level (subfamily) becomes required once a family passes 12 members. `instruction` (~19) and `witness` (~18) already cross it.
**Options.** A) Hard enforceable cutoff at 12 (validator errors). B) Soft alarm in the coverage ledger; maintainer decides each split.
**Recommendation.** **A (hard).** Determinism beats judgment here: a hard cutoff prevents a family quietly ballooning to 30 flat members, which is exactly the noise the taxonomy exists to prevent. The cost (an occasional forced split) is small and the split is itself gate-checkable.
**Source.** ADR 0010 open question 6.
**Maintainer decision:** _pending_

### A3 - Subfamily naming pass (P2)
**Context.** ADR 0010 fixes the three levels but does not enumerate subfamily names. First binding cases: `instruction` (reference vs tutorial) and `witness`.
**Options.** A) Name them now, inline. B) Defer to a gate-arbitrated follow-on working doc before mass-add into those two families.
**Recommendation.** **B (defer).** Subfamily names are best cut against real candidate entries, not in the abstract; the gate's de-dup behavior will reveal the natural seams. Not needed until v0.4.0 touches those families.
**Source.** ADR 0010 open question 1.
**Maintainer decision:** _pending_

### A4 - Facet-tag enum scope (P1)
**Context.** A governed faceted-tag namespace (`channel:`, `formality:`, `modality:`, `epistemic:`, `length:`, `stance:`, `delivery:`) absorbs the rejected fifth axes and is the highest-leverage anti-rot mechanism.
**Options.** A) Ship all 7 facets with seed value lists in `tools/taxonomy.py`. B) Start with a narrower set and widen on demand.
**Recommendation.** **A for the 7 facet keys (closed set), values widen on demand.** The keys are the contract and should be fixed now so tags are consistent from the first backfilled entry; the value lists can grow without a schema change.
**Source.** ADR 0010 open question 2.
**Maintainer decision:** _pending_

### A5 - Coverage target bands (P1)
**Context.** The coverage ledger needs per-family target bands so "comprehensive" has a number. Proposed: dense families 12-20, narrow 3-8.
**Options.** A) Accept the bands and the proposed per-family assignment. B) Adjust bands or reassign families.
**Recommendation.** **A.** The proposed dense set (`instruction`, `deliberation`, `correspondence`, `broadcast`, `tribute`, `devotion`, `witness`) matches where the inventory is genuinely deep; the rest as narrow is honest. Tune after the first fill if a band feels wrong.
**Source.** ADR 0010 open question 3.
**Maintainer decision:** _pending_

### A6 - Freeze the four axes (P0)
**Context.** ADR 0010 section 1 freezes Voice/Tone/Style/Format and demotes every candidate fifth axis (rhetorical stance, epistemic stance, register, medium, persona, modality) to a facet tag or subfamily.
**Options.** A) Freeze the four axes. B) Add a fifth axis for one of the candidates.
**Recommendation.** **A (freeze).** None of the candidates passes the axis test (orthogonal, one-value-per-instruction, independently changes the phrasing); all are cleaner as facets. A fifth axis multiplies the combinatorial space and breaks ADR 0001.
**Source.** ADR 0010 section 1; scaling matrix #7.
**Maintainer decision:** _pending_

## Group B - Composition (S1)

### B1 - `avoid_with` symmetry (P0)
**Context.** Conflict-aware composition must decide whether `avoid_with` is symmetric: if A lists B in `avoid_with` but B does not list A, is the pair still flagged?
**Options.** A) Symmetric - flag if either entry lists the other (union both directions). B) Directional - flag only the listed direction.
**Recommendation.** **A (symmetric).** A conflict is a property of the pair, not of one entry's bookkeeping; asymmetry would make the warning depend on authoring order. Symmetric is deterministic and forgiving of incomplete cross-references. Validation can still warn on missing reciprocal links as a hygiene nudge.
**Source.** spec #4; scaling matrix #9.
**Maintainer decision:** _pending_

### B2 - Conflict handling: warn vs hard-block (P1)
**Context.** When a composition pairs entries that conflict, the skill can warn, or refuse.
**Options.** A) Warn and still compose, applying voice -> tone -> style -> format precedence and annotating the tension. B) Hard-block the composition.
**Recommendation.** **A (warn + precedence).** `avoid_with` means "discouraged", not "forbidden"; a user may want a deliberate tension. Blocking would break legitimate experimentation and is a worse default than an honest warning plus a precedence order so the output stays coherent.
**Source.** scaling matrix #9; backlog S1.
**Maintainer decision:** _pending_

## Group C - The adherence gate (E1)

### C1 - What the gate scores (P0)
**Context.** The gate could score only blind distinguishability, or also a taste/quality rubric.
**Options.** A) Distinguishability only. B) Distinguishability AND a pass/fail quality rubric.
**Recommendation.** **B.** Distinguishability is necessary but not sufficient: a generator optimized purely to pass attribution produces distinct-but-bad caricature. A second quality gate keeps prose good while it becomes distinct. This is the difference between "big" and "best-in-class".
**Source.** scaling matrix #1.
**Maintainer decision:** _pending_

### C2 - Judge policy (P0)
**Context.** The smoke test flagged "strong model on both ends" as its main caveat: an Opus-class judge scoring Opus-class output can collude.
**Options.** A) Same model family judges everything. B) A judge from a different model family, plus a 15 percent human spot-audit of clean passers (mandatory before any distillation).
**Recommendation.** **B.** Without an independent judge and periodic human audit, the gate slowly lies to itself (a real failure mode). The cross-family judge is the cheapest guard against judge monoculture.
**Source.** scaling matrix #2; gate spec.
**Maintainer decision:** _pending_

### C3 - Held-out reference set (P0)
**Context.** The proven human-authored 60 can be reused as few-shot exemplars, or frozen as untouched ground truth.
**Options.** A) Reuse the 60 freely as few-shot. B) Freeze the 60 (or a curated subset) as ground truth never used for training or few-shot.
**Recommendation.** **B (freeze).** The whole blend depends on uncontaminated ground truth to audit against; model collapse in generated content is invisible without it. Freezing the 60 costs nothing and is the regression backstop.
**Source.** scaling matrix #3; gate spec.
**Maintainer decision:** _pending_

### C4 - Gate thresholds (P1)
**Context.** The gate needs concrete numbers to be executable: the distinguishability band, the embedding de-dup threshold, and the first-pass-rate stop floor.
**Options.** A) Leave thresholds illustrative. B) Commit pilot numbers: forced-choice correct AND a "subtle"-or-better band; cosine ~0.92 for de-dup; 70 percent first-pass-rate stop floor.
**Recommendation.** **B, pilot-tuned.** Commit the numbers so the gate runs, then tune on the first batch. Treat a first-pass rate below the floor as a stop signal (the model cannot differentiate that territory), not a knob to loosen.
**Source.** spec #3; scaling matrix #5; gate spec.
**Maintainer decision:** _pending_

## Group D - Anchor topics

### D1 - The 12 topics + slate balance (P0)
**Context.** The proposal locks 12 anchor topics (3 existing + 9 new) distributed 4 professional / 2 public / 2 relational / 2 ceremonial / 2 contemplative.
**Options.** A) Accept 4/2/2/2/2. B) Drop professional to 3 to free a slot for a commercial (`outreach`/`copy`) home topic. C) A different distribution.
**Recommendation.** **A**, with the commercial-family gap noted (D3 / E-group). Professional is the deepest domain and warrants four; the `outreach`/`copy` families can be exercised on the public topics (5, 6) for now and revisited if they prove under-served.
**Source.** spec #2; anchor-topics open question 1.
**Maintainer decision:** _pending_

### D2 - `morning-routine` domain (P1)
**Context.** The existing `morning-routine` topic is assigned `relational`, though it has contemplative reach.
**Options.** A) Relational (a person designing their own daily life, addressable to a known reader). B) Contemplative (if its dominant frame is formation/discipline).
**Recommendation.** **A (relational).** Topics 11 and 12 carry the contemplative load natively; `morning-routine`'s dominant frame is personal-life design, not a discipline of formation.
**Source.** anchor-topics open question 2.
**Maintainer decision:** _pending_

### D3 - `accountability` family home (P2)
**Context.** The `accountability` family (public apology, security advisory) has no fully native topic; topic 3 (a hard internal cut) is its closest substrate but is professional.
**Options.** A) Test `accountability` on its boundary (topic 3). B) Mint a register-bearing native topic (e.g. `public-apology`).
**Recommendation.** **A (boundary).** A `public-apology` topic fails the isolation criterion the same way a eulogy does (it bakes in contrition), so testing on the boundary is the disciplined trade. Revisit only if the family proves badly served.
**Source.** anchor-topics open question 3.
**Maintainer decision:** _pending_

### D4 - The 9 new topic slugs (P1)
**Context.** The 9 new slugs (`roadmap-deprioritization`, `onboarding-a-new-hire`, `remote-work-policy`, `product-launch-announcement`, `thanking-a-mentor`, `retirement-send-off`, `team-milestone-celebration`, `daily-rest-practice`, `a-hard-year-in-review`) are first-draft names that will be written into the generator and route manifest.
**Options.** A) Accept as-is. B) Rename specific slugs now.
**Recommendation.** **A, but rename now if any jar** - slugs are cheap to change before they enter the generator and route manifest, expensive after. Lock them before v0.4.0 generation.
**Source.** anchor-topics open question 4.
**Maintainer decision:** _pending_

## Group E - Scope

### E1 - Scope boundaries (P1)
**Context.** The aspirational inventory scopes out fiction, poetry, legal/medical/scientific, working journalism, government, children's writing, and translation. "World's most comprehensive" may mean revisiting some.
**Options.** A) Hold the full out-of-scope list. B) Admit selectively at the register boundary, gate-arbitrated.
**Recommendation.** **B.** Admit journalism (news-brief, feature-lead) and plain-language legal/medical (`plain-english-legal-summary`, `patient-instructions`) only if they clear the gate and teach register, not domain knowledge. Hold fiction, poetry, translation, and children's writing - separate crafts the gate cannot judge. Any reopening is a maintainer ADR, never a mechanical add.
**Source.** spec #5; scaling matrix #6.
**Maintainer decision:** _pending_

### E2 - Journalism placement if admitted (P2)
**Context.** If journalism is admitted (E1), it can be a `public` subfamily or its own sixth domain.
**Options.** A) A `public` subfamily. B) A sixth domain.
**Recommendation.** **A (public subfamily).** Widening an existing domain is a lighter contract than adding a domain; journalism's public-record, external-convention character fits `public`. Promote to a domain only if it outgrows a subfamily.
**Source.** ADR 0010 open question 4.
**Maintainer decision:** _pending_

## Group F - Program and sequencing

### F1 - Breadth vs depth weighting (P1)
**Context.** "10x/100x" can be reached by more entries, more samples per entry, or both.
**Options.** A) Grow toward ~600 entries. B) Hold entries lower and let 12+ samples per entry carry the scale.
**Recommendation.** **Blend, depth-weighted.** Target ~600 entries (format concentrates breadth; voices/tones saturate faster), but the bulk of the multiple is sample depth (600 x 12 is already ~120x today's 195). Let the gate reject near-duplicate entries so breadth never inflates past distinguishability.
**Source.** scaling matrix #4.
**Maintainer decision:** _pending_

### F2 - Migration sequencing relative to E1 (P0)
**Context.** ADR 0010's tighten-to-required step and the E1 gate are interdependent: the gate renders against family neighbors, so families must be populated before the gate runs at volume, and fields should not be required before they are backfilled.
**Options.** A) Land taxonomy optional -> backfill the 60 -> stand up E1 -> tighten to required. B) Make fields required immediately.
**Recommendation.** **A.** Optional-with-warning first prevents a half-backfilled build from breaking; tighten to required only after all 60 carry valid values and the gate exists. This is the v0.3.0 phase order.
**Source.** ADR 0010 open question 5; spec sequencing.
**Maintainer decision:** _pending_

### F3 - Resourcing posture (P0)
**Context.** The scaling analysis was blunt: API tokens are a rounding error; human review hours are the binding constraint and do not parallelize cleanly (roughly 250-300 review hours per 1,000 entries).
**Options.** A) Solo evenings. B) 2-4 people for 18-24 months with a real budget. C) Consciously cap the target at 10x or 30x.
**Recommendation.** **B or C, never A.** Solo evenings at full scale is just 100x of the distinct-but-mediocre failure mode. Either fund the review capacity or pick a smaller target deliberately; keep the right to stop at 10x/30x if distinguishability stops scaling. This decision sets how far v0.4.0+ pushes and is worth making before the foundation work, not after.
**Source.** spec #6; scaling matrix #10.
**Maintainer decision:** _pending_

---

## What unblocks once these are decided

- **The P0 rows** (A1, A6, B1, C1, C2, C3, D1, F2, F3) gate moving ADR 0010 and ADR 0009 to Accepted and starting v0.3.0 execution. Most have a clear recommended default; the genuinely strategic one is **F3 (resourcing)**, which sizes the whole program.
- **The P1 rows** are needed during v0.3.0 execution but not before it starts.
- **The P2 rows** can be settled when v0.4.0 first touches the relevant family or scope.

Recording the calls here (replace each `_pending_`) turns this from a proposal into a committed plan; the release plan's Phase 0 references this document as its decision gate.

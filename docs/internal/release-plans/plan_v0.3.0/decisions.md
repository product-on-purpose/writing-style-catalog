# v0.3.0 / Expansion Decision Record

> The consolidated decision log for the expansion-foundation effort. It dedupes the open
> decisions raised across four sources: the scaling strategy's decision matrix
> ([`../../scaling-the-library-100x.md`](../../scaling-the-library-100x.md)), ADR
> [`0010`](../../adr/0010-domain-and-family-organization.md), the
> [`adherence-gate-spec.md`](adherence-gate-spec.md), and [`anchor-topics.md`](anchor-topics.md),
> plus [`spec.md`](spec.md) Section 6. Each decision has context, options, and a recommendation;
> the maintainer slot is where the call gets recorded. Until a P0 row is decided, v0.3.0 stays
> Proposed and execution does not begin.

**Status:** OPEN - 7 of 9 P0 rows decided 2026-06-09 (A6, B1, C1, C2, C3, F2, F3). The A1 (taxonomy cuts) external review has now LANDED: Fable returned a full evaluation on 2026-06-09 plus two addenda on 2026-06-10 (`_LOCAL/2026-06-09_a1-taxonomy-evaluation_by-fable.md`, Sections 10-13). Verdict: adopt the 5-domain / 16-family / 6-voice-family cut (do NOT re-cut), with specific repairs, distilled into a 12-item maintainer register (Q1-Q12). A1 is therefore no longer blocked on the review; it is blocked on the maintainer working the Q1-Q12 register, and Fable's own first-recommended step (Q12) is a gate pilot before ratifying. D1 (anchor topics) remains deferred pending A1 and example review. P1 and P2 rows still `_pending_`.
**Priority key:** P0 = blocks v0.3.0 execution; P1 = needed during v0.3.0; P2 = can defer past v0.3.0.

> **Referencing convention.** Always cite a decision as `ID - short title` (for example
> `A1 - taxonomy cuts`, `F3 - resourcing posture`), never the bare ID, so the context
> travels with the reference. The same applies to priority codes: spell them out as
> `P0 (execution-blocking)`, `P1 (needed during v0.3.0)`, `P2 (deferrable)` rather than the
> bare code.

---

## Summary table

| # | Decision | Recommendation | Priority | Maintainer call |
|---|---|---|---|---|
| A1 | Accept the v2 taxonomy cuts | Accept as-is | P0 | **Review landed (Fable, 2026-06-10): adopt with changes; ratification pending the Q12 gate pilot** |
| A2 | Subfamily 12-member trigger: hard vs soft | Hard cutoff | P1 | _pending_ |
| A3 | Subfamily naming pass | Defer to a gate-arbitrated follow-on | P2 | _pending_ |
| A4 | Facet-tag enum scope | Ship the 7, values widen on demand | P1 | _pending_ |
| A5 | Coverage target bands | Accept dense 12-20 / narrow 3-8 | P1 | _pending_ |
| A6 | Freeze the four axes | Freeze (ratify ADR 0010 sec. 1) | P0 | **Freeze (ratified)** (2026-06-09) |
| B1 | `avoid_with` symmetry | Symmetric (union both directions) | P0 | **Symmetric (union both directions)** (2026-06-09) |
| B2 | Conflict handling: warn vs block | Warn + precedence, never block | P1 | _pending_ |
| C1 | What the gate scores | Distinguishability AND a quality rubric | P0 | **Both; quality-measurement method TBD** (2026-06-09) |
| C2 | Judge policy | Cross-family judge + 15% human audit | P0 | **Cross-family judge (required); human audit capacity-bounded, distillation deferred** (2026-06-09) |
| C3 | Held-out reference set | Freeze the 60 as ground truth | P0 | **Freeze as held-out ground truth** (2026-06-09) |
| C4 | Gate thresholds | Commit pilot numbers, then tune | P1 | _pending_ |
| D1 | The 12 topics + slate balance | Accept 4/2/2/2/2 | P0 | **Deferred - revisit after A1; exploring expanded/randomized topics** (2026-06-09) |
| D2 | `morning-routine` domain | Relational | P1 | _pending_ |
| D3 | `accountability` family home | Test on the boundary (topic 3) | P2 | _pending_ |
| D4 | The 9 new topic slugs | Accept first-draft, rename now if any jar | P1 | _pending_ |
| E1 | Scope boundaries | Admit journalism + plain-language legal/medical, gate-arbitrated; hold fiction/poetry/translation/children's | P1 | _pending_ |
| E2 | Journalism placement | A `public` subfamily, not a 6th domain | P2 | _pending_ |
| F1 | Breadth vs depth weighting | ~600 entries, depth-weighted | P1 | _pending_ |
| F2 | Migration sequencing vs E1 | Taxonomy -> backfill -> gate -> tighten to required | P0 | **Accept (optional -> backfill -> gate -> required)** (2026-06-09) |
| F3 | Resourcing posture | Fund 2-4 people, or consciously cap | P0 | **Agentic-first; no funded headcount** (2026-06-09) |

---

## Group A - Taxonomy and structure (ADR 0010)

### A1 - Accept the v2 taxonomy cuts (P0)
**Context.** ADR 0010 codifies 5 domains (professional, public, relational, ceremonial, contemplative), 16 format families, and 6 voice families (expert, care, principal, witness, dissident, pastoral), with evocative family names. This supersedes a stale v1 (6 domains, 14 functional-sounding families). The taxonomy is load-bearing: the adherence gate's neighbor sets are defined by the tree, so loose categories make loose gates.
**Options.** A) Accept the v2 cuts and names as-is. B) Accept the cuts but rename specific families. C) Re-cut the domains/families. D) Drop the domain layer, families only. E) Stay flat, no taxonomy.
**Recommendation.** **A.** The v2 cuts were already iterated once against maintainer feedback and stress-tested against the ~195-format inventory; they are sound and naming is evocative rather than database-flat. Renames (B) are cheap to apply later if a name jars in use; do not block on them.
**Source.** spec #1; scaling matrix #7; ADR 0010.
**Maintainer decision:** **DEFERRED - out for independent external evaluation before commit.** Rather than accept on internal review alone, the maintainer is sending the taxonomy to a second model (Fable) for a deliberately non-leading best-fit evaluation, because this cut is load-bearing: it defines the adherence gate's neighbor sets, and a wrong cut propagates into every downstream admission decision and is expensive to reverse once entries are placed. The evaluation request is at `_LOCAL/2026-06-09_a1-taxonomy-evaluation_by-fable.md` (full situation, the proposed structure, the ~195-format / ~68-voice inventory, the constraints, and the alternatives, with the maintainer's own leaning withheld so as not to bias the reviewer). Option A (accept as-is) is the working hypothesis but is NOT committed; options B (rename families) and C (re-cut) stay live pending the review. Consequence: ADR 0010 stays Proposed, and everything that depends on the frozen taxonomy (Phase 1 schema codification, subfamily naming, the gate's neighbor lookup, F2's tighten-to-required step) waits on this. Rejected for now: committing on internal review alone, because the reversal cost after entries are placed is high and a second independent perspective is cheap insurance on the one structural decision the whole quality system renders against.

**Update (2026-06-16) - the review returned.** Fable delivered its evaluation (2026-06-09) plus two addenda (2026-06-10) in the same `_LOCAL` file, Sections 10-13. Headline verdict: **adopt the proposed 5-domain / 16-format-family / 6-voice-family structure with specific changes; do NOT re-cut** - every recorded alternative (drop-domains, single-level, tags-only, fifth-axis, the v1 cut) fails for its recorded reason, and the cut imposes zero gate cost because the gate operates at family/subfamily level. Fable found three *structural* (not cosmetic) defects to repair before ratifying: (1) the `relational` domain definition contradicts its own `essay` family, which breaks machine-tractable placement; (2) `broadcast`/`messaging` contain channel-clones that violate the catalog's own channel-as-facet design; (3) the tree-only neighbor function is blind to cross-family confusables that the live 60-entry graph already exhibits (roughly half of ~35 declared `confusable_with` edges cross the proposed family lines). It also corrected one internal inconsistency: ten of twenty-two groups (not two) bind the 12-member subfamily trigger at full build-out. The whole review reduces to a 12-item maintainer register (Q1-Q12) in Section 13, with Q1 (ratify) to be decided LAST. Consequence: A1 is no longer gated on the review; it is gated on working that register, and Fable's own first-recommended action is **Q12 - run a ~10 hard-pair near-neighbor gate pilot before ratifying**, because every remaining uncertainty (the 12-member threshold value, the borderline placements, whether the gate's bar is even achievable on near neighbors) is empirical, not analytical. That pilot is the next action; ADR 0010 stays Proposed and the F2 tighten-to-required step still waits until A1 ratifies on the pilot's evidence.

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
**Maintainer decision:** **DECIDED - Freeze.** Voice, Tone, Style, and Format remain the only top-level axes; every candidate fifth axis (rhetorical stance, epistemic stance, register/formality, medium/channel, persona-archetype, output modality) is demoted to a governed facet tag or a subfamily per ADR 0010 section 1. Rationale: none of the candidates passes the axis test (orthogonal to the others, exactly one value selected per instruction, independently changes the phrasing); each is cleaner as a cross-cutting facet. Under the agentic-first operating model (F3 - resourcing posture) this matters more, not less: every added axis multiplies the neighbor-pairs the automated gate must evaluate and the composer's combinatorial space, so holding at four keeps the gate tractable. Rejected: adding a fifth axis (option B), because it would force Tone and Style entries to declare an inapplicable value, multiply the combinatorial space, and break ADR 0001. The facet-tag namespace (A4 - facet-tag enum scope) is the pressure-release valve that makes the freeze sustainable. This ratifies ADR 0010 section 1, though ADR 0010 as a whole stays Proposed until A1 - taxonomy cuts resolves.

## Group B - Composition (S1)

### B1 - `avoid_with` symmetry (P0)
**Context.** Conflict-aware composition must decide whether `avoid_with` is symmetric: if A lists B in `avoid_with` but B does not list A, is the pair still flagged?
**Options.** A) Symmetric - flag if either entry lists the other (union both directions). B) Directional - flag only the listed direction.
**Recommendation.** **A (symmetric).** A conflict is a property of the pair, not of one entry's bookkeeping; asymmetry would make the warning depend on authoring order. Symmetric is deterministic and forgiving of incomplete cross-references. Validation can still warn on missing reciprocal links as a hygiene nudge.
**Source.** spec #4; scaling matrix #9.
**Maintainer decision:** **DECIDED - Symmetric (union both directions).** A pair is flagged if either entry lists the other in `avoid_with`. Rationale: a conflict is a property of the pair, not of one entry's bookkeeping; a directional rule would make the warning depend on which entry's author remembered to record the link, which is non-deterministic and brittle. This is more important under agentic-first authoring, not less: agent-generated entries will have incomplete cross-references (an entry authored late in a generation run will not reliably back-link to an early one), so a symmetric union is the only rule robust to that incompleteness. Composition stays deterministic regardless of which side recorded the conflict. Validation should additionally emit a hygiene WARNING on a missing reciprocal link, nudging the catalog toward complete cross-references without making correctness depend on them. Rejected: directional (option B), because the same pair would behave differently depending on which entry you start from, and it would silently miss real conflicts whenever the back-link was omitted.

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
**Maintainer decision:** **DECIDED - Both distinguishability AND a quality rubric (accepted emphatically).** The gate scores blind distinguishability against neighbors AND a separate pass/fail quality rubric. Rationale, sharpened by the agentic-first model (F3 - resourcing posture): distinguishability alone is gameable - a generator optimized purely to pass attribution learns that exaggeration is distinguishable and produces distinct-but-bad caricature. Under a funded human-review model, reviewers would catch that; the maintainer has consciously chosen NOT to fund that review team, so the quality rubric is the direct substitute for the reviewers who are not being hired. It is therefore not optional polish; it is the keystone that makes the whole agentic bet pay off. The rubric is applied by the cross-family judge (C2 - judge policy), so it costs judge tokens, not maintainer hours, which fits the operating model. Rejected: distinguishability only (option A), because it would let agentic generation drift to distinct-but-mediocre with nothing in the loop to catch it.
**Open sub-problem (gate-blocking, not Phase-1-blocking).** HOW to measure "quality" rigorously is unresolved. "Distinct" has a clean operationalization (blind forced-choice attribution plus a distinguishability band); "good" does not yet. Before the gate ships, this needs a concrete, judge-applicable quality rubric (named criteria, a scoring method, a pass threshold) that is neither circular nor gameable. Candidate directions to evaluate: a small set of explicit prose-quality criteria scored by the cross-family judge; calibration against the frozen reference set (C3 - held-out reference set); and a human spot-audit of the rubric's own verdicts during pilot. Rule: do not ship the gate on distinguishability alone while the rubric is undefined - treat "quality measurement undefined" as a release blocker for the GATE (Phase 5), not for Phase 1. Tracked as a Phase 5 design sub-item.

### C2 - Judge policy (P0)
**Context.** The smoke test flagged "strong model on both ends" as its main caveat: an Opus-class judge scoring Opus-class output can collude.
**Options.** A) Same model family judges everything. B) A judge from a different model family, plus a 15 percent human spot-audit of clean passers (mandatory before any distillation).
**Recommendation.** **B.** Without an independent judge and periodic human audit, the gate slowly lies to itself (a real failure mode). The cross-family judge is the cheapest guard against judge monoculture.
**Source.** scaling matrix #2; gate spec.
**Maintainer decision:** **DECIDED - cross-family judge, operated lean.** Two parts. (1) The judge MUST be from a different model family than the generator. This is non-negotiable and effectively free (point a different model at it); it is the core guard against judge/generator monoculture, the failure mode where a same-lineage judge co-adapts to the generator and stops noticing collapsing distinctions. (2) The human spot-audit is bounded to the maintainer's sustainable capacity, NOT the spec's flat "15 percent of all clean passers." Reasoning: that 15 percent is the binding human cost (roughly 250-300 review-hours per 1,000 entries) and there is no funded review team (F3 - resourcing posture). The gate spec ties the full 15-percent audit specifically to turning on distillation (training a generator on gate-passing output), which is a later, optional accelerator. So the operating rule is: run the gate automatically with the cross-family judge on everything; audit 100 percent of the two SMALL high-risk buckets (entries the judge rated `subtle`, and pairs the de-dup check flags as near-collisions); sample clean passers only as far as maintainer time allows; and DEFER distillation, and its mandatory full audit, until the maintainer chooses to invest that rigor. The automated stop-floor (C4 - gate thresholds: halt adding entries in a territory whose first-pass rate falls below ~70 percent) is the circuit-breaker that protects quality on the renders the maintainer does not personally read. Rejected: same-model-family judge (option A), because it colludes and the gate slowly lies to itself. Also explicitly NOT accepted: a standing unconditional 15-percent human audit, because it is unsustainable solo and would silently cap or stall the program; it is replaced by the capacity-bounded plus high-risk-bucket rule above. Coupled to F1 - breadth vs depth weighting: the sustainable audit capacity is what sizes the program, so F1 should be set with this operating rule in mind.

### C3 - Held-out reference set (P0)
**Context.** The 60 reviewed baseline entries (the v0.1.0 seed catalog: LLM-generated, maintainer-curated, frozen as `stable`, and the set the 8/8 distinguishability smoke test was run against) can be reused as few-shot exemplars for generation, or frozen as untouched ground truth the generator and judge never see. (Correction: earlier drafts called these "human-authored"; they are not - see the maintainer decision.)
**Options.** A) Reuse the 60 freely as few-shot. B) Freeze the 60 (or a curated subset) as ground truth never used for training or few-shot.
**Recommendation.** **B (freeze).** The whole blend depends on uncontaminated ground truth to audit against; model collapse in generated content is invisible without it. Freezing the 60 costs nothing and is the regression backstop.
**Source.** scaling matrix #3; gate spec.
**Maintainer decision:** **DECIDED - Freeze (accepted), with an authorship correction.** Freeze the 60 reviewed baseline entries (plus the 8 smoke-test pairs and their recorded ratings) as held-out ground truth that the generator and judge never see as training data or few-shot exemplars. They re-run every CI as a regression test: if a previously-distinguishable pair goes blurry after an edit, the build fails. Authorship correction (flagged by the maintainer): the 60 are NOT human-authored - they are LLM-generated and maintainer-reviewed. The reference's value comes from being UNCONTAMINATED by the generation/training loop, not from who wrote it, so the "human-authored" framing in earlier docs was both inaccurate and beside the point. It has been corrected here, in `scaling-the-library-100x.md`, and in `adherence-gate-spec.md`. Under agentic-first this freeze is the single cheapest insurance against model collapse (generated content silently homogenizing), which is invisible without a clean yardstick; the cost is zero because the entries already exist. Consequence: because the 60 are frozen as ground truth, they cannot ALSO serve as generation exemplars - a separate small exemplar set must be curated to seed generation (exemplar curation is one of the few high-leverage human acts in the pipeline). Rejected: reuse the 60 freely as few-shot (option A), because it contaminates the only clean reference and makes drift undetectable.

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
**Maintainer decision:** **DEFERRED - not accepting the fixed 4/2/2/2/2 slate yet.** Three reasons. (a) Topic balance is derived from the domain structure, which is itself under external review (A1 - taxonomy cuts); finalizing topics before the taxonomy is settled risks rework. (b) The maintainer wants to see more concrete worked examples before committing to which topics best exercise each family. (c) The maintainer wants to explore EXPANDING the topic set beyond 12, or introducing RANDOMNESS (a larger topic pool with randomized selection per gate run) rather than a small fixed slate. Open design tension to resolve when this reopens: the gate's regression mechanism (C3 - held-out reference set) depends on a FROZEN golden set rendered on FIXED topics - randomized or expanding topics improve coverage and reduce overfitting to a dozen prompts, but they complicate the frozen-regression guarantee. A likely reconciliation to evaluate (not yet decided): freeze a small fixed core for regression while drawing additional gate renders from a larger randomized pool for breadth. Revisit after A1 resolves and after reviewing more examples. Rejected for now: accepting the fixed 12 at 4/2/2/2/2 (option A), as premature while the taxonomy is unsettled and while expansion/randomness is still being explored; option B (drop professional to 3) is moot until the slate question reopens.

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
**Maintainer decision:** _pending_ (folded into D1 - the slugs are moot until the topic-set shape is decided)

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
**Maintainer decision:** _pending_ (now coupled to C2 - judge policy: under agentic-first, the maintainer's sustainable spot-audit capacity is the real throttle on scale, so set the F1 target with C2's operating rule in mind. This is the next decision to make.)

### F2 - Migration sequencing relative to E1 (P0)
**Context.** ADR 0010's tighten-to-required step and the E1 gate are interdependent: the gate renders against family neighbors, so families must be populated before the gate runs at volume, and fields should not be required before they are backfilled.
**Options.** A) Land taxonomy optional -> backfill the 60 -> stand up E1 -> tighten to required. B) Make fields required immediately.
**Recommendation.** **A.** Optional-with-warning first prevents a half-backfilled build from breaking; tighten to required only after all 60 carry valid values and the gate exists. This is the v0.3.0 phase order.
**Source.** ADR 0010 open question 5; spec sequencing.
**Maintainer decision:** **DECIDED - Accept the phased sequence.** Land the taxonomy fields optional-with-warning first, backfill the 60 baseline entries, stand up the E1 gate, then tighten fields to required. Rationale: the gate renders against family neighbors, so families must be populated before it runs at volume, and a field cannot be required before it is backfilled; optional-then-tighten prevents a half-migrated build from breaking and matches the repo's existing additive-then-enforce pattern. Under agentic-first it has a bonus: the gate can be built and validated on the trusted 60 before being pointed at scale. Rejected: making fields required immediately (option B), because it would break every not-yet-backfilled entry and force a big-bang migration with no safe intermediate state. Note: the "tighten to required" step is itself gated on A1 - taxonomy cuts (the taxonomy must be the committed one before fields become required) and on the backfill being complete, so Phase 1 can start now but its final tightening step waits on A1.

### F3 - Resourcing posture (P0)
**Context.** The scaling analysis was blunt: API tokens are a rounding error; human review hours are the binding constraint and do not parallelize cleanly (roughly 250-300 review hours per 1,000 entries).
**Options.** A) Solo evenings. B) 2-4 people for 18-24 months with a real budget. C) Consciously cap the target at 10x or 30x.
**Recommendation.** **B or C, never A.** Solo evenings at full scale is just 100x of the distinct-but-mediocre failure mode. Either fund the review capacity or pick a smaller target deliberately; keep the right to stop at 10x/30x if distinguishability stops scaling. This decision sets how far v0.4.0+ pushes and is worth making before the foundation work, not after.
**Source.** spec #6; scaling matrix #10.
**Maintainer decision:** **Agentic-first - no funded headcount.** Recorded 2026-06-09 (jprisant). This rejects A (solo by-hand grind) and B (fund 2-4 reviewers); it is a fourth posture the original A/B/C set did not frame. The binding constraint the context names (roughly 250-300 human review hours per 1,000 entries) is to be met by agentic processes - automated generation plus the cross-family adherence gate (E1) as the primary quality mechanism - with the maintainer giving only a light spot-audit, not a funded review team. Consequence: the gate (C1/C2/C3) and the depth-over-breadth discipline become load-bearing, because there is no human review capacity behind them; the bet only pays off if the gate is genuinely good. The numeric target and any conscious cap are set in F1, sized by how much spot-audit the maintainer can personally sustain, not by buying review hours.

---

## What unblocks, and what is still gated

- **7 of 9 P0 (execution-blocking) rows are decided:** A6 - freeze axes, B1 - avoid_with symmetry, C1 - what the gate scores, C2 - judge policy, C3 - held-out reference set, F2 - migration sequencing, F3 - resourcing posture. These ratify ADR 0010 section 1 (the axis freeze) and the gate's core design, and they let Phase 1 (schema codification on the optional-then-tighten path) begin.
- **2 P0 rows are still open, but A1's blocker changed.** A1 - taxonomy cuts: the external review has RETURNED (Fable, 2026-06-09/10) with an "adopt with changes; do not re-cut" verdict and a 12-item register (Q1-Q12). A1 is now blocked on the maintainer working that register, whose first step (Q12) is a near-neighbor gate pilot; until A1 ratifies, ADR 0010 stays Proposed and the tighten-to-required step (F2 phase 3) does not run. D1 - anchor topics is deferred pending A1 and example review, and pending a decision on whether to expand or randomize the topic set.
- **Two follow-on blockers surfaced while recording.** (i) C1 leaves the quality-MEASUREMENT method undefined - the gate must not ship on distinguishability alone until a concrete, judge-applicable quality rubric exists. (ii) C2 and F1 are coupled - the maintainer's sustainable audit capacity sizes the program, so F1 (a P1) should be set with C2's operating rule in mind; it is the next decision to make.
- **The P1 rows** are needed during v0.3.0 execution but not before it starts. **The P2 rows** can be settled when v0.4.0 first touches the relevant family or scope.

Recording the calls here (replacing each `_pending_`) turns this from a proposal into a committed plan; the release plan's Phase 0 references this document as its decision gate.

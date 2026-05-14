---
title: Writing Style Library Strategy Review and Recommendations
slug: writing-style-library-strategy-review-recommendations
date: 2026-05-10
status: draft-v1
authors: [chatgpt]
artifact_type: strategy-review
reviewed_documents:
  - strategy-approach-roadmap_2026-05-08.md
  - overbuilt-v1-execution-plan_2026-05-09.md
---

# Writing Style Library Strategy Review and Recommendations

## 1. Executive Summary

The strategy package is directionally strong and worth continuing. The controlling idea is clear: build a single-source-of-truth library of composable writing instructions using three primary axes: Voice and Tone, Style/Mode/Genre, and Format/Output Structure. That model is coherent because it decomposes the overloaded idea of writing “style” into parts that can be named, taught, composed, validated, and reused. (confidence: high)

The `strategy-approach-roadmap_2026-05-08.md` document should remain the plan of record. It has the right operating discipline: start with a walking skeleton, keep the catalog small, validate the schema, build the Skill Pack, prove the examples, and avoid committing to SDK, MCP, browser extension, and eval infrastructure before there is usage evidence. (confidence: high)

The `overbuilt-v1-execution-plan_2026-05-09.md` document is useful, but not as the actual execution plan. It is better understood as a maximal scope reference or full-catalog cost model. Its value is that it makes the full ambition visible: 80 voices, 50 tones, 60 styles, 100 formats, roughly 1,750 example files, six surfaces, hundreds of static pages, and a 12-month build. That is strategically useful because it prevents accidental underestimation. It is operationally dangerous if treated as the real v1 plan. (confidence: high)

The key recommendation is to explicitly split the documents into a hierarchy: the strategy roadmap is the plan of record, and the overbuilt plan is a north-star scope map. When they conflict, the roadmap wins. (confidence: high)

## 2. Recommended Document Hierarchy

### 2.1 Plan of record

Use the strategy roadmap as the controlling document. It should define the actual release sequence, decision gates, scope discipline, and build order. (confidence: high)

Recommended title:

`Writing Style Library: Strategy, Approach, and Roadmap`

Recommended role:

Plan of record for the project.

### 2.2 Maximal scope reference

Rename the overbuilt plan so it does not accidentally imply commitment. The current title, `Overbuilt v1 Execution Plan`, contains a useful warning word, but `v1` and `Execution Plan` still create commitment pressure. (confidence: high)

Better titles:

1. **Writing Style Library: Maximal Scope Reference**. Best option. It communicates scope without implying execution commitment. (confidence: high)
2. **Writing Style Library: Full-Catalog Cost Model**. Good if the main purpose is to expose labor and maintenance cost. (confidence: medium-high)
3. **Writing Style Library: North-Star Scope Map**. Good if the project wants an aspirational artifact. (confidence: medium)
4. **Writing Style Library: Overbuilt Scope Boundary**. Good if the primary purpose is to stop scope creep. (confidence: medium)

Recommended role:

A reference artifact used to understand what a complete mature system might include, not a binding release plan.

### 2.3 Decision record

Create a third short file that resolves the relationship between the two documents. (confidence: high)

Recommended file name:

`decision-record_2026-05-10_plan-of-record.md`

Recommended content:

```md
# Decision Record: Plan of Record for Writing Style Library

Date: 2026-05-10
Status: accepted

## Decision

The strategy roadmap is the plan of record. The overbuilt execution plan is retained as a maximal scope reference and cost model.

## Consequences

1. Phase 0 will not exceed 5 entries per axis.
2. Composer v1 will not include live model runs.
3. SDK, MCP, eval harness, and browser extension require explicit decision gates.
4. New taxonomy entries require a confusability review and admission rationale.
5. Examples are treated as the product, not supporting material.
6. The catalog will grow through usage evidence, not through completion pressure.
```

## 3. Strategic Assessment

### 3.1 What is strongest

The three-axis model is the strategic center of gravity. It works because it gives users a practical vocabulary for something they currently ask for imprecisely. A user who asks for “a professional post” gets generic prose. A user who asks for “executive voice, candid tone, comparison-contrast style, and PRD format” gives the model a far more controlled instruction. (confidence: high)

The project is not really a prompt library. It is closer to a structured writing instruction ontology with examples and generation surfaces. That distinction matters for positioning. Prompt libraries are easy to dismiss as collections of reusable snippets. This project is more defensible if it presents itself as a composable vocabulary, example corpus, and agent-callable instruction system. (confidence: high)

The examples-first instinct is correct. The catalog entries alone will not teach the system. Users need to see the difference between `operator` and `program-manager`, `warm` and `reassuring`, `ADR` and `RFC`, `tutorial` and `how-to`. Diff-pairs and vertical slices are not supplemental. They are the core teaching mechanism. (confidence: high)

The Skill Pack plus Composer pairing is the right initial product strategy. The Skill Pack serves agent workflows. The Composer serves human exploration and prompt assembly. Together, they cover both practical utility and learning. (confidence: high)

### 3.2 What is most fragile

The project is fragile because its hardest work is editorial, not technical. The repo can be scaffolded quickly. The schema can be validated. The Composer can be built. The difficult part is creating entries that are meaningfully distinct, useful, and not just plausible-sounding labels. (confidence: high)

The taxonomy can collapse under ambiguity if entry admission is weak. Many proposed entries sound distinct at list level but will blur when rendered in actual model outputs. Examples: `executive` vs `chief-of-staff`, `operator` vs `program-manager`, `warm` vs `empathic`, `reverent` vs `reverential`, `reflective-essay` vs `memoir-personal-essay`, and `technical-description` vs `technical-writing-style`. (confidence: medium-high)

The overbuilt plan creates scope gravity even though it warns against itself. Listing 80 voices, 50 tones, 60 styles, and 100 formats will make the project feel incomplete until those lists are filled. That is the opposite of the walking skeleton discipline. (confidence: high)

The six-surface ambition is too much for early v1. Skill Pack, Composer, static site, TypeScript SDK, Python SDK, MCP server, eval harness, and browser extension each have maintenance implications. Even if they share the same build artifact, each surface has documentation, support, versioning, validation, and usability burdens. (confidence: high)

## 4. Core Recommendation

Build the smallest complete system, not the largest impressive catalog. (confidence: high)

The smallest complete system includes:

1. A complete schema model.
2. A small set of high-quality entries per axis.
3. One strong anchor topic.
4. Vertical-slice examples across every starting entry.
5. A working `compose-instruction` skill.
6. Basic static docs.
7. CI validation for schema, slugs, cross-references, and examples.

That is enough to prove whether the project works. It is also enough to expose where the taxonomy is too vague, where entries overlap, and where the examples do not actually teach. (confidence: high)

## 5. Recommended Release Ladder

The current roadmap has phases, but the overbuilt plan makes the target feel like a large v1. A clearer release ladder would reduce scope confusion. (confidence: high)

| Release | Purpose | Catalog size | Surfaces | Release question |
|---|---:|---:|---|---|
| `v0.1` | Prove the skeleton | 5 entries per axis | Skill Pack, minimal docs | Can the model compose useful instructions? |
| `v0.2` | Prove human usability | 10 to 15 entries per axis | Composer alpha | Can another person use this without coaching? |
| `v0.5` | Prove repeat value | 20 to 30 entries per axis | Composer beta, recipes, diff-pairs | Which entries are genuinely useful? |
| `v0.8` | Stabilize the system | Pruned catalog | Static site, stronger validation | Is the schema stable enough for public use? |
| `v1.0` | Public stable release | Only validated entries | Skill Pack, Composer, docs, schema | Is this maintainable and useful? |

SDK, MCP, browser extension, and eval harness should not be assumed as v1 requirements. They should be gated by observed use. (confidence: high)

## 6. Scope Control Rules

### 6.1 Rule 1: No new axis before v1

Do not add Audience, Length, Channel, Register, Persona, Brand, or Medium as full axes before v1. Treat them as constraints or metadata. (confidence: high)

Suggested constraint fields:

```yaml
audience:
  primary: senior_engineers
  familiarity: high
  sensitivity: medium
length:
  target: concise
channel:
  name: slack
context:
  use_case: internal_team_update
```

### 6.2 Rule 2: Every new entry needs an admission rationale

A new entry should not be accepted because it is recognizable. It should be accepted because it changes output in a useful, teachable, and repeatable way. (confidence: high)

Suggested required field:

```yaml
entry_admission_reason: >
  This entry deserves to exist because it produces a distinct instruction effect not covered by existing entries.
```

### 6.3 Rule 3: Every new entry needs confusables

Every entry should identify nearby entries and explain the distinction. (confidence: high)

Suggested field:

```yaml
confusable_with:
  - id: operator
    distinction: >
      Program-manager focuses on sequencing, dependencies, cadence, and coordination. Operator focuses on execution pressure, accountability, and practical next action.
```

### 6.4 Rule 4: No entry graduates without examples

An entry should not be marked stable until it has at least one reviewed example and one anti-example. (confidence: high)

Suggested lifecycle:

1. `proposed`: concept exists.
2. `draft`: entry is written but not validated through examples.
3. `candidate`: at least one generated example exists.
4. `reviewed`: human review completed.
5. `stable`: example and anti-example both validate the distinction.
6. `deprecated`: replaced or collapsed into another entry.

### 6.5 Rule 5: Every surface must justify its maintenance cost

A new surface should be added only when it serves a distinct job that current surfaces cannot serve. (confidence: high)

Decision test:

1. Does this surface serve a distinct user?
2. Does it unlock use that Skill Pack plus Composer cannot unlock?
3. Can it read the same build artifact without custom content drift?
4. Can it be maintained alone for 12 months?
5. Does usage evidence justify it?

## 7. Taxonomy Critique and Suggestions

### 7.1 Voice axis

The voice axis is the most valuable and the most dangerous. It is valuable because voice is what most users struggle to name. It is dangerous because voice categories can become stereotypes, caricatures, or vague vibes. (confidence: high)

#### Keep in early core

These voices are likely to be useful, stable, and less prone to caricature:

1. `executive`
2. `senior-consultant`
3. `industry-analyst`
4. `pragmatic-architect`
5. `operator`
6. `program-manager`
7. `principal-engineer`
8. `friendly-mentor`
9. `patient-teacher`
10. `socratic-tutor`
11. `academic`
12. `public-intellectual`
13. `explainer-journalist`
14. `columnist`
15. `pastor`
16. `theologian`
17. `chaplain`
18. `marketer`
19. `salesperson`
20. `essayist`

#### Defer until stronger guardrails exist

These may be valuable later but are risky in early public form:

1. `valley-girl`
2. `bro-dudespeak`
3. `surfer-socal`
4. `southern-folksy`
5. `aussie-larrikin`
6. `gen-z`
7. `boomer`
8. `mad-genius-inventor`
9. `trickster-provocateur`

The issue is not that these are unusable. The issue is that they require anti-caricature guidance, respectful boundaries, and examples that show rhetorical function rather than stereotype. (confidence: high)

#### Suggested voice entry template

```yaml
id: pragmatic-architect
axis: voice
status: draft
summary: Tradeoff-oriented, systems-aware, calmly opinionated.
entry_admission_reason: >
  Useful for technical and product decisions where the output needs judgment, constraints, and implementation realism.
not_a:
  - Generic senior engineer voice
  - Purely technical writing style
  - Blunt tone
confusable_with:
  - id: principal-engineer
    distinction: >
      Principal-engineer centers technical depth and engineering judgment. Pragmatic-architect centers system tradeoffs, constraints, and cross-functional decision design.
language_patterns:
  - Names tradeoffs explicitly
  - Uses constraint-first framing
  - Distinguishes reversible from irreversible decisions
  - Prefers practical sequencing over idealized architecture
  - Flags operational consequences
anti_patterns:
  - Over-indexing on abstract architecture
  - Sounding dismissive of implementation detail
  - Turning every answer into a framework
```

### 7.2 Tone axis

Tone is useful but should be pruned aggressively. Many tone entries are near-synonyms unless they are located on a clear spectrum. (confidence: high)

Recommended change: make tone entries explicitly axis-bound. (confidence: medium-high)

Example tone families:

1. **Confidence**: tentative, humble, confident, authoritative.
2. **Warmth**: cold, cool, neutral, warm, affectionate.
3. **Energy**: subdued, calm, measured, energetic, urgent.
4. **Formality**: casual, conversational, formal, stiff.
5. **Rhetorical posture**: conciliatory, diplomatic, candid, blunt, provocative.
6. **Emotional register**: hopeful, somber, mournful, joyful, defiant.

Recommended pruning questions:

1. Does `reverent` differ from `reverential` in output?
2. Does `supportive` differ from `encouraging` in output?
3. Does `cool` differ from `aloof` in output?
4. Does `confident` differ from `assertive` in output?
5. Does `direct` differ from `candid` in output?

If the difference is not visible in examples, collapse the entries. (confidence: high)

### 7.3 Style, Mode, and Genre axis

The style axis is conceptually correct but internally broad. It combines rhetorical modes, exposition techniques, documentation approaches, fiction genres, nonfiction genres, professional writing approaches, and religious writing modes. (confidence: high)

Recommended documentation structure:

1. **Rhetorical modes**: narration, description, argument, exposition.
2. **Expository moves**: definition, classification, comparison, cause and effect, process, problem-solution.
3. **Documentation modes**: tutorial, how-to, reference, explanation.
4. **Genre modes**: memoir, journalism, fiction, theology, cultural criticism.
5. **Professional modes**: technical, business, strategic, operational, marketing.

This prevents “style” from becoming a junk drawer. (confidence: high)

Suggested rule: no style entry should be admitted unless it names the reader contract. (confidence: high)

Example:

```yaml
reader_contract: >
  The reader expects to understand the cause of a problem, the mechanism that produced it, and the consequences that followed.
```

### 7.4 Format axis

The format axis is the easiest to validate and the most immediately useful. Formats should probably be the strongest early catalog category because they can include canonical templates and structural rules. (confidence: high)

Recommended early format set:

1. `adr`
2. `prd`
3. `rfc`
4. `design-doc`
5. `tech-spec`
6. `slack-message`
7. `email-longform`
8. `blog-post-long-form`
9. `devotional-entry`
10. `sermon-outline`
11. `lesson-plan`
12. `checklist`
13. `decision-register-entry`
14. `runbook`
15. `quick-reference-card`

Formats are good early candidates because users can recognize whether the output looks structurally correct. (confidence: high)

## 8. Example Strategy

### 8.1 Treat examples as the product

The project should be evaluated by whether examples teach the differences between entries. If the example set is weak, the catalog is weak regardless of schema quality. (confidence: high)

### 8.2 Use three example types

#### Vertical slices

A vertical slice holds the topic constant and varies one axis. This is the best way to teach distinction. (confidence: high)

Example:

Topic: “How should a team protect focused work while staying connected?”

Render across:

1. `executive`
2. `operator`
3. `friendly-mentor`
4. `pastor`
5. `academic`

#### Horizontal slices

A horizontal slice combines one voice, one tone, one style, and one format into a named recipe. This is the best way to serve users who do not want to compose from primitives. (confidence: high)

Example:

`architect-adr = pragmatic-architect + measured + problem-solution + adr`

#### Diff-pairs

A diff-pair holds most variables constant and changes one thing. This is the best teaching format for confusable entries. (confidence: high)

Example:

`operator` vs `program-manager`, same topic, same format, same tone.

### 8.3 Improve the first anchor topic

The current first anchor topic, “Should we adopt async-first standups?”, is useful but somewhat narrow. It strongly favors product and engineering contexts. (confidence: medium-high)

A more flexible first anchor topic:

**“How should a team protect focused work while staying connected?”**

Why this is better:

1. It still supports async standups.
2. It works for PM, engineering, leadership, and workplace writing.
3. It has a human dimension.
4. It stretches pastoral and reflective voices without feeling absurd.
5. It creates room for operational, strategic, and cultural framing.

Recommended anchor sequence:

1. `focused-work-and-connection`: broad professional and human topic.
2. `morning-routine`: personal and accessible topic.
3. `discipline-of-rest`: spiritual and reflective topic.
4. `db-choice`: technical stress test.
5. `farewell-colleague`: emotional and pastoral stress test.

## 9. Surface Strategy

### 9.1 Skill Pack

The Skill Pack is the most important first surface because it proves the catalog can operate inside real agent workflows. (confidence: high)

Start with only:

1. `compose-instruction`
2. `find-compatible`
3. `suggest-recipe`
4. `explain-entry`

Defer:

1. `apply-voice`
2. `convert-format`
3. `evaluate-against-entry`
4. 50 callable recipe commands

Reason: the first release should validate composition, not become a full writing transformation suite. (confidence: high)

### 9.2 Composer

Composer v1 should be intentionally small. The overbuilt Composer is a good future product concept, but it is too large for initial release. (confidence: high)

Composer v1 should include:

1. Axis pickers.
2. Topic input.
3. Optional audience/context input.
4. Live composed instruction.
5. Copy to clipboard.
6. “Why this combination works” explanation.
7. Example preview where available.

Defer:

1. BYO-key live model runs.
2. Side-by-side comparison.
3. Save and share via URL state.
4. Personal library.
5. Export to JSON.
6. Paste-your-text auditor.
7. Brand voice builder.
8. Voice fingerprint flow.

Reason: the first Composer should teach composition and produce reusable instructions. It should not become a prompt runner or writing workspace. (confidence: high)

### 9.3 Static site

The static site should not become the main product too early. It should be a generated reference surface for entries, examples, and recipes. (confidence: medium-high)

Useful early pages:

1. Home.
2. Three-axis model.
3. Quick start.
4. Entry reference.
5. Examples gallery.
6. Diff-pairs gallery.
7. Contribution guide.

Defer:

1. Full design system.
2. Large editorial docs.
3. SEO-driven content strategy.
4. Public eval reports.

### 9.4 SDK

The TypeScript SDK is plausible earlier than the Python SDK because the Composer likely needs TypeScript utilities anyway. (confidence: medium-high)

Recommended threshold before publishing to npm:

1. Catalog schema is stable for at least two releases.
2. At least one internal consumer exists.
3. The build artifact format is stable.
4. `composeInstruction()` has a real consumer outside tests.

The Python SDK should wait until someone asks for it or MCP use reveals demand for non-TypeScript consumers. (confidence: medium)

### 9.5 MCP server

The MCP server is strategically attractive but should not precede proof that the catalog itself is useful. (confidence: high)

Recommended threshold:

1. At least 20 stable entries per axis.
2. At least 10 validated recipes.
3. At least 3 non-maintainer users.
4. Clear evidence that agent workflows need remote catalog access.
5. A stable build artifact.

### 9.6 Eval harness

The eval harness should be split into structural checks and subjective quality checks. (confidence: high)

Structural checks can happen early:

1. Does the output include required sections?
2. Does it follow the format template?
3. Does it avoid banned patterns?
4. Does it include required metadata?

Subjective checks should be treated as advisory:

1. Does this read as pastoral?
2. Does this feel executive?
3. Does this sound too generic?
4. Does this voice collapse into another voice?

LLM-as-judge is useful for triage but not enough for stable quality claims. (confidence: high)

## 10. Product Positioning

### 10.1 Avoid “prompt library” positioning

Do not position this as a generic prompt library. That category is crowded and low-trust. (confidence: high)

Better positioning:

**A composable writing instruction system for humans and agents.**

Alternate positioning options:

1. **A structured vocabulary for controlling AI-generated writing.**
2. **An open catalog of reusable writing instructions, examples, and recipes.**
3. **A writing style library for composing voice, tone, genre, and format into reliable AI instructions.**
4. **A skill-pack-first taxonomy for better AI writing outputs.**

### 10.2 The strongest differentiation

The project’s strongest differentiator is not the number of entries. It is the combination of:

1. Orthogonal axes.
2. Examples and diff-pairs.
3. Schema validation.
4. Agent-callable Skill Pack.
5. Composer UI.
6. Compatibility graph through `pairs_well_with`.

The compatibility graph may become the hidden moat. If users can pick one entry and get good compatible combinations, the catalog becomes more than a glossary. (confidence: high)

### 10.3 Target users

Primary early users:

1. Product managers.
2. Technical writers.
3. Engineers writing design docs.
4. PMs creating product artifacts.
5. Pastors and ministry writers, given the existing user context.
6. AI tool builders who want reusable instruction primitives.

Secondary later users:

1. Marketers.
2. Educators.
3. Fiction writers.
4. Brand teams.
5. Prompt engineers.
6. Developer tool builders.

The early catalog should over-serve the primary users rather than pretending to serve every writing domain equally. (confidence: high)

## 11. Governance Recommendations

### 11.1 Entry admission rubric

Every proposed entry should answer these questions:

1. What axis does this belong to?
2. What output behavior changes when this entry is used?
3. What existing entry is closest?
4. Why not merge it with that existing entry?
5. What is the canonical example?
6. What is the anti-example?
7. What contexts should avoid this entry?
8. Does this entry risk caricature, stereotyping, or misuse?
9. What validation rules can be automated?
10. What must remain human-reviewed?

### 11.2 Promotion criteria

Recommended lifecycle:

| Status | Meaning | Required evidence |
|---|---|---|
| `proposed` | Idea captured | Short description |
| `draft` | Entry written | Frontmatter complete |
| `candidate` | Example generated | At least one example |
| `reviewed` | Human reviewed | Example plus anti-example |
| `stable` | Publicly reliable | Confusables resolved |
| `deprecated` | Retired or merged | Replacement path |

### 11.3 Deprecation policy

Entries should be deprecated when:

1. They are indistinguishable from another entry in examples.
2. They create more confusion than value.
3. They rely on stereotypes or brittle cultural assumptions.
4. They are too narrow to justify ongoing maintenance.
5. They belong better as a recipe, tag, constraint, or example.

## 12. Technical Architecture Recommendations

### 12.1 Single build artifact

All surfaces should read from one generated catalog artifact. This is the right architectural decision. (confidence: high)

Recommended artifact:

`dist/catalog.json`

Recommended sections:

```json
{
  "version": "0.1.0",
  "generated_at": "2026-05-10T00:00:00Z",
  "voices": [],
  "tones": [],
  "styles": [],
  "formats": [],
  "recipes": [],
  "examples": [],
  "compatibility_graph": {}
}
```

### 12.2 Validation pipeline

The validation plan is strong. Keep it. (confidence: high)

Core checks:

1. Schema validation.
2. Slug validation.
3. Cross-reference resolution.
4. Reciprocal compatibility warnings.
5. Deprecated entry resolution.
6. Controlled vocabulary validation.
7. Markdown linting.
8. Link checking.
9. No-em-dash linting if that remains a house rule.
10. Example metadata validation.

### 12.3 Avoid false precision

Avoid numeric scores for subjective qualities unless they are truly used in computation. (confidence: medium-high)

Prefer categorical fields:

```yaml
humor_profile: none | light | moderate | high
formality: casual | conversational | formal | ceremonial
energy: subdued | calm | measured | energetic | urgent
```

This is easier to review and less likely to imply nonexistent precision. (confidence: medium-high)

## 13. Revised Phase 0 Plan

### 13.1 Goal

Prove the taxonomy, schema, examples, and Skill Pack work as a complete loop. (confidence: high)

### 13.2 Scope

Phase 0 should include:

1. Repo scaffold.
2. JSON Schemas.
3. 5 entries per axis.
4. One anchor topic.
5. 20 vertical-slice examples.
6. One Skill Pack with `compose-instruction`.
7. Minimal generated docs.
8. CI validation.
9. One decision record.
10. One contribution guide stub.

Phase 0 should exclude:

1. Composer beyond a static prototype.
2. SDK.
3. MCP.
4. Eval harness.
5. Browser extension.
6. Full recipe library.
7. Full static site IA.
8. Brand voice builder.
9. Personal library.
10. Hosted model runs.

### 13.3 Recommended first 5 per axis

#### Voices

1. `pragmatic-architect`
2. `operator`
3. `friendly-mentor`
4. `pastor`
5. `explainer-journalist`

#### Tones

1. `measured`
2. `warm`
3. `candid`
4. `reverent`
5. `encouraging`

#### Styles

1. `problem-solution`
2. `comparison-contrast`
3. `diataxis-explanation`
4. `process-explanation`
5. `reflective-essay`

#### Formats

1. `adr`
2. `prd`
3. `slack-message`
4. `blog-post-long-form`
5. `devotional-entry`

This set creates meaningful range without becoming arbitrary. It includes professional, educational, spiritual, and explanatory use cases. (confidence: medium-high)

## 14. Composer v1 Product Definition

### 14.1 User story

As a user, I want to choose a voice, tone, style, and format, add a topic and audience context, and receive a clear reusable instruction I can paste into an LLM. (confidence: high)

### 14.2 Must-have features

1. Choose voice.
2. Choose tone.
3. Choose style.
4. Choose format.
5. Add topic.
6. Add audience or context.
7. Preview composed instruction.
8. Copy instruction.
9. See why the combination works.
10. View a matching example if available.

### 14.3 Nice-to-have features

1. Random good combination.
2. Recipe picker.
3. Diff-pair explorer.
4. Search and filter.
5. Export to Markdown.

### 14.4 Defer

1. Live model calls.
2. API key management.
3. Personal account.
4. LocalStorage library.
5. Prompt history.
6. Browser extension.
7. Text auditor.
8. Brand voice builder.
9. Voice fingerprint flow.

### 14.5 Product warning

Composer will fail if it feels like a form. It needs to feel like a guided composition tool. The most important interaction is not picking values. It is understanding why the selected values work together. (confidence: high)

## 15. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---:|---:|---|
| Catalog sprawl | High | High | Entry admission rubric and phase caps |
| Six-surface maintenance fatigue | High | High | Gate SDK, MCP, eval, browser extension |
| Examples feel generic | Medium-high | High | Human review and diff-pairs |
| Voice entries become caricatures | Medium | High | Defer cultural voices, add anti-patterns |
| Composer becomes too large | High | Medium-high | Define strict v1 feature cap |
| Static site becomes the product | Medium | Medium | Prioritize Skill Pack and Composer |
| Eval harness overclaims quality | Medium | Medium-high | Separate structural and subjective evals |
| Schema churn breaks surfaces | Medium | High | Delay SDK and MCP until schema stabilizes |
| No external adoption | Medium | Medium | Dogfood first, then invite 3 to 5 users |
| Repo positioning looks generic | Medium | Medium | Avoid prompt-library framing |

## 16. Recommended Redline Edits

### 16.1 In the overbuilt plan

Replace:

`v1 target`

With:

`full-catalog target`

Replace:

`Surfaces shipped: 6`

With:

`Candidate mature surfaces: 6`

Replace:

`Timeline target: 12 months`

With:

`12-month maximal build scenario`

Add near the top:

> This document is not the plan of record. It is a maximal scope reference used to understand the cost, architecture, and maintenance burden of a full catalog build.

Move the 80 voice list, 50 tone list, 60 style list, and 100 format list into appendices. Keep only the recommended early subset in the main body. (confidence: medium-high)

### 16.2 In the strategy roadmap

Add a “Document hierarchy” section. (confidence: high)

Add a “Release ladder” section. (confidence: high)

Add a “New entry admission rubric” section. (confidence: high)

Add explicit success metrics for each phase. (confidence: high)

Add a stricter Composer v1 feature definition. (confidence: high)

Add a short note that Phase 2 surfaces are decision-gated, not pre-committed. (confidence: high)

## 17. Success Metrics

### 17.1 Phase 0 metrics

1. Maintainer uses the Skill Pack at least 10 times for real work.
2. At least 20 examples exist and pass metadata validation.
3. At least 3 entries are revised because examples exposed ambiguity.
4. CI catches at least one real issue before merge.
5. One outside reviewer understands the three-axis model without explanation.

### 17.2 Phase 1 metrics

1. 3 to 5 users compose a useful instruction without coaching.
2. At least 5 recipes are used more than once.
3. At least 5 confusability issues are found and resolved.
4. Composer copy-to-clipboard flow is used repeatedly.
5. The examples gallery is more useful than the raw catalog list.

### 17.3 Phase 2 metrics

1. At least one user asks for programmatic access.
2. Catalog schema remains stable across several releases.
3. At least 20 entries per axis have reviewed examples.
4. Diff-pairs become a primary learning surface.
5. SDK or MCP work has a named consumer.

## 18. Strongest Strategic Insight

The library should not optimize for catalog completeness. It should optimize for **instructional leverage**. (confidence: high)

An entry has leverage when it helps users:

1. Name a writing behavior.
2. See what that behavior looks like.
3. Compose it with other behaviors.
4. Avoid confusing it with nearby behaviors.
5. Generate a more reliable LLM instruction.

That means a 40-entry library with excellent examples, confusables, and recipes can be more valuable than a 290-entry library with shallow definitions. (confidence: high)

## 19. Recommended Immediate Next Actions

1. Create `decision-record_2026-05-10_plan-of-record.md`. (confidence: high)
2. Rename the overbuilt document to `maximal-scope-reference`. (confidence: high)
3. Add document hierarchy language to both documents. (confidence: high)
4. Define `v0.1` as 5 entries per axis and one anchor topic. (confidence: high)
5. Create the entry admission rubric before adding more entries. (confidence: high)
6. Build the first 20 examples before building Composer. (confidence: high)
7. Cut Composer v1 down to instruction composition and copy-to-clipboard. (confidence: high)
8. Defer SDK, MCP, eval, and browser extension until usage evidence exists. (confidence: high)
9. Create a confusability matrix for the first 20 entries. (confidence: high)
10. Dogfood the Skill Pack before polishing the public site. (confidence: high)

## 20. Source List

1. `strategy-approach-roadmap_2026-05-08.md`. Uploaded strategy brief for the Writing Style Library.
2. `overbuilt-v1-execution-plan_2026-05-09.md`. Uploaded maximal execution plan for the Writing Style Library.

## 21. Unsure or Not Verified

1. I do not know the actual available weekly time budget for this project. (confidence: high)
2. I do not know whether the intended end state is open-source utility, public portfolio project, sponsorship-supported tool, or commercial SaaS. (confidence: high)
3. I did not verify external claims about agentskills.io, Claude Code plugin behavior, MCP adoption, or marketplace mechanics against live web sources in this document. (confidence: high)
4. I did not review the companion `value-delivery-approaches_2026-05-09.md` document because it was not included in the uploaded files visible for this review. (confidence: high)
5. I do not know whether `pm-skills` should remain a sibling repo, dependency, or downstream consumer. My recommendation assumes sibling repo with shared conventions. (confidence: medium-high)

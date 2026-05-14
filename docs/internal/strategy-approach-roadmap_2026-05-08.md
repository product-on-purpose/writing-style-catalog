---
title: Writing Style Library - Strategy, Approach, and Roadmap
slug: strategy-approach-roadmap
date: 2026-05-08
status: draft-v1
authors: [jonathan]
artifact_type: strategy-brief
source_inputs:
  - _LOCAL/opus-4.7_three-axis-writing-taxonomy_2026-04-30.md
  - _LOCAL/opus-4.7_taxonomy-model_2026-04-30.md
  - _LOCAL/opus-4.7_taxonomy-frontmatter-schema_2026-04-30.md
  - _LOCAL/opus-4.7_operationalize-taxonomy-model_2026-04-30.md
  - _LOCAL/opus-4.7_taxonomy-repo-architecture_2026-04-30.md
  - _LOCAL/taxonomy-model_gemini-pro_2026-04-30.md
  - _LOCAL/taxonomy-model_gpt-5.5_2026-04-30.md
  - _LOCAL/chatgpt_2026-05-08_writing_instruction_taxonomy_three_axes.md
  - _LOCAL/chatgpt_2026-05-08_writing_instruction_resource_library.md
  - _LOCAL/claude_2026-05-08_best-in-class-skill-repo-blueprint.md
  - _LOCAL/ai-chats/Claude - Writing taxonomy for LLM content generation_2026-04-30_11-11-25.md
  - _LOCAL/ai-chats/ChatGPT - Writing Taxonomy for LLMs_2026-05-08_16-34-45.md
license: CC-BY-4.0
---

# Writing Style Library: Strategy, Approach, and Roadmap

## TL;DR (read this even if you skip everything else)

**Build a single-source-of-truth catalog of composable writing instructions, organized along three orthogonal axes (Voice & Tone, Style/Mode/Genre, Format/Output Structure), packaged as an agentskills.io-compliant Claude Code plugin, and rendered through a small set of progressively richer surfaces (Composer web app, Skill Pack, SDK, MCP server).**

The 80/20 path: ship a Phase-0 walking skeleton in 2-3 weekends - 5 entries per axis, one anchor topic, the atomic-skill folder pattern, JSON-Schema-validated frontmatter, a working `compose-instruction` skill, and a minimalist static site. Resist the four traps that kill projects like this: clinical-browser-without-tool, axis sprawl, hosted-API cost exposure, and trying to maintain six surfaces alone. Treat examples (especially diff-pairs) as the product, not as appendices. Treat the `pairs_well_with` graph as the hidden value.

What follows is the long version: how I read the source material, why this work matters, what could go wrong, the four paths considered, the recommended path, a phased roadmap with named deliverables and decision points, and the open questions that still need a human call.

---

## 1. What I Understand (input mirror)

The `_LOCAL/` directory holds 13 source documents authored across 2026-04-30 and 2026-05-08, produced by three frontier LLMs (Claude Opus 4.7, GPT-5.5 Thinking, Gemini Pro) plus two raw chat transcripts. They converge on a single product idea, with productive disagreement at the edges.

**The convergent core (all three models agree):**

- A **three-axis taxonomy** is the right primitive for instructing LLMs on writing. The axes are independent: Voice & Tone (who is speaking and how they feel), Style/Mode/Genre (what kind of writing this is), and Format/Output Structure (the container). Composing one value from each yields a precise instruction.
- "Style" alone is too overloaded to be a top-level axis. People use it to mean tone, voice, genre, structure, brand standards, or visual formatting all at once. The taxonomy must decompose it.
- Audience is a constraint dimension, not a fourth full axis - at least at v1.
- Examples are the product. Catalogs that bury examples behind clicks lose users; catalogs that ship paired examples teach the taxonomy itself.
- The atomic-skill folder pattern (each entry = its own directory with `ENTRY.md` + frontmatter + examples) beats both flat files and a YAML monolith for anything ambitious.
- Validation is non-negotiable. JSON Schema for frontmatter, cross-reference checks for `pairs_well_with` IDs, no-em-dash linting, all wired into CI.

**The productive disagreements:**

- Whether Voice and Tone collapse into one axis (GPT-5.5's view) or live as a paired-but-distinct axis (Opus 4.7's view). Opus is more right; the persistent-versus-situational distinction matters.
- Whether the entry count for v1 should be 5, 10, or 15 per axis. This is a roadmap question, not a strategy question.
- Whether to ship as a peer plugin inside an existing repo (`pm-skills`-adjacent) or as a standalone repo (`writing-style-library`, which is what already exists here). The repo name signals the answer.
- The right phasing of operational surfaces. There are six candidate surfaces (Composer, Skill Pack, SDK, MCP, browser extension, eval harness) and clear opinions about which two come first, but no consensus on Phases 2 and 3.
- Whether the eval harness is a Phase 2 rigor layer or a Phase 3 community-flywheel piece. Both views are defensible.

**What is NOT in the source material (and that I am inferring):**

- A clear sense of the user's time budget. The Opus operationalization doc assumes "indie scope" but does not name an hour count.
- A concrete commercial intent. Most discussion treats this as a craft project. The roadmap below assumes free-and-open with optional sponsorship, but a paid SaaS variant is technically possible.
- The relationship between this repo and `pm-skills`. They are clearly siblings under `product-on-purpose`. I assume separate repos with shared house style, not a merge.

If any of those inferences is wrong, the recommendation in Section 5 shifts; I flag specifically where.

---

## 2. Problem Space

### 2.1 The underlying problem

LLM-generated writing is uneven because instructions are uneven. A user types "write a professional blog post" and gets generic LLM-prose; another types "write a PRD in a pragmatic-architect voice with a candid tone, structured as Problem/Goals/Non-Goals/Risks, for senior engineers" and gets something usable. The gap between those two prompts is not skill at typing - it is access to a vocabulary that names the moves a writer can make. Most people do not have that vocabulary.

The three-axis taxonomy is a vocabulary. The library is the place that vocabulary lives, with examples that show what each named value actually produces, and tooling that lets people compose the values into ready-to-use instructions without memorizing the catalog.

### 2.2 Why it matters now

Three trends converge in 2026:

1. **Skills as the dominant agent extension primitive.** agentskills.io plus Claude Code 2.1.x have collapsed slash-commands and skills into a single shape. Anyone building agent-callable utilities has a clear, portable target. A taxonomy shipped as a skill pack lands inside the workflows of every Claude Code, Codex, Cursor, and Cline user.
2. **MCP adoption.** Model Context Protocol gives a single integration surface to Claude.ai, ChatGPT (where supported), and most coding agents. A catalog exposed as an MCP server is reachable from agents that do not yet exist.
3. **Style guides are the wrong primitive for AI workflows.** Style guides (Mailchimp, Microsoft, GOV.UK, IBM Carbon) are excellent prose-prescriptive documents for human writers and brands. They are weak as composable LLM controls because they fuse voice, tone, structure, and rules. The market gap is real: GPT-5.5's research scan in `chatgpt_2026-05-08_writing_instruction_resource_library.md` confirms that no mature open-source library cleanly catalogs voice/tone, genre/approach, and format as separate reusable controls.

### 2.3 Who is affected

Three jobs-to-be-done, three audiences:

- **The composer.** A PM, engineer, designer, pastor, marketer, or writer who needs to produce something specific right now. They want speed and good defaults. The Composer surface and the `compose-instruction` skill serve them.
- **The learner.** Someone wanting to understand the craft, see voices side by side, build intuition. Diff-pairs and the static site serve them.
- **The agent.** An LLM in a workflow needs a deterministic instruction string assembled from named parts. The catalog as build-artifact JSON, the Skill Pack, the SDK, and the MCP server serve them.

Any surface that serves only one of these jobs has to be exceptional at it. Surfaces that serve at least two compound their value.

### 2.4 What "solved" looks like

A future state where:

- A teammate at any product-on-purpose-adjacent project can drop into a Claude Code session and write `Use the writing-style-library:compose-instruction skill to draft a pastoral devotional on the discipline of rest` and get a usable artifact in one turn.
- A first-time visitor to the public site lands on a Composer page, picks three values from clearly-labeled grids, copies a prompt, runs it in their own LLM client, and feels they learned something about writing in the process.
- A developer can `npm install @product-on-purpose/writing-style-library` and call `composeInstruction({voice, tone, style, format})` with full TypeScript autocomplete on valid IDs.
- An evaluator can re-run the eval harness when a new model drops and publish a "how does Sonnet 4.7 handle pastoral voice on grief topics" page that drives traffic and credibility.
- The catalog reaches ~50 entries per axis, with vertical slices on three anchor topics and horizontal slices on the 20 most-used combinations, all generated and reviewed under a documented process.

### 2.5 Adjacent problems out of scope (for now)

- A model-eval product like Promptfoo (we will use it, not build it).
- A general-purpose prompt manager (we constrain to writing).
- A brand voice consultant or generator (we ship vocabulary, not bespoke house-style services).
- An LLM router or generation infrastructure (the skill pack runs in whatever client the user already has).

---

## 3. Analysis

### 3.1 Strengths

- **Pre-existing alignment with agentskills.io and Claude Code patterns.** The user already runs `pm-skills`, has authored multiple plugins, and understands the SKILL.md/atomic-folder pattern. This is the cheapest possible architectural starting point.
- **Three-axis taxonomy is internally consistent and externally novel.** The decomposition is sharper than every public style guide surveyed, sharper than every existing prompt library, and lines up with both the classical rhetoric tradition (Newman 1827) and modern UX practice (NN/g, Diataxis). It teaches well.
- **The repo already exists and the working name is good.** `writing-style-library` under `product-on-purpose` is a credible URL and signals the scope without overpromising.
- **Examples-as-product is a discipline already proven elsewhere.** GOV.UK Design System and Atlassian Design System work because the patterns ship with concrete renderings. The vertical-slice/horizontal-slice/diff-pair structure formalizes that discipline.
- **The frontmatter schema is already designed.** `opus-4.7_taxonomy-frontmatter-schema_2026-04-30.md` is a near-shippable v1. JSON Schema validation is a one-day chore, not a research problem.

### 3.2 Weaknesses

- **The catalog is a content problem, not a code problem.** The repo can be scaffolded in two days; populating 50 entries per axis with quality examples is a months-long writing job. The roadmap must respect this.
- **Voice/tone characterization is subjective.** "Pastoral" means different things across denominations and contexts. "Pragmatic architect" reads as charming or cold depending on the reader. Without a way to signal intent and mean it, the catalog loses to the variance of human taste.
- **Six surfaces is too many for one maintainer.** Even with the Composer + Skill Pack as the two priority surfaces, the SDK, MCP server, browser extension, and eval harness all have non-trivial maintenance burdens.
- **Evaluating writing quality is genuinely hard.** LLM-as-judge works for structure adherence (was it an ADR? did it have the four sections?) but is shaky for voice fidelity (does this read pastoral or just polite?). Phase-3 eval claims need human review to be credible.

### 3.3 Risks

- **The clinical-browser trap.** Building a beautiful read-only catalog browser, never building the Composer or the Skill Pack. The repo becomes documentation people respect and never use.
- **Axis sprawl.** Tempting to add Audience, Length, Register, Channel as full axes. Each addition multiplies the combination space and dilutes the teaching power of the original three. Resist for at least 12 months of real use.
- **Hosted-run cost exposure.** Any "run this prompt" button using the maintainer's API key is a cost-leak risk if traffic spikes. Bring-your-own-key from day one is the safe default.
- **Maintainability decay.** Six surfaces is too many for solo maintenance. The browser extension and the eval harness are the most likely to drift; the SDK and Composer must always work.
- **The personality risk.** Catalogs without editorial taste lose to catalogs with taste, even when the taste-led one is objectively narrower. This is not a polish risk; it is a positioning risk. Every surface needs a point of view.
- **Confusion with adjacent offerings.** "AI prompt library" sites are a saturated category. The differentiation has to be loudly opinionated structure (three orthogonal axes) and composable infrastructure (skill, SDK, MCP), not "browse 500 prompts."

### 3.4 Open questions

- Where this fits relative to `pm-skills`. Sibling repo with cross-references, or absorbed as a peer skill family inside the existing plugin? My read: sibling. (See Section 8.)
- Whether to register the catalog as a public agentskills.io entry in the marketplace or keep it private to `product-on-purpose` for the first six months.
- Which license to put on content (CC-BY-4.0 favored), versus code (Apache-2.0), and whether LLM-generated examples create a license gray area.
- Whether the eval harness is Phase 2 (rigor layer) or Phase 3 (community flywheel). Both views in the source material are defensible.

### 3.5 Concerns

- **Time budget realism.** The Phase 0 weekend MVP is plausible. Phase 1 ("usable in your own daily writing workflow") implies sustained part-time effort over a month. Phase 2 ("infrastructure for other tools") is a quarter. None of these are calendar-light.
- **Quality of LLM-generated examples.** Seeding examples by prompting Claude Opus 4.7 will scale faster than human-authoring. The risk: the catalog teaches the model's voice back to itself, with no human ground truth. Mitigation: every example marked `author_type: llm` requires `author_type: hybrid` review before promoting to `review_status: reference-quality`.

### 3.6 Situational lenses

Three additional lenses worth applying:

**Pre-mortem lens.** If this project fails 18 months from now, the three most likely causes are: (1) catalog too small to be useful, (2) maintenance fatigue across surfaces, (3) lack of distribution / nobody knows it exists. The roadmap addresses 1 and 2 directly; 3 is a marketing problem the technical roadmap cannot solve alone.

**Distribution lens.** This category of tool succeeds through the agentskills.io marketplace, the Claude Code plugin registry, the npm/PyPI long tail, and word-of-mouth from the `product-on-purpose` audience. The roadmap should produce installable artifacts (skill, SDK package, MCP server) before producing a marketing site. Discoverability inside the toolchain beats a beautiful homepage.

**Compound interest lens.** The catalog grows in value with examples, not entries. One entry with 20 vertical-slice examples is more valuable than 20 entries with one example each. This argues for narrow, deep, opinionated v1 over broad, shallow, balanced v1.

---

## 4. Approaches

Four genuinely distinct paths exist. They are not intensity variants of each other. Pick one; the others are wrong for this repo.

### 4.1 Approach A: Catalog-First (a beautifully structured reference site)

**Summary:** Treat this as a publishing project. The deliverable is a content site (MkDocs Material), with the catalog as content. The Skill Pack and SDK are deferred indefinitely. Examples are LLM-generated, lightly curated.

**Detailed breakdown:** Spend the first three months populating ~50 entries per axis, each with prose entries and 2-3 examples. Build the static site with cross-reference indexes derived from frontmatter. Promote on Hacker News, the agentskills.io discussion forums, and Twitter. Consider a printed reference card at scale.

**Pros:** Lowest tooling complexity. Highest content density. Best for SEO. Best fit for someone who likes writing more than coding.

**Cons:** Falls into the clinical-browser trap by design. Does not serve the agent job-to-be-done well. Hard to differentiate from existing style guides at the surface level. Creates content debt with no operational payoff.

**Key risks:** The site looks great and gets used by nobody, because nobody can compose with it. Six months of writing produces a respected reference and zero workflow integrations.

**Effort/complexity:** Medium-low engineering, very high content. Solo-maintainable.

**Honest commentary:** This is the wrong path for someone whose adjacent work is `pm-skills`. The user already knows how to ship plugins; leveraging that knowledge by building a Composer and a Skill Pack is a much bigger leverage move. Approach A is the path the project ends up on if energy fades and nothing more ambitious gets started.

### 4.2 Approach B: Skill-First (Claude Code plugin as primary surface)

**Summary:** The catalog ships first and only as a Claude Code plugin. Entries live in the plugin's resources directory. The plugin exposes `compose-instruction`, `apply-voice`, `convert-format`, and a small set of named recipes. There is no public web site; the README in the GitHub repo is the only human surface.

**Detailed breakdown:** Build the plugin to agentskills.io spec. Register on the marketplace. Use it in your own workflow. Iterate on entry quality based on what the user actually invokes. Write a `pm-skills`-style decision log of what works and what doesn't. After 6 months, decide whether to add a Composer based on observed demand from non-Claude-Code users.

**Pros:** Fastest path to "useful in my own work." Highest leverage per hour. Defensible scoping ("we do one thing well"). Distribution is solved by the marketplace, not by traffic.

**Cons:** Excludes anyone who is not already a Claude Code user. Loses the learner job-to-be-done entirely. No path to community contribution beyond GitHub PRs. Hard to demonstrate value to people who do not already speak fluent skills.

**Key risks:** The catalog ends up shaped by a single user's needs. Without the discipline of a public surface, examples skew toward the maintainer's domains (PM, ministry) and stay narrow. Adoption stalls below 100 installs because the Claude Code skills market is still small in absolute terms.

**Effort/complexity:** Medium engineering, medium content. Solo-maintainable.

**Honest commentary:** This is the most sensible single-surface path. It is also where I would land if Approach D (the recommended one) felt like too much. The downside is forgone leverage; the catalog will eventually want a public face, and starting with a skill-only repo means rebuilding the public layer later.

### 4.3 Approach C: Big-Tent (full operationalization across all six surfaces)

**Summary:** Build the Composer, Skill Pack, SDK, MCP server, browser extension, and eval harness in parallel as first-class surfaces from the start. Hire help if needed. Commit to a 12-month runway.

**Detailed breakdown:** Hire a part-time frontend engineer for the Composer. Build the SDK and MCP server in the same monorepo. Outsource the browser extension to a contractor. Build the eval harness on top of Promptfoo. Aim for 200 entries, 5 anchor topics, 50 horizontal-slice combinations within the first year.

**Pros:** If it works, the catalog becomes infrastructure. Network effects across surfaces. Defensible category leadership.

**Cons:** Requires capital or full-time commitment. Overwhelmingly likely to spread thin. Six surfaces means six ongoing maintenance loads. The SDK and Composer need updates every time the catalog schema changes. The eval harness needs human-grading infrastructure to be credible.

**Key risks:** Maintenance fatigue at month 6. Two surfaces drift to "stale but works." Composer becomes the de facto product and the rest are dead weight. Worst case: nothing is maintained well, and the project's reputation suffers across all surfaces.

**Effort/complexity:** Very high engineering, very high content, very high coordination. Not solo-sustainable.

**Honest commentary:** This is the path investors would push for. It is the wrong path for an indie maintainer. The good news: Approach D's roadmap can graduate into Approach C if traction warrants it, without rework. Do not start here.

### 4.4 Approach D: Walking Skeleton (recommended)

**Summary:** Ship the Composer and Skill Pack together as Phase 1, with the catalog deliberately small (5 entries per axis, one anchor topic) and the schema deliberately complete. The Composer is a static SPA reading a build-artifact JSON. The Skill Pack reads the same content directly. Both surfaces stay in sync because they read the same source. Defer SDK, MCP server, browser extension, and eval harness to later phases gated on real usage signals.

**Detailed breakdown:**

Phase 0 (2-3 weekends): repo skeleton, schemas, 5 entries per axis on one anchor topic, vertical slice across all entries, Skill Pack with `compose-instruction`, static site that renders the catalog read-only.

Phase 1 (1 month part-time): Composer SPA with three axis pickers, live preview, copy-to-clipboard, smart defaults from `pairs_well_with`. 15 entries per axis. Second anchor topic. Five horizontal-slice recipes. A "diff-pair" of the week.

Phase 2 (1 quarter): TypeScript SDK, Python SDK, MCP server. Side-by-side compare in the Composer. Bring-your-own-key live runs. 30 entries per axis. Eval harness using Promptfoo, with public "how does each model handle voice X" results. Decision gate: do we keep growing or freeze the catalog at this size?

Phase 3 (long horizon): Browser extension or bookmarklet, community contribution flow, third anchor topic, full-axis catalog at ~50 entries, formal governance.

**Pros:** Two surfaces serve all three jobs-to-be-done from Phase 1. Layered architecture means new surfaces add cost-linearly, not exponentially. Solo-maintainable if scoped to two primary surfaces. Each phase has a real-world utility milestone, not just a feature milestone. Compound interest on the catalog matters more than surface count.

**Cons:** Two surfaces is still more than one. Phase 2 makes a real call on whether SDK + MCP are worth the engineering cost. The Composer needs design polish to feel like a craft tool rather than a form.

**Key risks:** Phase 0 takes 5 weekends instead of 2 because polish is hard. The Composer's smart-defaults logic is harder than it looks. The Skill Pack's recipe library tempts scope creep.

**Effort/complexity:** Medium engineering, growing content. Solo-maintainable through Phase 2 if disciplined.

**Honest commentary:** This is the right path. It maps to your actual capacity, your actual existing skills, the actual market gap, and the actual phasing logic in the source documents. It also has a graceful failure mode: if energy fades after Phase 1, the result is a usable Skill Pack and a working Composer with 15 entries per axis on two anchor topics, which is already more than most adjacent projects ship.

---

## 5. The 80/20 Recommendation

Take Approach D (Walking Skeleton). Specifically, the highest-leverage actions, in priority order:

**1. Ship Phase 0 in two to three weekends.** The deliverables are non-negotiable: repo skeleton, JSON Schema for all four axis types, 5 entries per axis (curated, not exhaustive), one anchor topic with vertical slices across all 20 entries, a working `compose-instruction` skill in a Claude Code plugin, a static site that renders entries from frontmatter, and CI that validates schema and cross-references. This is the walking skeleton. If you cannot finish Phase 0, the rest of the roadmap is academic.

**2. Use the Skill Pack in your own daily workflow for two weeks before designing the Composer.** This is the most important behavioral decision in the whole plan. The Composer's smart-defaults, the recipe library, and the priority of Phase-2 surfaces all benefit from real usage data. Resist the temptation to build the public surface first.

**3. Make examples the product.** Every entry ships with at least one vertical-slice example. Every horizontal-slice combination ships with at least three topic instantiations. Every Phase 2 release adds at least three diff-pairs. The catalog's value is the examples, not the entries. Treat this as the central content discipline.

**4. Defer the SDK, MCP server, browser extension, and eval harness until Phase 2 or later.** Each of these has a real use case. None of them earn their maintenance cost in Phase 0 or Phase 1. Phase 2 reassesses with real usage data.

**5. Adopt the existing frontmatter schema as v1, with two changes.** The schema in `opus-4.7_taxonomy-frontmatter-schema_2026-04-30.md` is near-shippable. Two judgment calls override it: (a) drop per-entry semver until evidence shows entries are consumed independently of repo releases - repo-level semver is enough; (b) treat `nn_g_profile` as discrete categorical (`funny | neutral | serious`) rather than numeric to avoid false-precision.

**Confidence:** High on Approach D as the right strategic shape. Medium-high on the Phase 0 timeline (it always takes longer than expected). Medium on Phase 2 surface decisions (real usage data should drive them).

**Confidence on what to defer:** High that Approach C (big tent) is the wrong starting point. High that the eval harness belongs in Phase 2 or later, not Phase 1. Medium on the browser extension - it might never earn its keep.

The recommendation does not depend on whether this stays free, becomes sponsorship-funded, or migrates to a SaaS layer later. The catalog and primary surfaces are valuable in any of those configurations. Defer pricing decisions until usage data exists.

---

## 6. Roadmap

### 6.1 Phase 0: Walking Skeleton (target: ship by 2026-05-25, two to three weekends)

**Deliverables:**

- Repo scaffold: `taxonomy/`, `examples/`, `schemas/`, `skills/`, `docs/`, `.github/workflows/`, `mkdocs.yml`. Mirrors `opus-4.7_taxonomy-repo-architecture_2026-04-30.md` Section 7.
- `.claude-plugin/plugin.json` declaring the plugin shape.
- `schemas/voice.schema.json`, `tone.schema.json`, `style.schema.json`, `format.schema.json`, `example.schema.json`, derived from `opus-4.7_taxonomy-frontmatter-schema_2026-04-30.md` with the two amendments noted in Section 5.
- 5 stable entries per axis, hand-authored, drawing from the catalogs in the source docs. Initial picks (subject to revision):
  - **Voices:** pragmatic-architect, friendly-mentor, pastoral, columnist, operator
  - **Tones:** matter-of-fact, warm, candid, reverent, encouraging
  - **Styles:** problem-solution, diataxis-explanation, devotional-reflection, comparison-contrast, classical-argument
  - **Formats:** adr, prd, devotional-entry, blog-post-long-form, slack-message
- One anchor topic - **"Should we adopt async-first standups?"** - rendered as a vertical slice across all 20 entries. This produces 20 example files that double as the catalog's first proof-of-concept.
- A working `compose-instruction` skill that takes axis IDs and returns a composed prompt.
- CI workflow that runs schema validation, cross-reference checks, and the no-em-dash linter.
- A minimal MkDocs Material site that lists entries, with auto-generated indexes from frontmatter.
- README.md, CONTRIBUTING.md, LICENSE (Apache-2.0 for code, CC-BY-4.0 for content), AGENTS.md.

**Decision gate at the end of Phase 0:** Use the Skill Pack in your own writing for two weeks. Log what you actually invoke and what feels missing. The Phase 1 priorities re-derive from that log.

### 6.2 Phase 1: Skill Pack v1 + Composer v1 (target: 2026-06-30, ~one month part-time)

**Deliverables:**

- Composer SPA at `composer.product-on-purpose.com` (or a similar domain): three axis pickers, topic input, audience input, live preview of the composed instruction, copy-to-clipboard. Stack: Vite + React + TypeScript + Tailwind, deployed to Cloudflare Pages.
- Smart defaults driven by `pairs_well_with`: picking pragmatic-architect highlights matter-of-fact and candid in the tone picker, ADR and RFC in the format picker.
- "Try a random good combination" button.
- Catalog grows to 15 entries per axis (45 new entries vs Phase 0).
- Second anchor topic added: **"How to start a morning routine"** - 60 vertical slices added.
- Five horizontal-slice recipes shipped under `examples/horizontal-slices/`:
  - `architect-matter-of-fact-adr` (3 topics)
  - `pastoral-warm-devotional` (3 topics)
  - `columnist-candid-blog-post` (3 topics)
  - `friendly-mentor-encouraging-tutorial` (3 topics)
  - `operator-direct-runbook` (3 topics)
- Skill Pack adds named recipes that can be invoked by name (e.g., `/writing-style-library:architect-adr`).
- A "diff-pair of the week" published to the site - one tone-swap, one voice-swap, one format-swap minimum.

**Decision gate at the end of Phase 1:** Did the Composer get used? Did the Skill Pack get installed? Open Phase 2 only if yes. If no, pause and audit positioning before building more surfaces.

### 6.3 Phase 2: SDK + MCP + Eval (target: 2026-09-30, one quarter)

**Deliverables:**

- TypeScript SDK published as `@product-on-purpose/writing-style-library` on npm. Exports `composeInstruction()`, `getEntry()`, `findCompatible()`, with TypeScript types generated from the JSON Schemas.
- Python SDK published as `product-on-purpose-writing-style-library` on PyPI with parity API.
- MCP server hosted on Cloudflare Workers (or Fly.io) exposing `list_voices`, `get_entry`, `compose_instruction`, `find_examples`, `suggest_combinations` tools. Listed in the public MCP server directories.
- Composer adds: side-by-side comparison view, bring-your-own-API-key live runs (Anthropic, OpenAI, Google), citations on generated outputs ("Composed from voice:pragmatic-architect, tone:matter-of-fact, format:adr").
- Catalog grows to 30 entries per axis.
- Third anchor topic considered (likely **"The discipline of rest"**) but not committed to.
- Eval harness using Promptfoo: per-entry rubrics derived from `language_patterns` and `markers`, run against three or four major models, results published.

**Decision gate at the end of Phase 2:** Has the catalog reached natural saturation? Some axes (formats especially) may converge around 20-30 entries; voice may want to keep growing. Decide whether Phase 3 expands the catalog or expands the surfaces.

### 6.4 Phase 3: Community + Polish (long horizon, gated on Phase 2 results)

**Deliverables (subject to Phase-2 decision):**

- Browser extension or bookmarklet for in-context invocation in Gmail, Slack, Notion, Google Docs.
- Public contribution flow with frontmatter validation, automated review dispatch, a contributor recognition surface.
- Catalog reaches ~50 entries per axis on three anchor topics.
- Formal governance documented (`GOVERNANCE.md`, `CODEOWNERS`, deprecation policy).
- Optional sponsorship or donation model if traffic warrants - this is the first phase where commercial questions become real.

**This phase has no fixed end date.** It is an operating mode, not a milestone.

### 6.5 Concrete next-three-actions checklist

1. Create the Phase 0 repo scaffold and commit the schemas. Two evenings of work.
2. Author the first 20 entries (5 per axis), prioritizing voices and formats over tones and styles - the schema for those is denser and tests the model better.
3. Render the async-standups anchor topic across all 20 entries, save the prompts and the model used, and commit example files with the example-file frontmatter shape.

After those three are done, the rest of Phase 0 is mechanical: stand up CI, polish the README, register the plugin locally, dogfood for a week, then publish.

### 6.6 What to explicitly defer

- Per-entry semver versioning (use repo-level semver until evidence demands more).
- The browser extension (Phase 3 at earliest).
- Hosted-API-run mode without rate limits (always BYO-key, always).
- A fourth axis for Audience (constraint metadata only through at least Phase 2).
- A community-contribution review queue (Phase 3 at earliest).
- Marketing site polish before the catalog is real (do not optimize a homepage that has nothing to point to).

---

## 7. Evidence & Source Map

Every claim in this document traces back to one or more of the 13 source documents in `_LOCAL/`, supplemented by the 2026-05-08 best-in-class repo blueprint and external references the source documents cite. Notable provenance:

- **Three-axis taxonomy structure.** Origin in `opus-4.7_three-axis-writing-taxonomy_2026-04-30.md`; corroborated by `taxonomy-model_gemini-pro_2026-04-30.md` and `chatgpt_2026-05-08_writing_instruction_taxonomy_three_axes.md`. All three models converged independently. Confidence: high.
- **Atomic-skill folder pattern.** Origin in `opus-4.7_taxonomy-repo-architecture_2026-04-30.md` Section 2 (Option B). Aligns with agentskills.io spec referenced in `claude_2026-05-08_best-in-class-skill-repo-blueprint.md`. Confidence: high.
- **Six-surface operationalization with Composer + Skill Pack as priority.** Origin in `opus-4.7_operationalize-taxonomy-model_2026-04-30.md` Sections 2 and 5. Phasing recommendation cross-checked against the indie-scope realism in the same document's Section 6. Confidence: medium-high; phasing assumes solo maintenance.
- **Frontmatter schema v1.** Origin in `opus-4.7_taxonomy-frontmatter-schema_2026-04-30.md`. Two amendments in Section 5 above are mine, not the source's. Confidence: high on the schema; medium on the amendments (worth re-checking with usage data).
- **Public-style-guide gap analysis.** Origin in `chatgpt_2026-05-08_writing_instruction_resource_library.md` Tier 1-5 scan and "Gaps in the public ecosystem" section. Confidence: high - the survey is thorough and the conclusion (no clean open-source taxonomy exists) is consistent with my own search.
- **agentskills.io / Claude Code plugin compliance details.** Origin in `claude_2026-05-08_best-in-class-skill-repo-blueprint.md`. This is a synthesis of the public agentskills.io spec and the Claude Code plugins reference. Confidence: high.
- **Risk catalog (clinical browser, axis sprawl, hosted-API exposure, maintenance fatigue, personality risk, confusion).** Origin in `opus-4.7_operationalize-taxonomy-model_2026-04-30.md` Section 6. Confidence: high.

**Evidence gaps and where I extrapolated:**

- The user's specific time budget. I assumed indie-pace solo maintenance with weekend-and-evening capacity. If the actual budget is larger or smaller, Phases 0 and 1 timelines shift.
- The relationship to `pm-skills`. Source material does not commit to "sibling repo" or "absorbed peer plugin." I recommended sibling based on the existing `writing-style-library` repo name, but the user could override.
- Phase 2 and Phase 3 specifics. The source material is consistent on Phase 0 and Phase 1; later phases are described as "natural sequence" without firm dates. I assigned target dates that match the indie-pace assumption; treat them as direction, not commitments.
- Pricing posture. Source material declines to recommend; I deferred the question to Phase 3.

This brief itself is reasoning from the source material, not new research. Where I take a position not directly stated in the sources (the two amendments to the frontmatter schema, the explicit recommendation against per-entry semver in Phase 0, the three-action concrete checklist in Section 6.5), I am making a judgment call rather than citing.

---

## 8. Uncertainties & Open Items

This section captures decisions and open questions surfaced by the strategy work. Each item gets a summary row and a full subsection below with:

- **Description** - what the question or decision is
- **Desired outcome context** - what a "right answer" looks like and why
- **Approach options** - the realistic paths
- **Recommendation** - my pick, with reasoning and confidence
- **Your feedback** - reserved space for the user to weigh in or override

The categories are: decisions to make before Phase 0 starts (8.1), decisions to defer until real-usage data exists (8.2), uncertainties I cannot resolve from desk analysis (8.3), out-of-scope topics this brief does not answer (8.4), and follow-up artifacts to produce (8.5).

### 8.1 Items requiring human decision before Phase 0 starts

| # | Decision | Recommendation | Confidence |
|---|---|---|---|
| 8.1.1 | License posture for LLM-generated content | Apache-2.0 for code, CC-BY-4.0 for content, with model + prompt attribution on LLM examples | Medium-high |
| 8.1.2 | Repo relationship to `pm-skills` | Sibling repo under `product-on-purpose`, cross-linked but independent | Medium |
| 8.1.3 | Phase 0 anchor topic | "Should we adopt async-first standups?" | Medium |

#### 8.1.1 License posture for LLM-generated content

**Description.** The repo will contain three kinds of artifact: code (validators, build scripts, the SDK once shipped), structured content (entry frontmatter, schemas, prose `ENTRY.md` bodies), and LLM-generated example texts. Standard practice dual-licenses code and content. LLM-generated examples create a gray area: is the prompt the licensable work, the output the licensable work, both, or neither?

**Desired outcome context.** A clear, single-paragraph license policy in `LICENSE` and `NOTICE` that contributors and downstream users can read once and follow forever. Should be permissive enough that the catalog gets adopted, restrictive enough that attribution is preserved. Should be stated before any LLM-generated content lands in the repo, because retroactive license changes are painful.

**Approach options.**

- **Option A.** Apache-2.0 across the board. Simplest. Treats prose entries and example texts as software artifacts.
- **Option B.** Apache-2.0 for code, CC-BY-4.0 for all content. Treats LLM-generated examples as content. Each example file's frontmatter records `author_type`, `llm_model`, and `llm_prompt_file` so the lineage is auditable.
- **Option C.** Dual-license everything CC-BY-4.0. Simplest from the user's perspective. Loses Apache-2.0's patent-grant clause for code.
- **Option D.** Apache-2.0 for code + CC0 (public domain) for examples. Maximally permissive for examples; loses attribution requirement, which weakens the auditability story.

**Recommendation.** Option B. Apache-2.0 mirrors `pm-skills` and is the right choice for the validators and the SDK. CC-BY-4.0 on content matches the agentskills.io ecosystem norms (the docs there are CC-BY-4.0) and preserves the attribution hook that makes the audit trail meaningful. Treat LLM-generated examples as CC-BY-4.0 with attribution to the model name and prompt file path, captured in the example's frontmatter. State the policy in `LICENSE` and `NOTICE` and link to it from `CONTRIBUTING.md`. Confidence: medium-high.

**Your feedback.**
> _[reserved for user input]_

---

#### 8.1.2 Repo relationship to `pm-skills`

**Description.** `writing-style-library` could live as a sibling repo under `product-on-purpose`, as an absorbed peer plugin inside `pm-skills`, or as a private fork that publishes a subset. Each choice changes discoverability, cross-installation, and maintenance shape.

**Desired outcome context.** The repo's URL and identity should signal the scope. Users should be able to install one or both without confusion. Cross-references should work in both directions (a `pm-skills` user finds this; a `writing-style-library` user finds `pm-skills`) without forcing a merge.

**Approach options.**

- **Option A.** Sibling repo. `product-on-purpose/writing-style-library` as its own marketplace plugin, cross-linked from `pm-skills` README and vice versa.
- **Option B.** Absorbed peer plugin. `pm-skills/plugins/writing-style/` directory, shipped as a peer plugin in the same marketplace catalog.
- **Option C.** Private incubator. Build it under a private repo for 3-6 months, then split off cleanly when stable.

**Recommendation.** Option A (sibling repo). The existing `writing-style-library` repo name strongly suggests this is the user's intent already. A sibling structure preserves focus (the writing taxonomy is a distinct domain from PM workflows), keeps versioning independent, and matches how the agentskills.io ecosystem expects plugins to be discoverable. Cross-references via `pm-skills` README and via `marketplace.json` `keywords` field cover the discovery cost. The downside (a second repo to maintain) is real but small, and the upside (clean focus) outweighs it. Confidence: medium - this is a posture decision; the user could choose differently without breaking the strategy.

**Your feedback.**
> _[reserved for user input]_

---

#### 8.1.3 Phase 0 anchor topic

**Description.** The Phase 0 vertical slice renders the same topic across all 20 initial entries (5 voices x 4 axes worth of cross-application). The choice of topic affects how well the catalog demonstrates its reach in early demos. A topic that bends naturally to all five seed voices teaches more than one that fits only the professional voices.

**Desired outcome context.** A topic that (a) is plausibly written about by a PM, a pastor, a journalist, a friend, and an operations engineer, (b) produces examples short enough to render in 200-800 words each, (c) is non-controversial enough that the audience is not distracted from the formal differences, and (d) the user actually has tacit knowledge about, so review is fast.

**Approach options.**

- **Option A.** "Should we adopt async-first standups?" - professional, opinion-bearing, fits ADR/RFC formats well, has a friend-version and a pastoral-version (rest, presence) but stretches.
- **Option B.** "How to start a morning routine" - personal, fits all voices, naturally renders short. Stretches less for the operator voice.
- **Option C.** "The discipline of rest" - spiritual-first, exceptional for pastoral and devotional renderings, harder for the operator and pragmatic-architect voices.
- **Option D.** "Choosing between Postgres and DynamoDB for a new service" - technical-first, exceptional for architect and operator, very awkward for pastoral.

**Recommendation.** Option A. It is the most balanced first topic because it covers the professional space credibly while still being personable enough that the friend, pastoral, and columnist voices can engage with it (rest cadence, presence, the ethics of always-on). It also exercises the most format diversity (ADR, slack-message, blog-post-long-form, devotional-entry, prd-style). Phase 1 adds Option B as the second anchor topic, broadening the coverage without rebuilding the first slice. Confidence: medium - the case for Option B as the *first* topic is also strong; either is defensible.

**Your feedback.**
> _[reserved for user input]_

---

### 8.2 Items deferred to real-usage data

| # | Decision | Recommendation | Confidence |
|---|---|---|---|
| 8.2.1 | Eval harness timing (Phase 2 rigor or Phase 3 community) | Phase 2, gated on Phase 1 demand signal | Medium |
| 8.2.2 | Audience as a fourth axis | Resist for 12+ months; constraint metadata only | High |
| 8.2.3 | Marketplace publishing timing | Ship as `status: experimental` on marketplace from Phase 0 | Medium |

#### 8.2.1 Eval harness timing

**Description.** An evaluation harness scores model outputs against entry-derived rubrics ("did this read pragmatic-architect?") and publishes results. It is the rigor layer. Two possible homes: Phase 2 (build it as soon as the SDK and MCP exist, treat it as the credibility floor) or Phase 3 (build it after community contribution starts, treat it as the community-flywheel piece).

**Desired outcome context.** The harness should exist before any external claim about quality is made. It should not exist before there is enough catalog content for the rubrics to be meaningful. A bad harness is worse than no harness because false-precision scores erode trust faster than missing scores.

**Approach options.**

- **Option A.** Phase 2 build. Use Promptfoo, derive rubrics from `language_patterns` and `markers` fields. Run against three or four models, publish results. Gate Phase 2 release on at least one credible eval pass.
- **Option B.** Phase 3 build. Treat eval as the community-engagement surface. Crowd-source reference examples and grading. Wait until traffic warrants the investment.
- **Option C.** Skip indefinitely. Quality stays a vibes-based claim; the catalog defends itself on examples alone.

**Recommendation.** Option A, gated on a Phase 1 demand signal. Concretely: if any user during Phase 1 asks "how do I know this works" or "how does this hold up across models," that is the trigger to start Phase 2 with the eval harness as a co-equal deliverable alongside the SDK and MCP. If no such signal arrives, push the harness to Phase 3 and ship Phase 2 without it. The rubrics can be drafted in Phase 1 alongside entry work without committing to the harness build. Confidence: medium - the right answer depends on usage data we do not yet have.

**Your feedback.**
> _[reserved for user input]_

---

#### 8.2.2 Audience as a fourth axis

**Description.** The current model treats Audience as a constraint dimension on entries and examples (`audience: senior-engineers`), not a fully cataloged axis. The case for promoting it to a fourth axis: audiences shape vocabulary, register, and example choice as much as voice does. The case against: three axes plus optional constraints already covers nearly all real compositions, and adding a fourth doubles the combinatorial explanation surface.

**Desired outcome context.** The repo holds the line at three axes long enough to learn whether users actually need a fourth, then decides based on real friction rather than theoretical completeness. A premature fourth axis fragments examples (which audience does this example serve?) and costs months of unnecessary content work.

**Approach options.**

- **Option A.** Hold at three axes. Audience is captured as constraint metadata in entries and examples. Re-evaluate after 12 months of real use.
- **Option B.** Promote Audience to a fourth full axis at Phase 1, with its own folder and frontmatter spec.
- **Option C.** Compromise: ship a controlled-vocabulary `audiences/` reference list (10 to 15 audience profiles) without making it a full axis. Entries reference audience IDs but do not get cross-axis combination examples for Audience.

**Recommendation.** Option A. Resist for at least 12 months of real use. Real signal: users repeatedly express the same audience constraint and find the current frontmatter inadequate. The over-axis trap is well-documented in the source material; resist it actively. Confidence: high - this is one of the safest calls in the brief.

**Your feedback.**
> _[reserved for user input]_

---

#### 8.2.3 Marketplace publishing timing

**Description.** The plugin can be published to the agentskills.io / Claude Code marketplace from Phase 0 (with a clear `status: experimental` flag), held private to `product-on-purpose` until Phase 1 or Phase 2, or registered but listed as `unlisted` until ready.

**Desired outcome context.** Discoverability is a multi-month flywheel. The earlier the plugin is on the marketplace, the earlier it accumulates installs, signal, and feedback. The risk: shipping rough work damages first impressions in a small ecosystem where reputation matters.

**Approach options.**

- **Option A.** Publish as `status: experimental` from Phase 0. Set user expectations clearly in the README.
- **Option B.** Hold private until Phase 1 ships (Composer + 15 entries per axis). Polished first impression at the cost of a month of incubation.
- **Option C.** Register but list as `unlisted` until Phase 1, allowing early adopters with a direct link to install but not surfacing in catalog browse.

**Recommendation.** Option A. Ship as `status: experimental` on the marketplace from Phase 0. Self-selection for early adopters in the agentskills.io community works well; users in this audience read status flags. The discoverability flywheel is worth more than the polish risk, and the experimental flag is the convention exactly for this case. Confidence: medium - reasonable people would choose Option B; Option C is the worst-of-both because it hides the plugin while still committing the maintainer to release discipline.

**Your feedback.**
> _[reserved for user input]_

---

### 8.3 Items I am uncertain about

| # | Question | Recommendation | Confidence |
|---|---|---|---|
| 8.3.1 | Composer smart-defaults: engaging feature or UI gimmick? | Ship in Phase 1, instrument override rate, decide on data | Medium |
| 8.3.2 | Is 5 entries per axis sufficient for Phase 0? | Yes if the 5 span distinctive territory; pick deliberately | Medium-high |
| 8.3.3 | Will LLM-generated examples hold up to human reading? | Yes if maintainer reviews before promoting from `draft` to `stable` | Medium |
| 8.3.4 | Does the no-em-dash rule cover other LLM tells? | No; consider a broader style-tells linter in Phase 2 | Medium |

#### 8.3.1 Composer smart-defaults engagement

**Description.** The Composer's smart-defaults logic surfaces compatible tones and formats when the user picks a voice (driven by the entry's `pairs_well_with` graph). I do not know whether this feels like a craft assist or a UI distraction until users hit it.

**Desired outcome context.** Smart defaults pay for themselves if they reduce the cold-start friction of "what tone goes with this voice." They become noise if users override them more than ~30% of the time, which would suggest the defaults are poorly calibrated rather than helpful.

**Approach options.**

- **Option A.** Ship smart defaults in Phase 1. Instrument override rate. Tune or remove based on data.
- **Option B.** Ship without smart defaults. Add them in Phase 2 only if usage shows users repeatedly flailing on the second and third axis picks.
- **Option C.** Ship a "suggested combinations" panel separately from the picker (defaults are not pre-selected; suggestions are visible alongside).

**Recommendation.** Option A. The `pairs_well_with` graph is the catalog's hidden value; not surfacing it in the primary surface squanders the asset. Ship the defaults, keep the override interaction frictionless (single click), and instrument the override rate. If it climbs above 30%, the data tells us either the defaults are wrong or the UI affordance is wrong. Either learning is more valuable than not knowing. Confidence: medium - this is a UI judgment call; option C is also reasonable.

**Your feedback.**
> _[reserved for user input]_

---

#### 8.3.2 Phase 0 entry count sufficiency

**Description.** The Phase 0 plan calls for 5 entries per axis. The risk is that 5 voices feels insufficient to demonstrate the catalog's reach in early demos, and a contributor or visitor evaluating the project at this stage walks away with the wrong impression.

**Desired outcome context.** Phase 0 demonstrates depth (the schema is real, the validation works, the examples teach) over breadth. The catalog should look intentionally curated, not unfinished. Early visitors should think "this is precise" rather than "this is empty."

**Approach options.**

- **Option A.** Hold at 5 per axis with deliberate spread. Pick the 5 voices to span distinct territory (one professional, one spiritual, one journalistic, one conversational, one operational); same logic for tones, styles, formats.
- **Option B.** Bump to 8 per axis. Reduces curation risk, costs roughly 60% more content work in Phase 0.
- **Option C.** Ship at 5 per axis but explicitly label remaining entries as `status: planned` so the roadmap is visible inside the repo.

**Recommendation.** Option A with intentional spread. Five is enough to teach if the picks are distinctive. Concretely: voices = pragmatic-architect, friendly-mentor, pastoral, columnist, operator. Tones = matter-of-fact, warm, candid, reverent, encouraging. Styles = problem-solution, diataxis-explanation, devotional-reflection, comparison-contrast, classical-argument. Formats = adr, prd, devotional-entry, blog-post-long-form, slack-message. The combination renders meaningfully across the anchor topic. Confidence: medium-high.

**Your feedback.**
> _[reserved for user input]_

---

#### 8.3.3 LLM-generated example quality

**Description.** Phase 0 and Phase 1 will lean on LLM-generated examples (Claude Opus 4.7 most likely) to populate the vertical slices and horizontal-slice topics. The risk: the catalog ends up teaching the model's voice back to itself, with no human ground truth and accumulated drift.

**Desired outcome context.** Examples that read as authentically rendered in the named voice/tone/format, not as generic LLM-prose with a thin coat of vocabulary. The reader should be able to identify the voice from the rendering, not from the frontmatter label.

**Approach options.**

- **Option A.** Maintainer reviews every example before promoting from `draft` to `stable`. Reference-quality examples get a third review pass. Frontmatter records `author_type` and `edited_by` so lineage is visible.
- **Option B.** Hand-author all reference examples. Slowest, highest quality, lowest scale.
- **Option C.** Crowd-source review through community contribution from Phase 2 onward.

**Recommendation.** Option A in Phase 0 and Phase 1; Option C added in Phase 2 to scale reviewing capacity. Hand-authoring (Option B) does not scale to 50 entries per axis. The schema's existing `review_status: draft | reviewed | reference-quality` field plus the maintainer review discipline is the right mitigation. Honest disclosure: if the user does not have time to do a thorough review pass, Option B for a smaller catalog beats Option A for a larger one with light review. Confidence: medium - depends on the user's review time budget, which I do not know.

**Your feedback.**
> _[reserved for user input]_

---

#### 8.3.4 No-em-dash rule coverage

**Description.** The user's CLAUDE.md identifies em-dashes (and en-dashes) as the canonical LLM-prose tell. Other tells exist: predictable trifold structures ("not just X, but Y, and Z"), the "It's not just X, it's Y" formula, hedged enthusiasm ("really exciting opportunity"), opener-cliches ("In today's fast-paced world"), specific adjective bundles ("seamlessly," "robust," "powerful"). The no-em-dash rule will not catch these.

**Desired outcome context.** The catalog's prose should not read as LLM-generated, especially in the prose `ENTRY.md` bodies and the README. A broader style-tells linter would catch the patterns deterministically, the same way the em-dash hook does.

**Approach options.**

- **Option A.** Defer until Phase 2 or later. Use human review as the primary defense in Phase 0 and Phase 1.
- **Option B.** Build a markdownlint plugin or pre-commit hook that flags a curated list of common LLM tells as warnings (not blocks). Deploy in Phase 1.
- **Option C.** Ship a `docs/design-standards/style-tells.md` reference document in Phase 1, with no automated enforcement. Trust contributors to read and apply.

**Recommendation.** Option C in Phase 1, Option B in Phase 2 or as a discrete weekend project later. The style-tells reference document is high-leverage and low-cost. The automated linter is genuinely useful but is a side-project that should not derail the main roadmap. Confidence: medium - the user might value the linter higher than I do based on how much LLM-generated prose ends up in the catalog.

**Your feedback.**
> _[reserved for user input]_

---

### 8.4 What this brief does not answer

These topics are deliberately out of scope for the strategy brief. They each merit their own document or working session.

- **The aesthetic direction of the Composer.** A design problem requiring sketches and a brief inspiration scan (Tailwind UI, Linear, Raycast, the agentskills.io site itself).
- **The exact wording of the static-site front page.** An editorial decision that should wait until the catalog has enough content to point to.
- **The marketing plan.** The roadmap assumes word-of-mouth distribution through the agentskills.io marketplace, the `pm-skills` audience, and Twitter/LinkedIn. An actual launch plan is a separate document.
- **The financial model.** Defer until Phase 3 or until traffic forces the question. The roadmap as drafted assumes free-and-open with optional sponsorship; a paid SaaS variant remains technically possible but is not addressed.

### 8.5 Suggested follow-up artifacts

If the recommendation in Section 5 is accepted, three follow-on documents are worth producing:

1. **A Phase 0 spec** (using `/jp-create-spec`) capturing the 20-entry, one-anchor-topic deliverable with acceptance criteria and source citations.
2. **Three short ADRs** (using `/pm-skills:develop-adr`) for: (a) the Voice-and-Tone-as-paired-axis decision; (b) the per-entry-versioning-deferred decision; (c) the LLM-content-license decision (see 8.1.1).
3. **A Phase 1 design brief** for the Composer, drafted after the Phase 0 dogfooding period closes, capturing what features earned their place in v1 based on real usage rather than upfront speculation.

---

*Strategy Brief v1.0 - 2026-05-08 - drafted by Claude Opus 4.7 from 13 source documents in `_LOCAL/`. Treat the recommendation as the starting position for a working session, not as a final commitment. The roadmap dates are direction, not promises. Re-derive after Phase 0 with real usage signal.*

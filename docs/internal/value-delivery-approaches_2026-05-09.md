---
title: Writing Style Library - Value Delivery Approaches
slug: value-delivery-approaches
date: 2026-05-09
status: draft-v1
authors: [jonathan]
artifact_type: product-catalog
companion_docs:
  - strategy-approach-roadmap_2026-05-08.md
  - overbuilt-v1-execution-plan_2026-05-09.md
license: CC-BY-4.0
---

# Writing Style Library: Value Delivery Approaches

> A catalog of ways to package, surface, and deliver value from the writing-style-library catalog. Spans the obvious (Skill Pack, Composer) through the personalized (LLM-generated individual voice guides) to the speculative (printed reference cards, gamified voice-DNA tests, collaborative team voice management). Use this document to expand the imagination of what the catalog *could become*, then narrow with intent.

---

## 0. Framing

The catalog itself is invisible content - structured frontmatter, prose entries, examples. Users do not "use the catalog." They use a **delivery surface** that consumes the catalog and turns it into something useful in their context.

Three orienting questions for every approach below:

1. **Who is the user?** Specifically, what role and what moment? "A PM writing a PRD at 9pm" is different from "a novelist drafting Chapter 3 on Sunday morning." Different surfaces fit different moments.
2. **What is the interaction unit?** A click, a command, a prompt, a paste, a hotkey, a download, an installation? The smallest meaningful action determines the surface shape.
3. **Where does the catalog touch their workflow?** In their IDE? In their browser? In a printed card on their desk? Embedded in their team's Notion?

The approaches below cluster into ten families. They are not mutually exclusive. A mature library could ship five of them simultaneously, and the catalog content powers all five from the same source of truth.

---

## 1. Agent and Plugin Surfaces

The catalog as callable utility inside agentic environments. Highest leverage for power users; lowest for laypeople.

### 1.1 The Skill Pack (Claude Code, Codex, Cursor, Cline, Windsurf)

**What it is.** An agentskills.io-compliant skill bundle that ships the full catalog as bundled resources and exposes utilities like `compose-instruction`, `apply-voice`, `convert-format`, `evaluate-against-entry`. Users invoke through natural language prompts or `/writing-style-library:recipe-name` slash commands.

**Audience.** Claude Code, Codex, Cursor, Cline users. PM and engineering power users. People already comfortable with skills as workflow primitives.

**Value proposition.** "Stop typing the same voice instructions over and over. Compose precise prompts from named building blocks. Discover combinations you would not have thought of."

**Technical shape.** Single skill folder with progressive disclosure. `taxonomy.json` build artifact bundled. Recipes registered as named callables. ~60 hours of engineering after the catalog exists.

**Business model fit.** Free, distributed via the open marketplace. Sponsorship or upsell could come later.

**Dependencies.** The catalog itself. agentskills.io spec compliance. Claude Code 2.1.x or compatible client.

**Why this matters.** This is the first surface for power users. It lives inside the workflow instead of being a separate destination.

### 1.2 The MCP Server

**What it is.** A Model Context Protocol server that exposes the catalog as tools (`list_voices`, `get_entry`, `compose_instruction`, `apply_voice`, `find_examples`) callable from any MCP-compatible agent: Claude.ai, ChatGPT (where supported), Cursor, Cline, custom agents.

**Audience.** Anyone using an MCP-aware client. Reaches beyond Claude Code into the broader agent ecosystem.

**Value proposition.** "Add this server URL once. The catalog is now available in every tool you use."

**Technical shape.** Cloudflare Worker hosting. Maybe 600 lines of TypeScript. Cache-first because the catalog is mostly static.

**Business model fit.** Free public endpoint with rate-limited free tier. Optional paid tier for high-volume customers (eventually).

**Dependencies.** MCP spec stability. Hosting budget for the public endpoint.

### 1.3 The Custom GPTs and Claude Projects

**What it is.** A library of pre-configured agents - one per voice, one per recipe - distributed through the OpenAI GPT Store and Anthropic's Projects feature. Each agent embodies a specific voice/tone/style/format combination.

**Audience.** Casual users who want one-click agents. People who do not install plugins or run their own MCP servers.

**Value proposition.** "Pick the agent that matches your task. The Pastoral Devotional Writer agent already knows how to write devotional entries in pastoral voice with reverent tone."

**Technical shape.** ~50 custom GPTs and ~50 Claude Projects, generated programmatically from the recipe catalog. Each one has the entry text in its system prompt and a description that aids discovery.

**Business model fit.** Free. Discovery flywheel through OpenAI's marketplace and Anthropic's directory.

**Dependencies.** GPT Store and Claude Projects access. Some prompt-engineering polish per agent.

**Why this matters.** Reaches non-technical users. The same recipe that powers the Skill Pack also powers a Custom GPT, and they share content.

### 1.4 The IDE Plugin (VS Code, JetBrains, Cursor)

**What it is.** A code editor extension that adds writing-style commands inside the IDE. Right-click any selected text, choose a voice, invoke. Especially useful for writing technical documentation, READMEs, comments, and PR descriptions in-context.

**Audience.** Engineers writing prose alongside code. Technical writers who live in VS Code.

**Value proposition.** "Rewrite this docstring in pragmatic-architect voice without leaving your editor."

**Technical shape.** VS Code extension as MVP. Calls the MCP server or SDK. Standard webview for the picker. ~50 hours of engineering.

**Business model fit.** Free in marketplace; visibility flywheel.

**Dependencies.** SDK or MCP server. VS Code extension API (mature).

### 1.5 The Slack and Discord Bot

**What it is.** A bot that responds to mentions with composed instructions or rewritten text. `@stylebot rewrite in friendly-mentor` on a draft message returns the rewritten version. `@stylebot recipe pastoral-devotional` returns a generated draft on a topic.

**Audience.** Teams collaborating in Slack/Discord. Workshop facilitators. Communities.

**Value proposition.** "Compose and rewrite without leaving the channel."

**Technical shape.** Bot framework (Bolt for Slack, discord.js for Discord). BYO-API-key per workspace. ~80 hours of engineering.

**Business model fit.** Free for small teams; paid tier for orgs with >25 seats.

**Dependencies.** SDK. OAuth handling for workspace install. Platform-specific bot review processes.

---

## 2. Web Application Experiences

The catalog as an interactive web product. Different walkthroughs serve different jobs-to-be-done.

### 2.1 The Composer (the canonical walkthrough)

**What it is.** A single-page app where the user picks one value from each axis (voice, tone, style, format), optionally adds topic and audience, and gets a ready-to-use prompt. Live preview, smart defaults, side-by-side comparison, BYO-key live runs.

**Audience.** Writers who want compositional precision. The default landing experience for the public site.

**Walkthrough shape:**
1. Hero: "Pick three things; get a writing recipe."
2. Voice picker: grid of curated cards with one-liners. Filter by category (professional, pastoral, literary).
3. Tone picker: NN/g 4-D slider as default; named-tone grid as alternate.
4. Style picker: Diátaxis or rhetorical-mode chooser, scoped by voice.
5. Format picker: container-and-shape chooser, scoped by voice + style.
6. Topic and audience inputs.
7. Live preview of composed instruction.
8. Run button (BYO key) with side-by-side output.
9. Copy, save, share.

**Value proposition.** "From blank prompt to crafted instruction in 90 seconds."

**Effort.** ~200 hours. Polish-heavy.

### 2.2 The Recipe Marketplace (the curated walkthrough)

**What it is.** A different entry point for users who do not want to compose. Browse 50+ named recipes (`pastoral-devotional`, `architect-adr`, `marketer-landing-page`). Each recipe shows examples, the underlying axis values, and a "use this" button.

**Audience.** Users who want speed over compositional flexibility. New users who do not know where to start.

**Walkthrough shape:**
1. Filter: by domain (professional, pastoral, marketing, literary, etc.).
2. Browse: cards with recipe name, one-liner, axis breakdown, sample output snippet.
3. Open recipe: full page with multiple example renderings, adjustment hints, copy-prompt button.
4. "Remix" link: opens the Composer with the recipe pre-filled.

**Value proposition.** "Already-curated combinations for the most common writing tasks."

**Effort.** ~60 hours on top of the Composer (shared rendering primitives).

### 2.3 The Diff Explorer (the educational walkthrough)

**What it is.** A teaching surface built around diff-pairs. Two columns side by side. Same topic, same three axes, varying one. Hover any phrase for an explanation of why that choice is in this column.

**Audience.** Learners. People who want to understand the taxonomy without committing to compose.

**Walkthrough shape:**
1. Browse pair gallery: filter by axis (voice diffs, tone diffs, etc.).
2. Open a pair: side-by-side examples, axis label highlighted.
3. Annotation layer: hover any sentence to see "this is the architect voice naming a tradeoff explicitly."
4. "Try the inverse" button: swap A and B to compose a new prompt that targets the opposite axis value.

**Value proposition.** "See exactly what 'pragmatic architect' means by reading what it is not."

**Effort.** ~80 hours. The annotation layer is the polish-heavy item.

### 2.4 The Doc Auditor (the analyze-existing-text walkthrough)

**What it is.** A user pastes existing text (a draft email, a blog post, a sermon, a PRD). The auditor analyzes voice, tone, style, format adherence and returns a report: "This reads like a hybrid of pragmatic-architect and operator voice, with matter-of-fact tone, but the format is closer to a tech-spec than the PRD it claims to be."

**Audience.** People who want feedback on existing writing rather than to compose new writing. Writing coaches. Editors. Brand consistency reviewers.

**Walkthrough shape:**
1. Paste text.
2. Optional: declare intended voice/tone/style/format.
3. Analysis pass: LLM-as-judge against entry rubrics.
4. Report: identified voice/tone/style/format with confidence scores. Where the text deviates from declared intent. Suggestions to tighten.
5. "Rewrite to match intent" button.

**Value proposition.** "Understand what your writing actually sounds like, in the catalog's vocabulary."

**Effort.** ~120 hours. Heavy LLM integration; high token cost per audit.

**Note on cost.** This is the surface most likely to require a paid tier or a tight token budget per session.

### 2.5 The Brand Voice Builder (the customized-package walkthrough)

**What it is.** A guided wizard. The user inputs their brand context (industry, audience, mission, tone preferences) plus optional sample writing. The wizard produces a customized brand voice guide as a downloadable package: a Markdown style guide, a one-page reference card, a custom recipe registered against the catalog, and an LLM system prompt ready to drop into ChatGPT, Claude.ai, or any other client.

**Audience.** Founders, brand teams, marketing leads, non-profits, ministries. Anyone who needs a coherent voice across multiple touchpoints and writers.

**Walkthrough shape:**
1. Brand basics: name, mission, audience, industry.
2. Voice direction: pick three to five voices and tones from the catalog as anchors.
3. Style preferences: rhetorical posture, formality, warmth, energy.
4. Sample writing: paste 1-3 examples (optional). Auditor analyzes and surfaces fit.
5. Constraints: words to use, words to avoid, formatting rules.
6. Generate package: LLM produces a complete style guide using catalog vocabulary.
7. Review and refine: click any section to regenerate with feedback.
8. Export: Markdown, PDF, JSON system prompt, Notion template.

**Value proposition.** "A complete brand voice guide in 20 minutes, expressed in the same vocabulary your writers and AI tools already understand."

**Effort.** ~150 hours. The LLM-orchestration logic is non-trivial.

**Business model fit.** Free for individuals; paid ($99-$499 one-time, or $19/month) for teams who want hosted updates and shared workspace.

### 2.6 The Personal Voice Fingerprint (the personalization walkthrough)

**What it is.** The user uploads or pastes 5-10 samples of their own writing. An LLM analyzes against the full catalog and produces a "voice fingerprint": which voices their writing most resembles, which tones dominate, where they shift, which formats they handle best, what makes their writing distinctive. The output is a personalized voice guide they can use as a system prompt or share with collaborators.

**Audience.** Individual writers. Newsletter authors. Solo creators. Anyone whose writing has a personal stamp they want to preserve when working with LLMs.

**Walkthrough shape:**
1. Upload writing samples (or paste, or connect Substack/Medium/Ghost).
2. Sample analysis: per-sample voice/tone/style/format identification.
3. Aggregate fingerprint: dominant voices (with percentages), characteristic tones, signature patterns.
4. Distinguishing markers: specific language patterns the writer uses repeatedly.
5. Personal guide: LLM generates a system-prompt-ready document expressed in catalog vocabulary plus the writer's own markers.
6. Refinement: writer flags items as "yes that is me" or "not quite" to refine.
7. Export: Markdown, system-prompt JSON, custom GPT, Claude Project.

**Value proposition.** "Stop having LLMs flatten your voice into generic LLM-prose. Your fingerprint document lets any model write in your voice with your patterns, named in a vocabulary that stays consistent across tools."

**Effort.** ~180 hours. The fingerprint algorithm needs careful tuning to avoid generic output.

**Business model fit.** Likely paid. The personal fingerprint is the most "I would pay for this" surface in the catalog.

**Why this matters.** This is the surface that turns the catalog from a public reference into a personal tool. It is also the surface most likely to be the breakthrough product.

### 2.7 The Voice Swap Service (the transformation walkthrough)

**What it is.** A simple paste-and-transform tool. Paste any text. Pick a voice and tone. Get the same content rewritten. Quick, single-purpose, no compositional friction.

**Audience.** Casual users. Anyone with a one-off rewrite task.

**Walkthrough shape:**
1. Paste source text.
2. Pick target voice + tone (defaults provided).
3. Optionally constrain length and format.
4. Get rewrite.

**Value proposition.** "Need this email to sound friendlier? Paste, pick, done."

**Effort.** ~40 hours.

**Business model fit.** Free with rate limit; paid for high-volume.

---

## 3. Pre-Packaged Vertical Products

The catalog as the source for hand-curated, domain-specific bundles. Sold or distributed as named products with their own value proposition.

### 3.1 The Academic Writing Package

**What it is.** A bundle of 15-20 entries plus 5-8 recipes specifically curated for academic writing. Includes voices like `academic`, `theoretician`, `historian`, `critic`; tones like `measured`, `tentative`, `analytical`; styles like `classical-argument`, `analysis`, `synthesis`, `comparison-contrast`; formats like `journal-article-section`, `literature-review`, `dissertation-chapter`, `conference-paper`.

**Plus:** A field-specific style guide pulling APA/MLA/Chicago conventions, a citation-aware recipe set, and templates for common academic genres.

**Audience.** PhD students, academics, journal editors, scholarly writers.

**Delivery.** Markdown bundle. Optional Pandoc + LaTeX templates. Custom GPT and Claude Project pre-configured. Workshop curriculum.

**Business model fit.** Free open package; paid extended edition ($39) with more recipes, eval rubrics, and field-specific variants (humanities, hard sciences, social sciences, education research).

### 3.2 The Fiction Writing Package

**What it is.** A bundle for novelists and short-story writers. Voices like `literary-novelist`, `hardboiled-narrator`, `gothic-narrator`, `young-adult-narrator`, `lyrical-beat`; tones across the full emotional register; styles like `chronological-narration`, `flashback-narration`, `in-medias-res`, `frame-narrative`; formats like `short-story`, `novel-chapter`, `scene`, `dialogue-scene`, `monologue`, `vignette`.

**Plus:** Genre-specific sub-packages (Mystery, Thriller, Sci-Fi, Fantasy, Romance, Literary, YA, Children's). Each sub-package has its own recipes, anchor scenes, and conventions.

**Audience.** Novelists, short-fiction writers, creative-writing students, hobbyists.

**Delivery.** Markdown bundle. Scrivener-importable template set. Recipe library focused on common scenes (opening, dialogue, emotional pivot, climax). Custom GPTs per genre.

**Business model fit.** Free core; paid genre add-ons ($19 each) and a complete bundle ($99). Workshop and editorial-coaching upsells.

### 3.3 The Professional and Brand Package

**What it is.** A modular bundle for organizations and professionals. Includes:

- **The Executive package:** voices and recipes for memos, board updates, all-hands.
- **The Product package:** PRDs, RFCs, ADRs, design docs.
- **The Engineering package:** runbooks, postmortems, tech specs, architecture decisions.
- **The Marketing package:** landing pages, case studies, campaign briefs, press releases.
- **The Sales package:** cold emails, proposals, objection-handling sheets.
- **The Customer Success package:** support replies, onboarding docs, escalation comms.

**Audience.** Companies and professionals working across these functions.

**Delivery.** Modular Markdown packages. SDK integration for tools like Notion, Coda, Slab. Custom Claude Projects per package. Branded onboarding for teams.

**Business model fit.** Free individual modules; paid bundles ($199-$499/team/year). Enterprise customization at higher tiers.

### 3.4 The Vertical Industry Packages

**What it is.** Industry-tuned packages that combine the right recipes with sector-specific vocabulary and constraints.

- **Healthcare communications package:** patient-friendly explanations, medical-precision tone, regulatory-aware constraints.
- **Fintech communications package:** clarity-first, compliance-aware, calm-under-uncertainty.
- **EdTech communications package:** learner-centered, scaffolded, age-aware.
- **Nonprofit communications package:** mission-led, donor-aware, story-driven.
- **Legal practice package:** precedent-aware, defensive, plain-English-where-allowed.
- **Real estate package:** description, listing, market analysis.

**Audience.** Vertical practitioners and small-team marketers in these industries.

**Delivery.** Markdown packages. Sector-specific recipes. Optional sector-specific Custom GPTs.

**Business model fit.** Paid ($99-$299 per vertical). Sells well to small businesses that need brand consistency without hiring a brand consultant.

### 3.5 The Pastoral and Ministry Package

**What it is.** A package specifically for clergy, ministry leaders, lay teachers, and devotional writers. Voices like `pastor`, `theologian`, `mystic-contemplative`, `devotional-writer`, `prophetic-voice`, `chaplain`, `liturgical-curator`. Recipes for sermons (manuscript, outline), funeral homilies, Bible studies, devotional entries, prayer composition, liturgy, congregational letters.

**Plus:** Optional theological tradition variants (Reformed, Anglican, Catholic, Orthodox, Evangelical, Wesleyan, Lutheran). Optional denomination-specific lectionary integration.

**Audience.** Pastors, lay ministers, ministry teams, seminarians, devotional bloggers.

**Delivery.** Markdown package. Lectionary-aware recipe set (gives a recipe per Sunday). Custom GPTs per role. Possible podcast integration.

**Business model fit.** Free core; paid theological-tradition add-ons ($29 each). Subscription for lectionary-aware weekly recipes ($9/month).

**Why this matters to the user specifically.** Given the user's product-on-purpose context and existing pastoral-voice work, this is plausibly the highest-personal-fit package and a defensible niche to lead with.

### 3.6 The Education Package

**What it is.** Packages for teachers, curriculum designers, and instructional designers. Voices like `patient-teacher`, `socratic-tutor`, `popular-science-explainer`; styles like `diataxis-tutorial`, `process-explanation`, `illustration-exemplification`; formats like `lesson-plan`, `worksheet`, `quiz-test`, `curriculum-outline`, `course-module`, `study-guide`.

**Plus:** Age-band variants (early elementary, middle grade, high school, college, adult professional development). Subject-specific sub-packages.

**Audience.** K-12 teachers, college instructors, corporate L&D, homeschoolers, course creators.

**Delivery.** Markdown package. Lesson-plan templates. Custom GPTs for "elementary tutor," "high-school tutor," "college TA." Optional grading rubrics.

**Business model fit.** Free core; paid age-band add-ons. Significant upsell potential for course creators.

---

## 4. LLM-Personalized Individual Outputs

The catalog as raw material that gets transformed by an LLM into something tailored to the individual user.

### 4.1 The Personal Voice Fingerprint (depth treatment)

Already introduced as 2.6. Worth elaborating because this is plausibly the breakthrough product.

**The problem it solves.** Solo creators (newsletter authors, bloggers, novelists, podcasters) have a recognizable voice. When they use LLMs to draft, edit, or expand, the LLM flattens their voice toward its own house style. Generic prompts ("write in my voice") fail because the LLM has no model of the writer's voice.

**The fingerprint as solution.** A document that names the writer's voice in catalog vocabulary plus their personal markers. Examples of fingerprint sections:

- *Dominant voices:* `columnist` (45%), `friendly-mentor` (25%), `essayist` (20%), `confidant` (10%).
- *Characteristic tones:* `candid` always; `playful` situationally; `reverent` for grief or change topics; never `stiff` or `corporate`.
- *Signature patterns:* lowercase headlines; "you" address; one-sentence-paragraphs for emphasis; long parenthetical asides; trailing m-dash replaced with " - ".
- *Format gravitational pull:* `essay`, `email-newsletter-issue`, `linkedin-post`, `magazine-article`. Avoids: `pitch-deck`, `whitepaper`.
- *Lexical signatures:* uses "actually" once per piece; never uses "leverage" as a verb; favors "and so" over "therefore."
- *Avoidances:* no exclamation marks except in dialogue; no "in today's world" openers; no trifold structures.

This document becomes a system prompt the writer drops into Claude.ai, ChatGPT, or any other tool. It also becomes a teaching artifact: the writer learns about their own voice by reading the fingerprint.

**Re-applying the fingerprint.** Annual or semi-annual refresh: paste new writing samples; the fingerprint updates as the voice evolves. Voice drift is now observable.

**Business model.** Free first fingerprint; paid refresh subscription ($49/year) or premium with multi-document analysis ($149 one-time).

### 4.2 The Personalized Style Guide (team-aware variant)

**What it is.** Same fingerprint approach, but applied to a team or brand. Multiple contributors paste samples; the system identifies the unifying voice ("your team writes like a hybrid of `pragmatic-architect` and `operator` voices, dominated by `candid` tone"), the divergences ("contributor B leans more `executive`, contributor C drifts toward `friendly-mentor` in customer-facing channels"), and produces a shared style guide expressed in catalog vocabulary.

**Audience.** Teams that want voice coherence without a brand consultant. Distributed companies. Open-source projects.

**Value.** A team voice document grounded in actual writing rather than aspirational adjectives.

### 4.3 The Drift Tracker

**What it is.** A long-running service that ingests a writer's published content (RSS, Substack API, Medium API) and produces monthly drift reports. "Your `confidant` percentage has risen from 10% to 25% over the last six months. Your `playful` tone shows up in 30% more pieces than a year ago. Your sentence-length median has dropped from 18 to 14 words."

**Audience.** Writers tracking their evolution. Editors who care about consistency.

**Value.** Voice as observable, measurable, comparable over time.

### 4.4 The Coaching Bot

**What it is.** An agent that gives feedback on drafts against the writer's stated voice goals. "You said you want to write more like `columnist`; this draft reads like `executive`. Three concrete edits would shift it." 

**Audience.** Solo writers without an editor. Writers actively trying to evolve their voice.

**Value.** Editorial coaching for $0-$20/month instead of $200/hour.

### 4.5 The Translation Tool

**What it is.** Paste your writing in your voice. Get the same content translated into another voice while preserving your factual content and signature markers.

**Use case.** "I want to publish this as a LinkedIn post in my normal columnist voice, AND as a more formal whitepaper section. Translate it across without rewriting from scratch."

---

## 5. Print and Physical Products

The catalog as content that escapes the screen. Slow to update but high tactile value.

### 5.1 The Reference Card Set

**What it is.** A boxed set of beautifully designed reference cards. One per voice. One per tone. One per format. Each card has the entry's name, one-liner, three language patterns, two pair-well-with hints, and a sample sentence.

**Audience.** Working writers, editors, brand teams, classroom teachers. People who like physical reference.

**Delivery.** Print-on-demand via a service like Inkthreadable, MOO, or Printify. Paid product ($59-$99 per set).

**Business model fit.** Profitable as a physical product. Doubles as a marketing surface.

### 5.2 The Wall Poster

**What it is.** A large-format poster (24"x36" or A1) showing the three-axis taxonomy as a single visual reference. Voices grouped by category, tones arranged on spectrums, formats organized by domain.

**Audience.** Writers' rooms, agency walls, classrooms.

**Delivery.** Print-on-demand. $39-$59. Tasteful, design-forward, not corporate.

### 5.3 The Reference Book (long horizon)

**What it is.** A printed book version of the catalog. ~250 pages. Each entry gets a one-page treatment with examples. Organized for reading, not just lookup.

**Audience.** Anyone who likes books over web pages. Writing instructors. People who want a permanent reference.

**Delivery.** Self-published or via a small press. Hardcover ($35), paperback ($25), digital ($15).

**Why this is interesting.** A book signals intent and earns credibility. It also forces editorial discipline ("does this deserve a page?") that purely-digital catalogs avoid.

### 5.4 The Anki Deck (or alternative SRS deck)

**What it is.** A spaced-repetition flashcard deck for learning the taxonomy. One card per entry: front shows the name and one-liner, back shows pairings, confusables, and a sample sentence.

**Audience.** Writing students, writing teachers, editors building their vocabulary.

**Delivery.** Free Anki deck. Free Mochi deck. Distributed through the Anki shared deck repository.

**Business model fit.** Free, marketing flywheel.

---

## 6. Editorial and Educational Products

The catalog as curriculum, content, and ongoing publication.

### 6.1 The Newsletter

**What it is.** A weekly or biweekly newsletter. Each issue ships one diff-pair (two examples of the same topic with one axis varied) and one new recipe. Issues are written in the voice they are teaching.

**Audience.** Writers, content people, knowledge workers. Anyone who wants to study writing alongside doing it.

**Delivery.** Substack or Ghost. Free with optional paid tier for archive access and recipe downloads.

**Editorial principle.** Each issue earns its place by teaching something the catalog page alone cannot: the rhythm of comparison, the surprise of a confusable, the satisfaction of a new recipe.

### 6.2 The Podcast

**What it is.** A podcast where each episode is one entry. The host reads aloud the prose entry, performs the language patterns, and reads the anchor-topic example in voice. Bonus episodes do diff-pair audio comparisons.

**Audience.** Writers who learn through hearing. Walking commuters. Students.

**Delivery.** RSS feed. Distributed to Apple, Spotify, YouTube. ~15-20 minute episodes.

**Production cost.** Real. Voice acting takes time and feels distinct in audio. Could start AI-narrated and migrate to human as the catalog matures.

### 6.3 The Curriculum

**What it is.** A structured course (online or in-person) that teaches the taxonomy and its application. 6 weeks: one week per axis, plus composition and personalization weeks. Includes assignments, peer review, and a final project (build your own personal voice fingerprint).

**Audience.** MFA programs, copywriting bootcamps, corporate L&D, individual learners.

**Delivery.** Self-paced course on a platform like Maven or Podia. Or licensed to MFA programs and bootcamps.

**Business model fit.** Premium product ($299-$799 per cohort). Possible enterprise licensing.

### 6.4 The Workshop and Conference Talk Set

**What it is.** A set of polished talks and workshops on the taxonomy, designed to be delivered at writing conferences, AI conferences, content design conferences, ministry training, or as paid workshops.

**Audience.** Conference programmers, organizational L&D leads, retreat organizers.

**Delivery.** Slide decks, speaker notes, workshop facilitation guides.

**Business model fit.** Speaking fees ($1,000-$5,000 per talk) and workshop facilitation ($2,500-$10,000 per session).

### 6.5 The Book (long horizon, the bigger book than 5.3)

**What it is.** A trade nonfiction book. Less a reference, more an argument. The Three-Axis Theory of Writing Instruction. The catalog is one chapter; the rest is the case for compositional precision in the AI era, the history of writing taxonomies, the case studies, and the manifesto.

**Audience.** Writers, editors, AI practitioners, content designers, the same audience that bought Diataxis as a book or Mailchimp's voice guide as a model.

**Delivery.** Trade publisher (preferred) or self-published.

**Why this is interesting.** Books are the strongest credibility artifact in this category. The catalog is invisible; the book is the visible thesis. Diataxis works because the framework is opinionated and book-shaped, even though most users encounter it on a website. Same logic could work here.

---

## 7. API and Developer Surfaces

The catalog as infrastructure other developers build on.

### 7.1 The TypeScript SDK

**What it is.** `@product-on-purpose/writing-style-library` on npm. Typed accessors for every entry, composition utilities, validation helpers. Built-in catalog (no network call required for the basic API).

**Audience.** Developers building writing tools, content platforms, brand-management software.

**Value proposition.** "The catalog as an importable module with full TypeScript autocomplete on valid IDs."

**Business model.** Free. Distribution flywheel.

### 7.2 The Python SDK

Same as 7.1, idiomatic Python, on PyPI. For data scientists, ML engineers, content automation builders.

### 7.3 The REST API

**What it is.** A hosted HTTP API that exposes the catalog and composition utilities. Gives non-Python/non-TS developers (Ruby, PHP, Go, Java, no-code platforms) a way in.

**Audience.** Developers in non-JS/Python languages. No-code platforms (Zapier, Make, Bubble).

**Delivery.** Cloudflare Worker. OpenAPI spec. Free tier with rate limits; paid tier for higher volume.

### 7.4 The Webhook Service

**What it is.** Subscribe to catalog changes. Get notified when a new entry, recipe, or example is added or updated. Useful for downstream integrations that mirror the catalog.

**Audience.** Anyone who has built on the catalog and wants to stay in sync.

### 7.5 The Open-Source SDK as Reference

**What it is.** The SDK code itself is the reference implementation of how to consume the catalog. Other clients (Ruby gem, PHP package) can crib from it.

---

## 8. Collaboration and Org Surfaces

The catalog as a team utility, not a solo tool.

### 8.1 The Team Voice Workspace

**What it is.** A multi-tenant SaaS where teams own their own brand voice (built via the Brand Voice Builder), invite collaborators, and assign voice rules per channel (LinkedIn voice vs Slack voice vs customer-comms voice). The workspace integrates with Slack, Notion, and Google Docs to auto-suggest voice corrections.

**Audience.** Marketing teams, content teams, distributed companies.

**Value proposition.** "One source of truth for how your team writes. Updated by voting and review, applied by tooling."

**Business model fit.** SaaS at $19-$99/seat/month. The most plausible significant-revenue surface.

### 8.2 The Brand Audit Service

**What it is.** A service (manual + LLM-assisted) that audits a company's existing content (website, docs, marketing materials, support replies) against their declared brand voice. Returns a report, suggested corrections, and a refresh proposal.

**Audience.** Mid-market companies with brand consistency problems.

**Delivery.** Service business. $5,000-$25,000 per engagement.

### 8.3 The Style Guide Hosting

**What it is.** A hosted home for organizational style guides built on the catalog. Version-controlled, searchable, cross-linked. Public or private. Like Frontify or Notion-as-a-style-guide but with the catalog as the underlying vocabulary.

**Audience.** Companies with style guides scattered across docs.

**Business model fit.** Free for public guides; paid ($49-$199/month) for private hosting.

### 8.4 The Editor's Dashboard

**What it is.** A dashboard for editors who manage multiple writers. Shows each writer's voice fingerprint, drift, recent submissions, and consistency with the publication's house voice.

**Audience.** Newsletter editors, magazine editors, content managers.

---

## 9. Integration and Embedding Surfaces

The catalog as a feature inside other tools the user already uses.

### 9.1 The Notion Integration

**What it is.** A Notion sidebar plugin that exposes the catalog inside Notion. Right-click any text block, choose "rewrite in voice" from the menu, get an inline rewrite.

**Audience.** Notion-native teams. Knowledge workers who live in Notion.

**Delivery.** Notion plugin or paid integration.

### 9.2 The Obsidian Plugin

**What it is.** Same idea, for Obsidian. Especially valuable for personal knowledge managers, journalers, devotional writers.

**Audience.** Obsidian users.

**Delivery.** Free plugin in Obsidian's community plugin directory.

### 9.3 The Substack and Ghost Integration

**What it is.** A button in the Substack/Ghost editor that opens the Composer or Voice Swap pre-filled with the current draft.

**Audience.** Newsletter writers.

**Delivery.** Browser extension (since Substack and Ghost have limited plugin APIs) plus an iframe-embed option.

### 9.4 The Mailchimp / ConvertKit / Beehiiv Integration

**What it is.** Email-marketing platforms get a voice-checker before send. Audit your campaign against your brand voice. Get suggestions. Optionally auto-apply.

**Audience.** Email marketers.

**Delivery.** Platform-specific integrations, gated on platform partnership programs.

### 9.5 The Google Docs Add-on

**What it is.** A Docs add-on that exposes the catalog's voice swap, audit, and brand-guide features inside Docs.

**Audience.** Anyone who writes in Docs (still a huge surface).

### 9.6 The Browser Extension (universal)

**What it is.** A lightweight browser extension that adds a hotkey for voice-swap on any web textarea. Works in Gmail, Slack web, LinkedIn, Twitter compose, X, Discord web, anywhere.

**Audience.** Casual users in many tools.

**Delivery.** Chrome Web Store, Firefox Add-ons, Safari (eventually).

---

## 10. Creative and Speculative Surfaces

The wild ideas. Some will work. Most will not. Worth listing because the breakthrough surface is usually not on the conservative list.

### 10.1 The Voice DNA Test

**What it is.** A gamified personality-style quiz. 20 questions about how the user writes (paired with sample comparisons: "Which of these emails sounds more like you, A or B?"). At the end, the user gets a "Voice DNA" result: a pretty sharable graphic naming their dominant voice and tone.

**Audience.** Casual users. Social media. The kind of audience that takes BuzzFeed quizzes.

**Value proposition.** "Find your writing voice in 5 minutes."

**Business model fit.** Free. Top-of-funnel for everything else. Lead magnet.

**Why this might work.** Catchy, low-stakes, shareable. People love quizzes about themselves.

### 10.2 The Voice Map Visualization

**What it is.** A 2D or 3D visualization of voice space. Each voice is a point. Distance encodes similarity. The user's fingerprint shows up as a region on the map. Public-figure fingerprints (Hemingway, David Sedaris, Anne Lamott - public-domain or with-permission samples) appear as labeled landmarks.

**Audience.** Visual learners. Generative-art enthusiasts. People who want to "see" the catalog.

**Delivery.** Interactive WebGL viz on the public site. Generative art prints as a paid product.

### 10.3 The "Write Like..." Series

**What it is.** A series of ethically-careful imitation models. "Write Like Hemingway" pre-loads voice = `hardboiled-narrator` + tone = `cool` + style = `chronological-narration` + format = `short-story`, plus a curated set of public-domain Hemingway markers.

**Audience.** Aspiring writers, students.

**Ethical note.** Avoid living writers without permission. Stick to public-domain authors (Twain, Austen, Hemingway, Wharton, Chesterton, Wells).

### 10.4 The Live Voice Coach (audio in/audio out)

**What it is.** A voice-conversation tool. The user speaks freely; the LLM transcribes, identifies dominant voice, gives feedback. Useful for speech writers, podcasters, sermon preppers.

**Audience.** Spoken-word people. Pastors. Podcasters.

**Delivery.** Web app with OpenAI Whisper + LLM analysis.

### 10.5 The Contemporary Letter Generator

**What it is.** An ethically-careful product that helps people write hard letters. Goodbye letters to dying loved ones. Letters of forgiveness. Letters of confession. Letters to a child for their 18th birthday. The catalog provides the voice scaffolding (`pastor`, `memoirist`, `confidant`, `mystic-contemplative`); the LLM provides the personalization.

**Audience.** People in hard moments who want help finding the words.

**Business model fit.** Free, mission-aligned. Doubles as the most defensible "this catalog matters" demonstration.

### 10.6 The Sermon Prep Co-Pilot

**What it is.** A specialized agent for preachers. Inputs: the lectionary text, the sermon's main idea, the congregation's context. The agent walks through the homiletic recipe (`pastor` + `reverent` + `homiletic-style` + `sermon-manuscript`), suggests structures, drafts paragraphs, flags style drift.

**Audience.** Pastors, lay preachers.

**Business model fit.** Subscription ($9-$29/month), bundled with the Pastoral Package.

### 10.7 The Generative Art Print Series

**What it is.** Each voice gets an algorithmically-generated visualization. The pragmatic-architect voice rendered as a Mondrian-grid. The mystic-contemplative voice rendered as flowing watercolor. Sold as art prints.

**Audience.** Art-buyers, writers' offices, agency walls.

**Delivery.** Print-on-demand.

### 10.8 The Voice Translation Game

**What it is.** A game/training tool. The user is given a paragraph in voice A. They have to rewrite it in voice B. The system grades.

**Audience.** Writing students, language learners (advanced English).

### 10.9 The Cross-Language Adaptation Tool

**What it is.** Paste an English original. Pick a target language and voice. Get a translation that preserves the voice across languages. ("Translate this in Spanish in `pastoral` voice.")

**Audience.** Multilingual content teams. Mission-driven organizations.

**Effort.** Real. Translation quality is hard. The voice consistency adds complexity.

### 10.10 The Public-Speaking Coach

**What it is.** A tool that adapts the catalog for spoken delivery. Voices have spoken-cadence variants. Tones map to vocal pitch and pace. Formats become talk structures. Output is a delivery script with stage directions.

**Audience.** Public speakers, conference presenters, sermon delivers.

---

## 11. Cross-Cutting Themes

A few patterns repeat across many of the surfaces above. Worth naming so they can be designed once and reused.

### 11.1 The "remix" affordance

Every surface should let users move sideways into another surface with state preserved. From a recipe page, "Open in Composer." From a fingerprint result, "Try with this voice swap." From a brand guide, "Test this on a draft." The catalog's value compounds when surfaces interconnect.

### 11.2 BYO API key

Every paid LLM-call surface defaults to bring-your-own-key for serious users, with a hosted-demo for casual. This keeps cost exposure bounded and aligns incentives. Free hosted-demo is a marketing budget, not a product feature.

### 11.3 Citations on outputs

Every LLM-generated output cites the catalog entries used: "Composed from voice:pragmatic-architect, tone:matter-of-fact, format:adr." This teaches the catalog and creates a feedback loop ("the tone is off; let me try matter-of-fact at lower intensity").

### 11.4 The fingerprint as the personalization primitive

Once the user has a fingerprint, every other surface gets richer. Composer pre-loads with the user's dominant voice. Voice Swap defaults to translating *to* the user's voice from generic LLM-prose. The audit measures distance from the fingerprint, not from a generic standard.

### 11.5 The package as the product

Packages (academic, fiction, brand, ministry, education, vertical) are how the catalog reaches non-power-users. They turn 290 entries into one purchase.

### 11.6 The ecosystem flywheel

Every surface that reaches a new audience grows the catalog's pull. Custom GPTs reach OpenAI users. MCP server reaches Cursor and Cline users. Notion plugin reaches Notion-native teams. The marginal cost of one more surface is low; the marginal audience reach is high.

---

## 12. Recommended Sequencing

If the user wants to build many of these but cannot build all of them simultaneously, this is a defensible order:

### Wave 1: Foundation surfaces (months 1-12)

1. The Skill Pack (1.1) - first because it serves the maintainer.
2. The Composer (2.1) - the canonical public surface.
3. The Recipe Marketplace (2.2) - shared infrastructure with Composer.
4. The TypeScript SDK (7.1) - cheap given the catalog is structured.
5. The Static Site - prerequisite for almost everything.

### Wave 2: Reach surfaces (months 13-18)

6. The MCP Server (1.2) - cross-agent reach.
7. The Custom GPTs and Claude Projects (1.3) - reaches non-Claude-Code users.
8. The Brand Voice Builder (2.5) - first paid product candidate.
9. The Personal Voice Fingerprint (2.6) - the breakthrough candidate.
10. The Newsletter (6.1) - editorial flywheel.

### Wave 3: Vertical and team surfaces (months 19-24)

11. Pastoral and Ministry Package (3.5) - leads the vertical packages, given user fit.
12. The Doc Auditor (2.4) - completes the analyze-existing-text capability.
13. The Team Voice Workspace (8.1) - first significant-revenue candidate.
14. The Notion and Obsidian Integrations (9.1, 9.2).
15. The Browser Extension (9.6) - universal reach.

### Wave 4: Editorial and physical (months 25+)

16. The Reference Card Set (5.1).
17. The Curriculum (6.3).
18. The Podcast (6.2).
19. The remaining vertical packages (3.1-3.6).
20. Speculative experiments (10.x).

### Wave 5: Books and consulting (long horizon)

21. The Reference Book (5.3) and the Trade Nonfiction Book (6.5).
22. The Brand Audit Service (8.2).
23. The Workshop and Conference Talk Set (6.4).

---

## 13. What This Document Does Not Decide

- Which surfaces become commercial vs free. Most have free defaults; some lean toward paid (Brand Voice Builder, Personal Voice Fingerprint, Team Voice Workspace, vertical packages).
- The exact pricing of paid surfaces. Suggestive ranges given; needs market testing.
- Whether to vertically integrate (build all surfaces in-house) or partner (license content to existing tools).
- Marketing strategy. The roadmap assumes word-of-mouth + agentskills.io marketplace + content flywheel; an actual launch plan is a separate document.
- The legal structure for the commercial surfaces. Sole-prop, LLC, or fund-raising depends on revenue projections this document does not produce.

---

## 14. Closing Frame

The catalog itself is a small thing: structured data plus prose plus examples. The surfaces above are how the small thing becomes a useful thing in the user's actual life. The breakthrough product is probably one of the personalization surfaces (2.6 Voice Fingerprint, 4.1 Personal Voice Fingerprint, 8.1 Team Voice Workspace) - the surfaces where the catalog stops being a public reference and starts being a private tool tailored to the user's specific writing.

The conservative move is Wave 1 only. The ambitious move is Waves 1-3 inside three years. The visionary move is the trade book plus three commercial surfaces plus a defensible niche package (likely pastoral). All three are defensible; the right one depends on time horizon, capital, and whether the maintainer sees this as a tool, a product, or a body of work.

---

*Value Delivery Approaches v1.0 - 2026-05-09 - inventory of surfaces and packages that consume the writing-style-library catalog. Not a commitment to build any single one; a menu of possibilities to narrow with intent. Companion to `strategy-approach-roadmap_2026-05-08.md` and `overbuilt-v1-execution-plan_2026-05-09.md`.*

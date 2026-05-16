---
title: Aspirational Catalog Inventory - Format and Voice Candidates
date: 2026-05-16
author: claude (Opus 4.7)
status: draft - working material for taxonomy evaluation
type: inventory
related:
  - docs/internal/_working/domain-and-family-taxonomy_2026-05-15.md
  - docs/internal/_working/phase-2-catalog-expansion_2026-05-15.md
---

# Aspirational Catalog Inventory - Format and Voice Candidates

## Purpose

The domain/family taxonomy proposal at `domain-and-family-taxonomy_2026-05-15.md` was evaluated against ~75 candidate formats and ~40 candidate voices. The v1 and v2 cuts were both rejected because the underlying sample was too thin to tell whether categories were working.

This document builds a much larger aspirational inventory - the full territory the catalog could plausibly grow into - so the taxonomy can be evaluated against material rather than theory. Targets: ~180 format candidates, ~70 voice candidates.

Each entry is tagged with its current status:

| Tag | Meaning |
|---|---|
| `[current]` | In the Phase 1 catalog at HEAD |
| `[v1-candidate]` | Proposed in the Phase 2 design spec |
| `[v2-candidate]` | Added in taxonomy v2 (May 15) |
| `[v3-new]` | Added in this inventory pass |

The inventory is grouped by the v2 domain/family taxonomy so categories can be stress-tested. Where an entry sits awkwardly in its assigned family, it is marked with a `?` and the alternative placement noted. Where an entry does not fit any family, it is collected in an "unfit" section at the end of each axis.

The inventory is not a commitment to build all of these. Phase 2 still targets 30 entries per axis. The inventory's purpose is to define the *territory* the taxonomy must cover.

## Scope rules

In scope:

- Writing produced by knowledge workers (engineers, PMs, designers, marketers, leaders, ops)
- Public writing (essays, posts, articles, public statements)
- Personal correspondence (letters, notes, cards)
- Ceremonial speech (eulogies, toasts, dedications)
- Pastoral and contemplative writing (sermons, devotionals, prayers, journals)
- Educational writing produced by teachers and curriculum designers
- Customer-facing communication (support, sales, marketing)
- Internal-facing communication (HR, ops, leadership)
- Long-form creative non-fiction (essays, memoir, profiles)

Out of scope:

- Fiction (novels, short stories, screenplays, plays)
- Poetry (separate craft with its own conventions)
- Highly specialized professional writing: legal briefs, medical clinical notes, scientific papers, academic monographs - these have field-specific conventions deserving their own treatment
- Journalism produced by working reporters (a related but separate territory)
- Government/policy writing produced by working staff (out of repo's intended audience)
- Children's writing (separate genre)
- Translation work

## Format inventory

### `professional` domain

#### `deliberation` family

Writing whose purpose is to record, propose, or argue for a substantive decision.

- `adr` - architecture decision record `[current]`
- `prd` - product requirements document `[current]`
- `design-doc` - technical design document `[v1-candidate]`
- `rfc` - request for comments `[v1-candidate]`
- `whitepaper` - long-form authoritative position paper `[current]`
- `postmortem` - post-incident analysis and learnings `[v2-candidate]`
- `position-paper` - structured argument for an internal position `[v2-candidate]`
- `decision-memo` - short memo recording a single decision and rationale `[v3-new]`
- `strategic-plan` - multi-year direction document `[v3-new]`
- `board-memo` - paper prepared for board or executive review `[v3-new]`
- `architecture-doc` - system architecture overview `[v3-new]`
- `feature-spec` - detailed specification of a single feature `[v3-new]`
- `roadmap` - sequenced direction document with rationale `[v3-new]`
- `swot-analysis` - structured strengths/weaknesses/opportunities/threats `[v3-new]`
- `risk-register` - structured catalog of known risks `[v3-new]`

#### `instruction` family

Writing whose purpose is to teach, guide, or document so a reader can act.

- `readme` - repository or project README `[current]`
- `technical-reference` - API, library, or system reference `[current]`
- `runbook` - operational procedure document `[v2-candidate]`
- `api-doc` - per-endpoint or per-method API documentation `[v2-candidate]`
- `error-message` - user-facing error text `[v1-candidate]`
- `microcopy` - UI string design `[v1-candidate]`
- `faq` - frequently asked questions `[v1-candidate]`
- `onboarding-walkthrough` - new-user or new-hire walkthrough `[v1-candidate]`
- `lesson-plan` - structured plan for a single teaching session `[v2-candidate]`
- `syllabus` - course-level scope and sequence `[v2-candidate]`
- `curriculum-outline` - multi-course or program-level structure `[v2-candidate]`
- `tutorial` - step-by-step task walkthrough `[v3-new]`
- `how-to-guide` - task-focused reference (not introductory tutorial) `[v3-new]`
- `study-guide` - reader-facing review document for learners `[v3-new]`
- `glossary` - controlled-term reference `[v3-new]`
- `style-guide` - editorial or design conventions document `[v3-new]`
- `policy-doc` - statement of policy with rationale and scope `[v3-new]`
- `sop` - standard operating procedure `[v3-new]`
- `accessibility-audit` - documented accessibility evaluation `[v3-new]`

#### `progress` family

Writing whose purpose is to communicate ongoing state, change, or completion to a known internal audience.

- `changelog-entry` - per-release change description `[current]`
- `daily-standup` - short daily team update `[current]`
- `status-report` - periodic project or team status `[current]`
- `release-notes` - per-release notes for internal or external audience `[v2-candidate]`
- `okr-update` - quarterly OKR progress and grading `[v2-candidate]`
- `deprecation-notice` - announcement of a forthcoming removal `[v2-candidate]`
- `meeting-notes` - notes from a meeting circulated forward `[current]`
- `weekly-update` - team or department weekly summary `[v3-new]`
- `all-hands-summary` - recap of an all-hands meeting `[v3-new]`
- `quarterly-review` - quarter-end retrospective and forward look `[v3-new]`
- `sprint-recap` - end-of-sprint summary `[v3-new]`
- `dashboard-narrative` - prose accompanying a data dashboard `[v3-new]`

#### `brief` family

Writing whose purpose is to compress a proposal, summary, or framing into a small, dense, decision-supporting artifact.

- `one-pager` - single-page brief `[current]`
- `talk-abstract` - talk or session description `[v1-candidate]`
- `conference-proposal` - CFP submission `[v1-candidate]`
- `cover-letter` - job application cover letter `[v2-candidate]`
- `proposal-cover-letter` - cover letter for a sales or grant proposal `[v2-candidate]`
- `executive-brief` - briefing memo prepared for executive review `[v2-candidate]`
- `pitch-deck-narrative` - prose backing of a pitch deck `[v3-new]`
- `business-case` - structured argument for a project or investment `[v3-new]`
- `project-charter` - kickoff document defining project scope `[v3-new]`
- `discovery-brief` - early-stage problem-framing brief `[v3-new]`

#### `appraisal` family

Writing whose purpose is to evaluate a person's work, performance, or fit.

- `performance-review` - periodic performance review `[v1-candidate]`
- `peer-feedback-note` - peer-to-peer feedback `[v1-candidate]`
- `360-feedback` - structured multi-source feedback `[v2-candidate]`
- `recommendation-letter` - letter recommending someone for a role `[v2-candidate]`
- `interview-rubric` - structured evaluation framework for candidates `[v2-candidate]`
- `exit-summary` - documentation of departure with learnings `[v2-candidate]`
- `job-description` - external job posting `[v2-candidate]`
- `code-review-comment` - inline review note on a PR `[v3-new]`
- `design-critique` - structured critique of a design artifact `[v3-new]`
- `promotion-justification` - written case for a promotion `[v3-new]`
- `manager-feedback-letter` - manager-to-direct feedback in writing `[v3-new]`

#### `messaging` family

Short two-way real-time-adjacent writing for known recipients or channels.

- `slack-message` - Slack post or thread reply `[current]`
- `email` - internal or external work email `[current]`
- `chat-message` - short conversational message in any work chat tool `[v3-new]`
- `dm` - direct message in any platform `[v3-new]`

#### `outreach` family

Writing that initiates contact with a recipient who has no prior relationship.

- `sales-email` - sales prospecting email `[v2-candidate]`
- `cold-outreach` - cold outreach for partnerships, hiring, or research `[v2-candidate]`
- `customer-success-email` - proactive customer success outreach `[v2-candidate]`
- `account-plan-email` - communication around a strategic account plan `[v3-new]`
- `partnership-pitch` - written pitch for a business partnership `[v3-new]`
- `expert-outreach` - cold outreach to an expert for advice or interview `[v3-new]`

#### `response` family

Writing produced in reply to inbound communication.

- `support-response` - reply to customer support ticket `[v2-candidate]`
- `refund-email` - written response handling refund or credit `[v2-candidate]`
- `escalation-reply` - response handling an escalation `[v2-candidate]`
- `customer-complaint-response` - reply to a formal complaint `[v3-new]`
- `legal-inquiry-response` - response to legal or compliance inquiry `[v3-new]`
- `media-inquiry-response` - response to a press question `[v3-new]`
- `pr-comment-reply` - reply to public commentary or review `[v3-new]`

### `public` domain

#### `broadcast` family

Writing for an open audience through a channel with its own conventions.

- `blog-post-long-form` - long blog post or essay `[current]`
- `newsletter-issue` - single newsletter edition `[v1-candidate]`
- `linkedin-post` - LinkedIn-native post `[v1-candidate]`
- `tweet-thread` - Twitter or X thread `[current]`
- `podcast-show-notes` - per-episode podcast show notes `[v1-candidate]`
- `youtube-video-description` - YouTube video description `[v3-new]`
- `substack-post` - Substack-native post `[v3-new]`
- `medium-article` - Medium-native article `[v3-new]`
- `instagram-caption` - Instagram caption `[v3-new]`
- `threads-post` - Threads-native post `[v3-new]`
- `mastodon-post` - Mastodon-native post `[v3-new]`
- `explainer-article` - explanatory long-form on a topic `[v3-new]`
- `deep-dive` - extended investigative or analytical piece `[v3-new]`
- `interview-article` - published interview write-up `[v3-new]`
- `listicle` - structured-list article format `[v3-new]`

#### `copy` family

Commercial-persuasion writing for marketing channels.

- `landing-page-copy` - hero and section copy for a landing page `[v2-candidate]`
- `ad-copy` - paid ad copy (search, social, display) `[v2-candidate]`
- `tagline` - product or brand tagline `[v2-candidate]`
- `email-marketing-copy` - copy for marketing email campaigns `[v3-new]`
- `product-description` - e-commerce product description `[v3-new]`
- `app-store-listing` - app store product page copy `[v3-new]`
- `brand-story` - narrative version of brand origin/purpose `[v3-new]`
- `case-study-marketing` - customer case study for marketing use `[v3-new]`
- `customer-story` - customer-centered story for marketing `[v3-new]`
- `pricing-page-copy` - copy for pricing/plans page `[v3-new]`

#### `position` family

Public writing that takes a stance or makes an argument.

- `op-ed` - opinion editorial `[v2-candidate]`
- `public-statement` - organizational public statement on an issue `[v2-candidate]`
- `advocacy-letter` - public letter advocating a position `[v2-candidate]`
- `testimony` - written testimony for hearings or proceedings `[v2-candidate]`
- `press-release` - organizational press release `[v2-candidate]`
- `endorsement` - public endorsement (political, professional, civic) `[v3-new]`
- `manifesto` - public declaration of principles `[v3-new]`
- `open-letter` - publicly addressed letter to a person, group, or institution `[v3-new]`
- `keynote-script` - script for a keynote address `[v3-new]`
- `boycott-or-protest-statement` - public protest or boycott declaration `[v3-new]`

#### `accountability` family

Writing produced in response to having broken something or caused harm publicly.

- `public-apology` - public apology statement `[v2-candidate]`
- `security-advisory` - public security disclosure `[v2-candidate]`
- `status-page-update` - status page incident update `[v2-candidate]`
- `recall-notice` - product recall notice `[v2-candidate]`
- `correction-notice` - editorial correction or retraction `[v3-new]`
- `incident-postmortem-public` - publicly published postmortem `[v3-new]`
- `data-breach-notification` - notification to affected users about a breach `[v3-new]`
- `policy-change-explanation` - public explanation of a controversial policy change `[v3-new]`

### `relational` domain

#### `correspondence` family

Personal letters, notes, and cards for someone the writer knows.

- `thank-you-note` - written thanks for a gift, favor, or kindness `[v2-candidate]`
- `condolence-note` - written sympathy on a death or loss `[v2-candidate]`
- `apology-letter` - written personal apology `[v2-candidate]`
- `personal-letter` - general personal letter `[v2-candidate]`
- `birthday-message` - written birthday note or card text `[v2-candidate]`
- `holiday-card` - holiday greeting card text `[v2-candidate]`
- `get-well-card` - get-well note text `[v3-new]`
- `sympathy-card` - sympathy card text (vs longer condolence note) `[v3-new]`
- `anniversary-card` - relationship anniversary card text `[v3-new]`
- `congratulations-note` - written congratulations on an achievement `[v3-new]`
- `christmas-letter` - annual family-update Christmas letter `[v3-new]`
- `catch-up-email` - personal email reconnecting with someone `[v3-new]`
- `personal-recommendation-letter` - letter recommending a friend `[v3-new]`
- `mentor-thank-you` - sustained note thanking a mentor `[v3-new]`
- `breakup-letter` - letter ending a romantic relationship `[v3-new]`
- `letter-to-future-self` - letter written for a later moment `[v3-new]`
- `letter-to-child` - parental letter to child for a milestone `[v3-new]`

#### `essay` family

Long-form personal writing addressed to a community of readers.

- `personal-essay` - first-person essay `[v2-candidate]`
- `memoir-excerpt` - memoir-form chapter or section `[v2-candidate]`
- `profile-piece` - written profile of another person `[v2-candidate]`
- `travel-writing` - travel essay or dispatch `[v2-candidate]`
- `vignette` - short scene or moment treated as standalone `[v3-new]`
- `micro-essay` - very short essay (under 500 words) `[v3-new]`
- `letter-essay` - essay framed as a letter `[v3-new]`
- `braided-essay` - essay weaving multiple threads `[v3-new]`
- `lyric-essay` - essay with lyric or poetic structure `[v3-new]`
- `flash-memoir` - very short autobiographical piece `[v3-new]`
- `food-writing` - first-person food essay or memoir `[v3-new]`
- `nature-essay` - first-person essay grounded in observation of nature `[v3-new]`

### `ceremonial` domain

#### `tribute` family

Occasion-bound speech that honors a person or transition.

- `eulogy` - funeral or memorial address `[v1-candidate]`
- `wedding-toast` - wedding or anniversary toast `[v1-candidate]`
- `retirement-speech` - speech at a retirement event `[v2-candidate]`
- `anniversary-letter` - letter for a relationship anniversary `[v2-candidate]`
- `graduation-speech` - commencement or graduation address `[v2-candidate]`
- `wedding-vows` - written vows for a marriage ceremony `[v3-new]`
- `valedictorian-speech` - valedictorian or salutatorian address `[v3-new]`
- `award-acceptance` - acceptance speech for an award `[v3-new]`
- `award-introduction` - introduction speech presenting an awardee `[v3-new]`
- `birthday-toast` - milestone birthday toast `[v3-new]`
- `welcome-speech` - speech welcoming new members, attendees, employees `[v3-new]`
- `farewell-speech` - speech marking someone's departure `[v3-new]`
- `obituary` - published obituary `[v3-new]`
- `memorial-tribute` - written tribute distinct from spoken eulogy `[v3-new]`
- `dedication` - dedication of a building, book, project, or initiative `[v3-new]`
- `oath-of-office` - written oath text for taking office `[v3-new]`

### `contemplative` domain

#### `devotion` family

Spiritual, devotional, or pastoral writing produced as discipline of formation or teaching.

- `devotional-entry` - daily or thematic devotional `[current]`
- `sermon` - sermon manuscript or notes `[v2-candidate]`
- `homily` - shorter sermon, typically liturgical `[v2-candidate]`
- `prayer` - written prayer for personal or communal use `[v2-candidate]`
- `meditation` - written meditation or contemplative reflection `[v2-candidate]`
- `lectionary-commentary` - commentary on assigned scripture readings `[v2-candidate]`
- `bible-study-notes` - structured notes for group bible study `[v3-new]`
- `theological-reflection` - reflection on a theological theme `[v3-new]`
- `spiritual-direction-letter` - letter from spiritual director to directee `[v3-new]`
- `discernment-notes` - notes from a discernment process `[v3-new]`
- `liturgical-prayer` - prayer composed for liturgical use `[v3-new]`
- `benediction` - blessing offered at end of gathering `[v3-new]`
- `examen-reflection` - daily examen reflection `[v3-new]`
- `lectio-divina-notes` - lectio divina reflection notes `[v3-new]`
- `breathwork-script` - guided breathwork or meditation script `[v3-new]`
- `retreat-talk` - talk given at a retreat `[v3-new]`
- `dharma-talk` - Buddhist dharma talk text `[v3-new]`

#### `journal` family

Private or semi-private reflective writing.

- `journal-entry` - personal journal entry `[v2-candidate]`
- `morning-pages` - stream-of-consciousness morning writing `[v2-candidate]`
- `gratitude-journal` - structured daily gratitude entry `[v3-new]`
- `commonplace-book-entry` - entry in a commonplace book `[v3-new]`
- `field-notes-personal` - personal field-notes-style observation `[v3-new]`
- `dream-journal-entry` - dream record `[v3-new]`

### Formats that do not yet fit any family

Used to surface taxonomy gaps. If items here cluster, they may indicate a missing family.

- (none identified at this pass; if `unfit` items accumulate during v3 review, they signal new families needed)

### Format count summary at expanded scale

- **professional**: deliberation 15, instruction 19, progress 12, brief 10, appraisal 11, messaging 4, outreach 6, response 7 = **84**
- **public**: broadcast 15, copy 10, position 10, accountability 8 = **43**
- **relational**: correspondence 17, essay 12 = **29**
- **ceremonial**: tribute 16 = **16**
- **contemplative**: devotion 17, journal 6 = **23**

**Total: ~195 format candidates** across 5 domains and 17 families (16 in v2 plus the new domains/families surface no new families - structure holds).

## Voice inventory

### `expert` family

Voices that signal deep practitioner knowledge.

- `pragmatic-architect` - the grounded, opinionated engineer `[current]`
- `technical-writer` - the clarifying documentarian `[current]`
- `researcher` - the curious investigator `[current]`
- `senior-consultant` - the seasoned outside advisor `[current]`
- `operator` - the runbook-and-on-call voice `[current]`
- `product-thinker` - the customer-and-tradeoffs voice `[current]`
- `ethicist` - the principled reasoner about right action `[v2-candidate]`
- `primer-author` - the patient beginner-explainer `[v2-candidate]`
- `artisan` - the deep craft voice tied to a making practice `[v2-candidate]`
- `curator` - the selective expert who frames what others made `[v2-candidate]`
- `scholar` - the academic-toned researcher-author `[v3-new]`
- `polymath` - the broadly-knowledgeable cross-discipline voice `[v3-new]`
- `analyst` - the data-grounded interpreter `[v3-new]`
- `strategist` - the long-view planner voice `[v3-new]`
- `clinician` - the case-grounded professional voice (consulting, medicine, therapy) `[v3-new]`

### `care` family

Voices oriented around tending to or accompanying other people.

- `coach` - the question-driven facilitator `[current]`
- `friendly-mentor` - the warm experienced guide `[current]`
- `caregiver` - the practical-compassion tender `[current]`
- `elder` - the generationally-seasoned voice `[v2-candidate]`
- `advocate` - the voice speaking for someone else's interest `[v2-candidate]`
- `chaplain` - the present-with-suffering voice `[v2-candidate]`
- `confidante` - the trusted-listener voice `[v3-new]`
- `peer-supporter` - the same-experience companion voice `[v3-new]`
- `healer` - the integrative wellness voice `[v3-new]`
- `family-elder` - the grandparent or auntie voice `[v3-new]`
- `godparent` - the moral-witness-from-outside-family voice `[v3-new]`

### `principal` family

Voices that speak from a defined role with positional clarity.

- `executive` - the senior-leader voice `[current]`
- `direct-communicator` - the plainspoken decisive voice `[current]`
- `defender` - the take-the-hit-publicly voice `[v2-candidate]`
- `spokesperson` - the speaks-on-behalf voice `[v2-candidate]`
- `founder` - the originator-with-vision voice `[v3-new]`
- `captain` - the in-charge-of-this-team voice `[v3-new]`
- `dignified-elder-leader` - the elder-statesperson voice `[v3-new]`
- `arbitrator` - the resolving-disputes voice `[v3-new]`
- `judge` - the rendering-decisions voice (formal or informal) `[v3-new]`

### `witness` family

Observational and narrative voices.

- `journalist` - the reporting-and-sourcing voice `[current]`
- `storyteller` - the narrative-arc voice `[current]`
- `columnist` - the recurring-perspective voice `[current]`
- `satirist` - the comic-critique voice `[v2-candidate]`
- `naturalist` - the close-observation-of-nature voice `[v2-candidate]`
- `historian` - the long-view chronicler voice `[v2-candidate]`
- `profiler` - the person-portrait voice `[v2-candidate]`
- `chronicler` - the recording-events voice `[v2-candidate]`
- `outsider` - the from-outside-the-room voice `[v2-candidate]`
- `insider-confidant` - the from-inside-the-room voice `[v2-candidate]`
- `ethnographer` - the participant-observer voice `[v3-new]`
- `biographer` - the long-arc-of-one-life voice `[v3-new]`
- `travel-writer` - the going-and-noticing voice `[v3-new]`
- `food-writer` - the eating-and-cooking voice `[v3-new]`
- `cultural-critic` - the reading-the-culture voice `[v3-new]`
- `tech-critic` - the reading-the-tech voice `[v3-new]`
- `observer` - the general-purpose noticing voice `[v3-new]`
- `eyewitness` - the I-was-there voice `[v3-new]`

### `dissident` family

Voices that challenge, contradict, or hold a position against prevailing sentiment.

- `contrarian` - the by-default-disagreeing voice `[v2-candidate]`
- `polemicist` - the sustained-argument-against voice `[v2-candidate]`
- `skeptic` - the show-me-the-evidence voice `[v2-candidate]`
- `whistleblower` - the from-inside-revealing voice `[v2-candidate]`
- `gadfly` - the persistent-needler voice `[v3-new]`
- `prophet-of-doom` - the warning-of-collapse voice `[v3-new]`
- `iconoclast` - the breaking-cherished-assumptions voice `[v3-new]`
- `dissenting-opinion` - the formal-disagreement-from-within voice `[v3-new]`

### `pastoral` family

Voices oriented around faith, formation, or pastoral care from within a tradition.

- `pastoral` - the shepherding voice `[current]`
- `prophet` - the speaking-truth-to-power tradition voice `[v2-candidate]`
- `mystic` - the contemplative-tradition voice `[v2-candidate]`
- `spiritual-director` - the formation-conversation voice `[v3-new]`
- `lay-teacher` - the from-the-pew teaching voice `[v3-new]`
- `retreat-leader` - the holding-the-space-for-retreat voice `[v3-new]`
- `liturgist` - the structured-worship-text voice `[v3-new]`

### Voices that do not yet fit any family

- (none identified; if items accumulate during v3 review, they signal new families needed)

### Voice count summary at expanded scale

- **expert**: 15
- **care**: 11
- **principal**: 9
- **witness**: 18
- **dissident**: 8
- **pastoral**: 7

**Total: ~68 voice candidates** across 6 families. Largest family (witness) is 18; smallest (pastoral) is 7. Average ~11 per family.

## Alphabetical indexes

### Formats (alphabetical)

A: accessibility-audit, ad-copy, adr, all-hands-summary, anniversary-card, anniversary-letter, api-doc, app-store-listing, apology-letter, architecture-doc, award-acceptance, award-introduction
B: benediction, bible-study-notes, birthday-message, birthday-toast, blog-post-long-form, board-memo, boycott-or-protest-statement, brand-story, braided-essay, breakup-letter, breathwork-script, business-case
C: case-study-marketing, catch-up-email, changelog-entry, chat-message, christmas-letter, code-review-comment, cold-outreach, commonplace-book-entry, condolence-note, conference-proposal, congratulations-note, correction-notice, cover-letter, curriculum-outline, customer-complaint-response, customer-story, customer-success-email
D: daily-standup, data-breach-notification, decision-memo, dedication, deep-dive, deprecation-notice, design-critique, design-doc, devotional-entry, dharma-talk, discernment-notes, discovery-brief, dm, dream-journal-entry
E: email, email-marketing-copy, endorsement, error-message, escalation-reply, eulogy, examen-reflection, executive-brief, expert-outreach, explainer-article
F: farewell-speech, faq, feature-spec, field-notes-personal, flash-memoir, food-writing
G: get-well-card, glossary, graduation-speech, gratitude-journal
H: holiday-card, homily, how-to-guide
I: incident-postmortem-public, instagram-caption, interview-article, interview-rubric
J: job-description, journal-entry
K: keynote-script
L: landing-page-copy, lectio-divina-notes, lectionary-commentary, legal-inquiry-response, lesson-plan, letter-essay, letter-to-child, letter-to-future-self, linkedin-post, listicle, liturgical-prayer, lyric-essay
M: manager-feedback-letter, manifesto, mastodon-post, media-inquiry-response, medium-article, meditation, meeting-notes, memoir-excerpt, memorial-tribute, mentor-thank-you, micro-essay, microcopy, morning-pages
N: nature-essay, newsletter-issue
O: oath-of-office, obituary, okr-update, one-pager, onboarding-walkthrough, op-ed, open-letter
P: partnership-pitch, peer-feedback-note, performance-review, personal-essay, personal-letter, personal-recommendation-letter, pitch-deck-narrative, podcast-show-notes, policy-change-explanation, policy-doc, position-paper, postmortem, pr-comment-reply, prayer, prd, press-release, pricing-page-copy, product-description, profile-piece, project-charter, promotion-justification, proposal-cover-letter, public-apology, public-statement
Q: quarterly-review
R: readme, recall-notice, recommendation-letter, refund-email, release-notes, retirement-speech, retreat-talk, rfc, risk-register, roadmap, runbook
S: sales-email, security-advisory, sermon, slack-message, sop, spiritual-direction-letter, sprint-recap, status-page-update, status-report, strategic-plan, study-guide, substack-post, support-response, swot-analysis, syllabus, sympathy-card
T: tagline, talk-abstract, technical-reference, testimony, theological-reflection, threads-post, thank-you-note, travel-writing, tutorial, tweet-thread
V: valedictorian-speech, vignette
W: wedding-toast, wedding-vows, weekly-update, welcome-speech, whitepaper
Y: youtube-video-description

### Voices (alphabetical)

A: advocate, analyst, arbitrator, artisan
B: biographer
C: captain, caregiver, chaplain, chronicler, clinician, coach, columnist, confidante, contrarian, cultural-critic, curator
D: defender, dignified-elder-leader, direct-communicator, dissenting-opinion
E: elder, ethicist, ethnographer, executive, eyewitness
F: family-elder, food-writer, founder, friendly-mentor
G: gadfly, godparent
H: healer, historian
I: iconoclast, insider-confidant
J: journalist, judge
L: lay-teacher, liturgist
M: mystic
N: naturalist
O: observer, operator, outsider
P: pastoral, peer-supporter, polymath, polemicist, pragmatic-architect, primer-author, product-thinker, profiler, prophet, prophet-of-doom
R: researcher, retreat-leader
S: satirist, scholar, senior-consultant, skeptic, spiritual-director, spokesperson, storyteller, strategist
T: tech-critic, technical-writer, travel-writer
W: whistleblower

## What to evaluate against this inventory

The v2 taxonomy should be evaluated against this inventory on five dimensions:

1. **Do the family names *feel right* against the actual members listed?** When you read "deliberation" and see adr, prd, design-doc, rfc, whitepaper, postmortem, position-paper, decision-memo, strategic-plan, board-memo, architecture-doc, feature-spec, roadmap, swot-analysis, risk-register - does "deliberation" land as the name for that group, or does another name suggest itself?
2. **Do the cuts hold up?** Are there entries you would move from one family to another? Entries you would not include at all? Entries that obviously belong but are missing?
3. **Are the domains right?** With professional swelling to 84 entries across 8 families, is `professional` still the right unit, or should it split? Is `relational` at 29 entries earning its keep as a domain?
4. **What does the inventory reveal about repo aspiration?** Looking at this list, does it match where you want the repo to go, or are areas over- or under-weighted?
5. **What names emerge naturally?** If you read the family contents and a different name pops into mind, that name is signal.

## What to do with this material

Three options once you've reviewed:

- **A.** Approve the v2 taxonomy as-is (the structure works at this scale); proceed to ADR 0010 sync and Phase 1.
- **B.** Revise names where they don't land but keep the cuts; produce a v3 of the taxonomy doc with renamed families.
- **C.** Re-cut the families (and/or domains) based on what the inventory reveals; produce a v3 with restructured taxonomy.

Or D: anything else suggested by reading the inventory.

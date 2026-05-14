---
title: Writing Style Library - Overbuilt v1 Execution Plan
slug: overbuilt-v1-execution-plan
date: 2026-05-09
status: draft-v1
authors: [jonathan]
artifact_type: execution-plan
companion_docs:
  - strategy-approach-roadmap_2026-05-08.md
  - value-delivery-approaches_2026-05-09.md
license: CC-BY-4.0
---

# Writing Style Library: Overbuilt v1 Execution Plan

> Maximalist scope. The opposite of a walking skeleton. Twelve-month timeline assuming sustained effort and at least one collaborator. Where the strategy brief recommended Phase 0 minimalism, this plan documents what a robust, broadly-spanning v1 actually looks like - so the user can see the cost honestly before committing.

---

## 0. How to use this document

This is a build-spec, not a strategy. It assumes the strategic question ("should we build this?") has already been answered yes, and answers the operational question ("what does v1 actually contain and how does it ship?").

The plan is structured so any single section can be deferred or scaled down without breaking the others. Treat it as a maximum-viable-product specification: every item below has a defensible reason to exist, but the plan as a whole is more than any solo maintainer should attempt without help.

---

## 1. v1 Vision and Scope

### 1.1 Headline numbers

| Dimension | v1 target |
|---|---|
| Voice entries | 80 |
| Tone entries | 50 |
| Style entries | 60 |
| Format entries | 100 |
| Anchor topics for vertical slices | 5 |
| Horizontal-slice recipe combinations | 50 |
| Diff-pair examples | 30 |
| Total example files | ~1,750 |
| Surfaces shipped | 6 (Skill Pack, Composer, TS SDK, Python SDK, MCP server, Eval Harness) |
| Static site pages | ~400 (auto-generated from frontmatter + manual editorial) |
| Browser extension | Stretch goal, Phase 4 |
| Timeline target | 12 months |
| Capacity assumed | Maintainer + 1 part-time contributor + LLM authoring loop |

### 1.2 What "robust" means here

- Every entry has full frontmatter populated to reference-quality.
- Every entry has at least one human-reviewed example.
- Cross-references (`pairs_well_with`, `avoid_with`, `confusable_with`) are populated for every entry, with reciprocal validation in CI.
- Every entry includes anti-pattern guidance and confusables.
- Every format entry has a `canonical_template`.
- Every voice entry has `language_patterns` (5+) and `llm_instruction_phrasing`.
- Every example file has `author_type`, `llm_model`, `llm_prompt_file`, and `review_status` populated.
- The repo passes schema validation, cross-reference validation, the no-em-dash linter, markdown linting, and link checking on every PR.
- All six surfaces stay in sync because they read the same build-artifact JSON.

### 1.3 What "overbuilt" means here

It means deliberately exceeding the lean recommendation in the companion strategy brief, on the assumption that the maintainer wants a complete reference work rather than an MVP that proves the concept. The cost trade is high: roughly 10x the content work and 4x the engineering work compared to the Phase 0/Phase 1 plan in the strategy brief.

---

## 2. The Catalog: Full Entry Lists

This section enumerates every entry to be authored for v1. Treat it as the build manifest for the content team.

### 2.1 Voices (target: 80)

#### 2.1.1 Professional and Authoritative (10)

1. `executive` - Decisive, big-picture, results-focused.
2. `senior-consultant` - Diagnostic, framework-driven, polished.
3. `industry-analyst` - Detached, comparative, market-aware.
4. `pragmatic-architect` - Tradeoff-oriented, calmly opinionated.
5. `operator` - Hands-on, accountability-driven, no-nonsense.
6. `general-counsel` - Cautious, precedent-aware, risk-flagging.
7. `cfo-financial` - Number-anchored, capital-allocation framed.
8. `chief-of-staff` - Coordinative, cross-functional, tact-led.
9. `program-manager` - Sequencing, dependency-aware, cadence-led.
10. `principal-engineer` - Deeply technical, mentor-shaped, opinionated about quality.

#### 2.1.2 Mentor and Coach (8)

11. `friendly-mentor` - Warm, patient, growth-oriented.
12. `tough-love-coach` - Direct, demanding, caring underneath.
13. `patient-teacher` - Step-by-step, scaffolding, encouraging.
14. `socratic-tutor` - Question-led, draws out reasoning.
15. `sage-elder` - Reflective, slow-paced, story-led.
16. `peer-collaborator` - Equals-talking-shop, low-hierarchy.
17. `executive-coach` - Outcome-focused, calibrated, accountability-led.
18. `learning-and-development` - Curriculum-aware, retention-conscious.

#### 2.1.3 Scholarly and Intellectual (8)

19. `academic` - Citation-laden, hedged, methodologically careful.
20. `public-intellectual` - Synthesizing, opinionated, accessible.
21. `theoretician` - Abstract, system-building, conjecture-friendly.
22. `historian` - Narrative, contextual, causation-tracking.
23. `critic` - Discriminating, comparative, evaluative.
24. `philosopher` - First-principles, conceptual, definitional.
25. `popular-science-explainer` - Metaphor-rich, anti-jargon, curious.
26. `essayist` - Voice-led inquiry, personal-and-intellectual.

#### 2.1.4 Storyteller and Literary (10)

27. `literary-novelist` - Character-driven, prose-forward, theme-led.
28. `memoirist` - First-person reflective, mining personal experience.
29. `folk-storyteller` - Oral cadence, repetition, archetypal.
30. `hardboiled-narrator` - Terse, cynical, sensory.
31. `gothic-narrator` - Atmospheric, foreboding, ornate.
32. `lyrical-beat` - Rhythmic, breath-driven, image-stacked.
33. `magical-realist` - Mundane-with-impossible, quietly accepted.
34. `satirist` - Ironic, exaggerating-to-expose, serious-underneath.
35. `young-adult-narrator` - Earnest, identity-exploring, accessible.
36. `picture-book-author` - Concrete, image-led, repetition-friendly.

#### 2.1.5 Journalist and Investigator (6)

37. `investigative-reporter` - Skeptical, evidence-chained, document-aware.
38. `beat-reporter` - Factual, timely, source-driven.
39. `feature-writer` - Narrative, scene-setting, character-led.
40. `columnist` - Voice-forward, recurring perspective, opinionated.
41. `explainer-journalist` - Patient, definition-rich, no-assumptions.
42. `op-ed-writer` - Argument-led, current-events anchored.

#### 2.1.6 Spiritual and Pastoral (8)

43. `pastor` - Caring, scriptural, application-oriented.
44. `theologian` - Doctrinally precise, exegetical, careful.
45. `mystic-contemplative` - Image-rich, paradoxical, slow.
46. `devotional-writer` - Personal, scriptural, prayerful.
47. `prophetic-voice` - Convicted, urgent, calling to action.
48. `spiritual-director` - Listening, discerning, gentle-questioning.
49. `chaplain` - Pluralistic, presence-led, comfort-oriented.
50. `liturgical-curator` - Communal, rhythmic, tradition-rooted.

#### 2.1.7 Persuader and Advocate (7)

51. `marketer` - Benefit-led, audience-aware, action-oriented.
52. `evangelist` - Visionary, energized, recruiting.
53. `activist` - Moralized, urgent, change-demanding.
54. `salesperson` - Relational, objection-handling, closing.
55. `lawyer-advocate` - Argumentative, precedent-citing, adversarial.
56. `policy-advocate` - Stakeholder-aware, evidence-led, coalition-building.
57. `fundraiser` - Story-led, urgency-balanced, gratitude-foregrounded.

#### 2.1.8 Conversational and Personal (7)

58. `best-friend` - Casual, frank, supportive.
59. `hype-friend` - Exclamatory, affirming, energy-boosting.
60. `confidant` - Quiet, listening, reflection-drawing.
61. `bro-dudespeak` - Loose, slang-heavy, low-stakes.
62. `big-sibling` - Warm, slightly teasing, protective.
63. `parent-to-parent` - Practical, lived-experience-aware, nonjudgmental.
64. `late-night-radio-host` - Intimate, thoughtful, slow-paced.

#### 2.1.9 Cultural, Regional, and Demographic (8)

65. `valley-girl` - Slangy, expressive, hedge-rich.
66. `surfer-socal` - Mellow, present-tense, vibe-led.
67. `new-yorker-fast` - Blunt, sardonic, fast.
68. `southern-folksy` - Storytelling cadence, idiomatic, courteous.
69. `british-dry-wit` - Understated, ironic, polite-with-edges.
70. `aussie-larrikin` - Direct, irreverent, informal.
71. `internet-native` - Meme-fluent, ironic, layered.
72. `startup-casual` - Fast, optimistic, action-biased.

#### 2.1.10 Generational (4)

73. `gen-z` - Internet-fluent, ironic, post-irony aware.
74. `millennial` - Self-aware, pop-culture-laden, semi-earnest.
75. `gen-x` - Skeptical, dry, allergic to corporate-speak.
76. `boomer` - Direct, principled, complete-sentence.

#### 2.1.11 Eccentric and Distinctive (4)

77. `eccentric-professor` - Tangent-prone, brilliant, beloved.
78. `mad-genius-inventor` - Excitable, leap-prone, half-finished.
79. `curmudgeon` - Grumbling, dryly funny, secretly principled.
80. `trickster-provocateur` - Subversive, assumption-flipping, gap-playing.

### 2.2 Tones (target: 50)

Organized by spectrum, with neutrals and named extremes.

#### 2.2.1 Confidence axis (6)

1. `authoritative`
2. `confident`
3. `tentative`
4. `humble`
5. `assertive`
6. `deferential`

#### 2.2.2 Warmth axis (6)

7. `warm`
8. `cool`
9. `cold-detached`
10. `affectionate`
11. `aloof`
12. `empathic`

#### 2.2.3 Energy axis (6)

13. `energetic`
14. `calm`
15. `urgent`
16. `subdued`
17. `excited`
18. `measured`

#### 2.2.4 Formality axis (5)

19. `formal`
20. `conversational`
21. `casual`
22. `stiff`
23. `intimate`

#### 2.2.5 Emotional register (10)

24. `joyful`
25. `somber`
26. `melancholy`
27. `hopeful`
28. `anxious`
29. `reassuring`
30. `mournful`
31. `reverent`
32. `nostalgic`
33. `defiant`

#### 2.2.6 Rhetorical posture (8)

34. `direct`
35. `indirect`
36. `diplomatic`
37. `blunt`
38. `provocative`
39. `conciliatory`
40. `candid`
41. `guarded`

#### 2.2.7 Stance toward subject (9)

42. `encouraging`
43. `skeptical`
44. `critical`
45. `supportive`
46. `challenging`
47. `curious`
48. `playful`
49. `serious`
50. `reverential`

### 2.3 Styles / Modes / Genres (target: 60)

#### 2.3.1 Classical rhetorical modes (15)

1. `chronological-narration`
2. `flashback-narration`
3. `in-medias-res`
4. `frame-narrative`
5. `sensory-description`
6. `spatial-description`
7. `character-sketch`
8. `mood-piece-description`
9. `technical-description`
10. `classical-argument` (Toulmin)
11. `rogerian-argument`
12. `polemic`
13. `apologetic`
14. `manifesto`
15. `reflective-essay`

#### 2.3.2 Exposition sub-modes (10)

16. `classification`
17. `definition`
18. `process-explanation`
19. `comparison-contrast`
20. `cause-and-effect`
21. `illustration-exemplification`
22. `analysis`
23. `synthesis`
24. `evaluation`
25. `problem-solution`

#### 2.3.3 Diátaxis modes (4)

26. `diataxis-tutorial`
27. `diataxis-howto`
28. `diataxis-reference`
29. `diataxis-explanation`

#### 2.3.4 Fiction genres (10)

30. `literary-fiction`
31. `mystery-detective`
32. `thriller-suspense`
33. `science-fiction`
34. `fantasy`
35. `horror`
36. `romance`
37. `historical-fiction`
38. `magical-realism-genre`
39. `coming-of-age`

#### 2.3.5 Non-fiction approaches (10)

40. `memoir-personal-essay`
41. `biography-profile`
42. `journalism-longform`
43. `investigative-nonfiction`
44. `popular-science-genre`
45. `philosophy-genre`
46. `theology-religious-nonfiction`
47. `cultural-criticism`
48. `travel-writing`
49. `nature-outdoor-writing`

#### 2.3.6 Professional / business approaches (6)

50. `technical-writing-style`
51. `business-writing-style`
52. `strategic-style`
53. `operational-style`
54. `marketing-style`
55. `executive-communication-style`

#### 2.3.7 Specialized writing modes (5)

56. `liturgical-style`
57. `devotional-style`
58. `exegetical-style`
59. `homiletic-style`
60. `confessional-style`

### 2.4 Formats (target: 100)

#### 2.4.1 Long-form documents (10)

1. `blog-post-long-form`
2. `pillar-page`
3. `magazine-article`
4. `essay`
5. `whitepaper`
6. `research-report`
7. `annual-report`
8. `book-chapter`
9. `field-guide`
10. `state-of-the-x-report`

#### 2.4.2 Short-form communications (12)

11. `email-transactional`
12. `email-longform`
13. `email-newsletter-issue`
14. `cold-email`
15. `slack-message`
16. `slack-thread-reply`
17. `text-sms`
18. `linkedin-post`
19. `tweet-x-post`
20. `twitter-thread`
21. `instagram-caption`
22. `dm-direct-message`

#### 2.4.3 Product, engineering, design (16)

23. `prd`
24. `rfc`
25. `adr`
26. `decision-register-entry`
27. `tech-spec`
28. `design-doc`
29. `postmortem-incident-report`
30. `runbook`
31. `playbook`
32. `style-guide-document`
33. `roadmap`
34. `okr-goals-doc`
35. `user-story`
36. `acceptance-criteria-list`
37. `creative-brief`
38. `project-charter`

#### 2.4.4 Marketing and content (12)

39. `listicle-thin`
40. `listicle-expanded`
41. `comparison-vs-post`
42. `roundup-best-of`
43. `faq-post`
44. `case-study-marketing`
45. `landing-page-copy`
46. `sales-page-longform`
47. `press-release`
48. `op-ed-format`
49. `how-to-tutorial-post`
50. `explainer-post`

#### 2.4.5 Sales formats (5)

51. `pitch-deck`
52. `sales-script`
53. `proposal-sow`
54. `discovery-questionnaire`
55. `objection-handling-sheet`

#### 2.4.6 Internal and leadership (8)

56. `town-hall-script`
57. `all-hands-deck`
58. `manager-update`
59. `team-newsletter`
60. `onboarding-doc`
61. `career-ladder-doc`
62. `performance-review`
63. `quarterly-business-review`

#### 2.4.7 Educational (8)

64. `lesson-plan`
65. `worksheet`
66. `quiz-test`
67. `curriculum-outline`
68. `course-module`
69. `lab-guide`
70. `study-guide`
71. `discussion-guide`

#### 2.4.8 Reference and data (10)

72. `glossary`
73. `cheat-sheet`
74. `quick-reference-card`
75. `index`
76. `comparison-matrix`
77. `decision-tree-text`
78. `checklist`
79. `timeline`
80. `spec-sheet`
81. `risk-register`

#### 2.4.9 Creative (10)

82. `short-story`
83. `flash-fiction`
84. `novella-outline`
85. `novel-beat-sheet`
86. `screenplay-scene`
87. `stage-play-scene`
88. `audio-drama-script`
89. `monologue`
90. `dialogue-scene`
91. `vignette`

#### 2.4.10 Visual / structured presentation (4)

92. `slide-deck`
93. `infographic-copy`
94. `mind-map`
95. `storyboard`

#### 2.4.11 Theological and devotional (5)

96. `sermon-manuscript`
97. `sermon-outline`
98. `devotional-entry`
99. `bible-study-guide`
100. `liturgy-order-of-service`

---

## 3. Anchor Topics for Vertical Slices

Five anchor topics, deliberately diverse, each rendered through every entry in the catalog. With 80 + 50 + 60 + 100 = 290 entries and 5 anchor topics, the vertical-slice corpus is **1,450 example files** at full coverage. Realistic v1 target: each entry gets at least one anchor topic rendering, plus optional second renderings for the most popular voices/formats. Practical example total: approximately **1,000 vertical-slice files**.

| # | Topic | Slug | Why it earns a slot |
|---|---|---|---|
| 1 | Should we adopt async-first standups? | `async-standups` | Professional, opinion-bearing, ADR/RFC fit, has personal/spiritual stretches. |
| 2 | How to start a morning routine | `morning-routine` | Personal, accessible across all voices, naturally renders short. |
| 3 | The discipline of rest | `discipline-of-rest` | Spiritual-first, exceptional for pastoral/devotional, stretches operator/architect productively. |
| 4 | Choosing between Postgres and DynamoDB for a new service | `db-choice` | Technical-first, exceptional for architect/operator, stretches storyteller voices into useful failure modes. |
| 5 | Saying goodbye to a longtime colleague | `farewell-colleague` | Emotional, fits memoirist/pastoral/columnist beautifully, stretches business voices into care. |

### 3.1 Per-anchor rendering plan

For each anchor topic, the production pipeline produces:

- One vertical slice per voice (80 files).
- One vertical slice per tone, against a default voice (50 files).
- One vertical slice per style, against a default voice and tone (60 files).
- One vertical slice per format, against a default voice, tone, and style (100 files).

That is **290 example files per anchor topic** at full coverage. Five anchors = **1,450 files**.

To make this tractable, the v1 plan staggers anchors:
- Anchor 1 (async-standups): full coverage. 290 files.
- Anchor 2 (morning-routine): full coverage. 290 files.
- Anchor 3 (discipline-of-rest): voice and format coverage only (180 files).
- Anchor 4 (db-choice): voice and format coverage only (180 files).
- Anchor 5 (farewell-colleague): voice and format coverage only (180 files).

**Total v1 vertical slice files: ~1,120.**

---

## 4. Horizontal-Slice Recipe Library (target: 50)

A "recipe" is a named combination of one voice, one tone, one style, and one format, rendered across multiple topics. Recipes are the front door for users who do not want to compose from primitives.

### 4.1 Professional recipes (12)

1. `architect-adr` - pragmatic-architect + matter-of-fact + problem-solution + adr.
2. `architect-rfc` - pragmatic-architect + candid + comparison-contrast + rfc.
3. `architect-design-doc` - pragmatic-architect + measured + analysis + design-doc.
4. `executive-strategy-memo` - executive + confident + synthesis + magazine-article.
5. `consultant-prd` - senior-consultant + matter-of-fact + problem-solution + prd.
6. `operator-runbook` - operator + direct + process-explanation + runbook.
7. `operator-postmortem` - operator + candid + cause-and-effect + postmortem-incident-report.
8. `pm-launch-brief` - program-manager + measured + synthesis + magazine-article.
9. `analyst-market-report` - industry-analyst + matter-of-fact + comparison-contrast + research-report.
10. `principal-tech-spec` - principal-engineer + measured + technical-description + tech-spec.
11. `cfo-quarterly-narrative` - cfo-financial + measured + cause-and-effect + quarterly-business-review.
12. `general-counsel-policy-memo` - general-counsel + cautious + classification + manager-update.

### 4.2 Mentor / Educational recipes (8)

13. `mentor-tutorial` - friendly-mentor + encouraging + diataxis-tutorial + how-to-tutorial-post.
14. `mentor-onboarding` - friendly-mentor + warm + process-explanation + onboarding-doc.
15. `coach-1on1-prep` - executive-coach + candid + analysis + email-longform.
16. `tutor-lesson-plan` - patient-teacher + encouraging + diataxis-tutorial + lesson-plan.
17. `socratic-discussion-guide` - socratic-tutor + curious + classical-argument + discussion-guide.
18. `sage-essay` - sage-elder + reflective + reflective-essay + essay.
19. `popular-science-explainer-post` - popular-science-explainer + curious + illustration-exemplification + explainer-post.
20. `essayist-newsletter` - essayist + reflective + reflective-essay + email-newsletter-issue.

### 4.3 Pastoral / Spiritual recipes (10)

21. `pastoral-devotional` - pastor + warm + devotional-style + devotional-entry.
22. `pastor-sermon-manuscript` - pastor + reverent + homiletic-style + sermon-manuscript.
23. `pastor-funeral-homily` - pastor + hopeful-sober + reflective-essay + sermon-manuscript.
24. `theologian-bible-study` - theologian + measured + exegetical-style + bible-study-guide.
25. `mystic-contemplative-reflection` - mystic-contemplative + reverent + reflective-essay + devotional-entry.
26. `devotional-writer-prayer` - devotional-writer + reverent + confessional-style + devotional-entry.
27. `prophetic-call-to-action` - prophetic-voice + urgent + manifesto + op-ed-format.
28. `chaplain-care-note` - chaplain + warm + reflective-essay + email-longform.
29. `liturgical-order-of-service` - liturgical-curator + reverent + liturgical-style + liturgy-order-of-service.
30. `youth-ministry-lesson` - friendly-mentor + encouraging + diataxis-tutorial + lesson-plan.

### 4.4 Marketing / Persuasion recipes (8)

31. `marketer-landing-page` - marketer + enthusiastic + persuasion + landing-page-copy.
32. `marketer-case-study` - marketer + measured + illustration-exemplification + case-study-marketing.
33. `evangelist-keynote` - evangelist + energetic + manifesto + slide-deck.
34. `salesperson-cold-email` - salesperson + warm + persuasion + cold-email.
35. `activist-op-ed` - activist + urgent + polemic + op-ed-format.
36. `fundraiser-appeal-letter` - fundraiser + hopeful + persuasion + email-longform.
37. `policy-advocate-position-paper` - policy-advocate + measured + classical-argument + whitepaper.
38. `lawyer-advocate-brief` - lawyer-advocate + formal + classical-argument + whitepaper.

### 4.5 Storyteller / Literary recipes (6)

39. `novelist-short-story` - literary-novelist + reverent + literary-fiction + short-story.
40. `memoirist-personal-essay` - memoirist + reflective + memoir-personal-essay + essay.
41. `journalist-feature` - feature-writer + curious + journalism-longform + magazine-article.
42. `columnist-blog-post` - columnist + candid + reflective-essay + blog-post-long-form.
43. `noir-flash-fiction` - hardboiled-narrator + cool + literary-fiction + flash-fiction.
44. `young-adult-chapter` - young-adult-narrator + warm + coming-of-age + book-chapter.

### 4.6 Conversational and Social recipes (6)

45. `friend-slack-explainer` - best-friend + casual + diataxis-explanation + slack-message.
46. `parent-text-thread` - parent-to-parent + warm + diataxis-howto + text-sms.
47. `colleague-linkedin-update` - peer-collaborator + measured + reflective-essay + linkedin-post.
48. `valley-girl-instagram` - valley-girl + casual + reflective-essay + instagram-caption.
49. `internet-native-thread` - internet-native + playful + reflective-essay + twitter-thread.
50. `startup-casual-launch-tweet` - startup-casual + enthusiastic + reflective-essay + tweet-x-post.

---

## 5. Diff-Pair Library (target: 30)

Diff-pairs hold three of four axes constant and vary one. They are the catalog's tutorial mode.

### 5.1 Voice diff-pairs (10)

1. `architect-vs-operator` (same topic, ADR format) - design-level vs in-the-weeds.
2. `architect-vs-academic` - decisive opinion vs hedged claims.
3. `pastor-vs-theologian` - applicational vs doctrinal.
4. `mentor-vs-coach` - asking vs telling.
5. `journalist-vs-essayist` - reported vs voice-led.
6. `marketer-vs-analyst` - benefit-led vs pattern-spotting.
7. `executive-vs-program-manager` - outcome-focused vs sequencing-focused.
8. `boomer-vs-gen-z` - same topic, generational register shift.
9. `british-vs-aussie` - same topic, regional register shift.
10. `literary-vs-genre-novelist` - prose-forward vs convention-led.

### 5.2 Tone diff-pairs (8)

11. `warm-vs-cold` (same voice, same format).
12. `confident-vs-tentative`.
13. `direct-vs-diplomatic`.
14. `urgent-vs-calm`.
15. `formal-vs-casual`.
16. `joyful-vs-somber`.
17. `encouraging-vs-critical`.
18. `serious-vs-playful`.

### 5.3 Style diff-pairs (6)

19. `narration-vs-exposition` - same voice, same format.
20. `classical-argument-vs-rogerian`.
21. `diataxis-tutorial-vs-howto`.
22. `comparison-contrast-vs-cause-effect`.
23. `analysis-vs-synthesis`.
24. `polemic-vs-apologetic`.

### 5.4 Format diff-pairs (6)

25. `adr-vs-rfc` - same voice, tone, style.
26. `listicle-vs-essay`.
27. `slack-message-vs-email`.
28. `pitch-deck-vs-whitepaper`.
29. `tweet-thread-vs-blog-post`.
30. `sermon-manuscript-vs-sermon-outline`.

---

## 6. Repository Architecture

```
writing-style-library/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── LICENSE                          # Apache-2.0
├── NOTICE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── GOVERNANCE.md
├── ROADMAP.md
├── CHANGELOG.md
├── llms.txt
├── mkdocs.yml
├── package.json                     # for the SDK and Composer
├── pyproject.toml                   # for the Python SDK
├── .editorconfig
├── .gitignore
├── .gitattributes
│
├── .claude-plugin/
│   ├── marketplace.json
│   └── plugin.json
│
├── taxonomy/
│   ├── voices/                      # 80 entries, atomic-folder pattern
│   │   ├── pragmatic-architect/
│   │   │   ├── ENTRY.md
│   │   │   ├── examples/
│   │   │   └── anti-examples/
│   │   └── ... (79 more)
│   ├── tones/                       # 50 entries
│   ├── styles/                      # 60 entries
│   └── formats/                     # 100 entries
│
├── examples/
│   ├── README.md
│   ├── vertical-slices/
│   │   ├── async-standups/
│   │   ├── morning-routine/
│   │   ├── discipline-of-rest/
│   │   ├── db-choice/
│   │   └── farewell-colleague/
│   ├── horizontal-slices/
│   │   └── ... (50 recipe folders)
│   └── diff-pairs/
│       └── ... (30 pair folders)
│
├── schemas/
│   ├── entry.universal.schema.json
│   ├── voice.schema.json
│   ├── tone.schema.json
│   ├── style.schema.json
│   ├── format.schema.json
│   ├── example.schema.json
│   └── recipe.schema.json
│
├── skills/
│   └── writing-instruction-builder/
│       ├── SKILL.md
│       ├── README.md
│       └── scripts/
│           └── build-instruction.py
│
├── recipes/
│   ├── architect-adr.yaml
│   └── ... (49 more)
│
├── packages/
│   ├── ts-sdk/                      # @product-on-purpose/writing-style-library
│   ├── py-sdk/                      # product-on-purpose-writing-style-library
│   ├── mcp-server/                  # standalone Cloudflare Worker
│   ├── composer-app/                # Vite + React SPA
│   └── browser-extension/           # Phase 4 stretch
│
├── docs/
│   ├── index.md
│   ├── concepts/
│   │   ├── three-axis-model.md
│   │   ├── composition.md
│   │   └── glossary.md
│   ├── how-to/
│   │   ├── compose-instruction.md
│   │   ├── pick-voice.md
│   │   ├── add-entry.md
│   │   └── run-eval.md
│   ├── reference/
│   │   ├── voices/                  # auto-generated
│   │   ├── tones/                   # auto-generated
│   │   ├── styles/                  # auto-generated
│   │   ├── formats/                 # auto-generated
│   │   └── recipes/                 # auto-generated
│   ├── design-standards/
│   │   ├── voice-and-tone.md
│   │   ├── output-templates.md
│   │   ├── naming-conventions.md
│   │   ├── description-style.md
│   │   └── style-tells.md
│   ├── governance/
│   │   ├── contribution-process.md
│   │   ├── review-criteria.md
│   │   └── deprecation-policy.md
│   └── internal/                    # this folder, holding strategy docs
│
├── tools/
│   ├── validate.py
│   ├── build-indexes.py
│   ├── generate-example.py
│   ├── promote-example.py
│   ├── run-evals.py
│   └── render-llm-instruction.py
│
├── tests/
│   ├── fixtures/
│   ├── golden-outputs/
│   └── evals/
│       ├── voices/
│       ├── tones/
│       ├── styles/
│       └── formats/
│
├── adr/
│   ├── 0001-three-axis-model.md
│   ├── 0002-atomic-folder-pattern.md
│   ├── 0003-license-strategy.md
│   ├── 0004-voice-and-tone-as-paired-axis.md
│   ├── 0005-no-em-dash-rule.md
│   ├── 0006-anchor-topic-selection.md
│   ├── 0007-llm-example-author-policy.md
│   └── 0008-marketplace-publishing-strategy.md
│
└── .github/
    ├── workflows/
    │   ├── validate.yml
    │   ├── build-site.yml
    │   ├── release.yml
    │   └── eval-on-pr.yml
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.yml
    │   ├── new-entry-proposal.yml
    │   └── new-recipe-proposal.yml
    ├── PULL_REQUEST_TEMPLATE.md
    ├── CODEOWNERS
    └── dependabot.yml
```

---

## 7. Schema and Validation

### 7.1 Schema set

Six JSON Schemas live in `schemas/`:

1. `entry.universal.schema.json` - shared base.
2. `voice.schema.json` - extends base with `language_patterns`, `diction`, `sentence_style`, `default_pov`.
3. `tone.schema.json` - extends base with `spectrum`, `spectrum_position`, `nn_g_profile`, `markers`.
4. `style.schema.json` - extends base with `frame`, `structural_conventions`, `evidence_types`, `reader_contract`.
5. `format.schema.json` - extends base with `typical_length`, `canonical_template`, `typical_voices`, `typical_tones`.
6. `example.schema.json` - for example-file frontmatter.

### 7.2 Validation pipeline

CI runs (in order):

1. JSON Schema validation against `schemas/` for every `ENTRY.md` and example file frontmatter.
2. Cross-reference validation: every ID in `pairs_well_with`, `avoid_with`, `confusable_with`, `related`, `examples_index` resolves to an existing entry.
3. Reciprocity validation: if A says `pairs_well_with: B`, then B should say `pairs_well_with: A` (or be flagged for review).
4. Deprecation chain validation: `deprecated_in_favor_of` resolves to a `stable` entry.
5. Tag controlled-vocabulary check against `tag.controlled-list.json`.
6. Slug regex enforcement: `^[a-z][a-z0-9-]*[a-z0-9]$`.
7. No-em-dash linter on all prose fields and bodies.
8. No-style-tells warnings (Phase 3 onward) for predictable LLM phrasings.
9. Markdown lint via `markdownlint-cli2`.
10. Link check via `lychee`.
11. agentskills.io `skills-ref validate` on the bundled skill.
12. `claude plugin validate` on the plugin and marketplace manifests.

### 7.3 Pre-commit hooks

A `.pre-commit-config.yaml` enforces the same checks locally before push. Contributors get instant feedback rather than CI-cycle delay.

---

## 8. Surface Build-Out Plan

### 8.1 Skill Pack (Claude Code, Codex, Cursor)

**Location:** `skills/writing-instruction-builder/`

**Core utilities:**
- `compose-instruction(voice, tone, style, format, topic?, audience?)` - composes a prompt string.
- `apply-voice(text, voice, tone?)` - rewrites existing text in the named voice.
- `convert-format(text, from_format, to_format)` - converts between formats.
- `evaluate-against-entry(text, entry_id)` - judges adherence to an entry.
- `find-pairs(seed_id, criterion?)` - returns compatible IDs based on `pairs_well_with`.
- `suggest-recipe(topic, audience?)` - recommends a named recipe.

**Recipe invocations:** Each of the 50 recipes registers a callable name. `/writing-style-library:architect-adr` runs the recipe with the current topic.

**Bundled resources:** The full catalog ships as `skills/writing-instruction-builder/resources/taxonomy.json`, loaded on demand.

**Distribution:** Listed in agentskills.io marketplace + Claude Code plugin marketplace.

### 8.2 Composer Web App

**Stack:** Vite + React + TypeScript + Tailwind, deployed to Cloudflare Pages.

**Routes:**
- `/` - hero landing with three axis pickers and topic input.
- `/compose` - full Composer interface with live preview.
- `/recipes` - browsable recipe gallery with filters.
- `/explore` - diff-pair gallery for learning the taxonomy.
- `/voices/:id`, `/tones/:id`, `/styles/:id`, `/formats/:id` - per-entry deep pages with examples.
- `/audit` - paste-your-text doc auditor (Phase 3).
- `/personalize` - voice fingerprint flow (Phase 4).
- `/brand` - brand voice builder (Phase 4).

**Composer features (v1):**
- Three axis pickers with category filters and search.
- Live preview of composed instruction.
- Smart defaults driven by `pairs_well_with`.
- "Try a random good combination" button.
- Side-by-side comparison view.
- Bring-your-own-API-key live runs (Anthropic, OpenAI, Google).
- Citations on generated outputs.
- Copy-to-clipboard, export-to-Markdown, export-to-JSON.
- Save-and-share via URL state.
- Personal library (LocalStorage in v1, optional account in v2).

### 8.3 TypeScript SDK

**Package:** `@product-on-purpose/writing-style-library`

**API:**
```typescript
import {
  composeInstruction,
  getEntry,
  listEntries,
  findCompatible,
  loadRecipe,
  validateInstruction,
  voices,
  tones,
  styles,
  formats,
  recipes,
} from '@product-on-purpose/writing-style-library';
```

**Types:** Generated from JSON Schemas via `json-schema-to-typescript`.

**Bundle:** Tree-shakable, ESM and CJS, with the catalog embedded as a JSON build artifact.

**Distribution:** npm.

### 8.4 Python SDK

**Package:** `product-on-purpose-writing-style-library`

**API parity:** Same surface as TS SDK, idiomatic Python.

**Distribution:** PyPI.

### 8.5 MCP Server

**Hosting:** Cloudflare Worker primary; Fly.io fallback.

**Tools exposed:**
- `list_voices(filter?)`, `list_tones(filter?)`, `list_styles(filter?)`, `list_formats(filter?)`.
- `get_entry(axis, id)`.
- `compose_instruction({voice, tone, style, format, topic?, audience?})`.
- `find_examples({voice?, tone?, style?, format?, topic?})`.
- `suggest_combinations({seed, criterion})`.
- `apply_voice({text, voice, tone?})`.

**Distribution:** Listed in MCP server directories. Public hosted endpoint at `mcp.product-on-purpose.com/writing-style-library`.

### 8.6 Eval Harness

**Backbone:** Promptfoo, with custom graders.

**Per-entry rubrics:** Derived from `language_patterns` and `markers` fields. LLM-as-judge with structured scoring.

**Coverage:** Every voice, every format, every recipe.

**Reports:** Auto-published to `/evals` on the static site. Re-run on every model release.

**Models tested:** Claude Opus 4.7, Claude Sonnet 4.6, GPT-5.5, Gemini Pro 2.

### 8.7 Static Site (MkDocs Material)

**Content:**
- Concept pages (three-axis model, composition, glossary).
- Auto-generated reference (per-entry pages with full frontmatter rendered, examples linked).
- How-to guides.
- Design standards.
- Governance and contribution.
- Eval reports.

**Plugins:** mkdocs-material, mkdocs-jsonschema-plugin (custom), mkdocs-redirects, mkdocs-rss-plugin.

### 8.8 Browser Extension (stretch, Phase 4)

**Targets:** Chrome first, Firefox second.

**Functionality:** Hotkey on selected text in any web textarea opens a quick-pick of voices and tones, sends to API (BYO key), replaces selection.

**Domains pre-tuned:** gmail.com, slack.com, notion.so, docs.google.com, linkedin.com, twitter.com, mail.proton.me.

---

## 9. Content Production Pipeline

### 9.1 Authoring loop (per entry)

1. **Draft frontmatter.** Fill required + recommended fields. Status: `draft`.
2. **Draft body.** Use `templates/skill/ENTRY.md` as scaffold. ~600-1,200 words.
3. **Schema validation.** Local pre-commit catches structural errors.
4. **Cross-reference draft.** Populate `pairs_well_with` and `confusable_with` (rough first pass).
5. **Generate first example.** Render anchor topic 1 in this entry, save prompt and model.
6. **Self-review.** Read body and example. Tighten language. Remove hedging.
7. **Promote to `reviewed`.** Set frontmatter status. Adds entry to validation pool.
8. **Peer review.** Second reviewer (collaborator or maintainer-on-different-day) checks against checklist.
9. **Promote to `stable`.** Live in v1.
10. **Optional: promote to `reference-quality`.** Reserved for entries that received a third pass and have multiple anchor renderings.

### 9.2 LLM-assisted authoring

LLM-assisted authoring is the only way to reach the v1 example count. Pipeline:

1. **Prompt template per anchor topic per axis.** Stored in `tools/prompts/`.
2. **Batch generation.** `tools/generate-example.py` runs Claude Opus 4.7 against the catalog and produces draft examples.
3. **Auto-frontmatter.** The script populates `author_type: llm`, `llm_model`, `llm_prompt_file`, `generated_at`.
4. **Maintainer review.** Each draft requires `review_status: reviewed` before promotion.
5. **Promotion gate.** A draft is `stable` only after a human reads it and confirms voice fidelity.

### 9.3 Capacity planning

| Activity | Time per unit | Total | Notes |
|---|---|---|---|
| Hand-authoring an entry to `stable` | 90 minutes | 290 entries x 90 min = 435 hours | Includes frontmatter, body, cross-refs. |
| LLM-generating an example | 5 minutes (incl. prompt) | 1,120 examples x 5 min = 93 hours | Automated batch, light review. |
| Reviewing an LLM example | 10 minutes | 1,120 x 10 = 187 hours | The bottleneck. |
| Authoring a recipe | 45 minutes | 50 x 45 = 38 hours | Frontmatter + 3 topic instantiations. |
| Authoring a diff-pair | 60 minutes | 30 x 60 = 30 hours | Two examples + explanation. |
| Engineering: SDKs | 80 hours each | 160 hours | TS + Python parity. |
| Engineering: MCP server | 40 hours | 40 hours | Cloudflare Worker. |
| Engineering: Composer | 200 hours | 200 hours | The polish-heavy item. |
| Engineering: Eval harness | 120 hours | 120 hours | Rubrics + Promptfoo wiring. |
| Engineering: Skill Pack | 60 hours | 60 hours | Tools + recipes + integration. |
| Engineering: Static site | 60 hours | 60 hours | MkDocs config + custom plugins. |
| Documentation set | 80 hours | 80 hours | All design-standards + governance docs. |
| Total | | ~1,500 hours | At 20 hours/week: 75 weeks. At 40 hours/week: 38 weeks. |

The 12-month timeline assumes 30+ hours per week of consistent effort across maintainer + contributor + LLM-assisted batch generation.

---

## 10. Quality Gates and Governance

### 10.1 Promotion gates

- `draft` (private, work-in-progress)
- `reviewed` (passes schema, has at least one human review)
- `stable` (public, indexed, in build artifacts)
- `reference-quality` (multi-anchor, multi-reviewer, used in eval harness)
- `deprecated` (kept but flagged)

### 10.2 Review checklist (per entry)

- Frontmatter required fields populated.
- `one_liner` is 1-2 sentences and stands alone.
- `pairs_well_with` and `avoid_with` have at least 3 entries each.
- `confusable_with` distinguishes from at least 2 nearby entries.
- `language_patterns` (voice) or `markers` (tone) or `structural_conventions` (style) or `canonical_template` (format) is concrete and observable.
- `when_to_use` and `when_not_to_use` each have at least 3 items.
- `llm_instruction_phrasing` is one paragraph, ready to copy.
- Body teaches a procedure, not a definition.
- Body has no em-dashes, no en-dashes, no LLM-tells.
- At least one anchor-topic example is committed.

### 10.3 Governance documents

- `GOVERNANCE.md` - maintainers, decision authority, release authority.
- `CODEOWNERS` - review routing.
- `CONTRIBUTING.md` - PR rules, dev loop, validation steps.
- `docs/governance/contribution-process.md` - how to propose entries and recipes.
- `docs/governance/review-criteria.md` - explicit grading criteria.
- `docs/governance/deprecation-policy.md` - how long an entry stays after replacement.

### 10.4 Release governance

- SemVer at the plugin layer.
- Keep a Changelog format.
- Releases tagged via `claude plugin tag --push`.
- Minor releases: new entries, new recipes, new examples.
- Major releases: schema changes, breaking renames, axis-level structural changes.
- Deprecated entries kept for two minor releases minimum.

---

## 11. Release Plan and Timeline (12 months)

The plan assumes a kickoff date of 2026-05-12 and a v1.0.0 target of 2027-05-15.

### Milestone 1: Foundation (weeks 1-4, target 2026-06-09)

**Deliverables:**
- Repo scaffold complete.
- All six schemas complete and validated.
- Pre-commit hooks and CI workflows green.
- 5 entries per axis (20 total) authored to `stable`.
- Anchor topic 1 (async-standups) rendered as vertical slice across the 20 entries.
- Skill Pack v0.1.0 with `compose-instruction` working.
- Static site rendering the 20 entries.
- README, CONTRIBUTING, LICENSE, NOTICE, AGENTS.md.
- ADRs 0001-0008 written.

**Exit criteria:** Maintainer can compose an instruction in Claude Code via `/writing-style-library:compose-instruction` and get a usable result.

### Milestone 2: Voice Catalog (weeks 5-12, target 2026-08-04)

**Deliverables:**
- All 80 voice entries authored to `stable`.
- Voices rendered on anchor topics 1-2.
- Voice diff-pairs (10) committed.
- 12 professional and 8 mentor recipes committed.
- Composer SPA in `alpha` (axis pickers + live preview).

**Exit criteria:** A user can browse all 80 voices on the public site and compose with any of them.

### Milestone 3: Tone, Style, Format Catalog (weeks 13-24, target 2026-10-27)

**Deliverables:**
- All 50 tone entries authored to `stable`.
- All 60 style entries authored to `stable`.
- All 100 format entries authored to `stable`.
- Tone, style, and format vertical slices on anchors 1-2.
- Tone diff-pairs (8), style diff-pairs (6), format diff-pairs (6) committed.
- Remaining 30 recipes committed.
- Composer SPA in `beta` (recipes, diff-explorer, side-by-side).

**Exit criteria:** Catalog is content-complete for v1 voice/tone/style/format counts. All 50 recipes are usable.

### Milestone 4: Surface Completion (weeks 25-36, target 2027-01-19)

**Deliverables:**
- TypeScript SDK published to npm.
- Python SDK published to PyPI.
- MCP server hosted and listed.
- Composer SPA in `rc` (BYO-key live runs, citations, personal library).
- Eval harness running against 4 models.
- Anchor topics 3-5 vertical slices on voices and formats only.
- All ADRs current.

**Exit criteria:** Three programmatic surfaces (SDK x 2, MCP) work end-to-end. Composer is usable end-to-end.

### Milestone 5: Polish and Launch (weeks 37-48, target 2027-04-13)

**Deliverables:**
- Documentation set complete (concepts, how-tos, design-standards, governance).
- Eval reports published.
- Browser extension in `alpha` (stretch, optional).
- Marketing site polished.
- Launch posts drafted (LinkedIn, Twitter, agentskills.io discussion).
- Listed on agentskills.io marketplace as `status: stable`.

**Exit criteria:** v1.0.0 release candidate ready for public launch.

### v1.0.0 Launch (week 49-52, target 2027-05-15)

**Activities:**
- Public launch announcements.
- Hacker News submission.
- Substack/Medium long-form launch post.
- Conference talk submissions for late-2027.
- Community contribution flow opens.

---

## 12. Capacity and Resource Plan

### 12.1 Roles

- **Maintainer (you).** Editorial direction, voice review, surface design, release decisions. ~20 hours/week.
- **Content contributor (1, part-time).** Entry drafting, example review, recipe authoring. ~10 hours/week.
- **Engineering contributor (optional, 1, part-time).** SDK + MCP + Composer + eval harness. ~10 hours/week.
- **LLM authoring loop.** Claude Opus 4.7 generates drafts; humans review.

### 12.2 Cost projection (rough)

| Item | Monthly | 12-month |
|---|---|---|
| Anthropic API (LLM authoring + Composer hosted-demo) | $300 | $3,600 |
| Cloudflare (Workers, Pages, R2) | $30 | $360 |
| GitHub Actions (paid tier for eval runs) | $20 | $240 |
| Domain | $1 | $12 |
| Promptfoo cloud (optional) | $50 | $600 |
| Contractor or contributor honorarium | variable | $0-$15,000 |
| **Total (no contractors)** | **$401** | **$4,812** |
| **Total (with one paid contractor)** | **$1,651** | **$19,812** |

### 12.3 Time-to-v1 sensitivity

- Solo, 20h/week: ~75 weeks (18 months).
- Solo + contributor at 10h/week: ~50 weeks (12 months).
- Solo + 2 contributors at 10h/week: ~37 weeks (9 months).
- Two full-time: ~19 weeks (5 months).

The 12-month plan assumes the second column.

---

## 13. Risk Register

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| 1 | Maintenance fatigue at month 6 | High | Critical | Strict surface scoping; freeze browser extension to Phase 4. |
| 2 | LLM examples read as generic LLM-prose | High | High | Maintainer review on every promotion to `stable`; explicit style-tells linter in M3. |
| 3 | Cross-reference graph drift as catalog grows | Medium | Medium | Reciprocity validation in CI from day 1. |
| 4 | Schema changes require mass retro-fit | Medium | High | Design schema for v1.0.0 explicitly; freeze structural changes after M1. |
| 5 | Composer design polish takes 2-3x estimate | High | Medium | Treat M2 alpha as functional-only; reserve M5 for polish. |
| 6 | Hosted MCP exceeds free-tier costs | Low | Medium | Rate limit; require BYO-key for compose calls; cache aggressively. |
| 7 | Eval rubrics produce false-precision scores | Medium | High | Pair LLM-judge with human review for all published claims; show distribution not just mean. |
| 8 | Marketplace rejection due to manifest issues | Low | High | Run `claude plugin validate` on every PR; follow agentskills.io spec strictly. |
| 9 | Contributor conflict on voice characterization | Medium | Medium | `confusable_with` field is the discussion locus; document review criteria explicitly. |
| 10 | License gray area on LLM-generated content stalls release | Low | High | Resolve in ADR 0007 before any LLM example is committed. |
| 11 | Twelve-month timeline slips into 18 | High | Medium | Plan-built with 25% buffer; treat M3 and M4 as the most slip-prone. |
| 12 | Public launch lands during model-release news cycle | Medium | Low | Watch Anthropic and OpenAI calendars; pick a quiet week. |

---

## 14. Success Metrics

### 14.1 Catalog metrics

- Entries at `stable` or above by v1: 290.
- Examples at `reviewed` or above by v1: ~1,120.
- Recipes at `stable`: 50.
- Diff-pairs published: 30.
- Cross-reference completeness: 100% (every entry has populated `pairs_well_with`, `confusable_with`).

### 14.2 Adoption metrics (12 months post-launch)

| Metric | Target | Stretch |
|---|---|---|
| Plugin installs (Claude Code) | 1,000 | 5,000 |
| npm downloads (TS SDK, weekly) | 200 | 1,000 |
| PyPI downloads (Python SDK, weekly) | 100 | 500 |
| MCP server unique callers | 50 | 250 |
| Composer monthly active users | 500 | 2,500 |
| Static site monthly visitors | 5,000 | 20,000 |
| GitHub stars | 200 | 1,000 |
| External contributors with merged PRs | 5 | 20 |

### 14.3 Quality metrics

- Eval pass rate (voice fidelity, top-3 model average): ≥80%.
- Schema validation pass rate on first PR: ≥95%.
- Time-to-merge for valid contributor PR: ≤7 days.
- Issue response time (median): ≤72 hours.

---

## 15. Launch and Distribution Plan

### 15.1 Pre-launch (M5)

- Soft-list on agentskills.io marketplace as `experimental` from M2 onwards.
- Solicit beta users from `pm-skills` audience and `product-on-purpose` newsletter.
- Beta cohort of ~25 users tests through M4.
- Final polish on Composer aesthetics during M5.

### 15.2 Launch sequence (week of v1.0.0)

- **Day -7:** Schedule announcements; brief beta cohort on launch date.
- **Day 0 (Tuesday):** Listing flips to `stable` on agentskills.io. README badge updates. Tag pushed.
- **Day 0 (Tuesday):** Long-form Substack/Medium post: "The Three-Axis Writing Library." Twitter/LinkedIn announcements.
- **Day +1 (Wednesday):** Hacker News submission with the Substack post.
- **Day +3 (Friday):** Recap and metrics post; respond to feedback.
- **Day +7:** Office-hours session with beta users.
- **Day +30:** First retrospective; v1.1 planning.

### 15.3 Post-launch growth

- Monthly newsletter: one vertical-slice diff-pair, one new recipe.
- Quarterly eval refresh: re-run against current models, publish updated leaderboard.
- Conference talks at PyConf, ReactSummit, AgentSummit (assume late 2027).
- Long-tail SEO via auto-generated entry pages.

---

## 16. Decision Points During Execution

These are the moments during the 12 months where the plan should pause and recalibrate against real signal:

- **End of M1.** Was the foundation actually built in 4 weeks? If 6+, the timeline doubles; recalibrate scope.
- **End of M2.** Are the 80 voices actually distinguishable in their renderings? If 20+ feel like duplicates, prune the catalog rather than push forward.
- **End of M3.** Is the example review sustainable? If review backlog exceeds 100 unreviewed examples, hire a reviewer or cut anchor-topic 4-5 coverage.
- **End of M4.** Are the SDK and MCP getting installs? If neither has crossed 50 installs by week 36, deprioritize browser extension and pour effort into Composer launch.
- **Two weeks before launch.** Does the eval harness produce results we are willing to publish? If no, hold launch one month rather than ship undertested.

---

*Execution Plan v1.0 - 2026-05-09 - assumes the strategic decision to build the overbuilt v1 has already been taken. Companion to `strategy-approach-roadmap_2026-05-08.md` and `value-delivery-approaches_2026-05-09.md`. Treat as a maximum-viable-product plan: every line is defensible, the whole is more than any solo maintainer should attempt without help.*

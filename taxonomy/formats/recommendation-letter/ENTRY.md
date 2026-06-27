---
id: recommendation-letter
name: Recommendation Letter
axis: format
domain: professional
family: outreach
one_liner: A letter by someone who knows a candidate, advocating for them to a third-party decision-maker.
description: |
  A recommendation letter is written by someone who knows a candidate to advocate for them to a
  third-party decision-maker - an admissions committee, an employer, a board. It speaks about the
  candidate to an evaluator, citing specific evidence of their qualities from firsthand experience.
  Unlike a cover letter, in which the candidate advocates for themselves in their own voice, a
  recommendation letter is written by a third party vouching for someone else - its credibility
  comes precisely from the fact that the writer is not the person being chosen.

  The genre has a specific rhetorical structure: the writer establishes their relationship to the
  candidate and the basis for their judgment, then presents concrete evidence from direct
  observation, and closes with a direct endorsement. The evidence is what separates a letter that
  helps from one that does not. Evaluators read many letters that assert the candidate is
  "hardworking" or "a pleasure to work with." A letter that describes a specific situation where
  the candidate made a decision under pressure, solved a novel problem, or demonstrated a quality
  that the evaluator cannot see from the application file - that letter carries weight.

  The writer's credibility is co-extensive with their specificity. A letter that praises without
  evidence reads as obligatory. A letter that reconstructs a specific moment, names the stakes, and
  connects the candidate's behavior to a conclusion signals that the writer paid attention and that
  the praise is earned.

  Typical length: 400-700 words.
canonical_template: |
  [Header: Writer name, title, institution, date]
  [Optional: Letterhead block]

  Dear [Admissions Committee / Hiring Manager / Selection Committee / Name],

  [Opening paragraph: state the writer's relationship to the candidate, how long and in what
  capacity they have known them, and the letter's purpose - recommending for [specific
  program/role/opportunity].]

  [Body paragraph 1: first piece of specific evidence. Describe a concrete situation, project,
  or observation from direct experience that demonstrates a quality relevant to what the evaluator
  is assessing. Name the context, the candidate's actions, and the outcome or signal.]

  [Body paragraph 2: second piece of specific evidence. Address a different dimension - a
  complementary quality or a situation that shows range or depth. Optional: preempt an observable
  gap with context the file does not contain.]

  [Closing paragraph: direct endorsement. Name the candidate, name the opportunity, and make the
  recommendation unambiguous. Optional: offer to discuss further.]

  [Signature: writer name, title, institution, contact information]
typical_voices:
  - senior-consultant
  - friendly-mentor
typical_tones:
  - confident
  - diplomatic
digital_or_print: both
pairs_well_with:
  - senior-consultant
  - friendly-mentor
  - confident
  - diplomatic
  - narrative-case-study
avoid_with:
  - skeptical
  - playful
  - urgent
confusable_with:
  - cover-letter
when_to_use:
  - When a candidate needs a credentialed third party to vouch for qualities an evaluator cannot assess from the application file alone
  - Applying to academic programs, fellowships, board positions, or roles where the selection process explicitly requests letters of recommendation
  - When the writer has direct, firsthand evidence of the candidate's performance, character, or potential from sustained professional or academic contact
  - When the stakes of the evaluation are high and the evaluator needs a human voucher who can be held accountable for the assessment
  - When the candidate's record contains gaps, pivots, or unconventional elements that a trusted voice can contextualize with direct observation
when_not_to_use:
  - When the writer does not have genuine direct experience with the candidate - a letter without firsthand evidence is worse than no letter
  - When the candidate can and should speak for themselves, as in a cover letter or personal statement where the candidate's own voice is the credential
  - When the request is informal or relational and a brief note of introduction would serve better than a formal letter of endorsement
tells:
  - 'Opens with the writer''s name, title, and direct relationship to the candidate, establishing the credibility base before the argument begins'
  - 'Cites specific, named situations from firsthand observation rather than general characterizations'
  - 'Written in third person about the candidate, from the first-person perspective of the writer'
  - 'Closes with an unambiguous direct endorsement, often naming the writer as available for further contact'
  - 'Evidence is tied to qualities the evaluator is assessing, not qualities the candidate emphasizes about themselves'
  - 'The writer''s institutional standing or length of relationship is made legible early in the letter'
anti_patterns:
  - pattern: 'Filling the letter with unsubstantiated praise - "exceptional leader," "outstanding communicator" - without a single concrete example from direct observation'
    why: 'Evaluators discount undifferentiated praise immediately because every letter contains it. Specificity is what moves a letter from obligatory to influential - a named situation the writer witnessed outweighs any number of superlatives.'
  - pattern: 'Writing as though the letter is a cover letter - framing the candidate''s qualifications from the candidate''s perspective rather than from the witness''s direct observation'
    why: 'A cover letter is written by the candidate advocating for themselves in their own voice to an evaluator already assessing a known set of needs. A recommendation letter derives its credibility from the writer''s third-party position as witness; conflating the two voices collapses the distinction that gives the letter its weight.'
  - pattern: 'Damning with faint praise - technically recommending the candidate while qualifying every strength with a hedge or withholding the full endorsement'
    why: 'Evaluators read for the endorsement. A letter that cannot commit signals that the candidate does not merit full backing; a writer''s hesitation reads as a warning, not a qualification.'
  - pattern: 'Describing the candidate in terms the writer could have assembled from a CV rather than from direct observation'
    why: 'A letter that could have been written without ever meeting the candidate signals the writer did not pay attention or lacks genuine firsthand experience - both outcomes damage the letter''s credibility.'
failure_modes:
  - mode: 'Over-endorses until every sentence is a superlative - "the best candidate in twenty years," "truly exceptional in every way" - so the letter reads as undifferentiated hyperbole rather than a calibrated expert assessment'
    mitigation: 'Reserve superlatives for genuine cases. One calibrated, specific superlative in an otherwise evidence-grounded letter lands harder than a letter in which every sentence claims the top tier. The writer''s credibility is the letter''s currency, and hyperbole spends it.'
  - mode: 'Third-party authority tips into the letter becoming about the writer''s own credentials, relationships, or judgment rather than about the candidate - the letter becomes a showcase for the writer''s discernment rather than evidence of the candidate''s qualities'
    mitigation: 'Read each paragraph and ask whether its central subject is the candidate or the writer. If the writer''s own history or standing is consuming more space than the candidate''s demonstrated qualities, redirect the paragraph to the candidate.'
  - mode: 'Specificity and formality tip into an over-structured enumeration - each paragraph names a quality and supplies exactly one supporting sentence - producing a letter that reads as a formatted checklist rather than a witness''s testimony'
    mitigation: 'Recommendation letters earn their persuasion from the texture of lived experience. Let the evidence drive the structure; an observation that requires two paragraphs to convey properly should have two paragraphs rather than being compressed into a formula.'
llm_instruction_phrasing: |
  Write as a recommendation letter. You are a credentialed third party - an employer, professor,
  supervisor, or colleague - who has direct firsthand experience with the candidate. Your credibility
  as a recommender is the letter's core asset; protect it by grounding every claim in specific,
  named evidence from your own observation. Open by establishing your relationship to the candidate
  and the letter's purpose. In the body, present concrete situations, projects, or decisions you
  observed directly that demonstrate the qualities relevant to what the evaluator is assessing. Do
  not assert qualities the reader cannot verify from your description; name what happened, who the
  candidate was in that moment, and what it showed. Close with an unambiguous endorsement. This is
  not a cover letter: you are a witness vouching for someone else, not an applicant making the case
  for yourself. The letter's persuasion comes from the writer's third-party authority and from the
  specificity of the evidence, not from enthusiasm or credential-stacking. Typical length: 400-700
  words.
tags:
  - professional
  - hiring
  - application
  - outreach
  - academic
  - endorsement
review_status: draft
---

## Recommendation Letter

A recommendation letter is written by someone who knows a candidate to advocate for them to a
third-party decision-maker - an admissions committee, an employer, a board. It speaks about the
candidate to an evaluator, citing specific evidence of their qualities from firsthand experience.
Unlike a cover letter, in which the candidate advocates for themselves in their own voice, a
recommendation letter is written by a third party vouching for someone else - its credibility
comes precisely from the fact that the writer is not the person being chosen.

The genre has a specific rhetorical structure: the writer establishes their relationship to the
candidate and the basis for their judgment, then presents concrete evidence from direct
observation, and closes with a direct endorsement. The evidence is what separates a letter that
helps from one that does not. Evaluators read many letters that assert the candidate is
"hardworking" or "a pleasure to work with." A letter that describes a specific situation where
the candidate made a decision under pressure, solved a novel problem, or demonstrated a quality
that the evaluator cannot see from the application file - that letter carries weight.

The writer's credibility is co-extensive with their specificity. A letter that praises without
evidence reads as obligatory. A letter that reconstructs a specific moment, names the stakes, and
connects the candidate's behavior to a conclusion signals that the writer paid attention and that
the praise is earned.

### Canonical template

```
[Header: Writer name, title, institution, date]
[Optional: Letterhead block]

Dear [Admissions Committee / Hiring Manager / Selection Committee / Name],

[Opening paragraph: state the writer's relationship to the candidate, how long and in what
capacity they have known them, and the letter's purpose - recommending for [specific
program/role/opportunity].]

[Body paragraph 1: first piece of specific evidence. Describe a concrete situation, project,
or observation from direct experience that demonstrates a quality relevant to what the evaluator
is assessing. Name the context, the candidate's actions, and the outcome or signal.]

[Body paragraph 2: second piece of specific evidence. Address a different dimension - a
complementary quality or a situation that shows range or depth. Optional: preempt an observable
gap with context the file does not contain.]

[Closing paragraph: direct endorsement. Name the candidate, name the opportunity, and make the
recommendation unambiguous. Optional: offer to discuss further.]

[Signature: writer name, title, institution, contact information]
```

### When to use

When a candidate needs a credentialed third party to vouch for qualities an evaluator cannot
assess from the application file alone; applying to academic programs, fellowships, board
positions, or roles where the selection process explicitly requests letters of recommendation;
when the writer has direct, firsthand evidence of the candidate's performance, character, or
potential from sustained professional or academic contact; when the stakes of the evaluation are
high and the evaluator needs a human voucher who can be held accountable for the assessment;
when the candidate's record contains gaps, pivots, or unconventional elements that a trusted
voice can contextualize with direct observation.

### When not to use

When the writer does not have genuine direct experience with the candidate (a letter without
firsthand evidence is worse than no letter); when the candidate can and should speak for
themselves, as in a cover letter or personal statement; when the request is informal or relational
and a brief note of introduction would serve better than a formal letter of endorsement.

### Pairs well with

`senior-consultant`, `friendly-mentor`, `confident`, `diplomatic`, `narrative-case-study`

### Often confused with

**cover-letter**: A cover letter is written by the candidate in their own voice, making the case
for one specific person for one specific role - it advocates for the writer themselves to an
evaluator who is already assessing candidates against a known set of needs. A recommendation
letter differs fundamentally in who holds the pen: the writer is a third party, not the person
being evaluated, and the letter's authority comes precisely from that separation. Where the cover
letter has the applicant argue their own qualifications directly, the recommendation letter has a
witness vouch for someone else based on direct observation.

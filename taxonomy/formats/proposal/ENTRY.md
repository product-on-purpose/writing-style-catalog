---
id: proposal
name: Proposal
axis: format
domain: professional
family: brief
one_liner: A document that pitches a specific piece of work or a deal to a client and asks them to say yes.
description: |
  A proposal is a document that pitches a specific piece of work or a deal to a prospective
  client, partner, or funder and asks them to say yes. It lays out the problem, the proposed
  approach, the scope, the timeline, and the terms - everything the decision-maker needs to
  approve and sign. A proposal is written to be read by someone who is not in the room: it
  stands entirely on its own prose, and the reader can treat it as the basis of a potential
  agreement.

  Because it is a standalone document, a proposal must do the work that a presenter does in a
  live meeting. It earns the reader's confidence by demonstrating that the writer understands
  the client's problem as well as the client does, then presents an approach specific enough
  to be acted on. A proposal that gestures at solutions without committing to scope, timeline,
  or price has not actually proposed anything - it is a brochure with a subject line.

  The canonical proposal moves through a predictable sequence: executive summary, problem
  statement, proposed approach, scope and deliverables, timeline, team or credentials, and
  pricing or terms. Not every proposal uses all sections, but the decision-maker must always
  be able to answer three questions: What are you going to do? When will it be done? What will
  it cost? Any proposal that leaves those unanswered is incomplete.

  Unlike a pitch deck - a sequence of presentation slides built to be walked through aloud by
  a speaker, with minimal text per slide - a proposal is a prose document the recipient reads
  independently. Where the deck relies on the presenter to carry detail and nuance, the
  proposal carries everything in its own text, including the specific scope, timeline, and
  terms a deck deliberately leaves out. Typical length: 500-2,500 words.
canonical_template: |
  # [Project or Engagement Title]
  ## Prepared for: [Client Name]
  ## Prepared by: [Your Name / Organization]
  ## Date: [Date]

  ## Executive Summary
  [2-4 sentences: the problem, the proposed solution, and the ask. The reader should be able
  to approve based on this section alone if they trust you enough.]

  ## The Problem
  [What challenge or need does the client face? State it in the client's own terms, not yours.]

  ## Proposed Approach
  [How will you solve the problem? Name the method and the reasoning. Say why this approach
  is right for this specific client, not for this category of problem in general.]

  ## Scope and Deliverables
  [What is included? What is explicitly not included? Ambiguity in scope becomes a dispute
  later - be specific.]

  ## Timeline
  [When will each phase or deliverable land? Name milestones, not just a final date.]

  ## Team and Credentials
  [Who will do the work and why are they qualified? Keep this brief unless the client asked
  for detail.]

  ## Investment
  [What does it cost? State the fee, the payment structure, and any conditions directly.]

  ## Next Steps
  [What does the client need to do to say yes? Name the action: a signature, a reply by
  date, a kickoff call.]
typical_voices:
  - senior-consultant
  - executive
typical_tones:
  - confident
  - diplomatic
digital_or_print: both
pairs_well_with:
  - senior-consultant
  - executive
  - confident
  - diplomatic
  - problem-solution
avoid_with:
  - confessional
  - reverent
  - playful
confusable_with:
  - pitch-deck
when_to_use:
  - Responding to a client's formal or informal request to outline how you would solve a specific problem
  - Initiating new commercial work by defining the scope, timeline, and terms before any work begins
  - Pursuing a grant, contract, or institutional partnership where the funder expects a formal written response
  - Following up a verbal conversation or presentation with a document that supplies the binding detail
  - Establishing a shared baseline that both parties can refer back to when scope questions arise later
when_not_to_use:
  - When the decision has already been made and the client needs a statement of work or a contract, not a persuasive document
  - When the relationship is informal and both parties prefer to agree by message or conversation rather than a formal document
  - When you are presenting to a live audience and the persuasive arc is better served by a visual slide sequence than by solo prose reading
tells:
  - 'An executive summary at the top that lets a decision-maker approve without reading the rest'
  - 'A problem section that restates the client''s need in the client''s own terms, not the vendor''s'
  - 'A scope section that explicitly names what is included and what is not'
  - 'A timeline with named milestones or delivery dates, not just a final end date'
  - 'A fee or pricing section that states the number directly and names the payment structure'
  - 'A next-steps or signature section that tells the reader exactly how to say yes'
  - 'Second-person address ("your organization," "you will receive") that keeps the reader as the subject'
anti_patterns:
  - pattern: 'Opening with a capabilities showcase or credential list before addressing the client''s problem'
    why: 'A proposal earns confidence by demonstrating that the writer understood the brief; leading with your own credentials before stating the problem signals you sent a template, not a tailored response.'
  - pattern: 'Leaving scope, timeline, or price vague so the proposal appears flexible'
    why: 'A proposal that does not commit to what it will deliver, when, or at what cost has not proposed anything the reader can approve; vagueness forces a follow-up conversation that delays or kills the yes.'
  - pattern: 'Submitting a slide deck when the client expects a standalone written document'
    why: 'A pitch deck is a sequence of presentation slides built to be walked through aloud by a speaker, with minimal text per slide, relying on a presenter to carry the detail; a proposal must supply all of that detail in its own prose, including the scope, timeline, and terms a deck deliberately leaves out.'
  - pattern: 'Padding the document with boilerplate sections not relevant to this client''s specific request'
    why: 'A proposal is a persuasive document, not a template audit; irrelevant sections signal the writer did not engage with the brief, and every filler page dilutes the reader''s confidence.'
failure_modes:
  - mode: 'Over-persuades into pure sales copy - the document reads as a letter of enthusiasm with vivid vision but no binding specificity, so the reader cannot actually approve anything concrete'
    mitigation: 'Anchor every persuasive claim in a concrete deliverable, date, or cost; if the scope and price sections are still vague after a revision pass, the proposal has not proposed anything.'
  - mode: 'Over-specifies into a contract draft - the document fills with exclusions, liability caveats, and legal-dense clauses until the reader routes it to counsel rather than signing it'
    mitigation: 'Keep contractual language proportional to the deal size; reserve exhaustive legal terms for the formal agreement that follows approval, and let the proposal remain a persuasive, readable document.'
llm_instruction_phrasing: |
  Write as a formal business proposal. The document must stand alone: the reader will not have
  a presenter to explain it, and they may treat it as the basis of an agreement. Structure
  the content in this sequence: Executive Summary (2-4 sentences covering the problem, the
  solution, and the ask), The Problem (the client's need in the client's own terms), Proposed
  Approach (the method and why it fits this specific client), Scope and Deliverables (what is
  included and what is explicitly not included), Timeline (milestones with dates, not just a
  completion date), Team and Credentials (brief unless the client asked for depth), Investment
  (state the fee and payment structure directly), and Next Steps (what the reader must do to
  say yes). Write in second person to keep the reader as the subject. Do not leave scope,
  timeline, or price vague - a proposal that cannot be approved is not a proposal. Do not
  open with a capabilities showcase; start by demonstrating you understood the problem.
tags:
  - professional
  - persuasion
  - client
  - scoping
  - business-development
review_status: draft
---

## Proposal

A proposal is a document that pitches a specific piece of work or a deal to a prospective client, partner, or funder and asks them to say yes. It lays out the problem, the proposed approach, the scope, the timeline, and the terms - everything the decision-maker needs to approve and sign. A proposal is written to be read by someone who is not in the room: it stands entirely on its own prose, and the reader can treat it as the basis of a potential agreement.

Because it is a standalone document, a proposal must do the work that a presenter does in a live meeting. It earns the reader's confidence by demonstrating that the writer understands the client's problem as well as the client does, then presents an approach specific enough to be acted on. A proposal that gestures at solutions without committing to scope, timeline, or price has not actually proposed anything - it is a brochure with a subject line.

The canonical proposal moves through a predictable sequence: executive summary, problem statement, proposed approach, scope and deliverables, timeline, team or credentials, and pricing or terms. Not every proposal uses all sections, but the decision-maker must always be able to answer three questions: What are you going to do? When will it be done? What will it cost? Any proposal that leaves those unanswered is incomplete.

### Canonical template

```
# [Project or Engagement Title]
## Prepared for: [Client Name]
## Prepared by: [Your Name / Organization]
## Date: [Date]

## Executive Summary
[2-4 sentences: the problem, the proposed solution, and the ask. The reader should be able
to approve based on this section alone if they trust you enough.]

## The Problem
[What challenge or need does the client face? State it in the client's own terms, not yours.]

## Proposed Approach
[How will you solve the problem? Name the method and the reasoning. Say why this approach
is right for this specific client, not for this category of problem in general.]

## Scope and Deliverables
[What is included? What is explicitly not included? Ambiguity in scope becomes a dispute
later - be specific.]

## Timeline
[When will each phase or deliverable land? Name milestones, not just a final date.]

## Team and Credentials
[Who will do the work and why are they qualified? Keep this brief unless the client asked
for detail.]

## Investment
[What does it cost? State the fee, the payment structure, and any conditions directly.]

## Next Steps
[What does the client need to do to say yes? Name the action: a signature, a reply by
date, a kickoff call.]
```

### When to use

- Responding to a client's formal or informal request to outline how you would solve a specific problem
- Initiating new commercial work by defining the scope, timeline, and terms before any work begins
- Pursuing a grant, contract, or institutional partnership where the funder expects a formal written response
- Following up a verbal conversation or presentation with a document that supplies the binding detail
- Establishing a shared baseline that both parties can refer back to when scope questions arise later

### When not to use

- When the decision has already been made and the client needs a statement of work or a contract, not a persuasive document
- When the relationship is informal and both parties prefer to agree by message or conversation rather than a formal document
- When you are presenting to a live audience and the persuasive arc is better served by a visual slide sequence than by solo prose reading

### Pairs well with

`senior-consultant`, `executive`, `confident`, `diplomatic`, `problem-solution`

### Often confused with

**pitch-deck**: A pitch deck is a sequence of presentation slides that tells a persuasive story to win a decision, one idea per slide, built to be presented aloud or skimmed quickly; the speaker carries the thread and the narrative detail. A proposal is a standalone prose document the recipient reads independently and can treat as the basis of an agreement. Where the pitch deck relies on a live presenter to supply the nuance and specifics each slide only gestures at, the proposal carries all of that in its own text - including the scope, timeline, and terms a slide deck deliberately leaves out.

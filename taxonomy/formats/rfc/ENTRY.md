---
id: rfc
name: RFC (Request for Comments)
axis: format
domain: professional
family: deliberation
one_liner: A design proposal circulated to invite critique before a decision is made.
description: |
  An RFC (Request for Comments) is a structured proposal that circulates a design or
  change to a group of reviewers before any decision is finalized. Its defining
  characteristic is the open invitation: the author lays out a problem, proposes an
  approach, names the alternatives they considered, and explicitly asks readers to push
  back. Where an ADR records a settled choice, an RFC is the conversation that happens
  before one.

  The format originated in the internet standards community, where IETF RFCs defined
  protocols through iterative public comment. Engineering teams borrowed the pattern to
  coordinate changes that are too consequential to decide unilaterally - a new API
  contract, a major refactor, a shift in technical direction. The RFC disciplines the
  proposal author to write down their reasoning before reviewers can probe it, and gives
  reviewers a structured place to respond asynchronously.

  An RFC earns its place because it surfaces objections early, while the design is still
  cheap to change. Reviewers who might nod along in a meeting are more likely to raise
  concerns in writing, where they have time to think. Open questions in the template
  signal the author's honest uncertainty - they are invitations, not weaknesses.

  Typical length: 500-1500 words, depending on the complexity of the proposal.
canonical_template: |
  # RFC-NNNN: [Proposal Title]

  ## Status
  [Draft | Under Review | Accepted | Rejected | Withdrawn | Superseded by RFC-NNNN]

  ## Author(s)
  [Name(s), date]

  ## Problem
  [What is broken, missing, or needed. Why this matters now.]

  ## Proposed Approach
  [What you are proposing. Be specific enough that a reviewer can push back on the details.]

  ## Alternatives Considered
  [Other approaches evaluated and why they were not chosen.]

  ## Open Questions
  [What the author is uncertain about and wants reviewer input on.]

  ## Consequences
  [What this change costs, enables, or forecloses if accepted.]
typical_voices:
  - pragmatic-architect
  - senior-consultant
typical_tones:
  - candid
  - diplomatic
digital_or_print: digital
pairs_well_with:
  - pragmatic-architect
  - senior-consultant
  - candid
  - diplomatic
  - problem-solution
  - dialectic
avoid_with:
  - urgent
  - playful
  - pastoral
  - reverent
confusable_with:
  - adr
  - prd
  - design-doc
when_to_use:
  - Proposing a significant technical or design change that requires team alignment before work begins
  - Coordinating cross-team decisions where multiple stakeholders need to be heard before a direction is set
  - Changes consequential enough to deserve structured written critique while still open to revision
  - Documenting a design process so reviewers can engage asynchronously and on their own schedule
  - Surfacing objections early, when the design is still cheap to change
when_not_to_use:
  - When a decision has already been made and needs to be recorded - write an ADR instead
  - Urgent changes that cannot wait for a comment period
  - Small, easily reversible decisions that do not warrant structured review
tells:
  - 'An explicit Status line that tracks the proposal lifecycle (Draft, Under Review, Accepted, Rejected, Withdrawn)'
  - 'An Open Questions section that names what the author is genuinely uncertain about and wants reviewer input on'
  - 'An Alternatives Considered section that records what was evaluated and why it was not chosen'
  - 'A Problem section that frames the gap or failure before the solution appears'
  - 'An author byline with date, marking it as a time-bound proposal and not a standing document'
  - 'Language that actively invites disagreement rather than presenting a finished position'
anti_patterns:
  - pattern: 'Writing the RFC as a fait accompli - no open questions, no real alternatives, and a Proposed Approach that reads like an announcement'
    why: 'An RFC without genuine openness is theater; if the decision is already made, write an ADR. Using an RFC form to manufacture the appearance of consultation corrodes reviewer trust.'
  - pattern: 'Skipping the Alternatives Considered section or listing only one throwaway alternative'
    why: 'Alternatives Considered is the core evidence that the author did comparative thinking; without it, reviewers cannot tell whether the proposed approach was chosen deliberately or defaulted to.'
  - pattern: 'Treating the RFC as a PRD by writing requirements and acceptance criteria instead of a design proposal open to critique'
    why: 'A PRD specifies what to build for an execution team; an RFC proposes an approach and asks peers whether it is the right one. Mixing the two makes the document unusable for either purpose.'
  - pattern: 'Leaving the RFC open indefinitely with no review deadline and no decision recorded'
    why: 'An RFC without a status update to close the loop becomes organizational clutter; the comment period needs a deadline and the author must update the status after review ends.'
failure_modes:
  - mode: 'Collapses into a question-dump - so many open questions and so little conviction that reviewers have nothing concrete to push back on'
    mitigation: 'An RFC needs a real proposed approach, not just a problem description. Draft a concrete recommendation before opening for comment; open questions should be targeted uncertainties, not a substitute for having a position.'
  - mode: 'Stretches into a permanent consultation - the comment period never closes, the status stays Draft, and the proposal never reaches a decision'
    mitigation: 'Set a review deadline when the RFC is opened. After the deadline, synthesize feedback and update the status to Accepted, Rejected, or Withdrawn; an undecided RFC is an abandoned RFC.'
llm_instruction_phrasing: |
  Write as an RFC (Request for Comments). Structure the document with these sections:
  Problem, Proposed Approach, Alternatives Considered, Open Questions, and Consequences.
  In Problem: frame what is broken, missing, or needed - do not lead with the solution.
  In Proposed Approach: be specific enough that a reviewer can push back on the details.
  In Alternatives Considered: honestly name what you evaluated and why you did not choose it;
  one throwaway alternative is not enough. In Open Questions: name the things you are
  genuinely uncertain about and want reviewer input on - these are invitations, not
  weaknesses. The tone should be candid and diplomatic: the author has a position but is
  genuinely open to being wrong. Do not write as if the decision is already made.
tags:
  - technical
  - proposal
  - design-review
  - collaboration
  - engineering
  - documentation
review_status: draft
---

## RFC (Request for Comments)

An RFC (Request for Comments) is a structured proposal that circulates a design or change to a group of reviewers before any decision is finalized. Its defining characteristic is the open invitation: the author lays out a problem, proposes an approach, names the alternatives they considered, and explicitly asks readers to push back. Where an ADR records a settled choice, an RFC is the conversation that happens before one.

The format originated in the internet standards community, where IETF RFCs defined protocols through iterative public comment. Engineering teams borrowed the pattern to coordinate changes that are too consequential to decide unilaterally - a new API contract, a major refactor, a shift in technical direction. The RFC disciplines the proposal author to write down their reasoning before reviewers can probe it, and gives reviewers a structured place to respond asynchronously.

### Canonical template

```
# RFC-NNNN: [Proposal Title]

## Status
[Draft | Under Review | Accepted | Rejected | Withdrawn | Superseded by RFC-NNNN]

## Author(s)
[Name(s), date]

## Problem
[What is broken, missing, or needed. Why this matters now.]

## Proposed Approach
[What you are proposing. Be specific enough that a reviewer can push back on the details.]

## Alternatives Considered
[Other approaches evaluated and why they were not chosen.]

## Open Questions
[What the author is uncertain about and wants reviewer input on.]

## Consequences
[What this change costs, enables, or forecloses if accepted.]
```

### When to use

Proposing a significant technical or design change that requires team alignment before work begins, coordinating cross-team decisions where multiple stakeholders need to be heard before a direction is set, changes consequential enough to deserve structured written critique while still open to revision, surfacing objections early when the design is still cheap to change.

### When not to use

When a decision has already been made and needs to be recorded (write an ADR instead), urgent changes that cannot wait for a comment period, small easily reversible decisions that do not warrant structured review.

### Pairs well with

`pragmatic-architect`, `senior-consultant`, `candid`, `diplomatic`, `problem-solution`, `dialectic`

### Often confused with

**adr**: An ADR records a decision already made and explains the reasoning behind it. An RFC is the proposal that precedes the decision - it is still open to revision and asks reviewers whether the proposed approach is the right one.

**prd**: A PRD specifies what to build and defines requirements for an execution team. An RFC proposes how to approach a design challenge and asks peers to evaluate that approach. The PRD is an input to engineering work; the RFC is a checkpoint before committing to a direction.

**design-doc**: A design doc is the implementation specification for something already being built - it answers "how exactly will this work?" An RFC is a comment-seeking proposal for a design direction that explicitly invites pushback before a decision is finalized. Their templates look alike: both have a problem statement, a proposed approach, and alternatives. The line is purpose and timing - an RFC asks "should we go this direction?"; a design doc answers "here is how we are going."

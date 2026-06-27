---
id: design-doc
name: Design Document
axis: format
domain: professional
family: deliberation
one_liner: An engineering document that explores a design space and justifies an approach before implementation.
description: |
  A design document works through how a non-trivial piece of software will be built,
  before it is built: the problem, the constraints, the proposed design, the alternatives
  weighed, and the risks. Where an ADR records a single decision already made, a design
  doc is the working space where the design is reasoned through before decisions solidify.
  Its audience is the engineers who will build and review the system - it exists to
  surface problems early, coordinate understanding, and create a record of the reasoning
  behind the implementation.

  The hallmarks of a good design doc are proportionality and specificity. It goes deep
  enough on schemas, APIs, component boundaries, and data flows to give reviewers
  something real to push back on - but it stays focused on the problem being solved
  rather than general principles. A design doc that covers everything equally covers
  nothing usefully.

  Design docs live in the space between "we are going to build X" (a PRD) and "we
  decided to do it this way" (an ADR). They are working documents: they may be updated
  as understanding evolves, and they expire when the system is built and the decisions
  have been absorbed into ADRs and operational docs. Their value is in the conversation
  they make possible before a line of production code is written.

  Typical length: 500-2000 words.
canonical_template: |
  # [System / Feature Name] Design Document

  ## Status

  [Draft | In Review | Accepted | Superseded]

  ## Problem

  [What problem is being solved. The constraints that shape the solution space.]

  ## Proposed Design

  [How the system will work. Schemas, APIs, component boundaries, data flows.
  Be specific enough that a reviewer can evaluate the approach.]

  ## Alternatives Considered

  [Other approaches evaluated and why they were not chosen.]

  ## Risks and Open Questions

  [What could go wrong. What is still uncertain.]

  ## Appendix (optional)

  [Supporting diagrams, data models, or reference material.]
typical_voices:
  - pragmatic-architect
  - senior-consultant
typical_tones:
  - candid
  - matter-of-fact
digital_or_print: digital
pairs_well_with:
  - pragmatic-architect
  - senior-consultant
  - candid
  - matter-of-fact
  - problem-solution
  - comparison-contrast
avoid_with:
  - playful
  - pastoral
  - urgent
  - reverent
confusable_with:
  - adr
  - prd
  - rfc
when_to_use:
  - Planning a non-trivial feature or system before implementation begins
  - Coordinating design across multiple engineers or teams
  - Surfacing risks and open questions before code is written
  - Creating a reviewable artifact that lets engineers evaluate the implementation at the concrete level - schemas, APIs, component boundaries - before code is written
  - Documenting the reasoning behind an implementation for future maintainers
when_not_to_use:
  - Small, self-contained changes where the implementation approach is obvious to any reviewer
  - After the system is already built (write ADRs for the decisions instead)
  - When a decision about direction is still open and needs broad input before committing to build (write an RFC instead)
tells:
  - 'A Problem or Background section that names the constraints shaping the solution space'
  - 'A Proposed Design section committing to concrete implementation specifics - schemas, APIs, component boundaries, or data flows - that an RFC would not yet pin down'
  - 'An Alternatives Considered section that shows what was evaluated and why it was rejected'
  - 'A Risks and Open Questions section that names what could go wrong or is still uncertain'
  - 'A Status header (Draft, In Review, Accepted, Superseded) tracking where the document stands'
  - 'Technical specificity at the implementation level, not the product requirement level'
  - 'Audience is the engineers who will build or review the system, not product stakeholders'
anti_patterns:
  - pattern: 'Writing at the product requirement level - what to build and why - instead of the implementation level - how to build it'
    why: 'A design doc that describes desired outcomes without specifying schemas, interfaces, or component boundaries is a PRD, not a design doc; engineers cannot evaluate or build from it.'
  - pattern: 'Omitting Alternatives Considered or listing alternatives without saying why they were rejected'
    why: 'The reasoning behind the chosen approach is where design docs earn their value; a list of alternatives without rejection rationale reduces to a menu, not a design.'
  - pattern: 'Scoping the document to the entire system rather than the specific change or addition being designed'
    why: 'System-wide scope turns a design doc into unmaintainable reference documentation; each design doc should cover one bounded change or addition.'
  - pattern: 'Soliciting a vote on whether to proceed rather than inviting technical review of how to proceed'
    why: 'That is the job of an RFC; a design doc assumes the decision to build has been made and works through the implementation, not the direction.'
failure_modes:
  - mode: 'Over-specifies too early - locks in implementation details before the team has validated the approach, so review becomes defensive rather than generative'
    mitigation: 'Flag uncertain areas explicitly in Risks and Open Questions; keep early drafts focused on structure and interfaces before committing to implementation minutiae.'
  - mode: 'Expands into a treatise - grows to cover every edge case and becomes unreadable before the first reviewer reaches the Proposed Design section'
    mitigation: 'Aim for the minimum specificity needed for a reviewer to evaluate the approach; move exhaustive detail to appendices or linked documents.'
llm_instruction_phrasing: |
  Write as a Design Document. Work through how the system will be built, not what it should
  do. Use these sections: Problem (the constraints shaping the solution space), Proposed
  Design (concrete specifics: schemas, APIs, component boundaries, data flows - enough for
  a reviewer to push back on the approach), Alternatives Considered (other approaches and
  why they were rejected), Risks and Open Questions (what could go wrong and what is still
  uncertain). Be technically specific. Your audience is engineers who will build and review
  the system. Do not write at the product requirement level - that is a PRD. Do not
  solicit a decision on whether to proceed - that is an RFC. Write at the implementation
  level, assuming the decision to build has been made.
tags:
  - technical
  - engineering
  - documentation
  - design
  - architecture
review_status: draft
---

## Design Document

A design document works through how a non-trivial piece of software will be built, before it is built: the problem, the constraints, the proposed design, the alternatives weighed, and the risks. Where an ADR records a single decision already made, a design doc is the working space where the design is reasoned through before decisions solidify. Its audience is the engineers who will build and review the system - it exists to surface problems early, coordinate understanding, and create a record of the reasoning behind the implementation.

The hallmarks of a good design doc are proportionality and specificity. It goes deep enough on schemas, APIs, component boundaries, and data flows to give reviewers something real to push back on - but it stays focused on the problem being solved rather than general principles. A design doc that covers everything equally covers nothing usefully.

Design docs live in the space between "we are going to build X" (a PRD) and "we decided to do it this way" (an ADR). They are working documents: they may be updated as understanding evolves, and they expire when the system is built and the decisions have been absorbed into ADRs and operational docs. Their value is in the conversation they make possible before a line of production code is written.

### Canonical template

```
# [System / Feature Name] Design Document

## Status
[Draft | In Review | Accepted | Superseded]

## Problem
[What problem is being solved. The constraints that shape the solution space.]

## Proposed Design
[How the system will work. Schemas, APIs, component boundaries, data flows.
Be specific enough that a reviewer can evaluate the approach.]

## Alternatives Considered
[Other approaches evaluated and why they were not chosen.]

## Risks and Open Questions
[What could go wrong. What is still uncertain.]

## Appendix (optional)
[Supporting diagrams, data models, or reference material.]
```

### When to use

Planning a non-trivial feature or system before implementation begins, coordinating design across multiple engineers or teams, surfacing risks and open questions before a line of code is committed, creating a reviewable artifact that lets engineers evaluate the implementation at the concrete level - schemas, APIs, component boundaries - before code is written, documenting the reasoning behind an implementation for future maintainers.

### When not to use

Small, self-contained changes where the implementation approach is obvious to any reviewer, after the system is already built (write ADRs for the decisions instead), when a decision about direction is still open and needs broad input before committing to build (write an RFC instead).

### Pairs well with

`pragmatic-architect`, `senior-consultant`, `candid`, `matter-of-fact`, `problem-solution`, `comparison-contrast`

### Often confused with

**adr**: An ADR records a single decision already made and its consequences. A design doc is the working space that precedes those decisions - one design doc typically generates several ADRs as the design is reviewed and accepted.

**prd**: A PRD defines what should be built and why - its audience is product stakeholders. A design doc specifies how the engineering solution will be built - schemas, APIs, component boundaries, data flows - and its audience is the engineers who will implement and review the work.

**rfc**: A design doc is the implementation specification for something already being built; its currency is technical specificity - schemas, APIs, component boundaries, data flows. An RFC is a comment-seeking proposal for a design direction that invites pushback before a decision. A design doc assumes the decision to build has been made and works out how; an RFC is still asking whether and how to proceed.

---
id: prd
name: Product Requirements Document
axis: format
domain: professional
family: deliberation
one_liner: A structured document that defines what a product or feature should do, for whom, and why - without specifying how to build it.
description: |
  A PRD (Product Requirements Document) is the contract between a product team and an engineering
  team. It answers: what is the problem, who has it, what does success look like, and what are the
  boundaries of the solution? What a PRD deliberately does not answer is: how will engineering
  implement this? That boundary is the PRD's most important feature. A PRD that specifies
  implementation details is not a PRD - it is a spec, and it is a sign that the PM does not trust
  engineering to make implementation decisions.

  A good PRD creates alignment without constraining the implementation. It gives engineering enough
  context to ask the right questions and make good tradeoffs. A bad PRD is either too vague
  (engineering guesses the intent) or too detailed (engineering follows the letter and misses the
  spirit).

  The canonical PRD structure: Problem statement (what is broken or missing), Goals (what success
  looks like, ideally measurable), Non-goals (what is explicitly out of scope), User stories or
  jobs-to-be-done, Open questions. The open questions section is often the most valuable - it
  surfaces the assumptions that have not yet been tested.

  Typical length: 500-1500 words.
canonical_template: |
  # [Feature Name] - Product Requirements

  ## Problem Statement

  [Who has what problem, with what frequency and impact.]

  ## Goals

  - [Measurable outcome 1]
  - [Measurable outcome 2]

  ## Non-Goals

  - [What we are explicitly NOT solving in this release]

  ## User Stories / Jobs-to-be-Done

  - As a [user], I want to [action] so that [outcome]

  ## Success Metrics

  - [How we will know this worked]

  ## Open Questions

  - [Assumption not yet validated]
typical_voices:
  - pragmatic-architect
  - operator
typical_tones:
  - matter-of-fact
  - candid
digital_or_print: digital
pairs_well_with:
  - pragmatic-architect
  - candid
  - matter-of-fact
  - problem-solution
avoid_with:
  - pastoral
  - devotional-reflection
  - warm
  - reverent
confusable_with:
  - adr
when_to_use:
  - Defining a new feature
  - Aligning engineering on scope
  - Communicating product intent to stakeholders
  - Planning a sprint or milestone
when_not_to_use:
  - Operational documentation
  - Post-launch retrospectives
  - Engineering design decisions
tells:
  - 'Canonical sections: Problem Statement, Goals, Non-Goals, User Stories, Success Metrics, Open Questions'
  - 'Defines what should be built and why, deliberately not how'
  - 'A problem statement that names the user, the friction, and the frequency'
  - 'Non-goals stated as explicitly as the goals'
  - 'Goals and Success Metrics expressed as measurable outcomes'
  - 'An Open Questions section naming assumptions not yet tested'
anti_patterns:
  - pattern: 'Specifying implementation details - how engineering should build it'
    why: 'A PRD that prescribes implementation is a spec; the what-not-how boundary is the format''s most important feature and signals distrust of engineering when crossed.'
  - pattern: 'Recording an architectural decision already made and its reasoning'
    why: 'That is the confusable adr; a PRD defines requirements before the implementation decisions exist, while an ADR documents a made decision about how.'
  - pattern: 'Leaving the non-goals blank or vague'
    why: 'Scope creep lives in what was left ambiguous; goals without matching non-goals let the boundary of the solution drift.'
failure_modes:
  - mode: 'Bloats into an exhaustive spec-of-everything - the document tries to pin down every requirement, edge case, and detail until engineering follows the letter and misses the spirit'
    mitigation: 'A PRD creates alignment without constraining implementation; if it leaves no room for engineering to make tradeoffs, it has overshot into a spec, so pull detail back to intent.'
  - mode: 'Over-specifies the requirements so tightly that the Open Questions section empties out and every assumption is asserted as settled'
    mitigation: 'The Open Questions section is often the most valuable part; if nothing is open, the PRD is likely hiding untested assumptions rather than having resolved them.'
llm_instruction_phrasing: |
  Write as a Product Requirements Document (PRD). Cover: Problem Statement (who has what problem),
  Goals (measurable outcomes), Non-Goals (explicit scope exclusions), User Stories or
  Jobs-to-be-Done, Success Metrics, and Open Questions. Do not specify implementation - the PRD
  describes what should be built and why, not how to build it. Make the problem statement specific:
  name the user, the friction, and the frequency. Make the non-goals as explicit as the goals -
  scope creep lives in what was left ambiguous. The open questions section is required: name the
  assumptions that have not yet been tested.
tags:
  - product
  - requirements
  - planning
  - engineering-alignment
  - pm
  - scope
review_status: stable
---

## Product Requirements Document

A PRD (Product Requirements Document) is the contract between a product team and an engineering team. It answers: what is the problem, who has it, what does success look like, and what are the boundaries of the solution? What a PRD deliberately does not answer is: how will engineering implement this? That boundary is the PRD's most important feature.

### Canonical template

```
# [Feature Name] - Product Requirements

## Problem Statement
[Who has what problem, with what frequency and impact.]

## Goals
- [Measurable outcome 1]

## Non-Goals
- [What we are explicitly NOT solving in this release]

## User Stories / Jobs-to-be-Done
- As a [user], I want to [action] so that [outcome]

## Success Metrics
- [How we will know this worked]

## Open Questions
- [Assumption not yet validated]
```

### When to use

Defining a new feature, aligning engineering on scope, communicating product intent to stakeholders, planning a sprint or milestone.

### When not to use

Operational documentation, post-launch retrospectives, engineering design decisions.

### Pairs well with

`pragmatic-architect`, `candid`, `matter-of-fact`, `problem-solution`

### Often confused with

**adr**: An ADR records an architectural decision already made. A PRD defines what should be built before engineering has made the implementation decisions.

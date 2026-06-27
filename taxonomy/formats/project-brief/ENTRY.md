---
id: project-brief
name: Project Brief
axis: format
domain: professional
family: brief
one_liner: A short kickoff document that sets an initiative's goal, scope, constraints, and success criteria before detailed work begins.
description: |
  A project brief sets the direction for an initiative before detailed work begins. It covers the
  goal, the scope, the constraints, the success criteria, and who is involved. The test of a good
  brief is simple: a stakeholder who has not been in the room should be able to read it once and
  understand why the work matters, what counts as done, and where the work stops.

  The brief is deliberately high-level. It frames the problem and defines the boundaries so that
  detailed requirements can be written next, by the people the brief mobilizes. That discipline is
  what makes a brief useful at kickoff: a brief that slides into requirements work has already
  failed, because the team cannot align on direction while fighting over feature details.

  A well-written brief creates the conditions for a PRD to be written well. It defines the
  initiative goal the PRD requirements must serve, the scope that keeps requirements from drifting,
  and the constraints engineering will need to honor. The brief does not specify what the product
  should do - that belongs in a PRD, which is a structured document defining what a product or
  feature should do, for whom, and why, covering problem statement, goals, non-goals, user stories,
  success metrics, and open questions. The brief simply makes that conversation possible.

  Typical length: 200-500 words.
canonical_template: |
  # [Project Name] - Project Brief

  ## Goal

  [The single outcome this initiative achieves. One sentence.]

  ## Background

  [Why this problem matters now. What is broken or missing. 2-4 sentences.]

  ## Scope

  ### In scope
  - [What this initiative covers]

  ### Out of scope
  - [What this initiative explicitly does not cover]

  ## Constraints

  - [Time, budget, technology, or dependency limits the team cannot negotiate]

  ## Success Criteria

  - [How we will know this succeeded. Measurable if possible.]

  ## Team

  - Owner: [Who decides]
  - Contributors: [Who does the work]
  - Informed: [Who needs to be kept in the loop]
typical_voices:
  - product-thinker
  - executive
typical_tones:
  - matter-of-fact
  - confident
digital_or_print: digital
pairs_well_with:
  - product-thinker
  - executive
  - matter-of-fact
  - confident
  - problem-solution
avoid_with:
  - confessional
  - reverent
  - playful
confusable_with:
  - prd
when_to_use:
  - Aligning a team on direction before requirements work begins
  - Communicating initiative purpose to stakeholders who need context, not detail
  - Establishing scope and constraints at the start of a project
  - Kicking off cross-functional work where roles and boundaries need to be named
  - Getting sign-off on a problem worth solving before anyone specifies the solution
when_not_to_use:
  - When the team already has a defined goal and needs feature-level requirements - write a PRD instead
  - When the deliverable is a made decision with context and consequences - write an ADR instead
  - When the audience needs step-by-step instructions or operational detail
tells:
  - 'A single-sentence Goal section that names the initiative outcome, not a cluster of aims'
  - 'An explicit Scope section with both in-scope and out-of-scope items named'
  - 'A Constraints section listing limits the team cannot negotiate away'
  - 'Success Criteria defined before any feature requirements exist'
  - 'A Team section naming owner, contributors, and informed parties'
  - 'Deliberate absence of user stories, feature specs, and implementation detail'
  - 'Short enough for a stakeholder to absorb in one read - typically 200-500 words'
anti_patterns:
  - pattern: 'Writing user stories, feature specs, or acceptance criteria inside the brief'
    why: 'The brief frames the initiative and defines its boundaries; a PRD is the structured document that defines what a product or feature should do, for whom, and why. The brief makes the PRD possible but does not replace it; mixing in requirements before the team is aligned removes the shared direction that makes requirements work effective.'
  - pattern: 'Leaving success criteria vague or omitting them entirely'
    why: 'The brief must define what counts as done before requirements work begins; without success criteria the team cannot judge whether the downstream requirements actually serve the initiative goal.'
  - pattern: 'Writing a brief that a stakeholder cannot absorb in one read'
    why: 'The brief exists to create shared direction quickly; if it exceeds 500 words, the initiative may not be well-defined yet or the detail belongs in a downstream document.'
failure_modes:
  - mode: 'Over-scopes into a project plan - begins listing tasks, milestones, and timelines until the strategic framing is buried under a schedule'
    mitigation: 'The brief covers goal, scope, constraints, success criteria, and team; project plans carry timelines and task breakdowns. If milestone dates appear in the brief, the document has changed shape.'
  - mode: 'Hedges the Goal section into a cluster of aims because committing to a single outcome is hard - lists A, B, C, and also D, leaving the team with no clear priority to align around'
    mitigation: 'Force the Goal section to a single sentence; if the team cannot agree on one sentence, the initiative is not ready for a brief and naming that disagreement is the work to do first.'
llm_instruction_phrasing: |
  Write as a Project Brief. Cover: Goal (a single sentence naming the initiative outcome, not a
  list of aims), Background (why this problem matters now), Scope (explicit in-scope and
  out-of-scope lists), Constraints (non-negotiable limits on time, budget, or technology), Success
  Criteria (how we will know this succeeded, measurable if possible), and Team (owner,
  contributors, informed parties). Stay deliberately high-level - no user stories, no feature
  specs, no implementation detail. A stakeholder who has not been in the room should be able to
  read the brief once and understand why the work matters, what counts as done, and where the work
  stops. Target 200-500 words. The Goal section must be a single sentence.
tags:
  - project-management
  - kickoff
  - planning
  - stakeholder-alignment
  - scope
  - brief
review_status: draft
---

## Project Brief

A project brief sets the direction for an initiative before detailed work begins. It covers the goal, the scope, the constraints, the success criteria, and who is involved. The test of a good brief is simple: a stakeholder who has not been in the room should be able to read it once and understand why the work matters, what counts as done, and where the work stops.

The brief is deliberately high-level. It frames the problem and defines the boundaries so that detailed requirements can be written next, by the people the brief mobilizes. A brief that slides into requirements work has already failed at its primary job: a team cannot align on direction while fighting over feature details. The discipline of staying high-level is not a shortcut - it is what makes the brief useful at kickoff and what makes downstream requirements work possible.

### Canonical template

```
# [Project Name] - Project Brief

## Goal
[The single outcome this initiative achieves. One sentence.]

## Background
[Why this problem matters now. What is broken or missing. 2-4 sentences.]

## Scope
### In scope
- [What this initiative covers]

### Out of scope
- [What this initiative explicitly does not cover]

## Constraints
- [Time, budget, technology, or dependency limits the team cannot negotiate]

## Success Criteria
- [How we will know this succeeded. Measurable if possible.]

## Team
- Owner: [Who decides]
- Contributors: [Who does the work]
- Informed: [Who needs to be kept in the loop]
```

### When to use

- Aligning a team on direction before requirements work begins
- Communicating initiative purpose to stakeholders who need context, not detail
- Establishing scope and constraints at the start of a project
- Kicking off cross-functional work where roles and boundaries need to be named
- Getting sign-off on a problem worth solving before anyone specifies the solution

### When not to use

- When the team already has a defined goal and needs feature-level requirements - write a PRD instead
- When the deliverable is a made decision with context and consequences - write an ADR instead
- When the audience needs step-by-step instructions or operational detail

### Pairs well with

`product-thinker`, `executive`, `matter-of-fact`, `confident`, `problem-solution`

### Often confused with

**prd**: A PRD (Product Requirements Document) is a structured document that defines what a product or feature should do, for whom, and why - it is the contract between a product team and an engineering team, covering problem statement, goals, non-goals, user stories, success metrics, and open questions. A project brief operates one level above: it establishes why the initiative matters and what the boundaries are, so that the PRD can be written well. The brief makes the PRD possible; it does not replace it.

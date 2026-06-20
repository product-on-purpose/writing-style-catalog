---
id: adr
name: Architecture Decision Record
axis: format
domain: professional
family: deliberation
one_liner: A short structured document that captures a significant architectural decision, its context, and its consequences.
description: |
  An ADR is a lightweight record of a decision that was hard to make and will be hard to change.
  Its value is not in the decision itself but in the reasoning: future engineers who encounter the
  system and wonder "why is it built this way?" have an answer that does not depend on
  institutional memory. An ADR is a gift to your future self and to everyone who inherits the
  codebase.

  The canonical ADR structure is three sections: Context (what forces were at play), Decision
  (what was chosen and why), and Consequences (what the decision costs and what it enables).
  Context is not history - it is the live forces at the time of the decision that made this the
  right call. Consequences are not just the good ones - a good ADR honestly names the tradeoffs.

  ADRs should be small and numerous rather than large and rare. A team that writes ADRs only for
  major architectural decisions misses the smaller decisions that compound over time into the shape
  of the system.

  Typical length: 300-600 words.
canonical_template: |
  # [ADR-NNNN] [Decision Title]

  ## Status

  [Proposed | Accepted | Deprecated | Superseded by ADR-NNNN]

  ## Context

  [What forces were at play. The problem, the constraints, the alternatives considered.]

  ## Decision

  [What was decided. Be specific. Name the choice, not just the category.]

  ## Consequences

  ### Positive
  - [benefit]

  ### Negative
  - [tradeoff or cost]

  ### Neutral
  - [consequence that is neither good nor bad]
typical_voices:
  - pragmatic-architect
  - operator
typical_tones:
  - matter-of-fact
  - candid
digital_or_print: digital
pairs_well_with:
  - pragmatic-architect
  - operator
  - candid
  - matter-of-fact
  - problem-solution
  - comparison-contrast
avoid_with:
  - pastoral
  - devotional-reflection
  - reverent
  - warm
confusable_with:
  - prd
when_to_use:
  - Recording architectural decisions
  - Capturing technology choices
  - Documenting tradeoffs for future maintainers
  - Team alignment on significant choices
when_not_to_use:
  - Operational documentation
  - Explaining how a system works
  - Consumer-facing content
tells:
  - 'Three canonical sections: Context, Decision, Consequences'
  - 'A Status line (Proposed, Accepted, Deprecated, or Superseded by ADR-NNNN)'
  - 'Context names the live forces and constraints at decision time, not project history'
  - 'Decision names the specific choice, not just the category'
  - 'Consequences honestly includes a Negative subsection, not only benefits'
  - 'Short and focused, roughly 300-600 words, readable in a few minutes'
anti_patterns:
  - pattern: 'Writing Context as a history narrative instead of the live forces at decision time'
    why: 'Context exists to show why this was the right call under the constraints then; history does not let a future reader reconstruct the reasoning.'
  - pattern: 'Listing only positive consequences and omitting the tradeoffs'
    why: 'The Consequences section is where an ADR earns its value; hiding the negatives turns a decision record into marketing.'
  - pattern: 'Reserving ADRs only for rare, major decisions'
    why: 'ADRs should be small and numerous; the compounding smaller decisions go unrecorded if the bar is set too high.'
  - pattern: 'Describing what to build rather than recording a decision already made about how'
    why: 'That collides with the confusable prd format; an ADR records a made decision and its reasoning, not a product specification.'
failure_modes:
  - mode: 'Balloons past a few minutes read into a design treatise'
    mitigation: 'Keep it to roughly 300-600 words; if it needs a 20-minute read, split the decision or move detail to a linked doc.'
  - mode: 'The Consequences section drops the negatives, so the record reads as justification'
    mitigation: 'Always populate the Negative subsection with tradeoffs the author means; a Consequences section with no costs is a red flag.'
  - mode: 'Decision names a category ("use a queue") rather than the specific choice'
    mitigation: 'Name the actual choice and reasoning ("use SQS because ..."); specificity is what makes the record useful later.'
llm_instruction_phrasing: |
  Write as an Architecture Decision Record (ADR). Use the canonical three-section structure:
  Context, Decision, Consequences. In Context: name the live forces at the time of decision - not
  history, but the constraints, options, and pressures that made this choice necessary. In
  Decision: name the specific choice, not just the category. In Consequences: be honest about the
  tradeoffs - name the negative consequences alongside the positive. The Consequences section is
  where ADRs earn their value. Do not omit the hard truths. Keep the document focused and short -
  an ADR that requires a 20-minute read is too long.
tags:
  - technical
  - decision-record
  - architecture
  - documentation
  - engineering
review_status: stable
---

## Architecture Decision Record

An ADR is a lightweight record of a decision that was hard to make and will be hard to change. Its value is not in the decision itself but in the reasoning: future engineers who encounter the system and wonder "why is it built this way?" have an answer that does not depend on institutional memory. An ADR is a gift to your future self and to everyone who inherits the codebase.

The canonical ADR structure is three sections: Context (what forces were at play), Decision (what was chosen and why), and Consequences (what the decision costs and what it enables). Context is not history - it is the live forces at the time of the decision that made this the right call. Consequences are not just the good ones - a good ADR honestly names the tradeoffs.

### Canonical template

```
# [ADR-NNNN] [Decision Title]

## Status
[Proposed | Accepted | Deprecated | Superseded by ADR-NNNN]

## Context
[What forces were at play. The problem, the constraints, the alternatives considered.]

## Decision
[What was decided. Be specific. Name the choice, not just the category.]

## Consequences
### Positive
- [benefit]
### Negative
- [tradeoff or cost]
### Neutral
- [consequence that is neither good nor bad]
```

### When to use

Recording architectural decisions, capturing technology choices, documenting tradeoffs for future maintainers, team alignment on significant choices.

### When not to use

Operational documentation, explaining how a system works, consumer-facing content.

### Pairs well with

`pragmatic-architect`, `operator`, `candid`, `matter-of-fact`, `problem-solution`, `comparison-contrast`

### Often confused with

**prd**: A PRD defines what should be built and why. An ADR records a decision already made about how to build it.

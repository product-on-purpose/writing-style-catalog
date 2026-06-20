---
id: decision-log
name: Decision Log
axis: style
one_liner: A real-time record of context, options considered, criteria used, and reasoning - capturing how a decision was reached, not justifying it after the fact.
description: |
  A decision log is written at the moment of deciding, not after the decision has proven itself.
  This timing is what gives it value. A document written after the fact is a justification dressed
  as a record - it knows the outcome and selects the evidence that supports it. A decision log
  written in the moment of deciding captures the actual options that were on the table, the actual
  criteria that mattered, and the actual reasons the chosen path seemed best given what was known
  at the time. Future readers can assess whether the reasoning was sound without being misled by
  hindsight selection.

  The context section is the most undervalued part of a decision log. Decisions made six months ago
  often look inexplicable without it. "Why did we deploy on a Friday?" makes no sense unless the
  reader knows that the client had a board presentation Monday and the demo environment was broken.
  Context is not a formality - it is the load-bearing section that makes everything that follows
  legible to a future reader who was not in the room.

  An ADR (architecture decision record) is a decision-log specialized for software architecture
  choices. Decision-log is the general form. The same structure applies to product decisions,
  process changes, hiring decisions, vendor selections, and any other choice where the reasoning
  will matter later. The specialization of ADR for architecture adds conventions about drivers and
  consequences; the general decision-log form is deliberately more open.
structural_conventions:
  - Context section captures the situation and constraints that existed at decision time
  - Options section lists the alternatives actually considered, not a post-hoc menu
  - Criteria section names the values or constraints that governed the evaluation
  - Decision section states the chosen option and the reasoning - the "because," not just the "what"
  - Written at decision time, not reconstructed afterward
  - Does not require the decision to have been correct - a good decision log records good reasoning, not good outcomes
frame: expository
evidence_types:
  - options list with trade-offs
  - stated criteria and weights
  - context at the time of decision
  - consequences anticipated
reader_contract: "After reading this, you will understand what we decided and why - as well as what else we considered and what we knew when we chose."
classical_mode: exposition
pairs_well_with:
  - pragmatic-architect
  - direct-communicator
  - adr
  - matter-of-fact
avoid_with:
  - devotional-reflection
  - playful
  - warm
confusable_with:
  - executive-summary
when_to_use:
  - Any significant decision where the reasoning will matter to future team members
  - Vendor selections, technology choices, product pivots, or process changes
  - Decisions made under uncertainty where future readers need to understand what was known at the time
  - Onboarding contexts where new team members need to understand why things are the way they are
  - Governance and compliance contexts where auditability of reasoning is required
when_not_to_use:
  - Routine operational decisions that will not affect future readers
  - Contexts where the audience needs the decision communicated, not the reasoning behind it
  - Real-time writing situations where the overhead of structured logging is not warranted
  - When the decision will be immediately visible in its outcomes and the reasoning is obvious
llm_instruction_phrasing: |
  Write as a decision log. Organize around four sections: context (what was true when this
  decision was made), options (what was actually considered, not a post-hoc list), criteria
  (what values or constraints governed the evaluation), and decision (what was chosen and why -
  the because, not just the what). Write as if the reader was not in the room. Do not justify
  the decision in hindsight - record the reasoning as it actually existed at decision time.
  A good decision log records good reasoning; it does not require the decision to have been
  correct in hindsight. Do not include pleasantries or framing prose; go directly to the
  structured record.
tags:
  - documentation
  - governance
  - structured
  - decision-making
  - audit
review_status: stable
---

## Decision Log

A decision log is written at the moment of deciding, not after the decision has proven itself. This timing is what gives it value. A document written after the fact is a justification dressed as a record - it knows the outcome and selects the evidence that supports it. A decision log written in the moment of deciding captures the actual options that were on the table, the actual criteria that mattered, and the actual reasons the chosen path seemed best given what was known at the time. Future readers can assess whether the reasoning was sound without being misled by hindsight selection.

The context section is the most undervalued part of a decision log. Decisions made six months ago often look inexplicable without it. "Why did we deploy on a Friday?" makes no sense unless the reader knows that the client had a board presentation Monday and the demo environment was broken. Context is not a formality - it is the load-bearing section that makes everything that follows legible to a future reader who was not in the room.

An ADR (architecture decision record) is a decision-log specialized for software architecture choices. Decision-log is the general form. The same structure applies to product decisions, process changes, hiring decisions, vendor selections, and any other choice where the reasoning will matter later. The specialization of ADR for architecture adds conventions about drivers and consequences; the general decision-log form is deliberately more open.

### Structural conventions

- Context section captures the situation and constraints that existed at decision time
- Options section lists the alternatives actually considered, not a post-hoc menu
- Criteria section names the values or constraints that governed the evaluation
- Decision section states the chosen option and the reasoning - the "because," not just the "what"
- Written at decision time, not reconstructed afterward
- Does not require the decision to have been correct - a good decision log records good reasoning, not good outcomes

### When to use

Any significant decision where the reasoning will matter to future team members: vendor selections, technology choices, product pivots, process changes, and hiring decisions. Especially valuable in onboarding contexts where new team members need to understand why things are the way they are, and in governance contexts where the auditability of reasoning is required.

### When not to use

Routine operational decisions that will not affect future readers. Avoid when the audience needs the decision communicated rather than the reasoning behind it, in real-time situations where structured logging overhead is not warranted, and when the outcome is immediately visible and the reasoning is self-evident.

### Pairs well with

`pragmatic-architect`, `direct-communicator`, `adr`, `matter-of-fact`

### Often confused with

**adr**: An ADR (architecture decision record) is a decision-log specialized for software architecture choices, with conventions specific to that domain - drivers, status, consequences in a technical sense. Decision-log is the general form that applies to any significant organizational choice. Every ADR follows the decision-log pattern; not every decision-log is an ADR. The distinction is scope and specialization, not structure.

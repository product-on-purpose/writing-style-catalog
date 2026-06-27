---
id: runbook
name: Runbook
axis: format
domain: professional
family: instruction
one_liner: A step-by-step operational procedure for a recurring task or incident, written to be followed correctly under pressure.
description: |
  A runbook is an operational document written to be executed, not just read. Its primary design
  constraint is that an operator who did not build the system must be able to complete the
  procedure correctly by following the steps sequentially, without needing to understand why each
  step exists. The format earns its place precisely because systems fail at unpredictable moments,
  and the operator handling the failure may be under time pressure, may have been paged at 3 AM,
  or may be unfamiliar with this specific system. A runbook makes the procedure survivable under
  those conditions.

  The canonical runbook structure groups steps into phases that match the operator's mental model
  of an operation: Prerequisites (what must be true before starting), Procedure (numbered steps
  with expected outputs), Verification (how to confirm the procedure succeeded), and Rollback (how
  to undo if something went wrong). Steps are numbered, not bulleted, because order matters. Each
  step should be atomic - one action, one expected output - so the operator knows at each point
  whether to continue or stop and escalate.

  Runbooks are most valuable for tasks that are infrequent enough that institutional memory is
  unreliable but common enough that a fully automated system has not yet replaced them. They are
  indispensable for incident response, where a well-structured playbook lets an on-call engineer
  perform a complex triage sequence correctly under conditions that make reasoning difficult. A
  runbook is not a teaching document - it is a decision aid that replaces the need to reason in
  the moment.

  Typical length: 200-800 words for the procedure itself, though complex runbooks may split into
  multiple sub-procedures or include clearly labeled decision branches.
canonical_template: |
  # [Runbook Title]

  ## Overview

  [One sentence: what this procedure does and when to trigger it.]

  ## Prerequisites

  - [ ] [Condition that must be true before starting]
  - [ ] [Access, credentials, or tools required]

  ## Procedure

  1. **[Action verb] [target]**
     Expected output: [what you should see if this step succeeded]

  2. **[Action verb] [target]**
     Expected output: [what you should see if this step succeeded]

  ## Verification

  [How to confirm the full procedure completed successfully.]

  ## Rollback

  [Steps to undo this procedure if something went wrong, or "Not applicable" with justification.]

  ## Escalation

  [Who to contact and how if this runbook does not resolve the situation.]
typical_voices:
  - operator
  - technical-writer
typical_tones:
  - instructional
  - matter-of-fact
digital_or_print: digital
pairs_well_with:
  - operator
  - direct-communicator
  - instructional
  - matter-of-fact
  - procedural
avoid_with:
  - columnist
  - confessional
  - playful
confusable_with:
  - readme
  - technical-reference
when_to_use:
  - Recurring operational procedures where step order matters and a missed step causes failures
  - Incident response playbooks that must be usable by engineers who did not build the system
  - Deployment or release procedures that carry rollback risk
  - Onboarding steps for new operators who need to run systems without full context
  - Any procedure where a person unfamiliar with the system must complete it correctly the first time
when_not_to_use:
  - Conceptual or architectural explanations where the goal is understanding, not execution
  - Reference material that is looked up non-sequentially rather than followed step by step
  - One-off procedures that will never be repeated and do not warrant documentation overhead
tells:
  - 'Numbered steps in strict execution order, one action per step'
  - 'An expected output note after each step so the operator knows whether to continue or stop'
  - 'A Prerequisites section listing conditions, access, and tools that must be true before starting'
  - 'A Rollback section that either states how to undo the procedure or explicitly notes rollback is not applicable'
  - 'Imperative verbs at the start of each step ("Run", "Navigate", "Verify", "Copy", "Confirm")'
  - 'A Verification section separate from the Procedure that confirms the full operation succeeded'
anti_patterns:
  - pattern: 'Writing steps at the level of concepts rather than concrete commands or interface actions'
    why: 'An operator under pressure cannot fill in implicit steps; every command, click, and navigation path must be spelled out so the procedure works for someone who has never run it before.'
  - pattern: 'Omitting the Rollback section because the author assumes the procedure is low-risk'
    why: 'Risk is assessed under normal conditions; a runbook is used under abnormal ones. Even "No rollback available" is a valuable signal that tells the operator to proceed with extra care.'
  - pattern: 'Writing the runbook as a prose explanation of how the system works instead of a sequence of actions'
    why: 'That produces a readme or technical-reference, not a runbook; the reader needs to do something right now, not understand the system architecture.'
  - pattern: 'Using a single numbered list for a procedure that has conditional branches ("If X, skip to step 7")'
    why: 'Branching logic inside a numbered list is impossible to follow under pressure; conditional paths belong in separate sub-procedures or clearly labeled sections with their own step sequences.'
failure_modes:
  - mode: 'Over-atomizes - breaks every action into sub-sub-steps until the procedure loses its navigational shape and an experienced operator cannot see the sequence for the individual steps'
    mitigation: 'Group logically inseparable actions into single steps. The target reader is competent but context-free, not inexperienced. If an operator with basic system familiarity would never mentally separate two actions, they belong in one step.'
  - mode: 'Buries the operator in inline verification notes and conditional branches within the Procedure until the document requires more reading than acting, defeating the execute-under-pressure purpose'
    mitigation: 'Consolidate post-step verification into the single Verification section. Reserve inline expected-output notes for steps where a silent failure would lead the operator to continue in a broken state.'
llm_instruction_phrasing: |
  Write as a Runbook. Use the canonical sections: Overview, Prerequisites, Procedure, Verification,
  Rollback, and Escalation. In Overview: one sentence stating what this procedure does and when to
  trigger it. In Prerequisites: a checklist of conditions, access, and tools that must be true
  before starting. In Procedure: numbered steps with one action per step. End each step with an
  expected output so the operator knows whether to continue or stop and escalate. In Verification:
  state how to confirm the full operation succeeded. In Rollback: state how to undo the procedure,
  or explicitly say rollback is not applicable and why. Start every step with an imperative verb
  ("Run", "Navigate", "Copy", "Verify"). Assume the reader is competent but has never run this
  procedure before and may be under time pressure. Do not explain why steps work - write what to do.
tags:
  - operational
  - procedure
  - incident-response
  - technical
  - engineering
review_status: stable
---

## Runbook

A runbook is an operational document written to be executed, not just read. Its primary design
constraint is that an operator who did not build the system must be able to complete the procedure
correctly by following the steps sequentially, without needing to understand why each step exists.
The format earns its place precisely because systems fail at unpredictable moments, and the operator
handling the failure may be under time pressure, may have been paged at 3 AM, or may be unfamiliar
with this specific system. A runbook makes the procedure survivable under those conditions.

The canonical runbook structure groups steps into phases that match the operator's mental model of
an operation: Prerequisites (what must be true before starting), Procedure (numbered steps with
expected outputs), Verification (how to confirm the procedure succeeded), and Rollback (how to undo
if something went wrong). Steps are numbered, not bulleted, because order matters. Each step should
be atomic - one action, one expected output - so the operator knows at each point whether to
continue or stop and escalate.

### Canonical template

```
# [Runbook Title]

## Overview
[One sentence: what this procedure does and when to trigger it.]

## Prerequisites
- [ ] [Condition that must be true before starting]
- [ ] [Access, credentials, or tools required]

## Procedure
1. **[Action verb] [target]**
   Expected output: [what you should see if this step succeeded]

2. **[Action verb] [target]**
   Expected output: [what you should see if this step succeeded]

## Verification
[How to confirm the full procedure completed successfully.]

## Rollback
[Steps to undo this procedure if something went wrong, or "Not applicable" with justification.]

## Escalation
[Who to contact and how if this runbook does not resolve the situation.]
```

### When to use

Recurring operational procedures where step order matters and a missed step causes failures, incident response playbooks that must be usable by engineers who did not build the system, deployment or release procedures that carry rollback risk, onboarding steps for new operators who need to run systems without full context, any procedure where a person unfamiliar with the system must complete it correctly the first time.

### When not to use

Conceptual or architectural explanations where the goal is understanding rather than execution, reference material that is looked up non-sequentially rather than followed step by step, one-off procedures that will never be repeated and do not warrant documentation overhead.

### Pairs well with

`operator`, `direct-communicator`, `instructional`, `matter-of-fact`, `procedural`

### Often confused with

**readme**: A README orients a reader to a project - what it is, how to install it, and where to start. A runbook is not an orientation document; it is a procedure to follow in sequence during a specific operation. A README can be read in any order; a runbook must be followed step by step to a defined end state.

**technical-reference**: A technical reference lists commands, parameters, APIs, or configuration options for lookup. A runbook sequences those primitives into a specific operation with a defined start condition, end state, and rollback path. A reader consults a reference to find information; a reader follows a runbook to complete a task under operational conditions.

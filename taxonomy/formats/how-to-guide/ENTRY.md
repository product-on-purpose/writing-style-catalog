---
id: how-to-guide
name: How-To Guide
axis: format
domain: professional
family: instruction
one_liner: A task-focused guide that teaches a reader to accomplish something they do not yet know how to do.
description: |
  A how-to guide teaches a reader to accomplish a specific task they do not yet know how to do,
  walking them through the steps with enough context to understand what they are doing and why. The
  format earns its place not just by listing actions but by building the reader's capability: it
  names prerequisites, anticipates where confusion is likely, and explains the purpose behind each
  stage. The goal is a reader who, having followed the guide once, could reproduce the task without
  the guide the second time.

  The how-to guide occupies a distinct position among technical documents. A reference lists
  commands, parameters, or APIs for lookup by a reader who already knows what they need. A tutorial
  introduces a technology through a worked example. A how-to guide bridges the gap: the reader knows
  what outcome they want but has not yet worked out how to reach it, and the guide gives them the
  path with just enough explanation to make the steps stick.

  Good how-to guides are sequenced by reader readiness, not by system architecture. Steps appear in
  the order a reader needs to take them, not in the order a developer would think to explain the
  internals. They acknowledge that readers may stop and restart, that prerequisites are often
  invisible to the author but critical for the reader, and that the step most likely to produce a
  stuck reader is usually one the author considered obvious.

  Typical length: 300-1500 words, depending on task complexity.
canonical_template: |
  # How to [accomplish specific task]

  ## Before you begin

  - [Prerequisite: what the reader must already have or know]
  - [Prerequisite: access, tool, or state required]

  ## Overview

  [1-2 sentences: what this guide covers and what the reader will be able to do when done.]

  ## Step 1: [Action phrase]

  [Brief explanation of why this step is needed.]

  [Specific, concrete instruction.]

  [What a successful outcome looks like at this step.]

  ## Step 2: [Action phrase]

  ...

  ## Troubleshooting

  [Common failure point and what to do about it.]

  ## Next steps

  [Where to go from here: related tasks, deeper reading, or what the reader just unlocked.]
typical_voices:
  - technical-writer
  - friendly-mentor
typical_tones:
  - instructional
  - encouraging
digital_or_print: digital
pairs_well_with:
  - technical-writer
  - friendly-mentor
  - instructional
  - encouraging
  - procedural
avoid_with:
  - skeptical
  - confessional
  - urgent
confusable_with:
  - runbook
when_to_use:
  - Teaching a reader to complete a task they have never done before, when understanding what they are doing matters as much as getting through the steps
  - Onboarding new users to a tool, workflow, or process where capability-building outlasts the first session
  - Documenting infrequent tasks that readers will return to repeatedly until the steps are internalized
  - Bridging the gap between reference documentation and a reader who cannot yet use that reference independently
  - Any situation where a reader who fails partway through needs enough context to diagnose and recover
when_not_to_use:
  - Situations where an experienced operator needs to execute a procedure correctly under pressure without pausing to read explanations
  - Reference lookup, where the reader already knows what they want and needs only the parameter, option, or command syntax
  - Conceptual or architectural overviews where the primary goal is understanding rather than task completion
tells:
  - 'Steps named with action verbs and framed for the reader, sequenced in the order the reader takes them'
  - 'A prerequisites section that names what the reader must have or know before starting'
  - 'Brief explanations of why each step exists, embedded within or immediately before the instruction'
  - 'Second-person prose addressed directly to the reader: "you will need", "your output should look like", "if you see"'
  - 'A troubleshooting or recovery section addressing common failure points by name'
  - 'A closing section that points the reader to what they can do next now that they have this skill'
  - 'Steps sequenced by reader readiness, not by the organization of the underlying system'
anti_patterns:
  - pattern: 'Omitting prerequisites and assuming the reader''s environment matches the author''s'
    why: 'Without stated prerequisites, a reader who fails on step one cannot tell whether the environment is wrong or the guide is broken. Unstated prerequisites are the most common reason a how-to guide works for the author and fails for everyone else.'
  - pattern: 'Writing steps as bare commands without indicating what a successful outcome looks like or why the step matters'
    why: 'A list of commands without context produces a reader who cannot recover when output differs from expectation. Explaining what each step does and what to expect afterward builds understanding, not just mechanical completion.'
  - pattern: 'Burying the first actionable step under a long conceptual orientation to the broader system'
    why: 'A how-to guide is task-oriented; long introductory explanations belong in overview or tutorial documents. A reader who came to accomplish something will abandon a guide that does not reach the first step quickly.'
  - pattern: 'Sequencing steps by system architecture or developer mental model rather than by reader readiness'
    why: 'Steps arranged to match system internals frequently omit the setup work that is obvious to the author but invisible to the reader. Reader-first sequencing surfaces those invisible prerequisites as named early steps.'
failure_modes:
  - mode: 'Over-explains - wraps every step in so much contextual scaffolding that the reader loses the thread of what to do; the guide becomes a lesson in the system rather than a path through a task'
    mitigation: 'Keep explanations proportional to the risk of confusion at that specific step. A one-sentence explanation is enough when a step is clear. The explanation serves the reader, not the depth of knowledge the author wants to display.'
  - mode: 'Over-anticipates confusion - so many warnings, edge cases, and conditional branches that a reader on the normal path cannot find the main sequence; addressing every exception makes the common case harder to follow'
    mitigation: 'Write the happy path cleanly, then consolidate exceptions in a troubleshooting section. Reserve inline warnings for genuine risks where a silent failure would mislead the reader. Conditional branches belong in separate labeled sections, not inside the numbered steps.'
  - mode: 'Over-scaffolds the reader to the point of condescension - restates what was just established, hedges every instruction with caveats, and treats the reader as incapable of any judgment call'
    mitigation: 'Assume a reader who is competent in general but has not done this specific task. Write to that intelligence, not to inexperience. Reserve warnings for genuine risks, not for things that cannot realistically go wrong.'
llm_instruction_phrasing: |
  Write as a How-To Guide. Use the canonical sections: Before you begin (prerequisites), Overview,
  numbered Steps, Troubleshooting, and Next steps. In Before you begin: list each prerequisite the
  reader must have or know before starting - do not assume the reader's environment matches yours.
  In Overview: one to two sentences stating what the guide covers and what the reader will be able
  to do when finished. In each Step: name the step with an action verb, briefly explain why the
  step exists, give the specific instruction, and state what a successful outcome looks like. In
  Troubleshooting: name common failure points and what to do about each. In Next steps: point the
  reader to related tasks or deeper resources. Sequence steps by reader readiness, not by system
  architecture. Write in the second person. Explain enough that the reader understands what they
  are doing, not just what to type.
tags:
  - documentation
  - tutorial
  - instructional
  - technical
  - onboarding
review_status: draft
---

## How-To Guide

A how-to guide teaches a reader to accomplish a specific task they do not yet know how to do,
walking them through the steps with enough context to understand what they are doing and why. The
format earns its place not just by listing actions but by building the reader's capability: it
names prerequisites, anticipates where confusion is likely, and explains the purpose behind each
stage. The goal is a reader who, having followed the guide once, could reproduce the task without
the guide the second time.

The how-to guide occupies a distinct position among technical documents. A reference lists
commands, parameters, or APIs for lookup by a reader who already knows what they need. A tutorial
introduces a technology through a worked example. A how-to guide bridges the gap: the reader knows
what outcome they want but has not yet worked out how to reach it, and the guide gives them the
path with just enough explanation to make the steps stick.

Good how-to guides are sequenced by reader readiness, not by system architecture. Steps appear in
the order a reader needs to take them, not in the order a developer would think to explain the
internals. They acknowledge that readers may stop and restart, that prerequisites are often
invisible to the author but critical for the reader, and that the step most likely to produce a
stuck reader is usually one the author considered obvious.

### Canonical template

```
# How to [accomplish specific task]

## Before you begin
- [Prerequisite: what the reader must already have or know]
- [Prerequisite: access, tool, or state required]

## Overview
[1-2 sentences: what this guide covers and what the reader will be able to do when done.]

## Step 1: [Action phrase]
[Brief explanation of why this step is needed.]
[Specific, concrete instruction.]
[What a successful outcome looks like at this step.]

## Step 2: [Action phrase]
...

## Troubleshooting
[Common failure point and what to do about it.]

## Next steps
[Where to go from here: related tasks, deeper reading, or what the reader just unlocked.]
```

### When to use

Teaching a reader to complete a task they have never done before, when understanding what they are doing matters as much as getting through the steps. Onboarding new users to a tool, workflow, or process where capability-building outlasts the first session. Documenting infrequent tasks that readers will return to repeatedly until the steps are internalized. Bridging the gap between reference documentation and a reader who cannot yet use that reference independently.

### When not to use

Situations where an experienced operator needs to execute a procedure correctly under pressure without pausing to read explanations. Reference lookup, where the reader already knows what they want and needs only the parameter, option, or command syntax. Conceptual or architectural overviews where the primary goal is understanding rather than task completion.

### Pairs well with

`technical-writer`, `friendly-mentor`, `instructional`, `encouraging`, `procedural`

### Often confused with

**runbook**: A runbook is an operational document written to be executed, not read for understanding. Its defining design constraint is that an operator who did not build the system must be able to complete the procedure correctly by following the steps sequentially, without needing to understand why each step exists. A runbook is not a teaching document - it is a decision aid that replaces the need to reason in the moment. A how-to guide is written for a learner who is building capability; a runbook is written for an operator who is completing a known procedure under pressure. Where a how-to guide explains, a runbook executes.

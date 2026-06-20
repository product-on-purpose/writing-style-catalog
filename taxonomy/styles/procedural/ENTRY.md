---
id: procedural
name: Procedural
axis: style
one_liner: Task-first writing that takes a reader from "I don't know how" to "I did it" by organizing every decision around user goals, not system features.
description: |
  A how-to tutorial is a success contract with the reader. It opens with the task - not the
  history of the technology, not the theory of operation, not a context-setting paragraph about
  why this matters. The reader is already motivated; they arrived because they want to do
  something. Every word that precedes the first step is a word the reader skips.

  Step numbers are sacred in this structure. Each numbered step contains exactly one action. Not
  one concept, not one paragraph of background, not two related actions that happen to be adjacent
  in the interface - one action. "Click Save" is a step. "Configure your settings and save" is two
  steps. When steps contain multiple actions, readers lose their place, skip one, and then blame
  themselves for the failure that follows.

  The test of a how-to tutorial is functional: can a reader complete the task by following it?
  If the tutorial passes this test, it succeeds regardless of prose elegance. If it fails this
  test, no amount of clarity in the writing rescues it. This is the axis of quality that
  distinguishes how-to writing from all other expository forms.
structural_conventions:
  - Opens with a one-sentence statement of the task goal, not background context
  - Each numbered step contains exactly one action
  - Prerequisites listed before step one, not embedded inside steps
  - Expected outcomes or confirmation signals follow steps where the result is not obvious
  - Warnings and cautions precede the step they apply to, never follow it
  - Ends with confirmation that the task is complete, not a summary of what was done
frame: procedural
evidence_types:
  - step-by-step instructions
  - screenshots or command output
  - expected outcomes per step
  - prerequisites list
reader_contract: "By the end of this tutorial, you will have completed the task successfully."
classical_mode: exposition
pairs_well_with:
  - technical-writer
  - instructional
  - friendly-mentor
avoid_with:
  - columnist
  - devotional-reflection
  - reverent
confusable_with:
  - diataxis-explanation
when_to_use:
  - The reader needs to accomplish a specific, bounded task
  - The outcome is verifiable - the reader can confirm they succeeded
  - The procedure has a defined sequence of steps
  - Onboarding flows where the reader needs a quick first success
  - Troubleshooting guides where each resolution path is a task
when_not_to_use:
  - The reader needs to understand how a system works, not just operate it
  - The subject is conceptual rather than procedural
  - The correct procedure depends heavily on context the tutorial cannot predict
  - The goal is to build judgment, not to execute a fixed sequence
llm_instruction_phrasing: |
  Write as a how-to tutorial. The very first line states the task goal in one sentence. List any
  prerequisites before step one. Number every step and put exactly one action in each step - not
  one paragraph, not one concept, one action. Where the result of a step is not obvious, add a
  brief expected-outcome note after the step. Put warnings before the step they apply to. Close
  with a one-sentence confirmation that the task is now complete. Do not add background context,
  explanatory asides, or section headers that delay the steps.
tags:
  - tutorial
  - procedural
  - task-based
  - instructional
  - technical
review_status: stable
---

## How-To Tutorial

A how-to tutorial is a success contract with the reader. It opens with the task - not the history of the technology, not the theory of operation, not a context-setting paragraph about why this matters. The reader is already motivated; they arrived because they want to do something. Every word that precedes the first step is a word the reader skips.

Step numbers are sacred in this structure. Each numbered step contains exactly one action. Not one concept, not one paragraph of background, not two related actions that happen to be adjacent in the interface - one action. "Click Save" is a step. "Configure your settings and save" is two steps. When steps contain multiple actions, readers lose their place, skip one, and then blame themselves for the failure that follows.

The test of a how-to tutorial is functional: can a reader complete the task by following it? If the tutorial passes this test, it succeeds regardless of prose elegance. If it fails this test, no amount of clarity in the writing rescues it. This is the axis of quality that distinguishes how-to writing from all other expository forms.

### Structural conventions

- Opens with a one-sentence statement of the task goal, not background context
- Each numbered step contains exactly one action
- Prerequisites listed before step one, not embedded inside steps
- Expected outcomes or confirmation signals follow steps where the result is not obvious
- Warnings and cautions precede the step they apply to, never follow it
- Ends with confirmation that the task is complete, not a summary of what was done

### When to use

When the reader needs to accomplish a specific, bounded task with a verifiable outcome. Ideal for onboarding flows where a quick first success builds confidence, for troubleshooting guides where each resolution path is a distinct task, and for any procedure with a fixed sequence that must be followed in order.

### When not to use

When the reader needs to understand how a system works rather than just operate it. Avoid when the subject is conceptual, when the correct procedure depends heavily on context the tutorial cannot anticipate, or when the goal is to build judgment and reasoning rather than execute a fixed sequence.

### Pairs well with

`technical-writer`, `instructional`, `friendly-mentor`

### Often confused with

**diataxis-explanation**: A Diataxis explanation is designed to build understanding - it answers "how does this work?" A how-to tutorial is designed to produce a completed action - it answers "how do I do this?" The distinction is functional: explanations serve comprehension; tutorials serve task completion. The same subject can yield two completely different documents depending on which goal governs the writing.

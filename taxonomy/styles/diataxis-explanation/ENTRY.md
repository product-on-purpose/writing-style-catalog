---
id: diataxis-explanation
name: Diataxis Explanation
axis: style
one_liner: The Diataxis "Explanation" mode - oriented toward understanding rather than action, building a conceptual model for the reader.
description: |
  Diataxis (from Daniele Procida's framework) distinguishes four modes of documentation: tutorial
  (learning by doing), how-to (achieving a goal), reference (looking things up), and explanation
  (understanding why things are the way they are). The explanation mode is the one most often
  missing from technical writing - and the one that makes the other three make sense.

  An explanation piece does not tell you how to do something. It tells you what something is, why
  it was designed this way, what tradeoffs were made, how it relates to other concepts. It is the
  mode that builds the mental model that makes how-to guides navigable. Without explanation,
  readers follow steps without understanding; they succeed when the steps apply and fail when the
  situation varies.

  Explanation is oriented toward understanding, not action. A good explanation piece could be read
  with no intention of ever using the described system. It is interesting in itself.
structural_conventions:
  - Does not contain steps or procedures (those belong in how-to or tutorial)
  - Does contain "why" reasoning - design decisions, tradeoffs, origins
  - Builds concepts in order - simpler before complex
  - 'Makes relationships explicit: "X relates to Y because..."'
frame: expository-conceptual
evidence_types:
  - analogies
  - conceptual diagrams described in prose
  - historical context
  - design rationale
reader_contract: "By the end, you will understand why this works the way it does."
classical_mode: exposition
pairs_well_with:
  - friendly-mentor
  - candid
  - warm
  - blog-post-long-form
confusable_with:
  - comparison-contrast
avoid_with:
  - operator
when_to_use:
  - Concept documentation
  - Architecture explanations
  - '"Why does X work this way" posts'
  - Onboarding to a new domain
  - Design system rationale
when_not_to_use:
  - When the reader needs to accomplish a specific task right now
  - Runbooks and operational guides
  - Reference documentation
tells:
  - 'Oriented toward understanding, not action - it could be read with no intention of ever using the system'
  - 'Contains no steps or procedures; those belong to how-to or tutorial'
  - 'Supplies "why" reasoning - design decisions, tradeoffs, origins - and uses "because" freely'
  - 'Builds concepts in order, simpler before complex'
  - 'Makes relationships between concepts explicit ("X relates to Y because...")'
  - 'Aims to leave the reader with a mental model that makes the how-to guides navigable'
anti_patterns:
  - pattern: 'Slipping numbered steps or a "do this, then that" procedure into the explanation'
    why: 'Producing a completed action is the job of how-to or tutorial; explanation serves comprehension and loses its orientation the moment it starts instructing.'
  - pattern: 'Setting two systems side by side and measuring them against each other'
    why: 'Weighing two subjects on parallel dimensions is comparison-contrast, a confusable neighbor; explanation examines a single subject in depth to build understanding.'
  - pattern: 'Stating the conclusion and elaborating it directly when the goal was to lead the reader to reason it out'
    why: 'Asking questions the reader answers in their own head is Socratic inquiry; explanation does state the model, but if the intent was reader-built insight this is the wrong style.'
failure_modes:
  - mode: 'Over-pursues complete understanding until the explanation balloons into conceptual scope-creep, surrounding the subject with so much context, history, and rationale that no graspable model ever crystallizes'
    mitigation: 'Understanding is the goal, but a usable mental model is the deliverable; bound the explanation to the concepts that make this subject make sense rather than chasing every adjacent why.'
  - mode: 'Indulges theory for its own sake, building abstraction on abstraction until the reader can follow each sentence yet cannot say what the thing is or why it matters'
    mitigation: 'Tie the why-reasoning back to something the reader can hold - an example, an analogy, a concrete consequence - so the model lands instead of floating.'
llm_instruction_phrasing: |
  Write in Diataxis explanation mode. Your goal is understanding, not action - do not include steps
  or procedures. Build the reader's mental model: explain what it is, why it is designed this way,
  what tradeoffs were made, how it relates to other concepts. Use the word "because" frequently.
  Make relationships explicit. Build from simpler concepts to complex ones. The piece should be
  interesting to read even by someone who never intends to use the described system.
tags:
  - conceptual
  - documentation
  - diataxis
  - understanding
  - technical-writing
  - why-oriented
review_status: stable
---

## Diataxis Explanation

Diataxis (from Daniele Procida's framework) distinguishes four modes of documentation: tutorial (learning by doing), how-to (achieving a goal), reference (looking things up), and explanation (understanding why things are the way they are). The explanation mode is the one most often missing from technical writing - and the one that makes the other three make sense.

An explanation piece does not tell you how to do something. It tells you what something is, why it was designed this way, what tradeoffs were made, how it relates to other concepts. It is the mode that builds the mental model that makes how-to guides navigable. Without explanation, readers follow steps without understanding; they succeed when the steps apply and fail when the situation varies.

Explanation is oriented toward understanding, not action. A good explanation piece could be read with no intention of ever using the described system. It is interesting in itself.

### Structural conventions

- Does not contain steps or procedures (those belong in how-to or tutorial)
- Does contain "why" reasoning: design decisions, tradeoffs, origins
- Builds concepts in order: simpler before complex
- Makes relationships explicit: "X relates to Y because..."

### When to use

Concept docs, architecture explanations, "why does X work this way" posts, onboarding to a new domain, design system rationale.

### When not to use

When the reader needs to accomplish a specific task right now. Runbooks, operational guides, reference documentation.

### Pairs well with

`friendly-mentor`, `candid`, `warm`, `blog-post-long-form`

### Often confused with

**comparison-contrast**: Comparison-contrast requires at least two subjects measured against each other. Diataxis explanation examines a single subject in depth to build understanding.

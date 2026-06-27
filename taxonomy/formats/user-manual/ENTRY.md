---
id: user-manual
name: User Manual
axis: format
domain: professional
family: instruction
one_liner: Comprehensive documentation covering everything a user can do with a product, organized for lookup.
description: |
  A user manual is comprehensive documentation that covers everything a user can do with a
  product, organized so a reader can look up any feature or task when they need it. Unlike
  documentation designed to be read from start to finish, a user manual is a reference artifact:
  the reader arrives with a specific question, locates the relevant section, reads what they need,
  and returns to the product. Completeness and reliable retrieval across the whole product surface
  are the defining values.

  The format earns its place by serving a reader who already knows what they want to accomplish
  but needs the exact steps, parameters, or options for this specific product. A user manual
  assumes a capable reader who is not new to the product category but may be unfamiliar with this
  product's conventions. It documents the product as it is, not as a teaching exercise, and trusts
  the reader to apply the information without capability-building scaffolding.

  Good user manuals are organized for lookup, not for reading. The table of contents is a
  navigational instrument. Section titles name features and tasks in terms the reader will
  recognize when searching for them - not terms organized by system architecture or build sequence.
  Each section is self-contained enough that a reader can enter from the table of contents and find
  what they need without reading surrounding sections.

  Unlike a how-to guide, which teaches one task end to end for a learner building capability, a
  user manual documents all tasks and features for a reader who arrives knowing what they want and
  consulting the relevant section the way one uses a dictionary rather than a tutorial.
canonical_template: |
  # [Product Name] User Manual

  ## Table of Contents

  [Section list organized by feature or task name]

  ## Getting Started

  [System requirements, installation, account setup, and first-session prerequisites.]

  ## [Feature or Task Area 1]

  ### [Task or Subtask Name]

  [Brief statement of what this feature does and when a user would reach for it.]

  Steps:
  1. [Concrete instruction]
  2. [Concrete instruction]
  ...

  Options / Parameters:
  - [Option name]: [What it controls, valid values or range]

  Notes:
  - [Edge case, constraint, or version-specific behavior]

  ## [Feature or Task Area 2]

  ...

  ## Troubleshooting

  [Symptom]: [Cause and resolution]

  ## Reference

  [Index, glossary, or quick-reference tables]
typical_voices:
  - technical-writer
  - operator
typical_tones:
  - instructional
  - matter-of-fact
digital_or_print: both
pairs_well_with:
  - technical-writer
  - operator
  - instructional
  - matter-of-fact
  - procedural
avoid_with:
  - confessional
  - reverent
  - playful
confusable_with:
  - how-to-guide
  - technical-reference
when_to_use:
  - Documenting a product or tool where users need to look up specific features or tasks at the moment of need rather than learn the product from scratch
  - Shipping the authoritative reference alongside a product that users will return to repeatedly across many sessions
  - Covering the full surface area of a product when one how-to guide per task would be impractical
  - Supporting users at all experience levels who need lookup access to features they have not yet used
  - Creating a lasting reference whose modular section structure remains accurate and maintainable across product versions
when_not_to_use:
  - Teaching a complete beginner who needs guided, capability-building instruction through a specific task for the first time (use a how-to guide)
  - Providing quick expert lookup for parameters, flags, or syntax when the reader already knows exactly what they need (use API reference or a cheat sheet)
  - Explaining concepts, background, or architectural decisions that do not map to a specific task or feature the user can perform
tells:
  - 'A table of contents that lists features and tasks by name, functioning as the primary navigation instrument for the document'
  - 'Self-contained sections a reader can enter directly from the table of contents without reading surrounding material'
  - 'Feature-first or task-first organization, not arranged by system architecture or development sequence'
  - 'Terse, declarative prose that names what the product does rather than teaching the reader why it works or building capability'
  - 'Step-numbered instructions within sections that rely on product terminology without defining it from first principles'
  - 'Cross-references within sections pointing to related features rather than prescribing a linear reading sequence'
anti_patterns:
  - pattern: 'Organizing sections by system architecture or internal component rather than by user task or feature name'
    why: 'A user who wants to accomplish something thinks in task terms, not system terms. Architecture-first organization forces readers to know how the product is built before they can find what they need to do.'
  - pattern: 'Writing each section as a how-to guide complete with prerequisites blocks, capability-building explanations of why each step matters, and troubleshooting for the learner'
    why: 'A how-to guide teaches one task end to end for a reader who is building capability and wants to understand what they are doing. A user manual documents all features for a reader who arrives with capability already and needs only the specific steps for this product. Teaching scaffolding in a reference document slows down a reader who came to look something up.'
  - pattern: 'Omitting a navigable table of contents, or organizing the table of contents to mirror the product build order rather than user lookup order'
    why: 'The table of contents is the primary navigation instrument of a user manual. A reader who cannot locate the right section from the table of contents cannot use the manual. Lookup order matters more than order-of-construction logic.'
failure_modes:
  - mode: 'Over-comprehensive - the commitment to covering the whole product surface drives the manual into exhaustive edge-case documentation, so every common task is buried in variant tables and parameter matrices that serve no reader who has just arrived with a single question'
    mitigation: 'Organize comprehensiveness hierarchically: standard cases prominent in the section body, edge cases and full parameter tables in sub-sections or appendices. A reader who needs the edge case will find it; a reader who does not need it will not be slowed by it.'
  - mode: 'Over-terse - the reference register is pushed so far that sections become command listings and parameter names with no context, producing output only parseable by a reader who already knows what the feature does and why they want it'
    mitigation: 'Each section needs at minimum a brief statement of what the feature does and when a user would reach for it. Even in a reference register, that one sentence of orientation is not teaching - it is the anchor that makes the steps that follow usable.'
  - mode: 'Over-modular - the self-contained section principle is taken to the extreme, repeating boilerplate across every section that shares a concept, inflating the document and introducing contradictions when updates touch only some of the duplicated content'
    mitigation: 'Use cross-references and a central Reference section for shared concepts rather than duplicating content. Trust the reader to follow a link. Redundancy that seemed helpful in authoring becomes a maintenance liability and a trust eroder when sections drift out of sync.'
llm_instruction_phrasing: |
  Write as a User Manual. Organize the content by user task or feature name, not by system
  architecture or development sequence. Begin with a navigable table of contents that lists
  sections in lookup order. Write each section to be self-contained: a reader who enters from the
  table of contents should find what they need without reading surrounding sections.

  Within each section, open with a brief statement of what the feature does and when a user would
  reach for it. Then give the steps in numbered form, using concrete instructions and
  product-specific terminology. Include options, parameters, or valid values where relevant.
  Collect edge cases and notes at the end of the section or in a sub-section, not inline in the
  main steps.

  Use terse, declarative prose throughout. Do not teach the reader why the product works the way
  it does; document what it does and how to use it. Do not add capability-building scaffolding.
  Add cross-references to related sections rather than repeating content. Close the manual with a
  Troubleshooting section and a Reference section (index, glossary, or quick-reference tables).
tags:
  - documentation
  - reference
  - technical
  - product
  - instruction
review_status: draft
---

## User Manual

A user manual is comprehensive documentation that covers everything a user can do with a
product, organized so a reader can look up any feature or task when they need it. Unlike
documentation designed to be read from start to finish, a user manual is a reference artifact:
the reader arrives with a specific question, locates the relevant section, reads what they need,
and returns to the product. Completeness and reliable retrieval across the whole product surface
are the defining values.

The format earns its place by serving a reader who already knows what they want to accomplish
but needs the exact steps, parameters, or options for this specific product. A user manual
assumes a capable reader who is not new to the product category but may be unfamiliar with this
product's conventions. It documents the product as it is, not as a teaching exercise, and trusts
the reader to apply the information without capability-building scaffolding.

Good user manuals are organized for lookup, not for reading. The table of contents is a
navigational instrument. Section titles name features and tasks in terms the reader will
recognize when searching for them - not terms organized by system architecture or build sequence.
Each section is self-contained enough that a reader can enter from the table of contents and find
what they need without reading surrounding sections.

Unlike a how-to guide, which teaches one task end to end for a learner building capability, a
user manual documents all tasks and features for a reader who arrives knowing what they want and
consulting the relevant section the way one uses a dictionary rather than a tutorial.

### Canonical template

```
# [Product Name] User Manual

## Table of Contents
[Section list organized by feature or task name]

## Getting Started
[System requirements, installation, account setup, and first-session prerequisites.]

## [Feature or Task Area 1]

### [Task or Subtask Name]
[Brief statement of what this feature does and when a user would reach for it.]

Steps:
1. [Concrete instruction]
2. [Concrete instruction]
...

Options / Parameters:
- [Option name]: [What it controls, valid values or range]

Notes:
- [Edge case, constraint, or version-specific behavior]

## [Feature or Task Area 2]
...

## Troubleshooting
[Symptom]: [Cause and resolution]

## Reference
[Index, glossary, or quick-reference tables]
```

### When to use

Documenting a product or tool where users need to look up specific features or tasks at the moment of need rather than learn the product from scratch. Shipping the authoritative reference alongside a product that users will return to repeatedly across many sessions. Covering the full surface area of a product when one how-to guide per task would be impractical. Supporting users at all experience levels who need lookup access to features they have not yet used. Creating a lasting reference whose modular section structure remains accurate and maintainable across product versions.

### When not to use

Teaching a complete beginner who needs guided, capability-building instruction through a specific task for the first time (use a how-to guide). Providing quick expert lookup for parameters, flags, or syntax when the reader already knows exactly what they need (use API reference or a cheat sheet). Explaining concepts, background, or architectural decisions that do not map to a specific task or feature the user can perform.

### Pairs well with

`technical-writer`, `operator`, `instructional`, `matter-of-fact`, `procedural`

### Often confused with

**how-to-guide**: A how-to guide teaches a reader to accomplish one specific task they do not yet know how to do, walking them through the steps with enough context to understand what they are doing and why. The goal is a reader who, having followed the guide once, could reproduce the task without the guide the second time - capability, not just completion, is the measure. A user manual is not a teaching document: it covers all tasks and features across the whole product surface for a reader who already has capability and arrives to look up a specific thing. Where a how-to guide takes a learner through one task end to end, a user manual is consulted the way one uses a dictionary rather than a tutorial.

**technical-reference**: A technical reference is a precise specification of inputs, outputs, and syntax for a developer artifact (API, library, CLI, config schema), organized by signature, parameters, and returns. A user manual is whole-product, end-user task and feature coverage with numbered procedural steps. The discriminator: if the unit of organization is a function, endpoint, or field, it is a technical reference; if it is a user-facing feature or task with steps, it is a user manual.

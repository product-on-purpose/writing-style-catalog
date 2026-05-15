---
id: frequently-asked-questions
name: Frequently Asked Questions
axis: style
one_liner: Sections are real reader questions in their natural phrasing, ordered by likelihood of being asked rather than by logical flow.
description: |
  The FAQ style organizes a piece around the questions a real reader would actually type or speak,
  ordered by how likely each one is to come up. It is not an outline disguised as questions; it is
  a structure built from the reader's mental model of the topic, not the writer's. Done well, a
  reader can land on any single question, get a complete answer, and leave - or stay and read the
  next one because it is the next thing they would naturally ask.

  Three disciplines distinguish a real FAQ from a fake one. First, the questions must be in the
  reader's voice, not the writer's - "How do I cancel?" not "On the topic of cancellation." Second,
  each answer must be self-sufficient. A reader who arrived via search or a deep link should not
  need to read the preceding question to make sense of the current one. Third, the order is
  empirical: which questions come up most often, asked first. Logical flow is a secondary concern,
  and sometimes a casualty.

  The FAQ is fundamentally a multi-entry-point format. The reader is not expected to read it
  linearly. This is its strength when the audience is heterogeneous and its weakness when the
  material needs to build a single conceptual model: each answer in isolation cannot do what a
  sustained explanation can.
structural_conventions:
  - Each section header is a question phrased the way a reader would actually ask it, not a topic
  - Questions ordered by frequency or urgency of being asked, not by logical dependency
  - Each answer is self-contained - a reader arriving at one question via search should not need to read earlier ones
  - Answers are direct and lead with the answer, not the setup ("Yes, you can. To do it..." not "Many users wonder...")
  - Cross-links between related questions are explicit when an answer depends on context from elsewhere
frame: expository
evidence_types:
  - direct procedural answers
  - examples
  - cross-references
  - decision trees
reader_contract: "By the end of any one question, you will have a complete answer to that question - without needing to have read the others."
classical_mode: exposition
pairs_well_with:
  - technical-writer
  - instructional
  - technical-reference
  - readme
avoid_with:
  - pastoral
  - storyteller
confusable_with:
  - how-to-tutorial
when_to_use:
  - Support documentation where readers arrive via search
  - Product help pages with heterogeneous audiences
  - Onboarding material covering questions of varying scope
  - Policy or compliance documents that need to be navigable
when_not_to_use:
  - Material that builds a single conceptual model the reader must absorb in order
  - Narrative or reflective writing
  - Content where the reader has not yet formed any questions
  - Tutorials with a single intended path
llm_instruction_phrasing: |
  Write using a frequently asked questions structure. Each section header is a question phrased the
  way a real reader would ask it, in their voice, not yours. Order the questions by how likely or
  urgent they are to come up, not by what would make a tidy outline. Each answer must be
  self-contained - a reader who arrived at one question via search must not need to read the others
  to understand it. Lead each answer with the answer itself, not setup. If two answers depend on
  shared context, repeat the context or cross-link explicitly. The reader is not reading top to
  bottom; treat every question as an entry point.
tags:
  - reference
  - navigable
  - reader-driven
  - multi-path
  - questioning
review_status: stable
---

## Frequently Asked Questions

The FAQ style organizes a piece around the questions a real reader would actually type or speak, ordered by how likely each one is to come up. It is not an outline disguised as questions; it is a structure built from the reader's mental model of the topic, not the writer's. Done well, a reader can land on any single question, get a complete answer, and leave - or stay and read the next one because it is the next thing they would naturally ask.

Three disciplines distinguish a real FAQ from a fake one. First, the questions must be in the reader's voice, not the writer's - "How do I cancel?" not "On the topic of cancellation." Second, each answer must be self-sufficient. A reader who arrived via search or a deep link should not need to read the preceding question to make sense of the current one. Third, the order is empirical: which questions come up most often, asked first. Logical flow is a secondary concern, and sometimes a casualty.

The FAQ is fundamentally a multi-entry-point format. The reader is not expected to read it linearly. This is its strength when the audience is heterogeneous and its weakness when the material needs to build a single conceptual model: each answer in isolation cannot do what a sustained explanation can.

### Structural conventions

- Each section header is a question phrased the way a reader would actually ask it, not a topic
- Questions ordered by frequency or urgency of being asked, not by logical dependency
- Each answer is self-contained - a reader arriving at one question via search should not need to read earlier ones
- Answers are direct and lead with the answer, not the setup ("Yes, you can. To do it..." not "Many users wonder...")
- Cross-links between related questions are explicit when an answer depends on context from elsewhere

### When to use

Support documentation where readers arrive via search, product help pages with heterogeneous audiences, onboarding material covering questions of varying scope, policy or compliance documents that need to be navigable.

### When not to use

Material that builds a single conceptual model the reader must absorb in order, narrative or reflective writing, content where the reader has not yet formed any questions, tutorials with a single intended path.

### Pairs well with

`technical-writer`, `instructional`, `technical-reference`, `readme`

### Often confused with

**how-to-tutorial**: A how-to tutorial assumes a single ordered path - step one, then step two, then step three - and the reader is expected to follow that path. An FAQ assumes many readers arriving at many points, each needing only their one answer. If the material has one correct order, it is a tutorial; if it has many, it is an FAQ.

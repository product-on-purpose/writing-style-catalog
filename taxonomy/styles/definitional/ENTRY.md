---
id: definitional
name: Definitional
axis: style
one_liner: Leads with a definition and elaborates through its facets, edge cases, and what-it-is-not - the definition is the load-bearing first move.
description: |
  Definitional writing puts the definition first and then tests it. The opening sentence or
  paragraph names what the thing is - precisely enough that the reader could use the definition to
  decide whether a given example counts. Everything that follows refines or stresses that
  definition: the facets it has, the edge cases it survives, the adjacent things it is not. The
  definition is not a summary at the end; it is the load-bearing first move, and the rest of the
  piece earns it.

  The discipline of definitional writing is the negative space. A good definition is as much about
  what the term excludes as what it includes. "Refactoring is changing the structure of code
  without changing its behavior" only does its work if the reader understands that changing
  behavior would not count - and the piece must show that, often through cases that look like
  refactoring but are not. The "what it is not" section is where the definition is tested under
  load.

  Definitional writing is the form of the glossary entry, the concept page, the "what is X"
  article. It fails when the definition is vague enough that no example could fail it, and when the
  elaboration loses the thread by drifting into adjacent topics. A reader who finishes a
  definitional piece should be able to apply the definition to a new case - that is the test of
  whether the piece worked.
structural_conventions:
  - The definition appears in the opening, often the first sentence, and is precise enough to discriminate cases
  - The body elaborates the definition through facets, components, or distinguishing features - not through narrative or argument
  - At least one section addresses what the term is not, with concrete adjacent cases that fail the definition
  - Examples are used to test the definition rather than to illustrate atmosphere - each example should be answerable as "does this count or not?"
  - The piece does not end on a new claim; it ends on a refined or stress-tested version of the opening definition
frame: expository
evidence_types:
  - bordering examples that do and do not fit the definition
  - decompositions into facets
  - etymological or historical clarification when relevant
  - contrast with adjacent terms
reader_contract: "By the end, you will be able to apply the definition to a new case and say whether it counts."
classical_mode: exposition
pairs_well_with:
  - technical-writer
  - diataxis-explanation
  - technical-reference
avoid_with:
  - storyteller
  - pastoral
confusable_with:
  - diataxis-explanation
when_to_use:
  - Glossary and concept reference pages
  - '"What is X" introductory articles'
  - Disambiguation between similar terms
  - Foundational documentation that other docs will build on
when_not_to_use:
  - Narrative or experiential writing
  - Argumentative pieces where the term is contested
  - Material covering questions across many concepts (use FAQ instead)
  - Devotional or reflective writing
llm_instruction_phrasing: |
  Write using definitional structure. Lead with the definition - the first sentence or short
  opening paragraph names what the thing is, precisely enough that the reader could use the
  definition to decide whether a given example counts. Elaborate through the definition's facets,
  components, or distinguishing features rather than through narrative or argument. Include a
  section on what the term is not, with concrete adjacent cases that fail the definition. Use
  examples to test the definition, not to add atmosphere - each example should be answerable as
  "does this count or not?" End on a refined or stress-tested version of the opening definition,
  not on a new claim.
tags:
  - reference
  - expository
  - conceptual
  - precise
  - foundational
review_status: stable
---

## Definitional

Definitional writing puts the definition first and then tests it. The opening sentence or paragraph names what the thing is - precisely enough that the reader could use the definition to decide whether a given example counts. Everything that follows refines or stresses that definition: the facets it has, the edge cases it survives, the adjacent things it is not. The definition is not a summary at the end; it is the load-bearing first move, and the rest of the piece earns it.

The discipline of definitional writing is the negative space. A good definition is as much about what the term excludes as what it includes. "Refactoring is changing the structure of code without changing its behavior" only does its work if the reader understands that changing behavior would not count - and the piece must show that, often through cases that look like refactoring but are not. The "what it is not" section is where the definition is tested under load.

Definitional writing is the form of the glossary entry, the concept page, the "what is X" article. It fails when the definition is vague enough that no example could fail it, and when the elaboration loses the thread by drifting into adjacent topics. A reader who finishes a definitional piece should be able to apply the definition to a new case - that is the test of whether the piece worked.

### Structural conventions

- The definition appears in the opening, often the first sentence, and is precise enough to discriminate cases
- The body elaborates the definition through facets, components, or distinguishing features - not through narrative or argument
- At least one section addresses what the term is not, with concrete adjacent cases that fail the definition
- Examples are used to test the definition rather than to illustrate atmosphere - each example should be answerable as "does this count or not?"
- The piece does not end on a new claim; it ends on a refined or stress-tested version of the opening definition

### When to use

Glossary and concept reference pages, "what is X" introductory articles, disambiguation between similar terms, foundational documentation that other docs will build on.

### When not to use

Narrative or experiential writing, argumentative pieces where the term is contested, material covering questions across many concepts (use FAQ instead), devotional or reflective writing.

### Pairs well with

`technical-writer`, `diataxis-explanation`, `technical-reference`

### Often confused with

**diataxis-explanation**: Diataxis explanation can use any structure - narrative, comparison, analogy, model-building - to convey understanding of a concept. Definitional commits to a specific structural move: lead with a precise definition, then test and elaborate it. A diataxis explanation might include a definition; a definitional piece is built around one.

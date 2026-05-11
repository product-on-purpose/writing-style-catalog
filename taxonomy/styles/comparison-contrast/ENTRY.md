---
id: comparison-contrast
name: Comparison-Contrast
axis: style
one_liner: Places two or more options, ideas, or states side by side to illuminate the differences that matter.
description: |
  Comparison-contrast is the style of the decision document and the analytical essay. Its power
  comes from the precision that side-by-side placement creates: similarities and differences emerge
  that would be invisible in a sequential treatment of each option. The reader comes away not just
  knowing both options but knowing the delta - which is usually what they needed.

  Two structural approaches exist. Block structure presents everything about A, then everything
  about B - better for complex subjects where the reader needs to understand each option fully
  before comparing. Alternating structure moves back and forth between A and B on each dimension -
  better for focused comparisons where the points of contrast are the main event.

  The risk of comparison-contrast is false balance: treating two things as equally deserving of
  parallel treatment when one is clearly better for the reader's situation. The style is most
  honest when it selects dimensions of comparison that actually matter for the decision at hand,
  not every dimension on which the options differ.
structural_conventions:
  - Establishes the comparison frame early - "We are comparing X and Y on dimensions D1, D2, D3"
  - Either block structure (all of A, then all of B) or alternating structure (A vs B on D1, then D2, etc.)
  - A summary comparison (usually a table or verdict) resolves the structure
  - Dimensions of comparison selected for relevance, not exhaustiveness
frame: expository-analytical
evidence_types:
  - side-by-side data
  - concrete examples for each option
  - a decision recommendation
reader_contract: "By the end, you will understand the key differences between the options and have a basis for choosing."
classical_mode: exposition
pairs_well_with:
  - pragmatic-architect
  - matter-of-fact
  - candid
  - adr
confusable_with:
  - classical-argument
  - problem-solution
avoid_with:
  - devotional-reflection
  - reverent
  - pastoral
when_to_use:
  - Technology selection documents
  - Architecture decision records
  - Research reports
  - Product comparisons
  - Any decision involving multiple options
when_not_to_use:
  - Single-subject explanations
  - Narrative writing
  - Persuasive essays with a settled conclusion
llm_instruction_phrasing: |
  Write using comparison-contrast structure. Establish the comparison frame early: name what you
  are comparing and on which dimensions. Choose between block structure (all of A, then all of B)
  or alternating structure (A vs B per dimension) based on complexity. Select dimensions that
  matter for the decision at hand - do not compare on every axis, only the relevant ones. End with
  a summary that resolves the structure: a table, a verdict, or a clear statement of the key
  differentiator. Avoid false balance - if one option is clearly better for the stated situation,
  say so.
tags:
  - analytical
  - decision-support
  - structured
  - comparative
  - professional
review_status: stable
---

## Comparison-Contrast

Comparison-contrast is the style of the decision document and the analytical essay. Its power comes from the precision that side-by-side placement creates: similarities and differences emerge that would be invisible in a sequential treatment of each option. The reader comes away not just knowing both options but knowing the delta - which is usually what they needed.

Two structural approaches exist. Block structure presents everything about A, then everything about B - better for complex subjects where the reader needs to understand each option fully before comparing. Alternating structure moves back and forth between A and B on each dimension - better for focused comparisons where the points of contrast are the main event.

The risk of comparison-contrast is false balance: treating two things as equally deserving of parallel treatment when one is clearly better for the reader's situation. The style is most honest when it selects dimensions of comparison that actually matter for the decision at hand, not every dimension on which the options differ.

### Structural conventions

- Establishes the comparison frame early: "We are comparing X and Y on dimensions D1, D2, D3"
- Either block structure (all of A, then all of B) or alternating structure (A vs B on D1, then D2, etc.)
- A summary comparison (usually a table or verdict) resolves the structure
- Dimensions of comparison selected for relevance, not exhaustiveness

### When to use

Technology selection docs, ADRs, research reports, product comparisons, any decision involving multiple options.

### When not to use

Single-subject explanations, narrative writing, persuasive essays with a settled conclusion.

### Pairs well with

`pragmatic-architect`, `matter-of-fact`, `candid`, `adr`

### Often confused with

**classical-argument**: Classical argument examines one position and defends it against objections. Comparison-contrast requires at least two subjects and measures relative differences without necessarily advocating for one.

**problem-solution**: Problem-solution names a pain and proposes a fix. Comparison-contrast evaluates options for a reader who is making a choice - the "problem" may already be understood.

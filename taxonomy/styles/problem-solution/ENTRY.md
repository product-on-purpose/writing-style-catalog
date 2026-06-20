---
id: problem-solution
name: Problem-Solution
axis: style
one_liner: Frames the piece as a diagnosis followed by a remedy - establishes the pain before the cure.
description: |
  Problem-solution is the workhorse of professional writing. It earns the reader's attention by
  naming what they already feel (the problem) before proposing anything (the solution). The pattern
  works because it meets the reader where they are: already experiencing the friction, already
  asking "why is this hard?" The solution then arrives as a response to a question the reader is
  already asking.

  The key discipline of problem-solution is specificity. A vague problem statement ("organizations
  face many challenges with process") earns nothing. A specific problem statement ("the deploy
  pipeline takes 45 minutes and blocks three engineers every afternoon") creates attention and
  stakes. The solution must then address the specific problem named, not a generalized version of
  it.

  Problem-solution is not Problem-Complaint. It must arrive at the remedy. A piece that diagnoses
  brilliantly and then ends without a path forward has only done half the work.
structural_conventions:
  - Problem stated before solution, never after
  - Problem section must be specific enough that the reader can confirm "yes, this is my situation"
  - Solution section addresses the specific problem named, not a generalized one
  - 'Optional: "before/after" contrast to show the delta'
frame: expository-argumentative
evidence_types:
  - concrete examples
  - before/after comparisons
  - statistics naming the cost of the problem
reader_contract: "By the end, you will understand what the problem is and have a concrete path to address it."
classical_mode: exposition
pairs_well_with:
  - pragmatic-architect
  - operator
  - candid
  - matter-of-fact
  - adr
  - prd
avoid_with:
  - devotional-reflection
  - reverent
  - pastoral
confusable_with:
  - comparison-contrast
  - classical-argument
when_to_use:
  - Technical proposals
  - Product requirement documents
  - Pitch decks and executive summaries
  - Blog posts addressing a real pain point
when_not_to_use:
  - Devotional writing
  - Narrative content
  - Contexts where the reader has not experienced the problem
tells:
  - 'States the problem before the solution, never after'
  - 'The problem is specific enough that the reader can confirm "yes, this is my situation"'
  - 'The solution addresses the specific problem named, not a generalized version of it'
  - 'Often draws a before/after contrast to show the delta the remedy creates'
  - 'Arrives at a concrete path forward rather than ending at the diagnosis'
  - 'Meets the reader inside a friction they already feel, so the solution answers a question already being asked'
anti_patterns:
  - pattern: 'Opening with a vague problem ("organizations face many challenges with process") instead of a concrete pain'
    why: 'A generic problem statement earns no attention or stakes; specificity is what makes the reader recognize their own situation and care about the fix.'
  - pattern: 'Diagnosing brilliantly and then ending without a remedy'
    why: 'This is Problem-Complaint, not problem-solution; the form must arrive at a path forward or it has done only half the work.'
  - pattern: 'Weighing several options against each other on parallel dimensions for the reader to choose among'
    why: 'Evaluating options relative to each other is comparison-contrast, a confusable neighbor; problem-solution names one pain and proposes one fix for it.'
failure_modes:
  - mode: 'Inflates the problem to glorify the solution, over-dramatizing the pain and its cost so the remedy looks more impressive and necessary than it actually is'
    mitigation: 'Size the problem honestly; the solution should fit the pain as named, and a remedy propped up by an exaggerated problem collapses the moment the reader recognizes the inflation.'
  - mode: 'Over-specifies the diagnosis until the problem section sprawls into an exhaustive account of the pain and the solution arrives starved of equivalent concreteness'
    mitigation: 'Name the problem precisely enough to create stakes, then give the solution the same specificity; the point is the remedy, not a catalogue of the suffering.'
llm_instruction_phrasing: |
  Write using problem-solution structure. Name the specific problem first - not a vague category
  but the concrete pain the reader experiences. Make the problem statement specific enough that
  the reader says "yes, that is my situation." Then introduce the solution as a direct response to
  the named problem. The solution must address what was actually named, not a generalized version.
  If you include a before/after contrast, make both sides concrete. Do not end the piece at the
  diagnosis - you must arrive at the remedy.
tags:
  - professional
  - expository
  - prescriptive
  - practical
  - direct
review_status: stable
---

## Problem-Solution

Problem-solution is the workhorse of professional writing. It earns the reader's attention by naming what they already feel (the problem) before proposing anything (the solution). The pattern works because it meets the reader where they are: already experiencing the friction, already asking "why is this hard?" The solution then arrives as a response to a question the reader is already asking.

The key discipline of problem-solution is specificity. A vague problem statement ("organizations face many challenges with process") earns nothing. A specific problem statement ("the deploy pipeline takes 45 minutes and blocks three engineers every afternoon") creates attention and stakes. The solution must then address the specific problem named, not a generalized version of it.

Problem-solution is not Problem-Complaint. It must arrive at the remedy. A piece that diagnoses brilliantly and then ends without a path forward has only done half the work.

### Structural conventions

- Problem stated before solution, never after
- Problem section must be specific enough that the reader can confirm "yes, this is my situation"
- Solution section addresses the specific problem named, not a generalized one
- Optional: "before/after" contrast to show the delta

### When to use

Technical proposals, product requirement documents, pitch decks, executive summaries, blog posts addressing a real pain point.

### When not to use

Devotional writing, narrative content, contexts where the reader has not experienced the problem.

### Pairs well with

`pragmatic-architect`, `operator`, `candid`, `matter-of-fact`, `adr`, `prd`

### Often confused with

**comparison-contrast**: Comparison-contrast traces relative differences between options. Problem-solution names a pain and proposes a fix.

**classical-argument**: Classical argument builds a defensible claim with warrant and rebuttal. Problem-solution is prescriptive (here is the fix) rather than argumentative (here is why this position is correct).

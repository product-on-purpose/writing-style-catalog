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

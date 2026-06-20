---
id: one-pager
name: One-Pager
axis: format
domain: professional
family: brief
one_liner: A single-page document that makes one argument or presents one situation. The page constraint is the discipline - everything that does not fit does not belong.
description: |
  The one-pager is a format defined entirely by its constraint: one page. That constraint is
  not aesthetic; it is functional. A one-pager forces the writer to identify the single most
  important thing they are trying to communicate and cut everything else. The reader - typically
  a decision-maker or stakeholder with limited time - gets the full picture without needing to
  extract it from a longer document. The discipline of fitting one page is the work of writing
  the one-pager; if the content does not fit, the problem is the content, not the page.

  One-pagers are used for briefings, proposals, and status updates. In each case, the format
  signals: here is the situation, here is what matters, here is what I am asking for or
  recommending. A briefing one-pager gives a decision-maker the context to engage in a meeting.
  A proposal one-pager makes an argument for a course of action. A status one-pager answers
  "where are we?" with enough detail to act but no more. The difference between these is the
  argument structure, not the format.

  The failure mode of the one-pager is using the page constraint as a reason to compress rather
  than to cut. Dense text, small fonts, and packed bullet lists that technically fit on one page
  have violated the spirit of the format. If the content cannot be written clearly in the white
  space a readable page affords, there is too much content. The one-pager is a forcing function
  for clarity, not a target for density.
canonical_template: |
  [Title - the argument or situation in one line]

  ## Situation / Background
  [2-4 sentences establishing context - what the reader needs to understand the rest]

  ## The Point
  [The central argument, recommendation, or finding - 2-5 bullet points or 2-3 sentences]

  ## Why It Matters / Implications
  [1-3 bullet points: consequences, stakes, or reasons this warrants attention]

  ## Ask / Recommendation / Next Steps
  [What you are requesting, recommending, or proposing - specific and actionable]

  [Optional: one line of supporting data, contact, or link for follow-up]
typical_voices:
  - executive
  - product-thinker
  - direct-communicator
typical_tones:
  - matter-of-fact
  - candid
  - urgent
digital_or_print: both
pairs_well_with:
  - executive
  - product-thinker
  - executive-summary
  - candid
  - matter-of-fact
avoid_with:
  - devotional-reflection
  - pastoral
  - reverent
  - playful
confusable_with:
  - prd
when_to_use:
  - Briefing a decision-maker or executive before a meeting
  - Making a proposal where a full document would not be read
  - Providing a status update to a stakeholder who needs the picture without the details
  - Communicating a situation or opportunity that requires a decision in the near term
  - Distilling a longer analysis into a form that can circulate independently
when_not_to_use:
  - Complex technical decisions that require the full context an ADR provides
  - Product requirements that will govern engineering work and need precision
  - Situations where the reader needs the full analysis to make a sound decision
  - Reference material that people will return to repeatedly
  - Documents where auditability, completeness, or versioning matters more than brevity
llm_instruction_phrasing: |
  Write as a one-pager. The entire document must fit on one printed page. Lead with a title
  that states the argument or situation in one line. Use short sections: situation, central
  point, implications, and ask or recommendation. Write for a decision-maker who has limited
  time - every sentence must earn its place. Cut context that the reader can infer. Cut
  supporting detail that does not change the conclusion. End with a specific ask or recommendation,
  not an open-ended invitation to discuss.
tags:
  - briefing
  - proposal
  - executive
  - concise
  - single-page
  - decision-support
  - print
review_status: stable
---

## One-Pager

The one-pager is a format defined entirely by its constraint: one page. That constraint is not aesthetic; it is functional. A one-pager forces the writer to identify the single most important thing they are trying to communicate and cut everything else. The reader - typically a decision-maker or stakeholder with limited time - gets the full picture without needing to extract it from a longer document. The discipline of fitting one page is the work of writing the one-pager; if the content does not fit, the problem is the content, not the page.

One-pagers are used for briefings, proposals, and status updates. In each case, the format signals: here is the situation, here is what matters, here is what I am asking for or recommending. A briefing one-pager gives a decision-maker the context to engage in a meeting. A proposal one-pager makes an argument for a course of action. A status one-pager answers "where are we?" with enough detail to act but no more. The difference between these is the argument structure, not the format.

The failure mode of the one-pager is using the page constraint as a reason to compress rather than to cut. Dense text, small fonts, and packed bullet lists that technically fit on one page have violated the spirit of the format. If the content cannot be written clearly in the white space a readable page affords, there is too much content. The one-pager is a forcing function for clarity, not a target for density.

### Canonical template

```
[Title - the argument or situation in one line]

## Situation / Background
[2-4 sentences establishing context - what the reader needs to understand the rest]

## The Point
[The central argument, recommendation, or finding - 2-5 bullet points or 2-3 sentences]

## Why It Matters / Implications
[1-3 bullet points: consequences, stakes, or reasons this warrants attention]

## Ask / Recommendation / Next Steps
[What you are requesting, recommending, or proposing - specific and actionable]

[Optional: one line of supporting data, contact, or link for follow-up]
```

### When to use

The one-pager belongs in the hands of decision-makers and stakeholders who need the full picture without the full document. Use it to brief an executive before a meeting, to make a proposal that a full document would not earn, to update a stakeholder who needs the situation without the detail, or to distill a longer analysis into something that can circulate on its own.

### When not to use

The one-pager is the wrong format when the reader genuinely needs more detail to make a sound decision - when the full context is not optional. It is also wrong for product requirements that govern engineering work, technical decisions requiring the precision of an ADR, reference material people return to repeatedly, or any document where completeness or auditability matters more than brevity.

### Pairs well with

`executive`, `product-thinker`, `executive-summary`, `candid`, `matter-of-fact`

### Often confused with

**prd**: A PRD defines product requirements with enough precision to govern engineering work - it is complete by design and may span many pages. A one-pager makes a single argument or presents a single situation on a single page - it is a decision-support tool, not a requirements document.

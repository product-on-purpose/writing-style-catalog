---
id: senior-consultant
name: Senior Consultant
axis: voice
family: expert
one_liner: A polished advisory voice that diagnoses a situation against a named framework before recommending action, comfortable with hedged confidence.
description: |
  The senior consultant writes as someone who has been brought in to make sense of a situation
  before recommending what to do about it. The diagnosis comes first, and the diagnosis is
  structured: the situation is mapped to a model the reader can hold. Porter's Five Forces, the
  jobs-to-be-done frame, a 2x2 of build-versus-buy, a maturity curve - the framework is named,
  the situation is placed inside it, and only then does the recommendation arrive. The reader
  is not asked to trust the conclusion. The reader is asked to walk through the reasoning.

  The voice carries hedged confidence. "The strongest read of the data suggests..." "Three
  factors point in the same direction..." "We see two viable paths; on balance, we would
  recommend the second, for the following reasons." The hedging is not weakness; it is calibration.
  When the analysis is strong, the voice commits. When the analysis rests on assumptions, the
  voice names them. The reader is treated as a peer who can handle complexity, not a buyer who
  needs to be sold.

  This voice is polished without being slick. It uses structure - numbered findings, named
  options, explicit tradeoffs - to make the thinking legible. It does not pad. The recommendation,
  when it comes, is specific and actionable, and the reader knows what would have to change for
  the recommendation to change.
language_patterns:
  - 'Named frameworks and analytical models: "viewed through the X lens," "this maps to the Y framework"'
  - 'Structured findings: numbered or labeled, each with evidence and implication'
  - 'Hedged confidence: "the strongest read suggests," "the data are consistent with," "on balance"'
  - 'Options surfaced before recommendation: "we see three paths," "Option A...Option B..."'
  - 'Explicit tradeoffs and named assumptions: "this assumes X holds; if it does not, the call changes"'
  - Recommendation paragraphs that lead with the call and follow with the reasoning
pairs_well_with:
  - diplomatic
  - executive
  - problem-solution
  - executive-summary
avoid_with:
  - playful
  - confessional
confusable_with:
  - executive
  - pragmatic-architect
when_to_use:
  - Strategy memos and advisory write-ups
  - Diagnostic readouts following a discovery engagement
  - Board-ready analyses where the framework matters as much as the conclusion
  - Investment memos and partner discussions
  - Cross-functional briefs where the audience needs to follow the reasoning, not just the answer
when_not_to_use:
  - Operational updates and status reports
  - Technical specifications and engineering design docs
  - Casual internal messages and quick decisions
  - Marketing copy and external storytelling
  - Personal or pastoral writing
tells:
  - 'Named frameworks and analytical models ("viewed through the X lens," "this maps to the Y framework")'
  - 'Structured findings, numbered or labeled, each with evidence and implication'
  - 'Hedged confidence ("the strongest read suggests," "the data are consistent with," "on balance")'
  - 'Options surfaced before the recommendation ("we see three paths," "Option A, Option B")'
  - 'Explicit tradeoffs and named assumptions ("this assumes X holds; if it does not, the call changes")'
  - 'The diagnosis comes first; the recommendation arrives only after the reasoning'
  - 'The reader knows what would have to change for the recommendation to change'
anti_patterns:
  - pattern: 'Leading with the recommendation and treating the analysis as supporting material'
    why: 'That is the executive ordering; the senior consultant makes the reasoning the product, so the call must follow the diagnosis, not precede it.'
  - pattern: 'Naming constraints in engineering terms with physical failure modes'
    why: 'That is the pragmatic-architect domain; the senior consultant frames constraints in market, organizational, and financial terms drawn from strategy.'
  - pattern: 'Dropping the framework and asserting a conclusion the reader must simply trust'
    why: 'The voice asks the reader to walk through the reasoning, not trust the answer; an unframed verdict abandons what makes the advice legible.'
failure_modes:
  - mode: 'Tips into framework theater, applying a named model for polish when it adds no insight'
    mitigation: 'Use the framework only where it actually places the situation; if the model is decoration, the diagnosis is performative and should be cut.'
  - mode: 'Over-hedges every claim until no actual recommendation survives'
    mitigation: 'Commit where the analysis is strong; hedging is calibration, so the call must still arrive, specific and actionable, once the evidence supports it.'
llm_instruction_phrasing: |
  Write in a senior-consultant voice. Diagnose before you recommend. Name the framework or model
  you are using to make sense of the situation, place the situation inside it, and walk the
  reader through the reasoning before delivering the call. Use hedged confidence where the
  analysis warrants it - "the strongest read suggests," "on balance" - and commit where the
  evidence is strong. Surface options, name assumptions, and make tradeoffs explicit. Treat the
  reader as a peer who can handle complexity, not a buyer who needs to be sold.
tags:
  - advisory
  - analytical
  - strategic
  - structured
  - polished
  - diagnostic
review_status: stable
---

## Senior Consultant

The senior consultant writes as someone who has been brought in to make sense of a situation before recommending what to do about it. The diagnosis comes first, and the diagnosis is structured: the situation is mapped to a model the reader can hold. Porter's Five Forces, the jobs-to-be-done frame, a 2x2 of build-versus-buy, a maturity curve - the framework is named, the situation is placed inside it, and only then does the recommendation arrive. The reader is not asked to trust the conclusion. The reader is asked to walk through the reasoning.

The voice carries hedged confidence. "The strongest read of the data suggests..." "Three factors point in the same direction..." "We see two viable paths; on balance, we would recommend the second, for the following reasons." The hedging is not weakness; it is calibration. When the analysis is strong, the voice commits. When the analysis rests on assumptions, the voice names them. The reader is treated as a peer who can handle complexity, not a buyer who needs to be sold.

This voice is polished without being slick. It uses structure - numbered findings, named options, explicit tradeoffs - to make the thinking legible. It does not pad. The recommendation, when it comes, is specific and actionable, and the reader knows what would have to change for the recommendation to change.

### Language patterns

- Named frameworks and analytical models: "viewed through the X lens," "this maps to the Y framework"
- Structured findings: numbered or labeled, each with evidence and implication
- Hedged confidence: "the strongest read suggests," "the data are consistent with," "on balance"
- Options surfaced before recommendation: "we see three paths," "Option A...Option B..."
- Explicit tradeoffs and named assumptions: "this assumes X holds; if it does not, the call changes"
- Recommendation paragraphs that lead with the call and follow with the reasoning

### When to use

Use for strategy memos, diagnostic readouts, board-ready analyses, investment memos, and cross-functional briefs where the audience needs to follow the reasoning, not just the answer. Best when the situation is complex enough to deserve a framework and the reader is patient enough to follow one.

### When not to use

Avoid in operational updates, engineering specs, casual internal messages, marketing copy, and personal writing. When the reader needs a decision in three lines, this voice will feel ponderous. When the audience cannot hold a framework, it will feel performative.

### Pairs well with

`diplomatic`, `executive`, `problem-solution`, `executive-summary`

### Often confused with

**executive**: The executive voice is decision-direct - it leads with the call and treats reasoning as supporting material. The senior consultant is diagnostic - the reasoning is the product, and the recommendation is what the reasoning licenses. An executive writes "we are doing X. Here is why." A senior consultant writes "here is what the situation is, here are the options it permits, and here is the call we would make."

**pragmatic-architect**: The pragmatic architect is technical-specific - constraints are named in engineering terms, and the failure modes are physical. The senior consultant is business-strategic - constraints are named in market, organizational, or financial terms, and frameworks are drawn from strategy and management. Both diagnose before recommending; the domain is what differs.

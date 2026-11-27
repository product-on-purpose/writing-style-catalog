---
id: first-principles-derivation
name: First-Principles Derivation
axis: style
one_liner: Opens on premises the reader already grants and derives the conclusion from them step by step, refusing to borrow any step from authority or precedent.
description: |
  First-principles derivation builds its conclusion rather than defending it. The piece opens by
  putting its premises on the page, separately and plainly, each one stated so the reader can
  grant it or refuse it before anything is built on top. Every step that follows rests on a
  premise or on an earlier step, and the piece says which. The conclusion arrives at the end, as
  a consequence, and is not announced at the start.

  The discipline of the style is the refusal to borrow. No step may be supported by a standard,
  a framework, a precedent, an industry convention, or a named authority, because a borrowed step
  is a step the reader cannot audit from the premises. This is a real cost. The style is slower
  than citing a known result, and it will sometimes derive, at length, something a practitioner
  already knows. The payoff is that a reader who disagrees can point at the exact premise they
  reject, and a reader who grants every premise has nowhere left to stand.

  That gives the style an unusual property: it is falsifiable at a named joint. A good piece in
  this style tells the reader which premise is the load-bearing one and what would follow if it
  were false. That is a stronger invitation than asking a reader to weigh evidence, because it
  tells them precisely where to push.

  A note on what counts as a premise. An observation, a measurement, or a number the writer took
  from somewhere is a legitimate premise, stated as one and open to challenge. What the style
  forbids is importing a *conclusion* and treating it as settled. The difference is whether the
  reader is being handed something to grant or something to accept.
structural_conventions:
  - The premises appear first, stated separately, each one grantable or refusable on its own before anything rests on it
  - No step is supported by a standard, a precedent, an industry convention, or a named authority
  - Each step names which premise or earlier step it follows from, so the chain can be walked backwards
  - The conclusion appears last, framed as a consequence of the chain rather than as a thesis
  - The piece names the load-bearing premise and says what would follow if it were false
  - Any number, measurement, or observation is introduced as a premise and labelled as one
frame: argumentative
evidence_types:
  - stated premises the reader is asked to grant
  - logical entailment from an earlier step
  - arithmetic or unit reasoning performed on the page
  - the named consequence of rejecting a premise
reader_contract: By the end, you will be able to name the single premise you would have to reject in order to reject the conclusion.
classical_mode: argumentation
pairs_well_with:
  - technical-writer
  - matter-of-fact
  - skeptical
confusable_with:
  - classical-argument
  - definitional
avoid_with:
  - marketer
  - ad-copy
when_to_use:
  - Questioning a practice everyone has inherited, where citing the practice would beg the question
  - Decisions where the disagreement is really about an unstated assumption rather than about evidence
  - 'Sizing something from scratch: a capacity estimate, a cost, a timeline, built from stated inputs'
  - Writing for a reader who will not accept an argument from authority, including one who should not
  - Any case where the writer wants the reader to be able to reject the conclusion precisely
when_not_to_use:
  - Writing for a reader who needs to act now, because the derivation costs them the time it takes
  - Settled questions where the known result is not in dispute and rederiving it wastes the reader
  - Subjects whose premises are genuinely contested with no common ground to start from
  - Task documentation, where the reader wants the steps rather than the reasoning behind them
  - Anything where the conclusion is already fixed and the derivation would be reverse-engineered to reach it
tells:
  - The opening is a list of premises rather than a claim
  - Each step says what it follows from ("from premise two and the step above")
  - No step cites a standard, a framework, or a named authority as its support
  - The conclusion is late, and is phrased as a consequence rather than as a thesis
  - One premise is identified as load-bearing, with the consequence of its failure stated
  - Numbers appear as premises, labelled as inputs rather than asserted as facts
  - The chain can be walked backwards from the conclusion to the premises without a gap
anti_patterns:
  - pattern: 'Stating the claim in the first or second paragraph and then presenting the premises as its support, answering the strongest objection along the way'
    why: 'That is classical argument, which earns a claim it has already made by supplying grounds, an explicit warrant, and a rebuttal. This style withholds the conclusion so the reader reaches it, and its rebuttal equivalent is naming the premise whose failure would break the chain.'
  - pattern: 'Opening on a precise definition and then testing it against cases that do and do not qualify'
    why: 'That is definitional writing, where the definition is the load-bearing first move and the piece ends on a stress-tested version of it. Here a definition can only be a premise, and the piece ends on a derived conclusion rather than on a sharper definition.'
  - pattern: 'Citing a standard, a benchmark, or a well-known result as a step in the chain'
    why: 'A borrowed step cannot be audited from the premises, which destroys the one property the style exists to deliver. If the result is needed, it is admitted as a premise the reader may refuse, not slipped in as a warrant.'
  - pattern: 'Fixing the conclusion first and selecting premises that reach it'
    why: 'A derivation assembled backwards has the form of the style and none of its value, and it is detectable: the premises will be oddly specific and no alternative consequence will be named anywhere.'
failure_modes:
  - mode: 'The derivation starts so far back that most of the piece establishes things nobody contested, and the one genuinely contested inference gets a single sentence'
    mitigation: 'Start at the last premise the reader already grants, not at the beginning of the subject. The length should sit where the disagreement sits, which is usually one or two steps deep.'
  - mode: 'The refusal to borrow hardens into a refusal to admit any outside input, so the chain is internally valid and factually untethered'
    mitigation: 'A measurement or observation is a legitimate premise; what is forbidden is importing a conclusion as settled. State the number, name where it came from, and let the reader challenge it as a premise.'
  - mode: 'The chain grows so long that every step is individually sound and no reader can hold the whole, so the auditability the style promised is gone in practice'
    mitigation: 'Keep the chain short enough to restate in a paragraph. If it cannot be, split it: derive an intermediate result, name it, and start the next stretch from there.'
llm_instruction_phrasing: |
  Write as a first-principles derivation. Open by stating your premises separately and plainly,
  each one phrased so the reader can grant or refuse it before anything is built on it. Then
  derive the conclusion step by step, and for each step say which premise or earlier step it
  follows from. Do not support any step with a standard, a framework, a precedent, an industry
  convention, or a named authority: if you need an outside result, introduce it as a premise
  the reader may refuse. Numbers and measurements are premises, so label them as inputs rather
  than asserting them. Put the conclusion last, phrased as a consequence rather than as a
  thesis. Before you finish, name the single load-bearing premise and say what would follow if
  it were false. Start from the last premise the reader already grants, not from the beginning
  of the subject.
tags:
  - reasoning
  - derivation
  - assumptions
  - analysis
  - auditable
review_status: draft
---

## First-Principles Derivation

First-principles derivation builds its conclusion rather than defending it. The piece opens by putting its premises on the page, separately and plainly, each one stated so the reader can grant it or refuse it before anything is built on top. Every step that follows rests on a premise or on an earlier step, and the piece says which. The conclusion arrives at the end, as a consequence, and is not announced at the start.

The discipline of the style is the refusal to borrow. No step may be supported by a standard, a framework, a precedent, an industry convention, or a named authority, because a borrowed step is a step the reader cannot audit from the premises. This is a real cost. The style is slower than citing a known result, and it will sometimes derive, at length, something a practitioner already knows. The payoff is that a reader who disagrees can point at the exact premise they reject, and a reader who grants every premise has nowhere left to stand.

That gives the style an unusual property: it is falsifiable at a named joint. A good piece in this style tells the reader which premise is the load-bearing one and what would follow if it were false. That is a stronger invitation than asking a reader to weigh evidence, because it tells them precisely where to push.

A note on what counts as a premise. An observation, a measurement, or a number the writer took from somewhere is a legitimate premise, stated as one and open to challenge. What the style forbids is importing a conclusion and treating it as settled. The difference is whether the reader is being handed something to grant or something to accept.

### Structural conventions

- The premises appear first, stated separately, each one grantable or refusable on its own before anything rests on it
- No step is supported by a standard, a precedent, an industry convention, or a named authority
- Each step names which premise or earlier step it follows from, so the chain can be walked backwards
- The conclusion appears last, framed as a consequence of the chain rather than as a thesis
- The piece names the load-bearing premise and says what would follow if it were false
- Any number, measurement, or observation is introduced as a premise and labelled as one

### When to use

Use it to question a practice everyone has inherited, where citing the practice would beg the question. It suits decisions where the real disagreement is about an unstated assumption rather than about evidence, and it suits sizing something from scratch: a capacity estimate, a cost, a timeline, built from stated inputs. Reach for it when the reader will not accept an argument from authority, including a reader who should not, and whenever the writer wants disagreement to land on a specific premise rather than on the whole piece.

### When not to use

Avoid it for a reader who needs to act now, because the derivation costs them exactly the time it takes. Avoid it on settled questions, where rederiving a known result spends the reader's attention for nothing. Avoid it where the premises themselves are genuinely contested and there is no common ground to start from, because the chain will never get off the ground. Avoid it in task documentation, where the reader wants the steps rather than the reasoning. Avoid it most of all where the conclusion is already fixed, because the derivation will be reverse-engineered to reach it.

### Pairs well with

`technical-writer`, `matter-of-fact`, `skeptical`

### Often confused with

**classical-argument**: Both are argumentative, both make their reasoning explicit rather than asserting, and both leave a reader able to say where they disagree, which is why the two are easy to mistake. The difference is order and provenance. Classical argument states its claim early, supplies grounds, makes the warrant that connects evidence to claim explicit, and then names the strongest objection and answers it; among its legitimate forms of support is cited authority. A first-principles derivation withholds the claim until the end, so the reader arrives at it, and it refuses cited authority at every step, because a borrowed step cannot be audited from the premises. Classical argument defends a position against an objection. This style offers the reader a chain and tells them which link to pull.

**definitional**: Both put something precise at the front of the piece and build everything afterwards on it, so they can look alike from a distance. Definitional writing leads with a definition that is exact enough to discriminate cases, then elaborates it through facets and edge cases and a section on what the term is not, and ends on a stress-tested version of that opening definition. A first-principles derivation leads with premises, not with a definition; where a definition appears, it is one premise among several and is there to be granted rather than tested. The two also end in different places. A definitional piece ends where it started, sharper. This one ends somewhere the opening did not state.

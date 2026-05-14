---
adr_id: "0001"
title: Adopt a Three-Axis Taxonomy (Voice & Tone, Style, Format)
date: 2026-05-10
status: Accepted
---

# 0001 - Adopt a Three-Axis Taxonomy (Voice & Tone, Style, Format)

## Status

Accepted

## Context

Writing instruction systems typically use monolithic style guides that fuse voice, tone, structure, and format into a single document. These work for human writers following a brand guide but are weak as composable LLM controls because they cannot be mixed and matched. A style guide is a read-once artifact for a human; an LLM instruction set is a runtime parameter that must compose cleanly with other runtime parameters.

Multiple LLM research sessions (Claude Opus 4.7, GPT-5.5 Thinking, Gemini Pro) independently converged on a decomposed model when asked to reason about the minimum orthogonal dimensions of written communication. The convergence was not prompted; it emerged from asking "what can you vary independently in a piece of writing without the other dimensions being forced to change?"

The core insight is that Voice (who is speaking), Tone (how they feel right now), Style (what kind of writing), and Format (the structural container) are orthogonal. You can hold any three constant and vary the fourth to produce meaningfully different results. A pragmatic-architect voice writing with urgency can produce either a crisp listicle or a formal RFC - the voice and tone stay constant while the format changes. The same voice and format can shift from urgency to measured-calm without changing the structural container.

This orthogonality is the property that makes the catalog useful as a composable instruction set rather than a collection of named styles.

## Decision

Adopt three conceptual axes:

- Axis 1 - Voice & Tone: the two dimensions that together answer "how does this piece of writing behave?" Voice is persistent identity (who is always speaking). Tone is situational register (how they are speaking right now).
- Axis 2 - Style / Mode / Genre: the kind of writing being produced (analytical, narrative, instructional, persuasive, and so on).
- Axis 3 - Format / Output Structure: the structural container (listicle, memo, ADR, RFC, sermon, letter, and so on).

Voice and Tone are separated into distinct catalog directories (`taxonomy/voices/` and `taxonomy/tones/`) because they need different frontmatter fields and have different composition rules. Voice entries document persistent identity traits; tone entries document situational registers. However, they remain one conceptual axis because together they answer the behavioral question rather than the content question.

The product is described and explained as a "three-axis" taxonomy throughout documentation and the SDK, with a clarifying note that Voice and Tone are paired dimensions within Axis 1 rather than a collapsed single concept.

## Consequences

### Positive
- Composability: any valid combination of one voice, one tone, one style, and one format works as an instruction set.
- Teachability: each axis can be explained independently, and contributors can reason about one axis without understanding the others.
- Extensibility: new entries add to one axis without requiring changes to other axes or to the composition engine.
- LLM-optimized: the decomposed structure maps cleanly to prompt parameter slots, making programmatic composition straightforward.

### Negative
- The "three-axis" label requires explanation because there are four catalog directories. First-time readers may count four and expect the model to be called four-axis.
- The Voice/Tone distinction requires careful documentation to avoid contributor confusion. Both axes influence "how writing sounds," and the persistent-vs-situational distinction is non-obvious until explained.

### Neutral
- Audience is not a fourth axis but a constraint dimension captured in entry metadata (`target_audience` and `use_for` fields). Treating it as metadata rather than an axis keeps the composition space three-dimensional while still allowing audience-based filtering.
- The choice of three axes is not a claim that writing has exactly three orthogonal dimensions; it is a claim that these three are sufficient for the catalog's intended use cases.

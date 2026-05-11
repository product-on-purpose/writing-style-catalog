---
adr_id: "0004"
title: Treat Voice and Tone as Paired Dimensions Within One Axis
date: 2026-05-10
status: Accepted
---

# 0004 - Treat Voice and Tone as Paired Dimensions Within One Axis

## Status

Accepted

## Context

During the research phase there was productive disagreement about whether Voice and Tone should collapse into one axis or remain as two fully separate axes, making the model four-axis rather than three.

The case for collapsing Voice and Tone into a single axis: "voice" is commonly used in style guides to mean everything about how writing sounds, including warmth, urgency, and register. The AP Stylebook, the Mailchimp content guide, and most brand style guides use "voice and tone" as a single compound noun without drawing a distinction. If the catalog uses the conventional terminology in an unconventional way, it will confuse contributors who come from a brand-writing background.

The case for keeping Voice and Tone as two fully separate axes: Voice is persistent (a pragmatic-architect always sounds like a pragmatic-architect across every piece they write) while Tone is situational (a pragmatic-architect can write with urgency in a post-mortem and with measured calm in a retrospective). The persistent vs. situational distinction is functionally meaningful at runtime. It determines whether the choice is made once for a persona (voice) or adjusted per-piece based on context (tone). This is the distinction that makes the catalog useful for programmatic composition, not just human reading.

The case for a paired-dimension solution: Voice and Tone are implemented as separate catalog directories with different schemas, giving them the functional separation of two axes, while the product description maintains the conventional three-axis framing by treating them as paired dimensions within one axis.

## Decision

Voice and Tone are two catalog dimensions within Axis 1 (Voice & Tone). They have:

- Separate entry directories: `taxonomy/voices/` and `taxonomy/tones/`
- Separate JSON Schemas with different required fields (voice entries require `identity_traits`, `persistent_patterns`, and `avoids`; tone entries require `register`, `markers`, and `situational_triggers`)
- Separate parameters in the `compose-instruction` SDK function: `voice` and `tone` are distinct keyword arguments

The product is called and explained as "three-axis" because Voice & Tone together constitute one conceptual axis. The distinction internal to Axis 1 is:

- Voice entries document persistent identity: the traits and patterns that remain constant regardless of situation.
- Tone entries document situational register: the emotional quality and urgency level that varies based on context.

Any writing instruction can specify both independently. Specifying neither defaults to the catalog baseline for each.

## Consequences

### Positive
- Compositional precision: a composer can hold voice constant while varying tone across multiple pieces, or hold tone constant while applying it to multiple voices. This cross-product flexibility is not possible if the two dimensions are collapsed.
- Teachable distinction: "persistent vs. situational" is a clear, memorable rule for deciding which catalog to contribute to.
- Matches classical rhetoric's distinction between ethos (who the speaker is, stable) and pathos (the emotional appeal, situational). Contributors with a rhetoric background will recognize the structure.

### Negative
- The "three-axis" name requires explanation since there are four catalog directories and four frontmatter parameters (`voice`, `tone`, `style`, `format`). Every piece of documentation that mentions "three-axis" needs a parenthetical explaining the Voice/Tone pairing.
- First-time contributors may try to create "voice" entries that are actually tones, or vice versa. The contribution guide must provide examples of entries that are commonly confused (e.g., "urgency" is a tone, not a voice; "pragmatic-architect" is a voice, not a style).

### Neutral
- The `confusable_with` field on voice and tone entries is the disambiguation hook for similar-sounding entries across axes. An entry for "urgent" in tones would list `confusable_with: [styles/analytical, voices/operations-engineer]` to steer contributors who are looking for those entries instead.
- The Voice/Tone pairing decision does not affect how composed instructions are rendered. The composition engine concatenates axis blocks in a fixed order regardless of whether Voice and Tone are considered one axis or two.

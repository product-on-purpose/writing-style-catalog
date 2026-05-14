---
adr_id: "0006"
title: Use "Should We Adopt Async-First Standups?" as the Phase 0 Anchor Topic
date: 2026-05-10
status: Accepted
---

# 0006 - Use "Should We Adopt Async-First Standups?" as the Phase 0 Anchor Topic

## Status

Accepted

## Context

The Phase 0 walking skeleton requires one anchor topic rendered as a vertical slice across all 20 initial entries (5 per axis). Every entry in the Phase 0 catalog needs at least one example file, and all Phase 0 examples are written about the same topic so that the formal differences between entries are maximally visible. A reader comparing two voice entries must be able to attribute any difference in the example texts to the voice, not to the topic shifting the content.

The anchor topic must satisfy several constraints simultaneously:

- It must be plausibly written about by five different personas (PM, pastor, journalist, friend, operations engineer) without forcing artificial stretching.
- It must produce examples short enough to render in 200-800 words each, so examples can be included inline in the catalog.
- It must be non-controversial enough that readers focus on formal differences rather than on the substantive argument being made.
- It must cover enough format diversity to test ADR, RFC, PRD, essay, memo, letter, listicle, sermon, and conversational formats without forcing unnatural fits.
- The maintainer should have tacit knowledge about it so review of example quality is fast.

Four candidates were evaluated:

1. "Should we adopt async-first standups?" - a professional workplace topic with cross-role relevance, moderate format diversity, and the maintainer's direct experience.
2. "How to start a morning routine" - a personal development topic with high voice diversity but limited professional format coverage.
3. "The discipline of rest" - a spiritual/philosophical topic with strong pastoral and essayist coverage but weak engineering-format coverage.
4. "Choosing between Postgres and DynamoDB" - a technical topic with strong RFC and ADR coverage but narrow voice diversity (pastoral and friendly-mentor voices strain against it).

## Decision

The Phase 0 anchor topic is "Should we adopt async-first standups?" with the slug `async-standups`.

This topic is the most balanced first topic across the constraint dimensions:

- Professional enough to exercise ADR, RFC, memo, and PRD formats credibly.
- Personable enough that pastoral, columnist, and friendly-mentor voices engage with it naturally. The topic touches presence, attention, the ethics of always-on culture, and what we lose when we remove synchronous ritual - all of which are productive territory for non-technical voices.
- Format-diverse enough to test the full Axis 3 spread without forcing.
- The maintainer has run and participated in async-standup experiments, enabling fast and accurate example review.

Phase 1 will add "How to start a morning routine" (slug: `morning-routine`) as the second anchor topic, broadening coverage toward personal development formats without replacing the professional baseline.

## Consequences

### Positive
- Tests the full axis spread in Phase 0. Every voice, tone, style, and format entry has a plausible instantiation for this topic.
- Produces demos that make the formal differences between voices and formats immediately visible to first-time catalog users.
- The maintainer's domain knowledge enables fast, accurate quality review of all Phase 0 examples.
- The professional-workplace framing makes the demos usable in product presentations and conference talks.

### Negative
- The topic leans professional, which means the spiritual and conversational voices require more creative stretching than they would on a topic like "morning routine." A pastoral voice writing about async standups must work harder to find its authentic register than a pastoral voice writing about rest.
- The topic will feel dated if async-standup practices become so normalized that the question is no longer interesting. The examples are illustrative, not evergreen advice.

### Neutral
- The anchor topic choice does not constrain the catalog content. Any topic works with any entry; the anchor topic is a scaffolding decision for the Phase 0 example set, not a constraint on the taxonomy.
- The slug `async-standups` is used in example file naming conventions across the Phase 0 entry directories. Phase 1 examples use `morning-routine` as the second slug prefix.

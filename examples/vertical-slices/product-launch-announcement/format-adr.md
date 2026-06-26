---
entry_id: adr
axis: format
topic_slug: product-launch-announcement
topic_label: Announcing a new product to an outside audience
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# ADR-0042: Lead the Tidemark Launch Announcement with the Problem, Not the Feature Set

## Status

Accepted

## Context

Tidemark ships next week. It ingests customer feedback from wherever a team has been accumulating it - a spreadsheet, a chat thread, a ticket tracker - and produces a single ranked, shareable roadmap view.

At launch, one announcement will reach three distinct audiences: prospective users who have never heard of Tidemark, press contacts who will determine how the product is categorized, and a small group of existing beta customers who already have opinions. Their needs diverge, but they will read the same text.

The central tension is that Tidemark does several things. It collects, synthesizes, ranks, and surfaces feedback as a roadmap. We could announce it as any one of those functions. Roadmap software is an established category. Feedback management is an established category. Neither fully describes the workflow Tidemark handles, and defaulting to either invites reviewers to slot Tidemark into a bucket it does not quite fit.

Three approaches were weighed:

1. Lead with the product category: "Tidemark is a roadmap tool." Familiar framing, easy to scan, but undersells the synthesis step and invites direct comparison to tools that do only the roadmap side.
2. Lead with the team outcome: "Tidemark helps teams ship the right things faster." Aspirational, but too vague to tell a prospective user what the product actually does. Press cannot categorize it from that sentence alone.
3. Lead with the problem: "Customer feedback piles up in spreadsheets, chat threads, and ticket trackers with no shared view of what matters most. Tidemark turns it into a ranked, shareable roadmap." Concrete, honest, and names the gap rather than a category.

A fourth option - describing only the input side and treating the ranked roadmap as a secondary detail - was rejected because it positions Tidemark as a research aggregator rather than a decision-support tool.

## Decision

The launch announcement leads with the problem (scattered feedback, no shared ranked view) and resolves it with one specific description of what Tidemark produces: a ranked, shareable roadmap. We do not position Tidemark inside any named tool category. We do not enumerate capabilities beyond the core workflow. The call to action is a free trial signup with no sales-call gate.

Existing beta customers receive a separate, direct note that acknowledges their early involvement. The launch announcement is not written for them.

## Consequences

### Positive

- Problem-led framing reaches the prospective users most likely to convert: small teams already frustrated with how they handle customer feedback today.
- Naming one workflow (feedback in, ranked roadmap out) keeps the announcement scannable and prevents it from reading as a feature inventory, which loses both press and casual readers.
- A free-trial CTA reduces the commitment threshold for the largest segment and avoids making first contact a sales interaction.
- The positioning holds consistently across the press release, the product site, and any partner channels without internal contradiction.

### Negative

- Teams with adjacent pain (general prioritization work that is not specifically feedback-driven) may not recognize themselves in the announcement and may never try Tidemark.
- Press will categorize the product regardless of our framing. We can slow the "just another roadmap tool" read; we cannot prevent it.
- Beta customers who think of Tidemark differently from the launch framing need explicit outreach. If we omit that step, the announcement can feel like a redefinition of something they helped build.

### Neutral

- This decision fixes the anchor language before any press coverage runs. Shifting the positioning after that point requires active re-framing effort; it does not happen by updating one page.
- The free-trial CTA commits the product team to a working self-serve onboarding flow on launch day. That dependency is not visible in the announcement copy, but it is real.

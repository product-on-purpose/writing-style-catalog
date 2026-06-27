---
entry_id: rfc
axis: format
topic_slug: product-launch-announcement
topic_label: Announcing a new product to an outside audience
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# RFC-0001: Tidemark Launch Announcement - Framing and Channel Strategy

## Status

Under Review

## Author(s)

Marisol Veen, Head of Product, Tidemark - June 20, 2026

## Problem

Tidemark ships publicly on June 30. We need to agree on how to frame the product for people who have never heard of it, and decide which channels get what version of the message.

The product does several things: it collects feedback from scattered sources, identifies recurring themes, scores them by frequency and recency, and surfaces a ranked roadmap view that teams can share. Any one of those steps could anchor the announcement, and the anchor we choose will shape how press categorizes the product and how prospective users decide whether it is for them.

This matters now because the announcement will run before we have any signal on what language actually converts. Once press coverage runs, we are working against an established framing, not building one.

The audiences who will read the same launch text have genuinely different needs:

- Prospective users need to recognize their own problem quickly enough to click through.
- Press contacts need enough specificity to file the product somewhere in how they think about software categories.
- Beta testers have opinions about what the product is for that the launch copy may or may not match.

We have not agreed on how to handle these three audiences with one announcement. We also have not resolved what to do about the beta cohort. They built expectations during the early-access period and the launch copy will not be written for them. If they read the public announcement before we say anything directly to them, that is a relationship problem.

## Proposed Approach

Lead the announcement with the problem, not the product category or a capability list.

Specifically: open with the scatter problem (customer feedback piling up in spreadsheets, chat threads, and ticket trackers with no shared view of what matters most), then resolve it with one specific description of what Tidemark produces - a ranked, shareable roadmap. Name the workflow, not the category. Do not enumerate capabilities beyond the core loop.

For the beta cohort: a separate direct note goes out before the launch announcement, acknowledging their early involvement and explaining that the public framing is written for a different reader. They should hear that from us, not infer it.

For call to action: free trial signup, no sales-call gate.

This approach is grounded in what the early-access cohort named consistently at intake - teams maintaining a separate spreadsheet to consolidate what users had asked for. That is the problem we know how to reach.

## Alternatives Considered

**Lead with the product category ("Tidemark is a roadmap tool.").**
Familiar framing, easy to scan, and gives press a clean box to put us in. I am not proposing this because "roadmap tool" undersells the synthesis step and invites direct comparison against tools that do only the roadmap side. Tidemark would lose that comparison on features unless reviewers understand that the workflow difference is the point.

**Lead with the team outcome ("Tidemark helps teams ship the right things faster.").**
Aspirational and true, but too vague for a prospective user to act on. A press contact cannot categorize a product from a benefit statement. This framing may be right for a brand campaign with room to develop the claim; it is not right for an announcement where the reader has ten seconds.

**Describe only the input side and treat the ranked roadmap as a secondary detail.**
This positions Tidemark as a research aggregator, which is not what it does in practice. Teams that need an aggregator are a different segment from teams that need a decision surface they can share with stakeholders. Positioning as an aggregator narrows the product to a step we do not control and misrepresents the output.

**Run separate announcements by audience - different messages for press, prospective users, and beta testers.**
Logistically cleaner, but I am skeptical we have the bandwidth to maintain three live versions without introducing inconsistency. If the core framing is right, one message should work across channels with minor adjustments. I am not certain this is true - see Open Questions.

## Open Questions

1. **Should the beta cohort note go out before or simultaneously with the launch announcement?** My instinct is before - a courtesy that lands after the fact is not a courtesy. But I do not know how much lead time is right. Input welcome from anyone who has managed a beta-to-launch transition.

2. **How much channel-specific variation does the core message need?** I am proposing one anchor with minor adjustments per channel. If someone has strong evidence that press requires materially different framing from what prospective users need, I want to hear it before we commit the language.

3. **Is the free-trial CTA the right first ask?** It works for solo users and small teams, but I am not confident whether the $29 team plan converts better from a self-serve trial or from a short walkthrough. We do not have data here. Proposing trial-first as a default; open to argument for demo-first if anyone has relevant experience.

4. **What do we do if press categorizes Tidemark in a way we cannot recover from?** Problem-led framing slows the "just another roadmap tool" read but does not prevent it. I want to understand whether we have a response plan if early coverage defines us in a bucket we do not fit, or whether we are treating that as an acceptable risk.

## Consequences

If this approach is accepted:

- The announcement and all supporting copy (product site, partner channels, press materials) need to use consistent language from day one. Inconsistency between the press release and the product landing page gives reviewers a reason to call out confused positioning.
- The free-trial CTA commits the product team to a working self-serve onboarding flow on June 30. That is not a copy decision - it is an engineering dependency this RFC is surfacing explicitly.
- Problem-led framing reaches the segment most likely to convert - small teams already frustrated with how they handle feedback - but it may not reach adjacent users with a general prioritization problem rather than a feedback-scatter problem. We accept some narrowing as the cost of being specific.
- Once press coverage runs, shifting the positioning is work, not a page update. This is the last point at which changing the anchor costs us only time.

**Review deadline: June 23, 2026.** I will synthesize comments and update the status to Accepted, Rejected, or Withdrawn after that date.

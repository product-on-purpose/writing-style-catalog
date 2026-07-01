---
id: review-response
name: Review Response
axis: format
domain: professional
family: response
one_liner: A public reply from a business to a customer's posted review, written for the reviewer but read by every future prospect.
description: |
  A review response is a public reply from a business to a customer's posted review - positive
  or negative - written for the reviewer but read by every future prospect who encounters it.
  Unlike a private support exchange, the review response has a dual audience: the person who left
  the review, and every onlooker who reads the thread before making a purchase or booking. This
  dual-audience character shapes every sentence. The response must genuinely address the reviewer
  while simultaneously signaling to strangers how the business handles praise, complaint, and
  criticism.

  The anatomy of an effective review response is compact: open by acknowledging the reviewer by
  name (if visible) and naming the specific feedback they left - not a generic "thank you for
  your review." For negative reviews, acknowledge the concern once and briefly, then redirect to
  a private channel (email or phone) where the resolution can happen. For positive reviews, thank
  the reviewer and reinforce a specific detail they praised, then close with the business name as
  a brand identifier. The resolution itself belongs in private; the public reply is the brand
  signal, not the case record.

  Unlike a support reply, which is a private one-to-one message resolving a specific customer's
  problem so they know exactly what to do next, a review response is public and the resolution
  path is an invitation, not the resolution itself. Brevity is load-bearing here: prospects skim
  reviews and their responses, and a long public reply usually signals that the writer forgot who
  the real audience is.

  Typical length: 50-150 words.
canonical_template: |
  [Greeting - use the reviewer's name if visible]
  Thank you for sharing your feedback, [Name].

  [For positive reviews: name what they praised and reinforce it]
  We're glad to hear [specific detail] made a difference - that's exactly what we aim for.

  [For negative reviews: acknowledge the concern once, briefly]
  We're sorry to hear about [specific issue]. That is not the experience we want for our guests.

  [Redirect to private channel for resolution]
  Please reach out to us at [email or phone] so we can make this right.

  [Close with the business name]
  [Business Name]
typical_voices:
  - caregiver
  - direct-communicator
typical_tones:
  - diplomatic
  - empathetic
digital_or_print: digital
pairs_well_with:
  - caregiver
  - direct-communicator
  - diplomatic
  - empathetic
  - problem-solution
avoid_with:
  - skeptical
  - confessional
  - urgent
confusable_with:
  - support-reply
when_to_use:
  - A customer has posted a review on a public platform (Google, Yelp, App Store, TripAdvisor) and the business wants to respond publicly
  - A negative review raises a specific concern that warrants public acknowledgment and a private resolution path
  - A positive review offers an opportunity to thank the reviewer and reinforce the brand for onlookers
  - Responding to a review where silence would signal indifference to future prospects
  - The situation calls for a short, public brand signal rather than a full private resolution
when_not_to_use:
  - The customer's issue requires a detailed, private resolution - send a support reply through a direct channel instead
  - The response would need to include confidential information (account details, order numbers, billing) that cannot be shared publicly
  - The review is from a bad-faith actor and any public response would amplify the complaint rather than de-escalate it
tells:
  - 'Opens by addressing the reviewer by name (if visible) and naming their specific feedback, not a generic "thank you for your review"'
  - 'Written in the first-person plural ("we") to represent the business, not a single agent'
  - 'Negative responses acknowledge the concern once and briefly, then redirect to a private channel for resolution'
  - 'Positive responses thank the reviewer and reinforce a specific detail they praised'
  - 'Closes with the business name as a brand identifier for onlookers'
  - 'Brief - typically 50-150 words - because the prospect audience skims rather than reads'
  - 'Never resolves account-level details, order specifics, or billing in the public text'
anti_patterns:
  - pattern: 'Responding defensively or contesting the reviewer''s account of events'
    why: 'Onlookers read a defensive reply as the business being difficult; even when the reviewer is factually wrong, a combative response signals poor judgment to prospects who have not yet formed an opinion of the business.'
  - pattern: 'Writing a generic response that does not name the reviewer''s specific feedback'
    why: 'A templated "Thank you for your review! We appreciate your business!" signals automation and indifference. Acknowledging specifics is what makes the dual-audience signal credible to both the reviewer and onlookers.'
  - pattern: 'Using the public reply to deliver a full resolution - account credits, order details, refund confirmation - as if the review response were a support reply'
    why: 'A support reply is a private one-to-one message whose job is to close the issue so the customer knows exactly what to do next. A review response is public; its resolution path is an invitation to a private channel, not the resolution itself. Account details in a public post harm the customer''s privacy and turn a brand signal into a case record.'
  - pattern: 'Using the reviewer''s praise as a launchpad for a promotional statement about the business'
    why: 'A response that tips into marketing copy reads as self-serving to onlookers and dismisses the reviewer''s specific experience in favor of a sales pitch.'
failure_modes:
  - mode: 'Over-apologizes - on negative reviews, the response tips into extended public apology that repeatedly validates the reviewer''s grievance, amplifying the complaint for every onlooker'
    mitigation: 'Acknowledge once, briefly and specifically, then move to the invitation for private resolution. Repeated apology in the public space makes the complaint more prominent, not less.'
  - mode: 'Over-markets - on positive reviews, the response tips into a promotional statement that uses the reviewer''s praise as a launchpad for brand messaging clearly aimed at prospects rather than as genuine thanks'
    mitigation: 'Positive responses should thank the reviewer and reinforce what they praised; any brand signal should emerge from genuine acknowledgment, not replace it. If the response reads like an ad, cut the last sentence.'
  - mode: 'Over-diplomatizes - the public caution gets so careful and noncommittal that the response sounds canned, evasive, and legally scrubbed instead of specific to the review'
    mitigation: 'Keep the reply brief but concrete: name the specific feedback, acknowledge it plainly, and use one human sentence before the private-channel invitation.'
llm_instruction_phrasing: |
  Write as a review response. This is a public reply from a business to a customer's posted
  review on a platform such as Google, Yelp, or the App Store. The reply is written for the
  reviewer but read by every future prospect who sees the thread. Open by addressing the reviewer
  by name if visible, and name their specific feedback - do not use a generic opening. For
  negative reviews: acknowledge the concern once, briefly and specifically, then invite the
  reviewer to a private channel (email or phone) for resolution. Do not include account-level
  details, order numbers, or refund specifics in the public text. For positive reviews: thank the
  reviewer and reinforce a specific detail they praised; do not let the response tip into a
  marketing statement. Close with the business name as a brand identifier for onlookers. Target
  50-150 words. Brevity matters because the prospect audience skims.
tags:
  - customer-reviews
  - reputation-management
  - public-response
  - customer-service
  - brand-signal
review_status: stable
---

## Review Response

A review response is a public reply from a business to a customer's posted review - positive or negative - written for the reviewer but read by every future prospect who encounters it. Unlike a private support exchange, the review response has a dual audience: the person who left the review, and every onlooker who reads the thread before making a purchase or booking. This dual-audience character shapes every sentence. The response must genuinely address the reviewer while simultaneously signaling to strangers how the business handles praise, complaint, and criticism.

The anatomy of an effective review response is compact: open by acknowledging the reviewer by name (if visible) and naming the specific feedback they left - not a generic "thank you for your review." For negative reviews, acknowledge the concern once and briefly, then redirect to a private channel (email or phone) where the resolution can happen. For positive reviews, thank the reviewer and reinforce a specific detail they praised, then close with the business name as a brand identifier. The resolution itself belongs in private; the public reply is the brand signal, not the case record.

Unlike a support reply, which is a private one-to-one message resolving a specific customer's problem so they know exactly what to do next, a review response is public and the resolution path is an invitation, not the resolution itself. Brevity is load-bearing here: prospects skim reviews and their responses, and a long public reply usually signals that the writer forgot who the real audience is.

### Canonical template

```
[Greeting - use the reviewer's name if visible]
Thank you for sharing your feedback, [Name].

[For positive reviews: name what they praised and reinforce it]
We're glad to hear [specific detail] made a difference - that's exactly what we aim for.

[For negative reviews: acknowledge the concern once, briefly]
We're sorry to hear about [specific issue]. That is not the experience we want for our guests.

[Redirect to private channel for resolution]
Please reach out to us at [email or phone] so we can make this right.

[Close with the business name]
[Business Name]
```

### When to use

- A customer has posted a review on a public platform (Google, Yelp, App Store, TripAdvisor) and the business wants to respond publicly
- A negative review raises a specific concern that warrants public acknowledgment and a private resolution path
- A positive review offers an opportunity to thank the reviewer and reinforce the brand for onlookers
- Responding to a review where silence would signal indifference to future prospects
- The situation calls for a short, public brand signal rather than a full private resolution

### When not to use

- The customer's issue requires a detailed, private resolution - send a support reply through a direct channel instead
- The response would need to include confidential information (account details, order numbers, billing) that cannot be shared publicly
- The review is from a bad-faith actor and any public response would amplify the complaint rather than de-escalate it

### Pairs well with

`caregiver`, `direct-communicator`, `diplomatic`, `empathetic`, `problem-solution`

### Often confused with

**support-reply**: A support reply is a written response to one customer's specific question or problem - private, one-to-one, with the goal of closing the issue so the customer knows exactly what to do next or knows the problem is already solved. A review response is public and dual-audience: it is written for the reviewer but read by every future prospect. Where a support reply resolves a case privately so the customer can act, a review response signals publicly how the business handles feedback - and then invites the reviewer to a private channel for the actual resolution.

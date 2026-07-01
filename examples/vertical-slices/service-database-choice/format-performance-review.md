---
entry_id: performance-review
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Performance Review: Marcus

## Period

2026-01-01 to 2026-06-30

## Reviewer

Ana Rivera, Tech Lead

## Summary

Marcus had a strong first half: sound technical judgment, real analysis behind his positions, and a professional response to being overruled on a call where he'd built the stronger technical case. The one gap is turning verbal agreement into written follow-through without a chase, which is what holds this at Meets Expectations instead of higher.

## Performance Against Goals

### Technical evaluation leadership on infrastructure decisions

Rating: Met

Marcus owned the technical case for DynamoDB in the notification-service datastore decision that became ADR-0023: he ran the spike in `experiments/notify-ddb/`, then presented the access-pattern analysis at Wednesday's architecture meeting. The team decided against his recommendation - the operational cost of a second datastore outweighed the access-pattern fit he had correctly identified - and he spent that evening working with me to turn two positions into one recommendation instead of leaving Priya to referee a split decision. He built the strongest case for the option we didn't choose, then helped land the one we did. That's worth naming on its own.

### Documentation and follow-through discipline

Rating: Partially Met

The 5M events/day revisit threshold written into ADR-0023 is Marcus's language, agreed to verbally the night of the architecture meeting. It was still pending written sign-off at end of day Thursday, a full day after the meeting, and I had to chase it down ahead of Friday's 11am lock. The effort gap between agreeing in the room and confirming in writing is small; it still cost a chase on a deadline he'd already agreed to.

## Strengths

- Does the analysis before forming the opinion. The DynamoDB spike was real work, not a slide deck, which is why the access-pattern tradeoff written into ADR-0023 is accurate instead of asserted.
- Absorbs a loss without turning it into friction. Marcus's case for DynamoDB was correct on its own terms; when the team weighted operational capacity higher, he didn't re-litigate it in the meeting or afterward, and he helped write the recommendation he hadn't originally held, the same day.

## Development Areas

- Close the loop in writing, not just in the room. Verbal agreement isn't the deliverable when a decision gates a scheduled lock; get confirmation into the document the same day you give it, so it isn't a follow-up item on someone else's status report.
- Widen the evaluation frame before the recommendation goes out, not after. The DynamoDB case was strong on access-pattern fit and light on what a second datastore costs the on-call rotation; the operational argument had to fill that gap afterward, in the room. A spike that weighs operational cost alongside technical fit from the first draft is the difference between a strong individual analysis and one that's ready to inform a team decision on its own.

## Goals for Next Period

- Own the technical spike if the notification service crosses the 5M events/day revisit threshold set in ADR-0023, scoped to weigh operational cost alongside access-pattern fit from the first draft - ongoing, revisit at Q4 2026 planning if the threshold hasn't been hit by then.
- Confirm gating decisions in writing the same day they're agreed verbally, starting with the next architecture decision - effective immediately.

## Overall Rating

Meets Expectations

## Additional Notes

This review leans on the notification-service datastore decision because it's the clearest, most citable example from the period: real analysis, a real disagreement, and a real recovery from being overruled, inside one week. It isn't the only work Marcus did in H1, but it's the example that shows both where he's strong and where the next increment of growth is.

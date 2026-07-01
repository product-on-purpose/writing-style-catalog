---
entry_id: recommendation-letter
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Ana Rivera
Tech Lead, Notification Service
Lattice Notify
July 8, 2026

Dear Engineering Leveling Committee,

I am Marcus's tech lead and have been for the past two years, most recently completing his H1 2026 performance review. I am writing to recommend him for promotion to Staff Engineer. The case rests heavily on one week this May, because it is the clearest example I have of both halves of what this level requires: technical judgment strong enough for the rest of us to build on, and the maturity to subordinate that judgment to the team's decision once it lost.

When the notification service needed a new persistent datastore this spring, Marcus owned the technical case for DynamoDB. He did not build that case from a slide deck. He ran an actual spike, documented in experiments/notify-ddb/, against the service's real access pattern - write-heavy, point-lookups by user - and tested it against our real growth numbers: 500K events/day at launch, with a 10x growth scenario in 12 months if the pending Slack-partnership deal closes. He presented the analysis at Wednesday's architecture meeting, and it held up under questions, because his own writeup was honest about DynamoDB's cost as well as its fit. He documented, in that same spike, that adopting it would double our operational surface for the 4-person on-call rotation that already runs our primary Postgres cluster. He built the strongest case for the option the team did not choose, and he built it well enough that the reason we did not choose it is written down in his own analysis, not mine.

The team decided against his recommendation. I made the operational-capacity argument in that same meeting, and the room weighted the cost of a second datastore over the access-pattern fit Marcus had correctly identified. What matters more to this recommendation is what he did next. Rather than leave Priya to referee a split decision the following morning, Marcus spent that evening working with me to turn two positions into one recommendation. The 5M events/day revisit threshold written into ADR-0023, the mechanism that keeps his original concern alive as a tracked trigger instead of a buried disagreement, is his language, not mine. If the committee pulls his H1 review, you will also see a Partially Met rating: written confirmation of that same threshold lagged the verbal agreement by a day, and I had to chase it down ahead of Friday's 11am lock. That is accurate, and it is the one place his execution has not yet caught up with his judgment. It is also, as of that review, a named commitment with an effective-immediately deadline attached, not a quiet pattern I am hoping he outgrows. I would rather the committee hear that from me, with the context, than find the rating alone and wonder what it means.

Marcus is ready for Staff Engineer. The level asks for technical judgment the rest of the team can build on, and for the discipline to turn a technical loss into a better team decision instead of a grudge. I watched him do both in the same week, on a decision that now runs our production notification traffic. I recommend him without reservation, and I am glad to discuss any part of this further.

Sincerely,
Ana Rivera
Tech Lead, Notification Service
Lattice Notify
arivera@latticenotify.com

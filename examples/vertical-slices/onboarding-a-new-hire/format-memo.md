---
entry_id: memo
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

TO: Backend Services Team
FROM: Mei, Onboarding DRI
DATE: July 6, 2026
RE: Two-Week Guided Pairing as the Standard Onboarding Protocol for New Engineers

Effective immediately, the two-week guided pairing protocol piloted with Priya's onboarding is the standard onboarding process for every new engineer joining Backend Services. The structure trialed under ADR-0023 is no longer a one-off arrangement for a single hire; it is how this team onboards going forward.

The pilot ran three fixed domains against a two-week window. Access and tooling were resolved in the first two days, with a named buddy owning a printed checklist and verifying each item directly with the new hire rather than assuming it was done. Codebase orientation filled week one: two ninety-minute guided walkthroughs, one on service topology and one on deployment and on-call tooling, plus a Friday check-in to catch anything blocked before it cost a second week. A first real change was scoped and ready before Priya's start date, so week two was implementation, not a search for something to work on. She opened her pull request, Arjun paired on the review, and the change shipped inside the two-week window.

The retrospective held this past Friday confirmed the structure did what it was designed to do. Access friction stayed contained to a single named owner instead of spreading across the team, and Priya was contributing to design discussion and catching edge cases by the end of week one, not week four. One gap surfaced during the pilot, a missing VPN certificate step, and has already been folded into the team's setup documentation so the next new hire will not hit it.

Three elements of this protocol are now standing practice, not decisions made case by case. Every new engineer is assigned a named buddy and a pre-scoped first change before their start date, not after. Every new engineer follows the same three-domain structure: access and tooling in days one and two, guided orientation in week one, a paired shipped change in week two. Every new engineer is excluded from the on-call rotation for their first 30 days, regardless of prior experience elsewhere.

This has a real cost, and sprint planning should account for it openly rather than absorb it quietly. A buddy should expect to lose roughly 30-40% of their capacity in the new hire's first week and 15-20% in the second. Managers assigning a buddy should plan sprint scope around this the same way they would plan around any other known reduction in capacity.

The onboarding guide in the team repository remains the operational reference for how to run each step; this memo is the record of the protocol's adoption. Other teams in engineering are welcome to adapt the structure for their own onboarding.

This memo establishes structured guided pairing as Backend Services' standard onboarding protocol for all new engineers going forward, superseding informal or ad hoc onboarding arrangements.

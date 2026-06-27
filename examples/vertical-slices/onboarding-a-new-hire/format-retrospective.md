---
entry_id: retrospective
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Retrospective: Priya Onboarding - Jun 22 to Jul 3

## Date

Fri Jul 3

## What Went Well

- Pre-scoping the first change before week one started meant Priya had a real task waiting in week two. The team made that decision without her; she did not have to wait for us to figure it out after she arrived.
- The access and tooling checklist gave day-one friction a named owner. When the setup doc turned out to be missing the VPN cert step, Priya caught it immediately because she was following the doc step-by-step. Mei patched the doc the same day. Nobody spent time in a silent gap wondering who was responsible.
- Guided walkthroughs front-loaded the architecture before Priya encountered it under pressure. By Day 3 she was navigating the three services she will own without hand-holding, including locating the test harness and naming conventions on her own.
- Pulling Priya into the Thursday design session as a co-driver rather than an observer produced an immediate return: she caught an edge case the team had missed. It also established her as a contributor before her first PR landed.
- Belonging was tracked alongside functional milestones, not assumed from them. Three async threads opened between Priya and teammates outside the formal protocol. That signal came from how the two weeks were structured, not from a dedicated "be welcoming" checklist item.

## What Did Not Go Well

- The staging access provisioning request went in on Jun 23 and sat in the infra queue for the remainder of the two weeks. The on-call alert drill had to be deferred because Priya did not have her own credentials. The team covered with a shared credential, but that was a workaround that masked the gap rather than fixing it.
- The setup doc gap (missing VPN cert step) was caught because Priya followed the doc precisely and got a hard error. A less thorough new hire would have self-debugged without surfacing it. The doc was fixed, but the review process did not catch it before her first day.
- Buddy capacity was absorbed but not planned for. The sprint carried standard load through both weeks. Arjun covered the week-two deficit informally. The cost was real and invisible to velocity tracking; it did not appear anywhere until this retro.
- The belonging vs. function question was flagged as a risk in the week-one status report but not operationalized until today. A single question at the end of week one would have been more actionable than a watch-list risk note.

## What Will We Change

- [ ] Move the staging access provisioning request to the week before a new hire's start date, not day one or day two. Add this step to the pre-boarding checklist. Owner: Mei - By: pre-boarding prep for next hire (target start Aug 4)
- [ ] Run a dry-run of the setup doc against a clean machine before each new hire's first day. Assign to whoever holds the buddy role for that cycle. Owner: Arjun (for next cycle) - By: one week before next hire's start date
- [ ] Add buddy capacity to sprint planning as a standing flag: 30% reduction for the primary buddy in week one, 15% in week two. This belongs in the sprint planning template, not the onboarding protocol. Owner: Mei - By: next sprint planning session (Jul 7)
- [ ] Add a ten-minute belonging check-in at the end of week one with one explicit prompt: "What has felt off this week that you have not said out loud yet?" Log the answer even when the answer is nothing. Owner: Mei - By: protocol update Jul 10

## Notes

Priya's first change was merged on Jul 3 before EOD. She drove the full deploy cycle. The formal onboarding window closes today with no open blockers.

The on-call alert drill was deferred, not cancelled. Rescheduled target: Jul 9, contingent on staging access resolving by Jul 7. The infra escalation is active; Mei owns the follow-up.

Priya is on the on-call rotation calendar starting week five. The buddy relationship with Arjun is expected to continue informally; the team should treat that as a feature of the protocol, not drift from it.

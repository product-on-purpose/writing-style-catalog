---
entry_id: proposal
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Project Halyard: Team Retrospective and Recognition Program
## Prepared for: Engineering Director
## Prepared by: Yuki Tanaka, Program Lead
## Date: June 20, 2026

## Executive Summary

Project Halyard delivered a clean checkout cutover on June 13 after fourteen months of parallel-track work. The team caught two production-threatening defects through careful judgment rather than automated gates, and absorbed two schedule slips rather than ship a system they could not stand behind. Standard sprint retrospective formats and standard recognition channels are not built for this kind of effort. This proposal asks for your approval of two days of engineering time and a $2,700 budget to run a structured retrospective and team recognition event before the team disperses to follow-on assignments.

## The Problem

Your organization completed the most complex internal engineering project of the past three years, and the standard tools for marking that completion do not fit what actually happened.

A sprint retrospective format assumes weeks of recent events. The Halyard team has fourteen months of material, two near-miss incidents with detailed postmortems, and a set of judgment calls made under real schedule pressure that do not appear in ticket metadata or commit logs. Compressing that history into a standard "what went well / what did not" format drops the most important causal detail and leaves the team with a document that does not reflect the experience.

Standard recognition is also not scaled to what specific contributors did. A Slack announcement or an all-hands mention can acknowledge that a project shipped. It cannot distinguish between the engineers who met the minimum bar and the engineers who, at specific moments, made the harder call:

- Dani Rowe called the hold on the March launch window when the schedule pressure was real and the February near-miss was not fully resolved.
- Marcus Teel filed the February bug when he could have marked it low severity and moved on. The fix was his initiative, not a response to escalation.
- Jordan Osei rewrote the payment callback handler over a weekend when a smaller patch was available and tempting.
- Sam Wickfield held the regression bar on June 9 when every hour of delay felt enormous and the pressure to ship was at its peak.

None of that shows up in delivery metrics. If the organization does not formally name and record those decisions, it does not learn from them, and the individuals do not receive acknowledgment proportional to what they contributed.

## Proposed Approach

A two-part program, run in the ten days remaining before the team disperses to follow-on assignments.

**Part 1 - Structured retrospective (June 30).** A half-day session with an outside facilitator, not a team member who was inside the same schedule pressure. The Halyard team has strong internal trust and does not need outside help to communicate, but a facilitator who was not in the room can ask the questions the team might sidestep. The output is a one-page decision log and a short set of transferable lessons for the engineering organization - not a standard sprint retro artifact.

**Part 2 - Team recognition event (week of July 7).** A team dinner, off-site, during working hours. This is not a reward for shipping; it is a formal acknowledgment that fourteen months of parallel-track work represents a different order of commitment than a standard project. The team carried significant operational overhead with no visible output for most of that period. The framing matters: this marks what the team sustained, not only what they delivered.

Four individual recognition letters will be drafted for Dani Rowe, Marcus Teel, Jordan Osei, and Sam Wickfield, naming the specific decisions each person made and the consequences those decisions prevented. The letters go to the individuals and to their direct managers. Priya Vasquez will review for accuracy before they are sent.

## Scope and Deliverables

**Included:**
- Retrospective session design and facilitation (June 30, half-day, up to ten attendees)
- One-page decision log drafted by the facilitator from session output, reviewed by Priya Vasquez
- Team recognition event logistics and coordination (week of July 7, up to twelve attendees)
- Four individual recognition letters, reviewed, and sent to recipients and their managers

**Not included:**
- External publication or blog post from the retrospective - that is a separate decision about what the organization wants to share publicly
- Formal performance review documentation - these letters are supplementary and do not modify formal review inputs
- Retrospective scope for teams outside the Halyard project

## Timeline

| Date | Action |
|------|--------|
| June 24 | Your approval confirmed; facilitator contract signed; June 30 slot booked |
| June 27 | Retrospective agenda distributed to all attendees |
| June 30 | Retrospective session (half-day, up to ten attendees) |
| July 3 | Decision log draft circulated to Priya Vasquez for accuracy review |
| July 7 | Team recognition event (dinner, up to twelve attendees) |
| July 10 | Individual recognition letters sent to recipients and their managers |

## Team and Credentials

Yuki Tanaka will coordinate all logistics and own the recognition letters. Priya Vasquez will serve as content reviewer for accuracy on all written outputs; she managed the program for fourteen months and can verify that the specific decisions named in the letters are described correctly. The retrospective facilitator will be an external contractor sourced from the approved vendor list.

## Investment

| Item | Estimated cost |
|------|---------------|
| Retrospective facilitation (external contractor, half-day) | $1,800 |
| Team recognition event (dinner, up to twelve attendees) | $900 |
| Coordinator time (Yuki Tanaka, est. 6 hours) | Internal |
| Program lead review (Priya Vasquez, est. 2 hours) | Internal |
| **Total cash outlay** | **$2,700** |

Engineering time: ten attendees at a half-day each equals five person-days. This is a one-time cost against a fourteen-month investment. No travel budget is required; all attendees are local.

## Next Steps

Please reply by June 24 confirming approval to proceed. That confirmation unlocks the facilitator booking and event logistics, both of which need lead time to close before June 30.

If budget approval requires a separate procurement step, flag that by June 24 and the timeline will adjust accordingly. The retrospective date has some flexibility; the team dispersion window does not.

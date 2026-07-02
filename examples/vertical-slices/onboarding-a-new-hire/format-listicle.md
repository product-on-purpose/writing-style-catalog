---
entry_id: listicle
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# 6 Things We're Taking Into the Next Onboarding Cycle

*Mei, onboarding DRI - posted Fri Jul 3, after the retro*

Priya's retro wrapped this afternoon and her first change is already deployed. The next new hire starts Aug 4, which means the 32-day gap between now and then is exactly enough time to write down what we would repeat, unedited, and what needs to change before we run this again.

1. **A named buddy owns the checklist, not a queue.** Arjun held the access and tooling checklist from day one, and nothing on it counted as done until Priya verified it herself. She had full access and a working local environment by Monday afternoon of week one. The one gap, a missing VPN cert step, surfaced immediately because Priya was following the doc exactly, and Arjun patched it into the doc that same day instead of leaving it for the next person to trip over.

2. **The first real change was chosen before she arrived.** The team picked Priya's task before her first day: one service, no on-call risk if it went wrong. She co-drove the design session on Thursday of week one and caught an edge case the team had missed, then opened the PR Wednesday of week two. It merged and deployed Friday afternoon, before end of day, with Priya driving the full deploy herself.

3. **Two 90-minute walkthroughs beat a week of solo docs.** Instead of pointing Priya at the architecture and service-map docs and leaving her to read alone, Arjun ran two guided sessions: one on service topology, one on deploy and on-call tooling. Priya kept her own notes; nobody wrote them for her. By Wednesday of week one she was navigating the three services she will own without hand-holding, including finding the test harness and the team's naming conventions on her own.

4. **The buddy's lost capacity is now a template line, not a memory.** Arjun's output dropped an estimated 30-40% in week one and 15-20% in week two, and sprint planning accounted for that before Priya's first day. Nobody could point to the actual cost until the retro named it out loud. Next cycle it becomes a standing flag in the sprint template, 30% in week one and 15% in week two, instead of a range someone has to remember to apply.

5. **Staging access filed on day two sat for the full two weeks.** The provisioning ticket went in Jun 23 and never cleared the infra queue, which pushed Priya onto a shared credential and moved her on-call alert drill from Jul 2 to Jul 9. The workaround covered the gap without closing it. The fix is not a faster ticket, it is filing the request before the new hire's first day instead of during week one.

6. **Belonging got asked about directly, not inferred from a green status.** Week one's Friday check-in covered blockers and codebase navigation, both functional questions with functional answers. The belonging question sat as a watch-list risk until today's retro asked it outright, later than it should have. Priya's answer was reassuring, but the next cycle moves that question to the end of week one instead of holding it for the two-week close.

The buddy checklist and the pre-scoped first task go into the next cycle unchanged. Everything else on this list is a small date or a small question moved earlier, which is usually what fixing a process actually looks like.

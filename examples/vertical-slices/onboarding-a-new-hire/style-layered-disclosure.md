---
entry_id: layered-disclosure
axis: style
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Getting Priya productive in two weeks, on a team that ships daily to production and carries an on-call rotation, comes down to two concrete outcomes: she ships something real by Friday of week two, and she ends those two weeks knowing she belongs, not just that she has credentials. Every decision about how to spend those fourteen days should be tested against those two outcomes.

## Week one: access before day one, pairing by day three

Access requests have longer lead times than most teams remember. File them the week before Priya starts: repository permissions, environment credentials, the ticket tracker, the chat tool, production read access. She should be able to clone and run the service on day one. If she cannot, the whole first week compresses into bureaucracy.

By day three, she should be paired on a real task. Not a sandbox exercise - a small bug or a bounded cleanup that will actually merge. The goal is that her first code review is about her code, not about whether she can navigate a tutorial. Pair programming is not about teaching; it is about doing real work together so that the codebase becomes familiar through use.

## Week two: the first ship

Pick the task for her first independent change at the end of week one, before she has to ask. It should be small enough that the review will be quick and bounded, and real enough that it touches the production path. A change to a configuration parameter, a small improvement to a logging statement, a minor fix to an endpoint she read the code for during pairing - anything in the actual service, not a test harness.

Walk her through the deployment checklist alongside her, not ahead of her. The point is not to remove uncertainty; it is to show her where uncertainty lives and how the team handles it. By the time the deploy runs, she should know who to call if something breaks and how to tell whether something has broken.

## The human side: belonging is built in specifics

Belonging is not produced by a welcome lunch. It accumulates through small signals that she was expected: her name already in the on-call rotation calendar (not yet on duty, but present), introductions framed as "this is Priya, she owns X" rather than "this is our new hire," her opinion solicited in a team decision during week two.

The on-call rotation is worth a separate conversation early in week one - not to assign her, but to explain the system: what gets paged, who handles it, how postmortems work, when to escalate. This is not administration. It is the fastest way to show her how the team thinks about reliability and shared responsibility.

By the end of week two, she should be able to answer three questions: who do I ask when I am stuck? What does the team care about? What did I ship? If those three questions have answers, the first two weeks worked.

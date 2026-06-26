---
entry_id: narrative-case-study
axis: style
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# What Priya's first Thursday told us

When Priya started on a Monday in February, the team sent her a welcome message in the chat tool, provisioned her laptop, and added her to the on-call rotation calendar. Nobody said when she would go live on rotation.

By Wednesday afternoon she had credentials to three of the five systems she needed. The ticket tracker she could read but not write to. The deployment pipeline was blocked pending an approval request that had been submitted but not yet surfaced to anyone. She read the service READs for the two services she had been told were "her area." She found references to a data model called the canonical event graph in eleven places. The term was not defined anywhere in those READs.

On Thursday she attended a live incident response call. The team was competent and fast. Priya listened for forty minutes, said nothing, and closed her laptop when it ended with the sense that she had watched a film in a language she was learning.

Her manager, Claire, noticed. Not because Priya said anything - she did not - but because Claire had been tracking a metric she had started keeping after the previous hire. She counted the days between a new engineer's start date and their first merged pull request. The two engineers before Priya had taken twelve and eleven days respectively. The one before them had taken twenty-two.

Claire made two changes in week two. First, she sat with Priya for ninety minutes Monday morning and walked the canonical event graph from scratch on the whiteboard. Not the full system - just the seventeen nodes Priya would actually touch in the coming month. Second, she picked a single real bug: a missed null check in the routing layer that had been sitting on the board for four days. She handed it to Priya as her only assigned work for the week. Not a tutorial task. A real bug affecting real traffic.

Priya fixed it. The pull request took her until Thursday to feel confident submitting. The team reviewed it without softening the feedback: two rounds, one structural comment, one naming question. It merged Friday afternoon.

At the retrospective that same Friday she offered one observation about the deploy sequence. Claire acted on it the following Monday.

The principle that emerged was not complicated: the engineer who belongs is the one whose work has already mattered. Structured context first, then real responsibility, before the end of week two. That ordering is not instinct for most teams - it has to be decided deliberately, early in the first week, before proximity starts substituting for planning.

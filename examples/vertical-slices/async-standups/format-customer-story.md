---
entry_id: customer-story
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Fernbridge Software: How Ending a 9:30pm Standup Cut Blocker Response Time to 18 Minutes

## About Fernbridge Software

Fernbridge Software is a Seattle-headquartered engineering organization. Its core engineering team has grown to eleven people spread across four time zones, from the US Pacific coast to India Standard Time, and its internal processes are built for a distributed team by default.

## The Challenge

Fernbridge Software's engineering team had grown from 6 to 11 people over 18 months, and its daily standup had not grown with it. The meeting stayed fixed at 9am Pacific, which put it at 9:30pm for the three engineers working from India.

The cost showed up in the data before anyone named it. Q1 attendance averaged 3.2 of 5 standups a week for the India-based engineers, against 4.6 for engineers in the US. The gap was not a motivation problem. It was a scheduling problem: a third of the team was being asked to sit through a status meeting after 9pm.

The meeting was not paying for itself even for the people who could attend it. It ran 14 minutes on average, but a month of analysis found only about 4.2 of those minutes were content that changed what anyone did next: a blocker raised, a dependency flagged, real context shared. The other 10 minutes went to status nobody needed to act on. The cost of that gap was concrete: three separate incidents in one quarter where an engineer spent over an hour re-solving a problem someone else had already fixed and mentioned out loud in a standup that nobody had written down.

## The Solution

Rather than rotate the meeting across time zones, which solves the equity problem for one group by breaking it for another, or buy a dedicated async-standup tool, Fernbridge Software's engineering team designed its own lightweight practice: the Async-First Standup Playbook.

Each engineer now posts a written update to the #team-standup channel by 10am their own local time, using a fixed three-field template: what shipped, what is in progress, and what is blocked or at risk, with a direct mention of whoever can unblock it. An on-call engineer checks the channel each morning and responds to flagged blockers within 30 minutes during business hours. The 9am Pacific meeting slot is gone. In its place is a single 60-minute working session held on Thursdays, reserved for discussion that genuinely needs everyone live, not for status updates.

## The Results

On-time posting climbed from 78 percent in the pilot's first week to 85.5 percent in the second, and held near that level for the rest of the 30-day trial. The median time between a flagged blocker and a substantive reply fell to 18 minutes, replacing a pattern where a blocker raised in the morning often did not get a real answer until the afternoon.

The clearest change was in who showed up. Under the old schedule, the India-based engineers had attended 3.2 of 5 standups a week, not from lack of effort but because the meeting landed at 9:30pm. During the pilot, they posted an update every weekday, the first time that had happened on this team.

"The number I keep coming back to is that our India-based engineers posted an update every single weekday of the pilot. That never happened under the old system. It was not that they did not care. It was that we were asking them to show up at 9:30 at night. Fix the schedule and the participation problem disappears on its own," said Jordan Ellis, Engineering Manager, Fernbridge Software.

The 30-day trial ended without a debate about whether to keep it. The Async-First Standup Playbook is now standard practice across the team, folded into onboarding for new hires, with no further trial review scheduled. Fernbridge Software will revisit the format only if a future retrospective turns up a problem the current template cannot handle.

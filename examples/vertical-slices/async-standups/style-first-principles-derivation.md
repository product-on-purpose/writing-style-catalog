---
entry_id: first-principles-derivation
axis: style
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-5-5
review_status: reviewed
---

The question is whether our standup should be async-first. Nobody has to accept the answer I reach, so I will start from six premises that I think we all grant, build only from them, and mark the one that carries the weight.

**Premises**

- **P1.** The team has 11 engineers across four timezones: US Pacific (3), US Eastern (3), UK (2), and India (3).
- **P2.** The standup is at 9am Pacific, which is 9:30pm India Standard Time. This is an input, read off the calendar.
- **P3.** Input from the Q1 attendance record: the three India engineers averaged 3.2 appearances out of 5 per week, and the US engineers averaged 4.6.
- **P4.** Input from last month's tally: the meeting averages 14 minutes, and 4.2 of those minutes changed someone's behavior, meaning a blocker was raised, a dependency was flagged, or context was shared. The rest was status that needed no response from anyone.
- **P5.** Input from last quarter: three times an engineer spent more than an hour on a problem that had already been solved and discussed in a standup. Nothing from the meeting was written down, so nobody could search for it.
- **P6.** A daily meeting also gives the team brief, unplanned contact with one another. This has value that a written post does not carry.

**Derivation**

*Step 1, from P2 and P3.* A single fixed time puts the whole cost of its hour on whoever is furthest from it. The gap between 3.2 and 4.6 is 1.4 appearances per week. A person at 9:30pm who attends less often has not stopped caring. Their absence is the cost of the time slot. So the meeting is not equally available to all 11 of us, and the people it excludes are the same three people every week.

*Step 2, from P4.* Of 14 minutes, 4.2 changed behavior. That is 30 percent, and the other 9.8 minutes carried content that required no reply. The content that changed behavior is a blocker, a flag, or a piece of context. Each of those can be written in a sentence. Nothing in the 4.2 minutes needs two people speaking at once.

*Step 3, from P5.* The meeting leaves no record. Three repeated hours of work in a quarter are what an unrecorded meeting costs. A written post is a record by construction, since writing it is the act of recording it.

*Step 4, from Steps 1, 2 and 3.* The behavior-changing content can be written (Step 2), a written version persists where the spoken one does not (Step 3), and a written version can be posted by each engineer at a time that suits their own timezone (Step 1). So a written post by each person, before 10am their local time, delivers the 4.2 minutes to everyone and costs nobody a 9:30pm meeting.

*Step 5, arithmetic.* Five meetings of 14 minutes is 70 minutes per engineer per week. If the daily meeting goes, that time is released. If a blocker is @mentioned to the person who can resolve it, that person is told directly and does not have to be present at a meeting to hear about it.

*Step 6, from P6.* The written post does not replace unplanned contact. Step 4 therefore removes something real. To keep it, a smaller amount of shared time must remain: one 60-minute working session on Thursday for questions that need a live exchange. Of the 70 minutes released in Step 5, 60 are spent here. That is a conscious trade of daily presence for one concentrated hour, and it is not a free gain.

**Consequence**

If P1 through P6 are granted and Steps 1 through 6 follow as stated, the team should move to async-first standups: a three-field written post by 10am local time, with the on-call engineer answering blocked items, and one Thursday working session for what needs real-time exchange.

**Where to push**

The load-bearing premise is P4, together with the assumption Step 2 rests on: that the content which changed behavior can be written without losing what made it work. If a blocker usually needs the back-and-forth of a spoken conversation to become clear, then a three-field template will hide blockers that the meeting used to surface, and Step 4 fails. In that case the right move would be a meeting at a rotating time, which fixes Step 1 but not Step 3.

P6 is the second joint. If you think daily presence is worth more than one hour of Thursday contact, you reject the sizing in Step 6, and the answer shifts toward a shorter live standup that keeps its 9:30pm cost. I do not think P3 or P5 is where a reader will disagree, but both are inputs from our own records and either can be challenged as such.

---
entry_id: op-ed
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# We Deleted Our Daily Standup. Yours Should Go Too.

*By Jordan Ellis*

Two weeks ago I signed a one-paragraph memo that deleted a recurring meeting from eleven engineers' calendars, and it is the best process decision I have made as an engineering manager. If your team spans more than two time zones and you are still holding a daily synchronous standup, delete yours too. You do not need a year of debate to get there. Thirty days of data was enough for us.

I run an eleven-person engineering team at Fernbridge Software, split across four time zones: US Pacific, US Eastern, the UK, and India. Eighteen months ago we were a six-person team, and a 9am Pacific standup worked fine for the people in the room. We hired, the team spread across the map, and nobody redesigned the meeting to match the team we had actually become. It stayed fixed at 9am Pacific, which lands at 9:30pm for the three engineers who joined us from India. We told ourselves that was a minor inconvenience. It was not minor, and it did not fall on everyone evenly.

Our own Q1 numbers said what none of us wanted to say out loud: the India-based part of the team averaged 3.2 standups out of 5 each week, against 4.6 for everyone working on a US clock. For months we quietly treated this as an engagement problem and wondered, without saying it out loud, whether those three engineers cared less. They did not care less. They were being asked to sit through a status meeting after their kids were asleep, night after night, and eventually some of them stopped showing up. That is not a motivation gap. That is a design flaw, and it was ours to fix.

The people who could attend were not getting much out of the meeting either. We timed a month of our own standups: fourteen minutes on the clock, and by our own count, only about four of those minutes changed what anyone actually did that day. The other ten were status nobody needed delivered out loud. Worse, none of it stuck. We found three separate cases last quarter where an engineer burned over an hour rediscovering a bug a teammate had already solved and mentioned, once, in a standup nobody could search afterward. A meeting that leaves no record is not a coordination tool. It is a performance with a 9am curtain.

So instead of arguing about this in the abstract for another year, we ran a 30-day trial. We replaced the meeting with a three-field written update, posted to a shared Slack channel by 10am each person's own local time: what shipped, what is in progress, what is blocked and who needs to see it. Someone reads the channel every morning and chases anything tagged. By the end of the trial, on-time posting had climbed from 78 percent to 85.5 percent, the median time from a flagged blocker to a real response had dropped to 18 minutes, and every one of our India-based engineers posted an update on every single weekday of the trial's final two weeks. That had not happened once in this team's history under the old system. We made the new format permanent on June 23. It was not a close call.

The objection I hear most is that a written update cannot replace the human contact of a daily call, and I do not think that objection is wrong. A few engineers said exactly this in their trial debriefs; they missed the small daily contact. But the fix for that is not keeping a status meeting alive as a stand-in for a relationship. We moved our old standup slot to a single 60-minute working session each week, built for actual discussion instead of status updates, and it has done more for how this team knows each other than five short calls a week ever managed. None of this required new software or a consultant, just a Slack channel, a pinned template, and someone willing to read it every morning. If your team is spread across more than two time zones and you are still holding a daily call because that is simply how it has always been done, run your own 30 days before you spend another year defending it. The math will make the argument for you. Ours did.

---

*Jordan Ellis is an engineering manager at Fernbridge Software in Seattle.*

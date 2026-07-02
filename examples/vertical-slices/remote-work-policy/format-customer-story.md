---
entry_id: customer-story
axis: format
topic_slug: remote-work-policy
topic_label: Arguing a public position on return-to-office
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Platform Engineering: From a Six-Week Thread to One Tuesday Session

## About Platform Engineering

Platform Engineering owns the internal services every other product team depends on: the deployment pipeline, the shared authentication layer, the internal API gateway. About a dozen engineers, spread across four time zones, several hired specifically because the team no longer required a local office for every role. Before ADR-0012 made two weekly anchor days company-wide policy, the team had spent more than a year under the same loosely defined "flexible" arrangement as everyone else: come in when you want, coordinate however you can.

## The Challenge

That looseness had a cost, and it showed up in specific, avoidable ways. Architecture decisions that used to resolve themselves in a corridor conversation were languishing in Slack threads for weeks instead, because the two or three people who needed to weigh in were rarely online at the same time on purpose, only by coincidence. New hires joining a fully distributed team took visibly longer to build the kind of trust that used to come from overhearing a conversation or catching someone between meetings. One schema migration review sat open for six weeks and got reopened three separate times, because the reviewers kept missing each other by a day or two. Nobody on the team was against being in the same room. Nobody had a reason to be, on any given day.

## The Solution

When Priya Ahluwalia's Policy Working Group asked for a pilot team ahead of ADR-0012, Platform Engineering volunteered. The team adopted the hybrid-anchor framework's two-day model exactly as written: Tuesday and Thursday as fixed anchor days for anyone who could physically reach an office, everything else left to individual judgment. Following the framework's own guidance, the team protected those two days from one-off exceptions for a full quarter before allowing any opt-outs, and moved its recurring rituals (standup, planning, one-on-ones) onto the anchor days on purpose, so the in-person time did double duty instead of competing with focus time.

## The Results

The stuck schema migration review was the first real test. Under the new model, the same reviewers who had been missing each other for six weeks sat down together on a Tuesday and closed it in one session. That became the pattern, not the exception: cross-team architecture questions that used to circulate for weeks now mostly resolve inside a single anchor-day block, because the people who need to be in the room already are.

The framework's other bet paid off too. Two of the team's engineers were hired from cities where the company has no office; under a five-day mandate, neither hire would have happened. Under the anchor-day model, they are simply exempt on the days they cannot physically reach an office, and the team kept two engineers it could not have hired any other way.

"We weren't the team that wanted this the least or the most," said Marcus Webb, Platform Engineering's manager. "We were just the team stuck longest in threads that should have been five-minute conversations. Two fixed days didn't fix everything, but it gave us back the room we'd lost. That was the whole problem to begin with."

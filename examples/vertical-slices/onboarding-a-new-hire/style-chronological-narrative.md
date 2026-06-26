---
entry_id: chronological-narrative
axis: style
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Priya arrived on Monday morning with her laptop in a bag and the name of one person to find: her team lead, Marcus. He had left her a note in the ticket tracker the previous Friday, pointing to the access request doc and the setup checklist. She read both before she found her desk.

By noon she had submitted the access requests. By the end of the day she was waiting on three of them. Marcus had expected this; he had already messaged the infrastructure team to prioritize her credentials. The next morning they came through.

That Wednesday, Marcus paired with her for two hours on the codebase. He did not give her a slide deck. He pulled up the service map and traced one request end to end, narrating as he went. She took notes. When he finished she had questions, and he answered them, but he also noticed which questions she asked: she wanted to know who owned which service, not just how it worked. He sent her a message that afternoon introducing her to Dani, who owned the three services that would touch any change she made in her first month.

By the end of the first week she had read the on-call runbook, attended the daily ship meeting, and watched two deploys go out. She had not touched the code yet.

The second Monday, Marcus assigned her a bug: a timeout in one of Dani's services that was logged but not alarmed. Small, real, and already understood. Priya found the fix in an hour but spent the rest of the morning reading the surrounding code because she wanted to understand the pattern, not just close the ticket. She opened a pull request that afternoon.

The review came back the next day with two comments, both from Dani. One was a nit. The other pointed to a shared utility Priya had reimplemented without knowing it existed. She updated the pull request, thanked Dani, and asked where else that utility was used. Dani answered, then added: "Nice catch on the root cause, by the way."

On Friday of week two, Priya merged the change. The deploy ran. The timeout disappeared from the logs. At the end-of-week retro, someone asked if she had gotten her first ship in. She said yes. Marcus said nothing; the team's reaction was enough.

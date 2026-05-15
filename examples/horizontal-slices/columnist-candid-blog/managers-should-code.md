---
entry_id: columnist
axis: voice
topic_slug: managers-should-code
topic_label: Engineering managers should write code
voice_id: columnist
tone_id: candid
style_id: classical-argument
format_id: blog-post-long-form
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Engineering Managers Should Write Code

I had a conversation recently with a director I respect, who has not written code in about four years, about whether to break apart a service. He had opinions. They were reasonable opinions. They were also, to anyone who had touched the code in the last six months, about eighteen months out of date. He did not know that. His team knew it, politely worked around it, and made the decision without him. He left the meeting thinking he had given useful input. I left thinking about how this happens to almost everyone who fully steps away.

So here is the position I want to argue. Engineering managers who fully step away from writing code lose load-bearing context within about eighteen months, and from that point on they are a slow, structural liability to their teams. The fix is not to go back to feature work. The fix is to maintain small, real, non-blocking contributions - tooling, internal utilities, occasional bug fixes, the occasional rough prototype - so the manager's hands stay in the codebase the team is actually shipping. "I committed once last quarter and I am still technical" is not the same thing.

## The eighteen-month problem

Software systems decay against your understanding of them at a predictable rate. In any team of three or more engineers shipping continuously, the codebase you knew eighteen months ago is a different codebase now. Frameworks have changed minor versions. Patterns the team agreed on in your absence have hardened into local conventions. The directory you remember has been refactored twice. The service boundaries you sketched on a whiteboard have been redrawn, usually because the original drawing was wrong in a way that only became visible once someone tried to live inside it.

You can survive this for a while on residual knowledge plus the manager's job of asking good questions. But the residue runs out. The questions you used to ask, which used to land because they came from someone who had recently been in the code, start landing differently. They sound like a person asking from outside. The team answers them politely and goes back to work. The small ambient awareness of where the rough edges actually live is gone, and you do not notice it is gone because nothing dramatic happens. You just become slightly less useful at every architectural decision for the next two years.

This is the failure mode I have seen most often, in myself and in managers I have worked for. It does not look like a crisis. It looks like meetings where the manager's opinion is heard, weighted lower than it used to be, and quietly outvoted by the people closer to the work.

## What the small contributions are actually for

Here is the warrant. The reason to keep coding as a manager is not to ship features. You are not on the team to ship features, and you should not be on the critical path of any deliverable. The reason is calibration. You need a current, honest sense of how hard things actually are in this codebase, on this team, with these tools. That sense is what makes the rest of your job - estimating, prioritizing, advocating for headcount, pushing back on unrealistic deadlines - work.

The contributions that calibrate you are small and off the critical path. The internal CLI nobody else wants to maintain. The flaky test that has been bothering everyone. The data migration script that runs once and gets thrown away. The five-line bug fix in a part of the codebase you used to know well. None of these are heroic. None will land you a promotion. All of them put your hands on the keyboard for a few hours a week in the systems your team is working in, and that is what prevents the eighteen-month decay.

What does not work, in my experience, is the gesture commit. The pull request you made because it had been a while. The architecture diagram you drew in Excalidraw and called technical contribution. The pairing session where the engineer drove and you watched. These are not nothing, but they do not give you the texture of the code. The texture is in the keyboarding, in the small frustrations, in the moments where you realize your test setup is genuinely hostile to new contributors. You only learn that by being a new contributor, in your own codebase, on a small enough scope that it does not matter if it takes three days.

## What about focusing on people

The strongest version of the case against me goes like this. Engineering management is a real discipline, not "engineer who manages people." The job is people, growth, hiring, prioritization, organizational health, and a hundred other things that are not coding. Managers who keep one foot in the code starve those activities. The right model is to be excellent at the manager job and trust the engineers to be excellent at the engineering job. Anything else is a manager who does not actually believe their team can do the work.

I want to take this seriously, because there is a real version of it that is correct.

A manager who codes because they cannot let go of being an engineer is a bad manager. A manager who reviews every PR because they do not trust the team is a bad manager. A manager who picks up the high-status feature work and crowds out their senior engineers is a bad manager. If your coding is taking time from your one-on-ones, your hiring loops, or the difficult conversations you have been putting off, you are coding wrong and you should stop.

The incorrect part is the leap from "do not crowd out the team" to "do not code at all." The argument for stepping fully out assumes calibration is free - that you can stay current through standups and one-on-ones and skip-levels. You cannot. The information you get from those channels is filtered through the team's interpretation of the code, which is the thing you need a direct read on. Reading code is not enough. The work is in the friction of changing it.

The honest version of the people-focused argument is, "Managers should focus mostly on people, and should keep a thin, deliberate strand of technical contribution to stay calibrated." That version, I agree with. The absolutist version, where managers stop touching the code entirely, is the version I have watched produce the directors who give confidently wrong opinions in architecture meetings.

## Closing

If you are a manager and you have not committed code in the last six weeks, I would be candid about what that means. It does not mean you are bad at your job. It means the part of your job that depends on knowing what your team is working with is going out of date, and the cost is being absorbed quietly by the team rather than charged back to you. The fix is one small, non-blocking thing this month. Then another next month. Your team will not say thank you, because they will not notice anything has changed. That is the point.

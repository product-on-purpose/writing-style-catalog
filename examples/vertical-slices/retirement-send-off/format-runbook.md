---
entry_id: runbook
axis: format
topic_slug: retirement-send-off
topic_label: Marking a long-serving colleague's departure
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Runbook: Howard Thayer Retirement Send-Off - June 25, 2026

## Overview

Execute the all-hands retirement send-off for Howard Thayer on June 25, 2026 at 2:00 PM, marking the conclusion of his twenty-six years as Operations Coordinator at Crestfield Group; trigger this runbook no later than one week before the event date.

## Prerequisites

- [ ] Conference Room A booked 1:30 PM - 4:00 PM on June 25, 2026
- [ ] AV tested: projector, room microphone, and speakers confirmed functional
- [ ] Video conferencing link active and distributed to all remote invitees
- [ ] Recording enabled; storage path confirmed at /ops/events/retirement-2026/howard-thayer/
- [ ] Regional site coordinator notified that they will receive the recording link in place of in-person attendance
- [ ] RSVP count closed and logged (target: 40 in-person; remote dial-in open)
- [ ] Team gift confirmed received and held by Carolyn Marsh prior to 1:30 PM
- [ ] Howard Thayer confirmed attending and briefed on approximate timing
- [ ] Dana Reyes and Marcus Okonkwo confirmed as speakers and briefed on three-minute cap
- [ ] Backup facilitator identified in case Carolyn Marsh is unavailable on the day

## Procedure

1. **Open Conference Room A** at 1:30 PM and verify all AV: projector displaying title slide, microphone live, remote dial-in active, recording started.
   Expected output: Remote attendees confirm they can see the room and hear audio; recording indicator is active.

2. **Log the headcount** at 2:00 PM before starting remarks. Record in-person count and remote attendee count in the event log at /ops/events/retirement-2026/howard-thayer/attendance.txt.
   Expected output: Two numbers recorded - in-person and remote - before any remarks begin.

3. **Welcome attendees** and state the purpose: this is Howard's official send-off after twenty-six years with Crestfield Group. Remind the room that the session is being recorded for the regional site, which could not send a representative.
   Expected output: Room is settled and attentive; no unresolved technical interruptions.

4. **Introduce Dana Reyes** and invite her to speak. She will speak to the incident-response runbook Howard drafted with her and Marcus Okonkwo during the knowledge transfer sessions in May and June. Cap is three minutes.
   Expected output: Dana completes her remarks. If she runs past three minutes, do not interrupt; note the overage and adjust step 5 accordingly.

5. **Introduce Marcus Okonkwo** and invite him to speak. He will speak to the operational handoff work and what Howard's presence meant to the team through the transition. Cap is three minutes.
   Expected output: Marcus completes his remarks.

6. **Open the floor** for two minutes of open remarks from any attendee. Accept up to three contributions. Do not solicit beyond the allotted window.
   Expected output: Zero to three contributions received and acknowledged. Proceed to step 7 whether or not anyone speaks up.

7. **Present the team gift** to Howard on behalf of Crestfield Group. Hand it directly to Howard. A brief verbal acknowledgment is sufficient; no extended speech is needed here.
   Expected output: Gift in Howard's hands; room applauds.

8. **Invite Howard to speak.** Do not state a time limit aloud. He will determine his own pace. Do not interrupt or signal time.
   Expected output: Howard delivers closing remarks. Remain attentive and do not start transitioning the room while he is speaking.

9. **Close the formal portion** immediately after Howard finishes. Thank all attendees. Announce that the recording will be posted within 24 hours and will be flagged for the regional site. Declare informal time open for in-person attendees who wish to stay.
   Expected output: Formal session declared closed. Remote attendees may drop; recording may be stopped.

10. **Stop the recording** and verify the file exists at /ops/events/retirement-2026/howard-thayer/. Confirm file size is nonzero before leaving the room.
    Expected output: Recording file is visible on the shared drive with a nonzero file size.

11. **Post the recording link** to the all-staff channel within 24 hours. Include a note in the message flagging the link for the regional site coordinator.
    Expected output: Link posted to all-staff channel; regional site coordinator confirms receipt by reply or direct message.

## Verification

The send-off is complete when all of the following are true:

- Attendance counts (in-person and remote) are logged in /ops/events/retirement-2026/howard-thayer/attendance.txt.
- Howard received the team gift and spoke.
- Recording file is saved, nonzero, and accessible at the confirmed storage path.
- Recording link has been posted to the all-staff channel and acknowledged by the regional site coordinator.

## Rollback

Rescheduling is not available: Howard's final day is June 27, 2026, and the all-hands is scheduled for June 25. If a minor issue occurs during the event (AV failure, speaker cancels, low remote attendance), continue with what is available. Partial execution is preferable to postponement.

If Howard is unable to attend on June 25 due to illness or personal emergency: contact Carolyn Marsh (cmarsh@crestfieldgroup.internal) immediately. Post a brief message to the all-staff channel acknowledging the postponement without disclosing Howard's reason. Attempt to reschedule within his remaining two days; if that is not possible, hold an asynchronous send-off via the all-staff channel with a written message and the option for video contributions.

## Escalation

**AV or technical failure during the event:** Contact Facilities at facilities@crestfieldgroup.internal. If unresolvable within five minutes, continue without projection and with room microphone only. Inform remote attendees via chat that projection is unavailable and ask them to confirm audio is intact before proceeding.

**Recording fails to save after the event:** Contact IT support at itsupport@crestfieldgroup.internal with the file path and the time range. A recording captured on a participant's device may substitute if the original is unrecoverable. The regional site coordinator must be notified of any delay beyond the 24-hour window.

**Howard is unable to attend and rescheduling within June 25 - 27 is not feasible:** Contact Carolyn Marsh and the direct management team. The asynchronous fallback in the Rollback section becomes the plan of record.

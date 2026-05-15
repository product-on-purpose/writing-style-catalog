# Recipe: operator-direct-runbook

A composition of `operator` voice, `matter-of-fact` tone, `how-to-tutorial` style, and `technical-reference` format. Used for production runbooks that on-call engineers read under pressure.

## When to use

Use this recipe for any document that an on-call engineer will open while a system is degraded or down. It fits service-specific runbooks, incident response checklists, failover procedures, and any "if you see X, do Y" guide where the reader is paged, tired, and needs exact steps with exact commands. The recipe assumes the reader is mid-incident, not learning the system for the first time.

## When to use something else

If the audience is a new hire learning the platform for orientation, swap `operator` for `friendly-mentor` and `matter-of-fact` for `encouraging` - the reader needs context and confidence, not just commands. If the document is explaining why the system is designed the way it is, reach for `pragmatic-architect` voice and `diataxis-explanation` style; runbooks deliberately strip out design rationale to keep the path to action short. If the situation is a post-incident communication to leadership or customers, `executive` voice with a `one-pager` format will land better than a runbook structure built for execution.

## Composition

| Axis | Entry | Why |
|------|-------|-----|
| Voice | `operator` | The reader has been paged. They need named services, exact flag values, named escalation contacts, and active-voice imperatives. Operator is the only voice that treats unclear documentation as a real cost rather than a stylistic preference. |
| Tone | `matter-of-fact` | The situation already supplies urgency. Adding it to the prose with intensifiers or warnings makes the document harder to scan. Matter-of-fact states what is true, lists what to run, and trusts the reader to feel the appropriate amount of stress without coaching. |
| Style | `how-to-tutorial` | The reader has one job: complete the procedure. Numbered atomic steps, prerequisites listed up front, expected outcomes after each step, and an explicit escalation path when the runbook fails to resolve the issue. One action per step is the rule that holds under pressure. |
| Format | `technical-reference` | A runbook is consulted, not read. Scannable headers, tables for diagnostic queries, fenced code blocks for exact commands, and a stable structure the reader can navigate by memory after the third time they have used it. |

## Worked examples on this recipe

- [Restart the auth service](restart-auth-service.md)
- [Investigate elevated p99 latency](investigate-p99-latency.md)
- [Fail over the primary database](database-failover.md)

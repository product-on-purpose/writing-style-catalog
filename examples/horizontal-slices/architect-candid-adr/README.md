# Recipe: architect-candid-adr

A composition of `pragmatic-architect` voice, `candid` tone, `decision-log` style, and `adr` format. Used for hard technical decisions that need to be documented honestly with their tradeoffs named.

## When to use

You have a load-bearing architectural call to make, the decision is hard, and the team needs the reasoning preserved for future engineers who will inherit the consequences. This recipe fits when you are choosing between defensible options where the deciding factor is which failure modes you can live with. It is the right tool for migrations, sunsetting, vendor selections, and platform commitments where the cost of being wrong is paid out over months.

## When to use something else

If the decision has already been made and you are communicating it to a broader audience, a one-pager or email in `executive` voice fits better. If the document is meant to persuade a skeptical reader rather than record a reasoned choice, a `problem-solution` style RFC carries more rhetorical force. If the audience is non-technical and the goal is alignment rather than technical durability, drop the ADR format and write a `narrative-case-study` in `warm` tone.

## Composition

| Axis | Entry | Why |
|------|-------|-----|
| Voice | `pragmatic-architect` | Leads with the decision, names constraints by type, and treats tradeoffs as known rather than discovered. The voice the future maintainer needs to hear. |
| Tone | `candid` | The hard part of these decisions is naming what we are giving up. Candid tone refuses to soften the negative consequences section, which is where ADRs earn their value. |
| Style | `decision-log` | Captures context, options, and reasoning at decision time rather than retrofitting a justification. The future reader can audit the reasoning even if the outcome disappoints. |
| Format | `adr` | Short, structured, numbered. Lives next to the code. Conventional Status / Context / Decision / Consequences sections give readers a predictable shape to scan. |

## Worked examples on this recipe

- [Migrate from REST to GraphQL](rest-to-graphql.md)
- [Adopt Kubernetes for staging deployments](kubernetes-staging.md)
- [Sunset the legacy auth service](sunset-legacy-auth.md)

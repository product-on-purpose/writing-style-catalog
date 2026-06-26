---
entry_id: readme
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Backend Services Team - Engineer Onboarding

![setup status](https://ci.example.internal/badge/onboarding-bootstrap-passing) ![on-call eligible](https://ci.example.internal/badge/oncall-week-five) ![ship target](https://ci.example.internal/badge/first-ship-week-two)

> Two-week onboarding guide for engineers joining the backend services team: access to shipping, start to belonging.

This guide covers what a new engineer needs in their first two weeks: access and tooling, codebase orientation, team context, a first real change shipped, and enough of the human side to feel like they belong and not just function. It is also for the teammate doing the pairing - the guide tells you both what week one looks like and what success at the end of week two means.

The team deploys daily and runs a shared on-call rotation. Getting comfortable with both is the orientation goal, not a test.

## Setup

Request any of the following that are not yet provisioned through the IT portal:

- Source control org membership
- VPN credentials and SSO setup
- CI/CD pipeline access
- Observability platform (logs, traces, metrics)
- On-call rotation viewer (actual on-call starts week five)
- Secret manager read access for staging
- Chat tool: add to `#backend-services`, `#incidents`, `#deployments`, `#team-random`

Once access lands, bootstrap the local environment:

```bash
git clone git@source.example.internal:backend/services.git
cd services
./scripts/bootstrap.sh
```

`bootstrap.sh` installs local tooling, sets environment variables, and runs the local health check suite. It exits non-zero and prints what is missing if any access is still pending.

## Quick start

```bash
make start-local          # starts all services in docker compose
make smoke-test           # runs the minimal end-to-end suite
make logs SERVICE=orders  # tail one service to see the shape of a real request
```

If `smoke-test` passes, the environment is healthy. If it fails, start with `docs/troubleshooting.md` before asking a teammate.

## Week one

The goal of week one is orientation, not output. Three things matter:

**Trace the system.** Read `docs/architecture-overview.md` and `docs/service-map.md`, then use the observability platform to trace one real production request from the API gateway to the data store. Reading without tracing leaves the architecture abstract.

**Meet the owners.** The `docs/ownership.md` file lists which teammates own the services Priya will most likely touch first. One-on-ones with those three people in week one are worth more than any doc.

**Watch a deploy.** Pair with the on-call engineer on one daily deploy before week one ends. The release process is not abstract when you have seen it once.

Hold a thirty-minute check-in on Friday of week one: is anything blocked, can Priya navigate the codebase on her own, are there gaps in the access list above?

## Week two

Pick one ticket from the `good-first-issue` label. Good criteria: touches one service and one data model, has a test that can be written in under an hour, does not require on-call context to understand.

The pairing engineer reviews the PR. Priya does the deploy. The point is not the change itself - it is that she owns the full cycle end to end.

The belonging side matters as much as the output. By the end of week two, Priya should know who to ask, not just where to look.

## Documentation

- [Architecture overview](docs/architecture-overview.md)
- [Service map and ownership](docs/ownership.md)
- [Local setup troubleshooting](docs/troubleshooting.md)
- [How we deploy](docs/deployment-guide.md)
- [On-call runbook](docs/on-call-runbook.md)
- [Code review process](docs/code-review-guide.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to open a PR, get it reviewed, and merge it.

## License

Internal use only.

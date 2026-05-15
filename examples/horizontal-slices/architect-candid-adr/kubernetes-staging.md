---
entry_id: pragmatic-architect
axis: voice
topic_slug: kubernetes-staging
topic_label: Adopt Kubernetes for staging deployments
voice_id: pragmatic-architect
tone_id: candid
style_id: decision-log
format_id: adr
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# ADR-0043: Do Not Adopt Kubernetes for Staging Deployments

## Status

Accepted

## Context

Our staging environment currently runs on three EC2 instances behind an ALB, provisioned and configured with Ansible playbooks we maintain in-house. The playbooks are six years old, partially undocumented, and primarily understood by two engineers, one of whom is the on-call rotation's longest-serving member. Deploys to staging take roughly 8 minutes and fail roughly 1 time in 20, usually for reasons related to drift between the Ansible-provisioned state and what is actually running on the boxes.

A proposal was raised to move staging to Kubernetes, with two arguments:

1. **Parity with future production.** There is an ongoing conversation about whether production should move to Kubernetes in the next 12 to 18 months. Running staging on Kubernetes first would give the team production-like operational experience in a lower-stakes environment.
2. **Modernize the deploy path.** Replacing the Ansible playbooks with declarative manifests would eliminate the drift problem and make staging deploys faster and more reliable.

I want to be direct about what this decision actually involves. The two arguments above are real, but the second one solves a problem (Ansible drift) by adopting a system (Kubernetes) that is significantly more complex than the problem warrants. The first argument is real only if we commit to Kubernetes in production, which we have not done.

The team is six engineers. None of us has shipped Kubernetes in production. Two have run kind clusters locally for personal projects. Our current staging footprint is three EC2 instances and a database. The "small footprint" framing is accurate.

We considered three options:

1. Move staging to Kubernetes (EKS), starting in Q3.
2. Stay on EC2 + Ansible. Continue paying the drift tax.
3. Move staging to ECS Fargate. Replaces the Ansible playbooks with declarative task definitions. Solves the drift problem without taking on cluster operations.

## Decision

Move staging to ECS Fargate over the next quarter. Do not adopt Kubernetes.

The drift problem is real and worth solving. Fargate solves it. Container images are immutable; task definitions are declarative; we do not run any host machines. The migration is roughly two engineer-weeks of work based on a spike I ran last sprint. The new deploy path will take under 3 minutes and will not fail for reasons of drift.

If and when we decide to run production on Kubernetes, we will revisit staging. At that point the parity argument becomes load-bearing, and we will accept the operational cost knowing what we are buying. Right now we would be paying the cost without a confirmed buyer.

## Consequences

### Positive

- Deploy reliability improves. Drift-related failures go to zero. Deploy time drops from 8 minutes to under 3.
- The Ansible playbooks can be retired. The two engineers who maintain them recover that cognitive load.
- Onboarding new engineers gets easier. Fargate task definitions are roughly 80 lines of YAML and behave the same in every environment. The Ansible playbooks took new engineers two weeks to feel confident in.
- We preserve the option to adopt Kubernetes later, on its own merits, when the production case is concrete.

### Negative

- We will have less Kubernetes operational experience when the production conversation comes back around. If we end up choosing Kubernetes for production, we will be learning it under higher-stakes conditions. This is a real cost and I want to name it - the people advocating for the original proposal are not wrong that experience compounds.
- Fargate has its own footguns: cold start latency on new tasks, IAM permission complexity around task roles, and a slightly opinionated networking model. We will hit some of these in the migration.
- Some product engineers wanted to learn Kubernetes through this project. That career-development value is real, and we are choosing not to provide it through this particular vehicle. We should find another way - a learning sprint, conference budget, or a non-production sandbox cluster - to address it.

### Neutral

- The CI/CD pipeline will need rewiring. The current GitHub Actions workflow runs Ansible; the new one will push container images and update task definitions. This is mechanical work of roughly one engineer-week.
- Monitoring shifts. We currently collect host metrics via the Datadog agent on the EC2 instances. On Fargate we move to the AWS-managed Datadog integration plus application-level metrics. Some dashboards will need to be rebuilt.
- The decision is reversible. If we move production to Kubernetes in 2027 and decide we want staging parity at that point, the work to migrate staging from Fargate to EKS is bounded and predictable.

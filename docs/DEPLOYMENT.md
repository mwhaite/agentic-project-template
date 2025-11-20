# Deployment Template

Use this template to describe how to deploy and release the project safely.

## Environments
List each environment with purpose, access patterns, and critical differences (feature flags, data sets, credentials).

## Prerequisites
- Required accounts/permissions
- Infrastructure dependencies (e.g., cloud resources, DNS, secrets)
- Build artifacts and how they are produced

## Deployment Steps
1. Build artifacts (commands)
2. Run pre-deploy checks/tests
3. Roll out (manual steps or pipeline stages)
4. Post-deploy verification/health checks
5. Rollback procedure (commands, triggers, timeouts)

## Release Management
- Versioning strategy and tagging
- Change management/approvals
- Feature flags and gradual rollout plans

## Monitoring & Alerting
- Dashboards and alerts to watch immediately after deployment
- KPIs and error budgets

---
## Instructions for AI Agents
1. Keep steps deterministic and scriptable; avoid manual steps when possible.
2. Always include rollback guidance before rollout steps.
3. If deployment is not yet defined, propose a minimal manual flow and mark follow-ups.

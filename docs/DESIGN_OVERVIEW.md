# Design Overview Template

Use this template to capture the foundational design of a new project or feature before implementation begins. Keep entries concise, actionable, and oriented toward an MVP-first approach.

## Mission & Problem Statement
- **What problem are we solving?**
- **Who is affected?**
- **Why now?**

## Goals & Non-Goals
- **Goals:** Bullet the concrete outcomes we must achieve.
- **Non-Goals:** Explicitly list what is out of scope for the initial release.

## Users & Use Cases
- **Primary users:** Who will use this?
- **Key use cases:** Top 3–5 scenarios this design must satisfy.
- **User journey:** Briefly outline the flow from start to finish for the MVP path.

## Success Criteria
- **Functional success:** What must be true for this to be considered done?
- **Operational success:** Telemetry, reliability, or support expectations.
- **Agent handoff:** What artifacts should agents produce (tests, docs, checklists)?

## Constraints & Assumptions
- **Technical constraints:** Languages, frameworks, platforms, performance needs.
- **Business/operational constraints:** Deadlines, compliance, approvals.
- **Assumptions:** Items believed true that should be validated early.

## Risks & Mitigations
- **Top risks:** List 3–5 risks with likelihood/impact.
- **Mitigations:** Immediate steps to reduce risk.

## MVP Definition
- **Scope:** Minimum functionality that delivers user value.
- **Deferred items:** Features intentionally postponed until after MVP.
- **Acceptance checklist:** Binary criteria to confirm MVP completion.

## Dependencies
- **Internal:** Reuse of existing services, components, or data models.
- **External:** Third-party APIs/services and their availability/SLA.

## Open Questions
Track unresolved decisions or clarifications needed before build. Convert answered items into decisions or constraints above.

---
## Instructions for AI Agents
1. Fill this template before architecture work; keep responses succinct.
2. Prefer ranked lists and checklists that map to atomic commits.
3. When uncertain, record questions explicitly instead of guessing.
4. Link to supporting artifacts (context, research notes, spikes) as they are created.

# Architecture Template

Use this document to capture the high-level system design that will guide implementation. Keep the design as small as possible to achieve the MVP while leaving room to evolve.

## System Overview
Provide a concise narrative of how the system delivers value, including its deployment context (cloud, on-prem, hybrid) and the primary runtime components.

## Component Model
List the major components/services, their responsibilities, and how they collaborate.
- **Component:**
  - Purpose:
  - Interfaces:
  - Data owned:
  - Dependencies:

## Data Flow
Describe the critical data paths, request/response flows, and background processing. Diagrams welcome.

## Technology Choices
Document the selected languages, frameworks, data stores, messaging, and infrastructure. Include rationale and alternatives considered.

## API & Contracts
Summarize externally visible APIs (HTTP/gRPC/CLI/events). Link to `API.md` for detailed endpoint/shape definitions.

## Deployment & Environments
- **Environments:** dev/stage/prod (or equivalents)
- **Topology:** containers, serverless, VMs, etc.
- **Scaling strategy:** horizontal/vertical, autoscaling triggers.
- **Resilience:** redundancy, graceful degradation, circuit breakers.

## Security & Compliance
- Authentication & authorization approach
- Data protection: encryption in transit/at rest, key management
- Compliance or privacy requirements

## Observability
- Metrics to collect and alert on
- Logging/structured events
- Tracing strategy

## Performance & Capacity
State target throughput/latency and expected load profile. Note assumptions used for capacity planning.

## Architecture Decisions
Capture key decisions (link ADRs when formalized):
- Decision:
  - Date:
  - Context:
  - Outcome:
  - Consequences:

---
## Instructions for AI Agents
1. Draft this after completing `docs/DESIGN_OVERVIEW.md` to ensure alignment with goals.
2. Bias toward simplicity and incremental delivery; call out what is postponed until after MVP.
3. Prefer checklists and tables for clarity; avoid ambiguous prose.
4. When uncertain, propose options with trade-offs and request confirmation before proceeding.

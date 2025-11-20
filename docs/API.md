# API Template

Use this template to define the externally visible contracts for the project. Keep it synchronized with implementation and tests.

## Overview
- **API style:** REST/gRPC/GraphQL/CLI/events
- **Auth model:** e.g., OAuth2, API keys, session tokens
- **Versioning strategy:** URL-based, header-based, or semantic tags
- **Rate limits & quotas:** Document defaults and override rules

## Resources / Endpoints
For each resource or command, capture the contract. Add examples that agents can replay in tests.

### Endpoint
- **Method/Verb:**
- **Path/Command:**
- **Description:**
- **Headers:** Required/optional
- **Query/Args:**
- **Request body:** Schema or example
- **Response:** Success schema and HTTP status/exit codes
- **Errors:** Standardized error shapes and retryability guidance
- **Notes:** Idempotency, pagination, sorting, filtering

## Data Models
Document request/response schemas, including field types and validation rules.

## Security Considerations
- **Authentication requirements**
- **Authorization rules**
- **Data sensitivity:** PII/PCI/PHI flags
- **Input validation:** Expectations and rejection patterns

## Testing Hooks
- **Contract tests:** How to assert compatibility
- **Mocking/stubs:** How to simulate dependencies
- **Golden examples:** Copy/pasteable requests and responses

---
## Instructions for AI Agents
1. Keep examples concise and executable; prefer cURL/HTTPie/CLI snippets.
2. When uncertain, propose conservative defaults and request confirmation.
3. Align this doc with `docs/ARCHITECTURE.md` and update alongside code changes.

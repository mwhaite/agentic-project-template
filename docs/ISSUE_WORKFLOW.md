# GitHub Issues and Comments for Agent Context

Use GitHub issues, comments, and feature requests as the primary way to capture and pass context between agents and humans. This workflow keeps work decomposed, traceable, and ready for atomic commits.

## When to open an issue
- **Feature requests:** Use `.github/ISSUE_TEMPLATE/feature_request.md` to capture desired behavior, scope, and acceptance criteria.
- **Planning / context capture:** Use `.github/ISSUE_TEMPLATE/agent_context.md` to log mission, constraints, and an ordered outline of steps.
- **Bugs / chores:** Create an issue with the relevant template and link to the mission/context issue so the agent can ingest both.

## How to write agent-friendly issues
1. **Lead with outcome:** Describe what success looks like, not the implementation.
2. **Surface constraints early:** Note non-goals, environment limits, and sequencing rules near the top.
3. **Link source material:** Always include the design doc, TODO items, ADRs, or discussions an agent must ingest.
4. **Decompose:** List the smallest possible sequential steps/commits under "Delivery Plan" to reduce ambiguity.
5. **Flag handoffs:** Use the "Notes for Agents" section to say what to read first and what to update after finishing.

## Using comments for continuity
- At the end of each work session, leave a comment that states:
  - What changed
  - What remains
  - Next command(s) or prompts to run
  - Files/documents to re-open first
- Prefer bullet points or numbered lists for easy ingestion.
- If an assumption was validated or rejected, add a short note and link to the source.

## Pull requests as context bundles
- Summarize the intent, scope, and acceptance criteria in the PR description.
- Link the originating issue(s) so agents can follow the thread of context.
- Add checklists to the PR body for required prompts/checks.
- If scope changes mid-PR, update the description so downstream agents inherit the latest intent.

## Operational tips
- Use labels to signal priority, stage (discovery/MVP/feature), and risk level.
- Keep issues small: close the issue after the MVP slice is merged, and open follow-ups for post-MVP features.
- Mirror key context in `docs/` or `.agentic/` files when it must persist beyond the issue tracker.

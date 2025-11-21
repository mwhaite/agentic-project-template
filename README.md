# agentic-project-template

Minimal base project template for agentic systems with guiding documents and bootstrap prompts.

## Quick Start
1. Review `TODO.md` to see the current plan for evolving this template.
2. Fill in `.agentic/PROJECT_CONTEXT.md` with project-specific details.
3. Walk through `docs/ONBOARDING_CHECKLIST.md` step by step to bootstrap your fork.
4. Use `.agentic/BOOTSTRAP.md` as the prompt sequence for agentic assistants.
5. Use the GitHub issue templates to capture feature requests and planning context for agents (`docs/ISSUE_WORKFLOW.md`).
6. Populate the documentation templates in `docs/` (design overview, architecture, API, setup, deployment, troubleshooting, examples) as you define the project.

## Repository Scaffolding
- `src/`: Application source code. Organize modules by domain or feature to keep changes atomic.
- `tests/`: Automated tests aligned with the source structure for fast feedback.
- `scripts/`: Helper scripts for local development, automation, or maintenance tasks.
- `config/`: Configuration samples and defaults (never secrets). Add env templates or service config examples here.
- `requirements.txt`: Empty Python dependency manifest ready for agents to populate.
- `package.json`: Neutral Node manifest with TODO fields and empty sections for scripts and dependencies.

## What This Template Provides
- Agent-ready prompts and context files under `.agentic/`
- Issue templates for agent-friendly feature requests and planning
- A repository-level TODO roadmap for building out the template
- An onboarding checklist to drive sequential setup and MVP-first delivery
- Placeholder documentation structure under `docs/`

## Next Steps
See `TODO.md` for the ordered backlog, and contribute improvements via small, atomic commits that align with the MVP-first approach.

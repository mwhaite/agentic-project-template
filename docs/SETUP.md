# Setup Template

Use this checklist to standardize local development setup across forks.

## Prerequisites
- Operating system(s) supported
- Required runtimes (e.g., Python/Node/Java) with versions
- Package managers/tools (e.g., pip, npm, pnpm, uv, poetry, brew)
- Required accounts or credentials (note how to store them securely)

## Environment Setup Steps
1. Clone the repository
2. Configure environment variables or `.env` (list keys and purpose)
3. Install dependencies (command(s))
4. Run initial validation (linters/tests) to confirm setup
5. Start the development server or entry point (if applicable)

## Tooling
- Linters/formatters and how to run them
- Type checkers or static analysis tools
- Git hooks (pre-commit) setup if used

## Local Data & Services
- How to run dependent services locally (containers, mocks, emulators)
- Seed data or fixtures

## Troubleshooting Setup
Link to `docs/TROUBLESHOOTING.md` for common issues.

---
## Instructions for AI Agents
1. Keep commands copy/pasteable and OS-agnostic when possible.
2. Default to the simplest stack; avoid optional tools unless justified.
3. When adding dependencies, update this file and `docs/DEPENDENCIES.md` (if present).

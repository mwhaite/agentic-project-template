# Contributing Guide

This project is an agent-friendly template. Start by reviewing the [README](README.md) for the repository overview and quick-start context before making changes.

## Branch Naming
- Use short, kebab-case branch names that describe the work.
- Prefix with the work type when useful, for example:
  - `feature/add-pr-template`
  - `chore/update-onboarding-docs`
  - `bugfix/fix-ci-workflow`
- Avoid reusing long-lived branches; prefer fresh branches per change set.

## Commit Message Format
- Follow the conventional `type(scope): summary` style, keeping the summary under 72 characters.
- Common types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`.
- Scope is optional but recommended for clarity (e.g., `docs(contributing): add guidelines`).
- Body (when needed) should explain the motivation and highlight breaking changes.

## Pull Request Checklist
Before opening a PR, make sure you:
- [ ] Rebased onto the latest `main` and resolved conflicts locally.
- [ ] Kept commits small and logically grouped.
- [ ] Added or updated relevant docs, tests, and automation where appropriate.
- [ ] Verified formatting, linting, and tests pass locally.
- [ ] Linked the related issue or task and provided context for reviewers.
- [ ] Included a concise summary and testing notes in the PR description.

## Expectations for Agent-Generated Work
- Read applicable project context (e.g., `.agentic/PROJECT_CONTEXT.md`, `docs/ONBOARDING_CHECKLIST.md`) before making changes.
- Respect existing conventions and instructions in repository docs; when in doubt, prefer minimal, atomic diffs.
- Explain assumptions in commit messages and PR descriptions to help reviewers understand automated decisions.
- Avoid introducing dependencies or tooling changes without justification.
- Include reproducible commands for any checks or scripts you run.

## Quick Start Commands
Use these commands to spin up a contribution quickly:

```bash
# Create and switch to a new branch
BRANCH="feature/short-description"
git checkout -b "$BRANCH"

# Make commits following the conventional format
# Example: git commit -m "docs(contributing): add guidelines"

# Push the branch and open a PR (replace origin if using a fork)
git push -u origin "$BRANCH"
# If you use the GitHub CLI, you can open a PR with:
# gh pr create --fill
```

Refer back to the [README](README.md) for the broader repository guide and onboarding steps.

# Contributing Guide

This project is built for agent-driven workflows. Start with the main [README](./README.md) to understand the repository scaffolding and onboarding steps before contributing.

## Branch Naming
- Use short, kebab-case branches prefixed by the change type, such as `feature/<summary>`, `fix/<summary>`, or `chore/<summary>`.
- Keep branch names descriptive but concise (ideally under 40 characters after the prefix).
- Align branch scope to a single, reviewable unit of work.

## Commit Message Format
- Follow Conventional Commits: `<type>[: scope]: <short summary>` (e.g., `feat: add PR checklist`).
- Common types: `feat`, `fix`, `chore`, `docs`, `refactor`, `test`, `ci`.
- Use the imperative mood and limit the subject line to 72 characters.
- If needed, add a concise body explaining context and any breaking changes.

## Pull Request Checklist
Before opening a PR, ensure you:
- Rebase on the latest `main` and resolve conflicts locally.
- Keep changes small and focused; split unrelated updates into separate PRs.
- Update or add tests and documentation relevant to your change.
- Run available linters or test suites and include results in the PR description.
- Provide a clear summary of changes and any manual verification steps.

## Expectations for Agent-Generated Work
- Follow any repository `AGENTS.md` instructions within the scope of touched files.
- Prefer deterministic, small diffs; avoid unnecessary reformatting.
- Do not add secrets or credentials; keep configuration values templated or documented.
- Document assumptions and edge cases in commit messages or PR notes.
- Cite sources or outputs when describing test results in PRs.

## Quick Start Commands
- Create a branch: `git checkout -b feature/<summary>`
- Rebase with main: `git pull --rebase origin main`
- Stage and commit: `git add <paths> && git commit -m "<type>: <summary>"`
- Push and open a PR (after configuring `origin`): `git push -u origin feature/<summary>`
- Create a PR via the CLI (GitHub CLI): `gh pr create --fill`

By following these conventions, you help keep the repository cohesive and reviewer-friendly.

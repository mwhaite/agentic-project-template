# Agent Onboarding Checklist

Follow this sequence to bring a fork of the base template online. Each step links to the guiding documents or prompts needed.

## 1) Align on Context and Goals
- [ ] Capture project specifics in `.agentic/PROJECT_CONTEXT.md` (fill all TODOs).
- [ ] Confirm non-goals and constraints with the requester.
- [ ] Translate the high-level mission into a short success statement for the README.

## 2) Choose Minimal Stack Assumptions
- [ ] Decide whether to stay language-agnostic or select an initial stack (Python/Node/etc.).
- [ ] If choosing a stack, drop in the matching manifest stub (e.g., `requirements.txt`, `package.json`).
- [ ] Log early dependency intentions in `.agentic/DEPENDENCIES.md`.

## 3) Design at a High Level
- [ ] Draft architecture in `.agentic/ARCHITECTURE.md` using the template sections.
- [ ] Identify components required for the first vertical slice.
- [ ] Record any Architectural Decision Records (ADRs) if choices are made.

## 4) Plan the Work into Atomic Commits
- [ ] Break down goals into a linear set of atomic commits aimed at the MVP.
- [ ] Mark feature work as "post-MVP" to avoid scope creep.
- [ ] Add the ordered list of commits to `TODO.md` or the project board.
- [ ] Open planning/feature issues using the templates in `.github/ISSUE_TEMPLATE/` so agents inherit the right context (`docs/ISSUE_WORKFLOW.md`).

## 5) Prepare Bootstrapping Prompts
- [ ] Review `.agentic/BOOTSTRAP.md` and adapt prompts as needed for the current stack.
- [ ] Store any runbook-style prompts in `docs/prompts/` (create if missing).
- [ ] Ensure prompts reference the templates for README, design doc, and mission statement.

## 6) Execute the MVP Plan
- [ ] Implement the first vertical slice end-to-end before expanding scope.
- [ ] Add minimal tests covering the slice.
- [ ] Update documentation placeholders with concrete instructions and examples.

## 7) Transition to Feature Development
- [ ] Enable branch/PR workflow per CONTRIBUTING once MVP is stable.
- [ ] Move deferred features into their own branches with clear acceptance criteria.
- [ ] Keep README and docs synced with new capabilities.

## 8) Validate and Retrospective
- [ ] Run through the bootstrap steps with an agent to identify gaps.
- [ ] Capture learnings and update checklists/templates accordingly.

---

Use this checklist as the default startup script: work top-to-bottom, and do not skip ahead until the preceding steps are complete.

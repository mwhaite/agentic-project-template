# Bootstrapping Crew (CrewAI-ready)

Use this crew to fork the template, interrogate the user, research requirements, and drive the repo toward an MVP skeleton. The crew assumes the operator has the GitHub CLI (`gh`) installed and will provide any project documentation paths or pasted content the agents request.

## How to run it
1. Install dependencies: `pip install -r requirements.txt`
2. Launch the crew: `python scripts/bootstrapping_crew.py --project-name "My Project" --template-repo org/repo`
3. Provide answers and documentation paths when the Engagement Lead asks; the crew will follow the phases below.

## Crew Composition
- **Engagement Lead** — interviews the user, extracts goals, constraints, success metrics, and documentation locations. Owns decision checkpoints with the user.
- **Research Navigator** — uses browsing tools or provided documents to confirm requirements, competitive baselines, and platform constraints. Summarizes findings with citations for the crew.
- **Repo Wrangler** — handles forking/cloning with `gh`, manages remotes, and captures repository-level context (default branch, branch protection expectations, templating).
- **Systems Architect** — translates requirements into architecture options, object relationships, data boundaries, and API surfaces. Produces an initial architecture note for review.
- **Scaffolding Engineer** — generates code skeletons, dependency manifests, and minimal implementations aligned with the architect’s decisions. Keeps structure synchronized with `docs/` templates.
- **Issue Tracker** — turns the roadmap into GitHub issues/milestones using `gh issue create`, ensuring each issue has clear acceptance criteria and owner hints for future agents.

## Quickstart CrewAI Sketch
This pseudo-configuration can be dropped into a CrewAI project. Replace `tools=[...]` with the actual browser, file, and GitHub utilities available in your environment.

```python
from crewai import Agent, Task, Crew

engagement_lead = Agent(
    role="Engagement Lead",
    goal="Capture user intent, constraints, and delivery checkpoints",
    backstory="Seasoned facilitator who keeps scope realistic and documented",
    tools=["browser", "file_search"],
)

research_navigator = Agent(
    role="Research Navigator",
    goal="Validate requirements and surface platform limitations",
    backstory="Analyst who cross-references docs, repos, and public sources",
    tools=["browser", "file_search"],
)

repo_wrangler = Agent(
    role="Repo Wrangler",
    goal="Fork/clone repo and prepare branches using gh CLI conventions",
    backstory="DevOps-minded engineer comfortable with GitHub automation",
    tools=["terminal", "gh_cli"],
)

systems_architect = Agent(
    role="Systems Architect",
    goal="Propose architecture, data contracts, and object relations",
    backstory="Architect who values MVP-first delivery and explicit tradeoffs",
    tools=["diagramming", "file_writer"],
)

scaffolding_engineer = Agent(
    role="Scaffolding Engineer",
    goal="Lay down minimal code, dependency manifests, and docs",
    backstory="Builder focused on fast, clean scaffolds with tests and docs",
    tools=["file_writer", "terminal"],
)

issue_tracker = Agent(
    role="Issue Tracker",
    goal="Translate the roadmap into actionable GitHub issues",
    backstory="Project manager fluent with gh CLI and acceptance criteria",
    tools=["gh_cli", "file_writer"],
)

crew = Crew(
    agents=[
        engagement_lead,
        research_navigator,
        repo_wrangler,
        systems_architect,
        scaffolding_engineer,
        issue_tracker,
    ],
    tasks=[],  # populate from the workplan phases below
)
```

## Workplan (User-Interactive, Research-Driven)
Each phase produces artifacts or commits and checkpoints with the user before proceeding.

1. **Intake & Context Sync (Engagement Lead)**
   - Ask for project name, target users, success criteria, constraints, and provided documentation paths.
   - Confirm preferred stack or leave open for Architect recommendation.
   - Capture answers in `.agentic/PROJECT_CONTEXT.md` or a new `docs/CONTEXT.md` note.

2. **Repository Fork & Setup (Repo Wrangler)**
   - `gh repo fork <template> --clone` and set upstream to the template.
   - `git checkout -b chore/bootstrap` as the working branch.
   - Record remotes and branch defaults in `docs/SETUP.md`.

3. **Requirement Validation (Research Navigator)**
   - Read provided docs and repository content; if allowed, run quick external research for integrations/competitors.
   - Summarize confirmed requirements, open questions, and platform constraints in `docs/DESIGN_OVERVIEW.md`.
   - Loop back with the user to close gaps.

4. **Architecture & Object Model (Systems Architect)**
   - Define core domain objects, relations, and data flow (include diagrams if possible).
   - Draft interfaces/APIs and persistence choices; log tradeoffs and MVP scope in `docs/ARCHITECTURE.md`.
   - Align with the Engagement Lead for signoff.

5. **Scaffolding & Dependencies (Scaffolding Engineer)**
   - Create or update manifests (`requirements.txt`, `package.json`) with chosen stack.
   - Generate module skeletons, domain models, and placeholder services/tests reflecting the object relations.
   - Add minimal CI/config stubs if appropriate; update `docs/SETUP.md` with install/run commands.

6. **Documentation Pass (Engagement Lead + Scaffolding Engineer)**
   - Fill README with project summary, setup, and quickstart commands.
   - Add API/usage examples or stubs in `docs/API.md` and `docs/EXAMPLES.md`.
   - Note known risks and follow-ups in `docs/TROUBLESHOOTING.md`.

7. **Issue Generation (Issue Tracker)**
   - Convert the roadmap into GitHub issues: `gh issue create --title "<feature>" --body "steps, AC, owner"`.
   - Label issues by area (architecture, backend, frontend, docs, infra) and milestone (MVP vs post-MVP).
   - Create a tracking issue linking all MVP tasks.

8. **Handoff & Next Steps (All)**
   - Share a status summary with links to docs, branches, and issues.
   - Agree on the next working session or automation trigger.

### Task Wiring for CrewAI
Map the phases to CrewAI tasks (simplified example):

```python
from crewai import Task

crew.tasks = [
    Task(description="Interview user and capture constraints", agent=engagement_lead,
         expected_output="Updated project context note"),
    Task(description="Fork and prepare repo with gh", agent=repo_wrangler,
         expected_output="Forked repo, branch created, remotes documented"),
    Task(description="Research requirements and summarize findings", agent=research_navigator,
         expected_output="Design overview with confirmed requirements"),
    Task(description="Draft architecture and object model", agent=systems_architect,
         expected_output="Architecture doc plus object relationships"),
    Task(description="Generate scaffold and dependencies", agent=scaffolding_engineer,
         expected_output="Code skeleton and updated manifests/docs"),
    Task(description="Create GitHub issues for roadmap", agent=issue_tracker,
         expected_output="Issue list covering MVP and follow-ups"),
]
```

Use this as a living playbook: adjust roles and phases per project while keeping the MVP-first discipline.

"""Runnable CrewAI crew for bootstrapping a fork from this template.

This crew follows the phases defined in `.agentic/CREW_BOOTSTRAP.md` and adds a
minimal CLI wrapper so you can launch it with a single command:

```bash
python scripts/bootstrapping_crew.py --project-name "Acme Widgets" \
  --template-repo org/agentic-project-template
```
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent

from crewai import Agent, Crew, Task


@dataclass
class BootstrapPaths:
    project_context: Path = Path(".agentic/PROJECT_CONTEXT.md")
    architecture: Path = Path("docs/ARCHITECTURE.md")
    design_overview: Path = Path("docs/DESIGN_OVERVIEW.md")
    setup_notes: Path = Path("docs/SETUP.md")


def build_agents() -> dict[str, Agent]:
    """Create the crew members with conservative defaults.

    The tool lists are intentionally empty so you can inject your preferred
    CrewAI tools (browser, file, GitHub) when wiring this into your runtime.
    """

    return {
        "engagement_lead": Agent(
            role="Engagement Lead",
            goal="Capture user intent, constraints, and delivery checkpoints",
            backstory="Seasoned facilitator who keeps scope realistic and documented",
            tools=[],
        ),
        "research_navigator": Agent(
            role="Research Navigator",
            goal="Validate requirements and surface platform limitations",
            backstory="Analyst who cross-references docs, repos, and public sources",
            tools=[],
        ),
        "repo_wrangler": Agent(
            role="Repo Wrangler",
            goal="Fork/clone repo and prepare branches using gh CLI conventions",
            backstory="DevOps-minded engineer comfortable with GitHub automation",
            tools=[],
        ),
        "systems_architect": Agent(
            role="Systems Architect",
            goal="Propose architecture, data contracts, and object relations",
            backstory="Architect who values MVP-first delivery and explicit tradeoffs",
            tools=[],
        ),
        "scaffolding_engineer": Agent(
            role="Scaffolding Engineer",
            goal="Lay down minimal code, dependency manifests, and docs",
            backstory="Builder focused on fast, clean scaffolds with tests and docs",
            tools=[],
        ),
        "issue_tracker": Agent(
            role="Issue Tracker",
            goal="Translate the roadmap into actionable GitHub issues",
            backstory="Project manager fluent with gh CLI and acceptance criteria",
            tools=[],
        ),
    }


def build_tasks(
    *,
    project_name: str,
    template_repo: str,
    bootstrap_branch: str,
    paths: BootstrapPaths,
    context_prompt: str | None,
) -> list[Task]:
    """Create CrewAI tasks wired to the crew's phases."""

    return [
        Task(
            description=dedent(
                f"""
                Interview the user to capture the initial context for the project
                named "{project_name}". Confirm goals, constraints, stack
                preferences, and documentation paths. Update or create
                `{paths.project_context}` with the answers and open questions.
                {context_prompt or ""}
                """
            ).strip(),
            expected_output="Updated project context note with decisions and open questions",
        ),
        Task(
            description=dedent(
                f"""
                Fork the template repository `{template_repo}` using the GitHub
                CLI (`gh repo fork {template_repo} --clone`) and create a working
                branch `{bootstrap_branch}`. Document remotes, branch defaults,
                and any auth prerequisites in `{paths.setup_notes}`.
                """
            ).strip(),
            expected_output="Forked repo cloned locally with remotes and branch documented",
        ),
        Task(
            description=dedent(
                f"""
                Review provided documentation and repository content to confirm
                requirements. Summarize confirmed needs, platform constraints, and
                unanswered questions in `{paths.design_overview}`.
                """
            ).strip(),
            expected_output="Design overview updated with confirmed requirements and gaps",
        ),
        Task(
            description=dedent(
                f"""
                Propose architecture and object relationships for the MVP. Cover
                data flow, API surfaces, persistence choices, and tradeoffs.
                Record the proposal in `{paths.architecture}`.
                """
            ).strip(),
            expected_output="Architecture document with object model and tradeoffs",
        ),
        Task(
            description=dedent(
                """
                Generate scaffolding: update dependency manifests, lay down
                placeholder modules/tests, and sync docs with the chosen structure.
                Note install/run commands in docs/SETUP.md.
                """
            ).strip(),
            expected_output="Code scaffold committed with updated manifests and setup notes",
        ),
        Task(
            description=dedent(
                """
                Create GitHub issues for the MVP roadmap using `gh issue create`.
                Group issues by area (architecture, backend, frontend, docs, infra)
                and link them via a tracking issue or milestone.
                """
            ).strip(),
            expected_output="Issue list created with clear acceptance criteria and labels",
        ),
    ]


def build_crew(
    *,
    project_name: str,
    template_repo: str,
    bootstrap_branch: str = "chore/bootstrap",
    context_prompt: str | None = None,
    paths: BootstrapPaths | None = None,
) -> Crew:
    paths = paths or BootstrapPaths()
    agents = build_agents()
    tasks = build_tasks(
        project_name=project_name,
        template_repo=template_repo,
        bootstrap_branch=bootstrap_branch,
        paths=paths,
        context_prompt=context_prompt,
    )

    return Crew(
        agents=list(agents.values()),
        tasks=tasks,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Launch the bootstrapping CrewAI crew.")
    parser.add_argument(
        "--project-name",
        required=True,
        help="Human-friendly project name used in context gathering tasks.",
    )
    parser.add_argument(
        "--template-repo",
        required=True,
        help="Template repository slug (e.g., org/agentic-project-template).",
    )
    parser.add_argument(
        "--bootstrap-branch",
        default="chore/bootstrap",
        help="Working branch name for the initial bootstrap commits.",
    )
    parser.add_argument(
        "--context-prompt",
        default=None,
        help="Optional extra instructions to append to the intake task.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    crew = build_crew(
        project_name=args.project_name,
        template_repo=args.template_repo,
        bootstrap_branch=args.bootstrap_branch,
        context_prompt=args.context_prompt,
    )
    crew.kickoff()


if __name__ == "__main__":
    main()

# Reference

Use this directory to store reusable materials that don't fit into formal specs or walkthroughs. It is the place for quick code snippets, API references, and notes about curated third-party data sources that support development work.

## What belongs here
- **Code snippets**: Small, well-scoped examples (queries, helper functions, config fragments) that accelerate common tasks. Each snippet should include a short description, prerequisites, and a copy/pasteable block.
- **API references**: Summaries of external contracts that your code calls, including auth requirements, rate limits, and example requests/responses. Link to upstream docs when possible and capture the minimum needed to unblock local development and testing.
- **Third-party data**: Provenance and usage notes for datasets, schemas, or seed files brought in from outside the repository. Document licensing, update cadence, and any transformation steps required before use.

## How to organize entries
- Create a dedicated Markdown file per topic (e.g., `api/stripe.md`, `snippets/logging.md`, `data/geojson-sources.md`). Subdirectories are encouraged for grouping related materials.
- Include a short frontmatter-style header with purpose, owners, and last verified date so future contributors know whether content is current.
- Prefer concise tables and bullet lists over long prose to keep content skimmable by humans and AI agents.

## Contribution workflow
1. Add or update files under `docs/reference/` when introducing new integrations or repeating patterns that benefit from reuse.
2. Cross-link relevant sections from `docs/API.md`, `docs/EXAMPLES.md`, or code comments so the reference material is discoverable.
3. Keep sensitive credentials out of this directory. Use placeholders and point to the appropriate secret management process defined in `SETUP.md` or `DEPLOYMENT.md`.
4. When retiring outdated entries, note their superseding source to avoid dead ends for future readers.

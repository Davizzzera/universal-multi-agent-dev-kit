# Web App Pack

> A preset for full-stack web applications, admin panels, SaaS dashboards, internal systems and product interfaces.

## Pack Overview
This pack curates the optimal configuration of agents, skills, and workflows to build and maintain modern web applications involving both frontend logic and backend services.

## When to use this pack
- React/Vite/Next-style apps
- Frontend + backend features
- Admin panels
- SaaS modules
- CRUD systems
- Authenticated dashboards

## When NOT to use this pack
- Static landing pages only
- Data-only reporting projects
- n8n-only automations

## Recommended Agents
This pack utilizes frontend and backend specialists alongside architectural planners to ensure safe cross-stack development. See `agents.md` for the full list.

## Recommended Skills
This pack relies on component creation, API contract design, and schema design skills. See `skills.md` for the full list.

## Recommended Workflows
This pack uses workflows that safely coordinate multi-agent tasks, such as `create-feature` and `coordinate`. See `workflows.md` for the full list.

## Validation Expectations
Strict frontend and backend unit tests must pass before delivery. Any UI changes should ideally be verified visually or via tests.

## Safety and Scope Notes
- Always restrict the frontend agent to the UI directory and the backend agent to the API directory.
- Database schema changes require high-risk validation.

## Example Use Cases
- "Build a new user settings page with a profile picture upload."
- "Implement a data table showing recent transactions, complete with a new REST endpoint."

## Related Packs
- `api-pack`
- `ecommerce-pack`

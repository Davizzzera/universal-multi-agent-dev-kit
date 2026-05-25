# API Pack

> A preset for backend APIs, REST endpoints, service layers, integrations, auth flows and webhook-based systems.

## Pack Overview
This pack curates the optimal configuration of agents, skills, and workflows to build robust, secure, and performant backend services without touching UI code.

## When to use this pack
- REST APIs
- Backend services
- Webhooks
- Auth systems
- External API integrations
- Backend refactors

## When NOT to use this pack
- Pure UI work
- Landing pages with no backend
- BI-only projects

## Recommended Agents
This pack utilizes backend developers, database engineers, and security reviewers. See `agents.md` for the full list.

## Recommended Skills
This pack relies heavily on contract design, request validation, and access control. See `skills.md` for the full list.

## Recommended Workflows
This pack uses workflows tailored to backend safety, such as `api-development`, `database-change`, and `security-review`. See `workflows.md` for the full list.

## Validation Expectations
Integration tests and unit tests must pass. Any new endpoints must be validated against their schema (e.g., OpenAPI). Security reviews are mandatory for auth changes.

## Safety and Scope Notes
- Ensure the `scope-guardian` restricts edits to backend logic and database folders.
- Database changes should be handled via proper migration scripts.

## Example Use Cases
- "Add a new GET /api/v1/users endpoint with pagination."
- "Implement a webhook receiver for Stripe payments."

## Related Packs
- `web-app-pack`
- `ecommerce-pack`

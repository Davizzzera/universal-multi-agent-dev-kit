# API Pack: Usage

## How to use this pack
1. Determine the backend feature you need to build.
2. Select this pack in your prompt to inform the Orchestrator.
3. Select a primary workflow (e.g., `api-development`).
4. Specify your database and security constraints.

## Recommended Prompt Structure
- **Context:** Brief intro to the backend architecture.
- **Goal:** Endpoint description.
- **Pack:** `api-pack`.
- **Workflow:** The chosen workflow.
- **Scope:** Which backend folders are allowed (e.g., `src/controllers/`, `src/routes/`).
- **Validation:** Integration tests required.

## Step-by-Step Usage
1. Ask the AI to `plan` the API contract.
2. Review the proposed request/response schema.
3. Instruct the AI to build the endpoint (`api-development`).
4. Ask the AI to run a `security-review`.
5. Run validation (`verify`).

## How to use with Antigravity
Include the pack reference in your initial prompt. Antigravity will map this pack to its internal context and pre-load the necessary agent personas (Backend Specialist, API Designer, Security Reviewer).

## How to validate
For an API pack, validation usually means:
- Unit tests for logic.
- Integration tests for endpoints.
- Database migration dry-runs.
- Linter checks.

## Common Mistakes
- Modifying endpoints without updating Swagger/OpenAPI documentation.
- Skipping input validation.
- Missing authorization checks on new endpoints.

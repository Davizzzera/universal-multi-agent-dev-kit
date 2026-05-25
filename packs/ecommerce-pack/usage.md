# Ecommerce Pack: Usage

## How to use this pack
1. Determine the scope of your commerce task.
2. Select this pack in your prompt to inform the Orchestrator.
3. Select a primary workflow (e.g., `create-feature` or `coordinate`).
4. Specify your required backend and frontend validations.

## Recommended Prompt Structure
- **Context:** Brief intro to the commerce architecture.
- **Goal:** Feature description.
- **Pack:** `ecommerce-pack`.
- **Workflow:** The chosen workflow.
- **Scope:** Which folders are allowed (e.g., `src/client/`, `src/api/`).
- **Validation:** What tests to run.

## Step-by-Step Usage
1. Ask the AI to `plan` the feature using this pack.
2. Review the API contract proposed by the AI.
3. Instruct the AI to build the backend (`api-development`).
4. Instruct the AI to build the frontend (`frontend-ui`).
5. Run full stack validation.

## How to use with Antigravity
Include the pack reference in your initial prompt. Antigravity will map this pack to its internal context and pre-load the necessary agent personas (Frontend Specialist, Backend Specialist, Security Reviewer, etc.).

## How to validate
For an Ecommerce pack, validation usually means:
- `npm run lint`
- `npm run test` (Frontend)
- `npm run test:api` (Backend)
- Output of these commands must be shown in the chat.

## Common Mistakes
- Trusting frontend pricing calculations on the backend.
- Not handling out-of-stock scenarios in the UI.
- Skipping security reviews for payment-related code.

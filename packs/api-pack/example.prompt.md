# API Pack: Example Prompt

**Copy and paste the following into Antigravity:**

```text
Goal: Create a new POST /api/v1/orders endpoint.
Pack: `api-pack`
Workflow: `api-development`

Scope: `src/routes/`, `src/controllers/`, `src/services/` and `tests/api/`.
Instructions:
1. Use the API Designer to define the JSON request payload schema.
2. Use the Backend Specialist to implement the endpoint, ensuring Zod is used for validation.
3. Use the Security Reviewer to ensure the endpoint checks the user's JWT token.
4. Use the QA Tester to write an integration test.
Validation: Run `npm run test:api` and provide the output showing the new test passes.
Commit: Do not commit until I review the validation output.

Language Rule: Answer me in Brazilian Portuguese, but write repository files in English.
```

# API Development Prompt

**Purpose:** Use this prompt when requesting backend API modifications, endpoints, or data services.

---

**Copy and paste the following into Antigravity:**

```text
Goal: [INSERT YOUR GOAL HERE, e.g., Add a new GET /api/v1/users endpoint with pagination]
Workflow: `api-development`

Scope: Only backend source code and related tests (`src/api/`, `src/services/`, `tests/api/`).
Constraints:
1. Ensure the `backend-specialist` agent handles the implementation.
2. Follow existing API design patterns and error handling structures.
3. Validate inputs safely.
Validation: Write an API integration test. Run the test suite and provide the output as evidence.
Commit: If successful, commit with "feat(api): [short description]" and push.

Language Rule: Answer me in Brazilian Portuguese, but write repository files in English.
```

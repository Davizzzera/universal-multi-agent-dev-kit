# Frontend UI Prompt

**Purpose:** Use this prompt when requesting frontend UI modifications, styling, or component updates.

---

**Copy and paste the following into Antigravity:**

```text
Goal: [INSERT YOUR GOAL HERE, e.g., Update the navigation bar to use the new brand colors and add a mobile menu]
Workflow: `frontend-ui`

Scope: Only frontend source code (`src/components/`, `src/styles/`).
Constraints:
1. Ensure the `frontend-specialist` agent handles the implementation.
2. Follow existing styling conventions (e.g., Tailwind classes or CSS Modules as currently used).
3. Ensure responsiveness.
Validation: Describe how the UI was tested (e.g., run `npm run lint` and `npm test` for frontend).
Commit: If successful, commit with "feat(ui): [short description]" and push.

Language Rule: Answer me in Brazilian Portuguese, but write repository files in English.
```

# Create Feature Prompt

**Purpose:** Use this prompt to instruct Antigravity to build a new, isolated feature.

---

**Copy and paste the following into Antigravity:**

```text
Goal: [INSERT YOUR GOAL HERE, e.g., Create a user profile component]
Workflow: `create-feature`

Scope: [INSERT SCOPE, e.g., `src/components/UserProfile/`]
Constraints:
1. Ensure the Scope Guardian prevents edits outside the targeted directory.
2. Follow standard coding conventions for this project.
3. Only use the required specialist agents for this domain.
Validation: Write and run unit tests for the new feature. Show me the successful output.
Commit: Do not commit until I approve the validation evidence.

Language Rule: Answer me in Brazilian Portuguese, but write repository files in English.
```

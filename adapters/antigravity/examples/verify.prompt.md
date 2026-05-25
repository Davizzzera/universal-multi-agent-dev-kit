# Verify Prompt

**Purpose:** Use this prompt to run validation checks across the project without making any implementation changes.

---

**Copy and paste the following into Antigravity:**

```text
Goal: Verify the health and integrity of the current project state.
Workflow: `verify`

Scope: Entire project.
Constraints:
1. Do NOT modify any source code files.
2. Run linters, type checkers, and test suites.
3. If this is the kit repository itself, run the Python verification scripts (`python .agent/scripts/verify_all.py` or equivalent).
Validation: Provide the exact output of the terminal commands as evidence. Do not summarize the output to the point of hiding errors.
Commit: Do not commit.

Language Rule: Answer me in Brazilian Portuguese, but write any validation reports in English.
```

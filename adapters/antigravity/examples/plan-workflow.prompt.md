# Plan Workflow Prompt

**Purpose:** Use this prompt when you want Antigravity to analyze a problem and create a plan *without* modifying any source code yet.

---

**Copy and paste the following into Antigravity:**

```text
Goal: [INSERT YOUR GOAL HERE, e.g., Plan the architecture for the new payment gateway]
Workflow: `plan`

Scope: Entire project for reading, but NO files may be modified other than creating a planning artifact.
Constraints: 
1. Use the Universal Orchestrator to route the planning request to the appropriate specialist agents.
2. Read the relevant context.
3. Output the plan in a temporary Markdown file (or as a standard plan artifact) containing proposed steps and risk assessment.
4. Stop and wait for my approval before executing any code changes.

Language Rule: Answer me in Brazilian Portuguese, but write repository files/plans in English.
```

# Antigravity Adapter Quick Start

Get up and running with the Universal Multi-Agent Development Kit inside Antigravity AI.

## 1. Get the Kit
```bash
git clone https://github.com/Davizzzera/universal-multi-agent-dev-kit.git
```

## 2. Copy to Project
Copy the `.agent` folder into the root of your target project.

## 3. Add Antigravity Entrypoint
Ensure the contents of `adapters/antigravity/AGENTS.md` are provided to Antigravity as its primary context/instruction set for the project.

## 4. First Test After Installation

Once the kit is installed as the default operating mode (with the root `AGENTS.md`), you can send a natural request without naming any agents.

Copy and paste this exact prompt into Antigravity to verify the Auto-Orchestration is working:

```text
Review the existing header component and improve only spacing and visual consistency if needed.
```

**What to expect in the response:**
- **Automatic Routing**: The Task Router should select the correct workflow and agents (e.g., UI/UX Designer, Frontend Specialist).
- **Orchestration Plan**: An explanation of what will be done before making changes.
- **Inline Execution Trace**: A block at the end detailing exactly what happened.
- **Registry Paths**: The trace must include exact paths to the agents and skills used.
- **Validation Evidence**: Proof that the UI wasn't broken by the changes.

## 5. Send Specific Prompts

If you want to be more explicit, you can use these prompts to get started safely.

### Option A: Safe Planning (Read-Only)
```text
Goal: Create a new user profile page.
Workflow: Use the `plan` workflow.
Constraint: Do NOT modify any project files. Just read the context and create an implementation plan in a temporary Markdown file.
Validation: None required yet.
```

### Option B: Feature Implementation
```text
Goal: Create a new user profile page in the frontend folder.
Workflow: Use the `create-feature` workflow.
Scope: Only touch the `/frontend` directory.
Constraint: Follow the `react-component-create` skill.
Validation: Run `npm test` when finished to ensure nothing is broken.
```

### Option C: Verification
```text
Goal: Verify that the project builds and all tests pass.
Workflow: Use the `verify` workflow.
Constraint: Act as the Final Reviewer and QA Tester.
Validation: Provide the exact output of the build and test commands as proof.
```

## 5. Validate Output
Always review Antigravity's summary, files changed, and validation evidence before accepting the work.

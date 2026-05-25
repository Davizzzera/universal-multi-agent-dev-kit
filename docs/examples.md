# Examples

> Conceptual usage examples for the Universal Multi-Agent Development Kit.

---

## Example 1: Implementing a New Feature

### Scenario

A developer asks: _"Add a user authentication module with login and registration endpoints."_

### How the Kit Handles This

```
1. USER REQUEST
   "Add a user authentication module with login and registration endpoints."

2. UNIVERSAL ORCHESTRATOR
   Parses intent: New feature implementation.
   Identifies scope: Authentication module, API endpoints.
   Sets constraints: Security-sensitive, requires validation.

3. CONTEXT READER (Parallel)
   Reads project structure.
   Identifies existing auth patterns.
   Maps dependencies (existing user model, database config).

4. TASK ROUTER (Parallel)
   Classifies task: Feature Implementation.
   Selects workflow: feature-implementation.
   Identifies complexity: Medium.

5. AGENT SELECTION
   Selected agents:
   - Code Writer (implementation)
   - Security Agent (security review)
   - Test Agent (test creation)
   - Documentation Agent (docs update)

6. PARALLEL RESEARCH PHASE
   Code Writer: Analyzes existing patterns, plans implementation.
   Security Agent: Reviews auth best practices for the stack.
   Test Agent: Plans test cases.
   Documentation Agent: Plans documentation updates.

7. SEQUENTIAL IMPLEMENTATION PHASE
   Step 1: Code Writer creates auth module files.
   Step 2: Code Writer creates API endpoint files.
   Step 3: Test Agent creates test files.
   Step 4: Documentation Agent updates API docs.

8. PARALLEL VALIDATION PHASE
   QA Agent: Verifies endpoints work correctly.
   Security Agent: Checks for vulnerabilities (SQL injection, XSS, etc.).
   Style Agent: Checks code formatting.
   Structure Agent: Verifies file placement.

9. FINAL REVIEWER
   Confirms all checks passed.
   Creates delivery summary.

10. DELIVERY
    All files created, validated, and ready.
```

---

## Example 2: Fixing a Bug

### Scenario

A developer asks: _"Fix the broken date formatting in the user profile page."_

### How the Kit Handles This

```
1. USER REQUEST
   "Fix the broken date formatting in the user profile page."

2. UNIVERSAL ORCHESTRATOR
   Parses intent: Bug fix.
   Identifies scope: User profile page, date formatting.

3. CONTEXT READER
   Locates the user profile page files.
   Identifies date formatting code.
   Maps related components.

4. TASK ROUTER
   Classifies task: Bug Fix.
   Selects workflow: bug-fix.

5. AGENT SELECTION
   Selected agents:
   - Code Writer (fix implementation)
   - QA Agent (verification)

6. PARALLEL RESEARCH PHASE
   Code Writer: Analyzes the bug, identifies root cause.
   QA Agent: Understands expected behavior.

7. SEQUENTIAL IMPLEMENTATION PHASE
   Step 1: Code Writer fixes the date formatting.

8. PARALLEL VALIDATION PHASE
   QA Agent: Verifies the fix works.
   Style Agent: Checks formatting.

9. FINAL REVIEWER
   Confirms the fix is complete.

10. DELIVERY
    Bug fixed and validated.
```

---

## Example 3: Repository Validation

### Scenario

A developer asks: _"Validate the repository structure and check for any issues."_

### How the Kit Handles This

```
1. USER REQUEST
   "Validate the repository structure and check for any issues."

2. UNIVERSAL ORCHESTRATOR
   Parses intent: Validation.
   Selects workflow: full-validation.

3. PARALLEL VALIDATION PHASE
   Structure Agent: Checks folder structure.
   Security Agent: Scans for secrets.
   Style Agent: Checks formatting.
   QA Agent: Verifies documentation.

4. FINAL REVIEWER
   Consolidates all validation results.
   Reports issues found.

5. DELIVERY
   Validation report delivered.
```

---

## Example 4: Choosing a Project Pack

### Scenario

A developer asks: _"I'm starting a new e-commerce project. Which pack should I use?"_

### How the Kit Handles This

```
1. USER REQUEST
   "I'm starting a new e-commerce project."

2. UNIVERSAL ORCHESTRATOR
   Parses intent: New project configuration.
   Identifies domain: Ecommerce.

3. TASK ROUTER
   Recommends pack: ecommerce-pack.
   Loads pack-manifest.json from packs/ecommerce-pack/.

4. AGENT SELECTION (From Pack)
   Primary: product-manager, frontend-specialist, backend-specialist,
            database-specialist, security-reviewer, qa-tester.

5. WORKFLOW SELECTION (From Pack)
   Recommended: plan → coordinate → create-feature → verify.

6. DELIVERY
   Orchestrator confirms the pack selection and asks the user
   for the first goal to execute.
```

---

## Example 5: Using web-app-pack

### Prompt

```text
Goal: Create a new user settings page with a profile picture upload.
Pack: web-app-pack
Workflow: coordinate

Scope: src/components/ and src/api/
Validation: Run npm test.
Language Rule: Answer me in Brazilian Portuguese, but write repository files in English.
```

---

## Example 6: Using landing-page-pack

### Prompt

```text
Goal: Create a new landing page for our upcoming Black Friday sale.
Pack: landing-page-pack
Workflow: plan

Scope: Only the public frontend directory.
Validation: None required yet. Output the copy and structure for review.
Language Rule: Answer me in Brazilian Portuguese, but write repository files in English.
```

---

## Example 7: Using automation-pack

### Prompt

```text
Goal: Create a Python script that polls an API every 5 minutes and saves new records to a CSV.
Pack: automation-pack
Workflow: automation

Scope: scripts/
Validation: Provide the code for my review, do not run it directly.
Language Rule: Answer me in Brazilian Portuguese, but write repository files in English.
```

---

## Example 8: Using enterprise-pack

### Prompt

```text
Goal: Refactor the authentication module to support SSO across all microservices.
Pack: enterprise-pack
Workflow: plan

Scope: services/auth/, services/gateway/, shared/auth-sdk/.
Validation: Output an implementation plan, rollback plan, and TDR. Do NOT modify source code.
Language Rule: Answer me in Brazilian Portuguese, but write repository files in English.
```

---

## Key Takeaways

1. **The orchestrator never does the work itself.** It always delegates to specialist agents.
2. **Research and analysis are parallel.** This makes execution faster.
3. **Writing is sequential.** This prevents file conflicts.
4. **Validation is always the last step.** Nothing is delivered without validation.
5. **The workflow determines the execution plan.** Different task types use different workflows.
6. **Project Packs accelerate agent selection.** They provide domain-specific presets for common project types.

---

## Current Status

> **v0.1.0 (Unreleased):** Agents, skills, workflows, adapters, and project packs are implemented. These examples are now executable scenarios.

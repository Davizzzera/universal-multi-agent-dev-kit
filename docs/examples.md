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

## Key Takeaways

1. **The orchestrator never does the work itself.** It always delegates to specialist agents.
2. **Research and analysis are parallel.** This makes execution faster.
3. **Writing is sequential.** This prevents file conflicts.
4. **Validation is always the last step.** Nothing is delivered without validation.
5. **The workflow determines the execution plan.** Different task types use different workflows.

---

## Current Status

> **Foundation Phase (v0.1.0):** These are conceptual examples. When agents, skills, and workflows are implemented in later phases, these examples will become executable scenarios.

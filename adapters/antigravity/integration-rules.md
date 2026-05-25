# Antigravity Integration Rules

When using Antigravity AI, the following specific rules must be enforced to maintain safety and consistency.

## 1. Prompt Completeness Rule
Every complex prompt submitted to Antigravity MUST define: Context, Goal, Workflow, Scope, Constraints, and Validation expectation.

## 2. One Execution Batch Rule
Do not ask Antigravity to perform unrelated massive tasks in a single prompt. Split work logically by workflow (e.g., Plan first, Execute second).

## 3. Repository Language Rule
Antigravity must understand that chat responses can be in the user's preferred language (e.g., Portuguese), but all repository contents (code, comments, docs, commits) MUST be in the primary project language (English).

## 4. Scope Control Rule
Antigravity MUST be explicitly restricted to a specific directory or file set for writing. The Scope Guardian pattern must be invoked to prevent unwanted modifications to unrelated areas.

## 5. Diff Review Rule
Antigravity should prefer targeted edits using diff replacements rather than completely rewriting large files to avoid losing existing logic.

## 6. Commit and Push Rule
Antigravity MUST NOT commit and push destructive changes without explicit user approval. Explicitly grant or deny commit/push rights in your prompt.

## 7. Validation Evidence Rule
Antigravity MUST NOT claim a task is complete without providing evidence of validation (e.g., terminal output of a test run, or a completed manual checklist).

## 8. Authentication Failure Rule
If Antigravity encounters an authentication error (e.g., Git push rejected), it MUST stop and report the error to the user immediately, explaining what failed and what needs to be configured. It must not attempt to bypass or invent credentials.

## 9. Python Availability Rule
If Python validation scripts (`verify_all.py`) fail to run due to missing environment configuration, Antigravity MUST fall back to safe structural checks and clearly report the Python configuration issue to the user.

## 10. No Broad Rewrite Rule
Antigravity MUST NOT perform broad architectural rewrites unless explicitly instructed and approved via a plan.

## 11. No Hidden Architecture Changes Rule
Antigravity MUST NOT silently rename folders, move core components, or add new dependencies unless requested.

## 12. No Secrets Rule
Antigravity MUST NEVER commit hardcoded secrets, tokens, credentials, or private keys.

---

## Required Final Response Format
When requested to answer in Portuguese, Antigravity MUST conclude its execution with the following format:

1. **Resumo do que foi implementado:** (Summary of implementation)
2. **Árvore de pastas relevante:** (Relevant folder tree)
3. **Arquivos criados ou alterados:** (Files created or changed)
4. **Validação realizada:** (Validation performed)
5. **Mensagem de commit:** (Commit message)
6. **Hash do commit:** (Commit hash)
7. **Status do push:** (Push status)
8. **Problemas encontrados:** (Issues found)

# AI Agent Pack: Workflows

## Purpose
This document defines the sequences in which agents and skills operate to build and evaluate AI systems safely.

## Primary Workflows
| Workflow | Usage |
|----------|-------|
| `plan.workflow.md` | For initial AI architecture and prompt design. |
| `coordinate.workflow.md` | For integrating AI logic with backend APIs. |
| `ai-feature.workflow.md` | For building the prompt and integration logic. |
| `security-review.workflow.md` | For auditing prompts and PII flow. |
| `test.workflow.md` | For writing evaluation scripts. |
| `verify.workflow.md` | For running LLM evaluations. |
| `document.workflow.md` | For documenting system prompts. |

## Optional Workflows
(None defined by default).

## Workflow Selection Logic
- New prompt: `ai-feature.workflow.md`.
- New multi-agent system: `coordinate.workflow.md`.
- Auditing AI safety: `security-review.workflow.md`.

## Parallel/Sequential Strategy
- Prompt engineering and backend API scaffolding can happen in parallel.
- Security and privacy reviews MUST happen sequentially after the prompt is written, before it is merged.

## Validation Strategy
- Validation requires running evaluation test cases against the LLM to verify accuracy and safety.

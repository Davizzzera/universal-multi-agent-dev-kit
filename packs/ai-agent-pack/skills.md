# AI Agent Pack: Skills

## Purpose
This document defines the core procedures and techniques required to design and evaluate AI features.

## Core Skills
| Skill | Usage |
|-------|-------|
| `prompt-architecture` | Designing context/instructions |
| `agent-definition` | Specifying agent roles |
| `subagent-definition` | Specifying delegated tasks |
| `multi-agent-orchestration` | Designing handoffs |
| `rag-pipeline-design` | Chunking and vector search |
| `llm-output-evaluation` | Testing AI accuracy |
| `project-intake` | Gathering requirements |
| `task-breakdown` | Planning AI features |
| `acceptance-criteria-writing` | Defining AI success |
| `privacy-review-guidance` | Checking for PII |
| `security-release-checklist` | Checking for prompt injection |
| `documentation-review` | Ensuring AI docs are clear |

## Optional Skills
(None defined by default).

## Skill Loading Logic
- Planning phase: Load `agent-definition`, `prompt-architecture`, `project-intake`.
- Implementation phase: Load `rag-pipeline-design`, `multi-agent-orchestration`.
- Evaluation phase: Load `llm-output-evaluation`, `privacy-review-guidance`, `security-release-checklist`.

## Progressive Loading Notes
Only load `rag-pipeline-design` if the AI feature requires searching a knowledge base.

## Validation Notes
`llm-output-evaluation` and `privacy-review-guidance` are strictly required before shipping AI features to production.

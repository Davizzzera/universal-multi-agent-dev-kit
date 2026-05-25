# AI Agent Pack: Agents

## Purpose
This document defines the agent ensemble required to safely design, build, and evaluate AI systems and prompt architectures.

## Primary Agents
| Agent | Role in this Pack |
|-------|-------------------|
| `universal-orchestrator` | Overall request handling |
| `project-context-reader` | Discovers architecture boundaries |
| `task-router` | Selects workflows |
| `scope-guardian` | Enforces AI logic boundaries |
| `conflict-controller` | Manages file locks |
| `final-reviewer` | Signs off on delivery |
| `ai-engineer` | Integrates LLMs into code |
| `prompt-engineer` | Designs prompts and personas |
| `agent-engineer` | Designs autonomous workflows |
| `rag-specialist` | Implements vector search |
| `qa-tester` | Writes evaluations |
| `security-reviewer` | Audits prompt injection |
| `privacy-compliance-reviewer` | Checks PII handling |
| `documentation-writer` | Documents AI features |

## Optional Agents
| Agent | Role in this Pack |
|-------|-------------------|
| `backend-specialist` | For building the API wrappers |
| `api-designer` | For defining tool schemas |
| `data-quality-specialist` | For cleaning fine-tuning data |
| `technical-writer` | For internal AI docs |

## Agent Selection Logic
- For prompts only: `prompt-engineer` + `qa-tester`.
- For RAG: `rag-specialist` + `ai-engineer`.
- For new multi-agent systems: `agent-engineer` + `security-reviewer`.

## Handoff Notes
The `prompt-engineer` must define the expected input/output format before the `ai-engineer` implements the API call.

## Boundary Notes
These agents MUST NOT touch frontend UI components unless they are specifically building a chatbot UI (in which case a `frontend-specialist` must be pulled in).

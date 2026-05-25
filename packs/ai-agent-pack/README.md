# AI Agent Pack

> A preset for AI features, prompt systems, agent architectures, RAG pipelines, LLM evaluation and multi-agent workflows.

## Pack Overview
This pack curates the optimal configuration of agents, skills, and workflows to design, build, and evaluate systems that rely on Large Language Models and AI orchestration.

## When to use this pack
- AI assistants
- Prompt engineering
- Multi-agent systems
- RAG systems
- LLM output evaluation
- AI workflow design
- Agent-based automation

## When NOT to use this pack
- Simple static pages
- Traditional CRUD with no AI
- Pure BI dashboard requirements

## Recommended Agents
This pack utilizes AI engineers, prompt engineers, and privacy reviewers. See `agents.md` for the full list.

## Recommended Skills
This pack relies heavily on prompt architecture, RAG design, and LLM evaluation. See `skills.md` for the full list.

## Recommended Workflows
This pack uses workflows tailored to AI development, such as `ai-feature` and `security-review`. See `workflows.md` for the full list.

## Validation Expectations
LLM output must be evaluated for hallucinations, toxicity, and correctness. Privacy reviews must confirm no PII is leaked to external APIs.

## Safety and Scope Notes
- Strict prohibition against sending PII (Personally Identifiable Information) to external LLM APIs without explicit consent and compliance checks.
- Ensure the `privacy-compliance-reviewer` is engaged before merging AI features.

## Example Use Cases
- "Design a RAG pipeline to answer customer queries based on our internal docs."
- "Write the system prompts for a new set of specialized sub-agents."

## Related Packs
- `api-pack`
- `web-app-pack`

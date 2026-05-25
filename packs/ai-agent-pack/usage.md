# AI Agent Pack: Usage

## How to use this pack
1. Determine the scope of the AI feature.
2. Select this pack in your prompt to inform the Orchestrator.
3. Select a primary workflow (e.g., `ai-feature`).
4. Specify your prompt guidelines and privacy rules.

## Recommended Prompt Structure
- **Context:** Brief intro to what the AI should do.
- **Goal:** Description of the prompt or agent behavior.
- **Pack:** `ai-agent-pack`.
- **Workflow:** The chosen workflow.
- **Scope:** Which folders are allowed (e.g., `src/prompts/`, `src/services/ai/`).
- **Validation:** What LLM evaluation tests to run.

## Step-by-Step Usage
1. Ask the AI to `plan` the prompt structure and context payload.
2. Review the proposed design for privacy issues.
3. Instruct the AI to build the feature (`ai-feature`).
4. Ask the AI to run a `security-review`.
5. Run an LLM evaluation (`verify`).

## How to use with Antigravity
Include the pack reference in your initial prompt. Antigravity will map this pack to its internal context and pre-load the necessary agent personas (Prompt Engineer, AI Engineer, Privacy Compliance Reviewer).

## How to validate
For an AI Agent pack, validation usually means:
- Running specific test cases where the output is judged by another LLM or via exact string matching.
- Reviewing the context payload to ensure no PII is accidentally included.

## Common Mistakes
- Writing prompts that are vulnerable to simple injection attacks.
- Including raw database records in the LLM context without stripping user emails/passwords.
- Skipping systematic evaluation in favor of "it looked good once".

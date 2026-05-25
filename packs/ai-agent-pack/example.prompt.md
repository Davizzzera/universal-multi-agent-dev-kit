# AI Agent Pack: Example Prompt

**Copy and paste the following into Antigravity:**

```text
Goal: Create a system prompt and integration code for a customer support chatbot.
Pack: `ai-agent-pack`
Workflow: `ai-feature`

Scope: `src/prompts/` and `src/services/ai/`.
Instructions:
1. Use the Prompt Engineer to draft the system prompt. Instruct the AI to be polite and concise.
2. Use the AI Engineer to implement the API call to OpenAI using the drafted prompt.
3. Use the Privacy Compliance Reviewer to ensure the user's email is stripped before sending the context to OpenAI.
4. Use the QA Tester to write an evaluation script.
Validation: Run the evaluation script and provide the output.
Commit: Do not commit until I review the prompt and validation output.

Language Rule: Answer me in Brazilian Portuguese, but write repository files in English.
```

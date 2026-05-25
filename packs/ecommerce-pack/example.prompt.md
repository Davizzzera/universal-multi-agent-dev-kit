# Ecommerce Pack: Example Prompt

**Copy and paste the following into Antigravity:**

```text
Goal: Implement a new "Add to Cart" button logic for the product detail page.
Pack: `ecommerce-pack`
Workflow: `coordinate`

Scope: `src/components/Product/` and `src/api/cart/`.
Instructions:
1. Use the Backend Specialist to create the API endpoint to handle adding items to the cart, ensuring it verifies stock availability.
2. Use the Frontend Specialist to create the React component and handle loading/error states.
3. Use the Security Reviewer to audit the endpoint and ensure pricing cannot be manipulated by the client request.
4. Use the QA Tester to write tests for both.
Validation: Run `npm run test` and provide the output showing all tests pass.
Commit: Do not commit until I review the validation output.

Language Rule: Answer me in Brazilian Portuguese, but write repository files in English.
```

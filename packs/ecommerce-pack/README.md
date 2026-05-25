# Ecommerce Pack

> A preset for product catalogs, checkout-related flows, inventory/admin interfaces, product pages and commerce-oriented systems.

## Pack Overview
This pack curates the optimal configuration of agents, skills, and workflows to build high-performance product pages and secure commerce workflows, combining the aesthetics of landing pages with the rigor of data-heavy backend systems.

## When to use this pack
- Product catalogs
- Admin product panels
- Product detail pages
- Inventory workflows
- Commerce landing pages
- Lead-based sales catalogs
- Checkout-adjacent flows

## When NOT to use this pack
- Payment implementation without strict security review
- Highly regulated financial systems without additional compliance review
- BI-only projects

## Recommended Agents
This pack utilizes frontend and backend specialists, alongside product managers, copywriters, and security reviewers. See `agents.md` for the full list.

## Recommended Skills
This pack relies on database design, conversion audits, and loading/empty state management. See `skills.md` for the full list.

## Recommended Workflows
This pack uses workflows tailored to full-stack feature creation, such as `create-feature` and `coordinate`. See `workflows.md` for the full list.

## Validation Expectations
Both backend integration tests (for inventory/cart states) and frontend conversion/layout audits (for product pages) are required.

## Safety and Scope Notes
- Any logic touching pricing, discounts, or payments MUST undergo a `security-review`.
- Ensure the `scope-guardian` is active to prevent accidental exposure of admin routes.

## Example Use Cases
- "Implement a new product detail page with image carousels and 'add to cart' logic."
- "Build the admin dashboard interface for updating product inventory levels."

## Related Packs
- `web-app-pack`
- `landing-page-pack`

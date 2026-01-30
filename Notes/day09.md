# Day 09 — GraphQL Security: Authorization Integrity & Resource Management

## 1. Assessment of Object-Level Authorization
- *Actions:* Conducted a security review of GraphQL resolver logic by mutating unique identifiers within the schema.
- *Actions:* Tested data-siloing enforcement between different user accounts.
- *Outcome:* Identified critical authorization failures enabling unauthorized cross-tenant data access.

---

## 2. Granular Data Exposure Audit
- *Actions:* Targeted field-level authorization to detect unauthorized access to privileged metadata.
- *Actions:* Verified whether the backend properly redacts sensitive fields based on requester context.
- *Outcome:* Confirmed missing controls preventing retrieval of administrative attributes by unauthorized users.

---

## 3. Query Complexity & Availability Analysis
- *Actions:* Evaluated API resilience against complex, resource-intensive GraphQL queries.
- *Actions:* Checked for query-cost analysis and depth-limiting middleware implementation.
- *Outcome:* Found vulnerability to Resource Exhaustion Attacks due to unconstrained query nesting.

---

## Summary
- *Actions:* Performed comprehensive authorization and availability audit of GraphQL implementation.
- *Outcome:* Recommended object-level checks and query-cost limiting to address data exposure and DoS risks.

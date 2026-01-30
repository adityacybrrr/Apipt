# Day 10 — Practical GraphQL Abuse: Batching & Aliasing

## 1. Batching & Rate Limit Bypass
- *Actions:* Combined multiple queries into one HTTP request to test existing rate limiting effectiveness.
- *Actions:* Observed how the server processed bulk operations under a single transaction.
- *Outcome:* Confirmed vulnerability to Unrestricted Resource Consumption through query batching.

---

## 2. Alias-Based Mass Extraction
- *Actions:* Used GraphQL aliases to rename fields and bypass duplicate field restrictions in a single query.
- *Actions:* Tested whether the server could detect and block "heavy" requests with many aliases.
- *Outcome:* Successfully performed mass data retrieval while evading traditional security filters.

---

## 3. Query Depth & DoS Probing
- *Actions:* Built deeply nested queries to test API depth-limit enforcement.
- *Actions:* Monitored backend latency as query complexity increased.
- *Outcome:* Identified critical lack of query complexity validation and enabling potential Resource Exhaustion attacks.

---

## Summary
- *Actions:* Tested advanced GraphQL features using Burp Repeater to uncover stealthy attack vectors.
- *Outcome:* Developed methodology for finding vulnerabilities that bypass REST-focused security controls.

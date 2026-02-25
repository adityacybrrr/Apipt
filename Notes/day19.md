# Day 19 — BOLA Summary: Resource Isolation Failure

## 1. Key Concepts
- *Actions:* Defined BOLA (API1) as valid user + wrong object (e.g., GET /invoice/others_id). Distinguished BOLA = Resource IDs from BFLA = Action Endpoints.
- *Outcome:* Critical Fact: Authentication ≠ Authorization. Valid tokens don't grant ownership.

---

## 2. Testing Logic
- *Actions:* Swap your ID for another user's ID in Burp Repeater. Change only the identifier; keep token and headers the same.
- *Outcome:* Success Criteria: Receiving 200 OK with data you don't own.

---

## 3. Risk & Mitigation
- *Actions:* Watch for patterns like UUIDs, emails, and GraphQL queries. Identified OAuth Trap where APIs ignore sub claim in favor of URL ID.
- *Outcome:* Fix: Enforce resource-level authorization checks at the database query level.

---

## Summary
- *Actions:* Confirmed BOLA as #1 API threat due to gap between valid login and missing ownership check.

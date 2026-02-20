# Day 17 — Practical BFLA: Testing Administrative Functionality

## 1. BFLA vs. BOLA: Operational Differences
- *Actions:* BOLA (API1): Unauthorized access to data objects (e.g., /users/123). BFLA (API5): Unauthorized access to functional logic (e.g., /admin/users).
- *Outcome:* Isolated the testing focus to "actions" rather than "IDs."

---

## 2. Vulnerability Vectors in Modern APIs
- *Actions:* Identified why APIs fail: Exposed endpoints, shared backend services, and over-reliance on frontend role enforcement.
- *Outcome:* Critical Rule: OAuth handles authentication (Identity); the API must independently handle authorization (Permission).

---

## 3. Execution: Burp Repeater Workflow
- *Actions:* 
  - Captured a valid low-privilege access token.
  - Identified "High-Risk" endpoints: /manage/*, /delete, /create, /settings.
  - Replayed the token against these endpoints in Repeater.
- *Outcome:* Observed response signals: 403 (Secure) vs. 200/204 (Vulnerable).

---

## 4. Remediation & Mapping
- *Actions:* Mapping: Primarily API5 (Broken Function Level Authorization). Remediation: Implement server-side RBAC, validate claims/scopes, and logically separate administrative APIs.
- *Outcome:* Applied a structured replay methodology to verify backend role enforcement, proving that valid tokens often lack granular functional restrictions.

---

## Summary
- *Actions:* Proved that valid tokens often lack granular functional restrictions through structured replay testing.

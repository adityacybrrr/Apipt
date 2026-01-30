# Day 05 — API Authentication & Broken Auth Analysis

## 1. The Authentication Mental Model
- *Actions:* Evaluated multiple authentication schemes including API keys, Bearer tokens (JWT), and Basic Auth.
- *Actions:* Analyzed where auth data is placed across headers, cookies, and query parameters.
- *Outcome:* Gained a clear view of the identity layer and why insecure placement (such as query parameters) can cause credential leakage.

---

## 2. Enforcement & Boundary Testing
- *Actions:* Performed “unauthenticated baseline” tests to confirm that protected endpoints stay inaccessible without credentials.
- *Actions:* Observed server behavior shifting from 401 Unauthorized to 200 OK when valid tokens were supplied.
- *Outcome:* Verified that the API should follow a strict “deny by default” model before processing any sensitive data.

---

## 3. Vulnerability Simulation (Broken Auth)
- *Actions:* Used Burp Repeater to remove, modify, and replay authentication tokens to probe for weaknesses.
- *Actions:* Checked for broken authentication indicators such as token reusability, missing expiry checks, and weak validation.
- *Outcome:* Simulated real‑world attack paths where malformed or expired tokens might still be accepted, enabling unauthorized access or account takeover.

---

## Summary
- *Actions:* Focused the day on testing the API’s authentication mechanisms as the primary “gatekeeper”.
- *Outcome:* Built skills to detect where identity verification is missing, misapplied, or weak, aligning directly with critical risks described in the OWASP API Top 10.

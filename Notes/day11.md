# Day 11 — API Security: Conceptualizing the OAuth 2.0 Framework

## 1. Framework Architecture and Roles
- *Actions:* Systematically mapped the interaction between the Client, Authorization Server, and the Resource Server.
- *Outcome:* Successfully identified the "Resource Server" (the API) as the most critical point of failure in real-world authorization testing.

---

## 2. Grant Type Analysis and Use-Case Mapping
- *Actions:* Analyzed the Authorization Code and Client Credentials flows to determine their appropriate security contexts.
- *Outcome:* Developed the ability to identify "Misconfigured Flows" where inappropriate grant types are utilized for sensitive API access.

---

## 3. Threat Identification: Common OAuth Logic Flaws
- *Actions:* Conceptualized high-impact vulnerabilities such as Scope Inflation, Audience Mismatch, and Token Substitution.
- *Outcome:* Positioned OAuth testing as a logic-based assessment rather than a simple payload-based search for bugs.

---

## Summary
- *Actions:* Established a comprehensive theoretical foundation for OAuth 2.0 in modern API environments.
- *Outcome:* Recognized that robust OAuth security requires the API to verify not just the token's signature, but its intended audience and permissions.

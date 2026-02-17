# Day 17 — SSO Attack Surface: OIDC, SAML & Identity Logic

## 1. Architecture & Trust Delegation
- *Actions:* Defined SSO as the delegation of authentication to external IdPs (Azure, Auth0, etc.).
- *Outcome:* Identified that the core risk lies in the application's "blind trust" of the IdP's result, often leading to over-privileged default roles.

---

## 2. Technology Comparison
- *Actions:* OAuth: API Access (Tokens). OIDC/SAML: User Login (Identity/Assertions).
- *Outcome:* Focused testing on post-login logic, where most high-impact bugs occur.

---

## 3. SSO-Specific Failure Modes
- *Actions:* Audited the attack surface for:
  - ID Token Abuse: Using identity tokens for authorization.
  - Audience (aud) Confusion: Cross-app token acceptance.
  - Logout Gaps: SSO sessions remaining active after app-level logout.
  - Role Mapping: Inconsistencies between IdP roles and internal app permissions.
- *Outcome:* Linked these failures to OWASP API2, API5, and API8.

---

## 4. Pentester Mental Model
- *Actions:* Shifted testing focus from the IdP to the application's consumption of IdP data. Questions: "Does identity equal permission?" and "What survives a logout?"
- *Outcome:* Established a roadmap for chaining SSO flaws with token misuse and BFLA.

---

## Summary
- *Actions:* Focused on mapping how SSO changes an application's attack surface, emphasizing that misconfigurations in identity mapping multiply authorization failures.

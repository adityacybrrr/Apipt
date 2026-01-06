# Day 6 — API Assessment: JWT Structural Analysis

## 1. Token Anatomy & Encoding Review
- *Actions:* Conducted a structural audit of the JSON Web Token (JWT) standard, focusing on header, payload, and signature segments.
- *Actions:* Verified that the header and payload use Base64URL encoding rather than encryption.
- *Outcome:* Confirmed that JWT contents are not confidential by default, highlighting privacy risks if sensitive data is placed inside tokens.

---

## 2. Authorization Claim Review
- *Actions:* Inspected payload claims for potential Sensitive Data Exposure, such as PII or internal role identifiers.
- *Actions:* Evaluated how strongly the application depends on these claims when making access-control decisions.
- *Outcome:* Determined how much the authorization model trusts client-controlled data, and where that trust could lead to Broken Access Control.

---

## 3. Transport Security Assessment
- *Actions:* Recorded how tokens are transmitted in requests, for example via the Authorization: Bearer <token> header.
- *Actions:* Assessed the likelihood of token leakage through less secure channels or logging mechanisms.
- *Outcome:* Verified whether the token handling approach aligns with industry best practices for secure transmission and storage.

---

## Summary
- *Actions:* Performed a reconnaissance-focused review of JWT structure, claims, and transport.
- *Outcome:* Recognized that the transparency of JWT claims is a key prerequisite for spotting Broken Access Control and other authorization vulnerabilities in API implementations.

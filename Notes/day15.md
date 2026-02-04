# Day 15 — OAuth 2.0: Token Misuse & The Authorization Fallacy

## 1. The Core Concept: Token ≠ Permission
- *Actions:* Challenged the developer assumption that "Valid Token = Trusted Request" by analyzing the multi-layer validation requirements of OAuth.
- *Outcome:* Established that security fails when APIs neglect to validate Scope, Audience (aud), and User-Object relationships, even if the token signature itself is valid.
- *Insight:* Today's focus shifted from authentication (identity) to authorization (permissions).

---

## 2. Methodological Approach: Opaque Token Analysis
- *Actions:* Utilized Firefox and Burp Suite to capture an Opaque Access Token via the Authorization Code Flow (POST /oauth/v2/oauth-token).
- *Outcome:* Since the token was opaque (non-JWT), local decoding was bypassed in favor of Behavioral Testing to determine the token's actual permissions.

---

## 3. Systematic Testing & Token Replay
- *Actions:* Executed a Burp Repeater workflow to replay the captured token against various endpoints, methods, and paths.
- *Actions:* Investigated Scope Integrity (can a "read" token perform "write" actions?) and Audience Validation (can this token be used on unintended services?).
- *Outcome:* Confirmed that token validation only occurs at the Resource Server level, as evidenced by the 404 error when replaying tokens to oauth.tools.

---

## 4. Vulnerability Mapping & Defense
- *Actions:* Mapped identified behaviors to the OWASP API Top 10, specifically BOLA (API1), BFLA (API5), and Security Misconfiguration (API8).
- *Outcome:* Defined the defensive mandate: APIs must independently enforce authorization logic and never assume a valid token grants universal access.

---

## Summary
- *Actions:* Focused on the critical gap between token validity and granular authorization, using behavioral replay to identify high-impact logic flaws.

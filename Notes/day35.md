# Day 35: Auth Token Abuse & Validation Weaknesses


## SECTION 1: The Trust Paradox

### 1.1 Cryptographic Validity $\neq$ Operational Security
A common developer mistake is verifying only the Signature of a JWT (JSON Web Token).
- The Logic: "The signature is valid; therefore, the user is allowed to do whatever the request says."
- The Flaw: This ignores the claims inside the token ($scope, aud, exp$) and the relationship between the token and the specific resource.

### 1.2 The "Swiss Army Token" Problem
When an API doesn't enforce Scopes, a token issued for a "Read-Only" mobile app can be used to perform "Write/Delete" actions on the web API. The token becomes a universal key because the Resource Server (the API) fails to check if the scope claim allows the requested HTTP method.

---

## SECTION 2: Common Token Abuse Vectors

### 2.1 Scope Enforcement Failure
The API sees scope: "user.read" in the token but fails to block a DELETE /api/v1/account request.
- Test: Capture a token from a low-privilege feature and replay it against a high-privilege endpoint.

### 2.2 Audience (aud) Confusion
A token meant for api.frontend.com is accepted by api.billing.com.
- The Risk: If Service A is compromised or less secure, its tokens can be "pivoted" to attack more sensitive services (Service B) because Service B isn't checking if it was the intended recipient.

### 2.3 ID Token vs. Access Token
- ID Token: For the client (the UI) to know who the user is.
- Access Token: For the API to authorize requests.
- The Vulnerability: Some APIs incorrectly accept an id_token in the Authorization header. ID tokens often lack the strict scope/rate-limiting protections of access tokens.

---

## SECTION 3: Technical Protocol - The "Token Replay" Audit
Professionals test if a token is bound to a specific session or environment.
1.	Cross-IP Replay: Use the token from a different IP address. If it works, the token is not IP-bound.
2.	Cross-Device Replay: Use a token captured from a mobile app on the desktop Web API.
3.	Expiration Probing: Save a token and wait for its exp time to pass. Attempt to use it at $T+1$ minute. If the API still responds with 200 OK, the server is not validating the expiration claim.

---

## SECTION 4: Chaining OAuth Misuse with BOLA/BFLA
Token abuse acts as an Amplifier for the vulnerabilities we've studied previously.
| Chain Pattern | Action | Result |
|--------------------|----------|---------|
| OAuth + BOLA | Use a valid token to request /api/users/102 (Victim). | Access to victim data because the API trusts the token signature but doesn't check the sub (subject) against the URL ID. |
| OAuth + BFLA|Use a "Guest" token to call /api/admin/system-stats. | Privilege escalation because the API ignores the role or scope claims. |
| OAuth + BLF | Use a token multiple times for a "one-time" action (e.g., POST /api/claim-reward). | Race Condition/Replay: Gaining multiple rewards with a single authorization. |

---

## SECTION 5: The "Audience Confusion" Workflow
The Attack Flow:
1.	Obtain: Log in to service-a.example.com and capture the JWT.
2.	Identify: Check the aud (Audience) claim. It says "Service-A".
3.	Pivot: Send a request to service-b.example.com (a different internal API) using the same JWT.
4.	Confirm: If Service B returns data, it is failing to validate the aud claim, allowing for lateral movement across the infrastructure.

---

## SECTION 6: Audit Checklist: Token Abuse
- Signature vs. Claims: Does the API validate the exp, nbf (not before), and iat (issued at) claims, or only the signature?
- Scope Hardening: Have you attempted a POST/DELETE action using a token that only has read scopes?
- Audience Check: Does the Resource Server verify that the aud claim matches its own identifier?
- Token Type Confusion: Have you tried using an id_token where an access_token is expected?
- Replay Resistance: Can the same token be used from a completely different geographic IP/User-Agent?
- Expiration Enforcement: Does the API reject tokens immediately after the exp timestamp?
- Revocation Test: If you "Log Out" (revoking the token), does the API still accept that token until it naturally expires? (Indicating a lack of a "Blacklist" or server-side revocation check).

---

### Summary 
Day 35 shifts the focus from "finding" a token to "abusing" the trust placed in it. While a token may be cryptographically perfect (signed by the correct authority and not tampered with), the vulnerability often lies in the Authorization Server or the Resource Server's failure to validate its context. We explore Broken Authentication (API2) and BFLA (API5) through the lens of Scope Creep, Audience Confusion, and Token Replay. The goal is to prove that a "valid" token for User A can be weaponized to perform actions it was never intended to authorize.

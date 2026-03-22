# Day 33: Auth + BOLA Chaining (Account Takeover)


## I. The Authentication vs. Authorization Gap
In a secure API architecture, Authentication ($Who are you?$) is merely the first gate. The second, more critical gate is Authorization ($What are you allowed to do with this specific ID?$).
*The Developer’s Trap:* Many backends implement a global "Auth Guard" that checks if a Bearer Token is valid. If it is, the code proceeds to fetch the requested resource ID from the database without verifying if the $Subject$ in the token matches the $Owner$ of the ID.

---

## II. The Anatomy of an Account Takeover (ATO) Pivot
A professional penetration test doesn't just "view" another user's profile; it seeks to own the account. This requires a multi-step logical chain.
### Phase 1: The Reconnaissance Leak
The attacker uses a valid session to probe for BOLA.
- Request: GET /api/user/102
- Leaked Fields: If the response includes sensitive keys like email, phone_number, or hidden internal_uuid, the pivot begins.
*JSON*

{
  "id": 102,
  "email": "victim@target.com",
  "is_mfa_enabled": false,
  "account_status": "active"
}

### Phase 2: The State-Changing Manipulation
The attacker identifies an endpoint that updates user attributes.
- Target: PUT /api/user/102
- Payload: {"email": "attacker-controlled@gmail.com"}
- Logic Failure: If the API allows a user with Token A to modify the email of User B, the attacker now "owns" the identity associated with that ID.

### Phase 3: The Identity Pivot (Final Takeover)
With the email changed to one they control, the attacker triggers the standard POST /api/password-reset flow. The reset link is sent to the new (attacker's) email, allowing them to set a new password and generate a fresh, legitimate session for the victim's account.

---

## III. Token Misuse & Resource Misalignment
In modern JWT-based architectures, the token often contains a sub (subject) claim representing the User ID.
-  The Vulnerability: The server extracts sub: 101 from the JWT but then executes:
SELECT * FROM users WHERE id = {request.params.id}
- The Secure Fix: The server must strictly use the ID from the Claims, not the Parameters:
SELECT * FROM users WHERE id = {jwt.claims.sub}
If an API accepts a User ID in the URL while a token is present, it is architecturally predisposed to BOLA.

---

## IV. Profile Update Abuse: The Silent Kill
The most dangerous BOLA variants are found in "Partial Updates" (PATCH/PUT).
- Scenario: An API allows updating a "Bio" or "Profile Picture."
- Exploit: An attacker adds a "hidden" parameter discovered via Parameter Mining (Day 25):
*HTTP*

PATCH /api/user/102
{
  "bio": "Hacked",
  "role": "admin",
  "email": "attacker@blackhat.com"
}

If the backend uses a generic "Update" function that maps the JSON body directly to the Database Model (Mass Assignment), the account is compromised.

---

## V. Professional ATO Testing Flow
A Senior Consultant follows this rigorous matrix to prove high-impact takeover paths:
1.	Cross-User Access: Can I read PII (Email/Phone) of User B?
2.	Sensitive Action Mapping: Find endpoints for password-change, email-update, or mfa-disable.
3.	Ownership Verification: Send a request to change User B's email using User A's token.
4.	Credential Pivot: Use the modified email to perform a "Forgot Password" workflow.
5.	Session Escalation: Log in as User B and verify access to their private resources (e.g., credit cards, messages).

---

## VI. OWASP API Security Mapping
| Risk Category | Tactical Connection to Day 32 |
|--------------------|----------------------------------------|
| API1:2023 BOLA | Using an authenticated session to access or modify objects belonging to others. |
| API2:2023 Broken Authentication | Failing to properly tie a session token to the specific resources it is authorized to modify. |
| API5:2023 BFLA | Escalating from a "User Update" to a "User Takeover" by manipulating functional boundaries. |

---

### Summary
This session dismantles the common architectural fallacy that "Authentication equals Authorization." We explore the Account Takeover (ATO) Path, where a legitimate, authenticated user leverages a BOLA vulnerability to pivot into a victim’s session. By analyzing how session tokens interact—or fail to interact—with resource ownership logic, we identify the critical gaps that allow a standard user to escalate their privileges to that of any other user in the system. This maps to API1: BOLA and API2: Broken Authentication.

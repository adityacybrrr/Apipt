# Day 34: BFLA Chaining (Function Abuse → System Compromise)

### Lesson Context
Today, we move from horizontal movement (User A to User B) to Vertical Escalation. Day 34 focuses on Broken Function Level Authorization (BFLA). This is the "God Mode" of API vulnerabilities. While BOLA lets you see someone else's data, BFLA lets you perform actions you aren't supposed to even know exist. We are mapping this to OWASP API5, focusing on how a standard user token can be "weaponized" to execute administrative, internal, or destructive functions.

---

## The Core of the Flaw: Role-Based Failure
BFLA occurs when the server relies on "Security by Obscurity" (hiding the button in the UI) rather than "Security by Design" (verifying the user's role on the backend).
*The Developer's Logic Gap*
A developer might create a middleware that checks for a valid login, but forgets to check the User Role.
- The Check: is_authenticated == True ✅
- The Missing Check: user_role == 'ADMIN' ❌
If the second check is missing, the API assumes that anyone with a valid token is allowed to call any endpoint they can find.

---

## Vertical Privilege Escalation: The "Promotion" Attack
The most critical impact of BFLA is when an attacker uses a low-privileged account to grant themselves higher privileges.
The Scenario:
You are logged in as a "Viewer." You discover an endpoint via JavaScript analysis:
POST /api/v1/admin/set-role

The Execution:
*HTTP*

POST /api/v1/admin/set-role
Authorization: Bearer <VIEWER_TOKEN>
Content-Type: application/json

{
  "userId": "my_user_id",
  "new_role": "SUPER_ADMIN"
}


The Result: If the server responds with 200 OK, you have just achieved Vertical Privilege Escalation. You have bypassed the entire hierarchy of the application.

---

## The Lethal Combo: BFLA + BOLA
BFLA is dangerous. BFLA chained with BOLA is catastrophic. This combination allows a regular user to perform administrative actions on specific target objects.
- BFLA Component: You can access the DELETE /api/admin/user/{id} function.
- BOLA Component: You can change the {id} to any user in the database.
*The Attack Flow:*
1.	Enumerate: Find the UUID of the CEO or a lead developer (using BOLA/Recon).
2.	Execute: DELETE /api/admin/user/ceo_uuid using your standard user token.
3.	Impact: System-wide disruption and unauthorized account deletion.

---

## Hunting for "Shadow" Admin Endpoints
Admin functions are rarely linked in the main navigation. Pentesters find them in the "leaks":
- Documentation Crawling: Searching for /v1/swagger.json or /api/v2/console. Often, "hidden" admin endpoints are listed in the schema but hidden from the UI.
- Naming Patterns: Probing for common internal paths:
- /api/internal/*
- /api/mgmt/*
- /api/debug/*
- /api/system-health
- Method Swapping: If GET /api/users is public, test if DELETE /api/users or POST /api/users (to create admins) is accessible via BFLA.

---

## Action-Based Impact Matrix
When reporting BFLA, the severity is determined by the Action the function performs.
| Discovered Function | Potential Action | Final Impact | Severity |
|-----------------------------|----------------------|------------------|------------|
| GET /api/admin/stats | View system usage | Information Leak | Medium |
| POST /api/admin/export | Download all user PII | Mass Data Breach | High |
| POST /api/admin/config | Change API timeout/keys | System Instability | Critical |
| PATCH /api/admin/user/role | Upgrade own account | Full System Takeover | Critical |

---

## Tactical Testing: The "Admin-to-User" Pivot
The best way to test for BFLA is to use two accounts with different privilege levels (Admin and User).
1.	Capture: Log in as Admin and perform a privileged action. Capture the request in Burp Suite.
2.	Swap: Send that exact request to Repeater. Replace the Admin token with a Standard User Token.
3.	Analyze:
- 401/403 Forbidden: Secure. The server is checking roles.
- 200 OK / 204 No Content: Vulnerable (BFLA). The server only checked if you were logged in, not who you were.

---

## OWASP API Mapping
| Risk ID | Title | Strategic Connection |
|----------|--------|-----------------------------|
| API5:2023 | BFLA | The primary vulnerability. Accessing unauthorized functions. |
| API1:2023 | BOLA | Used within BFLA to target specific resources (deleting a specific user). |
| API9:2023 | Improper Assets | Admin endpoints often reside in "Internal" or "Legacy" API versions that are forgotten. |

---

### Summary
Day 34 teaches us that endpoint visibility is not security. A professional pentester doesn't just look for "bugs"; they look for "Power." By identifying functions meant for administrators and attempting to execute them with low-privilege tokens, we uncover the flaws in the application's governing logic.

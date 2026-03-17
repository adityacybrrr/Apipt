# Day 25: API Versioning & Deprecated Endpoints

## SECTION 1: The Architecture of Persistence
### 1.1 Why Versioning Exists (and Persists)
API versioning is a functional necessity for maintaining service continuity. When developers introduce "breaking changes" (modifying data structures, changing authentication requirements, or refactoring endpoints), they cannot force all clients—especially third-party integrations and legacy mobile apps—to update simultaneously.
**Common Implementation Methods:**
- **URI Pathing:** https://api.target.com/v1/resource
- **Custom Headers:** X-API-Version: 2.0
- **Accept Headers:** Accept: application/vnd.company.v1+json
### 1.2 The Security Failure: Version Drift
Version Drift is the divergence of security implementations across different versions of the same functional logic.
While the current version may implement robust OAuth2.0 and strict input validation, the legacy version (often running on the same backend infrastructure) might still rely on weak API keys or lack rate-limiting entirely.
---
## SECTION 2: Identifying the Hidden Attack Surface
### 2.1 Patterns of Legacy Discovery
Professionals do not rely on luck; they apply logical incrementation to discovered routes.
**The "Predictable Path" Methodology:**
If a baseline endpoint is identified as GET /api/v2/user/profile, the following variants must be audited:
- /api/v1/user/profile (The Legacy Path)
- /api/v3/user/profile (The "Hidden" Next-Gen/Beta Path)
- /api/v0/user/profile (The Initial Alpha/Internal Path)
- /api/beta/user/profile
- /api/test/user/profile
### 2.2 Version Leakage Vectors
Legacy endpoints are rarely advertised but frequently "leaked" through:
- Client-Side JavaScript: Hardcoded fallback URLs in JS bundles.
- Mobile Binary Analysis: Older APK/IPA versions frequently communicate with deprecated endpoints that remain server-side.
- Documentation History: Archived versions of Swagger/OpenAPI docs.
- Server Headers: Analyzing X-Powered-By or custom version headers in response packets.
---
## SECTION 3: Technical Protocol for Version Comparison
### 3.1 The "Differential Audit" Workflow
Once multiple versions of an endpoint are identified, the tester must perform a side-by-side comparison of the responses.
**Case Study: Data Sanitization Failure**
- Request (v2): GET /api/v2/users/me
- Response: {"id": 1, "username": "pentester"} (Sanitized)
- Request (v1): GET /api/v1/users/me
- Response: {"id": 1, "username": "pentester", "password_hash": "$2b$12$...", "internal_role": "admin"} (Vulnerable)
### Key Areas for Comparison
| Testing Vector | What to Look For |
|-------------------|-----------------------|
| Field Exposure | Does the old version return "Extra" sensitive fields? |
| Auth Bypass | Does the old version accept expired tokens or lack BOLA checks? |
| Rate Limiting | Is the legacy endpoint unprotected against brute-force attacks? |
| Error Handling | Does the older version provide more verbose stack traces? |
---
## SECTION 4: Real-World Risks & OWASP Alignment
| Vulnerability Type | Legacy API Behavior | Morden API Behavior |
|-------------------------|----------------------------|-----------------------------|
| BOLA (API1) | Permissive: ID based access only. | Strict: Verifies ownership of the object. |
| Excessive Data (API3) | Returns the full DB object. | Returns only required fields. |
| Rate Limiting (API4) | No limits (supports old bulk-sync). | Strict per-user/per-IP limits. |
| Auth (API2) | Uses legacy API_KEY in URL. | Uses short-lived JWTs. |

**OWASP API9: Improper Assets Management**
This is the primary mapping for Day 24. Failure to retire old versions results in "Shadow APIs" that function as backdoors into the current database.
---
## SECTION 5: The "Shadow API" Visualization
The image above illustrates the fundamental danger: even if the Front Door (v2) is locked with modern security, the Side Door (v1) often provides an unmonitored path to the same sensitive Data Layer.
---
## SECTION 6: Audit Checklist: Versioning & Deprecation
-  Path Incrementation: Have you manually tested v0 through v[current+1] for all identified routes?
- Header Modification: Have you attempted to change version numbers in X-API-Version or Accept headers?
- Response Comparison: If multiple versions exist, have you compared the JSON keys returned for sensitive data leakage?
- Auth Regression: Does a token that is rejected by v2 (e.g., due to scope) work on v1?
- Subdomain Recon: Have you checked for dev.api.target.com or beta.api.target.com which often run legacy code?
- Documentation Check: Can you access /v1/swagger.json or /v1/api-docs?
---
### Summary:
Day 24 focuses on the "Shadow API" phenomenon, where legacy versions of an interface remain active to support backward compatibility, creating a significant security vacuum. This session explores Version Drift—the delta between the security posture of a modern API and its predecessor. We move beyond simple discovery to perform Comparative Analysis, identifying cases where vulnerabilities patched in $v_{n}$ remain exploitable in $v_{n-1}$. This addresses the critical "Improper Assets Management" risk, exposing how attackers leverage "forgotten" endpoints to bypass modern security controls.

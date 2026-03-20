# Day 30: Improper Asset Management

## I. The "Shadow API" Architecture
In a rapidly iterating DevOps environment, the rate of API creation often outpaces the rate of decommissioning. This leads to an architectural state where "Shadow APIs" exist—endpoints that are functional and connected to live databases but are not documented, monitored, or included in the standard security audit.
The Core Threat: While the "Production" API might be hardened with MFA, WAFs, and rigorous authorization logic, a "Beta" or "Dev" version residing on a forgotten subdomain might point to the same production database without any of those protections.

---

## II. The Catalyst: Why Assets Become "Improper"
Architectural drift occurs due to several organizational factors:
- Microservice Proliferation: Large ecosystems make it difficult to maintain a centralized "source of truth" for all active routes.
- Backward Compatibility Requirements: Keeping $v1$ active for a small group of legacy partners while the rest of the world moves to $v3$.
- Environment Leakage: Test, Staging, or Development environments being accessible from the public internet rather than restricted to an internal VPN.

---

## III. Advanced Reconnaissance for Unmanaged Assets
A Senior Consultant moves beyond standard discovery to find what the organization has "forgotten."
### 1. Subdomain & Environment Brute-forcing
Attackers look for naming conventions that suggest non-production environments.
- Targets:
- dev-api.target.com
- staging-api.target.com
- qa-auth.target.com
- beta-v2.target.com

### 2. Pattern-Based Version Discovery
If api.target.com/v3/ is the standard, we programmatically probe for the "Ghost Versions."
- Probing Logic: Testing for /v1/, /v2/, /v0/, or even /v4-alpha/.
- The Goal: Finding the version that lacks the BOLA or BFLA fix implemented in the current release.

### 3. Passive Leaks (JS and Documentation)
- JavaScript Analysis: Searching production frontend bundles for hardcoded development strings. A React component might contain a fallback URL to a test-api that was used during the sprint.
- Swagger/OpenAPI UI Discovery: Searching for /swagger-ui.html, /v2/api-docs, or /redoc. These tools often list all endpoints, including those intended only for internal developers.

---

## IV. The Danger of "Forgotten" Security Controls
Unmanaged APIs are dangerous because they are "frozen in time." They usually suffer from:
- Lack of Patching: Vulnerable to old exploits because they aren't part of the automated update cycle.
- No Monitoring: Security Operation Centers (SOC) typically only monitor the main production logs. Attacks on /api/v1-beta may go completely unnoticed.
- Permissive Authorization: Developers often skip complex auth logic in "Dev" or "Beta" versions to speed up testing, forgetting that these routes are public.

---

## V. Strategic Integration: The Entry Point
Improper Asset Management is rarely the end of an attack; it is the Entry Point. Once a forgotten API is discovered, it provides the "playground" for all other vulnerabilities:
1.	Find Hidden API (Day 30)
2.	Enumerate Users (Day 24)
3.	Perform BOLA (Day 26/27)
4.	Extract Data (Day 26)

---

## VI. OWASP API Security Mapping: API9:2023
| Vulnerability Class | Tactical Connection to Day 30 |
|--------------------------|-----------------------------------------|
| Improper Assets Management | The fundamental failure to keep an accurate inventory and retire legacy/test endpoints. |
| Security Misconfiguration | Development environments left with default credentials or verbose debugging enabled. |
| Broken Authentication | Older API versions using deprecated, weaker, or completely absent authentication mechanisms. |

---

### Summary
This module addresses the critical risk of Shadow APIs and Legacy Exposure. Improper Asset Management is often cited as the root cause of high-profile data breaches, as it represents the gap between an organization's known attack surface and its actual footprint. By exploring forgotten versions, leaked subdomains, and abandoned development environments, we identify entry points that bypass modern security perimeters. This guide maps directly to API9:2023 Improper Assets Management.

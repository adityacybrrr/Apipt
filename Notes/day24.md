# Day 24: Structured Endpoint Enumeration

## 🔐 SECTION 1: Architectural Definitions & The Enumeration Logic

### 1.1 Defining the Enumeration Process

In the context of a Senior Security Audit, Enumeration is defined as the systematic process of gathering exhaustive details about a target system's internal resources. Unlike general discovery, enumeration is an active, iterative phase where a tester extracts specific metadata regarding users, roles, unique identifiers, and service configurations to identify high-value attack vectors.

---

### 1.2 Reconnaissance vs. Enumeration: The Strategic Gap

Understanding the distinction between these two phases is critical for maintaining a "low-noise" profile during an engagement.

| Feature | Reconnaissance (Broad) | Enumeration (Deep) |
|-----------|------------------------|--------------------|
| Primary Goal | Asset Discovery: Identifying that an API exists. | Data Extraction: Identifying what is inside the API. |
| Questions Asked | "Where is the API host?" / "Is there documentation?" | "What are the valid UserIDs?" / "What are the hidden roles?" |
| Focus | High-level mapping (Versions, Gateways). | Granular probing (Parameters, Object IDs). |
| Output | A surface-level map of the infrastructure. | A categorized target list for exploitation (BOLA/BFLA). |

**Reconnaissance Example (The Map):**

Locating the entry points:

  - GET /api/v1  
  - GET /swagger.json  
  - GET /graphql  
  - Identifying headers: Server: nginx, X-Powered-By: Express, Authorization: Bearer <JWT>

**Enumeration Example (The Targets):**
Extracting the "meat" from the entry points:
  - ID Extraction: GET /api/users/1, GET /api/users/2
  - Schema Extraction:
```graphql
{
__schema {
types { name }
}
}
```
- Object Discovery: GET /api/orders/ORD-2026-000124
---
## SECTION 2: The Enumeration Taxonomy (Types of Discovery)
### 2.1 User & Identity Enumeration
The goal is to validate the existence of accounts. A professional observes the differential response from the server:
  - GET /api/users/101 $\rightarrow$ 200 OK (User Valid)
  - GET /api/users/999 $\rightarrow$ 404 Not Found (User Invalid)
  - GET /api/users?email=admin@company.com $\rightarrow$ Returns profile data (High-value target confirmed).
### 2.2 Order & Object Enumeration (The BOLA Foundation)
Testing for predictable, incremental identifiers. If an API uses sequential naming conventions, it is inherently vulnerable to mass enumeration.
  - GET /api/orders/ORD-2026-0001
  - GET /api/orders/ORD-2026-0002
  - *Security Impact:* Directly feeds into BOLA (Broken Object Level Authorization) testing.
### 2.3 Parameter & Hidden Field Enumeration
Attackers probe for undocumented parameters that might bypass logic or grant elevated privileges.
  - Standard Request: POST /api/update-profile with {"name": "Sam"}
  - Probed Parameters: * is_admin: true
     - role: "super_user"
     - debug: 1
     - user_type: "internal"
### 2.4 Role & Privilege Enumeration
Identifying the hierarchy of the application. We test for administrative endpoints that may not be linked in the UI but exist in the routing logic:
- /api/admin/users
- /api/manager/dashboard
- /api/support/ticket-delete
### 2.5 GraphQL Schema Enumeration
Leveraging the __schema and __type introspection queries to rebuild the entire backend data model, revealing hidden mutations and queries.
---
## SECTION 3: Technical Protocol for Professional Discovery
### 3.1 Sources of Truth (The Professional Hierarchy)
Professionals do not start with a wordlist; they start with Observation.
1.	Browser DevTools: The "Network" tab is the primary source of truth. By analyzing XHR/Fetch requests in SPAs (Single Page Applications), we identify the real-time interaction between the frontend and the backend API.
2.	Burp Suite HTTP History: Analyze captured traffic for patterns. Look for "leakage" in pathing:
- /v1/ vs /v2/
              - /beta/ or /staging/ routes
           - /mobile/ specific endpoints that may have weaker security controls.
3.   JavaScript Static Analysis: De-minify and search frontend JS bundles for:
       - Hardcoded API keys or Base URLs.
       - Routes like config.API_URL + "/internal/auth".
       - Feature flags (enable_debug_logging: false).
4. Logical Version Manipulation: Once a path is found, logically iterate.
       - If /api/v2/user exists, manually test /api/v1/user or /api/v0/user to find deprecated, unpatched logic.
5. Parameter Fuzzing: If GET /api/user?id=1 works, try variations like userId, uid, uuid, or account_id to trigger different backend functions.
---
## SECTION 4: The Strategic Difference: Amateurs vs. Professionals
|Amateur Approach (Fuzz-First) | Professional Approach (Context-First) |
|--------------------------------------------|-------------------------------------------------------|
| Immediately runs ffuf or dirb with 100k wordlists. | Observes application traffic to identify naming conventions. |
| Ignores the "why" and looks for 200 OKs. | Categorizes endpoints into "Object-based" vs "Function-based." |
| Generates massive WAF logs and noise. | Uses targeted, logical manipulation (e.g., v1 $\rightarrow$ v2). |
| Misses endpoints hidden in JS files. | Deep-dives into JS and documentation schemas first. |

--- 

## SECTION 5: OWASP API Security Mapping
The activities performed during Endpoint Enumeration directly identify risks associated with the following OWASP API Top 10 categories:
- API9: Improper Assets Management: Discovery of "Shadow APIs," deprecated versions (/v1/), and unmanaged staging environments.
- API10: Unsafe Consumption: Identifying internal-only endpoints or third-party integrations that are exposed to the public internet.
- API1: Broken Object Level Authorization (BOLA): Enumeration of sequential IDs (/users/101) provides the list of targets for BOLA testing.
- API5: Broken Function Level Authorization (BFLA): Discovery of administrative paths (/api/admin/...) sets the stage for privilege escalation testing.
___
## SECTION 6: Audit Checklist for Enumeration
- Traffic Capture: Have all XHR/Fetch requests from the web and mobile clients been captured in Burp?
- JS Grep: Have you searched all .js files for string patterns like http, /api/, and _key?
- Version Probing: Have you manually checked for v0, v1, v2, beta, and dev prefixes on all discovered routes?
- Parameter Guessing: Have you tested for common hidden parameters like admin, debug, test, and internal?
- Auth Analysis: Does the enumeration change when authenticated as a low-level user vs. an unauthenticated guest?
- Identifier Predictability: Are IDs UUIDs (Good) or sequential integers (Vulnerable to Enumeration)?

___
## Summary:
This module marks the transition from passive reconnaissance to operational enumeration, moving beyond simple discovery to the systematic mapping of the API attack surface. We explore the granular differences between broad recon and deep-seated enumeration, focusing on the extraction of specific, actionable data points. By identifying hidden routes, versioning inconsistencies, and object identifiers, we build the foundational intelligence required for BOLA and BFLA exploitation. This guide establishes a professional workflow that prioritizes traffic analysis and logic over blind, noisy fuzzing.

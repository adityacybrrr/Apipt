# Day 26: Parameter Mining & Hidden Input Vector Analysis

## SECTION 1: The Logic of Undocumented Inputs

### 1.1 Defining Parameter Mining
Parameter Mining is the adversarial process of identifying valid input keys that the API backend recognizes but does not explicitly advertise in public documentation (e.g., Swagger/OpenAPI). These inputs are often "ghost parameters" that remain active in the code but are excluded from the frontend implementation.

### 1.2 Why "Hidden" Parameters Exist
Development lifecycles often necessitate "short-circuit" parameters for efficiency. These typically fall into three categories:
1.	Administrative Overrides: Parameters that allow support staff to see more data (e.g., ?view_as=admin).
2.	Legacy Integration: Parameters kept for older clients that required specific data structures (e.g., ?ver=legacy).
3.	Debug & Trace Flags: Inputs that trigger verbose error reporting or bypass certain checks during local development (e.g., ?debug=true).

---

## SECTION 2: The Mining Methodology (Sources of Leakage)
Professional consultants do not "guess" parameters; they mine them from the application's own footprint.

### 2.1 JavaScript Static Analysis (Client-Side Clues)
Frontend developers frequently leave references to backend parameters in the client-side code to handle future features or conditional rendering.
- Grep Targets: Search .js bundles for assignment operators or URL builders.
- Patterns: include=, expand=, isAdmin, debug, filter, fields.
- Example: Finding config.api + "?expand=permissions" in a JS file reveals a high-value parameter for authorization testing.

### 2.2 Response Metadata Analysis
The API itself may provide "hints" in its JSON responses about what it can do.
- Example Response:
*JSON*
{
  "user_id": "101",
  "links": [
    {"rel": "self", "href": "/api/v1/users/101"},
    {"rel": "internal", "href": "/api/v1/users/101?view=internal"}
  ]
}

The view=internal parameter is now a confirmed target for mining.

### 2.3 Traffic Pattern Analysis (Burp History)
Observing how the application handles pagination or sorting can reveal naming conventions.
- If the API uses ?sort_by=date, try mining for ?group_by=, ?filter_by=, or ?include_deleted=.

---

## SECTION 3: Technical Protocol for Parameter Testing
Once a parameter is identified, apply the Incremental Probing Protocol:
1.	Value Swapping: If ?include=profile works, test ?include=all, ?include=config, or ?include=shadow.
2.	Boolean Flipping: Test binary flags like ?debug=1, ?admin=true, or ?test_mode=yes.
3.	Type Juggling: If a parameter expects a string, provide an array or an object (common in Node.js/Express environments) to trigger unexpected logic.
- Example: GET /api/users?id[]=1&id[]=2

---

## SECTION 4: High-Risk Parameter Categories

| Parameter Class | Typical Syntax | Targeted Vulnerability |
|------------------------|--------------------|------------------------------|
| Expansion | expand, include, join | API3 (Excessive Data Exposure): Forces the backend to return sensitive nested objects. |
| Logic Flags | debug, trace, verbose | Information Disclosure: Triggers stack traces or internal system paths. |
| Administrative | is_admin, role, su | API5 (BFLA): Directly modifies the user's privilege level within the request context. |  
| Filtering | status, deleted, hidden | BOLA/BFLA: Accessing objects that should be restricted (e.g., ?status=all). |

---

## SECTION 5: OWASP Mapping & Impact Logic
Parameter mining is the precursor to several OWASP API Top 10 exploitations:
- API1 (BOLA): Using parameters like ?userId=102 on an endpoint meant for the current user (/me).
- API3 (Excessive Data Exposure): Using ?fields=password_hash,salary to force the API to return data it usually hides.
- API5 (BFLA): Manipulating a role parameter in a PATCH /api/user/settings request to elevate privileges:
*HTTP*
PATCH /api/v1/user/settings HTTP/1.1
Content-Type: application/json

{
  "name": "Attacker",
  "is_admin": true
}


---

## SECTION 6: Audit Checklist: Parameter Mining
- Static Analysis: Have all .js and .map files been analyzed for URL parameters?
- Introspection: Does the API documentation (Swagger) have "hidden" sections or deprecated parameters still listed?
- Naming Conventions: Have you tried common variations (e.g., uid, userId, user_id, userID)?
- Metadata Leakage: Do API responses contain keys like expandable, supported_filters, or available_views?
- Fuzzing (Structured): Have you used a targeted wordlist (like params.txt) against high-value endpoints?
- Response Comparison: Does adding ?debug=true change the Content-Length or the number of JSON keys returned?

---

### Summary: 
Day 25 investigates the "Hidden Logic" of APIs through Parameter Mining. We move beyond the visible schema to uncover undocumented inputs—often left behind for debugging, administrative oversight, or internal testing—that can radically alter backend execution. By identifying parameters like debug, include, and is_admin, we probe for architectural weaknesses that lead to unauthorized data exposure and privilege escalation. This module establishes a methodology for converting "blind" inputs into high-impact entry points for BOLA, BFLA, and Excessive Data Exposure.

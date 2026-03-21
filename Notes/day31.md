# Day 31: Recon → Attack Mapping


## I. The Philosophy of Attack Mapping
In high-end security consultancy, the "hacker" is distinguished from the "automated scanner" by their ability to understand Context. Reconnaissance provides the what, but Attack Mapping defines the how and why.
*The Transition Logic:*
1.	Reconnaissance: "I found an endpoint /api/v1/internal/export-pdf."
2.	Analysis: "This is a versioned, internal, resource-heavy function."
3.	Mapping: "Target this for API9 (Asset Management), API4 (Resource Consumption), and API5 (BFLA)."

---

## II. Endpoint Classification: The Consultant’s Taxonomy
A list of 500 URLs is useless without organization. Professionals group endpoints by their Functional Risk Profile.

| Category | Typical Path Examples | Primary Attack Vector |
|-------------|-------------------------------|-------------------------------|
| Identity & Access | /api/auth, /api/login, /api/mfa | Credential Stuffing, JWT Manipulation |
| Resource-Centric | /api/account/{id}, /api/docs/{uuid} | API1: BOLA (Broken Object Level Auth) |
| Privileged Actions | /api/admin/*, /api/config/set | API5: BFLA (Broken Function Level Auth) |
| Stateful Workflows | /api/cart/checkout, /api/pay | API6: Business Logic Flaws |
| Utility/Search | /api/v1/search, /api/v1/upload | API4: Rate Limiting / DoS |

---

## III. Constructing the Testing Matrix
The Testing Matrix is the central artifact of a professional API penetration test. It ensures 100% coverage and prevents the tester from "getting lost" in a large API surface.

| Endpoint | Vulnerability Type | Priority | Testing Technique |
|-------------|-------------------------|-----------|-------------------------|
| /api/v1/users/{id} | BOLA | Critical | Iterate IDs as User A; access User B’s data. |
| /api/admin/delete | BFLA | High | Attempt call using a standard User Token. |
| /api/v1/coupon | Logic Flaw | Medium | Test race conditions or multiple applications. |
| /api/v2/search | Rate Limit | Low | 500 requests/sec via Burp Intruder. |

---

## IV. Risk-Based Prioritization (The 80/20 Rule)
In a time-limited engagement, 80% of critical findings usually come from 20% of the API surface. Pentesters prioritize based on Business Impact:
1.	Administrative Gateways: Any endpoint with admin, root, internal, or mgmt in the path.
2.	PII-Heavy Object Endpoints: Paths that return user profiles, financial records, or private documents.
3.	Legacy/Shadow Assets: Discovered during Day 30; these are the "low-hanging fruit" often missing modern WAF protections.
4.	Mobile-Only Routes: Frequently discovered during Day 28; these often lack the robust authorization checks of the web-facing API.

---

## V. Strategic Integration: Connecting the Dots
Day 31 represents the culmination of all previous methodologies:
- From Day 24: Use Endpoint Enumeration to fill the "Target" column of the matrix.
- From Day 26: Use Parameter Mining to find the "Hidden Switches" for the "Method" column.
- From Day 28: Use Mobile Recon to find the "Alternative Paths" that bypass the main firewall.
- From Day 29: Apply Rate Limiting tests to ensure the mapping process itself can't be easily blocked.

---

## VI. OWASP API Security Mapping: The "Big Picture"
Professional reporting maps the entire attack map back to the OWASP API Top 10.
- Recon Stage: Addresses API9 (Improper Assets) and API10 (Unsafe Consumption).
- Mapping Stage: Identifies potential for API1 (BOLA), API3 (Excessive Data Exposure), and API5 (BFLA).
- Exploitation Stage: Validates API2 (Authentication), API4 (Resource Consumption), and API6 (Business Logic).

---

## VII. The Professional Workflow
1.	Aggregate: Consolidate findings from Burp, JS files, and Mobile binaries.
2.	Categorize: Group by function (Auth, Data, Admin, Workflow).
3.	Prioritize: Rank by potential business damage.
4.	Execute: Begin systematic testing following the Matrix.
Reconnaissance is the map; Attack Mapping is the plan; Testing is the journey.

---

### Summary: 
This capstone module synthesizes 31 days of technical study into an operational framework. Students will learn the critical transition from Data Gathering (Reconnaissance) to Strategic Execution (Attack Mapping). By classifying discovered endpoints into risk-based categories and constructing a formal Testing Matrix, practitioners move away from "blind fuzzing" and toward a professional, methodical exploitation phase that prioritizes high-impact business logic and authorization flaws.

# Day 4 — API Pentesting Workflow with Burp Suite

## Phase 1: Traffic Capture & Mapping
- *Actions:* Routed all Postman traffic through the Burp Suite proxy.
- *Actions:* Populated the HTTP history to identify the API's structure and data flow.
- *Outcome:* Built a comprehensive map of the API surface area and observed how the application handles authentication.

---

## Phase 2: Request Manipulation (Repeater)
- *Actions:* Selected interesting requests and sent them to the Repeater module.
- *Actions:* Isolated these requests to test server responses in a controlled environment.
- *Outcome:* Removed browser/client noise and focused purely on the raw request–response cycle.

---

## Phase 3: Vulnerability Testing (Experiments)
- *Actions:* Performed ID mutation by changing resource IDs to test for BOLA conditions.
- *Actions:* Carried out header injection by modifying User-Agent values and adding debug-style headers.
- *Actions:* Conducted body tampering by adding unauthorized fields such as role: admin to JSON payloads.
- *Outcome:* Simulated realistic attack scenarios and observed how well the server enforced security boundaries.

---

## Phase 4: Response & Impact Analysis
- *Actions:* Evaluated server status codes (for example, 403 Forbidden vs 200 OK) after each manipulation.
- *Actions:* Searched responses for stack traces or overly verbose error messages.
- *Outcome:* Assessed the security impact of each test and identified potential information disclosure risks.

---

## Summary
- *Actions:* Followed a structured “Capture → Analyze → Manipulate” workflow for API requests.
- *Outcome:* Aligned practice with professional methodology by emphasizing manual validation and Proof-of-Concept creation instead of relying solely on automated scanning.

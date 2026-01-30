# Day 03 — Mixed Style (Strategic + Practical)

## 1. POST as a State-Changer
- *Actions:* Treated POST as the HTTP verb used to send data that modifies backend state.
- *Actions:* Placed the payload in the request body, recognizing it as central to both application features and potential exploits.
- *Outcome:* Understood that POST is security-critical because it drives key business actions such as creating orders or updating profiles.

---

## 2. GET vs POST in APIs
- *Actions:* Used GET to retrieve data with parameters in the URL, aware that these are often cached and logged.
- *Actions:* Used POST to submit data with parameters in the body, driving create/update operations on the server.
- *Outcome:* Noted that complex API vulnerabilities tend to cluster in POST/PUT/PATCH endpoints where logic and permissions intersect.

---

## 3. JSON Bodies as the Contract
- *Actions:* Treated the request body as the “contract” that defines how the client and server communicate.
- *Actions:* Used JSON as the dominant representation with fields such as title, body, and userId.
- *Outcome:* Recognized that each field can influence ownership, visibility, or privileges if not properly controlled.

---

## 4. Observing a Real POST (Postman)
- *Actions:* Sent a JSON POST request to https://jsonplaceholder.typicode.com/posts.
- *Actions:* Verified that the server responded with HTTP 201 Created and returned a new id, confirming resource creation.
- *Outcome:* Saw how this behavior mirrors production APIs that handle record creation in real systems.

---

## 5. Offensive Mindset — Tweaking the Contract
### IDOR probe
- *Actions:* Altered the userId field to simulate acting as another account.
- *Outcome:* Acceptance of this change illustrated how BOLA/IDOR can begin when servers trust client-supplied identifiers.

### Mass Assignment probe
- *Actions:* Appended fields like isAdmin and role that were never exposed in the UI.
- *Outcome:* While the dummy service ignored them, this highlighted how real backends might bind and persist such fields automatically via Mass Assignment.

---

## 6. Burp in the Loop
- *Actions:* Captured the outgoing POST request to inspect exact headers and JSON content.
- *Actions:* Adjusted the body on the fly before forwarding it to the server.
- *Outcome:* Successfully replicated realistic attacker behavior by modifying live traffic in transit.

---

## 7. Scaling via Python
- *Actions:* Reproduced the POST call using requests.post() with JSON payloads in Python.
- *Actions:* Iterated over different users, roles, and payload variants using scripts.
- *Outcome:* Enabled rapid, large-scale testing of API behavior across many scenarios.

---

## 8. Security Takeaways (High-Level)
- *Actions:* Consistently treated POST bodies as untrusted, high-impact inputs requiring strict validation and authorization.
- *Actions:* Focused testing on POST/PUT/PATCH endpoints where business logic and access control intersect.
- *Outcome:* Used deliberate body manipulation to uncover IDOR and Mass Assignment, combining Postman, Burp, and Python into a repeatable API pentest workflow.
## Summary
Day 3 focused on understanding POST requests as state-changing operations, building and manipulating JSON request bodies, and observing how servers react to modified data. This established the core mindset and tooling needed to uncover issues like IDOR and Mass Assignment in POST/PUT/PATCH endpoints through deliberate, repeatable request manipulation.

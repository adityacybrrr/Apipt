 Day 02 — Core Concepts of API Request Tampering
---

1. Client Metadata Tampering
- *Learning:* We learned to manually control the User-Agent string.
- *Learning:* We gained experience injecting completely new custom headers.

Purpose:
To prove the client controls all request headers and to investigate how servers react to modified or unexpected metadata.

---

2. URL Input Testing
- *Learning:* Explored the structural process of adding and modifying key-value pairs in the query string:
  - test=123
  - debug=true

Purpose:
To practice the crucial technique of adding query parameters, specifically targeting features that may be accidentally left exposed (like the debug flag).

---

3. Object ID Vulnerability Simulation
- *Learning:* Demonstrated how the request path can be altered to target different resources, e.g., changing from resource ID 1 to ID 99.

Purpose:
To understand the mechanism and testing methodology behind Broken Object Level Authorization (BOLA/IDOR).

---

4. Enumeration of Resources
- *Learning:* Practiced requesting a sequence of related object IDs (/posts/1 through /posts/10).

Purpose:
To simulate the enumeration step of an IDOR attack, which is testing the authorization boundaries across multiple known resources.

---

5. Burp Suite Practical Application
- *Success:* Confirmed the ability to intercept, halt, and manually edit the contents of a live HTTP request.
- *Success:* All planned modifications to headers, paths, and query parameters were successfully executed.

---

Summary
Day 2 provided essential, hands-on experience in manipulating API requests. This practice confirmed that client input is untrusted and laid the groundwork for future vulnerability discovery.

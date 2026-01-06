# Day 4 — Practical Burp Suite Core Mastery

## 1. Proxy & History Audit
- *Actions:* Monitored live API traffic flowing through the Burp Proxy.
- *Actions:* Filtered HTTP History to identify /api/v1 endpoints and undocumented routes.
- *Outcome:* Gained full visibility into the API's functional map and established baseline application behavior.

---

## 2. Manual Replay (Repeater)
- *Actions:* Captured and replayed POST and GET requests using Repeater.
- *Actions:* Modified headers and JSON bodies directly without re-triggering the client UI.
- *Outcome:* Bypassed client-side logic to interact directly with the API backend for precise security testing.

---

## 3. Vulnerability Probing Experiments
- *Actions:* Performed path mutation to test for IDOR (e.g., /posts/1 → /posts/2).
- *Actions:* Injected custom headers like X-Test: burp to check server-side metadata processing.
- *Actions:* Tampered with JSON body parameters to probe for Mass Assignment and privilege escalation.
- *Outcome:* Built hands-on proficiency with the most common manual API attack techniques.

---

## 4. Comparative Analysis: Intercept vs. Repeater
- *Actions:* Defined Intercept as the tool for real-time traffic capture and inspection.
- *Actions:* Defined Repeater as the primary tool for iterative exploitation and clean testing.
- *Outcome:* Clarified the distinct roles of observation versus controlled manipulation in the Burp workflow.

---

## Summary
- *Actions:* Focused on manual manipulation of API requests from interception through analysis.
- *Outcome:* Established a professional pentesting workflow capable of identifying security flaws through systematic traffic modification and response analysis.

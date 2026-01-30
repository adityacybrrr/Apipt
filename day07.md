# Day 7 — API Security: Playing with JWT Logic & Claim Abuse

## 1. Checking if the Server is "Too Trusting"
- *Actions:* Examined how the backend uses userId and role claims to control access to data and features.
- *Actions:* Tested the "trust gap" by changing token values and seeing what the server actually verifies against its own database.
- *Outcome:* Discovered that if the server blindly believes token claims without server-side checks, attackers can impersonate anyone or self-escalate to admin.

---

## 2. Breaking the Rules with Burp Repeater (BFLA)
- *Actions:* Used Burp Repeater to capture a low-privilege token and replay it against admin/protected endpoints.
- *Actions:* Monitored server responses to find "Admin" or "Pro" features accessible with just a valid (but wrong-level) token.
- *Outcome:* Confirmed classic Broken Function Level Authorization (BFLA) where privilege checks were missing or token-based only.

---

## 3. Speeding Things Up with Python
- *Actions:* Wrote a Python script to batch-decode multiple JWTs and extract claims without signature verification.
- *Actions:* Used the script to scan tokens across API endpoints for hidden info, weak patterns, or misconfigurations.
- *Outcome:* Demonstrated that simple automation can quickly identify vulnerable tokens across large-scale API environments.

---

## Summary
- *Actions:* Targeted "logic flaws" in how the application reasons about authorization rather than cryptographic token attacks.
- *Outcome:* Proved that mathematically secure JWTs are still dangerous if developers fail to implement proper server-side identity and privilege validation.

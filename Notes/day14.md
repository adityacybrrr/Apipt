# Day 13 — OAuth 2.0: Redirect URI Misconfigurations & Testing

## 1. Trust Model & Misconfiguration Patterns
- *Actions:* Analyzed how insecure Redirect URI handling allows for token interception.
- *Observations:* Identified high-risk patterns: Wildcards, Substring matching, Open Redirects, HTTP scheme acceptance, and Parameter Pollution.
- *Outcome:* Established that these configuration errors directly result in full account compromise and token leakage.

---

## 2. Controlled Testing Workflow
- *Actions:* Utilized Burp Repeater to modify Redirect URI elements (path, subdomain, protocol) following the "one change per request" rule.
- *Outcome:* Verified server-side validation logic safely without attempting to redirect to external domains.

---

## 3. API Impact & Security Risks
- *Actions:* Evaluated how redirect flaws lead to valid tokens being replayed against the API.
- *Outcome:* Identified that even a bug-free API can be compromised if the OAuth client allows for user impersonation via redirect abuse.

---

## 4. Defensive Takeaways
- *Actions:* Outlined remediation strategies: Enforcing HTTPS, utilizing exact matching, and disabling wildcards.
- *Outcome:* Positioned server-side URI validation as a mandatory security barrier.

---

## Summary
- *Actions:* Targeted the identification of redirect URI flaws that lead to token leakage, emphasizing a structured and safe testing approach using Burp Suite.

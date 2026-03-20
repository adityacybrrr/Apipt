# Day 29: Rate Limiting & Abuse Testing Methodology

## SECTION 1: The Mechanics of Rate Limiting
### 1.1 Defining Rate Limiting Logic
Rate limiting is the implementation of a "governor" on API consumption. It ensures that no single actor—whether a malicious bot or a buggy third-party integration—can monopolize backend resources.

### 1.2 The Goal of Abuse Testing
The objective is not just to see if a limit exists, but to determine if that limit is meaningful. A limit of 10,000 requests per minute on a login endpoint is technically a "limit," but it is functionally useless against a modern brute-force attack.

---

## SECTION 2: High-Value Targets for Rate Limiting
Not all endpoints require the same level of throttling. A Senior Consultant prioritizes the following "Abuse Profiles":

| Endpoint Category | Example Path | Risk of Abuse |
|--------------------------|-------------------|--------------------|
| Authentication | POST /api/v1/login | Credential stuffing and brute-force. |
| Communication | POST /api/v2/sms/send-otp | SMS toll fraud and user harassment (OTP flooding). |
| Data Extraction | GET /api/products/search | Competitor scraping and intellectual property theft. |
| Heavy Processing | POST /api/reports/export | DoS (Denial of Service): Exhausting CPU/Memory via complex queries. |

---

## SECTION 3: Technical Protocol for Rate Limit Validation
*Step 1: Baseline Identification*
Identify the identification mechanism. Does the server use X-Forwarded-For, a session cookie, or an Authorization bearer token to track you?
*Step 2: Automated Probing (The Burst Test)*
Use Burp Intruder or a Python script to send a burst of 100+ requests to the target endpoint in under 10 seconds.
- Expected Result: 429 Too Many Requests.
- Vulnerable Result: 200 OK (Continuous).
*Step 3: Response Analysis*
Observe how the API communicates the limit. Does it provide a Retry-After header? Does it use custom headers like X-RateLimit-Remaining?
*Step 4: Identifier Rotation*
Attempt to bypass the block by changing your "identity":
- IP Rotation: Use a proxy or VPN.
- Header Spoofing: Add/modify headers like X-Forwarded-For: 127.0.0.1 or X-Real-IP: 8.8.8.8.
- Token Rotation: If limited per user, does the limit reset if you switch to a different low-privileged account?

---

## SECTION 4: Common Rate Limiting Bypasses (The Pentester's Edge)
Professionals look for "holes" in the implementation logic:
1.	Version/Path Shifting:
If POST /api/v2/login is limited, test if POST /api/v1/login or POST /api/beta/login lacks the same protection.
2.	Case Manipulation:
In some poorly configured WAFs, POST /api/LOGIN or POST /api/login/ (trailing slash) might bypass a rule set specifically for /api/login.
3.	Null Byte/Garbage Injection:
Adding ?ignore=123 or a null byte %00 to the URL to bypass exact-match string filters in the rate-limiter.
4.	Client-Side "Limits":
Verification that the "Please wait 60 seconds" message is just a UI timer and not a server-side enforcement.

---

## SECTION 5: OWASP Mapping & Business Impact
- API4: Unrestricted Resource Consumption: This is the direct mapping. Without limits, an attacker can drive up infrastructure costs (Auto-scaling groups spinning up instances) or crash the database.
- API6: Unrestricted Business Flows: Using an API meant for "One-time" use (like a referral code) thousands of times to exploit business logic.

## SECTION 6: Audit Checklist: Rate Limiting & Abuse
- Identification: Have you identified if the rate limit is tied to IP, Session, or JWT?
- Header Spoofing: Have you attempted to bypass IP-based limits using X-Forwarded-For or X-Client-IP?
- Method Permutation: Does the rate limit apply to all HTTP methods (GET, POST, PUT) on the same resource?
- Endpoint Parity: Are mobile-specific (/mobile/api/) or legacy (/v1/) endpoints equally protected?
- Response Codes: Does the server return a proper 429 status code, or does it silently drop requests (DoS)?
- Search Scoping: On search/list endpoints, does the API limit the limit or page_size parameter to prevent "Select All" queries?
- Resource Exhaustion: Can you trigger a multi-second delay on the server by requesting a large resource (e.g., a 10,000-page PDF export) repeatedly?

---

### Summary
Day 29 focuses on the defensive thresholds of the API—specifically its ability to withstand automated subversion. We examine Unrestricted Resource Consumption (OWASP API4), where a lack of request throttling allows for brute-force attacks, data scraping, and denial-of-service conditions. This module establishes a professional methodology for testing rate limit efficiency, identifying bypass vectors such as header manipulation and endpoint rotation, and ensuring that high-impact workflows (Login, OTP, Search) are resilient against high-velocity abuse.

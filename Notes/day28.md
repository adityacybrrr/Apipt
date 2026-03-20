# Day 28: Introduction to Mobile API Reconnaissance

## SECTION 1: The Mobile-API Symbiosis
### 1.1 The API-Centric Architecture
In modern mobile development, the application is rarely more than a "thin veneer" or UI wrapper. The intelligence, data storage, and business logic reside entirely behind REST or GraphQL APIs.
*The Recon Logic:*
If a feature exists in the mobile app (e.g., "Check Loyalty Points"), an equivalent API endpoint must exist to serve that data. By mapping every button and screen to its network request, a pentester can reconstruct the entire backend schema.
### 1.2 The "Security by Obscurity" Fallacy
A common developer pitfall is the assumption that mobile traffic is "invisible" compared to web traffic. This leads to:
- Weaker Authorization: Assuming no one will "see" the GET /api/mobile/admin/stats call.
- Hardcoded Secrets: Embedding API keys, Firebase credentials, or even private certificates within the app binary.
- Legacy Support: Keeping v1 APIs active specifically for older app versions that haven't been updated.

---

## SECTION 2: The Mobile Discovery Toolkit
### 2.1 Intercepting the Stream (Man-in-the-Middle)
To "see" what the app is doing, we must place a proxy between the device and the internet.
- Tools: Burp Suite Professional, OWASP ZAP, or mitmproxy.
- The Challenge: SSL Pinning. Many apps validate the server's certificate. A Senior Consultant must use tools like Frida or Objection to bypass pinning and allow traffic inspection.

### 2.2 Static Analysis: Decompiling the APK
For Android, the .apk file is essentially a ZIP archive containing compiled Java code (DEX files).
- jadx-gui: Used to decompile the DEX files back into readable Java code.
- Target Search Strings:
- https:// or http://
- api_key, secret, client_id
- Bearer, Authorization
- /v1/, /v2/, /internal/

### 2.3 Hybrid & React Native Recon
Many apps use React Native or Flutter. These apps often bundle a index.android.bundle file—a massive JavaScript file containing the entire application logic.
- Technique: Running strings or grep on the bundle file often reveals a treasure trove of hidden API routes and parameter names (e.g., ?debug=true or ?admin=1).

---

## SECTION 3: High-Value Mobile API Targets
| Target Type | Why it's Vulnerable | Exploitation Goal |
| Mobile-Specific Routes | Often lack the robust WAF/Rate Limiting applied to web routes. | API4 (Lack of Resources): Brute-force or DoS. |
| Debug/Staging URLs | Hardcoded URLs like https://dev-api.target.com. | API9 (Improper Assets): Access to non-production data. |
| Hardcoded Keys | Keys for AWS S3, SendGrid, or Google Maps. | Credential Theft: Pivoting to cloud infrastructure. |
| Direct Object Refs | Mobile UIs often pass raw IDs (user_id=500). | API1 (BOLA): Changing the ID to access other users. |

---

## SECTION 4: The Mobile-to-BOLA Pipeline
Mobile reconnaissance is the single best way to find BOLA (Broken Object Level Authorization).
1.	Observe: The app calls GET /api/v1/mobile/tickets/9921.
2.	Analyze: The request uses a simple integer ID.
3.	Test: Repeat the request in Burp Suite, changing the ID to 9922.
4.	Result: If the API returns another user's ticket, a critical BOLA vulnerability is confirmed. Developers often assume that because the UI only shows the user's own tickets, the API doesn't need to check authorization.

---

## SECTION 5: OWASP Mapping & Vulnerability Impact
- API9: Improper Assets Management: Mobile apps are the #1 source for discovering "forgotten" v1 or beta APIs that were supposed to be retired but remain active for backward compatibility.
- API3: Excessive Data Exposure: Mobile APIs often return the entire user object (including password_hash or internal_notes) and rely on the mobile app to "filter" it. A pentester sees the raw, unfiltered JSON.

---

## SECTION 6: Audit Checklist: Mobile API Recon
- Proxy Setup: Is the device/emulator correctly routing traffic through Burp Suite?
- SSL Pinning Bypass: If traffic is encrypted/blocked, have you used Frida/Objection to hook the trust manager?
- Binary Grep: Have you run grep -r "http" . on the decompiled source code?
- Secret Extraction: Have you checked res/values/strings.xml for API keys or tokens?
- Hardcoded Endpoints: Did you identify any staging, dev, or test subdomains in the source code?
- Bundle Analysis: For React Native apps, have you extracted and beautified the .bundle file for manual route mapping?
- Version Comparison: Does the mobile app use a different version of the API (e.g., /v1/) than the web app (/v2/)?

---

### Summary
Day 28 explores the "Mobile-First" attack surface. As modern organizations shift toward thick-client mobile applications, the backend APIs powering them often become neglected silos of security. This module focuses on the extraction of hidden endpoints, hardcoded secrets, and undocumented routes from Android (APK) and iOS environments. We move beyond browser-based testing to intercepting binary traffic and reverse-engineering application code, mapping these findings to API9: Improper Assets Management and API3: Excessive Data Exposure.

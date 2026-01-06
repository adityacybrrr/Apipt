 OAuth 2.0: Controlled API Testing & Validation Logic

## 1. The OAuth Testing Mindset
- *Actions:* Adopted an API-centric testing philosophy focused on validating token handling logic rather than endpoint discovery.
- *Actions:* Applied the "Isolation Principle": modifying one variable per request to ensure observed behaviors are tied to specific token changes.
- *Outcome:* Established that effective OAuth testing must answer a single question per request to accurately map the API's authorization logic.

---

## 2. Establishing the Baseline: Capture & Identification
- *Actions:* Utilized Burp Proxy to capture authenticated Authorization: Bearer <access_token> requests.
- *Actions:* Decoded JWT access tokens in read-only mode to identify critical claims such as scope, aud, iss, and roles.
- *Outcome:* Created a controlled baseline in Burp Repeater to evaluate whether the API actively enforces the claims identified within the token.

---

## 3. Systematic Token Validation Tests (Repeater Workflow)
- *Actions:* Performed a series of controlled tests including No Token (header removal), Malformed Token (invalid/empty values), and Token Replay across different endpoints and actions.
- *Actions:* Conceptually modeled Token Substitution scenarios involving tokens from different users or applications without performing brute-force.
- *Outcome:* Identified that inconsistent responses or 200 OK status codes during these tests serve as primary indicators for Broken Authentication and BFLA/BOLA.

---

## 4. Analyzing OAuth Failure Signals
- *Actions:* Monitored API behavior for "Silent Failures," such as identical responses regardless of token presence or role.
- *Actions:* Evaluated the consistency of 401 Unauthorized vs 403 Forbidden responses and analyzed verbose error messages for information leaks.
- *Outcome:* Determined that weak OAuth implementations often fail silently, making subtle behavioral shifts the most important signals for a pentester.

---

## Summary
- *Actions:* Focused on structured, low-noise OAuth2 testing to recognize authorization failure signals, preparing for exploitation phases without introducing unnecessary risk.

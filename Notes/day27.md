# Day 27: The Architecture of Business Logic Flaws & Systemic Impact

## I. Defining the Business Logic Layer
In a secure architecture, Business Logic is the set of rules that governs how an application handles data and workflows. While a technical bug might be a missing semicolon or an unescaped string, a business logic flaw is a failure of intent.
- Intended Rule: "A coupon code may only be applied once per unique Transaction ID."
- Logical Violation: The API accepts the coupon twice if the requests are sent in parallel (Race Condition) or if the step is repeated before the final checkout call.
Business logic flaws do not require "malformed" data; they use "valid" data in "invalid" sequences.

---

## II. The API Workflow Anatomy
APIs often decompose complex business processes into a series of discrete, stateful steps. A Senior Consultant must map these transitions to identify where the chain can be broken.
Example: E-Commerce Transaction Workflow
1.	Step 1: POST /api/cart/add (Initializes the cart object)
2.	Step 2: POST /api/cart/checkout (Calculates taxes and shipping)
3.	Step 3: POST /api/payment/process (Interacts with Payment Gateway)
4.	Step 4: POST /api/order/confirm (Finalizes the sale and triggers shipping)
The Architectural Failure: If the backend of Step 4 does not verify that Step 3 returned a SUCCESS status for the specific TransactionID, an attacker can jump from Step 2 directly to Step 4, effectively acquiring goods for free.

---

## III. Taxonomy of Logical Abuse
A high-end portfolio must categorize these flaws by the type of logic being subverted.

### 1. Workflow Bypass & Step Skipping
The exploitation of endpoints that assume a prior state has been verified.
- Attack Vector: Calling /api/v1/admin/setup after a normal user registration, assuming the "Setup" phase is only accessible once.
- Formula: If $Action(N)$ assumes $Action(N-1)$ is complete without server-side verification, the workflow is vulnerable.

### 2. Price and Numeric Manipulation
Occurs when the API trusts the client to provide authoritative values for financial or quantitative data.
- Technical Payload:
*JSON*
 {
"item_id": "WS-99",
"quantity": 1,
"price": 1.00
}

- Logic: If the server doesn't re-fetch the price of WS-99 from the database and instead uses the $1.00 provided in the JSON body, the business logic is fundamentally broken.

### 3. Quantity & Integrity Abuse
Testing the boundaries of mathematical logic within the business rules.
- Negative Values: {"quantity": -5}. If the backend adds a negative value to a cart, it may reduce the total price of other items.
- Buffer Overflows in Logic: Ordering $9,999,999$ items to see if the total cost "wraps around" to a negative or zero value.

---

## IV. Professional Testing Methodology: State Machine Analysis
Testing business logic requires a structured observation of how the API maintains "state" across multiple calls.
1.	Mapping (The Blueprint): Identify every API call involved in a process. Use Burp Suite to group these requests into a "Flow."
2.	Interchangeability Testing: Can the parameters of Step A be used in Step C?
3.	Order Manipulation: * Try 1 $\rightarrow$ 3 $\rightarrow$ 2 $\rightarrow$ 4.
- Try 4 (Directly).
4.	Replay Attacks: If I redeem a coupon in Step 2, can I send the same POST request again before Step 3 completes to get a double discount?
5.	Parameter Tampering: Identify client-controlled variables that should be server-controlled (e.g., is_admin, discount_rate, user_id).

---

## V. Strategic Integration: The Vulnerability Multiplier
Business Logic Flaws rarely exist in isolation; they act as a force multiplier for other OWASP risks.
- BLF + BOLA: An attacker uses a POST /api/refund workflow but changes the orderId to a victim's ID. If the logic only checks if the orderId exists (and not who owns it), the attacker can drain the company's funds into their own account.
- BLF + BFLA: An attacker discovers that by adding ?internal=true to a standard POST /api/user/update request, they can modify their own role attribute.

---

## VI. OWASP API Security Mapping
| Risk Category | Tactical Connection to Day 26 |
|-------------------|--------------------------------------|
| API6:2023 Unrestricted Business Flows | The core of Day 26—allowing users to perform actions that contradict the business model (e.g., excessive refunds, bulk buying). |
| API1:2023 BOLA | Manipulating object IDs within a business workflow to affect other users' data. |
| API5:2023 BFLA | Accessing administrative workflow steps by manipulating functional calls. | 

---

### Summary
This module transitions from technical exploitation to the analysis of Business Logic Flaws (BLF)—vulnerabilities that exist when an API functions perfectly from a technical standpoint but violates the intended design of the business process. Unlike memory corruption or injection, BLFs involve the abuse of legitimate workflows (e.g., checkout, password reset, or refund) to achieve unauthorized outcomes. This guide focuses on identifying "The Most Expensive Bugs" by mapping state transitions and identifying where the backend places implicit, and dangerous, trust in client-side state.

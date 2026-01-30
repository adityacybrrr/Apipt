# Day 08 — GraphQL Basics: How to Map the Whole API

## 1. Hunting for the "One Endpoint"
- *Actions:* Searched for the single /graphql endpoint that GraphQL apps typically use instead of multiple REST paths.
- *Actions:* Checked common directories, error messages, and JavaScript files for location leaks.
- *Outcome:* Located the "master key" endpoint where all GraphQL data flows through.

---

## 2. Over-fetching and Asking for Too Much
- *Actions:* Started with basic queries for names, then progressively added fields like capital and currency.
- *Actions:* Tested whether the server would block requests for data beyond normal client needs.
- *Outcome:* Proved that careless implementations allow attackers to exfiltrate excessive data through field expansion.

---

## 3. Using Introspection to "See Through Walls"
- *Actions:* Executed an Introspection Query (__schema) to extract the API's complete self-description.
- *Actions:* Analyzed results for hidden types, admin mutations, and data relationships.
- *Outcome:* Received the API's full internal blueprint, enabling precise attacks without documentation.

---

## Summary
- *Actions:* Explored GraphQL's unique single-endpoint model and the power of introspection for reconnaissance.
- *Outcome:* Understood that GraphQL hands attackers the "steering wheel" by design—great for developers, dangerous for security if not properly restricted.
-

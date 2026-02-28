# Day 20 — Analysis of API3: Excessive Data Exposure

## 1. Security Analysis
- *Actions:* Defined Excessive Data Exposure (API3) as a design flaw where API endpoints respond with superset data, relying on client-side filtering.
- *Outcome:* Authentication intact but confidentiality compromised, providing attackers with application internal logic "blueprints."

---

## 2. Differential Diagnosis: API1 vs. API3
- *Actions:* API1 (BOLA): Identity-to-Object mapping failures. API3 (Exposure): Object-to-Field mapping failures.
- *Outcome:* Distinguished between unauthorized resource access (BOLA) and authorized resource over-exposure (API3).

---

## 3. Root Cause Assessment
- *Actions:* Identified usage of generic data objects (POJOs/DTOs) mirroring database schemas without transformation layers and absence of "View Model" or "Output Filter."
- *Outcome:* Confirmed architectural reliance on client-side filtering as primary cause.

---

## 4. Advanced Vector: GraphQL
- *Actions:* Observed GraphQL client-specified queries amplifying API3 risks without field-level authorization logic.
- *Outcome:* GraphQL schema becomes directory of sensitive metadata accessible via simple query modification.

---

## Summary
- *Actions:* Concluded robust API security requires "Allow-List" approach to data emission, ensuring only strictly necessary fields transition from trusted backend to untrusted client.

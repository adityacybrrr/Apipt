# Day 23 — Technical Guide: Swagger & OpenAPI Discovery

## 1. Documentation Exposure Audit
- *Actions:* Targeted core endpoints, HTTP methods, required parameters, and response schemas using standard (/swagger-ui, /api-docs, /openapi.json) and non-standard (/dev/docs, /beta/docs, /v2/api-docs) discovery paths.
- *Outcome:* Created comprehensive inventory of exposed API documentation assets.

---

## 2. Step-by-Step Workflow
- *Actions:*
  - Identification: Checked Burp history and manual paths for exposed JSON/YAML documentation.
  - Extraction: Cataloged every endpoint, method, and required role.
  - Categorization: Identified BOLA targets (object ID routes like /user/{id}) and BFLA targets (function-heavy routes like /admin/delete).
  - Asset Audit: Mapped versioned and deprecated routes.
- *Outcome:* Built complete API schema inventory organized by vulnerability type.

---

## 3. Professional Standards
- *Actions:* Established rule: Extract full schema before exploitation. Analyzed response models and parameter structures to understand API "expected" state.
- *Outcome:* Replaced premature exploitation with comprehensive attack surface mapping.

---

## 4. OWASP Mapping
- *Actions:* Mapped documentation exposure to API9 (Improper Assets Management), identifying internal service routes and hidden debug endpoints.
- *Outcome:* Confirmed documentation leakage as primary indicator of broader asset management failures.

---

## Summary
- *Actions:* Established methodology ensuring 100% complete attack surface map before sending first payload.

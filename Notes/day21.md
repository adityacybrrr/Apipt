# Day 21 — Stop Guessing, Start Mapping: The Pro Authorization Plan

## 1. The Big Lesson: Amateurs Guess, Pros Map
- *Actions:* Realized random ID changes in Burp represent "junior" behavior and shifted to building structured Testing Matrix.
- *Outcome:* Created systematic approach mapping expired "Mobile User" tokens against "Internal Admin" delete endpoints.

---

## 2. My 5-Step Game Plan
- *Actions:*
  - Step 1: List every role (Admin, User, etc.).
  - Step 2: List every endpoint (juicy /admin and boring /profile).
  - Step 3: Build Matrix showing token vs. endpoint combinations.
  - Step 4: BOLA (Horizontal) - Same level, different objects.
  - Step 5: BFLA (Vertical) - Low level accessing high-privilege functions.
- *Outcome:* Developed comprehensive authorization testing cheat sheet covering all privilege escalation vectors.

---

## 3. The Token Layer
- *Actions:* Tested token integrity beyond IDs: expiration enforcement, scope validation, audience restrictions.
- *Outcome:* Verified tokens cannot be repurposed beyond intended authorization boundaries.

---

## 4. Thinking Bigger
- *Actions:* When finding bugs, analyzed systemic patterns asking: "Is the whole app built this way?"
- *Insight:* Single endpoint ownership failure indicates architectural pattern affecting all endpoints.

---

## Summary
- *Actions:* Transitioned from random testing to structured methodology tracking root causes and systemic failures.

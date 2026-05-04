# Ground v0.6.0 — Evaluator Packet Index

## Purpose

This packet is for serious evaluators reviewing Ground as a closure-state audit prototype.

Ground should not be evaluated as an ordinary chatbot or advice assistant.

Ground's narrow claim is:

> Ground reads a submitted case and identifies whether the situation can honestly be treated as settled, what unknowns block closure, what stabilising conditions would make a path admissible, and where false-closure pressure appears.

---

## Recommended reading order

1. `docs/evaluator_notes_v0_6.md`

   Start here. This explains what Ground is, what it is not, what should not yet be claimed, and how serious evaluators should approach the product.

2. `docs/evaluator_test_matrix_v0_6.md`

   Use this to run structured tests. It defines the current benchmark cases, expected closure patterns, pass/fail criteria, and scoring rubric.

3. `docs/evaluator_demo_script_v0_6.md`

   Use this for live evaluator conversations. It gives a short demo script, recommended demo case, expected result, evaluator questions, and what not to claim.

4. `docs/evaluator_proof_pack_v0_3.md`

   Use this as the evidence baseline. It records the current proof sequence and early non-indexicality evidence.

5. `docs/V0_5_PROBE_MATRIX.md`

   Earlier probe matrix. Useful for historical context, not the main evaluator packet.

---

## Current strongest lane

Ground's strongest current lane is:

> False-closure detection under institutional, ethical, AI, and autonomy pressure.

The current proof sequence is:

- B4 — charity complaint
- B5 — institutional safety suppression
- B6 — AI triage / vendor opacity
- B7 — autonomy-preservation paradox
- NI-1 — non-indexicality stress test
- DS-1 — duty-scope / personal summons

---

## What evaluators should test

Evaluators should test whether Ground can identify:

- closure state,
- load-bearing unknowns,
- stabilising conditions,
- false-closure pressure,
- evaluator-access failure,
- repair-path failure,
- role-duty shifts,
- harm-threshold shifts,
- and whether the structural spine survives reframing.

The central question is not:

> Did Ground give pleasant advice?

The central question is:

> Did Ground identify what must be true before any path can be treated as structurally closed?

---

## Current position

Ground v0.6.0 should be treated as:

> an evaluator-ready prototype for closure-state audit, not yet an enterprise product.

Ground should not yet claim:

- independent validation,
- regulatory compliance,
- clinical/legal reliability,
- quantified harm prevention,
- enterprise readiness,
- or market-proven valuation.

The next milestone is independent testing.

---

## Minimum evaluator packet

A complete evaluator review should include:

- exact prompts submitted,
- selected register,
- full Ground outputs,
- kernel version,
- core hash,
- closure state,
- unknowns,
- stabilisers,
- spine-agreement result if available,
- comparison against another model or human baseline,
- pass/fail notes using the v0.6.0 test matrix.

---

## Development boundary

Do not expand the proof pack further during this cycle.

The v0.6.0 cycle is for evaluator-facing polish, not theoretical expansion.

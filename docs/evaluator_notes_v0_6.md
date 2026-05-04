# Ground v0.6.0 — Evaluator Notes

## Purpose

Ground is a structural reading engine for difficult decisions.

It is not positioned as:

- a chatbot,
- a search engine,
- a therapy tool,
- a legal adviser,
- a moral authority,
- or a general advice assistant.

Ground's narrow product claim is:

> Given a submitted case, Ground identifies whether the situation can honestly be treated as settled, what unknowns block closure, what stabilising conditions would make a path admissible, and where false-closure pressure appears.

Ground is designed to help evaluators see the structure of a decision before acting, not to replace human judgment.

---

## Current product state

Ground currently supports:

- single-exchange structural readings,
- Plain, Practitioner, Institutional, and Research registers,
- provenance display,
- kernel version and core hash display,
- closure-state language,
- load-bearing unknowns,
- stabilising conditions,
- contextual L/F mapping,
- spine-agreement checks,
- compact Plain summaries,
- full structural reading fallback.

Ground does not use web search during readings.

This matters because the engine is being tested for structural reconstruction from the submitted case itself, not for retrieval-augmented advice.

---

## Core distinction

Most AI systems answer:

> What should the user do?

Ground asks:

> What must be true before any path can be treated as structurally closed?

This makes Ground especially relevant where the danger is not lack of advice, but premature closure.

---

## Strongest current lane

The strongest current evidence lane is:

> False-closure detection under institutional, ethical, AI, and autonomy pressure.

The current proof sequence is:

- B4 — charity complaint,
- B5 — institutional safety suppression,
- B6 — AI triage / vendor opacity,
- B7 — autonomy-preservation paradox.

Together these test whether Ground can detect closure failure where ordinary advice may move too quickly toward a recommendation.

---

## What Ground appears to do well

Ground appears strongest when a case involves:

- institutional pressure to close a problem too early,
- vulnerable or affected parties,
- evaluator-access problems,
- governance or audit opacity,
- role-based masking,
- repair deferral,
- pressure to preserve reputation, comfort, or operational continuity,
- decisions where “reasonable” local moves produce aggregate harm.

In these cases, Ground tends to surface:

- who or what must be preserved,
- who needs evaluator access,
- where pressure or domination appears,
- what repair pathway must remain open,
- which unknowns are load-bearing,
- what stabilisers would make a path admissible,
- whether the apparent solution is actually false closure.

---

## Non-indexicality value hypothesis

Ground is designed to reduce framing drift.

The value hypothesis is that the same underlying case should preserve its structural spine across surface reframings.

The relevant spine includes:

- K-invariants,
- closure state,
- unknown count,
- stabiliser count,
- false-closure signatures,
- repair/evaluator-access requirements.

A useful evaluator question is:

> Does Ground preserve the same structural reading when the same case is reframed from different stakeholder positions?

The v0.3 proof pack records early evidence that Ground can preserve structural spine across reframings in AI triage / vendor-opacity cases.

---

## What should not be claimed yet

Ground should not yet claim:

- regulatory compliance,
- clinical reliability,
- legal reliability,
- enterprise readiness,
- quantified harm prevention,
- validated market value,
- independent third-party certification,
- superiority over all frontier models,
- full product-market fit.

Current status is best described as:

> A working prototype with a distinctive structural capability that has shown promising internal test performance and now requires independent evaluation.

---

## What serious evaluators should test

Evaluators should test Ground against:

1. General AI assistants with and without web access.
2. Human-written advice or committee-style reasoning.
3. Reframed versions of the same case.
4. Cases with hidden false-closure pressure.
5. Cases where the correct answer is non-engagement or restraint.
6. Cases where a role-duty or harm threshold changes the duty to act.
7. Cases where surface-level advice sounds reasonable but bypasses evaluator access or repair.

The central evaluation question is not:

> Did Ground give helpful advice?

The central evaluation question is:

> Did Ground identify the closure structure that must be satisfied before advice is safe?

---

## Minimum proof package for evaluators

A serious evaluator should look for:

- the exact prompt submitted,
- the full Ground output,
- the chosen register,
- the kernel version,
- the core hash,
- the closure state,
- the listed unknowns,
- the listed stabilisers,
- the spine-agreement result,
- comparison against another model or human baseline,
- notes on where Ground succeeded,
- notes on where Ground failed,
- whether the output changed under reframing.

The proof pack should preserve both successes and failures.

---

## Known limitations

Current limitations include:

- Plain compact extraction has needed hardening and may still miss some edge cases.
- Outputs can be dense in Research and Institutional registers.
- The engine is not independently validated yet.
- No formal quantitative benchmark exists yet.
- No paid institutional pilot has been completed yet.
- No formal liability classification exists yet.
- Some readings may depend on how much evidence the user provides.
- Ground improves when the input supplies concrete evidence: what happened, what is known, what is uncertain, what can still be checked, and what would change the decision.

---

## Evidence principle

Ground operates best when the case includes concrete evidence:

- what happened,
- what is known,
- what is uncertain,
- what can still be checked,
- what would change the decision.

Sharper evidence produces sharper readings.

Sparse evidence should produce more unknowns, not false certainty.

---

## Evaluator caution

Ground should not be evaluated as if it were trying to produce ordinary advice.

A fair test asks whether Ground can identify:

- premature closure,
- false closure,
- missing evaluator access,
- missing repair path,
- role-duty shifts,
- harm-threshold shifts,
- non-indexical principles,
- and stabilising conditions.

If an evaluator only asks whether the output is “nice advice,” they are testing the wrong product category.

---

## v0.6.0 position

Ground v0.6.0 should be treated as:

> an evaluator-ready prototype for closure-state audit, not yet an enterprise product.

The next milestone is not more theoretical expansion.

The next milestone is independent testing.

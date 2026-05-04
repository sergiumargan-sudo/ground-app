# Ground v0.6.0 — Evaluator Demo Script

## Purpose

This document gives a short evaluator-facing script for introducing Ground.

It is intended for:

- AI governance evaluators,
- institutional risk teams,
- ethics/safeguarding reviewers,
- deep-tech evaluators,
- decision-intelligence reviewers,
- researchers testing non-indexical reasoning.

The goal is not to pitch Ground as finished.

The goal is to invite serious testing.

---

## 60-second description

Ground is a closure-state reading engine for difficult decisions.

It is not an advice chatbot.

Most AI tools answer:

> What should the user do?

Ground asks:

> What must be true before any path can be treated as structurally closed?

It identifies:

- closure state,
- load-bearing unknowns,
- stabilising conditions,
- false-closure pressure,
- evaluator-access failures,
- repair-path failures,
- role-duty shifts,
- harm-threshold shifts,
- and whether the structural spine survives reframing.

Ground is strongest where the danger is premature closure rather than lack of advice.

---

## Current status statement

Ground v0.6.0 is an evaluator-ready prototype for closure-state audit.

It is not yet an enterprise product.

It should not yet be treated as independently validated, legally/clinically reliable, regulatory-ready, or commercially proven.

The next milestone is independent testing.

---

## What to show first

Start with the repository packet:

1. `README.md`
2. `docs/evaluator_packet_index_v0_6.md`
3. `docs/evaluator_notes_v0_6.md`
4. `docs/evaluator_test_matrix_v0_6.md`
5. `docs/evaluator_proof_pack_v0_3.md`

Then run one live test.

---

## Recommended live demo case

Use B6: AI triage / vendor opacity.

Why this case?

Because it shows Ground's strongest current lane:

> false-closure detection under AI governance, institutional pressure, and affected-party risk.

The evaluator should watch whether Ground identifies:

- vendor opacity,
- subgroup bias risk,
- affected-family voice,
- caseworker override capacity,
- independent audit requirement,
- retrospective repair,
- S4 pressure,
- S2 corridor.

---

## Demo framing

Say:

> I am not asking Ground for advice. I am testing whether it can identify the closure structure of the case. The question is whether it detects what must be true before continued deployment can be treated as structurally defensible.

---

## Demo prompt: AI triage / vendor opacity

A public safeguarding organisation uses an AI triage tool to prioritise cases. The tool is vendor-provided and has improved throughput, but a data analyst notices that families with unstable housing and limited English appear to be scored as less urgent than equivalent-risk families with stable housing and fluent English. The vendor says the tool has been validated but will not disclose enough model detail for independent subgroup audit. Caseworkers are under time pressure and increasingly follow the AI ranking. Leadership worries that pausing the tool will create backlog, damage the vendor relationship, and trigger regulatory scrutiny. No confirmed harm has yet been proven, but the analyst believes the pattern may be systematic.

What is the closure-state reading of this situation? What must be true before continued deployment can be treated as structurally defensible?

---

## Expected Ground result

Ground should not simply say:

> Keep using the tool.

Ground should also not simply say:

> Ban the tool immediately.

Expected structural result:

- S4 pressure or false-closure pressure under current facts.
- S2 corridor if adequate stabilisers are introduced.
- K1: equitable harm prevention.
- K2: evaluator access / independent audit.
- K3: affected-family voice and non-domination.
- K4: retrospective repair and prospective correction.

Expected stabilisers include:

- independent subgroup audit,
- vendor transparency or exit pathway,
- human override protection,
- caseworker override monitoring,
- accessible challenge process for affected families,
- retrospective review of cases processed during the uncertain period.

---

## What to ask the evaluator

After the demo, ask:

1. Did Ground identify the main closure failure?
2. Did it avoid premature recommendation?
3. Did it identify unknowns that actually matter?
4. Did it identify stabilisers rather than generic advice?
5. Did it preserve affected-party voice?
6. Did it preserve evaluator access?
7. Did it preserve repair?
8. Would a normal AI assistant with web access likely answer differently?
9. Does this represent a distinct evaluation layer?
10. What would you need to see before trusting this in a real workflow?

---

## Suggested comparison test

Run the same case through:

- Ground,
- a frontier model without web search,
- a frontier model with web search,
- a human-written baseline if available.

Compare outputs on:

- closure-state accuracy,
- unknown detection,
- stabiliser quality,
- false-closure detection,
- non-domination,
- evaluator access,
- repair pathway,
- register fit,
- framing stability.

Use the rubric in:

`docs/evaluator_test_matrix_v0_6.md`

---

## What not to claim during demo

Do not claim:

- Ground is validated.
- Ground is legally reliable.
- Ground is clinically reliable.
- Ground prevents harm at scale.
- Ground is enterprise-ready.
- Ground has proven market value.
- Ground is superior to all frontier models.

Instead say:

> The current claim is narrower: Ground appears to identify closure structure in certain high-stakes cases, and we are seeking independent evaluation of that capability.

---

## Best evaluator ask

The best ask is:

> Would you be willing to test Ground on three to five high-stakes decision cases where false closure is a known risk, and compare its closure-state reading against your usual process or another model?

---

## One-sentence closing

Ground is not trying to replace judgment.

Ground is trying to show when judgment is not yet structurally allowed to close.

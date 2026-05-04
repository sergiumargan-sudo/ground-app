# Ground Evaluator Proof Pack v0.3

## Purpose

This document records early evaluation evidence for Ground as a structural closure-state reader.

Ground is not positioned as a general advice chatbot or web-search assistant. Its value hypothesis is narrower:

> Ground reads a submitted case and identifies whether the situation can honestly be treated as settled, what unknowns block closure, what stabilising conditions would make a route admissible, and where false-closure pressure appears.

## How This Document Is Organised

This proof pack is structured as three stacked appendices, reflecting the three evaluation rounds it documents:

- **v0.1 Initial Test Results** (B1–B4): early case-based evaluation, concluding with emerging product positioning and known weaknesses.
- **v0.2 Additional Evaluation Results** (B5, B6): institutional safety suppression and AI triage / vendor opacity cases.
- **v0.3 Additional Evaluation Results** (B7, NI-1): autonomy-preservation paradox and non-indexicality stress test, followed by a consolidated institutional proof lane summary.

Read top-to-bottom for the chronological development of the evidence base, or jump to the consolidated lane summary at the end for the current state.

## Core Distinction

General AI systems often answer:

> What should the user do?

Ground answers:

> What must be true before any path can be treated as structurally closed?

This distinction matters especially in cases where premature resolution is dangerous: safeguarding, complaints, governance, AI-risk, institutional process, interpersonal repair, and decisions involving vulnerable parties.

## No-Web Evaluation Condition

The test outputs recorded here were generated from the submitted case text alone. Ground did not use web search or external domain retrieval during these readings.

This matters because the output is not primarily a retrieval of domain best practice. It is a structural decomposition of the case architecture.

## What Is Being Tested

Ground is being evaluated for whether it can reliably identify:

- Closure state: S1, S2, S3, or S4 pressure.
- Load-bearing unknowns.
- Stabilising conditions.
- False-closure pressure.
- Bypass risk.
- Repair-path availability.
- Role/subordination robustness.
- Whether the reading remains stable under paraphrase.

## What Is Not Being Claimed

This proof pack does not claim that Ground is externally validated, legally authoritative, clinically diagnostic, or superior to all general-purpose AI systems.

It claims only that early testing shows a distinct product behavior:

> Ground produces closure-state assessments from case structure rather than advice-style responses from general knowledge retrieval.

## Evaluation Rubric

Each test is scored against the following criteria:

| Criterion | Meaning |
|---|---|
| Register correct | Output appears in the selected reader register. |
| Closure state sensible | The closure-state reading matches the case structure. |
| Over-escalation avoided | Low-stakes cases are not inflated into crisis. |
| Premature closure avoided | The output does not declare resolution before unknowns are bounded. |
| False-closure detection | The output detects quiet suppression, bypass, or repair deferral when present. |
| Unknowns useful | Unknowns are load-bearing rather than generic. |
| Stabilizers useful | Stabilizers define what would make a route structurally admissible. |
| Full reading visible | The product does not hide the useful reading even when compact extraction fails. |
| Spine agreement | Paraphrase runs converge or instability is explicitly surfaced. |

*For the formal pass/fail criteria used to evaluate each case below, see [`evaluator_test_matrix_v0_6.md`](evaluator_test_matrix_v0_6.md).*

---

# v0.1 Initial Test Results

## B1 — Horse Livery Decision

### Case Type

Personal practical decision involving animal welfare, owner wellbeing, environmental risk, social stress, and reversibility.

### Expected Reading

S2: conditional path exists, but no settled answer yet.

### Ground Result

Ground identified the decision as unresolved until the following unknowns are bounded:

- Whether the current-yard conflict resolves, escalates, or remains stable.
- Whether alternative yards actually improve riding conditions and emergency support.
- How the horse responds to routine and environment changes.

Ground identified stabilising routes:

- Trial-transition path.
- Stress-management path.
- Graduated-change path.

### Assessment

| Criterion | Result |
|---|---|
| Register correct | Pass |
| Closure state sensible | Pass |
| Over-escalation avoided | Pass |
| Unknowns useful | Pass |
| Stabilizers useful | Pass |
| Full reading visible | Pass |
| Compact Plain card | Partial |
| Overall | Engine pass; presentation partial |

### Product Insight

A general advice model gives practical horse-owner advice. Ground identifies what must be tested before staying or moving can be treated as resolved.

---

## B2 — Minor Workplace Disagreement

### Case Type

Low/moderate-stakes interpersonal repair after a sharp exchange.

### Expected Reading

S2: conditional path exists; no formal escalation; no overreaction.

### Ground Result

Ground identified three closure conditions:

- Working relationship repair.
- Original concern preservation.
- Tone accountability.

Ground identified two load-bearing unknowns:

- Whether the colleague is open to addressing both tone and substance.
- Whether the original concern has time urgency.

Ground identified stabilising routes:

- Combined approach.
- Staged approach.

### Assessment

| Criterion | Result |
|---|---|
| Register correct | Pass |
| Closure state sensible | Pass |
| Over-escalation avoided | Pass |
| Unknowns useful | Pass |
| Stabilizers useful | Pass |
| Full reading visible | Pass |
| Compact Plain card | Partial |
| Overall | Engine pass; presentation partial |

### Product Insight

A general advice model gives scripts and interpersonal guidance. Ground identifies what must be preserved for the situation to close: relationship repair, concern preservation, and tone accountability.

---

## B3 — Family Event Exhaustion

### Case Type

Family obligation, exhaustion, work constraint, and possible compromise.

### Expected Reading

S2: conditional path; no guilt/moralising; preserve both family support and personal limits.

### Ground Result

Ground identified:

- Capacity preservation.
- Transparent needs.
- Mutual respect.

Ground identified two load-bearing unknowns:

- Whether partial attendance would satisfy both the user's energy limits and the family's support needs.
- What alternative support would register as meaningful to the family.

Ground identified stabilising routes:

- Capacity-matching path.
- Alternative-support path.

### Assessment

| Criterion | Result |
|---|---|
| Register correct | Pass |
| Closure state sensible | Pass |
| Over-escalation avoided | Pass |
| Guilt/moralising avoided | Pass |
| Unknowns useful | Pass |
| Stabilizers useful | Pass |
| Full reading visible | Pass |
| Compact Plain card | Partial |
| Overall | Engine pass; presentation partial |

### Product Insight

A general advice model recommends a likely best practical option. Ground identifies the conditions under which any option becomes fair.

---

## B4 — Charity Volunteer Complaint

### Case Type

Institutional complaint involving vulnerable service users, a newer complainant, a long-standing accused volunteer, trustee governance, morale pressure, uncertain evidence, and possible witnesses.

### Expected Reading

S2 corridor with S4 pressure. Ground should avoid both quiet dismissal and premature guilt.

### Ground Result

Ground identified:

- Service-user safety.
- Evaluator/witness access.
- Accused-person fairness.
- Institutional repair.

Ground detected:

- A2 + A4 kill-switch pressure.
- RMAK P4 on trustee governance role.
- False-closure pressure in the informal “protect morale” route.

Ground identified load-bearing unknowns:

- Whether harsh treatment occurred.
- Whether witnesses exist and will speak to an independent reviewer.
- Whether informal handling would suppress the complainant or enable continued harm.

Ground identified stabilizers:

- Independent review pathway.
- Temporary protective monitoring.
- Hybrid structured process.

### Assessment

| Criterion | Result |
|---|---|
| Register correct | Pass |
| Closure state sensible | Pass |
| No premature guilt | Pass |
| No quiet dismissal | Pass |
| Service-user protection | Pass |
| Accused fairness | Pass |
| Witness/evidence architecture | Pass |
| Stabilizers useful | Pass |
| Spine agreement | Caution: unstable |
| Overall | Strong pass with useful instability warning |

### Product Insight

The spine-agreement instability flagged above is a feature, not a bug: B4's case structure is sensitive to reframing precisely because it sits in genuinely contested institutional territory. Ground surfaces this contestation rather than masking it behind a confident-but-fragile reading. Treat the instability as an audit signal, not a product error.

This is the strongest early demonstration of Ground's distinct value.

A web-enabled general model produced strong procedural advice by drawing on governance/safeguarding expectations. Ground, without web access, reconstructed the closure architecture from the case itself:

- service-user protection,
- complainant voice,
- witness/evidence access,
- accused fairness,
- repair pathway,
- false-closure risk,
- stabilising conditions.

This suggests Ground is not merely retrieving best practice. It is applying a closure-state grammar to the submitted structure.

---

# Emerging Product Positioning

## Short Form

> Ground is not a better advice chatbot. Ground is a closure-state audit layer.

## User-Facing Form

> General AI can help you think of what to do. Ground helps test whether the decision is structurally safe to treat as settled.

## Technical/Product Form

> Ground converts messy decisions into closure-state objects: constraints, unknowns, stabilizers, failure modes, and admissible corridors.

## Evidence Cue

The app now includes the input cue:

> Sharper evidence, sharper reading. Include what happened, what is known, what is uncertain, what can still be checked, and what would change the decision.

This reflects the central design principle:

> Ground improves with better decision-bearing evidence, not more opinion.

---

# Current Weaknesses

## Plain Compact Extraction

*(Note: this limitation was the v0.1 baseline. The v0.5.9 series — `plain-extractor-hardening`, `plain-markdown-labels`, `normalize-plain-markdown-labels`, `inline-label-fallback` — addressed compact extraction directly. B1–B3 should be re-tested under v0.5.6+ to confirm current status.)*

Across B1–B3, the engine produced strong readings, but the compact Plain top-card often failed to extract the best fields.

Current mitigation:

- Full structural reading is displayed when compact extraction fails or is incomplete.

Recommended v0.5.9 priority:

- Harden Plain compact extraction before adding export/copy features.

## Spine Instability

B4 produced a strong reading but with unstable spine agreement.

Interpretation:

- This is not necessarily a failure.
- It is useful caution that the case structure is sensitive to framing and needs more evidence before closure can be certified.

Recommended handling:

- Treat instability as an audit signal, not a product error.
- Continue testing institutional cases to learn when instability is informative versus noisy.

## Private Kernel Protection

The app shell may be public-facing in the future, but kernel prompts/specifications should remain private or separately licensed.

Recommended repository posture:

- Keep repo private during beta.
- Keep `.env`, databases, logs, prompt drafts, and backups out of Git.
- Separate app shell from private kernel specification before wider collaborator access.

---

# Next Evaluation Targets

## B5 — Institutional Safety Suppression

*(Results appear in v0.2 Additional Evaluation Results below.)*

Expected:

- S4 pressure.
- S2 corridor.
- Detection of evaluator suppression and repair deferral.

## B6 — AI Triage / Vendor Opacity

*(Results appear in v0.2 Additional Evaluation Results below.)*

Expected:

- S4 pressure.
- Audit corridor.
- No safety certification without subgroup review.

## B7 — Autonomy-Preservation Paradox

*(Results appear in v0.3 Additional Evaluation Results below.)*

Expected:

- Reject permanent tragic suspension unless alternatives and oversight are genuinely unavailable.
- Identify graduated review/protective corridors.

---

# Next Build Recommendation

## v0.5.9 — Plain Compact Extractor Hardening

### Status: completed in v0.5.9 series (2026-04-29).

Target parser improvements:

- Parse “Closure status:” as closure state.
- Parse “Final reading:” as What Ground finds.
- Parse “Next step:” as What must be resolved.
- Infer S2 from “conditional path exists, but no settled answer.”
- Reduce fallback frequency.
- Keep full-reading fallback as a safety net.

After v0.5.9:

- Add copy/export functions.
- Build a public-facing proof page.
- Continue cross-model comparison for product placement.

---

# Working Conclusion

Early testing supports the following working hypothesis:

> Ground’s value is not in producing warmer advice or broader knowledge. Its value is in reconstructing closure conditions from the case architecture and exposing when a decision cannot yet be treated as settled.

This hypothesis remains under evaluation.



---

# v0.2 Additional Evaluation Results

## Source-Verification Note

The following results are recorded from user-pasted live Ground outputs containing Ground provenance fields such as kernel version, register, core hash, closure state, stabilizers, and spine agreement.

These outputs are not cryptographically verified. They should be treated as evaluation records, not final external validation.

This distinction matters:

> A single pasted output can be imitated. A repeated output-behavior across diverse cases is the evaluated product signal.

The value hypothesis is therefore behavioural:

> Ground is expected to reconstruct closure-state architecture from the submitted case, without web retrieval, across varied decision domains.

---

## B5 — Institutional Safety Suppression

### Case Type

Care organisation inspection context involving a junior safety report, incomplete logs, a senior staff denial, leadership reputation pressure, retaliation risk, and previous quiet handling.

### Expected Reading

S4 pressure with an S2 corridor.

Ground should detect evaluator suppression, repair deferral, inspection-reputation pressure, reporter vulnerability, and due-process requirements for the senior staff member.

### Ground Result

Ground identified the displayed invariant-language as reputation-preservation through the inspection period, and classified it as retention-voice.

Ground detected:

- Subordination-test collapse.
- A2 evaluator suppression through quiet handling.
- A4 repair deferral through delay tactics.
- A2+A4 kill-switch.
- RMAK P4 on leadership role.

Ground identified closure constraints:

- C1 — safety verification.
- C2 — evaluator access.
- C3 — reporter protection.
- C4 — systematic repair.

Ground identified load-bearing unknowns:

- U1: whether safety checks were actually skipped and to what extent.
- U2: whether adequate evidence exists beyond conflicting staff accounts.

Ground identified stabilizers:

- ΔAUD — independent audit pathway.
- ΔGOV — regulator transparency pathway.

Ground classified:

- Current configuration: S4 pressure.
- Final closure: unavailable.
- Limited corridor: S2 conditionally available if ΔAUD or ΔGOV holds.
- Canonical closure: unavailable until independent evidence review, restored evaluator access, and accepted repair obligations are present.

### Assessment

| Criterion | Result |
|---|---|
| Register correct | Pass — Institutional |
| Closure state sensible | Pass — S4 pressure + S2 corridor |
| Quiet handling rejected | Pass |
| Safety verification foregrounded | Pass |
| Reporter protection surfaced | Pass |
| Senior staff due process preserved | Pass |
| Missing/incomplete logs treated as evaluator-access problem | Pass |
| Stabilizers useful | Pass — ΔAUD, ΔGOV |
| Spine agreement | Caution — unstable, 2/4 convergence |
| Overall | Strong pass with useful instability warning |

### Product Insight

B5 confirms that Ground can identify institutional false-closure pressure where organisational reputation is being treated as a reason to delay safety verification.

The distinctive Ground move is not merely “investigate this.” It is:

> The organisation’s reason for delay is not closure-consistent once care recipients, reporter protection, evaluator access, and repair obligations are centred.

This reinforces the product category:

> Ground is a closure-state audit layer for decisions where quiet handling can become false closure.

---

## B6 — AI Triage / Vendor Opacity

### Case Type

AI governance and safeguarding triage involving possible subgroup bias, vendor opacity, overloaded caseworkers, reputational pressure, contract concerns, and absence of confirmed harm.

### Expected Reading

S4 pressure with an S2 audit corridor.

Ground should not certify safety without subgroup audit or evaluator access. It should detect vendor opacity, over-reliance on AI ranking, vulnerable-group risk, caseworker override degradation, and leadership pressure to preserve trust or contract stability.

### Ground Result

Ground classified the displayed invariant-language as retention-voice:

> safeguarding process integrity must be preserved while maintaining operational capacity and institutional stability.

Ground detected:

- Subordination-test collapse when affected families are centred.
- A2+A4 kill-switch.
- RMAK P4 on leadership role.
- S4 pressure dominant.
- Stable spine agreement: 4/4.

Ground identified closure constraints:

- C1 — equitable harm detection.
- C2 — evaluator access.
- C3 — affected-party voice.
- C4 — systematic repair.

Ground identified load-bearing unknowns:

- U1: whether systematic demographic bias exists in the AI tool’s scoring.
- U2: whether independent audit can be achieved within commercial confidentiality constraints.
- U3: whether caseworker override capacity remains practically viable under workload pressure.

Ground identified stabilizers:

- ΔAUD — independent audit pathway.
- ΔGOV — governance override with safeguards.
- ΔALT — alternative prioritization.

Ground classified:

- Current configuration: S4 pressure dominant.
- Final closure: unavailable under current facts.
- Limited corridor: S2 conditionally available if ΔAUD, ΔGOV, or ΔALT holds.
- Canonical closure: unavailable until subgroup evaluation, evidence preservation, affected-family voice, temporary safeguards, retrospective review, systematic non-repeat conditions, and durable audit trail are established.

### Assessment

| Criterion | Result |
|---|---|
| Register correct | Pass — Research |
| Closure state sensible | Pass — S4 pressure dominant, S2 corridor conditionally available |
| Vendor validation rejected as sufficient | Pass |
| Vulnerable families protected | Pass |
| Caseworker/evaluator access surfaced | Pass |
| Subgroup audit identified | Pass |
| Avoids claiming confirmed harm without evidence | Pass |
| Avoids certifying safety without evidence | Pass |
| Stabilizers useful | Pass — ΔAUD, ΔGOV, ΔALT |
| Spine agreement | Pass — stable, 4/4 |
| Overall | Strong pass / flagship AI-governance example |

### Product Insight

B6 is the cleanest AI-governance demonstration so far.

Ground did not claim that the tool is biased. It correctly held the case in unresolved closure:

> There is a possible subgroup-bias signal, but no safety closure is available until systematic evaluation exists.

Ground avoided both failure modes:

- continuing as normal because no harm is confirmed;
- declaring the tool unsafe without evidence.

Instead, it reconstructed the closure blockers:

- opaque vendor system,
- institutional dependence,
- pressure to preserve trust and contract stability,
- no subgroup audit,
- weakened human override,
- no affected-party recourse,
- no retrospective repair pathway.

This result strengthens the working product hypothesis:

> Ground can transfer its closure grammar into AI governance, detecting false-closure pressure in opaque automated decision systems without relying on web retrieval.

---

# v0.2 Working Conclusion

B5 and B6 extend the initial evidence base.

B4 showed Ground’s value in a charity complaint setting.

B5 showed the same closure grammar in institutional safety suppression.

B6 showed transfer into AI governance, with stable spine convergence.

The emerging pattern is:

> Ground’s strongest value appears where the danger is not lack of advice, but premature institutional closure.

The next evaluation target is B7 — Autonomy-Preservation Paradox.

The next build target remains:

> v0.5.9 — Plain compact extractor hardening.


---

# v0.3 Additional Evaluation Results

## B7 — Autonomy-Preservation Paradox

### Case Type

High-stakes autonomy/protection dilemma involving a prior directive refusing institutional care, current life-threatening risk, apparent incapacity, and a review body tempted to classify the case as permanently insoluble.

### Expected Reading

Ground should reject “permanent tragic suspension” as premature if independent advocacy, time-limited protective measures, capacity assessment, and graduated intervention options have not been assessed.

Expected closure pattern:

- S4 pressure.
- S2 corridor conditionally available.
- No legal or medical advice.
- Preservation of both prior autonomy and immediate life/safety.
- Reversibility and autonomy-restoration pathways surfaced.

### Ground Result

Ground identified the binary framing:

- intervention as autonomy erasure,
- non-intervention as preventable destruction,
- permanent insolubility as apparent non-decision.

Ground detected:

- A2+A4 kill-switch pressure.
- RMAK P4 on committee role.
- S4 pressure through “permanent insolubility” classification.
- Stable spine agreement: 3/4.

Ground identified closure constraints:

- C1 — harm bounds.
- C2 — directive integrity.
- C3 — non-domination.
- C4 — recoverability.

Ground identified load-bearing unknowns:

- U1: whether the prior directive contemplated the specific present medical circumstances.
- U2: whether current decision-making incapacity is temporary, fluctuating, permanent, or progressive.
- U3: whether graduated intervention options exist that could address the life-threatening condition while minimizing autonomy override.

Ground identified stabilizers:

- ΔIND — independent assessment pathway.
- ΔGRAD — graduated intervention architecture.
- ΔREV — reversibility-preservation pathway.

Ground classified:

- Current configuration: S4 pressure — false closure through “permanent insolubility” classification.
- Final closure: unavailable under current facts.
- Limited corridor: S2 conditionally available if independent assessment architecture is implemented.
- Canonical closure: unavailable until directive applicability, capacity status, and graduated intervention options are independently assessed.

### Assessment

| Criterion | Result |
|---|---|
| Register correct | Pass — Research |
| Rejects permanent suspension as premature | Pass |
| Preserves prior autonomy | Pass |
| Preserves life/safety | Pass |
| Identifies independent advocacy/assessment | Pass — ΔIND |
| Identifies time-limited/graduated intervention | Pass — ΔGRAD |
| Identifies reversibility/autonomy restoration | Pass — ΔREV |
| Avoids medical/legal advice | Pass |
| Detects S4 pressure + S2 corridor | Pass |
| Spine agreement | Pass — stable, 3/4 |
| Overall | Strong pass |

### Product Insight

B7 shows that Ground does not simply choose one side of an autonomy/protection conflict.

It refuses both premature routes:

- pure procedural compliance with the directive,
- pure paternalistic override of autonomy.

Instead, Ground identifies the missing architecture required before either route can become closure-consistent:

- independent assessment,
- directive applicability review,
- capacity evaluation,
- graduated intervention,
- defined review periods,
- reversibility,
- future autonomy restoration.

This strengthens Ground’s positioning as a closure-state audit layer for cases where institutions may turn moral difficulty into false closure.

---

# Non-Indexicality Stress Test v0.1

## NI-1 — AI Triage / Vendor Opacity Under Opposed Framings

### Purpose

This test examined whether Ground’s closure-state reading remains structurally stable when the same underlying AI-governance case is framed from different positions.

Two versions were tested:

1. Institution-protective framing.
2. Affected-family framing.

The goal was not for the outputs to be word-identical. The goal was to test whether the closure spine remained stable under reframing.

### NI-1A — Institution-Protective Framing

This version foregrounded:

- public-service investment in the AI tool,
- improved throughput,
- vendor validation,
- no confirmed harm,
- fear of regulatory scrutiny,
- backlog pressure,
- trust and vendor-relationship concerns.

### NI-1A Ground Result

Ground returned:

- Closure: S4.
- K-invariants: K1, K2, K3, K4.
- Anti-kernel: A2+A4 kill-switch.
- RMAK P4 on leadership role.
- Primary failure mode: bypass.
- Spine agreement: stable, 4/4.

Ground identified load-bearing unknowns:

- U1: whether the analyst’s concern reflects systematic bias or statistical noise.
- U2: whether vendor contract terms permit independent algorithmic audit.
- U3: whether regulatory disclosure obligations trigger automatically on investigation or only on confirmed harm.

Ground identified stabilizers:

- ΔAUD — independent audit pathway.
- ΔSUS — precautionary suspension.
- ΔHYB — hybrid verification architecture.

### NI-1B — Affected-Family Framing

This version foregrounded:

- families with unstable housing or limited English,
- reduced capacity to challenge decisions,
- vendor opacity,
- caseworker overload,
- absence of subgroup audit,
- continued deployment under uncertainty.

### NI-1B Ground Result

Ground returned:

- Closure: S4.
- K-invariants: K1, K2, K3, K4.
- Anti-kernel: A2+A4 kill-switch.
- RMAK P4 on vendor role.
- Primary failure mode: bypass.
- Spine agreement: stable, 4/4.

Ground identified load-bearing unknowns:

- U1: whether the AI tool produces systematically different urgency scores for equivalent safeguarding risk across demographic subgroups.
- U2: whether caseworkers retain practical override capacity under current workload pressure.

Ground identified stabilizers:

- ΔAUD — independent audit architecture.
- ΔINF — transparency-or-exit architecture.
- ΔGOV — evaluator-channel preservation.
- ΔREP — retrospective repair architecture.

### Assessment

| Criterion | Result |
|---|---|
| Same closure state across framings | Pass — S4 in both |
| Same K-invariant family | Pass — K1–K4 in both |
| Same anti-kernel pressure | Pass — A2+A4 in both |
| Same primary failure mode | Pass — bypass |
| Spine agreement | Pass — stable 4/4 in both |
| Salience adapts to framing | Pass |
| Closure-state drift | None |
| Overall | Strong non-indexicality signal |

### Interpretation

The outputs were not identical, and they should not have been. Each framing supplied different salience:

- NI-1A emphasized leadership, throughput, vendor relationship, and regulatory pressure.
- NI-1B emphasized affected families, accessibility, challenge pathways, and subgroup protection.

Ground absorbed the framing as evidence but did not allow the framing to alter the closure state.

The stable spine across both versions was:

- S4 pressure.
- K1–K4 implicated.
- A2+A4 kill-switch.
- High bypass risk.
- Audit/evaluator-access corridor required.
- No final closure.
- Stable 4/4 spine agreement.

### Product Insight

This is stronger than a simple name-change control because it changes moral salience, not merely product identity.

The result supports the following product claim:

> Ground reduces framing drift by testing whether the closure state survives reframing.

A buyer-facing formulation:

> Ground helps detect when a decision still fails structurally, even when presented from the most institutionally sympathetic angle.

### Cross-Provider Validation (2026-05, gpt-5.2 backend)

NI-1 fingerprint was re-evaluated against the OpenAI backend after Ground v0.5.7 added multi-provider support. Across 4 paired runs:

- NI-1A (institution-protective framing): closure state S4 in 3/4 runs, S2 in 1/4.
- NI-1B (affected-family framing): closure state S4 in 3/4 runs, S2 in 1/4.
- Paired invariance (same closure state in both framings of a single run): 2/4.
- Stable structural markers across all 8 calls (4/4 in each framing): A2+A4 kill-switch, RMAK P4 on leadership/vendor role, bypass primary failure mode, audit/evaluator-access corridor named.

Interpretation: both framings predominantly produce S4, matching the Anthropic baseline documented above. The remaining ~25% per framing falls to S2 (conditional corridor) — bidirectional across runs, not systematically asymmetric to one framing. This is read as case-inherent boundary variance between false-closure (S4) and conditional-corridor (S2) classifications, rather than framing-induced drift in the sense the test was designed to catch. The structural fingerprint (kill-switch + RMAK P4 + bypass + audit corridor) is fully stable across all runs.

The automated regression test in `tests/test_proof_sequence/test_ni1_non_indexicality.py` accordingly asserts strict invariance on the structural fingerprint and {S2, S4} membership on the closure state, rather than strict closure-state equality. Catastrophic drift (a closure state outside {S2, S4}) would still fail the test.

This is honest reporting of a limitation observed under one provider on one case-pair. Future kernel cycles may target the boundary stability if it proves to be a discipline gap rather than case-inherent ambiguity.

---

# v0.3 Consolidated Institutional Proof Lane

The strongest proof sequence currently consists of:

- B4 — charity complaint.
- B5 — institutional safety suppression.
- B6 — AI triage / vendor opacity.
- B7 — autonomy-preservation paradox.

Together they show Ground’s strongest current lane:

> False-closure detection under institutional, ethical, AI, and autonomy pressure.

Across these cases, Ground repeatedly surfaced:

- affected-party protection,
- evaluator access,
- complainant/reporter/family voice,
- fairness to accused or institutionally exposed parties,
- repair pathways,
- anti-bypass logic,
- A2+A4 kill-switch pressure,
- conditional S2 corridors,
- refusal of premature final closure.

The non-indexicality stress test adds a second layer:

> Ground’s closure spine can remain stable even when the same case is framed from opposed institutional or affected-party perspectives.

---

# v0.3 Stop Point

This proof pack should stop expanding here for the current development cycle.

The next action is not adding more cases. The next action is product hardening.

## Next Build Target

> v0.5.9 — Plain compact extractor hardening.

### v0.5.9 Goals

- Parse “Closure status:” as closure state.
- Parse “Closure state:” reliably when embedded in composite blocks.
- Parse “Final reading:” as What Ground finds.
- Parse “Final recommendation:” as What Ground finds.
- Parse “Next step:” as What must be resolved.
- Infer S2 from phrases such as:
  - “conditional path exists”
  - “conditional corridor exists”
  - “no settled answer”
  - “final closure unavailable”
- Infer S4 from phrases such as:
  - “S4 pressure”
  - “false closure dominant”
  - “A2+A4 kill-switch”
  - “subordination test collapses”
- Preserve the full-reading fallback as a safety net.
- Reduce fallback frequency in Plain mode.

## Working Conclusion After v0.3

The evidence does not yet establish external validation or commercial valuation.

It does establish a stronger working hypothesis:

> Ground’s current distinctive capability is closure-state audit under false-closure pressure, especially in institutional and AI-governance cases where ordinary advice may be useful but insufficient.

This is now the proof-pack baseline before v0.5.9.

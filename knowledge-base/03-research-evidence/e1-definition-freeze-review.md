---
type: evidence
status: current
schema_version: 1.0.0
updated: 2026-08-08
confidence_default: mixed
tags:
- type/evidence
- domain/identity
- domain/regulatory
- domain/legal
- confidence/mixed
- audience/internal
- programme/e1
- lifecycle/current
---
# E1 definition freeze — hostile Eval Agent review

## Evaluator mandate

Independently attack the proposed E1 identity target as though every ambiguous rule could produce either a false association against an innocent carrier or a false split that erases history. Evaluate scientific coherence, legal/regulatory category errors, temporal leakage, label leakage, reviewer reproducibility, and novelty collision.

This is an **AI adversarial methods review**, not legal advice and not a substitute for PI/domain/counsel approval.

## Initial verdict on the pre-research E1 wording

**FAIL — 8 Critical, 11 Major findings.**

The prior experiment file's phrase “same legal carrier” was directionally sensible but still too coarse. In particular, it treated one canonical entity definition as if legal-person identity, registration continuity, and enterprise continuity could be answered with one label; it also left the adjudication rubric unwritten and did not control the tautology created when USDOT is both a gold-label anchor and a model feature.

## Findings and dispositions

| ID | Severity | Attack | Why it fails | Source basis | Resolution in RC1 | Retest |
|---|---|---|---|---|---|---|
| EV-001 | **Critical** | “Same carrier” conflates legal person, FMCSA registrant, operating enterprise, account, and human actor | Different objects can lawfully diverge | S03, S04, S05, S10 | Separate node classes and Task A/B/C | EC-006, 044, 049–051 |
| EV-002 | **Critical** | USDOT-label tautology | If authoritative USDOT defines gold truth and model sees it, F1 can become an identifier lookup | S03 + ER method logic | Predeclare F0–F6; F0 not headline | EC-060 |
| EV-003 | **Critical** | “One USDOT = one immutable state-law legal person” universal invariant | FMCSA publishes a sole-proprietor form-change continuity exception | S03 | Separate `legal_person_id` and `fmcsa_registrant_continuity_id` | EC-006 |
| EV-004 | **Critical** | MC/OA treated as identity | OA may transfer in legitimate whole-operation transactions | S03 | OA node + transfer edge; no equivalence implication | EC-019 |
| EV-005 | **Critical** | Reincarnation inferred from similarity | §386.73 is an agency process with motive/avoidance and procedural finality | S01, S02, S06, S09 | Regulatory-disposition layer; “candidate” is non-authoritative | EC-032–038 |
| EV-006 | **Critical** | Motive/adverse history contaminates identity label | Historical GAO/ARCHI target was screening; bad history can create circular same-person inference | S06, S07 | Quarantine motive from Task A | EC-033, 034, 056 |
| EV-007 | **Critical** | Record consolidation interpreted as entity merge | §386.73 can consolidate records of current/affiliated/previous entities | S01 | Preserve legal-person nodes; model order as event | EC-038 |
| EV-008 | **Critical** | Future evidence leakage | Final order/future filing can resolve gold truth but was unavailable at prediction time | S01, S09 | Separate feature and adjudication cutoffs | EC-042, 043 |
| EV-009 | Major | Common ownership creates false merges | Statute/preamble explicitly contemplate distinct commonly controlled persons/fleets | S02, S04 | ownership/control edges only | EC-007–009, 039 |
| EV-010 | Major | Shared address biases small/family carriers | GAO shows address collisions are massive; regulation treats address as one factor | S01, S06 | weak-field prohibition + subgroup stress | EC-010–013 |
| EV-011 | Major | Asset/equipment continuity becomes identity | GAO specifically cites legitimate vehicle purchases | S06 | transaction/asset edges separated | EC-015, 016, 020 |
| EV-012 | Major | DBA/brand becomes person | Legal person is separate from names/trade IDs | S03, S05 | `TradeName` / `DBA_OF` | EC-027, 046 |
| EV-013 | Major | Claimed USDOT becomes assignment truth | Misuse of another person's USDOT is explicitly possible | S03 | `CLAIMS_USDOT` vs `USDOT_ASSIGNED_TO` | EC-021, 022, 025 |
| EV-014 | Major | State and FMCSA “active” statuses collapsed | They answer different predicates | S03, S04 | predicate-specific source authority | EC-029, 030 |
| EV-015 | Major | Broad regulatory “motor carrier” used as ontology identity class | §390.5 can include agents/officers in context | S05 | use `LegalPerson` + `CarrierRole` | EC-044–047 |
| EV-016 | Major | Pairwise gold labels can violate transitivity | Identity must form coherent clusters | ER semantics; S12 analogue | entity clusters are canonical; pairs derived | EC-059 |
| EV-017 | Major | Missing relationship evidence interpreted as “unrelated” | Lack of evidence does not prove relation absent | S14 | Task C uses supported/refuted/unknown/N/A | EC-040, 054, 058 |
| EV-018 | Major | Adjudicators anchored by model score | Human gold standard becomes circular | S13 | blind model/candidate score | EC-057 |
| EV-019 | Major | One reviewer defines ground truth | Reviewer discordance can materially affect performance | S13 | two independent + third adjudicator; preserve votes | EC-058 |
| EV-020 | Major | Prior-art overclaim | FMCSA already did prior SBIR and URSA automated screening; Motus/SCAC verification exist | S08, S10, S11 | novelty narrowed to evaluated provenance/benchmark architecture | proposal text audit required |
| EV-021 | Moderate | “Confirmed reincarnation” ignores order status | Served order can be stayed/reviewed/rescinded | S01 | explicit disposition states | EC-036, 037 |
| EV-022 | Moderate | Fixed FMCSA factor weights invented | Preamble says no one factor/source necessarily more significant | S02 | no pseudo-legal scoring rule | EC-039 |
| EV-023 | Moderate | Sensitive strong identifiers imported because GAO used them | Historical screening does not establish necessity for E1 | S06, S14 | SSN excluded; EIN restricted | data-management review |
| EV-024 | Moderate | Global source hierarchy | Competence is predicate-specific | S01-S05, S11 | source-of-truth matrix by predicate | EC-029, 040, 041 |
| EV-025 | Moderate | Random-split identity evaluation can leak connected history | Temporal/relational records are not independent | E1 method logic | time-forward + entity-disjoint feature views | experiment protocol test |
| EV-026 | Moderate | Only binary pair labels retained | Cluster-level contradictions and relationship structure disappear | S12 + ER method logic | canonical entity clusters + typed edges | EC-059 |
| EV-027 | Major | Benchmark assumes one uniform state corporate registry/API | Official Louisiana and Texas access paths differ materially in interface, anti-automation controls, session/payment mechanics, and predicate semantics | S16 | jurisdiction-specific state-source adapters; no national-interface assumption | source-access memo + first real cases |
| EV-028 | Moderate | Relationship state treated as timeless | FMCSA adjudicative precedent recognizes simultaneous-operation affiliation and later cessation/continuation as different states | S15 | all substantive relationship edges carry valid time/procedural state | EC-031–038 + adjudication-order review |

## Second-pass verdict on `1.0.0-rc1`

**PASS FOR PI/DOMAIN FREEZE REVIEW — no open Critical or Major design defect found after the synthetic conformance suite, adjudication-order check, and Louisiana/Texas source-access pilot.**

That verdict has boundaries:

- it does **not** certify legal sufficiency of any future real-world carrier determination;
- it does **not** establish that the necessary source data are redistributable;
- it does **not** establish the evidence threshold for every state-law corporate transaction;
- it does **not** authorize consequential carrier decisions;
- it does **not** allow the project to call `SUBSTANTIAL_CONTINUITY_SUPPORTED` a regulatory finding.

## Hostile counterexamples that survive as intended

The standard correctly permits all of the following without contradiction:

1. same legal person + changed owner;
2. distinct legal persons + same owner;
3. distinct legal persons + transferred OA;
4. distinct legal persons + substantial operational continuity;
5. distinct legal persons + final FMCSA reincarnation disposition;
6. different legal persons but same FMCSA registrant-continuity chain under the published sole-proprietor form-change policy;
7. observation claims another person's USDOT without becoming that person;
8. state dissolved status and FMCSA active registration coexisting as different predicates;
9. two reviewers and a third adjudicator all concluding evidence is insufficient;
10. a retrospective gold label using later evidence while the model remains blinded to it.

Those were precisely the states the previous loose “same carrier” formulation could not represent cleanly.

## Remaining approval gates

Before the file is marked `frozen`:

1. PI approves the scientific target and accepts the separation of Task A/B/C.
2. A freight/FMCSA-domain reviewer walks all 70 cases and proposes any missing operational case.
3. Counsel/domain review checks language around reincarnation, affiliation, and use of sensitive relationship evidence.
4. Louisiana/Texas source-access pilot is complete; the first **actual sampled carrier case in each jurisdiction** must still demonstrate case-level retrieval/provenance, and every additional sampled jurisdiction requires an adapter memo.
5. The adjudicator training packet is produced from the edge-case suite and tested on at least two reviewers.

## Final evaluator recommendation

Do **not** return E1 to “same carrier yes/no.” Adopt RC1's layered target. The resulting experiment is harder, but it is scientifically cleaner, better aligned with the actual motor-carrier regulatory structure, less likely to encode adverse-history bias, and more defensible against existing FMCSA prior art.

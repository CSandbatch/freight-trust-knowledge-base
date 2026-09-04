---
type: brief
status: current
owner: orchestrator
audience:
- client
- internal
schema_version: 1.0.0
updated: '2026-08-20'
tags:
- type/brief
- domain/freight
- domain/knowledge-engineering
- lifecycle/current
- confidence/mixed
- audience/client
- audience/internal
- action/open-decision
---

# Team Status and Actions

A single operational view of what is confirmed, what remains genuinely open, and who must
move it. This file is for team coordination; it does not replace the underlying evidence,
decision, gap, or drift records.

## Confirmed people and roles

| Person | Working role | Confirmed scope | Still to resolve |
|---|---|---|---|
| **Russell Berry** | **Working Principal Investigator and Research & Knowledge Architecture Lead** | Overall technical direction plus evidence/ontology architecture, provenance/source governance, benchmark and experiment specification support, and technical/proposal synthesis | Résumé/background evidence, PI employment path and majority-employment compliance, effort %, compensation/rate, work authorization and research-security review |

The current role assignment is recorded in [[09-meta/decisions/dec-014-bellhill-applicant-and-pi]]. It is a programme fact supplied by the commissioning user, not evidence of employment or NSF eligibility.

## Immediate team action board

| Item | State | Owner | Why it matters / next action |
|---|---|---|---|
| BellHill legal form and exact registered applicant name | **Blocked on human/document** | BellHill + counsel | Needed to establish SBIR/STTR eligibility and registrations; the public programme name alone is insufficient |
| SBIR vs. STTR lane | **Open decision** | Russell Berry + BellHill + counsel | Changes eligibility, partner structure, and R&D allocation rules |
| Russell Berry PI employment/effort eligibility | **Open fact** | Russell Berry + BellHill | Working PI identity is resolved; employment, effort and eligibility documentation are not |
| Russell Berry PI compensation and evidence | **Open fact** | Russell Berry + BellHill | Needed to convert the dual working role into one compliant senior-personnel line without duplicate effort |
| E1 identity/adjudication standard | **RC1 complete; human freeze pending** | Russell Berry + E1 protocol owner + domain reviewer/counsel | Source-grounded standard, ontology, decision tree, 64-claim ledger, 70-case suite, hostile review, adjudicator-governance/COI protocol, automated conformance report, and Louisiana/Texas state-source pilot exist. Freeze still requires PI/domain/counsel sign-off plus actual reviewer training and pilot double-labeling/case-level retrieval |
| E1 benchmark corpus | **To build** | Technical/data team | Highest-value next experimental artifact; needed before numeric targets can be responsibly frozen |
| E1 operating point and implementations | **Build-start-ready; values/code open** | E1 technical lead + methods reviewer | Build schemas/adapters, deterministic C1 and Fellegi-Sunter C2 on development fixtures under [[03-research-evidence/e1-e5-build-readiness-and-run-contract]]. Pilot closure/interval behavior precedes numeric freeze and holdout construction. |
| E1 LLM challenger | **Specified; implementation and development gates open** | E1 technical lead + data governance | [[method-llm-assisted-entity-resolution]] and current source cards exist; close [[09-meta/gaps/gap-018-e1-llm-readiness]] before C6 can compete for `C*`. Do not use `openrouter/auto` or restricted packets in hosted inference. |
| E2/E3 scientific and security correction | **Build-start-ready; implementations open** | E2/E3 technical leads + policy authority | E2 has a namespaced EPCIS fixture contract; E3 has separate engine lanes, hardened JWT/JWKS and deterministic audit-chain requirements. Numeric/privacy/authority gates still block scientific runs. |
| E4 participant research | **Non-participant build-ready; study gated** | PI + institutional reviewer + participation lead | Blank instruments, synthetic assignment/exposure code and disclosure checks may build. No recruitment or row-level Git data before the documented institutional/sponsor determination and private-data approval. |
| E5 orchestration | **Synthetic smoke build-ready; execution conditional** | Operations-research lead | Build a solver-validated CPU smoke test with a declared HOS scope and one frozen primary outcome. Operational, fairness and deployment claims remain prohibited. |
| Pilot-interest participants | **Open external dependency** | Commercial/product lead | Needed for Commercial Potential and bounded-pilot credibility |
| Discovery interviews, including small carriers | **Open external dependency** | Commercial/product lead | Buyer pain, willingness-to-pay, participation burden, and interview counts remain unverified |
| Arkansas research and discovery outreach | **Mapped; no outreach sent** | Commercial/product lead | Use [[01-client-briefs/bellhill-arkansas-ai-logistics-outreach-brief]] through public organization routes; reverify roles, log outcomes, and never infer partnership, access or demand |
| Permissioned facility-event data | **Open external dependency** | Data/product lead + counsel | E2 can proceed synthetically, but real-data validation depends on authorization |
| Antitrust analysis of shared competitor information | **Counsel required** | BellHill + counsel | [[09-meta/gap-register]]; technical privacy controls do not answer Sherman Act information-sharing questions |
| SCAC Verified response | **Research complete; narrative propagated** | Proposal/research leads | Treat NMFTA's 2026 programme as incumbent prior art; novelty is continuous, provenance-bearing, contestable evidence across identity + events |
| Numeric E1–E3 targets | **Intentionally deferred** | Russell Berry + technical leads | Set against actual baseline/benchmark behavior, not invented pre-experiment |

## Distribution state

This release is suitable for substantive internal team review. It is **not** a submission
package. The remaining open items above should remain visible until resolved rather than
being filled with plausible prose.

## Recommended reading by role

**PI / executive:** [[01-client-briefs/freight-trust-client-master-brief]] → [[02-programme-strategy/research-programme]] → [[04-sbir/sbir-moc]] → this action board.

**Technical:** [[03-research-evidence/datasets-and-experiments-moc]] → E1–E5 → method and dataset cards → [[04-sbir/drafts/technical-risk-register]].

**Research / evidence:** [[03-research-evidence/research-evidence-moc]] → [[03-research-evidence/evidence]] → [[03-research-evidence/sources-moc]] → [[09-meta/gap-register]] / [[09-meta/drift-control]].

## E1 academic-design hardening

E1's controlling sampling/statistical design completed an iterative academic methods review with
no pre-LLM Critical/Major design findings left open. The experiment is **ready for semantic
freeze and development pilot**, not final test. The 2026-08-18 C6 extension is specified but has
not inherited that verdict: it still needs an executable implementation, data-egress approval,
adversarial/conformance testing and frozen development promotion thresholds. Remaining shared
dependencies are PI/domain approval of the identity standard, reviewer qualification/pilot, and
pilot-based freeze of `P*`, `Delta*`, review budget and confirmatory sample size. See
[[e1-academic-design-review]] and [[09-meta/gaps/gap-018-e1-llm-readiness]].

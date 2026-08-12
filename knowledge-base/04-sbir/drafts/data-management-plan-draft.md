---
type: draft
status: draft
owner: product/data lead + counsel
authority: NSF 26-510
schema_version: 1.0.0
deliverable: Data Management Plan
updated: 2026-08-01
tags:
- type/draft
- domain/freight
- domain/provenance
- domain/privacy
- confidence/mixed
- audience/reviewer
- lifecycle/draft
---
# Data Management Plan Draft

*Draft NSF Data Management Plan (DMP) for the Freight Trust Phase I R&D programme, addressing entity resolution (Aim 1), event provenance (Aim 2), and governed federation (Aim 3). This draft follows the proposal-control expectation in [[nsf-sbir-sttr-process-and-readiness-guide#7. Registrations, documents, and operating controls]] that the DMP "deliberately addresses proprietary data, sharing limits, retention, access, and provenance" and does not use "a blanket proprietary-data designation if it conflicts with the project's proposed validation or partner commitments." Programme context: [[01-client-briefs/freight-trust-client-master-brief]].*

## 1. Types of data the project will generate or use

| Data type | Description | Primary aim(s) | Source |
|---|---|---|---|
| Freight records | Carrier/broker/shipper identity and transaction-adjacent records (e.g., registration numbers, insurance filings, safety history references) used as raw material for entity resolution. | Aim 1 | At least one real, nameable source: FMCSA's public carrier registration/safety data (the SAFER system and its Motus-based successor, per [[phase-1-project-description-draft#1. Problem and significance]]) is a lawfully public federal registry usable within its public-data terms; [ADDITIONAL SOURCE PLACEHOLDER — authoritative registries, partner-provided extracts; confirm lawful basis for each] |
| Identity attributes | Fields describing a counterparty's identity and affiliations (legal name, DOT/MC-type identifiers, affiliate/ownership signals) used to test resolution across fragmented, conflicting records. | Aim 1 | FMCSA's public registration data (SAFER/Motus) as above, for the identifier fields it publishes; [ADDITIONAL SOURCE PLACEHOLDER] |
| Event assertions | Facility/operational event claims (e.g., appointment, arrival, gate, dock, loading/unloading, departure) with source, timestamp, and confidence metadata, used to test provenance and tamper/contradiction detection. | Aim 2 | [SOURCE PLACEHOLDER — facility or telematics partner feeds, per [[01-client-briefs/freight-trust-client-master-brief#Proposed system]]] |
| Benchmark labels | Adjudicated ground-truth labels (correct/incorrect entity match, verified/contradicted event) created to evaluate Aim 1 and Aim 2 systems against defined baselines. | Aim 1, Aim 2 | Created by the project team through an adjudication protocol; underlying raw records may be partner-sourced. [ADJUDICATION PROTOCOL OWNER PLACEHOLDER] |
| Interview records | Structured customer-discovery interview notes/recordings/transcripts with buyer-role contacts (brokers, carriers, facilities) capturing workflow pain, alternatives, and pilot interest. | Commercialization evidence supporting all aims | Collected directly by the project team; see [[commercialization-plan-draft]]. |

## 2. Provenance and permitted-use recording

Every ingested record — freight record, identity attribute, or event assertion — must carry, at minimum:

- **Source identifier**: where the record originated (authoritative registry, named partner system, telematics feed), consistent with the federated-by-default design in [[01-client-briefs/freight-trust-client-master-brief#Proposed system]] where "source systems remain authoritative; the trust layer establishes what evidence exists, where it came from, and how it may be used."
- **Timestamp**: when the record was captured or asserted, and when it was ingested.
- **Confidence/authoritativeness flag**: whether the source is authoritative-and-current, secondary, stale, or unverified (mirrors the governance loop in [[01-client-briefs/freight-trust-client-master-brief#Governance and redress]]).
- **Permitted-use tag**: the purpose(s) for which the data's source or contributing partner has authorized use (e.g., benchmark evaluation only; internal R&D only; not for redistribution) — recorded per record or per source-batch, not assumed globally.
- **Correction/dispute status**: whether the record has been challenged, corrected, or is under active dispute, with a pointer to the correcting record (see Section 7).

No record should be used for a purpose beyond its recorded permitted-use tag. Where a partner's authorization is undocumented, the record is treated as evaluation-only pending written confirmation, never as freely shareable or reusable by default. [PARTNER AUTHORIZATION LOG OWNER PLACEHOLDER].

## 3. Proprietary-data handling without a blanket designation

Some freight records, identity attributes, and event assertions will originate from named commercial partners (carriers, brokers, facilities) who may consider portions of their raw data proprietary or commercially sensitive. Consistent with the explicit caution in [[nsf-sbir-sttr-process-and-readiness-guide#7. Registrations, documents, and operating controls]], this plan does **not** apply a single blanket "all data is proprietary and confidential" designation, because that would block the independent validation NSF review requires (e.g., held-out benchmark evaluation, reproducible error analysis) and would conflict with any partner commitments to support pilot validation.

Proprietary handling is scoped at the field/record level:

- **Field-level sensitivity classification**: each ingested field is tagged as (a) shareable for benchmark/methodology reporting in de-identified or aggregate form, (b) usable for internal evaluation only, not reportable even in aggregate, or (c) restricted to the minimum personnel required, per partner agreement. [CLASSIFICATION OWNER PLACEHOLDER — data/product lead + counsel, per [[nsf-sbir-sttr-process-and-readiness-guide#9. Immediate deliverables for the programme]]].
- **De-identification for reporting**: where Aim 1/Aim 2 results are reported to NSF or in any public artifact, identity-level detail is removed or aggregated (e.g., segment-level precision/recall rather than named-carrier results), unless a specific partner has authorized identified reporting in writing.
- **No validation-blocking default**: the classification scheme must preserve at least one lawful, sufficiently representative slice of data on which the held-out benchmark and calibration tests (per [[nsf-sbir-sttr-process-and-readiness-guide#5. Full Phase I proposal: build around proof, not aspiration]]) can actually run and be independently reviewed — a partner's proprietary designation cannot be allowed to eliminate all testable evidence.
- **Written basis required**: no dataset is treated as "proprietary and unusable for validation" or "shareable" based on assumption; each partner's actual data-use agreement or letter governs its classification. [PARTNER DATA-USE AGREEMENTS PLACEHOLDER — list actual agreements once executed].

## 4. Retention and deletion

| Data type | Retention approach | Deletion trigger |
|---|---|---|
| Raw partner-sourced freight/identity/event records | Retained only as long as needed for the funded benchmark and prototype work, per the partner's data-use terms. | **Provisional default: award period plus 3 years, per standard federal audit-retention practice**, unless a partner agreement specifies a shorter period — [OVERRIDE PLACEHOLDER — apply only where a specific partner agreement requires shorter retention or earlier deletion/return]. |
| Benchmark labels (adjudicated ground truth) | Retained for the duration of the award plus any NSF-required post-award reporting window. | **Provisional default: award period plus 3 years**, matching the raw-record default above; reviewed for continued lawful basis before Phase II reuse, if any. |
| Interview records (notes/recordings/transcripts) | Retained per participant consent terms; recordings, if any, minimized in retention relative to notes. | **Provisional default: raw recordings deleted within 1 year of the interview** unless the participant's consent terms specify otherwise — [CONSENT TERMS PLACEHOLDER — apply only where an actual consent form states a different period]; de-identified synthesis may be retained longer for commercialization evidence. |
| Derived/aggregate benchmark artifacts (e.g., precision/recall tables, calibration curves) | Retained indefinitely as project evidence, since these do not expose raw partner data. | No routine deletion trigger; reviewed if a source dataset's authorization is later withdrawn. |

Deletion and retention commitments in this section must be checked against, and cannot exceed, whatever a partner's actual written data-use agreement permits. The 3-year and 1-year figures above are provisional company-stateable defaults (matching standard federal grant audit-retention practice), not partner-specific commitments; they are overridden by any partner agreement requiring shorter retention. [COMPANY RETENTION POLICY OWNER PLACEHOLDER — confirm or adjust these defaults].

## 5. Access and security controls

- **Role-based access**: access to raw freight/identity/event data is limited to named project personnel with a defined need (e.g., benchmark construction, model evaluation), consistent with the "role-based access, purpose limitation, data minimization" principles in [[01-client-briefs/freight-trust-client-master-brief#Governance and redress]].
- **Purpose-limited federation prototype**: the Aim 3 federation/policy-enforcement prototype must itself be tested against disallowed partner/field/purpose combinations (automated denial-and-audit tests), per [[nsf-sbir-sttr-process-and-readiness-guide#5. Full Phase I proposal: build around proof, not aspiration]] — the DMP's access model and the Aim 3 technical deliverable should be the same model, not two inconsistent descriptions.
- **Storage and transmission security**: **Provisional default**: encryption at rest (e.g., AES-256 or equivalent) and in transit (TLS 1.2+), using a mainstream cloud provider's standard security controls, pending confirmation of the company's actual provider and control implementation [ENCRYPTION/STORAGE CONTROL PLACEHOLDER — confirm actual cloud provider, specific control implementation, and any compliance regime (e.g., SOC 2) the company already follows; override this default only with the company's real, stronger or provider-specific commitment].
- **Credential and audit logging**: all access to raw partner data is logged; audit logs are themselves retained per Section 4 to support any partner or NSF review.
- **Personnel security**: access is removed promptly on role change or offboarding. [OFFBOARDING PROCESS OWNER PLACEHOLDER].

## 6. Sharing: benchmark artifacts vs. protected partner data

| Artifact class | Sharing posture | Rationale |
|---|---|---|
| Methodology, benchmark protocol, evaluation code/harness | Shareable in the proposal, in publications, and potentially as open methodology after award, subject to company IP decisions. | Permits independent review of Intellectual Merit without exposing partner data (per NSF's expectation that claims be verifiable). |
| Aggregate/segment-level benchmark results (precision/recall, calibration, disparity metrics) | Shareable in reporting and publication in de-identified/aggregate form. | Supports Broader Impacts and Intellectual Merit reporting while protecting identified partner data. |
| Raw partner-sourced freight records, identity attributes, event assertions | Not shared outside the funded project team and NSF-required reporting/audit channels; not published or redistributed. | Preserves partner trust and matches the federated, source-stays-authoritative design principle. |
| Interview records (raw) | Not shared outside the project team; synthesis only is used in commercialization evidence (see [[commercialization-plan-draft]]). | Protects interviewee confidentiality and matches typical discovery-interview consent scope. |
| Correction/redress case records | Retained internally; may be summarized (counts, resolution time) for reporting, not shared as raw content. | Supports the measurable "correction-time target" milestone in [[nsf-sbir-sttr-process-and-readiness-guide#5. Full Phase I proposal: build around proof, not aspiration]] without exposing dispute specifics. |

## 7. Correction and redress records

Consistent with the governance loop in [[01-client-briefs/freight-trust-client-master-brief#Governance and redress]] ("Participant challenges record? → Correct, annotate, or retain disagreement"), the DMP must record:

- Every instance where a benchmark label, identity record, or event assertion is challenged by a data subject or partner.
- The resolution: corrected, annotated with retained disagreement, or upheld — with timestamp and resolving party.
- The downstream effect: whether correction propagated to dependent decisions/records within the target time window defined by the Aim 2/redress milestone in [[nsf-sbir-sttr-process-and-readiness-guide#5. Full Phase I proposal: build around proof, not aspiration]].
- These records are treated as protected data (Section 6) but their existence and aggregate statistics (count, average resolution time) are reportable evidence of the redress-workflow milestone.

## Facts needed from company

- [ ] Confirmed list of actual data sources/partners for freight records, identity attributes, and event assertions, and the lawful basis/authorization for each.
- [ ] Actual data-use agreements or letters governing proprietary/sensitivity classification per partner.
- [ ] Company's chosen retention periods and deletion mechanics for raw partner data.
- [ ] Interview consent language and recording-retention policy.
- [ ] Encryption/storage/compliance specifics (cloud provider, security controls already in place).
- [ ] Named data/product lead and counsel responsible for classification and access decisions.
- [ ] Adjudication protocol and adjudicator identity for benchmark ground-truth labels.

## Related notes

- [[nsf-sbir-sttr-process-and-readiness-guide]]
- [[01-client-briefs/freight-trust-client-master-brief]]
- [[phase-1-budget-and-justification-draft]]
- [[commercialization-plan-draft]]
- [[technical-risk-register]]
- [[04-sbir/sbir-moc]]

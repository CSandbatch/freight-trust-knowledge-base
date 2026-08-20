---
type: experiment
id: E4
status: planned
phase: phase-i-or-pilot
owner: adoption-lead-plus-small-carrier-reviewers
schema_version: 1.0.0
updated: 2026-08-20
primary_outcome: participation-without-disproportionate-burden
tags:
- type/experiment
- lifecycle/planned
- domain/freight
- domain/identity
- domain/adoption
- domain/equity
---
# E4 — Participation and Small-Carrier Equity

Protocol standard: [[experiment-protocol-standard]].

## Thesis

Participants will share a limited set of evidence when the system offers a concrete
reciprocal benefit, but adoption will fail or become inequitable if the value is vague, the
data burden is high, access is paywalled, or errors are concentrated among small carriers.

This is an adoption and equity experiment, not a survey of whether people like the idea.
The unit must perform an observable task or make a real participation decision.

## How E4 tests the Freight Trust thesis

Participation is not a downstream commercialization detail. Voluntary, cross-party data
sharing is one of the programme's central assumptions. If the system produces technically
good evidence that no one will provide or use, the infrastructure thesis fails.

| Thesis layer | What E4 contributes |
|---|---|
| A neutral utility needs multiple actors | Observes activation, repeat use, refusal, and retention rather than assuming goodwill. |
| Data sharing must create reciprocal value | Compares concrete benefits against an information-only control. |
| The system must be fair to small carriers | Measures burden, errors, appeals, and time-to-benefit by fleet-size band. |
| Governance should increase agency, not coerce disclosure | Tests comprehension, consent, correction, and whether participation is genuinely voluntary. |
| Network interventions affect nonparticipants | Designs around spillovers through shared brokers, facilities, and workflows. |

E4 is the socio-technical test of the thesis. E1-E3 can show that the system is accurate,
traceable, and controllable; E4 asks whether those properties create enough practical value
for real actors to participate without shifting costs onto the least-resourced actors. A
positive result identifies a credible mechanism and segment. It does not prove industry-wide
adoption.

### How the methods connect to the thesis

- **Staged participation evaluation** tests behavior over time, separating activation from
  repeat use and retention.
- **Cluster/two-stage assignment** protects comparisons when a treated facility or broker
  changes the workflow for connected controls.
- **Burden accounting** translates low friction into staff minutes, fields, systems,
  assistance, waiting, cost, and failed attempts.
- **Comprehension testing** makes trust observable: participants must be able to describe
  sharing, access, retention, and redress.
- **Subgroup analysis** prevents a small-carrier penalty from disappearing inside an average.

### How the factors map to decisions

O0 tests organic value, and O1-O3 identify which reciprocal mechanism drives participation.
O4 asks whether a bundle adds value without pretending to identify one component. A0/A1
tests accessibility independently of offer and fleet stratum; T0/T1 tests added comprehension
support without weakening the institutionally approved common information/consent process. Spillover analysis determines whether the
result is an organization effect, a network effect, or both.

## Provenance

### Where E4 came from

E4 exists because of the single most persistent objection in this programme's own review
record — a standing objection from the Review Agent that no technical finding has ever
resolved.

| Origin | What it contributed to E4 | Status |
|---|---|---|
| [[goals]] G7 — "Test the data-sharing incentive assumption" | The core problem statement: the entire model assumes brokers and carriers will voluntarily share data with a neutral third party, and no direct evidence exists for freight specifically. Success requires finding at least one analogous precedent — a banking KYC utility, airline on-time reporting compliance — and identifying what actually drove participation: mandate, liability shield, or market pressure | open |
| [[goals]] G12 — "Test the participation mechanism" | The concrete requirement: specify at least three reciprocal benefits and a pilot method to measure uptake and retention by stakeholder and fleet size. O1, O2, and O3 are those three benefits | Open |
| [[goals]] G8 — "Assess small-carrier compliance-cost equity risk" | The requirement to identify who speaks for small and owner-operator carriers and what they have actually said about verification burden scaling with fleet size | Open |
| [[review-notes]] R-WN-02 — "Adoption mechanism undefined" (severity: high) | The finding that federation and neutrality do not themselves create willingness to share commercially sensitive data, and the required action: predefine three reciprocal offers and measure participation, retention, requested data fields, and rejection reasons by stakeholder and fleet segment. E4's outcome list is that action, restated as measurements | Open |
| [[review-notes]] R-WN-05 — "Small-carrier equity remains inferential" (severity: medium) | The finding that public evidence supports small-carrier relevance but not the programme's specific burden estimate, and the required action: direct primary research with a documented sampling plan | Open |
| [[improvement-suggestions]] items 6, 9, 10 | Small-carrier equity in the primary evaluation design rather than a fairness paragraph (6); participation as an experiment with concrete reciprocal benefits, measured burden, retention, and refusal reasons (9); the proposal-readiness gate (10) | Adopted |
| [[04-sbir/drafts/phase-1-project-description-draft]] Section 9 | The pre-submission commitment that at least 3 of the structured discovery interviews will be with carriers below a defined fleet-size threshold, so small-carrier perspective is captured during customer discovery rather than only inferred later from error-disparity measurement | Draft |

### The negative finding that shapes E4

The 2026-08-01 federation scan specifically checked whether the federated-learning
benchmark literature — LEAF, FedML, Flower — sheds any light on why a carrier or broker
would participate. It does not. Those are technical-computation benchmarks, not
adoption-economics research. That check is itself provenance: G7/G12 remain open because
the answer is **not** in the technical literature, not because nobody looked. The question
needs direct stakeholder research or a researched adjacent-industry analogy, neither of
which a dataset scan can produce.

This is why E4 is the only one of the five experiments whose primary input must be
generated by talking to people.

### Provenance of each input

| Input | Origin | Access mechanism | Terms | Verification status | What it can support | What it cannot support |
|---|---|---|---|---|---|---|
| [[dataset-partner-participation-burden-log]] | To be created by this project from consented participation | Collected from participating carriers, brokers, facilities, and reviewers during the pilot | Consent-based; purpose, fields, recipients, retention, correction process, and withdrawal limits must all be stated to the participant | **To-build.** Phase I-or-pilot | Activation, repeat use, requested fields, staff minutes, rejection reasons, appeals, and fleet-size band — the observable behaviour the hypotheses are about | Anything about non-participants, or about the industry beyond the recruited frame |
| Recruitment frame | Carriers across at least three fleet-size bands where feasible, plus brokers, shippers, and facilities who would actually request or supply evidence | Direct outreach; partner recruitment is an open decision | Voluntary; participation must not gate access to an essential service | **Open.** No named pilot participants exist yet — a live placeholder in the Project Description | Mechanism evidence and directional effects | A representative sample of the sector. Volunteers skew trust-oriented, and the design says so |

### Provenance of the external anchors

| Anchor | What it establishes | How E4 uses it |
|---|---|---|
| [[source-gao-2016-small-business-estimate]] — FMCSA estimated that approximately 99.1% of regulated carriers met one of several applicable SBA small-business standards | Small-business-standard coverage is broad enough that scale-sensitive analysis cannot be treated as optional | Supports primary stratification, but does **not** establish that 99.1% are owner-operators, very small fleets, or resource-constrained firms; fleet bands require separate FMCSA data and direct burden measures |
| [[source-ooida-2025-broker-record-access]] — OOIDA requested electronic broker transaction records within 48 hours of a carrier request and opposed contractual waiver of access rights | A first-party carrier association has placed record access and timeliness on the public policy record | Supports an access/timeliness concern only; it does not establish a Freight Trust correction right, correction-latency target, or independent burden estimate |
| [[source-fmcsa-2024-broker-transparency-nprm]] — FMCSA proposed electronic broker records and production within 48 hours after a carrier request | Official rulemaking context for the association position | Proposal only as of the 2026-08-20 retrieval; not current law, an automatic-delivery rule or a Freight Trust requirement |
| [[source-imai-2021-interference-noncompliance]] | Two-stage randomization can identify direct and spillover effects under explicit interference and noncompliance assumptions | Supports a cluster/exposure design when the recruitment network can sustain it; citation alone does not validate an unspecified network design |
| **G7's named adjacent precedents** — banking KYC utilities, airline on-time reporting compliance | The classes of analogy worth researching for what actually caused participation: mandate, liability shield, or market pressure | Recorded as the research direction G7 still requires. Neither has been researched yet, and E4 does not assume either transfers |

### Provenance of the method

| Method | Intellectual origin | What E4 borrows | What must be built | Known limitation |
|---|---|---|---|---|
| [[method-staged-participation-and-equity-evaluation]] | Standard field-experiment practice — intention-to-treat analysis, treatment-receipt separation, cluster-robust inference — combined with R-WN-02's specific measurement list | The staging: activation, repeat use, retention measured separately rather than collapsed into "adoption" | The offers themselves, the consent language, the burden instrument, the comprehension instrument, and the fleet-size band definitions | Small samples and self-selection may prevent causal conclusions. The design's answer is to label a directional result directional rather than dress it as significance |

### Provenance of the individual design choices

| Design choice | Why it is there, and whose finding forced it |
|---|---|
| The unit must perform an observable task or make a real participation decision — not answer a survey | R-WN-02's finding is that stated willingness is exactly what cannot be trusted here. A survey would reproduce the assumption instead of testing it |
| Three distinct reciprocal offers (O1, O2, O3) rather than one value proposition | G12 requires at least three concrete benefits. Testing one offer would confound "this benefit works" with "any benefit works" |
| O4 (combined offer) admitted only if combining does not destroy attribution | A bundle usually wins and explains nothing. Including it without that condition would produce a marketing result, not a mechanism result |
| Accessibility as an independent A0/A1 axis | Assisted onboarding and low-bandwidth support must not be confounded with fleet size or offer. No-paywall basic verification is common to all cells and is not withheld as a treatment |
| Burden measured as staff minutes, fields, systems, assistance requests, failed attempts, waiting, and direct cost — with median, tail, and maximum reported | "Low friction" is unfalsifiable. R-WN-05 found the programme's own burden estimate unsupported; this replaces the estimate with an instrument. A small carrier with one administrator may experience a different burden from a large carrier with a compliance team even at identical field counts |
| Comprehension check on what was shared, with whom, for what purpose, retention, and how to challenge | G13 and improvement item 5. A participant who activates but misunderstands the terms is a governance failure recorded as a success — the exact error the trust framing must not commit |
| Refusal reasons recorded as outcomes; nonresponse never treated as missing at random | Failure mode F10 (unmeasured burden) and F15 (unreported null). The reasons people decline are the most informative data this experiment can produce, and they vanish if refusal is treated as attrition |
| Cluster or two-stage assignment where interference is plausible | Imai, Jiang, and Malani. Failure mode F11 (spillover/interference) |
| Participation must never gate access to an essential service, and offers must not promise legal protection, insurance savings, or guaranteed freight access unless independently supported | G13's non-discrimination requirement, and the standing no-invented-claims rule. An offer that overpromises produces uptake that means nothing and exposes participants to harm |
| Underpowered results labelled directional, with a sample-size update for the next phase | Failure mode F15. An underpowered null is not evidence of no value, and treating it as one would misinform the Phase II decision |

## What E4 adds

### To the proposal

- It is the answer to the reviewer question the programme's own review process has flagged
  as its sharpest: who would actually give you this data, and why. E1 through E3 can
  demonstrate accuracy, traceability, and control; none of them addresses willingness.
- It makes Section 9's broader-impacts claims falsifiable. NSF broader impacts stated as
  intentions are weak; stated as a measured, preregistered subgroup design with a blocking
  decision rule, they are a research contribution.
- It supplies the commercialization narrative with mechanism evidence in place of
  assertion: which reciprocal benefit moves behaviour, in which segment, at what burden.

### To the benchmark artifact

E1–E3 leave behind datasets others can rerun. E4 leaves a recruitment, consent, and
treatment protocol; an assignment and spillover map; a participation/burden dataset with a
codebook; and a refusal-and-correction analysis. The codebook and burden instrument are the
reusable pieces. The documented review through 2026-08-20 did not identify a programme-ready
standard instrument for freight data-sharing burden; that is a bounded retrieval finding, not a
claim that no relevant instrument exists.

### To the evidence chain

E4 licenses claims about whether a concrete reciprocal benefit changes participation
behaviour in a recruited sample, which offers differ, what participation costs in staff
time by fleet-size band, and whether participants understand what they agreed to. It does
**not** license any claim about industry-wide adoption. A positive result identifies a
credible mechanism and a segment — nothing broader.

### To risk retirement

E4 is designed to test the risk that the programme builds technically excellent infrastructure
that no one supplies data to. If an institutionally approved, adequately identified study passes
its preregistered gates, it can narrow—not permanently retire—the participation and equity risk: if small
carriers bear disproportionate burden, that surfaces at pilot scale with a mitigation
requirement attached, not at deployment scale as a structural feature.

### What E4 deliberately does not add

Not a market-sizing exercise, not a survey of sentiment, and not proof that the sector
will adopt. Participants who volunteer may already be more trust-oriented, and fleet size
is an imperfect proxy for resources, geography, and technology maturity. The design states
both limits; a reviewer does not have to find them.

## Why we are using E4

### The counterfactual

Without E4, the programme's central adoption assumption remains exactly where R-WN-02 left
it: unaddressed, high-severity, and load-bearing. The technical experiments would all
succeed against an assumption nobody tested, and the first evidence about participation
would arrive during commercialization, when redesigning the incentive structure is most
expensive. There is also a fairness argument: without E4, small-carrier
equity stays a paragraph, and the broad population covered by applicable SBA small-business
standards would find out about the burden by bearing it.

### Alternatives considered and rejected

| Alternative | Why rejected |
|---|---|
| Survey stated willingness to share data | Stated preference is precisely what R-WN-02 says cannot be trusted. The unit must do something observable |
| Infer participation incentives from federated-learning benchmarks | Specifically checked in the 2026-08-01 scan and found absent. LEAF, FedML, and Flower are computation benchmarks; none addresses why anyone participates |
| Individual randomization throughout | Invalid where a treated facility or broker changes the workflow for connected controls. This is H5, tested rather than assumed |
| Recruit whoever is easiest — technology-forward participants | Would produce an uptake number and generalize it to a sector it does not represent. The design explicitly forbids it |
| Use a mandate or paywall to drive participation | G13 prohibits paywalling basic verification, and a mandate is not available to a Phase I project. And coerced participation would not test the reciprocal-value hypothesis at all |
| Defer all participation research to Phase II | It is the highest-severity open objection in the review record. Phase I therefore validates instruments, recruitment, burden, and mechanisms; only the powered field-effect claim is conditional on adequate clusters, approvals, partners, and resources |
| Report a single fairness score | Improvement item 6 rejects exactly this. A composite score can be similar in aggregate while burden, error, and appeal access all diverge by segment |

### Cost, dependency, and sequencing

E4 is the most expensive of the five in human terms and the least controllable in
schedule, because it depends on recruiting real organizations — none of whom are named
yet. Phase I work is limited by default to instruments, recruitment feasibility, burden, and
mechanism evidence; a powered field experiment is conditional. It depends on E1 and E3 having
produced something worth participating in: the offers in O1–O3 (faster onboarding,
portable evidence, dispute support with visible correction status) are only honest if the
resolution, policy, and correction machinery behind them actually works. Running E4 first
would mean testing offers the system cannot yet deliver.

Its open decisions — fleet-size band definitions, minimum acceptable small-carrier
subgroup size, and the first permissioned partner — are tracked in
[[datasets-and-experiments-moc]] and are the practical blockers on scheduling it.

## Research questions

1. Which reciprocal benefit most increases activation and repeat use?
2. How many fields and staff minutes does participation require by fleet-size band?
3. Do small carriers experience higher rejection, correction, or appeal rates?
4. Do participants understand what is shared, with whom, for what purpose, and how to correct it?
5. Does treatment spill over across a broker, facility, or carrier network?

## Hypotheses and nulls

| ID | Hypothesis | Null / failure interpretation |
|---|---|---|
| H1 | A concrete reciprocal benefit increases activation versus an information-only control. | Stated value does not change behavior. |
| H2 | Faster onboarding, portable evidence, and dispute support have different uptake effects. | Offers are indistinguishable or poorly specified. |
| H3 | Small-carrier burden satisfies a preregistered non-inferiority or veto rule after accounting for baseline capacity. | Design shifts cost to the least-resourced participants or precision is insufficient. |
| H4 | An interactive comprehension aid added to the institutionally approved common information/consent process improves understanding of purpose, access, retention, and correction without reducing voluntary completion. | The aid does not improve comprehension or creates unacceptable burden; required disclosure is never weakened. |
| H5 | Exposure mapping detects nonzero direct or spillover effects when the frozen network design supports them. | No detectable spillover under the frozen mapping; inability to identify the estimand is a design failure, not this null. |

## Experimental factors

| Condition | Description |
|---|---|
| Offer O0 | Information-only control: explanation of the system, no additional reciprocal benefit. |
| Offer O1 | Faster onboarding or reusable verification packet. |
| Offer O2 | Portable evidence and reduced repeat data entry across participating workflows. |
| Offer O3 | Dispute-resolution support with visible correction status. |
| Offer O4 | Predeclared combined offer, used only when the design can estimate a bundle effect without attributing it to one component. |
| Access A0 | Standard accessible path with the institutionally approved information/consent process, including any approved waiver or alteration, and the programme's proposed no-paywall basic-verification safeguard. |
| Access A1 | A0 plus predeclared assisted onboarding and low-bandwidth support. |
| Comprehension T0/T1 | The same institutionally approved information/consent process in every cell, including any approved waiver or alteration, with T1 adding an interactive comprehension aid such as teach-back. No cell receives less disclosure than that process requires. |

## Unit of analysis and estimand

- Provisional primary assignment unit: invited organization.
- Secondary units: onboarding case, shared field, correction, appeal, and repeat transaction.
- Primary estimand: organization-level intention-to-treat effect of each offer on activation and repeat use.
- Secondary estimands: treatment-on-the-treated effect, burden, trust comprehension, error,
  and subgroup difference by fleet-size band.

## Data and recruitment

- [[dataset-partner-participation-burden-log]] — consent-based participation outcomes.
- Recruit carriers across at least three fleet-size bands where feasible, plus brokers,
  shippers, and facilities who would actually request or supply evidence.
- Record non-participation and refusal reasons; do not treat nonresponse as missing at random.

The organization assignment unit is provisional until recruitment links, shared brokers,
facilities, loads, and workflows are mapped. Freeze the cluster definition and exposure mapping
before randomization. If the available organizations and clusters cannot support the declared
estimand and precision target, E4 remains a feasibility, instrument, and mechanism study; it does
not produce a powered field-effect claim.

The experiment must not make access to an essential service conditional on participation.
Offers must be comparable in time, contact, and explanation. Do not promise legal protection,
insurance savings, or guaranteed freight access unless independently supported.

## Methods

- [[method-staged-participation-and-equity-evaluation]]

Because participants interact in networks, treatment can affect controls through shared
brokers, facilities, or workflows. Use cluster or two-stage randomization where interference
is plausible; see [[source-imai-2021-interference-noncompliance]]. Human-subjects and consent
requirements are bounded in [[source-nsf-common-rule-human-subjects-consent]].

## Protocol

1. Obtain and record the determination required by the responsible institution/sponsor process
   (exempt, expedited, full review, or not human-subjects research as applicable) and approve the recruitment, consent,
   private-data, adverse-event, retention, withdrawal, and export-control plan before recruitment.
2. Define the participation task, offer axis, accessibility axis, institutionally approved common information/consent process, optional
   comprehension aid, and minimum data request.
3. Pre-register fleet-size bands, primary outcome, minimum detectable effect, stopping rule,
   organization assignment unit, clusters, and exposure mapping.
4. Randomize offers and accessibility support within predeclared strata or mapped clusters;
   record assignment, exposure, and treatment receipt separately.
5. Observe activation, completion, repeat use, fields requested, staff time, corrections,
   appeals, and reasons for refusal.
6. Conduct a short comprehension check on purpose, access, retention, and redress.
7. Analyze intention-to-treat first; report noncompliance and spillovers separately.
8. Return a participant-facing summary and offer correction of the study record.

## Variables

**Treatment:** factorial reciprocal-offer, accessibility-support, and optional comprehension-aid axes.

**Primary outcomes:** invitation-to-activation, task completion, repeat use, and retention.

**Burden outcomes:** staff minutes, number of fields, number of systems touched, technical
failures, assistance requests, and direct cost.

**Equity outcomes:** outcomes by fleet-size band, error/appeal/correction rate, abandonment,
time-to-benefit, and access to basic verification.

**Trust outcomes:** comprehension, perceived control, willingness to reuse, and stated concern.

**Safety outcomes:** coercion, unauthorized disclosure, adverse commercial consequence, or
participant misunderstanding of the system’s authority.

## Analysis plan

- Report primary outcomes by intention-to-treat with confidence intervals.
- Use cluster-robust or randomization-based inference when organizations or networks are
  the assignment units.
- Estimate direct and spillover effects when the design supports them; do not assume SUTVA.
- Compare burden and error distributions, not only means.
- Treat missingness and refusal as outcomes to explain, not records to silently discard.
- Do not call a difference “fair” because subgroup averages are similar; inspect mechanisms,
  burden, opportunity, and correction access.

## Initial decision rules

- Advance only if a concrete offer increases participation without coercion.
- Block scale if small carriers face materially higher burden, false positives, or appeal delay.
- Do not introduce a paywall for basic verification as a participation intervention.
- If spillover prevents a clean comparison, redesign around cluster/two-stage assignment.
- If sample size cannot support causal inference, label the result directional and prioritize
  qualitative mechanism evidence rather than overclaiming statistical significance.
- Phase I defaults to instrument validation, recruitment feasibility, burden measurement, and
  directional mechanism evidence. A powered field-effect claim is conditional on institutional
  approval, partner commitments, adequate clusters, precision, budget, and follow-up capacity.

## Threats to validity

- Small, recruited samples may not represent the industry.
- Participants who volunteer may already be more trust-oriented.
- Network spillovers can contaminate control conditions.
- Offers can differ in perceived value for reasons unrelated to the underlying mechanism.
- Fleet size is an imperfect proxy for resources, geography, and technology maturity.
- Participants may alter behavior because they know they are observed.

## Extended operational specification

### Participation unit and recruitment frame

The invitation unit must be the organization or workflow that can actually provide or use
evidence. Record organization role, fleet-size band, geography, operating model, existing
systems, baseline data burden, and prior relationship with the pilot. Do not recruit only
technology-forward participants and then generalize to the sector.

### Treatment integrity

For each offer, record what the participant was shown, what they understood, what they
received, and what they actually used. A participant assigned to faster onboarding who never
encounters a real onboarding task has not received the treatment. Analyze assignment,
exposure, and compliance separately.

### Spillover design

Map shared brokers, facilities, loads, and evidence flows before randomization. If a treated
carrier can make a control broker faster, or a treated facility changes the workflow for all
carriers, individual randomization is contaminated. Prefer cluster or two-stage assignment;
estimate direct, spillover, and total effects when the design supports them.

### Sample-size and precision plan

Before recruitment, specify baseline activation, target minimum detectable effect, power,
alpha, attrition, intracluster correlation, and number of clusters. If the pilot is too small
for a powered causal test, use it as a feasibility and mechanism study with confidence
intervals and a sample-size update for the next phase. Do not call an underpowered null result
evidence of no value.

### Burden accounting

Measure time with task timestamps where possible and self-report only as a secondary source.
Count fields requested, fields re-entered, systems accessed, support contacts, upload failures,
waiting time, direct fees, and opportunity cost. Report median, tail, and maximum burden. A
small carrier with one administrator may experience a different burden from a large carrier
with a dedicated compliance team even when field counts match.

### Equity analysis

Predeclare fleet-size bands and compare activation, completion, false-positive or rejection
rate, correction access, appeal latency, staff minutes, and benefit time. Do not use a single
average or a generic fairness score. Investigate mechanisms: missing system integration,
language/accessibility, records availability, financial cost, or different exposure to review.

### Trust and comprehension instrument

After exposure, ask participants to identify: what data was shared, who could see it, why it
was used, how long it would be retained, how to challenge it, and whether participation was
required. A participant who activates but misunderstands these terms is not an unqualified
success.

### Analysis model

Primary analysis is intention-to-treat. Use cluster-robust or randomization-based inference
for organization/network assignment. Report treatment receipt, noncompliance, attrition,
refusal, and missingness. Use interaction terms or stratified estimates for fleet-size bands,
but do not interpret small subgroup estimates without uncertainty intervals.

### Safety and consent

Participation must not affect access to an essential service or create a hidden penalty for
refusal. Consent must state the purpose, fields, recipients, retention, correction process,
withdrawal limits, and contact for concerns. Do not collect unnecessary identity, financial,
or operational detail. Return a participant-facing correction path for study records.

Follow the responsible institution/sponsor procedure; investigators do not self-authorize the
study. No recruitment or identifiable/private data collection begins before the documented
determination or approval required by that procedure. All arms receive the same approved
information/consent process, including any permitted waiver or alteration; comprehension support
may be additive but required disclosure may not be reduced as an experimental control.

### Public/private data boundary

The Git-tracked knowledge base is public. It may contain the protocol, blank instruments,
synthetic examples, disclosure-control method, and reviewed aggregate findings only. Raw or
pseudonymized invitation, refusal, staff-time, cost, appeal, correction, commercial-harm, and
linkage records must remain outside the repository in encrypted access-controlled storage. Keep
the re-identification key separate, log access, predeclare suppression/export review, and publish
no row-level participant data merely because a note is tagged `audience/internal`.

### Exit and escalation

Pause recruitment if participants report coercion, unexpected disclosure, or material
commercial harm. Block scale if small carriers experience higher burden or error without a
mitigation that is tested, not merely promised. If spillover is larger than anticipated,
re-estimate the design rather than pretending the control group remained untreated.

## Build-start specification

Before human-subject authorization, build only versioned blank instruments marked `NOT APPROVED -
NOT FOR RECRUITMENT`, synthetic fixture rows, data dictionaries/schemas, recruitment-frame and
cluster/exposure templates, deterministic assignment/power-analysis code, private-store and
threat-model designs, disclosure/suppression tests, accessibility checks and mock offer flows.
O1-O3 mocks test wording and software behavior only; they cannot support participation behavior
until E1/E3 capabilities and the study are authorized. Use the common run contract in
[[e1-e5-build-readiness-and-run-contract]].

Build acceptance requires reproducible synthetic assignment/exposure calculations, frozen
primary feasibility outcomes, burden statistic and sparse-cell rules, blocked unsafe exports,
complete consent/comprehension schema and no participant contact or real rows. The correction
path, no-paywall safeguard, export review and adverse-event workflow are project governance
choices unless a controlling rule or agreement separately requires them.

## Required outputs

1. Recruitment, consent, and treatment protocol.
2. Assignment and spillover map.
3. Private participation/burden dataset and codebook, with only disclosure-reviewed aggregates
   or synthetic examples eligible for the public vault.
4. Activation, retention, burden, equity, and comprehension report.
5. Refusal and correction analysis.
6. Go/no-go recommendation with partner feedback.

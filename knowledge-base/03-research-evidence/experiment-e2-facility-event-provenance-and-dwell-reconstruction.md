---
type: experiment
id: E2
status: planned
phase: phase-i
owner: event-modeling-lead-plus-facility-adjudication-panel
schema_version: 1.0.0
primary_outcome: provenance-aware-dwell-reconstruction-error
tags:
- type/experiment
- lifecycle/planned
- domain/freight
- domain/provenance
---
# E2 — Facility-Event Provenance and Dwell Reconstruction

Protocol standard: [[experiment-protocol-standard]].

## Thesis

A provenance-aware event model will reconstruct freight movement and distinguish confirmed,
inferred, missing, delayed, contradictory, and tampered records more accurately than a
simple timestamp or last-write-wins baseline. It will improve the evidentiary quality of
dwell and detention disputes without converting inference into fact.

## How E2 tests the Freight Trust thesis

The programme's second load-bearing claim is that trust is temporal and operational.
Knowing who a carrier is leaves open what happened, when it happened, which source supports
it, and what remains unknown. E2 tests whether the proposed event-provenance layer can
create that record.

| Thesis layer | What E2 contributes |
|---|---|
| Freight disputes arise from incompatible records | Creates competing source observations and tests reconciliation without erasing disagreement. |
| Dwell must be measured before it can be optimized | Separates appointment, arrival, gate, dock, loading, release, and departure intervals. |
| Provenance is more valuable than a cleaned-up timeline | Penalizes false certainty and rewards correct unknown/missing labels. |
| Federation should preserve source authority | Keeps source assertions, derivations, corrections, and views distinct. |
| Later orchestration depends on trustworthy state | Produces event-quality and uncertainty inputs E5 needs before scheduling claims. |

E2 connects identity trust to operational trust. An identity graph without event
provenance can support onboarding but cannot support detention disputes or coordinated
planning. An event timeline without source authority can create a more polished version of
the same dispute. E2 succeeds only if it makes uncertainty more visible and supported
conclusions easier to reach.

### How the methods connect to the thesis

- **Event-log generation and anomaly injection** creates controlled versions of the failures
  the project addresses: missing, delayed, duplicated, contradictory, and tampered records.
- **Provenance-aware reconstruction** tests whether the system preserves the difference
  between observed, inferred, and unresolved events.
- **Travel-time calibration** prevents unrealistic synthetic timing from masquerading as
  freight evidence while keeping the benchmark operationally plausible.
- **Expert adjudication** tests whether a reconstructed timeline helps a human dispute
  reviewer, not only whether it matches synthetic labels.

### How the conditions map to decisions

C0 represents fragmented-record status quo. C1 tests whether simple rules are enough. C2
tests the provenance thesis. C3 tests whether anomaly detection adds value without turning
irregularity into accusation. C4 tests privacy-preserving utility. C5 tests transfer to a
real partner without tuning on partner data.

## Provenance

### Where E2 came from

| Origin | What it contributed to E2 | Status |
|---|---|---|
| [[goals]] G14 — "Build the freight evidence benchmark" | The facility-event half of the benchmark: adjudicated event cases with provenance labels, against which completeness and dispute-resolution metrics can be measured | Open; scan complete, benchmark not built |
| [[goals]] G11 — "Define the minimum trusted-data architecture" | The requirement that every claim type carry an authoritative source, provenance record, access policy, correction path, and retention rule. E2's event schema is the operational answer for event claims | Open |
| [[review-notes]] R-WN-04 — "Evaluation dataset absent" (severity: high) | The finding that no adjudicated benchmark exists for facility-event provenance, and the required action to build one and preregister completeness and dispute-time measures | Open |
| [[improvement-suggestions]] items 4 and 8 | Separating authoritative evidence, operational event evidence, and inferred indicators in the data model itself (4); using synthetic data for feasibility but not as a substitute for external validation, hence C5 (8) | Adopted |
| [[dataset-scan-event-provenance-and-federation]] (2026-08-01), Aim 2 section | Every tooling decision below, and the confirmed negative finding that no freight-specific facility-event benchmark exists anywhere | Current |
| [[04-sbir/drafts/phase-1-project-description-draft]] Sections 1(b), 4, 6, 7 | The scoping constraint that disputed facility events are Aim 2's *research validation context*, not a second Phase I beachhead; the four named threat classes; the Month 7 milestone; the failure condition | Draft |

The scoping point is load-bearing and easy to lose. Facility-event disputes are the more
vivid story, but the Project Description deliberately keeps them out of the bounded pilot
(improvement item 1: narrow to one beachhead). E2 therefore has to be useful as
a research result on its own, evaluated against simulated and permissioned data, and it
has to leave behind a schema and architecture that generalize to the facility-event
instance for Phase II reuse. It is not allowed to smuggle a second product into Phase I.

### Provenance of each input

| Input | Origin and publisher | Access mechanism | License / terms | Verification status | What it can support | What it cannot support |
|---|---|---|---|---|---|---|
| [[dataset-openepcis-generated-event-logs]] | OpenEPCIS Test Data Generator, an actively maintained open-source project implementing the GS1 EPCIS 2.0 / CBV 2.0 standard | Free download and local generation; configurable JSON/JSON-LD output | **Apache 2.0** for the generator; the EPCIS/CBV standard itself is royalty-free per GS1 | **Primary.** Standard is GS1-published; generator is a maintained, documented open-source project | Valid, configurable synthetic event sequences today, at no cost, with fields that map onto the Aim 2 schema: business step, timestamp, source/location, disposition | Real facility ground truth. EPCIS is retail/product-tracking-oriented, not facility-appointment-oriented; the freight profile fields must be added |
| [[dataset-bts-truck-travel-time-data]] | BTS–ATRI Freight Mobility Initiative, county-to-county truck travel times, derived from ATRI's panel of ~350,000 unique tractors, published 2018–2024 | Free public download via data.bts.gov (Socrata portal), CSV/API | US federal open-data product; standard public-domain federal posture, though the exact per-dataset license text did not return to automated fetch | **Primary/secondary mix.** BTS is a primary federal statistical agency; the underlying ATRI panel's own licence terms are not stated on the BTS page | Calibration of inter-event transit and delay distributions so synthetic timing is not arbitrary | Facility events. It is aggregated to county pairs — no arrival, dock, or departure records exist in it. It must never be described as facility ground truth |
| [[dataset-permissioned-terminal-facility-event-feed]] | A pilot partner, if one is secured. Real, documented analogs exist: APM Terminals' API Store and Port Houston's Data Integration API, both offering appointment create/update/cancel and gate-event endpoints | Account registration, app registration, OAuth credentials, and in practice a customer or partner relationship | Commercial/partner terms; not open data | **Secondary** (vendor developer documentation read, live data not accessed) | C5 external validity, and — already, without any access — a schema cross-check against two independent real industry implementations | Anything in Phase I unless an agreement exists. It is not a Phase I dependency |

Sources deliberately excluded, and why:

- **ATRI's raw Freight Performance Measures GPS panel** — billions of points, ~1M heavy
  trucks, 10+ years, North America-wide. This is the closest real analog to facility
  arrival/departure telematics, and it is **restricted**: ATRI partners with individual
  MPOs, state DOTs, and universities under negotiated data-sharing agreements. No
  self-service download exists. It is a known hard blocker, not an oversight.
- **PIERS (S&P Global)** — bill-of-lading-level records are conceptually the kind
  of source-attributed trade event Aim 2 models, but it is a paid commercial licence, and
  the product page returned HTTP 403 to automated fetch, so even the terms are
  secondary-sourced.
- **STB Carload Waybill Sample** — access restricted by STB rule.
- **FMCSA ELD data-transfer specification** — a real, public *format* standard for
  source-attributed, timestamped driver-side records, useful as a schema reference. There
  is no public bulk dataset of actual ELD records. Schema only.
- **BTS Freight Analysis Framework, USACE Waterborne Commerce Statistics, FRA Data
  Portal** — all real, free, federal, and all at the wrong granularity: flow volumes,
  aggregate tonnage, and rail safety incidents respectively. No event-level facility data.
- **TradeLens** — discontinued Q1 2023 with no public dataset released. Its value to this
  project is narrative, not data: a real blockchain-provenance freight platform reached
  175+ organizations and failed for governance and trust reasons, not technical ones.
  That is prior-art context for the Project Description, and a caution for E3.
- **IBM Food Trust** — commercial, no accessible sample dataset found.

### Provenance of each method

| Method | Intellectual origin | What E2 borrows | What must be adapted or built | Known limitation |
|---|---|---|---|---|
| [[method-event-log-generation-and-anomaly-injection]] | The process-mining field's established practice: the Process Discovery Contest 2020/2021 benchmarks (192–480 synthetic training logs plus ground-truth models per year, published with DOIs on 4TU.ResearchData) and the Nolle et al. synthetic-log tradition, described in the literature as the de facto standard for anomaly-detection validation. Generator lineage: PLG / PLG2 / RT-PLG | The whole construction pattern: take a clean base log, apply anomaly classes to a defined share of traces at controlled rates, retain ground-truth labels for which traces were altered | Freight semantics. PDC logs are generic business processes with no facility, appointment, or dwell meaning. The four threat classes named in Project Description Section 4 — single-party fabrication, backdated timestamp, replay/silent edit, selective omission — must be encoded as injection operators | Injection mechanisms can make anomalies unrealistically easy to detect. An injected "tamper" without a documented threat model is an arbitrary edit, not an attack |
| [[method-provenance-aware-event-reconstruction]] | The programme's own architectural claim, grounded in NIST IR 8536's traceability meta-framework (cited in Project Description Section 2): traceability requires trusted repositories, linked records, secure access, and event recording — not a graph database alone. Event structure from GS1 EPCIS | The distinction the whole experiment turns on: observed, inferred, and unresolved are different states and must stay different | The freight profile: `source_id`, `observed_at`, `valid_time`, `clock_quality`, `actor`, `confidence`, `correction_state`, `access_purpose` on top of EPCIS's what/when/where/why | It cannot recover facts no available source supports. Its output quality is bounded by observability, which is why a separate "observability truth" is recorded |
| [[method-travel-time-calibration]] | BTS's published ATRI-derived county-to-county travel times | Realistic transit and delay distributions, so synthetic timing has an external anchor | Facility-side service-time distributions, which the BTS data does not contain | Aggregate travel times capture none of the appointment, dock, chassis, or labor constraints that drive dwell. Calibration makes timing plausible, not authoritative |
| [[method-expert-adjudication]] | Same panel discipline as E1 | Human judgment of whether a reconstruction is supported, overconfident, incomplete, or misleading — with "cannot determine" always available | A facility-side rubric distinct from E1's identity rubric | Costly; inter-rater agreement is itself a result |

Methodological analogs examined and set aside: **ISOMORPH** (MIT-licensed, current,
well-documented open supply-chain digital twin) simulates inventory and order flow between
echelons, not facility-level events — right spirit, wrong unit. **DataCo Smart Supply
Chain** carries real fraud and late-delivery labels but is order/transaction-level and not
trucking-specific. **IoT-23 / TON_IoT** are the closest thing to labeled tampering
datasets outside process mining, and are network-security data with no freight semantics.
Each is evidence that the *methodology* is established; none supplies usable content.

### Provenance of the individual design choices

| Design choice | Why it is there, and whose finding forced it |
|---|---|
| The hidden canonical trace is constructed first, and the system sees only derived observations | Standard hidden-truth benchmark construction, inherited from the PDC design. Without it, F02/F06 (source leakage, oracle information) are unavoidable |
| A separate "observability truth" recording what a permitted participant could actually know | The federation premise. A canonical trace says what happened; it must not imply every party could have seen it. Conflating the two would make the benchmark reward omniscience |
| Missing records never treated as proof of non-occurrence | Failure mode F05 in [[experiment-protocol-standard]] (missingness treated as negative evidence), and the substantive fairness point: in a dispute, absence of a record is usually a data-quality fact about one party's systems, not evidence about the other party's conduct |
| Dwell intervals decomposed — appointment-to-arrival, arrival-to-gate, gate-to-dock, dock-to-release, release-to-departure — and "detention" never inferred from long dwell alone | FMCSA treats detention measurement, as distinct from ordinary dwell, as an active unresolved research question. The programme's own evidence base cannot presently settle it either: the widely repeated $15.1B/year figure ($11.5B lost productivity, $3.6B added expense) is flagged **unverified** and may trace to an older ATRI study; the separately verified ATRI 2025 update reports $1.779/mile non-fuel marginal cost and roughly 1.5–2 hours average dwell per stop, with secondary sources disagreeing between ~1h38m and ~1h49m. A benchmark that collapsed dwell into detention would inherit that unresolved ambiguity as a silent assumption |
| Anomaly performance reported by family *and* rate, never as one headline number | The scan found that process-mining literature itself reports wide variance across methods and log types — one cross-benchmark study spanning 16 methods against 32 synthetic and 19 real logs found no dominant method. There is no borrowable target number, only a borrowable measurement method |
| Re-identification risk is a first-class outcome with its own release tiers, not an appendix | Published research shows event-log cases can be re-identified through sequence uniqueness and cross-correlation; NIST SP 800-188 supplies the de-identification framing. Freight event sequences are commercially sensitive as well as personally sensitive |
| C5 is external validation and is never pooled into the synthetic estimate | Improvement item 8. Pooling a small partner sample into a large synthetic one would let synthetic performance masquerade as validated performance |
| Numeric tamper-detection and correction-latency targets left bracketed | No external benchmark supplies a freight-transferable target. Stated explicitly in the scan's placeholder table |

## What E2 adds

### To the proposal

- It gives Aim 2 a build path that requires no partner, no purchase, and no signed
  agreement: OpenEPCIS plus a documented anomaly-injection methodology with academic
  precedent. Before the scan, Aim 2's honest status was "we would need data that does not
  exist."
- It converts "no adjudicated event-provenance benchmark exists" from a weakness into the
  argument for the work — a first-of-kind resource, consistent with G14's own framing.
- It supplies the Month 7 milestone with something falsifiable: detection of a defined
  share of simulated contradiction/tampering cases at a defined false-alarm ceiling, with
  an auditable evidence trail per test case.

### To the benchmark artifact

E2 leaves behind: a versioned event ontology and data contract, a base-trace generator, an
anomaly-injection manifest, a hidden-label evaluation set, and an adjudication record. The
scenario matrix — event coverage, anomaly rate, source count, clock skew, trace length,
dwell distribution, anomaly family, source reliability — is itself the reusable part,
because it defines the difficulty axes anyone else would have to specify to compare.

### To the evidence chain

E2 licenses claims about whether a timeline can be reconstructed from incomplete or
contradictory sources, whether uncertainty can be made visible without being made
accusatory, and what event coverage and timestamp quality a facility claim requires before
it is usable. That last question has the most practical downstream value and the least
existing literature.

### To risk retirement

It retires the second technical unknown: whether provenance metadata earns its complexity.
A negative result here is informative — it would mean the simpler timestamp
model is sufficient and the architecture should shed weight. It also front-loads the
privacy question, which is far cheaper to discover in a synthetic corpus than in a
partner's production feed.

### What E2 deliberately does not add

No claim that detention or dwell is reduced. No second commercial workflow in Phase I. No
assertion that synthetic traces represent real facility failure modes — that is what C5
exists to test, and what its absence would leave open.

## Why we are using E2

### The counterfactual

Without E2, the programme has an identity graph and nothing operational attached to it.
Identity alone supports onboarding — which is the beachhead — but cannot support any claim
about what happened at a facility, which is where the Phase II expansion and the
orchestration case (E5) both live. E5 in particular needs event-quality and uncertainty
inputs that only E2 produces; running E5 without them would mean planning over data whose
reliability was never characterized.

### Alternatives considered and rejected

| Alternative | Why rejected |
|---|---|
| Wait for a real facility-event benchmark | None exists anywhere — public, academic, or commercial. This was confirmed by direct scanning, not assumed. Waiting is not a plan |
| Make a permissioned partner feed the primary dataset | It would put the Phase I schedule inside someone else's contracting process. Kept as C5, an optional holdout that strengthens the result when available and does not block it when not |
| Reuse Process Discovery Contest logs directly as the evaluation set | Generic business-process logs with no facility semantics, no dwell intervals, no multi-source disagreement structure. The methodology transfers; the content does not |
| Adapt ISOMORPH | Wrong simulation unit — inventory and order flow between echelons, not appointment/arrival/dock/departure events. It would need substantial rework, not reuse |
| Model events as a blockchain ledger and claim tamper-proofing | TradeLens is the cautionary precedent: a real, well-funded freight provenance platform that reached 175+ organizations and shut down for governance and trust reasons, not technical ones. Hash-chaining appears in E3 as *tamper evidence*, deliberately scoped to detecting alteration, not to proving an event was true |
| Report one aggregate anomaly-detection number | It would hide what a reader needs: which failure families are detectable, at which rates, and where the method mistakes missing data for misconduct |

### Cost, dependency, and sequencing

E2 depends on E1 only loosely — event traces reference carrier entities, so entity
definitions should be stable first — but it can be built in parallel, which is how the
work plan schedules it (Months 4–7, after the provenance schema in Months 1–2). Its cost
is the generator configuration and the adjudication panel; its schedule risk is the case
count and taxonomy, which remain open decisions. C5 is the only part that can slip for
reasons outside the project's control, which is why nothing else depends on it.

## Research questions

1. Can the system reconstruct a case timeline when events are incomplete or contradictory?
2. Can it detect injected anomalies without confusing missing data with misconduct?
3. Does preserving provenance reduce dwell-duration and dispute-resolution error?
4. What event coverage and timestamp quality are required before a facility claim is usable?
5. Can useful outputs be produced without exposing re-identifying operational detail?

## Hypotheses and nulls

| ID | Hypothesis | Null / failure interpretation |
|---|---|---|
| H1 | Provenance-aware reconstruction has lower event-order and dwell error than timestamp baseline. | Provenance adds complexity without evidentiary improvement. |
| H2 | Anomaly detection identifies labeled missing, duplicate, contradiction, and tamper cases above baseline. | Event noise cannot be separated reliably from normal variation. |
| H3 | The system labels unknown/uncertain events more honestly than a forced-complete timeline. | It overstates certainty or silently fills gaps. |
| H4 | Better provenance reduces time to adjudicate a dispute. | Record quality does not translate to workflow value. |
| H5 | Privacy controls reduce re-identification risk with acceptable utility loss. | Event detail is too identifying or anonymization destroys utility. |

## Experimental conditions

| Condition | Description |
|---|---|
| C0 | Raw timestamp/last-write-wins baseline with no explicit provenance. |
| C1 | Rule-based event ordering and missingness flags. |
| C2 | Provenance-aware reconstruction with source priority, temporal constraints, and confidence. |
| C3 | C2 plus anomaly detector for missing, duplicate, contradiction, and tamper patterns. |
| C4 | Privacy-reduced release of C2/C3 outputs with generalized or perturbed timestamps. |
| C5 | External-validity holdout using permissioned facility events, if available. |

## Unit of analysis and estimand

- Primary unit: event trace/case for one load or movement.
- Secondary unit: event and reconstructed interval.
- Primary estimand: absolute error in reconstructed event times and dwell duration.
- Secondary estimands: anomaly precision/recall, event completeness, uncertainty calibration,
  dispute-resolution time, and privacy risk/utility trade-off.

## Data and labels

- [[dataset-openepcis-generated-event-logs]] — controlled synthetic event traces.
- [[dataset-bts-truck-travel-time-data]] — travel-time calibration, not facility ground truth.
- [[dataset-permissioned-terminal-facility-event-feed]] — optional partner holdout.

Each base case must contain a hidden canonical trace, source records, event timestamps,
actor, location granularity, event type, and provenance metadata. Inject anomalies only after
the base trace is frozen. Required anomaly families: deletion, delay, duplication, swap,
contradiction, impossible order, clock skew, source disagreement, and tampering.

## Methods

- [[method-event-log-generation-and-anomaly-injection]]
- [[method-provenance-aware-event-reconstruction]]
- [[method-travel-time-calibration]]
- [[method-expert-adjudication]]

Process-mining research shows that missing, duplicated, and swapped events materially affect
event-log analysis and that labeled anomaly benchmarks are needed. See [event-log anomaly
detection research](https://www.sciencedirect.com/science/article/pii/S0020025520311038) and
[temporal sequencing anomalies](https://www.mdpi.com/2076-3417/13/5/3143).

## Protocol

1. Define the event vocabulary, case boundary, authoritative source rule, and unknown label.
2. Generate valid base traces with realistic travel and service-time distributions.
3. Hide the canonical trace and inject anomalies at prespecified rates and combinations.
4. Run C0-C3 without access to injected labels.
5. Evaluate event reconstruction, anomaly detection, uncertainty, and dwell error.
6. Run C4 privacy transformations and measure utility versus uniqueness/re-identification risk.
7. If available, run C5 on a partner holdout with no tuning on partner data.
8. Have reviewers adjudicate a stratified sample of reconstructed cases and disagreements.

## Variables

**Inputs:** event type, source, timestamp, location granularity, actor, sequence, source
reliability, missingness, delay, clock skew, and case complexity.

**Treatment:** condition C0-C5 and anomaly severity.

**Primary outcomes:** event-order accuracy, timestamp error, dwell-duration error, and
anomaly precision/recall.

**Secondary outcomes:** completeness, calibration of confidence, unknown/abstention rate,
review time, correction latency, computational cost, and privacy risk.

**Guardrails:** no inferred event may be reported as confirmed; a missing record must not be
interpreted as proof that an operational event did not occur.

## Analysis plan

- Stratify by anomaly type, anomaly rate, trace length, source count, and event coverage.
- Report both case-level and event-level performance.
- Use paired comparisons because each corrupted trace has a known base trace.
- Report confidence intervals across independent generated seeds and, separately, partner cases.
- Plot the trade-off between event completeness, dwell error, uncertainty, and privacy risk.
- Treat C5 as external validation; do not pool it into the synthetic estimate.

## Initial decision rules

- No feasibility claim unless C2 improves dwell reconstruction or dispute evidence over C0
  without increasing false certainty.
- No anomaly-detection claim unless performance is reported separately by anomaly type and rate.
- No operational use if missingness and contradiction are collapsed into a single clean timeline.
- No public event release until the re-identification risk assessment and minimum-cell rules pass.

## Threats to validity and privacy

- Synthetic traces may omit real facility failure modes.
- Injection mechanisms can make anomalies unrealistically easy to detect.
- Public event traces can reveal organizations through unique sequences or timing.
- Travel-time calibration does not reproduce appointment, dock, chassis, or labor constraints.
- A partner feed may have its own undocumented clock and data-quality biases.

The privacy threat is substantive: research on event logs has shown that cases can be
re-identified through uniqueness and cross-correlation. See [event-log re-identification
research](https://pmc.ncbi.nlm.nih.gov/articles/PMC7266437/) and [NIST SP 800-188](https://csrc.nist.gov/pubs/sp/800/188/final).

## Extended operational specification

### Event model

Use an event representation with explicit `what`, `when`, `where`, `why`, and `how` fields,
plus source and provenance metadata. GS1 EPCIS is a useful event-visibility reference because
it structures what happened, when, where, and in what business context: [GS1 EPCIS](https://www.gs1.org/standards/epcis).
The freight profile should add `source_id`, `observed_at`, `valid_time`, `clock_quality`,
`actor`, `confidence`, `correction_state`, and `access_purpose`.

### Minimum event schema

| Field | Required meaning |
|---|---|
| `case_id` | Load, shipment, container, or movement boundary |
| `event_id` | Source-scoped immutable event identifier |
| `event_type` | Appointment, arrival, gate, dock, load, depart, deliver, or exception |
| `event_time` | Time claimed by the source |
| `observed_at` | Time the event was received or retrieved |
| `location` | Facility and precision level; avoid unnecessary exact coordinates |
| `actor` | Reporting or responsible actor, subject to permission |
| `source_id` | System or participant that asserted the event |
| `source_version` | Source schema or feed version |
| `confidence` | Confidence in the claim, not a generic model score |
| `provenance_chain` | Derivations, merges, corrections, and reviewers |
| `status` | confirmed, inferred, disputed, missing, superseded, or unknown |
| `sensitivity` | Re-identification and commercial-sensitivity class |

### Scenario matrix

Generate a full factorial or fractional factorial over:

- event coverage: 100%, 90%, 75%, 50%;
- anomaly rate: 0%, 1%, 5%, 10%, 20%;
- source count: one, two, and three independent sources;
- clock skew: none, fixed offset, drift, and daylight/time-zone error;
- trace length: short, normal, and long;
- dwell distribution: low-variance, heavy-tailed, and multimodal;
- anomaly family: deletion, delay, duplicate, swap, contradiction, impossible order, and tamper;
- source reliability: equal, known unequal, and unknown.

Do not use one anomaly rate as a universal benchmark. Report performance by family and rate.
An injected “tamper” must have a documented threat model; arbitrary edits are not equivalent
to a realistic attack.

### Hidden-truth construction

Create a canonical trace first, store it separately, and derive source observations from it.
The system under test sees only the observations. The canonical trace contains the intended
event, but it must not imply that an operational record would have been observable by every
party. A separate “observability truth” records what a permitted participant could actually know.

### Dwell and detention definitions

Predeclare the interval definitions. For example, appointment-to-arrival, arrival-to-gate,
gate-to-dock, dock-to-release, and release-to-departure are distinct intervals. “Detention”
must not be inferred from a long dwell interval alone; the threshold, appointment context,
carrier/facility rule, and exception policy must be explicit. Report interval uncertainty when
start or end events are missing.

### Privacy and release tiers

Maintain three outputs: raw partner-held records, restricted benchmark records, and public
aggregates. Test uniqueness of event sequences, timestamp/location combinations, and actor
relationships before release. Generalization, suppression, or perturbation must be evaluated
against utility loss. Re-identification risk is a first-class outcome, not an appendix.

### Statistical analysis

Use paired case-level comparisons because every anomaly case has a canonical trace. Report
absolute timing error, interval overlap, order accuracy, event-level precision/recall,
case-level anomaly detection, calibration, and uncertainty coverage. For dwell, report MAE,
median absolute error, 90th-percentile error, and the proportion of disputes whose conclusion
changes. Bootstrap over independent cases, not individual events alone.

### Human adjudication

Reviewers receive the evidence packet, source lineage, and reconstructed output. They label
whether the output is supported, overconfident, incomplete, or misleading. Reviewers must be
able to select “cannot determine.” Measure inter-rater agreement and time-to-resolution.

### Exit and escalation

Block release if the system reports inferred events as confirmed, treats missingness as proof
of non-occurrence, or produces high uniqueness risk without mitigation. Reopen the event model
if partner data introduces event types or clock behavior absent from the synthetic generator.

## Required outputs

1. Versioned event ontology and event-data contract.
2. Base-trace generator and anomaly-injection manifest.
3. Hidden-label evaluation set and adjudication record.
4. Reconstruction, anomaly, uncertainty, dwell, and privacy report.
5. Partner-holdout report, if data rights permit.

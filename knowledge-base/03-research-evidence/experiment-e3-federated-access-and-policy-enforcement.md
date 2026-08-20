---
type: experiment
id: E3
status: planned
phase: phase-i
owner: security-and-governance-lead
schema_version: 1.0.0
updated: 2026-08-20
primary_outcome: policy-enforcement-conformance
tags:
- type/experiment
- lifecycle/planned
- domain/freight
- domain/federation
---
# E3 — Federated Access and Policy Enforcement

Protocol standard: [[experiment-protocol-standard]].

## Thesis

A governed, authenticated federation can enforce partner-, field-, and purpose-specific access
rules and produce a tamper-evident audit record for the tested path while keeping designated raw
commercial data at its source. The experiment
tests whether the policy specification, implementation, and audit behavior conform to the
intended governance rules; it does not claim that passing tests proves the policies are
complete or socially acceptable.

## How E3 tests the Freight Trust thesis

Distributing data does not by itself make a federation trustworthy. The thesis requires
governed federation: the right participant gets the right evidence for the right purpose,
access is auditable, and corrections remain contestable. E3 tests those technical and
institutional conditions.

| Thesis layer | What E3 contributes |
|---|---|
| Participants retain control of raw data | Tests whether a decision can use permitted summaries or derived evidence instead of unrestricted raw access. |
| Neutral infrastructure must be governed | Encodes purpose, role, resource, consent, time, and policy version as explicit decision inputs. |
| Trust requires accountability | Tests whether every decision, including denial and error, is captured in an auditable record. |
| Participants need correction and redress | Traces correction through source, claim, derived view, and audit history without rewriting the past. |
| Federation must not create hidden surveillance | Tests metadata leakage, inference from denials, and privacy/utility trade-offs. |

E3 separates a knowledge graph from trust infrastructure. A graph can connect records while
still enabling overbroad access, silent overwrites, and opaque secondary use. Passing E3 does
not prove the governance model is legitimate. Failing E3 shows the architecture cannot yet
make a credible controlled-federation promise.

### How the methods connect to the thesis

- **Policy conformance testing** turns governance principles into executable, reviewable
  cases and tests prohibited workflows alongside legitimate ones.
- **Hash-chained audit logging** connects accountability to a technical artifact. The
  instrumented PEP/PDP path records tested decisions and can detect specified post-hoc
  alterations only under the declared capture, anchoring, key, time and reconciliation
  assumptions; it does not prove completeness, authenticity or source truth by itself.
- **Correction propagation** is the operational form of contestability.
- **Adversarial testing** covers misuse by authorized actors, stale attributes, purpose
  substitution, replay, or inference from errors.

### How the conditions map to decisions

C0 demonstrates why governance is needed at all, and C1 tests whether role-only access is
insufficient. C2 tests the intended policy model, C3 contestability, C4 active misuse. C5
asks whether privacy-preserving release remains useful for freight decisions. One high-risk
false allow blocks advancement regardless of aggregate pass rate.

## Provenance

### Where E3 came from

| Origin | What it contributed to E3 | Status |
|---|---|---|
| [[goals]] G11 — "Define the minimum trusted-data architecture" | The requirement that the architecture be federated by default, with raw partner-data pooling needing specific justification, and that every claim type have a documented access policy and correction path | Open |
| [[goals]] G13 — "Define redress and non-discrimination requirements" | The written-policy requirement for abstention, human review, participant correction/challenge, false-positive remediation, and no-paywall basic verification. C3 is the executable form of the correction half | Open |
| [[review-notes]] R-WN-03 — "Automated-score liability risk" (severity: high) | The required action: evidence paths and challengeable indicators, with abstention, human review, correction, and appeal before consequential use. `permit-with-redaction`, `require-review`, and `abstain` exist in E3's decision vocabulary because of this | Open |
| [[improvement-suggestions]] items 5 and 7 | The formal abstention/human-review path (5); leading with the neutral, federated, challengeable infrastructure distinction and explicitly disclosing conflict-of-interest risk in vendor-authored standards (7) | Adopted |
| [[dataset-scan-event-provenance-and-federation]] (2026-08-01), Aim 3 section | The finding that this is the *most resolved* of the three aims: a concrete, no-cost, no-partner build path exists using government- and standards-body-maintained tooling | Current |
| [[04-sbir/drafts/phase-1-project-description-draft]] Sections 5, 7, 9 | The Month 9 milestone (100% denial and 100% audit-log capture of disallowed partner/field/purpose combinations), the failure condition, and the broader-impacts commitments E3's tests are supposed to make real rather than rhetorical | Draft |

### Provenance of each input

E3 can use current public standards, NIST guidance and prototype software, but its freight
policy corpus, adapters, enforcement point, authentication, and audit reconciliation remain
project work. The open questions include whether policy can be specified correctly and whether
the assembled authenticated enforcement path behaves as intended.

| Input | Origin and publisher | Access mechanism | License / terms | Verification status | What it can support | What it cannot support |
|---|---|---|---|---|---|---|
| [[source-nist-policy-machine]] | NIST Policy Machine core/PDP software | Free source download | See repository license | **Official software; configuration-dependent.** Reverified 2026-08-18 | An NGAC/PML implementation lane after version pinning and secure configuration | Freight policy authority, XACML execution, complete request logging, or secure defaults |
| [[source-oasis-xacml-3-0]] | OASIS XACML 3.0 standard and committee tests | Public standard/test artifacts | OASIS terms; implementation licenses separate | **Primary standard.** Reverified 2026-08-18 | XACML-native decisions, requests, obligations, and a separate conformance lane | NGAC/PML conformance, OASIS certification, or freight policy correctness |
| [[dataset-nist-policy-machine-xacml-cases]] | To be built by this project, in the above format | Authored from Section 5's own examples and the policy catalogue | Project-defined | **To-build** | The conformance, adversarial, and correction case sets | Proof that the policy is complete or legitimate — only that the implementation conforms to what was written |
| Derived audit records | Produced by the prototype itself | Generated during test execution | Project-defined | **To-build** | Audit-capture and integrity evidence | Truth about the underlying event. Hash chaining detects alteration; it says nothing about whether the original assertion was accurate |

### Provenance of the governing standards

| Standard | What it is | How E3 uses it |
|---|---|---|
| **NIST SP 800-192**, *Verification and Test Methods for Access Control Policies/Models* | Official NIST guidance specifically on verifying and testing ABAC systems | The test-design reference. Its core argument is E3's premise: policy models can be inconsistent or incomplete, and implementations can embed constraints not visible in the policy specification. That is why the protocol treats oracle separation, mutation testing, and independent review as requirements, not as optional rigor |
| **NIST SP 800-162**, *Guide to Attribute Based Access Control* | The definitional ABAC guidance | The attribute-family vocabulary: requester, organization, resource, purpose, action, context, decision |
| **NIST SP 800-178** | A comparison of ABAC standards including XACML and NGAC | Requires separate XACML and NGAC/PML execution lanes or an explicitly tested translation; a test convention from one is not conformance for the other |
| **NIST AI RMF** | Trustworthiness framing used across all five experiments | The insistence in [[experiment-protocol-standard]] that validity, robustness, reliability, and context-specific risk are distinct concerns — hence E3's refusal to let a 100% structural pass rate stand in for governance legitimacy |

**NIST ACPT / ACTS** (combinatorial access-control policy test generation) was found only
in secondary and academic sources describing SP 800-192-era tooling; a direct fetch of the
current NIST page did not surface it by name. It is recorded as an unconfirmed lead, not a
resource E3 depends on. If confirmed live, it would be relevant to generating the
cross-product test matrix.

### Provenance of each method

| Method | Intellectual origin | What E3 borrows | What must be adapted or built | Known limitation |
|---|---|---|---|---|
| [[method-policy-conformance-testing]] | OASIS/AT&T XACML conformance practice, with SP 800-192 as the verification methodology | Repeatable structural testing with explicit expected outcomes, plus the mutation-testing idea: alter one rule and verify the suite catches the regression | Freight-specific disallowed combinations drawn from Section 5's own examples — a facility receiving a carrier's unrelated insurance-rate data; a broker receiving raw telematics beyond a permitted event summary | Passing synthetic tests does not prove policy completeness in live operations, and the oracle can encode the same mistake as the implementation. Oracle separation is the mitigation, not a cure |
| [[method-hash-chained-audit-logging]] | Standard append-only/hash-chain construction | Verifiable access history without centralizing raw partner data | The freight audit record: requester, organization, resource class, purpose, action, decision, policy version, attributes used, timestamp, correlation ID, hash pointer — and the semantic distinction between denied, permitted, redacted, abstained, and errored | Tamper evidence is not truth. A perfectly complete, cryptographically sound log of wrong decisions is still a failure, which is why audit completeness and decision correctness are measured separately |

### Provenance of the contestability design

Correction propagation is the part of E3 with the least technical precedent and the most
institutional precedent. The scan looked for both and found the following, none of which
supplies an importable number:

- **FCRA reinvestigation provision** (15 U.S.C. §1681i). This verified statute applies to
  consumer reporting agencies and consumer disputes, including a generally 30-day
  reinvestigation period with statutory qualifications. It is adjacent-domain evidence for
  specifying authority, notice, correction, and redress—not a freight obligation or an
  importable latency target.
- **Meta Oversight Board case reporting.** Published individual case outcomes, including
  appeal volumes and overturn rates — one documented case had 215 user appeals with a 98%
  success rate — across roughly 75 decisions from 2021 through January 2024. Useful purely
  as a precedent for *how to report* a correction/appeal workflow: overturn rate, appeal
  volume, elapsed time. Not a dataset, not freight-related.
- **GLEIF** (Global Legal Entity Identifier System), cited in Project Description Section
  2. A cross-industry analogue for standardized identity data with independent governance
  and a working challenge/update mechanism. Its component list — governance, standardized
  records, quality control, challenge mechanism — is a design reference for what a neutral
  utility has to contain.
- **Algorithmic recourse literature.** Examined and set aside as a *different problem*.
  That literature explains or reverses a model's decision ("what would need to change for
  a different outcome"); E3's redress workflow corrects a **factual record** and propagates
  the correction downstream. Conceptual background only.

### Provenance of the individual design choices

| Design choice | Why it is there, and whose finding forced it |
|---|---|
| C0 is a deliberately unsafe permissive baseline | Without a negative control, a passing test suite proves nothing about whether the policy layer is doing the work. It also makes the cost of *no* governance visible, which is the argument the proposal has to make |
| C1 tests role-only access rather than assuming it is insufficient | The programme's claim is that purpose, field sensitivity, consent, and data age matter. Asserting that RBAC is inadequate would be exactly the kind of unfalsifiable premise R-WN-01 flagged elsewhere. C1 makes it a measured comparison |
| Purpose limitation as its own hypothesis (H3) | A request must not gain access by changing only its stated purpose. This is the specific failure that separates governed federation from a well-organized data pool |
| One high-risk false allow blocks advancement regardless of aggregate pass rate | Severity, not average, is the right frame for an access-control failure. A weighted pass rate may summarize operations; it may not offset a severity-one false allow. Failure mode F09 (policy incompleteness) |
| "Default deny" declared insufficient on its own | A system that denies everything passes every negative test and is useless. The suite must prove permitted workflows remain usable — false-deny is a first-class outcome |
| Oracle separation between policy author, test-case author, and implementer | SP 800-192's central caution. Without separation, the test suite and the implementation can share one misunderstanding and both pass |
| Mutation testing of the policy itself | A suite that passes the original policy but misses a material single-rule mutation is incomplete. Failure mode F13: it measures the *test suite*, not the system |
| Metadata and inference leakage treated as an open enumeration item, not a solved problem | No dedicated freight leakage benchmark is confirmed in this experiment file. Metadata/inference leakage and insider misuse remain open enumeration items; the protocol must not imply that passing policy-conformance tests resolves them. |
| "100% structural conformance does not establish that the policy is complete" stated as a decision rule, not a caveat | The most likely misreading of a green test suite is that governance is solved. Independent governance review remains required, and a passing suite authorizes only the tested policy version and attribute vocabulary |

## What E3 adds

### To the proposal

- Its structural lane has no external-data dependency, but it still depends on an authority-
  reviewed freight policy oracle, authenticated identity/JWKS, a pinned engine/adapter/runtime,
  and independent request-ledger reconciliation. NIST Policy Machine and a separate XACML lane
  are implementation candidates, not interchangeable proof or OASIS certification.
- It converts the proposal's privacy and commercial-boundary claims from assurances into
  tests. Section 9's data-minimization commitment — grant only the minimum necessary
  fields for a stated purpose, with a full audit trail of what was requested, by whom, and
  why — is measured here or nowhere.
- It gives improvement item 7's "neutral, federated, challengeable" positioning something
  to stand on, and the conflict-of-interest disclosure about vendor-authored standards is
  more credible coming from a project that built on NIST's implementation rather than its
  own.

### To the benchmark artifact

The policy-cases third of the G14 benchmark: a plain-language policy catalogue, an
attribute dictionary, a versioned conformance suite with expected decisions, enforcement
and audit logs with integrity verification, a correction-propagation report, and a
threat-model and privacy/utility report. The freight-specific `(policy, request, expected
decision)` corpus is reusable by anyone else working on the same problem, which is unusual
for access-control work in a vertical domain.

### To the evidence chain

If its preregistered gates pass, E3 supports measured claims that permitted and disallowed access combinations can be expressed
unambiguously, that an engine returns the expected decision for tested cases, that
decisions are auditable, and that a correction can propagate without rewriting history. It
does **not** license any claim that the policies are complete, socially acceptable, or
legally sufficient — the experiment says so in its own thesis paragraph.

### To risk retirement

E3 is designed to test the "is this just a graph with extra words" objection by comparing a
decision the graph-only control would allow with one the frozen policy layer denies and
reconciling the audit record. Only a passing result can retire that bounded objection. It also front-loads the discovery of policy gaps,
which are far cheaper to find in a conformance suite than in a partner pilot.

### What E3 deliberately does not add

No certification of the organization's broader governance. No proof that the audit log's
underlying events were true. No evidence that partners will accept the policy model — that
is E4's question, and the two must not be conflated.

## Why we are using E3

### The counterfactual

Without E3, "federated" is a word in a diagram. A knowledge graph can connect records
while still permitting overbroad access, silent overwrites, and opaque secondary use — the
distinction E3 exists to make operational. There is a commercial consequence too.
Participation is only conceivable because participants retain control of their raw data;
if E3 has not demonstrated the control mechanism, E4's offers are not credible.

### Alternatives considered and rejected

| Alternative | Why rejected |
|---|---|
| Build a bespoke policy engine | NIST maintains a reference implementation of an ANSI/INCITS standard, free. Building our own would spend Phase I budget re-deriving solved engineering and would move the risk to the wrong place — the hard part is specifying freight policy, not evaluating a decision request |
| Treat NGAC and XACML as interchangeable | SP 800-178 makes their semantic differences explicit. Phase I selects one pinned native lane; a second native lane or declared translation is an optional later comparison whose fixtures, native results, and claims remain separate. A XACML fixture is never run directly against the Policy Machine and called conformant |
| Rely on role-based access control | Not rejected — demoted to C1 and tested. If role-only access turns out to be sufficient for the freight cases, that is a finding worth having |
| Use federated-learning frameworks (Flower, FedML) as the federation demonstration | They solve cross-party *computation*, not gated access. Aim 3's core hypothesis — access restricted to permitted combinations, audited, correctable — is fully testable with the Policy Machine and a conformance suite alone. Recorded as an optional stretch component if Phase I also wants to demonstrate computation without pooling |
| Import FCRA's reinvestigation period as the correction-latency target | The statute applies to consumer reporting agencies and consumer disputes, not freight federation. It informs redress structure only; a freight rule must be authorized and preregistered independently |
| Treat a passing conformance suite as governance validation | The most dangerous available shortcut. Explicitly forbidden in the decision rules |
| Use LEAF as the benchmark structure | LEAF's three-part shape (datasets / evaluation framework / reference implementations) is a good template for packaging a benchmark, but LEAF evaluates ML training under federation, not policy enforcement. Structure borrowed, content irrelevant |

### Cost, dependency, and sequencing

E3's synthetic structural lane needs no partner dataset, purchase, or data agreement. It still
has runtime, authentication, policy-authority, reviewer, and software-version dependencies.
Its programme dependency is internal — the work plan schedules it Months 6–9, after Aim 1 and Aim 2 components are
stable enough to integrate, because the policy subjects are E1's entities and the
protected resources include E2's event summaries. Its real cost is the writing: the
plain-language policy catalogue has to exist before anything is encoded, and that is
legal and commercial judgment, not engineering.

## Research questions

1. Are allowed and disallowed access combinations represented unambiguously?
2. Does the enforcement engine return the expected decision for every tested case?
3. Are denied, permitted, and exceptional requests captured in the audit trail?
4. Can a correction propagate to derived evidence without rewriting history?
5. Does the policy design leak sensitive information through metadata or aggregate outputs?

## Hypotheses and nulls

| ID | Hypothesis | Null / failure interpretation |
|---|---|---|
| H1 | Each pinned engine-native lane conforms to its approved policy test suite for all high-risk cases. | Policy, adapter or implementation gaps remain in that lane. |
| H2 | Disallowed requests are denied and auditable; permitted requests are not over-denied. | Access is unsafe or unusable. |
| H3 | Purpose limitation prevents a valid request in one context from being reused in another. | Context is not carried through enforcement. |
| H4 | Corrections become visible to authorized consumers while the prior record remains auditable. | Correction silently overwrites or fails to propagate. |
| H5 | A specified derived-output release exposes less measured information than a centralized-minimum-data release while retaining preregistered decision utility. | The release offers no measured privacy benefit or loses required utility. |

## Experimental conditions

| Condition | Description |
|---|---|
| C0 | Negative control: policy engine disabled or permissive default; establishes unsafe baseline. |
| C1 | Role-based access only: partner role controls access, without purpose or field sensitivity. |
| C2 | Attribute/purpose-based policy using partner, field class, purpose, time, and consent attributes. |
| C3 | C2 plus correction propagation and challenge workflow. |
| C4 | C2/C3 under authentication and authorization attacks: invalid/expired JWT, wrong issuer or audience, stale consent, role confusion, purpose substitution, replay, privilege escalation, and sandbox/bypass attempts. |
| C5 | Compare a specified federated derived-output release with centralized-minimum-data and no-release controls under one declared attacker, risk, and utility model. |

## Unit of analysis and estimand

- Primary unit: policy/request/expected-decision test case.
- Secondary unit: access event and correction case.
- Primary estimand: conformance rate by policy family and risk class.
- Secondary estimands: false allow, false deny, audit capture, coverage, correction latency,
  and privacy/utility trade-off.

## Data and labels

- [[dataset-nist-policy-machine-xacml-cases]] — synthetic policy/request/expected-decision cases.
- Derived audit records — requester, purpose, decision, timestamp, policy version, and event hash.

Build cases from concrete freight scenarios: a broker may receive a verification summary
for onboarding; a facility may receive an event status needed for dispute resolution; neither
should automatically receive unrelated insurance rates, raw telematics, or another actor’s
commercial terms. Each test must state the expected decision and why.

## Methods

- [[method-policy-conformance-testing]]
- [[method-hash-chained-audit-logging]]

NIST SP 800-192 recommends systematic verification and testing because policy models can
be inconsistent or incomplete and implementations can embed constraints that are not visible
in the policy specification. Use it as the test-design reference: [NIST SP 800-192](https://csrc.nist.gov/pubs/sp/800/192/final).

## Protocol

1. Write the governance policy in plain language before encoding it.
2. Translate each rule into positive, negative, boundary, and conflict cases.
3. Record authority, policy version, effective scope, attributes, request, engine-native expected
   decision, project decision mapping, enforcement-point behavior, and audit expectation.
4. Pin each engine and adapter. For the Policy Machine, reject `none` authentication and
   sandbox/admin bypass in evaluation; require a signed JWT with an approved algorithm, `exp`,
   issuer, audience, token type and subject-to-project-attribute binding. Test missing/expired
   claims, unknown `kid`, JWKS rotation and unapproved claim/URL handling. Run XACML fixtures only
   on the XACML lane.
5. Run C0-C2 against the risk-based suite; do not tune against hidden cases.
6. Run C3 correction cases and measure propagation to each authorized view.
7. Run C4 adversarial and malformed requests, including missing and stale attributes.
8. Capture requests at the policy-enforcement point and reconcile decisions, errors, and
   timeouts against an independently generated request ledger.
9. Verify the declared hash-chain property by attempting alteration, truncation, rollback,
   replay, and chain rebuilding, with external anchoring tested separately if claimed.
10. Run C5 output-release privacy tests and document utility against both controls.
11. Have an independent reviewer inspect policy gaps and false allows.

## Variables

**Inputs:** requester role, organization, field class, purpose, consent/basis, data age,
jurisdiction/contract constraints, policy version, and correction state.

**Treatment:** enforcement condition C0-C5 and policy family.

**Primary outcomes:** false-allow rate, false-deny rate, conformance rate, and audit capture.

**Secondary outcomes:** test coverage, decision latency, correction propagation latency,
replay resistance, policy explainability, privacy leakage, and utility.

**Security guardrails:** no raw data in test outputs; no test fixture may use live secrets;
all failures must preserve minimized request context sufficient for remediation. An unauthenticated
or sandbox/bypass configuration is a failed evaluation setup, not an experimental condition.

## Analysis plan

- Report results by policy family, actor role, field class, purpose, and adversarial case.
- Treat any false allow for a prohibited high-risk combination as a severity-one failure,
  regardless of aggregate pass rate.
- Distinguish policy error from implementation error and from test-oracle error.
- Measure audit completeness independently from decision correctness.
- Test policy mutation: remove or alter one rule and verify the suite catches the regression.

## Initial decision rules

- The acceptance rule for each risk class must be authorized and preregistered before the
  hidden suite is run; no post-result threshold is permitted.
- Any unaudited access, false allow, or untraceable correction blocks advancement.
- 100% structural conformance does not establish that the policy is complete; independent
  governance review remains required.
- No raw-data pooling claim unless the federation and disclosure threat model is documented.

## Threats to validity

- The test suite may omit real policy conflicts.
- The policy oracle may encode the same mistaken assumption as the implementation.
- Synthetic requests will not capture every insider or metadata attack.
- Hash chaining detects alteration but does not prove the original event was true.
- A passing engine can still enforce an unfair or legally inappropriate policy.

## Extended operational specification

### Policy vocabulary

Every policy must be expressible using typed attributes, not informal prose alone:

| Attribute family | Example values |
|---|---|
| Requester | carrier, broker, facility, shipper, insurer, regulator, reviewer |
| Organization | organization ID, contract, stewardship role, partner status |
| Resource | identity claim, insurance status, safety record, event summary, raw telematics |
| Purpose | onboarding, dispute resolution, safety review, analytics, audit |
| Action | read, write, derive, export, correct, challenge, delegate |
| Context | consent/basis, time, jurisdiction, data age, incident state |
| Decision | permit, deny, permit-with-redaction, require-review, abstain |

The last three are project-domain outcomes, not native decisions shared by both engines.
XACML returns Permit, Deny, Indeterminate, or NotApplicable: `permit-with-redaction` requires
a Permit obligation that the PEP demonstrably enforces, while Indeterminate and NotApplicable
follow a preregistered fail-closed or review mapping. NGAC/PML results use their own separately
tested adapter. Preserve every engine-native result alongside the mapped domain outcome.

The policy catalogue must state both allowed and forbidden combinations. “Default deny” is
not enough: the test suite must prove that a permitted workflow remains usable and that a
request cannot gain access by changing only its stated purpose.

### Risk-based test matrix

Exhaust the combinations classified as high severity by the approved policy authority and use
risk-based covering arrays for the remainder; report all uncovered combinations. Add boundary
cases for missing attributes, contradictory
attributes, stale consent, revoked partnership, policy-version mismatch, delegated access,
and emergency override. Mark each case by severity and expected human escalation.

### Oracle separation

The policy author, test-case author, and implementation operator should be separated. Each
expected decision records policy owner, authority or contract citation, effective date,
jurisdiction, version, reviewer, and uncertainty. A reviewer verifies the expected decision
from the plain-language rule before the engine runs.
Otherwise the implementation and test oracle can share the same mistake. Maintain a “policy
uncertainty” set for rules that require legal, commercial, or participant judgment.

### Adversarial suite

Test privilege escalation, confused deputy, replayed authorization, purpose substitution,
identifier substitution, stale-cache access, malformed requests, partial attribute disclosure,
and audit-log truncation. Include attempts by an authorized requester to access a resource
outside the permitted purpose and attempts by a partner to infer denied data from error messages.

### Audit specification

The policy-enforcement point must record each attempted request and response, including
authentication failures, malformed requests, PDP errors, and timeouts, then reconcile that log
to an independent request ledger. Do not infer complete capture from Policy Machine EPP events:
the documented implementation emits them for Admin and Resource operations, not Query operations.
Each access decision must record requester, organization, resource class, purpose, action,
decision, policy version, attributes used, timestamp, correlation ID, and hash pointer. The
audit log must distinguish a denied request, a permitted request, a redacted response, an
abstention, and a system error. Test completeness and semantic correctness alike: a perfectly
complete log of wrong decisions is still a failure. Hash links detect specified alterations
under the declared trust and anchoring model; they do not authenticate the requester, prove
source truth, prevent truncation/rebuilding by a controller, or provide confidentiality.

Canonicalize each entry as UTF-8 RFC 8785 JSON before SHA-256 hashing. Record sequence number,
`prev_hash`, correlation ID, event type, policy/runtime versions and a defined genesis entry;
store a terminal checkpoint independently. The PEP records an attempt before the PDP call and an
outcome afterward so authentication failures, malformed requests, PDP errors and timeouts remain
reconcilable.

### Correction and lineage test

Create a source correction and trace it through raw assertion, canonical claim, derived
summary, downstream view, and audit history. The prior assertion remains visible as
superseded/disputed; the current view updates for authorized users; unauthorized users do not
receive more detail than policy permits. Measure propagation time and identify every stale view.

### Quantitative analysis

Report false-allow and false-deny rates by policy family, severity, actor, resource, purpose,
and missing-attribute condition. Report decision latency distributions, audit capture, test
coverage, mutation-test detection, correction latency, and privacy leakage. A weighted pass
rate may summarize operations, but it may not offset a severity-one false allow.

### Formal and mutation checks

Where possible, check policy consistency, completeness, and conflict before implementation.
Then mutate one policy rule at a time and verify the regression suite catches the change. A
test suite that passes the original policy but misses a material mutation is incomplete.

### Exit and escalation

Any false allow for a prohibited high-risk combination, unaudited decision, or untraceable
correction blocks pilot use. A passing suite authorizes only the tested policy version and
attribute vocabulary; it is not a certification of the organization’s broader governance.

## Contract with the experiment programme

- **Inputs:** E1 actor identifiers and identity confidence; E2 resource, sensitivity, provenance,
  and correction-lineage classes; an authority-reviewed policy catalogue; version-pinned engines,
  adapters, authentication configuration, and independent request ledger.
- **Conditions:** C0-C5 as defined above. Phase I build acceptance requires one declared pinned
  native engine lane. A comparison may add the other lane later, but NGAC/PML and XACML fixtures
  remain separate; C5 uses a declared centralized-minimum/no-release comparison.
- **Outputs:** native and mapped decisions, PEP-enforced obligations/redactions, reconciled audit
  evidence, correction-lineage results, coverage, mutation results, and privacy/utility estimates.
- **Gates:** authorized oracle; valid authentication; sandbox/bypass disabled; engine/adapter pin;
  PEP capture reconciled to the request ledger; risk-based coverage disclosed; acceptance and
  privacy rules preregistered; independent governance review.
- **Consumers:** E4 consumes only approved burden/equity summaries; E5 consumes authorized,
  purpose-limited derived state; no consumer receives raw E1/E2 inputs by implication.

## Build-start specification

Phase I starts with exactly one declared pinned engine-native lane. If both are later built, keep NGAC/PML and XACML policy,
request, response and expected-result fixtures separate. Use a neutral domain-decision schema and
preserve the native decision before explicit mapping. The first package includes an independent
oracle, JWT/JWKS fixture issuer, PEP harness, append-only attempt ledger, deterministic hash-chain
format, correction cases and mutation/adversarial suites under
[[e1-e5-build-readiness-and-run-contract]].

Smoke acceptance requires a human-approved synthetic oracle, exact engine/adapter/runtime hashes,
authentication and sandbox protections, enforcement of every obligation defined by the selected
native lane, reconciliation of every attempt, alteration/truncation/replay tests, a caught single-rule mutation, preserved
superseded correction history and a complete run packet. `C5` remains an optional separately
gated privacy experiment; policy conformance does not imply privacy. Adapter-parity testing and
the XACML-specific PEP obligation test are required only when both lanes, or XACML respectively,
enter the declared build scope.

## Required outputs

1. Plain-language policy catalogue and attribute dictionary.
2. Versioned conformance suite with expected decisions.
3. Enforcement and audit logs with integrity verification.
4. Correction-propagation report.
5. Threat model and privacy/utility report.
6. Independent policy-gap review and remediation list.

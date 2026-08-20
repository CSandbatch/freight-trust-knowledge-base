---
type: experiment
id: E1
status: planned
phase: phase-i
owner: technical-lead-plus-domain-adjudication-panel
schema_version: 1.0.0
updated: 2026-08-20
primary_outcome: identity-resolution-quality-at-fixed-false-positive-ceiling
tags:
- type/experiment
- lifecycle/planned
- domain/freight
- domain/identity
---
# E1 — Entity Resolution and Identity Assurance

Protocol standard: [[experiment-protocol-standard]].

## Thesis

The primary E1 question is whether one prospectively selected non-manual resolver (`C*`) can
increase legal-person auto-resolution yield over the transparent deterministic baseline C1 while
meeting a preregistered assignment-precision safety floor and the same human-review budget. The
incremental value of graph context (C3) and the effect of model assistance on operational-review
correctness and time (C4 versus C0) are separate secondary questions; a C2 or C6 win does not by
itself validate the graph mechanism, and the confirmatory C1-versus-`C*` result does not by itself
establish a manual-workflow time saving.

E1 separately represents FMCSA registrant continuity, identifier assignment/use, corporate
succession/affiliation, substantial operational continuity, and regulatory dispositions. It does
not collapse those relationships into “same carrier.” Whether the system can produce a fraud or
risk score is not under test. The controlling semantic contract is
[[e1-carrier-identity-and-relationship-standard]] (`1.0.0-rc1`, pending PI/domain freeze).

## How E1 tests the Freight Trust thesis

The programme thesis begins with a practical claim: freight participants cannot make
defensible decisions when identity and credential evidence is fragmented, stale, or
unexplainable. E1 tests the first load-bearing link in that chain.

| Thesis layer | What E1 contributes |
|---|---|
| Fragmented records create uncertainty | Tests whether observations can be resolved to the correct legal person while distinguishing identifier assignment, registrant continuity, and related-but-distinct entities. |
| A shared evidence graph can improve decisions | Tests whether temporal and relational context adds measurable value beyond field-by-field matching. |
| Trust must be explainable and contestable | Requires evidence packets, source lineage, reviewer rationale, abstention, and correction, not a score alone. |
| The system must not become a new exclusion mechanism | Measures false positives, subgroup performance, burden, and outcomes for small carriers. |
| The system should support human judgment, not replace it | Treats uncertain cases as reviewable and measures review time rather than optimizing only automated coverage. |

E1 estimates, under the declared population, jurisdiction/source, time, evidence, and review
conditions, whether the proposed identity substrate is technically credible enough to justify
further bounded integration work. It says nothing about whether freight becomes safer or fraud
disappears. If E1 fails, E2-E5 may still be useful as isolated experiments, but the programme
cannot responsibly claim that its shared evidence layer has a validated identity foundation.

### How the methods connect to the thesis

- **Deterministic matching** establishes a transparent constructed rules baseline. It is not
  represented as current practice unless a real operating workflow is documented and mapped to
  the frozen rules. If C3 cannot beat C1 at comparable false-positive risk, a graph-specific
  performance claim is not justified.
- **Probabilistic resolution** tests whether uncertainty can be represented quantitatively
  instead of disappearing inside brittle yes/no rules. Calibration connects output to review policy.
- **Graph-assisted resolution** tests the infrastructure claim itself: identity is a network of
  attributable evidence, not only row-level similarity or an opaque risk score.
- **Expert adjudication** supplies contestability and reveals whether the underlying identity
  question is determinate at all.

### How the conditions map to decisions

C0-C1 ask whether current practice is sufficient. C2 tests uncertainty-aware evidence. C3
tests whether relationships add value. C4 tests safe human workflow. C5 tests whether the
method survives the record changes and source conflicts that motivate the trust layer.

## Provenance

### Where E1 came from

E1 is the operational form of seven programme inputs: four dated findings plus three design/control artifacts already in this vault.
Nothing in its design originates with the experiment file itself.

| Origin | What it contributed to E1 | Status |
|---|---|---|
| [[goals]] G14 — "Build the freight evidence benchmark" | The requirement that Phase I produce an *adjudicated* sample of identity cases with provenance labels against which precision, recall, calibration, and abstention can be measured. E1 is the identity half of G14. | Open; scan complete, benchmark not built |
| [[review-notes]] R-WN-04 — "Evaluation dataset absent" (severity: high) | The finding that no adjudicated U.S. freight identity benchmark was located, and the required action: create a labeled benchmark and *preregister* the measures. E1's preregistration discipline exists because of this finding. | Open |
| [[review-notes]] R-WN-03 — "Automated-score liability risk" (severity: high) | The requirement for abstention, human review, correction, and appeal before consequential use. This is why C4 exists and why E1 is framed as identity resolution rather than risk scoring. | Open; tracked as G13 |
| [[review-notes]] R-WN-05 — "Small-carrier equity remains inferential" (severity: medium) | The requirement to segment outcomes by fleet size rather than assert equity. This is why fleet-size band is a predeclared subgroup estimand, not a post-hoc slice. | Open |
| [[improvement-suggestions]] items 2, 3, 4, 5, 6 | Baseline/intervention/threshold/failure-condition framing (2); benchmark as a named deliverable (3); separation of authoritative identity evidence from inferred risk indicators (4); formal abstention path (5); fleet-size subgroup metrics in the primary design (6). | Adopted |
| [[dataset-scan-entity-resolution]] (compiled 2026-08-01; FMCSA refresh 2026-08-18) | Concrete seed/access/tooling findings, gated sources, and bounded negative retrieval results. Superseding confirmed source cards control current FMCSA claims. | Current |
| [[04-sbir/drafts/phase-1-project-description-draft]] Section 3 (Aim 1) | The proposal-side commitments E1 has to satisfy: beat the deterministic baseline at a matched operating point, report calibration and fleet-size error slices, Month 6 milestone, and the stated failure condition. | Draft |

### Provenance of each input

The entity-resolution scan distinguished three tiers: confirmed and directly accessible,
gated behind money or a signed agreement, and not identified in the documented search. Public
download access does not establish redistribution rights or fitness for a benchmark, so E1 still
requires source-by-source rights and case-closure review.

| Input | Origin and publisher | Access mechanism | License / terms | Verification status | What it can support | What it cannot support |
|---|---|---|---|---|---|---|
| [[dataset-fmca-company-census-file]] | FMCSA MCMIS census extract, mirrored on data.transportation.gov | Direct bulk download (CSV/JSON/XML) via Socrata export endpoints; no login, no API key, no access agreement | Metadata license field reads "unknown"; almost certainly public domain as a U.S. government work (17 U.S.C. §105) but **the metadata does not say so** — confirm, do not assume | **High.** Confirmed by direct fetch of the catalog.data.gov page, not a search snippet. Catalog "last updated" 30 July 2026 at scan time | Clean seed entities: legal/DBA name, USDOT number, address, entity type, status; carrier size fields make fleet-size disaggregation structurally feasible | Any labeled fraud or chameleon outcome. It carries no ground truth about identity reuse |
| [[dataset-fmca-registration-insurance-safety-records]] | FMCSA Open Data Program; current Motus operating-authority files and other FMCSA registration/safety families | Official FMCSA successor page and DOT Data Portal/Socrata APIs; current operating-authority files include “All With History” baselines and daily-difference variants | Public access confirmed for the named files; catalog metadata reports **Unknown License**, so reuse and redistribution remain unresolved | **Confirmed, scoped.** The legacy `jeyh-5nsj` L&I record is an empty link-only stub, while current Motus successor datasets, selected fields, and daily cadence are directly verified in [[source-fmcsa-licensing-and-insurance-dataset]] and [[source-fmcsa-mcmis-catalog]] | Time-bounded authority, insurance, registration, and selected safety evidence, subject to predicate-specific field and temporal validation | A blanket licence, complete legacy-to-Motus schema mapping, guaranteed delivery time, or legal-person gold truth |
| [[dataset-e1-adjudicated-carrier-identity-cases]] | No qualifying public corpus was identified in the documented search through 2026-08-18; the reference standard is to be built by this project | Blinded expert review over permitted source records | [[e1-carrier-identity-and-relationship-standard]] + [[e1-adjudication-decision-tree]]; RC1 complete, PI/domain/counsel freeze pending; per-source rights remain required | **To-build.** This is a bounded negative retrieval result, not proof that no such corpus exists | Layered Task A/B/C reference labels, reviewer disagreement, and typed relationships | No real-world prevalence/detection rate. Every numeric target in Aim 1 stays bracketed until the corpus exists |

Sources deliberately excluded, and why:

- **Historical/longitudinal MCS-150 snapshots (2000–2019).** A MuckRock FOIA request
  (Control #2019-3095) for semi-annual snapshots was marked "Fully Granted" in February
  2021, but the released files are a scanned image and a short PDF of correspondence —
  not bulk data. FMCSA said it "can't go as far back as requested." This is a **hard
  blocker**: the documented retrieval did not produce a ready-made historical snapshot series
  for tracking reincorporation over time. A new, narrowly scoped FOIA is a plausible path but cannot be a Phase I
  dependency, because its timeline is outside the project's control.
- **OpenCorporates.** Real and directly relevant — company formation dates, officers,
  registered addresses across 140+ jurisdictions — but bulk access requires a paid plan
  or a free at-scale research grant contingent on open-license republication. Pricing was
  confirmed only through third-party aggregators, not OpenCorporates' own page. Treated
  as an application/budget step the scan could not complete, not as a secured source.
- **State Secretary of State registries.** The signal that would most directly expose a
  "new company, old carrier" discontinuity, but fragmented across 50 states with no
  common portal, format, or bulk-access programme. Not researched state by state.
- **FMCSA SAFER Company Snapshot.** Live and free, but one carrier per query. Scripted
  bulk querying is not confirmed as permitted, so it is not treated as a bulk path.

### Provenance of each method

E1's four methods are not equally novel. Two are established practice used as honest
floors, one is the claim under test, and one is a human process.

| Method | Intellectual origin | What E1 borrows | What must be adapted or built | Known limitation |
|---|---|---|---|---|
| [[method-deterministic-entity-matching]] | Standard record-linkage practice; also the shape of the real current workflow (rules-based MC/DOT lookup) | The transparent, auditable floor. If the graph cannot beat this at comparable false-positive risk, the graph language is not justified | Normalization rules specific to carrier legal names, DBA conventions, and identifier namespaces | Brittle to spelling changes, ownership changes, missing fields, and deliberate identity variation — the adversarial case |
| [[method-probabilistic-entity-resolution]] | Fellegi–Sunter-style probabilistic linkage, named as a candidate method in the Project Description Section 2; toolchain precedent in the `recordlinkage` Python toolkit and the Febrl datasets it bundles (Christen, ANU) | Weighted field similarity, blocking, and a calibrated threshold as a stronger statistical baseline | Calibration protocol and false-positive ceiling; the Febrl/Febrl-derived data is *person* records, so only the method transfers | Requires labels and calibration; published numbers from person-name benchmarks are not transferable to carrier records |
| [[method-graph-assisted-entity-resolution]] | The programme's own architectural claim, supported by peer-reviewed work on knowledge graphs for multi-hop supply-chain relationships (Brintrup et al. 2022; AlMahri, Xu, Brintrup 2026, cited in Project Description Section 2) | Multi-hop conflict detection across owner, insurer, broker, vehicle, address, and filing edges | The edge set itself, and the leakage controls that keep a graph edge from smuggling the label into the features | Can amplify incomplete or biased source relationships; the least-proven of the three, which is why it is a condition and not an assumption |
| [[method-expert-adjudication]] | Multi-reviewer gold-label practice plus the domain-specific legal/regulatory distinction established in the 2026-08-08 identity-definition research | Two independent reviewers blinded to model/candidate scores, `UNRESOLVED` allowed, third-reviewer adjudication, original votes preserved, agreement and sensitivity analysis | Panel composition/COI policy and PI/domain/counsel freeze remain open; the rubric/decision tree now exist | Costly, and not perfect ground truth. Disagreement is a reportable result and can expose a specification defect |

### Provenance of the benchmark-construction method

No labeled chameleon-carrier dataset was identified in the documented search. Every
candidate source either describes a detection methodology without releasing the matched
pairs, is a single enforcement case requiring manual reconstruction, or could not be
verified. E1's construction path therefore borrows methodology from outside freight:

| Borrowed from | Domain of origin | What transfers | What explicitly does not transfer |
|---|---|---|---|
| **North Carolina Voter Registration (NCVR) linkage benchmark** — the highest-value analog found | Public voter registry, person records | The technique: researchers periodically re-download a public registry and use a persistent identifier (NCID) to establish ground truth across time, instead of a vendor label. Structurally identical to re-pulling the FMCSA census / L&I daily-diff feed and using USDOT continuity — or its absence — as a temporal ground-truth signal | Content. These are people, not organizations, and NC's registry has no analog to operating authority or insurance |
| **Magellan / `py_entitymatching` benchmark suite** (Mudgal et al., SIGMOD 2018) | Product and bibliographic records | The clean-versus-"dirty"-variant construction pattern: systematically corrupt a clean benchmark to produce a harder labeled variant, with a documented 3:1:1 split convention | Its published precision/recall figures. Different data characteristics; importing those numbers as targets would be unfounded |
| **GeCo** (Tran, Vatsalan, Christen, SIGMOD 2013) and its maintained successor **Gecko** (`ul-mds/gecko`) | Synthetic person-identity generation | The generate-then-corrupt engine: frequency-table-driven typos, edit errors, field swaps, deletions at controlled, documented rates | Its frequency tables. GeCo/Gecko ship person-name corpora; carrier legal-name conventions, DBA patterns, address-abbreviation variants, and MC/DOT transcription-error patterns must be authored from scratch. Original GeCo is Python-2.7-era and unmaintained since 2013 |
| **WDC Product Data Corpus gold standard** | E-commerce product offers | The scale pattern: a small, manually adjudicated gold standard drawn from a much larger weakly-labeled corpus — the plausible shape for FMCSA's large unlabeled population plus a small adjudicated subset | Everything else |
| **GAO-12-364** (March 2012), retrieved and confirmed directly | Federal audit of motor-carrier registration | The operational definition of "chameleon attributes": a carrier (1) submitted registration information matching a previously registered carrier, **and** (2) that prior carrier had a motive for evading detection, such as a safety-violation history. Reported prevalence rose from 759 (2005) to 1,136 (2010); 18% of chameleon-attribute applicants were involved in severe crashes versus 6% of other new applicants | The underlying matched-record dataset — GAO does not release it. The specific matching field list (ownership, address, phone) appears in trade-press summaries, not confirmed in the primary GAO text |
| **DOT OIG enforcement precedent** — Billingslea guilty plea announced 11 April 2024, involving multiple reincarnated carriers | Prosecuted federal case | One real, named, adjudicated chameleon pattern usable as a hand-verified qualitative positive control | Statistical power. It is one case, and turning it into even a single benchmark example requires independent court-record and registration-history research |

The consequence must survive into the proposal: a synthetic corruption pipeline can
simulate only the *surface* errors — typos, field noise, missing values. It cannot manufacture the *underlying adversarial reincorporation pattern* GAO's
two-prong definition targets, because the second prong is a motive, not a field. Any
chameleon-detection evaluation in Phase I therefore rests on (a) a handful of
hand-researched real cases, which are qualitative and not statistically powered, and (b)
deliberately constructed re-registration scenarios, which test whether the method can
detect a *designed* pattern — not whether it detects real chameleon carriers at any
measured rate. E1 keeps that distinction.

### Provenance of the individual design choices

| Design choice | Why it is there, and whose finding forced it |
|---|---|
| Time-forward holdout is *primary*, random split is a diagnostic | Deployment encounters future records. The NCVR precedent establishes that temporal ground truth is obtainable by re-pulling a registry; H5 exists to expose the gap between the two split types, so that no random-split number stands as a deployment estimate |
| Blocking recall reported separately from end-to-end recall | Papadakis et al. on blocking and nearest-neighbor search: a method that never generates the true candidate cannot recover it downstream. Aggregate recall hides this |
| An **unknown/unresolved** label that is never forced into binary truth | Failure mode F01 (label ambiguity) in [[experiment-protocol-standard]], plus the GAO motive prong that public records cannot settle. Forcing a binary would fabricate certainty the sources do not contain |
| Abstention and a human review queue as their own condition (C4) | R-WN-03 and G13: no automated indicator decides eligibility, pricing, contracting, or liability without human review. Improvement item 5 makes this a formal path, not a caveat |
| Fleet-size band as a predeclared subgroup, with equity as a blocking gate | GAO-16-401R: approximately 99.1% of FMCSA-regulated carriers meet small-business standards. A method that degrades on small carriers degrades on nearly the whole population. R-WN-05 and improvement item 6 |
| Entity-clustered bootstrap rather than pair-level intervals | Pairs drawn from one carrier are not independent; pair-level intervals would overstate precision. Failure mode F03 (entity contamination) |
| Calibration evaluated on its own terms — reliability diagrams, ECE, Brier, coverage-risk | The Project Description names Bayesian calibration and conformal-prediction-style abstention sets as *candidates to be evaluated, not assumed*. Calibration connects a score to a review policy; without it, C4's abstention has nothing to threshold on |
| Numeric floors deliberately left unset until after the label count and baseline review | The scan found no comparable published benchmark for carrier registration records. Inventing a precision target now would violate the no-borrowed-numbers rule and would be unfalsifiable |

## Prior-art boundary after identity-definition research

E1 cannot claim to invent automated chameleon/reincarnation screening or point-in-time identity
verification. GAO demonstrated registration-data matching as a targeting method; FMCSA then
implemented match+motive screening and later the URSA risk tool, whose lineage includes a prior
SBIR Phase I and automated chameleon/reincarnation risk assessment. In 2026, FMCSA Motus also
separates individual identity verification from company-account/business verification, while
NMFTA SCAC Verified performs a form of lifecycle-point identity assurance.

The defensible E1 novelty question is narrower: whether a **source-attributed, temporally
coherent, contestable identity graph** can improve legal-person resolution under missing,
corrupted, and conflicting anchors while preserving distinct relationship/disposition semantics,
calibrated uncertainty, and human abstention. See [[source-fmcsa-ursa-risk-screening-prior-art]],
[[source-fmcsa-motus-identity-and-business-verification]], [[source-gao-12-364-chameleon-carrier-matching]],
and [[source-nmfta-scac-verified-and-standards-role]].

## What E1 adds

### To the proposal

- It converts Aim 1 from an assertion into a preregistered comparison with a named
  baseline, a matched operating point, a declared failure condition, and a Month 6
  go/no-go. R-WN-01 and improvement item 2 asked for this.
- It supplies the one section of the proposal where "we confirmed a real, no-agreement
  data source" can be said honestly: the FMCSA Company Census File moves Aim 1 from "no
  dataset exists" to "one confirmed seed source plus a documented construction method."
- It makes the small-carrier commitment measurable, not rhetorical. Section 9's
  broader-impacts claim is not reviewable otherwise.

### To the benchmark artifact

E1 leaves behind the identity half of the G14 benchmark: a versioned ontology and identity
standard; canonical legal-person clusters; separate FMCSA registrant/identifier-continuity
labels; typed relationships among distinct persons; frozen train/development/test manifests with
entity-disjoint and time-forward views; reviewer-level labels/disagreement; hard negatives
(shared addresses, name collisions, ownership transitions, stale records, reused phone numbers,
claimed-versus-assigned identifiers, conflicting sources); and an error taxonomy. This is a reusable asset even if
the product hypothesis fails — improvement item 3's entire point.

### To the evidence chain

E1 licenses these claims, and only these: that carrier records from multiple authoritative
sources can (or cannot) be resolved without assuming identifier permanence; that temporal
and relational context does (or does not) add measurable value over field matching; that
confidence scores are (or are not) reliable enough to triage review. It does **not**
license any claim about fraud reduction, and its results say nothing about industry-scale
outcomes.

### To risk retirement

E1 retires the first technical unknown in the chain: whether the identity substrate is
credible enough for anything else to rest on it. It also surfaces, early and cheaply, the
two failure modes that would be most expensive to discover in a pilot — a graph that
leaks labels through its edges, and an error pattern concentrated on small carriers.

### What E1 deliberately does not add

It is not a risk score, not a fraud detector with a measured real-world detection rate,
not a compliance determination, and not evidence that private carrier workflows behave
like public records. A benchmark pass is not authorization to make a consequential
carrier decision. The exit conditions say so too.

## Why we are using E1

### The counterfactual

Without E1, every downstream experiment inherits an unmeasured assumption. E2's event
traces attach to entities nobody verified. E3's policies govern access to claims about
entities whose resolution quality is unknown. E4 asks carriers to participate in a system
whose first function has never been evaluated. E5 optimizes across actors that may not be
distinct actors. E1 failing is survivable — E2 through E5 remain individually useful — but
the programme could not then claim its shared evidence layer has a reliable identity
foundation. That claim is load-bearing for the whole thesis.

### Alternatives considered and rejected

| Alternative | Why rejected |
|---|---|
| Use an existing public ER benchmark (Magellan, WDC, Febrl) as the evaluation set | Different domains with different data characteristics. The scan is explicit that their published precision/recall must not be imported as if transferable. They contribute methodology only |
| Buy bulk OpenCorporates or commercial trade data | Cost, and nothing is secured. A Phase I whose central experiment depends on an unsigned commercial license is not a credible plan |
| FOIA the historical MCS-150 snapshot series | The 2019 precedent was granted and still produced no usable data. Timeline outside project control |
| Rely on synthetic corruption alone | It can only manufacture surface noise. The adversarial pattern that motivates the aim would be structurally absent, and a strong result would mean nothing |
| Skip adjudication and use weak/heuristic labels | Reintroduces F01 and F02 (label ambiguity, source leakage) into the one artifact whose value is that it is adjudicated. The benchmark *is* the deliverable |
| Score carriers instead of resolving identity | R-WN-03: a composite score creates opaque, contestable consequences and can be mistaken for a legal standard of care. This is the design mistake the programme exists to avoid |

### Cost, dependency, and sequencing

E1 needs no partner, no signed agreement, and no purchase to start: the seed source is
downloadable today. Its real cost is human — the adjudication panel and case-by-case state/legal
source work. The identity rubric, ontology, decision tree, claims ledger, and 70-case conformance
suite now exist as an RC1 package; the written panel/COI/training rules and Louisiana/Texas source-access pilot now exist; the remaining schedule risk is PI/domain/counsel freeze, actual reviewer training/pilot double-labeling, and case-level retrieval for the first real carriers. It runs first (Project Description work plan, Months
3–6) because E2's entity references, E3's policy subjects, and E4's participant records
all assume a resolved carrier identity.

## Research questions

### Confirmatory question

**RQ1.** In a probability-based, entity-centric, time-forward evaluation cohort, does the single development-selected non-manual E1 system (`C*`) produce greater legal-person auto-resolution yield than the deterministic baseline C1 **while meeting the preregistered assignment-precision safety floor and the same human-review budget**?

### Secondary questions

2. Does graph-assisted temporal/relationship context improve legal-person resolution over a non-graph probabilistic baseline when both receive the same candidate set?
3. Does the end-to-end graph system improve over deterministic/probabilistic systems after each method's candidate-generation errors are included?
4. Can the system separately resolve Task B identifier/registrant continuity and Task C relationships without collapsing them into Task A identity?
5. Does calibrated abstention reduce accepted-case error across the risk/coverage curve and at the operational review-capacity point?
6. How do performance, calibration, abstention, review burden, and error mechanisms vary by fleet size, record age, jurisdiction/source environment, graph degree, missingness and F6a/F6b status?
7. How rapidly does performance degrade under empirically calibrated observation corruption and missingness in the nonrepresentative challenge cohort?
8. Does the frozen C6-LLM challenger add resolution value over the non-LLM probabilistic method
   on the same candidates/evidence, and do any gains survive end-to-end retrieval, evidence-support,
   cluster-consistency, stability, injection, privacy, latency and cost constraints?

## Hypotheses and estimands

Only H1 is confirmatory unless the preregistration explicitly promotes another hypothesis and adds a multiplicity procedure.

| ID | Status | Hypothesis / estimand | Failure interpretation |
|---|---|---|---|
| H1a | Confirmatory safety gate | In Cohort R/F6, the lower 95% CI bound for `C*` design-weighted automatic assignment precision is >= preregistered `P*`. | Automated resolution is not sufficiently precise for the proposed operating point. |
| H1b | Confirmatory utility gate, tested only if H1a passes | At the same `P*` policy and review budget, `C*` improves design-weighted assignment recall/auto-resolution yield over C1 by at least preregistered `Delta*`. | Proposed method does not produce a meaningful workload/coverage gain over transparent rules. |
| H2 | Secondary | C3 graph context improves resolution over C2 on the same common candidate set without increasing related-but-distinct false merges. | Graph structure does not add resolver-level information or adds harmful noise. |
| H3 | Secondary | End-to-end C3/C* improves over baselines when blocking misses and compute are included. | Apparent graph gains vanish when retrieval is evaluated honestly. |
| H4 | Secondary | Calibrated abstention lowers risk as coverage decreases and meets the operational precision floor without excessive deferral. | Confidence is not useful for safe triage. |
| H5 | Secondary validity | Error/burden differences across prespecified groups are small enough to support the intended scope, or are identifiable with actionable mechanisms. | Scope must be narrowed or method redesigned; underpowered groups are reported as insufficient precision, not “pass.” |
| H6 | Preregistered secondary challenger analysis | On the frozen common-candidate/evidence view, C6 improves assignment yield at the declared precision/review point over the designated non-LLM probabilistic comparator while both receive identical case evidence and while meeting frozen evidence-support, reconciliation, instability, injection-resistance, privacy/data-egress, latency and cost gates. The graph-augmented L3 view is excluded from H6 and analyzed only as a separate equal-evidence `resolver family × evidence view` factorial diagnostic. | No positive LLM-specific incremental-value claim is supported. The result is retained and cannot retrospectively change C* selection or the H1 conclusion. |

The primary operational unit is a post-cutoff observation-resolution decision: `LINK_EXISTING`, `CREATE_NEW`, or `ABSTAIN`. Gold identity remains the canonical legal-person partition.

## Experimental conditions

| Condition | Role | Description |
|---|---|---|
| C0 | Operational human comparator only | Documented manual/current review workflow using the same evidence scope but no E1 model assistance. C0 does not define gold truth. |
| C1 | Primary transparent baseline | Frozen deterministic normalized-field/authoritative-anchor rules with explicit new-entity and abstention behavior. |
| C2 | Statistical baseline | Frozen Fellegi-Sunter-style or equivalently preregistered probabilistic linkage model with calibrated probabilities. |
| C3 | Proposed mechanism | Graph-assisted temporal/relationship model using only permitted, source-attributed, pre-cutoff edges. |
| C* | Confirmatory candidate | Exactly one eligible C2/C3/C6 system chosen on development data using the preregistered selection/tie-break rule; C6 is eligible only if its frozen development promotion gates pass. |
| C4 | Operational composite | Frozen `C*` + abstention + a **separate operational reviewer panel**; gold adjudicators do not perform runtime review. |
| C5 | Challenge/stress | Real hard cases plus empirically calibrated missingness/corruption. Nonrepresentative; no population-performance claim. |
| C6-LLM | Preregistered challenger | Fixed LLM/embedding-assisted resolver evaluated under [[method-llm-assisted-entity-resolution]]. It is evidence-bounded, schema-constrained, reconciled into coherent clusters, and conditionally eligible for C* after frozen development gates. |

No C6 implementation or result exists yet, and no benchmark/test is frozen or opened. C6 may
enter the first `C*` development selection only if the preregistered reproducibility, privacy,
evidence-support, injection-resistance, stability, calibration, cost, subgroup, retrieval, and
cluster-reconciliation gates in [[method-llm-assisted-entity-resolution]] are met before test
access. If a gate fails or C6 is not selected, it remains secondary and its outputs are
descriptive; exactly one C2/C3/C6 system reaches the confirmatory holdout as `C*`.

### Resolver-versus-retrieval ablation

Primary method results are **end to end**, including each condition's frozen candidate-generation/blocking pipeline. A secondary common-candidate-set experiment supplies the same broad candidate union to C1-C3 to isolate scoring/graph effects. Candidate recall is never silently assumed to be 100%.

C6 has both views: a common-candidate reranking analysis that isolates its resolver and a frozen
end-to-end analysis that includes its own embedding or other candidate generator. Its bounded
L0-L7 family separates zero/few-shot scoring, retrieval, graph context, evidence-citation,
nondeterminism, memorization/feature reliance, and prompt-injection questions without turning an
unbounded prompt search into model selection.

## Benchmark cohorts

Detailed design: [[e1-benchmark-sampling-and-split-plan]].

- **Cohort R — representative evaluation cohort.** Stratified probability sample from a frozen FMCSA registration frame; entity-centric gold clusters; inclusion probabilities/design weights retained. This cohort supplies headline population estimates.
- **Cohort H — hard/adversarial challenge cohort.** Purposive rare/ambiguous cases and controlled corruptions. Used for failure discovery only.
- **Cohort J — jurisdiction/source-environment holdout.** Secondary external-validity cohort if Phase I resources permit. Otherwise the claim scope is explicitly limited.

A sampled entity enters confirmatory metrics only when its cluster-closure audit is `closed` or meets a preregistered equivalent standard. Incomplete clusters remain visible but are not allowed to masquerade as complete gold truth.

## Split and temporal design

Training/development gold entities and confirmatory test gold entities are disjoint for model fitting, feature learning, thresholding and model selection. This does **not** forbid a deployment-realistic resolver from consulting public pre-cutoff records of a test entity as reference evidence.

F6 is split into:

- **F6a continuing entities:** post-cutoff observation belongs to a legal person with pre-cutoff reference evidence;
- **F6b novel entities:** legal person is absent from the pre-cutoff reference graph; correct action is `CREATE_NEW` or `ABSTAIN`, never forced attachment.

Freeze `T_train_end`, `T_dev_end`, `T_feature_cutoff`, `T_test_start`, `T_test_end` and `T_adjudication_cutoff`. Evidence after the feature cutoff may settle retrospective gold truth but is masked from models, candidate generation, normalization/frequency statistics, graph embeddings, calibration and thresholds.

All learned preprocessing is fit on train/development only. The graph leakage audit must detect future edges, reviewer-created edges, duplicate records across splits, test-derived frequency/degree statistics, and embeddings trained over post-cutoff/test structure.

## Data and labels

- [[dataset-fmca-company-census-file]] — frozen registration sampling frame and seed records.
- [[dataset-fmca-registration-insurance-safety-records]] — permitted time-bounded evidence; negative safety/enforcement/motive history remains excluded from Task A.
- [[dataset-e1-adjudicated-carrier-identity-cases]] — representative and challenge benchmark artifacts governed by the identity standard.

Gold layers remain: **Task A legal-person partition**, **Task B identifier/registrant continuity**, **Task C typed relationships**, and a separate **regulatory-disposition layer**. `UNRESOLVED` remains valid.

The representative corpus is constructed entity-centrically rather than as a bag of model-proposed pairs. This is required because naive benchmark pair precision/F1 can be optimistic and can mis-rank systems. See [[source-binette-2024-entity-centric-er-evaluation]].

## Methods

- [[method-deterministic-entity-matching]]
- [[method-probabilistic-entity-resolution]]
- [[method-graph-assisted-entity-resolution]]
- [[method-llm-assisted-entity-resolution]]
- [[method-expert-adjudication]]
- [[e1-benchmark-sampling-and-split-plan]]
- [[e1-statistical-analysis-and-preregistration-plan]]

### Blocking / candidate generation

Each production condition has a preregistered candidate generator. Report candidate recall/pair completeness, recall@K where relevant, reduction ratio, candidate-set size, latency, downstream recall conditional on retrieval, and total end-to-end recall. Blocking loss is a first-class error source. See [[source-dasylva-goussanou-2021-blocking-false-negatives]].

### Method-selection discipline

Before final test opening, enumerate eligible C2/C3 variants and the conditionally eligible C6 configuration, preprocessing, hyperparameter spaces, random seeds/budget, development metric, promotion gates, and tie-break. Select exactly one `C*` from the gate-qualified systems. Final-test performance of rejected/nonselected configurations is descriptive only and cannot be used to redefine the winner.

## Protocol

1. **Semantic lock:** freeze [[e1-carrier-identity-and-relationship-standard]] and adjudication rules after PI/domain review.
2. **Frame lock:** freeze the Cohort R population frame, strata, inclusion/exclusion rules and source-access scope.
3. **Pilot:** construct a development-only adjudication pilot to estimate nuisance quantities, reviewer disagreement and sample-size requirements.
4. **Preregister:** freeze `P*`, `Delta*`, sample size, primary/secondary estimands, sampling weights, statistical code, candidate generators, subgroup list, corruption levels, hyperparameter budgets and chronology.
5. **Sample/adjudicate:** draw Cohort R with known inclusion probabilities; build clusters using model-independent retrieval; build Cohort H separately.
6. **Train/develop:** fit preprocessing, C2/C3, graph features/embeddings and calibration on train/dev only.
7. **Select C*:** choose exactly one non-manual confirmatory candidate under the preregistered development rule.
8. **Data/code lock:** hash manifests, code, environment, model configs, split files and replicate-weight/bootstrap procedure.
9. **One-shot test:** execute one immutable holdout batch whose manifest names every permitted
   configuration before access. C1 and `C*` are the only confirmatory systems. Any preregistered
   nonselected system included in that same batch is secondary/descriptive and permanently
   consumes its holdout evaluation; no later holdout run, prompt search, or reranking may revise
   C* selection. Preserve all raw predictions before metrics are computed.
10. **Primary analysis:** apply design weights and hierarchical H1a→H1b gate.
11. **Secondary analyses:** cluster metrics, common-candidate ablation, calibration, risk/coverage, Task B/C, subgroups and Cohort H.
12. **Operational C4:** separate reviewers evaluate randomized manual versus assisted cases against independent frozen gold.
13. **Error audit:** classify false merges/splits, blocking misses, source conflict, missingness, graph contamination and reviewer uncertainty.
14. **Independent review:** methods reviewer checks protocol deviations, leakage logs, denominators, weights and claim language before release.
15. **C6 challenger:** before test access, run the frozen development promotion gates and include C6 in `C*` selection only if they pass. If a frozen nonselected C6 configuration is included in the preregistered immutable holdout batch, its result and L0-L7 diagnostics are secondary/descriptive and cannot authorize a later test-set rerun. Retain raw requests/responses under their data classification.

## Primary and secondary outcomes

### Primary

- design-weighted automatic assignment precision (PPV);
- design-weighted assignment recall / auto-resolution yield;
- paired `C* - C1` difference at the same `P*` and review budget.

The joint assignment estimand is accompanied by action-specific `LINK_EXISTING` and `CREATE_NEW`
precision, recall, confusion counts, and harm categories. Pooling the actions must not hide a high
false-attachment or false-new-cluster rate.

### Secondary clustering

- pairwise precision/recall;
- B-cubed precision/recall/F1;
- cluster precision/recall;
- over-merge and under-merge rates/distributions;
- exact-cluster recovery where meaningful.

### Candidate generation

- pair completeness/candidate recall;
- recall@K;
- reduction ratio and candidate-set size;
- blocking contribution to total false negatives.

### Calibration and selective prediction

- calibration intercept/in-the-large;
- calibration slope;
- smooth reliability curve;
- Brier score (and log loss where defined);
- risk-coverage curve;
- accepted-case error and coverage at the preregistered operating point;
- ECE only as a secondary descriptive measure.

### Operational / burden

- review correctness against independent gold;
- review elapsed/active time distribution;
- abstention rate;
- evidence opened/interaction count where instrumented;
- compute latency, memory/candidate volume.

### LLM challenger safety and operability

- schema-valid response and evidence-ID support rates;
- unsupported-assertion, reconciliation-intervention and inconsistent-cluster rates;
- repeated-inference action/target/evidence flip rates;
- masked-versus-unmasked diagnostic degradation and prompt-injection success rate;
- abstention/system-failure cause distribution; and
- token use, per-decision cost, latency, retries, timeouts and provider failures.

## Statistical analysis

Controlling document: [[e1-statistical-analysis-and-preregistration-plan]].

- Use design-weighted estimators for Cohort R.
- Use entity/anchor-level survey-aware resampling within strata; never bootstrap pairs independently.
- Preserve pairing of C1 and C* predictions inside each replicate for the method-difference CI.
- Use 95% intervals under a frozen replicate/interval procedure.
- Primary success is hierarchical H1a safety then H1b utility; only this sequence is confirmatory.
- Challenge-set results are case/failure-mechanism analyses, not prevalence estimates.
- Gold uncertainty is examined through contested-case exclusion, reviewer-specific labels, unresolved bounds, and if warranted a latent-class sensitivity analysis.
- Report subgroup effective sample size and intervals; underpowered groups are `insufficient precision`.

## Sample-size rule

After the development-only pilot, simulation under the actual stratified/entity-centric design determines confirmatory `n`. The preregistration freezes desired CI half-width around the precision safety floor, precision for recall/yield, the meaningful improvement `Delta*`, any power/assurance target, and decision-critical subgroup requirements. If the available adjudication budget cannot satisfy those targets, E1 narrows its claim rather than inventing precision.

## Human adjudication and workflow review

Gold labeling continues under [[e1-adjudicator-governance-and-training]]. Gold adjudicators do not serve as C4 operational reviewers.

Before recruiting reviewers or recording/analyzing their time, correctness, explanations, or
other behavior, obtain a documented determination under the responsible institution or sponsor's
human-subjects process. Investigators do not self-authorize an exemption. Ordinary paid labeling
that produces case labels only must remain operationally and analytically separate from the C4
research panel unless that determination permits the combined design.
The governing source boundary is recorded in
[[source-nsf-common-rule-human-subjects-consent]].

For C0 versus C4, operational reviewers are randomized across manual/assisted cases in a blocked crossover over **different cases**; no reviewer sees the same case twice. Both arms receive equivalent underlying evidence, with model ranking/explanation only in the assisted arm. Accuracy is measured against frozen independent gold; time/correctness analyses account for reviewer and case effects.

## Initial decision rules

Numbers remain pilot-dependent but the structure is now fixed:

1. **No automatic-use claim unless H1a passes:** lower 95% CI bound for assignment precision >= `P*`.
2. **No superiority claim unless H1b passes:** lower 95% CI bound for `C* - C1` auto-resolution yield/recall >= `Delta*` at matched review budget.
3. No headline use of F0 anchor-visible performance.
4. No headline population metric from Cohort H.
5. No deployment recommendation from benchmark performance alone.
6. No subgroup “pass” where effective sample size/CI is inadequate.
7. Reopen protocol if cluster closure fails systematically, gold disagreement remains high after training, a new source/feature is added after lock, or leakage is discovered.

## Threats to validity and mitigations

| Threat | Mitigation |
|---|---|
| Benchmark convenience/hard-case bias | Probability-based entity-centric Cohort R; Cohort H separated. |
| Incomplete gold clusters | Model-independent retrieval + cluster-closure status; report design-weighted closure failure and reasons, define the closure-eligible estimand, and run preregistered bounds/sensitivity analysis so exclusion does not silently redefine the target population. |
| Blocking false negatives | Candidate recall/pair completeness and end-to-end metrics. |
| Pairwise metric distortion | B-cubed/cluster/merge-split metrics plus operational observation assignment. |
| Gold-reviewer error | Independent duplicate review, adjudication, agreement reporting, sensitivity analyses. |
| Graph/future/test leakage | Entity-disjoint model development, frozen feature cutoffs, train-only transforms, graph path audit. |
| Model shopping | One development-selected `C*`; final test opened once. |
| Calibration illusion | Intercept/slope/reliability/Brier + risk-coverage, not ECE alone. |
| Abstention hiding subgroup failure | Coverage/error reported jointly and by prespecified groups. |
| Temporal drift | F6 primary time-forward analysis; F6a/F6b separated. |
| Jurisdiction/source heterogeneity | Sampled source adapters + optional Cohort J; scope limited if external holdout unavailable. |
| Synthetic corruption unreality | Empirically calibrated observation-noise perturbations; genuine business events treated as real temporal cases. |
| Human workflow carryover | Separate operational panel; each reviewer sees each case once. |
| LLM public-record memorization / future knowledge | No external tools; L6 masking/randomization and chronology diagnostics; residual pretraining contamination disclosed. |
| Prompt injection in source fields | Treat source text as untrusted data; strict delimiters/schema; no tools; L7 challenge cases and fail-closed abstention. |
| LLM hallucinated or unsupported evidence | Evidence-ID output contract; unknown IDs/unsupported assertions fail validation and are counted. |
| Hosted-model privacy/data egress | Field-level approval and minimized evidence view; restricted evidence remains controlled or uses an approved self-hosted model. |
| Model/provider drift and nondeterminism | Exact route/configuration manifest, no dynamic router/fallback, repeated-inference stability test, new version on any change. |

## Required outputs

1. Identity-definition package: [[e1-carrier-identity-and-relationship-standard]], [[e1-identity-ontology.yaml]], [[e1-adjudication-decision-tree]], [[e1-identity-claims-ledger]], [[e1-edge-case-suite.csv]], [[e1-definition-freeze-review]].
2. Academic methods package: [[e1-academic-design-review]], [[e1-benchmark-sampling-and-split-plan]], [[e1-statistical-analysis-and-preregistration-plan]], [[e1-reporting-and-reproducibility-checklist]].
3. Frozen frame/sample/split/chronology and feature-regime manifests with inclusion probabilities and cluster-closure status.
4. Versioned representative Cohort R plus separate Cohort H challenge corpus and optional Cohort J.
5. Baseline/proposed method configuration cards, hyperparameter budgets and selected `C*` decision record.
6. Raw one-shot test predictions, design/replicate weights and complete metric output.
7. Primary safety/utility gate report; clustering/candidate/calibration/abstention/subgroup reports; false-merge/split taxonomy.
8. Operational manual-versus-assisted workflow report using a reviewer panel separate from gold adjudicators.
9. Reproducibility archive and deviations log under [[e1-reporting-and-reproducibility-checklist]].
10. Go/no-go recommendation that explicitly states the population/jurisdiction/source scope supported by the evidence.
11. C6 configuration/model card, prompt and provider manifests, common-candidate and end-to-end raw outputs, L0-L7 diagnostic report, privacy approval, contamination/injection/stability audit, promotion-gate decision, and selected-versus-secondary claim label.

## References

- [Papadakis et al., blocking and nearest-neighbor search for entity resolution](https://arxiv.org/abs/2202.12521)
- [Unsupervised Evaluation of Entity Resolution](https://doi.org/10.1145/3721985)
- [[source-binette-2024-entity-centric-er-evaluation]]
- [[source-lam-2026-ambiguity-aware-clerical-review]]
- [[source-dasylva-goussanou-2021-blocking-false-negatives]]
- [[source-chipperfield-2018-linkage-precision-recall-estimation]]
- [[source-harron-2017-linkage-quality-guide]]
- [[source-bailey-2019-record-linkage-bias]]
- [[source-traub-2024-selective-classification-evaluation]]
- [[source-van-calster-2016-calibration-hierarchy]]
- [[source-dasylva-2016-clerical-review-quality]]

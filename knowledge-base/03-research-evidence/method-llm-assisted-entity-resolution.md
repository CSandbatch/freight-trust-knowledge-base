---
type: method
status: candidate
schema_version: 1.0.0
updated: 2026-08-18
tags:
- type/method
- lifecycle/candidate
- domain/freight
- domain/identity
- domain/data-science
- confidence/mixed
- audience/internal
- programme/e1
---
# LLM-Assisted Entity Resolution

This method defines `C6-LLM`, a bounded learned challenger for E1. It tests whether a fixed
language-model or embedding-assisted pipeline can improve legal-person resolution when it is
given only the same permitted, pre-cutoff evidence available to the other E1 methods. It does
not make the model a source of facts, an adjudicator, a legal decision-maker, or a chameleon-
carrier detector.

No C6 implementation, model selection, benchmark run, or result exists yet. This note is a
candidate protocol component for preregistration.

The condition is justified as a test, not an assumed improvement. Published generative-LLM
matching results show competitive behavior and prompt sensitivity on product/bibliographic
benchmarks, while realistic open-entity/imbalanced reconstruction can materially reduce apparent
performance; none establishes freight legal-person resolution. See
[[source-peeters-2025-llm-entity-matching]],
[[source-wang-2022-reality-ideality-entity-matching]], and
[[source-li-2021-ditto-deep-entity-matching]].

## Intended role

C6 has two evaluation views:

1. **Common-candidate resolver view.** C6 receives the frozen broad candidate union also used
   in the C1-C3 resolver ablation. This is the primary mechanism comparison because it isolates
   scoring/reasoning from retrieval.
2. **End-to-end view.** C6 uses its own frozen production candidate generator, which may include
   an embedding retriever, followed by the same fixed resolver. Candidate recall, compute, cost,
   and blocking misses remain part of the result.

The common-candidate view cannot establish production performance. The end-to-end view cannot
attribute a gain to the resolver unless the retrieval ablation supports that interpretation.
If a candidate-set selection prompt is used, candidate order is randomized or counterbalanced in
development diagnostics and then frozen because position can change LLM selection performance;
see [[source-wang-2025-comem-llm-entity-matching]].

Adaptive operator/model routing is outside the default C6 protocol. Although
[[source-guo-2026-carl-em-cost-aware-llm-entity-matching]] provides peer-reviewed precedent for
cost-aware selection among matching, comparing, selecting, and deciding operations, importing
such a controller would create a separately versioned method. Its policy, model pool, action
space, training data, budget, stopping rule, provider routes, and development selection rule would
all have to be frozen before it could become eligible; it cannot be introduced through a silent
provider router or post-test cost optimization.

## Permitted input

Each request contains a machine-serialized evidence packet derived only from records permitted
by the case's `feature_cutoff`. Task A, Task B, Task C, and regulatory-disposition fields are
separated. Every fact carries an evidence ID, source class, observation/valid time, and claim or
authority status.

C6 receives no:

- post-feature-cutoff evidence;
- gold label, reviewer rationale, candidate-generation score, or test-set statistic;
- safety, enforcement, bankruptcy, fraud, or motive history for Task A;
- outside retrieval, browser, tool, or model-generated evidence;
- restricted field not approved by the data-management and privacy review.

If C6 receives raw narrative text while another resolver receives only extracted fields, that is
reported as a different evidence-interface/system comparison, not a resolver-only comparison.

## Structured output contract

C6 returns schema-validated data, not free-form truth:

```yaml
case_id: ...
action: LINK_EXISTING | CREATE_NEW | ABSTAIN
target_legal_person_id: ... | null
task_a_label: SAME_LEGAL_PERSON | DISTINCT_LEGAL_PERSON | UNRESOLVED | OUT_OF_SCOPE
evidence_ids: []
conflict_evidence_ids: []
abstain_reason: insufficient_evidence | conflicting_evidence | no_candidate | schema_failure | policy_failure | other | null
model_score: ... | null
```

Every substantive output must cite packet evidence IDs. A missing/unknown evidence ID,
unsupported factual assertion, invalid schema, unavailable model, exhausted retry budget, or
policy violation becomes `ABSTAIN` or a recorded system failure under the frozen rule. Model-
written explanations are hypotheses about supplied evidence, not evidence themselves.

A model's self-reported confidence is not treated as a probability. Calibration may use only a
predeclared score available reproducibly from the frozen pipeline and a calibrator fit on
development data. [[source-kamsteeg-2025-entity-matching-calibration]] supports separating
calibration from discrimination but does not validate verbal confidence from a hosted generative
model.

## Cluster reconciliation

Pair/candidate outputs cannot directly define Task A truth. A frozen reconciliation layer checks
symmetry, transitivity, conflicting assignments, new-entity behavior, and the identity standard's
hard prohibitions before producing a legal-person partition. Report:

- raw C6 decisions;
- reconciled decisions;
- the number and type of decisions rejected or changed;
- inconsistent-cycle and multi-cluster conflict rates; and
- performance before and after reconciliation.

Reconciliation may reject or abstain; it may not invent evidence or silently convert a Task C
relationship into Task A equivalence.

## Frozen L0-L7 ablation family

The preregistration fixes the exact prompts, models, providers, evidence views, development
selection rule, and compute/call budget. The named ablations are:

| ID | Purpose |
|---|---|
| L0 | Structured-field, zero-shot common-candidate reranker. |
| L1 | Same resolver with a fixed set of examples selected only from development data. |
| L2 | Frozen embedding candidate retrieval followed by the fixed resolver; evaluated end to end. |
| L3 | Evidence-view factorial diagnostic: adds source-attributed, pre-cutoff typed graph paths to the fixed common-candidate resolver and compares both C6 and its designated non-LLM comparator with and without the identical graph serialization. |
| L4 | Removes the evidence-ID requirement as an unsafe diagnostic of whether citation constraints change behavior; never eligible for operational use or promotion. |
| L5 | Repeats a frozen case subset to measure within-configuration decision instability and API nondeterminism. |
| L6 | Masks/randomizes names and identifiers on a frozen diagnostic subset to probe public-record memorization and feature reliance; not a population-performance estimate. |
| L7 | Injects inert instruction-like strings into untrusted evidence fields to test prompt-injection resistance; challenge analysis only. |

L0-L2 are bounded method variants. L3-L7 are diagnostics and cannot be selected as the headline
system. L3 cannot support an LLM-specific incremental-value claim: it is a preregistered
`resolver family × evidence view` factorial contrast, with identical case evidence and graph
serialization supplied to C6 and the designated non-LLM comparator. The H6 common-candidate
contrast uses the selected C6 resolver on the same case-evidence packet as its comparator and
excludes the graph-augmented L3 view. Rejected configurations, prompts, development scores, and
failures remain in the run log.

## Model and provider lock

The run manifest records the exact model identifier and revision where available, provider,
endpoint class, prompt/system-template hashes, output schema, sampling parameters, seed support,
token limits, retry and timeout rules, fallback policy, tool availability, request timestamps and
IDs, code/environment hash, and raw responses. Dynamic routers and silent provider/model fallback
are prohibited. A provider, model, prompt, evidence schema, or reconciliation change creates a
new method version.

For an approved OpenRouter run, pin the provider/model, disable unplanned fallbacks, require
supported parameters, request routing metadata, and set `data_collection: "deny"` and `zdr: true`.
Those vendor controls do not replace data authorization or minimization; see
[[source-openrouter-routing-privacy-and-metadata]].

Nominal temperature zero is not assumed deterministic. L5 measures flip rate, action agreement,
target-cluster agreement, and evidence-citation stability across repeats.

## Contamination and prompt-injection controls

A hosted model may have memorized public carrier records, including evidence later than E1's
feature cutoff. Tool isolation alone cannot prove clean pretraining. C6 therefore:

- declares the provider's documented training/data limitations where known;
- performs L6 masked/randomized-name and identifier diagnostics;
- uses chronology canaries and records whose later public outcome was unavailable at prediction
  time where feasible;
- reports the residual contamination risk rather than claiming it is eliminated; and
- cannot use C6 output to construct or close the gold cluster.

All source text is untrusted data. Evidence is strongly delimited/encoded, instructions inside
record fields are ignored by contract, no tools or external retrieval are exposed, schema output
is validated, and L7 measures instruction-following failures. A successful injection is a safety
failure even if the final match label happens to be correct.

## Privacy and data-egress controls

Public availability does not by itself authorize third-party model processing. Before hosted C6
calls, freeze a field-level data-egress review covering provider retention/training terms,
jurisdiction, logging, contractual use, sensitive-person fields, and source redistribution terms.
SSNs remain prohibited; EINs, familial relationships, private partner records, restricted state
filings, reviewer identity, and full internal adjudication packets remain excluded unless a later
approved protocol explicitly permits them.

Use a minimized public-record view for the first hosted evaluation or an approved self-hosted
model where the necessary evidence cannot leave the controlled environment. Request/response
logs inherit the most restrictive input classification and are never published merely because
aggregate metrics are public.

## Metrics

C6 receives every applicable E1 metric plus:

- schema-valid response rate;
- unsupported-assertion and unknown-evidence-ID rate;
- evidence citation precision/coverage under a frozen audit sample;
- abstention and system-failure rate by cause;
- reconciliation intervention and inconsistency rates;
- L5 action/target/evidence flip rates;
- candidate-order-induced action/target/evidence flip rates;
- L6 masked-versus-unmasked performance change;
- L7 prompt-injection success rate;
- input/output tokens, per-decision cost, latency distribution, retries, timeouts and provider
  failures; and
- performance and abstention by fleet size, F6a/F6b, source environment, missingness, graph
  degree, and feature regime.

Accuracy and explanation faithfulness are separate outcomes. A fluent rationale cannot repair an
incorrect match or unsupported evidence use.

Model-generated explanations may later be studied as auditable teacher-to-student artifacts, but
they remain predictions rather than gold and may transmit teacher errors; see
[[source-wadhwa-2024-explanation-distillation-entity-matching]].

## Confirmatory eligibility and promotion

Because no E1 benchmark or confirmatory test is frozen or opened, C6 is a prospectively
preregistered challenger that may become eligible for the first `C*` selection only after all of
these development-only gates pass:

1. exact model/provider/prompt/schema/reconciliation and compute budget are locked;
2. privacy/data-egress approval is recorded for the frozen evidence view;
3. schema, evidence-support, injection-resistance, instability, latency/cost, and subgroup
   ceilings are numerically frozen and met;
4. calibration and abstention can be defined without self-reported confidence;
5. candidate generation and cluster reconciliation pass their audits; and
6. C6 enters the same frozen development selection/tie-break rule as other eligible non-manual
   systems, with exactly one C2/C3/C6 system selected as `C*` for the confirmatory holdout.

If any gate fails, C6 remains a secondary challenger and cannot become `C*`; any frozen C6
holdout outputs are descriptive/secondary. If the gates pass, eligibility does not guarantee
selection: development performance and the preregistered tie-break still select exactly one
`C*`. All nonselected model/prompt outputs remain descriptive. No post-test prompt/model
selection, favorable rerun, or provider substitution can promote C6.

## Claim boundary

A positive C6 result can support only a scoped claim that the frozen LLM-assisted pipeline
improved a declared E1 benchmark outcome under the stated evidence, cohort, time, provider, cost,
and review conditions. It cannot establish legal identity, regulatory reincarnation, fraud,
deployment fitness, future-model performance, industry-wide benefit, or autonomous suitability
for consequential carrier decisions. For a hosted model, the result is performance of the exact
dated black-box model/provider route and evidence interface. It does not establish clean temporal
learning, absence of pretrained public-record knowledge, a causal benefit from language-model
reasoning, or generalization to a later model/provider version.

Related: [[dec-013-llm-e1-challenger]] · [[gap-018-e1-llm-readiness]] · [[experiment-e1-entity-resolution-and-identity-assurance]] · [[e1-carrier-identity-and-relationship-standard]] · [[e1-benchmark-sampling-and-split-plan]] · [[e1-statistical-analysis-and-preregistration-plan]] · [[e1-reporting-and-reproducibility-checklist]] · [[dataset-e1-adjudicated-carrier-identity-cases]]

## Sources

[[source-peeters-2025-llm-entity-matching]] ·
[[source-wang-2025-comem-llm-entity-matching]] ·
[[source-li-2021-ditto-deep-entity-matching]] ·
[[source-wang-2022-reality-ideality-entity-matching]] ·
[[source-kamsteeg-2025-entity-matching-calibration]] ·
[[source-wadhwa-2024-explanation-distillation-entity-matching]] ·
[[source-guo-2026-carl-em-cost-aware-llm-entity-matching]] ·
[[source-openrouter-routing-privacy-and-metadata]]

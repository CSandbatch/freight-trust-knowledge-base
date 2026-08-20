---
type: source
status: active
schema_version: 1.0.0
source_class: peer-reviewed
verification: confirmed
accessed: 2026-08-18
updated: 2026-08-18
review_by: 2028-08-18
tags:
- type/source
- domain/identity
- domain/data-science
- confidence/peer-reviewed
- audience/internal
- programme/e1
- lifecycle/active
---
# Wadhwa et al. 2024 - explanation distillation for entity matching

## Citation and verification

Somin Wadhwa, Adit Krishnan, Runhui Wang, Byron C. Wallace, and Luyang Kong. "Learning
from Natural Language Explanations for Generalizable Entity Matching." *Proceedings of
EMNLP 2024*, 6114-6129. DOI: 10.18653/v1/2024.emnlp-main.352.

<https://aclanthology.org/2024.emnlp-main.352/>

The full paper and authoritative ACL Anthology metadata were retrieved on 2026-08-18.
The conditional-generation formulation, explanation-distillation method, ablations, and
out-of-domain evaluation were confirmed.

## What the source supports

The paper recasts pairwise entity matching as conditional generation and trains smaller
models using natural-language explanations derived from a larger LLM. Its experiments
report improved out-of-domain generalization, including a 10.85-point F1 improvement in
the study's cross-domain setting, and ablations associate the explanation supervision with
performance and robustness gains. The approach is motivated by the high inference cost of
using a large generative model for every candidate pair.

This supports testing distillation as a later cost/throughput strategy if an E1 LLM teacher
first demonstrates valid behavior against independently adjudicated gold.

## Limits

- The numerical gain belongs to the paper's product-domain and split design; it is not an
  expected E1 effect size.
- An explanation used as training supervision is still model-generated. It is not gold,
  provenance, or proof that the stated rationale caused the teacher's decision.
- Distillation can reproduce teacher errors and biases while making them cheaper to scale.
- The work is pairwise and does not establish legal-person cluster coherence, calibrated
  abstention, or safe human-review behavior.

## E1 relevance

E1 may evaluate a distilled student only after the teacher and training-data permissions
are frozen. Human adjudicators, not the LLM, remain the reference standard. Store the
teacher version, prompt, raw output, explanation, filtering rules, and resulting student
training example so the lineage of every distilled label is auditable.

## Consumers

[[experiment-e1-entity-resolution-and-identity-assurance]] ·
[[method-probabilistic-entity-resolution]] ·
[[e1-reporting-and-reproducibility-checklist]]

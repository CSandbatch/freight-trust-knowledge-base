---
type: source
status: active
schema_version: 1.0.0
source_class: peer-reviewed-workshop
verification: confirmed
accessed: 2026-08-18
updated: 2026-08-18
review_by: 2027-08-18
tags:
- type/source
- domain/identity
- domain/data-science
- confidence/peer-reviewed
- audience/internal
- programme/e1
- lifecycle/active
---
# Kamsteeg et al. 2025 - confidence calibration in entity matching

## Citation and verification

Iris Kamsteeg, Juan Cardenas-Cartagena, Floris van Beers, Tsegaye Misikir Tashu,
and Matias Valdenegro-Toro. "Confidence Calibration in Large
Language Model-Based Entity Matching." *Proceedings of the 2nd Workshop on
Uncertainty-Aware NLP (UncertaiNLP 2025)*.

- ACL Anthology: <https://aclanthology.org/2025.uncertainlp-main.12/>
- Authors' manuscript: <https://arxiv.org/abs/2509.19557>

The full workshop paper and ACL Anthology record were retrieved on 2026-08-18. The tested
model, datasets, calibration methods, repetitions, and reported metrics were read directly.

## What the source supports

The study evaluates a RoBERTa entity matcher on Abt-Buy, DBLP-ACM, iTunes-Amazon, and a
company dataset. It compares uncalibrated sigmoid outputs with temperature scaling,
Monte Carlo dropout, and ensembles. Baseline ECE varies by dataset; temperature scaling
reduces ECE in several reported cases without changing the underlying F1 predictions.

The work supports measuring calibration separately from discrimination and fitting any
post-hoc calibration only on development data.

## Limits

- Despite the title's use of "large language model," the empirical matcher is RoBERTa,
  an encoder classifier. The paper does not calibrate a hosted generative LLM's free-text
  or verbalized confidence.
- ECE is bin-dependent, and a lower ECE does not prove a safe abstention policy at E1's
  high-precision operating point.
- The dataset-specific findings and workshop-scale study do not establish freight-domain
  calibration or subgroup safety.
- Monte Carlo dropout and ensembles require access patterns that may not exist for a
  closed hosted model.

## E1 relevance

Do not treat an LLM's self-reported percentage as an assignment probability. E1 must
declare the actual confidence signal, calibrate it on development only, and report
calibration intercept/slope, a smoothed reliability plot, Brier score, and risk/coverage
behavior. This source is evidence for that evaluation posture, not validation of a specific
generative-LLM calibration method.

## Consumers

[[e1-statistical-analysis-and-preregistration-plan]] ·
[[experiment-e1-entity-resolution-and-identity-assurance]] ·
[[e1-reporting-and-reproducibility-checklist]]

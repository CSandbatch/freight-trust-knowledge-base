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
# Wang et al. 2022 - reality versus ideality in entity-matching benchmarks

## Citation and verification

Tianshu Wang, Hongyu Lin, Cheng Fu, Xianpei Han, Le Sun, Feiyu Xiong, Hui Chen,
Minlong Lu, and Xiuwen Zhu. "Bridging the Gap between Reality and Ideality of Entity
Matching: A Revisiting and Benchmark Re-Construction." *Proceedings of IJCAI 2022*,
3978-3984.

- IJCAI record and paper: <https://www.ijcai.org/proceedings/2022/552>
- Authors' manuscript: <https://arxiv.org/abs/2205.05889>

The IJCAI record and full authors' manuscript were retrieved on 2026-08-18. Venue,
authorship, benchmark interventions, and reported evaluation scope were confirmed.

## What the source supports

The paper identifies three benchmark assumptions that can inflate entity-matching results:
test entities or records covered by training data, artificially balanced match/non-match
labels, and records restricted to simplified modalities. It reconstructs benchmarks toward
open entities, imbalanced labels, and more realistic records and reports substantial
degradation of evaluated methods under those conditions.

The result supports evaluating entity matching in the open, imbalanced environment in
which it will actually operate instead of relying only on randomly split candidate pairs.

## Limits

- The experiments do not use E1 carrier data or its legal-person ontology.
- The paper does not establish a universal correction factor between standard-benchmark
  and deployment performance.
- It predates the main generative-LLM matching studies and therefore does not directly
  compare a current hosted LLM with Fellegi-Sunter or E1's graph method.
- Its benchmark results support design choices, not numeric E1 acceptance thresholds.

## E1 relevance

The source strongly supports E1's entity-disjoint, time-forward F6 evaluation, explicit
F6b novel-entity cohort, naturally imbalanced representative cohort, and separation of
development selection from the one-shot final test. A public product benchmark may be a
pipeline smoke test, but it cannot answer E1's scientific question.

## Consumers

[[e1-benchmark-sampling-and-split-plan]] ·
[[experiment-e1-entity-resolution-and-identity-assurance]] ·
[[e1-statistical-analysis-and-preregistration-plan]]

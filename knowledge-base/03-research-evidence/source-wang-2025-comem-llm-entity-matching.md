---
type: source
status: active
schema_version: 1.0.0
source_class: peer-reviewed
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
# Wang et al. 2025 - ComEM matching, comparing, and selecting

## Citation and verification

Tianshu Wang, Xiaoyang Chen, Hongyu Lin, Xuanang Chen, Xianpei Han, Le Sun, Hao Wang,
and Zhenyu Zeng. "Match, Compare, or Select? An Investigation of Large Language Models
for Entity Matching." *Proceedings of COLING 2025*, 96-109.

- ACL Anthology record and paper: <https://aclanthology.org/2025.coling-main.8/>
- Authors' manuscript: <https://arxiv.org/abs/2405.16884>

The full paper and ACL Anthology metadata were retrieved on 2026-08-18. The eight-dataset,
ten-model evaluation and the definitions of matching, comparing, selecting, and ComEM were
confirmed.

## What the source supports

The paper shows that binary independent pair classification is only one way to prompt an
LLM for entity matching. It compares: independent pair matching; pairwise comparison among
candidates; and selecting a match from a candidate set. The proposed ComEM framework uses
a filtering strategy before candidate-set selection and reports improved effectiveness and
cost-efficiency across its benchmark suite.

The study also reports position bias in candidate selection: accuracy falls as the true
match appears later in a candidate list. This is directly relevant to ranked candidate
packets and to any proposal to let an LLM resolve several carrier candidates jointly.

## Limits

- Candidate-set selection is not a legal-person clustering algorithm and does not by
  itself enforce transitivity across all observations.
- Results on eight established ER datasets do not transfer numerically to E1.
- Candidate ordering, set size, and filtering become additional learned or engineered
  components whose errors must be measured end to end.
- The paper does not validate calibrated abstention or a high-consequence false-positive
  threshold.

## E1 relevance

E1 should compare a simple evidence-grounded pairwise LLM with any candidate-set LLM
variant rather than assuming one prompt topology is sufficient. Candidate order must be
randomized or counterbalanced in development tests, and common-candidate-set versus
end-to-end results must remain separate. An LLM selection result is evidence for a frozen
cluster resolver, never canonical identity truth by itself.

## Consumers

[[experiment-e1-entity-resolution-and-identity-assurance]] ·
[[method-graph-assisted-entity-resolution]] ·
[[e1-reporting-and-reproducibility-checklist]]

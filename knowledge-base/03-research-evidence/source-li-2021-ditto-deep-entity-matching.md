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
# Li et al. 2021 - Ditto deep entity matching

## Citation and verification

Yuliang Li, Jinfeng Li, Yoshihiko Suhara, AnHai Doan, and Wang-Chiew Tan. "Deep
Entity Matching with Pre-Trained Language Models." *Proceedings of the VLDB Endowment*
14(1), 2021, 50-60. DOI: 10.14778/3421424.3421431.

- Paper: <https://www.vldb.org/pvldb/vol14/p50-li.pdf>
- Authors' artifact: <https://github.com/megagonlabs/ditto>

The full PVLDB paper and artifact repository were retrieved on 2026-08-18. The paper states
the model architecture, benchmark families, optimization methods, large company-matching
case, and artifact location.

## What the source supports

Ditto serializes two structured records as text and fine-tunes BERT-, DistilBERT-, or
RoBERTa-family encoders as a binary sequence-pair classifier. It adds optional domain-
knowledge tags, TF-IDF-based summarization, and data augmentation. The paper evaluates
standard entity-matching benchmarks and reports a large-scale application matching two
company datasets containing 789,000 and 412,000 records.

Ditto is therefore a credible supervised Transformer matcher against which a generative
LLM condition can be compared when sufficient E1 development labels exist. The paper also
keeps blocking and matching conceptually separate.

## Limits

- Ditto is a fine-tuned encoder classifier, not a prompted generative LLM.
- Most published benchmark results concern product and bibliographic data. The company
  application does not establish performance on U.S. motor-carrier legal-person identity.
- The output is pairwise match/non-match. The paper does not supply E1's `UNRESOLVED`,
  `CREATE_NEW`, temporal-relation, or cluster-coherence semantics.
- Reported F1 values cannot be imported as E1 targets, and the released implementation's
  older dependency stack requires a separately frozen reproduction environment.

## E1 relevance

Ditto is a useful learned baseline or later student model, not a replacement for C2. E1
must evaluate it with the same time-forward entity-disjoint splits, candidate generator,
false-positive ceiling, calibration, abstention policy, and cluster metrics used for every
other condition.

## Consumers

[[method-probabilistic-entity-resolution]] ·
[[experiment-e1-entity-resolution-and-identity-assurance]] ·
[[e1-reporting-and-reproducibility-checklist]]

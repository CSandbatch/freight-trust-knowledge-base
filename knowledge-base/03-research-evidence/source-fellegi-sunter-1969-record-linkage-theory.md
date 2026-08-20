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
# Fellegi and Sunter 1969 - a theory for record linkage

## Citation and verification

Ivan P. Fellegi and Alan B. Sunter. "A Theory for Record Linkage." *Journal of the
American Statistical Association* 64(328), 1969, 1183-1210.
DOI: 10.1080/01621459.1969.10501049.

<https://doi.org/10.1080/01621459.1969.10501049>

The article metadata and abstract were retrieved from the DOI record on 2026-08-18.
Publication, authorship, journal, pagination, and the three-decision formulation were
confirmed.

## What the source supports

The paper develops a likelihood-ratio framework for deciding whether two records describe
the same person, object, or event from their comparison pattern. Its decision space has
three outcomes: link, non-link, and a possible-link region where the evidence is
insufficient for either automatic disposition. The theory selects decision regions subject
to stipulated bounds on false-link and false-non-link errors.

This is the primary intellectual source for a Fellegi-Sunter-style C2 baseline and for
treating review/abstention as part of record linkage rather than as an LLM-specific add-on.

## Limits

- The framework is pairwise; it does not by itself produce a coherent multi-record legal-
  person partition.
- Its optimality result is conditional on the modeled match and non-match comparison
  distributions and the stated decision problem. It does not guarantee that estimated
  weights or error rates are correct under misspecification, dependent fields, sampling
  bias, temporal drift, or weak labels.
- It predates learned representations, graph evidence, and generative LLMs.
- It establishes a method, not a performance target transferable to freight records.

## E1 relevance

E1 should retain a separately implemented and calibrated Fellegi-Sunter-style baseline.
An LLM challenger does not make this baseline obsolete. The source also supports explicit
`LINK`, `NON_LINK`, and review/possible-link behavior at declared error tolerances, while
E1's legal-person ontology and cluster-reconciliation policy remain project-specific.

## Consumers

[[method-probabilistic-entity-resolution]] ·
[[experiment-e1-entity-resolution-and-identity-assurance]] ·
[[e1-statistical-analysis-and-preregistration-plan]]

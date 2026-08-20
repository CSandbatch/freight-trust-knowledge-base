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
# De Meer Pardo et al. 2025 - GraLMatch group matching

## Citation and verification

Fernando De Meer Pardo, Claude Lehmann, Dennis Gehrig, Andrea Nagy, Stefano Nicoli,
Branka Hadji Misheva, Martin Braschler, and Kurt Stockinger. "GraLMatch: Matching Groups
of Entities with Graphs and Language Models." *Proceedings of EDBT 2025*, 1-12.

- Paper/manuscript: <https://arxiv.org/abs/2406.15015>
- EDBT proceedings: <https://www.openproceedings.org/html/pages/2025_edbt.html>

The full authors' manuscript and EDBT proceedings record were retrieved on 2026-08-18.
The company/securities use case, synthetic multi-source benchmarks, graph-cleanup method,
and reported precision finding were confirmed.

## What the source supports

GraLMatch studies multi-source entity group matching where sources update company and
financial-security records at different times. It shows how a small number of false-
positive pair predictions can connect many records transitively and corrupt entire groups.
Its graph-cleanup procedure uses graph properties to identify and remove some suspect
positive edges before final grouping.

The experiments also show that the pair matcher with the most or the most elaborate
training was not necessarily best at group resolution; high pairwise precision can be
decisive once transitive closure amplifies false links.

## Limits

- The proposed cleanup only partially detects false positives; it is not a proof of
  coherent or correct legal-person clusters.
- The language model in the reported pipeline is a fine-tuned Transformer encoder, not a
  prompted generative LLM reasoning over E1 evidence paths.
- The benchmarks are company/securities analogues, not U.S. motor-carrier adjudications.
- Transitive information can help matching, but E1 may not infer legal-person equivalence
  transitively from affiliation, shared address, ownership, equipment, or another weak
  typed relationship.

## E1 relevance

This is the closest source in the LLM/Transformer set to E1's group, temporal, and company
setting. It supports treating LLM pair outputs as fallible edges, evaluating complete
clusters, reporting over-merge size, and prioritizing the false-positive ceiling. Any E1
graph cleanup must preserve edge type, time, source, and contradiction rather than convert
all connectivity into identity equivalence.

## Consumers

[[method-graph-assisted-entity-resolution]] ·
[[experiment-e1-entity-resolution-and-identity-assurance]] ·
[[e1-statistical-analysis-and-preregistration-plan]]

---
type: source
status: active
schema_version: 1.0.0
source_class: vendor
verification: confirmed
accessed: 2026-08-18
updated: 2026-08-18
review_by: 2026-11-18
tags:
- type/source
- domain/data-science
- domain/privacy
- confidence/vendor
- audience/internal
- programme/e1
- lifecycle/active
---
# OpenRouter - routing, privacy, and router metadata documentation

## Citation and verification

OpenRouter official documentation, retrieved in full on 2026-08-18:

- "Data Collection": <https://openrouter.ai/docs/guides/privacy/data-collection>
- "Provider Routing": <https://openrouter.ai/docs/guides/routing/provider-selection>
- "Zero Data Retention": <https://openrouter.ai/docs/guides/features/zdr>
- "Router Metadata": <https://openrouter.ai/docs/guides/features/router-metadata>

All four pages were readable on the vendor's official domain. This card records current
product behavior claimed by OpenRouter; it is not independent validation.

## What the vendor documentation establishes

OpenRouter states that it does not retain prompt/response content unless an account opts
into private input/output logging or use of inputs/outputs. It states that request metadata,
including token counts and latency, is retained separately from prompt/response content.

Provider routing defaults to load balancing across available providers and permits
fallbacks. The request `provider` object can constrain provider order, disable fallbacks,
require supported parameters, set `data_collection: "deny"`, and set `zdr: true` to limit
routing to endpoints OpenRouter classifies as zero-data-retention. OpenRouter also offers
opt-in router metadata describing the requested model, strategy, region, provider/model
candidates, selected endpoint, attempts, and guardrail pipeline.

## Limits

- These are vendor assertions about OpenRouter and its representation of downstream
  provider policies, not an audit, contractual legal opinion, or certification that a
  dataset is safe to transmit.
- Endpoint availability and provider policies can change after the access date.
- ZDR addresses retention as OpenRouter defines it; it does not eliminate processing by a
  third party, metadata collection, network exposure, contractual constraints, or E1 data-
  governance review.
- Router metadata documents routing activity; it does not expose model weights, training
  data, hidden provider transformations, or deterministic inference.
- `openrouter/auto`, default load balancing, and fallbacks are unsuitable for attributing a
  confirmatory research result to one stable model/provider configuration.

## E1 relevance

Any hosted E1 LLM run should pin the exact model and approved provider, disable unplanned
fallbacks, require supported parameters, request router metadata, and record the returned
provider/model/routing fields with the run artifact. Where approved data is transmitted,
set `data_collection: "deny"` and `zdr: true`; these controls supplement but do not replace
data minimization and authorization. Restricted adjudication material remains out of the
hosted path unless separately approved.

Because these pages are mutable, the card carries a short `review_by` interval. Freeze the
retrieved documentation or a content hash in the experiment's reproducibility package when
the hosted condition is preregistered.

## Consumers

[[aws-experiment-execution-and-findings-plan]] ·
[[experiment-e1-entity-resolution-and-identity-assurance]] ·
[[e1-reporting-and-reproducibility-checklist]]

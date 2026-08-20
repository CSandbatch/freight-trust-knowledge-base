---
type: source
status: active
schema_version: 1.0.0
source_class: vendor
verification: confirmed
accessed: 2026-08-20
updated: 2026-08-20
review_by: 2027-02-18
tags: [type/source, domain/provenance, domain/software, confidence/primary, audience/internal, programme/e2, lifecycle/active]
---
# OpenEPCIS Test Data Generator

## Citation and verification

OpenEPCIS, `epcis-testdata-generator`, official repository and documentation, inspected
2026-08-18: <https://github.com/openepcis/epcis-testdata-generator> and
<https://openepcis.io/docs/test-data-generator/>. Repository license: Apache-2.0. The README
documented container image tag `0.9.4` at access time. Formal release `v0.9.4` was published
2024-11-14 at commit `60866b2e9802484b035d6b5bb6b82d4b16794155`. Repository HEAD inspected
2026-08-20 was `ab2b62a324e23f0bb7a26ab9e18bc0705f787177` dated 2026-07-14.

## Exact support

Supports local, configurable generation of EPCIS test data and documents the project's own
software interfaces and container use.

## Limits and E2 relevance

This is project/vendor documentation, not GS1 authority or peer-reviewed freight evidence.
It does not establish normative conformance, realistic facility behavior, or ground truth.
E2 should qualify the formal release first, pin a commit and image digest, record config and seed,
validate output against GS1, and license project-added data separately. The release/HEAD choice is
unresolved. Docker was unavailable during this audit, so the registry image digest was not
retrieved and must not be represented as pinned.

Consumers: [[dataset-openepcis-generated-event-logs]] · [[method-event-log-generation-and-anomaly-injection]]

---
type: source
status: active
schema_version: 1.0.0
source_class: primary
verification: confirmed
accessed: 2026-08-20
updated: 2026-08-20
review_by: 2027-02-18
tags:
- type/source
- domain/freight
- domain/orchestration
- confidence/primary
- audience/internal
- programme/e5
- lifecycle/active
---
# FMCSA — property-carrying driver hours of service

## Citations

Federal Motor Carrier Safety Administration. “Summary of Hours of Service Regulations.”

<https://www.fmcsa.dot.gov/regulations/hours-service/summary-hours-service-regulations>

Electronic Code of Federal Regulations. 49 CFR Part 395.

<https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-395>

## Supported propositions

For covered property-carrying operations, the federal framework includes driving, duty-window,
break, off-duty, cycle, and exception rules. The FMCSA summary includes the 11-hour driving limit
after 10 consecutive hours off, the 14-hour window, the break after eight cumulative driving
hours without a qualifying interruption, and the 60/70-hour limits, subject to applicability and
exceptions in Part 395.

## Limits

The summary is guidance; the regulation controls. Applicability and exceptions depend on the
driver and operation. E5 must not represent “HOS tightening” as current law; it may use an
explicitly non-legal synthetic stress case after implementing the applicable conformance layer.
The first implementation must declare its covered operating population and base rules; sleeper,
restart, adverse-driving, short-haul and other exceptions are included only with explicit scope
and test vectors.

## Consumers

[[experiment-e5-orchestration-value]] · [[method-synthetic-orchestration-simulation]]

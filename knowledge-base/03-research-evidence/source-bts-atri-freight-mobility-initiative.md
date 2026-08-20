---
type: source
status: active
schema_version: 1.0.0
source_class: primary
verification: confirmed
accessed: 2026-08-20
updated: 2026-08-20
review_by: 2027-02-18
tags: [type/source, domain/freight, domain/data-access, confidence/primary, audience/internal, programme/e2, lifecycle/active]
---
# BTS–ATRI Freight Mobility Initiative truck travel times

## Citation and verification

U.S. Bureau of Transportation Statistics, *Trucking Movements: BTS Freight Mobility* and
FMI county-pair dataset, inspected 2026-08-18:
<https://www.bts.gov/explore-topics-and-geography/topics/freight-transportation/trucking-movements-bts-freight-mobility>,
<https://doi.org/10.21949/1530061>, and <https://data.bts.gov/d/d7b8-pmxm>.

## Exact support

The official methodology supports annual 2018–2024 county-pair elapsed-movement quantiles
derived from roughly 350,000 core tractors. BTS identifies the data as U.S. public domain
and suppresses movements with fewer than 100 observations while binning released counts.

## Limits and E2 relevance

A movement is not a trip and can include stops; the product remains experimental. County-pair quantiles are not appointment,
gate, dock, service, dwell, detention, or partner truth. E2 may calibrate timing distributions
and check held-out published quantiles; it may not infer facility service time by subtraction.
Any implementation must pin the methodology DOI, annual files/checksums, extraction date,
county-pair/year selection and the fewer-than-100 suppression rule.

Consumers: [[dataset-bts-truck-travel-time-data]] · [[method-travel-time-calibration]]

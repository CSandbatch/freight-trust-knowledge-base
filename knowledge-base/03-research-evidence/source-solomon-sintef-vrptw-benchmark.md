---
type: source
status: active
schema_version: 1.0.0
source_class: mixed
verification: confirmed
accessed: 2026-08-20
updated: 2026-08-20
review_by: 2028-08-18
tags:
- type/source
- domain/orchestration
- domain/data-science
- confidence/mixed
- audience/internal
- programme/e5
- lifecycle/active
---
# Solomon and SINTEF — VRPTW benchmark and comparison convention

## Citations

Marius M. Solomon. “Algorithms for the Vehicle Routing and Scheduling Problems with Time
Window Constraints.” *Operations Research* 35(2), 1987, 254–265.

<https://pubsonline.informs.org/doi/10.1287/opre.35.2.254>

SINTEF. “Solomon benchmark,” published 2008.

<https://www.sintef.no/projectweb/top/vrptw/solomon-benchmark/>

## Supported propositions

The Solomon instances are established VRPTW test problems. SINTEF reports best-known results
under a hierarchical objective: first minimize vehicles, then distance, using double-precision
Euclidean distance and specified rounding for reported totals.

Solomon is the peer-reviewed methods source; SINTEF is an organizational benchmark resource.
This combined card therefore uses mixed source metadata rather than treating both as one source
class.

## Limits

SINTEF explicitly warns that monolithic objectives and integral or low-precision distance/time
conventions are not directly comparable. A benchmark run is not solver qualification unless E5
pins the instance, objective, precision, solver/runtime, time limit, seed, status/gap, and an
independent feasibility check.
It does not validate HOS, governance, uncertainty, actor economics or Freight Trust value.

## Consumers

[[experiment-e5-orchestration-value]] · [[method-synthetic-orchestration-simulation]]

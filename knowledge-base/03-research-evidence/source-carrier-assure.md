---
type: source
status: active
schema_version: 1.0.0
source_class: vendor
verification: confirmed
accessed: 2026-08-07
updated: 2026-08-07
review_by: 2027-02-07
tags:
- type/source
- domain/freight
- domain/identity
- confidence/vendor
- audience/internal
- programme/g4
- programme/g5
- lifecycle/active
---
# Carrier Assure — vendor product documentation

**Classification.** Architecture: **closed proprietary scoring database; undisclosed
algorithms, no knowledge-graph or interoperability claim.** Primary focus: **fraud
detection** (carrier performance and double-brokering risk scoring).

## Citation

Carrier Assure. "How It Works." <https://www.carrierassure.com/how-it-works> — retrieved
2026-08-07.

## What the source establishes, in its own terms

The scoring product, verbatim: **"algorithms use real-time data from the FMCSA, tracking
systems, and user reports to give you a simple A-F score."** The company states it
compares **"each carrier to similar-sized peers"**.

The fraud signal is crowd-sourced and human-reviewed, verbatim: **"Users can flag serious
issues like double brokering, fraud, hostage loads, theft, and unresolved balances. Every
report is reviewed and verified by our team before it affects the score."**

Named inputs: **"FMCSA DOT safety records"**, **"Project44 data"** for GPS tracking, and
user reports from shippers and brokers. Stated processing volume, verbatim: **"over
2,000,000 million DOT numbers every day"**.

Method is described only as **"hundreds of algorithms"**.

## Axis-1 finding

No knowledge graph, ontology, open standard, or interoperability framework is claimed. The
score is a proprietary output over a proprietary blend of public records, a commercial
telemetry feed, and a private user-report channel. The user-report channel is a closed
reputation ledger — it is Carrier Assure's, and its contents are not portable.

## Finding not currently in the G4 row

The page names **project44 as a data supplier** to Carrier Assure. Two entries on the same
competitor list stand in a supplier relationship. Whoever reconciles G4 should decide
whether the register treats them as independent competitors.

## Limits and scope

Vendor self-description; not independent validation. **"over 2,000,000 million DOT numbers
every day"** is internally malformed as written on the vendor's own page — "2,000,000
million" is not a coherent quantity, and the intended figure cannot be recovered from the
page. It is recorded verbatim here and **must not be cited as a volume figure**. The A–F
score has no published validation study, no ground-truth definition, and no error rate.

Conflict of interest carried forward from [[evidence]] G5: Carrier Assure's founder/CEO
Cassandra Gaines is the releaser of the CAVRA Standard. Vendor framework, not neutral
standard.

## Consumers

[[evidence]] G4 competitor table, Carrier Assure row; [[evidence]] G5 CAVRA entry.

---
type: source
status: active
schema_version: 1.0.0
source_class: unverified
verification: retrieval-failed
accessed: 2026-08-07
updated: 2026-08-07
review_by: 2026-11-07
tags:
- type/source
- domain/freight
- domain/identity
- confidence/unverified
- audience/internal
- programme/g4
- action/needs-adjudication
- lifecycle/active
---
# "RMJ" — unidentified entry in the G4 competitor register

**Classification: none. The referent could not be established, so neither axis can be
assigned.**

## Failure mode

This is not an HTTP failure. There was no document to retrieve, because no company could be
identified to retrieve one from. The name **"RMJ"** as it appears in the G4 competitor
table does not resolve to any freight-technology, carrier-verification, visibility, or
load-matching company in a scan of the open web on 2026-08-07.

## Search scope — what was actually searched

Four distinct queries, all on 2026-08-07, via general web search:

1. `"RMJ" freight carrier vetting fraud technology company trucking`
2. `"RMJ" company logistics freight software platform`
3. `RMJ freight tech startup carrier verification competitor Highway Carrier Assure FreightValidate`
4. `"RMJ" OR "RMJ Group" freight fraud detection carrier vetting 2025 2026`

Queries 1, 3 and 4 returned the carrier-vetting competitive landscape without any "RMJ"
entity in it. The vendors that did surface repeatedly in that landscape were Highway,
Verified Carrier, GenLogs, Descartes, FreightValidate, Truckstop/RMIS, Carrier 411,
CarrierCheck and VerifyCarrier — none of them an "RMJ".

Query 2 returned four unrelated entities that share the initials and are **not** freight
technology vendors: RMJ Transport LLC (an auto-transport carrier listed on a third-party
TMS marketplace), RMJ Logistics Inc (an interstate freight carrier, Elizabethtown NC), RMJ
Logistic Solutions PTY LTD (a South African clearing and forwarding firm), and RMJ Cargobull
(a transport enterprise founded 2021). None is a competitor to this programme, and nothing
connects any of them to carrier verification, fraud detection, or visibility software.

## The standing conjecture, and why it stays a conjecture

[[evidence]] G4 records a guess that "RMJ" was meant to be **RMIS** (Registry Monitoring
Insurance Services, acquired by Truckstop). That remains plausible on phonetic and
contextual grounds and remains **unconfirmed**. No source was found that writes RMIS as
"RMJ", and nothing in this scan corroborates the substitution.

If the conjecture is correct, it has a consequence the register should absorb rather than
paper over: **RMIS is not a thirteenth competitor.** It is the vetting arm inside
Truckstop, already represented by the Truckstop row. The list would then hold twelve
distinct companies, not thirteen — which is very likely the origin of `DRIFT-009`, the
thirteen/twelve inconsistency between the G4 heading and the G5 cross-reference.

That is an inference about the register's history, not a fact about a company. It is
offered to the human doing the reconciliation and is not acted on here.

## Confirmed absence versus failure to find

Stated precisely, because the two are different claims:

- **Confirmed:** the four queries above, run on 2026-08-07, surfaced no freight-technology
  company named "RMJ" in the carrier-verification, visibility, or load-matching space.
- **Not confirmed:** that no such company exists. A private, rebranded, non-indexed, or
  very recently founded entity would not necessarily surface in a four-query open-web scan.
  This is a bounded negative finding, not an exhaustive one.

## Resolution path

The referent is recoverable only from the team's own notes — whoever wrote "RMJ" into the
original competitor list. This needs a human with access to that provenance, not another
scan. Until then the row should stay explicitly marked unidentified.

## Consumers

[[evidence]] G4 competitor table, "RMJ" row; `DRIFT-009` in [[drift-control]]; `GAP-009` in
[[gap-register]].

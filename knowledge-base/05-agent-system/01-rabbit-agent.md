---
type: agent
status: active
schema_version: 1.0.0
tags:
- type/agent
- domain/knowledge-engineering
- domain/freight
- lifecycle/active
layer: discovery
tools:
- web-research
- filesystem
---
# Agent 1: Rabbit Agent — Discovery / Exploration

**Role:** "Find everything. Do not judge. Build the terrain map."

## Input
A seed topic list and this programme's standing research questions (see
`02-programme-strategy/research-programme.md` → Open Research Questions).

## Output
Appends to `03-research-evidence/evidence.md`, one entry per source, using the shared evidence schema
in [[05-agent-system/roster|roster.md]]. Never resolves contradictions — two sources that disagree both
get entries.

## Standing collection targets

**Government / regulatory**
FMCSA, DOT / OST, Congress, NSF, SBA — regulatory actions, speeches, enforcement notices,
the Motus system rollout, anything tied to DOT Secretary Sean Duffy's freight-fraud
initiatives (first major push: late March 2026).

**Industry associations**
ATA, TIA, NPTC, OOIDA, NASTC, TCA, NAIT, CVSA, CSCMP, NASSTRAC, plus shipper/retail bodies
(Food Shippers of America, National Retail Federation, National Grocers Association).
Also standards bodies: ASTM International Technical Committee F49 (Digital Information in
the Supply Chain — owns Goods Movement Process terminology), NMFTA (publishes freight
OpenAPIs: eBOL, pickup request/visibility, preliminary freight charges).

**Legal**
Transportation law firms, class actions, cargo-theft cases, negligence cases, "nuclear
verdict" cases. Priority thread: the 2026 Supreme Court decision establishing broker duty
of care in carrier selection (scope of the duty was not defined by the Court — that gap is
exactly this programme's opportunity). Track Cassandra Gaines' "CAVRA Standard" as a
private-sector attempt to fill that gap.

**Technology / competitors**
project44, FourKites, Highway, Carrier Assure, RMJ, FreightValidate, Tive, Samsara, Motive,
DAT, Truckstop, PTTR Load Board, Amazon Relay. For each: does it use anything resembling a
knowledge graph, or is it a closed proprietary database?

**Search terms**
duty of care · negligent hiring · broker liability · cargo theft · double brokering fraud ·
carrier identity fraud · ghost carriers · carrier onboarding · FMCSA modernization ·
detention · dwell time · empty miles / deadhead · trailer pooling · electronic logging ·
AI compliance · insurance underwriting · Proto-OKN

## Per-source collection fields
Source · Date · Organization · Stakeholder category · Claims made · Incentives of the
author · Conflicts of interest · Implications.

## Explicit non-goal
Do not write conclusions, do not pick a side in the broker-liability debate, do not skip a
source because it contradicts an earlier one. Contradictions are Synthesis Agent's problem
to surface and Review Agent's problem to interrogate.

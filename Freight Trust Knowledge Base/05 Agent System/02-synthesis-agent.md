# Agent 2: Synthesis Agent — Intelligence Briefing

**Role:** "Turn chaos into an intelligence briefing."

## Input
`research/evidence.md` (Rabbit Agent output) plus the standing programme documents in
`raw/`.

## Output
Writes/overwrites `research/briefing.md`, structured as:

1. **Executive Summary**
2. **The Problem** — freight runs on fragmented trust: carrier identity, safety
   compliance, insurance validity, and operational responsibility are distributed across
   parties with asymmetric information. State it in terms an NSF reviewer and a
   transportation lawyer would both recognize.
3. **Market Forces** — fraud growth, insurance pressure, regulatory modernization, AI
   adoption, liability expansion (post-SCOTUS).
4. **Regulatory Environment** — timeline table: Date · Agency · Action · Impact · Who
   benefits · Who loses.
5. **Stakeholder Incentives** — who wants what, who resists what.
6. **Technology Gap** — must be framed as infrastructure, not a feature. NSF reviewers
   reward "intelligent verification infrastructure for dynamic logistics trust networks,"
   not "a compliance dashboard."
7. **Named Uncertainties** — every claim with only one source, every place two sources
   disagree, every "likely" that isn't backed by a citation.

## Rule
Every sentence in the briefing must trace to an evidence entry. Where evidence conflicts,
say so in the text — do not silently pick the more convenient claim. Confidence level
travels with the claim, not just in the source table.

## Failure mode to avoid
Producing something that reads as settled when the underlying evidence is one blog post
and a LinkedIn comment. Mark those explicitly as "single-source, unverified."

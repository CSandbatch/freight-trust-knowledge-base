---
type: log
status: active
schema_version: 1.0.0
updated: '2026-08-08'
tags:
- type/log
- domain/freight
- domain/knowledge-engineering
- audience/internal
- lifecycle/active
---
# Research Run Log

Operational ledger for delegated work. Keep one row per task attempt; do not delete
failed or superseded attempts.

| Run/task ID | Parent | Owner | Input/version | Queries/tools | Sources added/rejected | Gate verdict | Retry/reason | Status | Timestamp |
|---|---|---|---|---|---|---|---|---|---|
| cycle-2026-08-01 | — | programme orchestrator | current workspace | workspace inspection + web search | framework sources identified | operating model drafted | initial setup | active | 2026-08-01 |
| luna-wide-net-01 | cycle-2026-08-01 | Terra + Luna branches | programme/evidence/goals | public, peer-reviewed, standards, and policy sources | detention, identity, data-sharing, governance, technical sources | synthesis accepted; outcome claims narrowed | n/a | accepted | 2026-08-01 |
| G3-nsf-verify-01 | cycle-2026-08-01 | research subagent | 04-sbir/NSF SBIR STTR Process and Readiness Guide | web search + direct fetch of nsf.gov/seedfund.nsf.gov + neutral trade sources (CargoNet, TIA, ATRI, FreightWaves) | solicitation facts confirmed (deadlines, award cap, Pitch fields/limits, PI rule, budget splits, registrations, cost-sharing prohibition, TABA amount); 9 market-evidence claims logged with confidence notes; see [[04-sbir/sbir-evidence-refresh]] | core facts verified; one item (invitation validity window) and two market figures (dwell-time discrepancy, detention-loss figure vintage) flagged unresolved | n/a | verified | 2026-08-01 |
| sbir-package-draft-01 | cycle-2026-08-01 | drafting subagents (4) | vault evidence base + readiness guide | vault reads + character-count scripts | Project Pitch, Phase I Project Description, Budget/Justification, DMP, Commercialization Plan, Technical Risk Register drafted; visuals 06–08 created | all real-world unknowns kept as bracketed placeholders; no unverified figures used | n/a | submitted | 2026-08-01 |
| sbir-package-review-01 | sbir-package-draft-01 | independent review subagent | six drafts + three diagrams vs rubric + evidence refresh | cross-document consistency + NSF-compliance checks | 9 blocking + 14 improvement findings in [[04-sbir/review/proposal-review-notes]] | fact discipline held (no unverified stats, no premature PI); beachhead contradiction and TABA treatment flagged blocking | n/a | accepted | 2026-08-01 |
| sbir-package-fix-01 | sbir-package-review-01 | fix subagent | review notes + evidence refresh + orchestrator decisions | edits + pitch recount script + mermaid-cli render check | single beachhead (carrier onboarding, working default), TABA inside $305K base, unverified-figure flags, diagram/schedule fixes; resolution log appended to review notes | 18/23 findings fixed, 2 partial, 4 deferred (would require inventing facts) | n/a | accepted | 2026-08-01 |
| G14-benchmark-dataset-scan-01 | cycle-2026-08-01 | research subagents (2, parallel) | Phase I Project Description Aims 1–3 + GOALS G14 | web search + direct fetch of FMCSA/data.transportation.gov, gao.gov, MuckRock, GitHub, NIST, OASIS, BTS sources | Aim 1: FMCSA Company Census File confirmed real/open seed source; no chameleon-carrier labeled dataset found anywhere. Aims 2–3: no freight-event benchmark exists anywhere; OpenEPCIS+process-mining path for Aim 2; NIST Policy Machine+XACML conformance format fully resolves Aim 3's build path. See [[dataset-scan-entity-resolution]] and [[dataset-scan-event-provenance-and-federation]] | benchmark methodology/tooling resolved for all 3 aims; no numeric targets invented; findings propagated into [[04-sbir/drafts/phase-1-project-description-draft]] | n/a | accepted | 2026-08-01 |

## Open task packets

These are the next bounded tasks implied by the current research plan. They are
intentionally not marked complete merely because related material exists.

| Task ID | Goal | Owner | Required output | Acceptance test | Max attempts | Status |
|---|---|---|---|---|---:|---|
| G1-legal-verify-01 | Recheck court holding and limits | Rabbit/legal | claim-level evidence entries | primary opinion/docket supports holding and limits separately | 2 | queued |
| G2-reg-verify-01 | Recheck Motus status and implementation claims | Rabbit/regulatory | dated primary-source entries | Federal Register/DOT/FMCSA source or explicit secondary-only status | 2 | queued |
| G3-nsf-verify-01 | Recheck current NSF solicitation and submission gates | Rabbit/grants | solicitation evidence + freshness date | official NSF page/document supports current process and deadline | 2 | verified |
| G4-market-01 | Resolve competitor classification gaps | Rabbit/market | one evidence entry per named company | source is product documentation or clearly labeled vendor claim | 2 | queued |
| G7-adoption-01 | Find neutral data-sharing precedent | Rabbit/adoption | precedent evidence + participation mechanism | mandate, liability protection, or market-pressure mechanism is explicit | 2 | queued |
| G8-equity-01 | Assess small-carrier compliance-cost equity risk | Rabbit/equity | primary evidence or research protocol | direct evidence separated from inference | 2 | queued |
| G10-pilot-01 | Define pilot measures and falsifiers | Terra + Luna | pilot measurement plan | core hypotheses have baseline, measure, and failure condition | 2 | queued |
| G11-architecture-01 | Specify minimum trusted-data architecture | Luna/technical | source/provenance/access/correction matrix | every claim type has an authoritative source and correction path | 2 | queued |
| G12-adoption-01 | Test reciprocal participation offers | Luna/adoption | adoption experiment design | benefits and segmented uptake measures are specified | 2 | queued |
| G13-redress-01 | Draft consequential-use safeguards | Terra + human/legal | governance policy | abstention, review, correction, appeal, and access rules present | 2 | queued |
| G14-benchmark-01 | Design adjudicated freight benchmark | Luna/technical + operations | benchmark protocol | labels, sampling, provenance, and metrics defined | 2 | queued |
| REVIEW-coverage-01 | Assign stable claim IDs to load-bearing evidence | evidence verifier | claim-ID index | every load-bearing claim has one stable ID and status | 1 | queued |

## Status vocabulary

`queued`, `running`, `submitted`, `verified`, `accepted`, `unverified`, `contradicted`,
`blocked`, `rejected`.

## Session log

### 2026-08-06 — Experiment provenance, prose pass, and the vault control layer

**Experiments E1–E5 expanded.** Each experiment note gained a Provenance / What it adds /
Why we are using it block: the finding that forced it, the origin and licence of every
input, the intellectual lineage of every method, the reason behind each design choice, the
counterfactual if dropped, and the alternatives rejected. Sourced entirely from the two
2026-08-01 dataset scans, [[goals]], [[review-notes]], [[improvement-suggestions]], and
the Project Description. No new external research; no new facts introduced.

**Prose pass across the vault.** An `ai-tell-editor` agent was defined and run over
roughly sixty notes in eight batches to remove LLM-statistical style without touching
facts, hedges, citations, or structure. Two batches were interrupted by a session limit
and re-run. Reported edit counts were low in the evidence registers and the dataset scans
— correctly so, since those files are mostly tables and confidence verdicts.

One deliberate numeric change: two self-reported character counts in
[[04-sbir/drafts/project-pitch-draft]] were recomputed because editing the prose would
otherwise have made the document's own stated counts false. Recorded as `DEC-005`,
tracked as `DRIFT-024`.

**Control layer built.** New `09-meta/` folder: [[kb-schema]] 1.0.0, [[tag-taxonomy]]
(seven layers), [[methodology]], [[agents-and-loops]] (five agent layers, four loops),
[[drift-control]], [[gap-register]], [[decision-log]], [[glossary]], [[dataset-index]],
[[client-common-action]], [[meta-moc]]. Eight executable agent definitions written to
`.claude/agents/`.

**Client recorded.** Common Action (common-action.org), retrieved 2026-08-06. Knowledge
infrastructure for climate action; Supply Chain is one of four stated focus areas. Entity
type, legal form, location, and team are **not stated** on the site, which leaves the SBIR
applicant/PI question open — `DEC-002`, `GAP-001`.

**Findings.** 37 drift issues opened, 6 high-severity. 16 gaps registered, 5 high. The
highest-value ones came from reading across files: a milestone-month mismatch between an
Aim's failure condition and the work plan (`DRIFT-001`), evidentiary content silently lost
from a dataset scan row in an earlier uncommitted edit (`DRIFT-005`), a self-contradicting
review finding (`DRIFT-027`), and a superseded two-workflow instruction still cited by
number from other notes (`DRIFT-028`).

**Not done.** No gap closed. No source re-fetched. The schema is defined but the vault is
not migrated to it (`GAP-011`), and the link graph has not been audited (`GAP-012`).
Nothing committed to git.

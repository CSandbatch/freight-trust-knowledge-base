---
type: policy
status: active
owner: orchestrator
version: 1.1.0
schema_version: 1.0.0
updated: 2026-08-08
tags:
- type/policy
- domain/knowledge-engineering
- audience/internal
- lifecycle/active
---
# Gap Register

The build-out backlog: what is missing before this vault is "complete", ranked, with
acceptance criteria specific enough that closure is checkable. Loop L3 in
[[agents-and-loops]] consumes this file top-down.

"Complete" here means: every claim sourced and current, every note typed, tagged, and
linked, every term defined, every external dataset registered with its access terms, and
every remaining unknown named with an owner. It does not mean every question answered;
several of these gaps close as *documented open questions*.

## Priority

**High** — blocks submission, a decision gate, or the integrity of what is already
written. **Medium** — materially improves the asset. **Low** — completeness and polish.

## Open gaps

### High

| ID | Gap | Why it matters | Acceptance criteria | Agent / owner |
|---|---|---|---|---|
| `GAP-001` | **Applicant legal form, route, and PI eligibility documentation remain unresolved** — applicant is Common Action and PI is Ellie Young (confirmed directly by the commissioning team) | PI identity is no longer open, but SBIR/STTR eligibility still depends on Common Action's legal form and the applicable PI employment/effort facts | Entity type/registered form corroborated; SBIR vs. STTR route chosen; Ellie Young's employment/effort eligibility documented | Common Action + Ellie Young + counsel (`DEC-002`) |
| `GAP-002` | **Unverified sources have never been re-fetched** | Load-bearing infrastructure claims rest on pages that returned HTTP 403 or a JS shell: FMCSA MCMIS catalog, FMCSA L&I dataset, the FMCSA chameleon-carrier Report to Congress, PIERS licence terms, OpenCorporates pricing, and the FCRA statutory window | Each retrieved by a method that works (browser, mirror, or direct request), with `accessed` and `verification: confirmed`, or reclassified as permanently unavailable with the failure documented | `source-scout` (L2) |
| `GAP-003` | **E1 identity/adjudication standard is RC1-complete; human freeze and E2-specific rubric remain open** | Research/eval produced [[e1-carrier-identity-and-relationship-standard]], ontology, decision tree, 64-claim ledger, 70-case suite, hostile review, [[e1-adjudicator-governance-and-training]], [[e1-definition-conformance-report]], and [[e1-state-corporate-source-access-memo]]. E1 no longer lacks a rubric, written COI/training protocol, or initial state-source workflow. Remaining E1 gates are PI/domain/counsel approval, actual reviewer training, pilot double-labeling, and case-level source retrieval. E2 still needs its own facility-event adjudication rubric | E1 RC1 approved/frozen and pilot double-labeling run completed; E2 rubric separately written before E2 gold labeling | Ellie Young + technical lead + domain reviewer + counsel |
| ~~`GAP-004`~~ | ~~G7/G12 participation precedent was never researched~~ | **Closed 2026-08-08.** Primary-source analogues are now documented for FinCEN §314(b), CISA information-sharing protections, FAA ASIAS, and DOT airline on-time reporting. The pass did not eliminate governance risk; it generated the more specific antitrust question now tracked as `GAP-017`. | Acceptance criteria met; follow-on risk moved to `GAP-017` | `source-scout` → `evidence-registrar` |
| `GAP-005` | **Small-carrier evidence is inferential** | R-WN-05 stands open: public evidence supports relevance, not the programme's burden estimate. §9 of the project description commits to ≥3 small-carrier discovery interviews before submission | Documented sampling plan; interviews conducted or a dated plan with owner; burden claims either sourced or downgraded | Commercial lead |
| `GAP-017` | **Antitrust exposure of the shared evidence graph has never been addressed** | Filed 2026-08-07 from the `GAP-004` participation-precedent research. The words "antitrust" and "competition law" appear nowhere in this vault outside the new source cards that surfaced the issue ([[source-cisa-2015-cyber-threat-sharing-liability-shield]]). CISA 2015 is primary evidence that Congress judged an *express antitrust exemption* necessary before competing companies would lawfully pool data (6 U.S.C. §1503(e)(1)). A broker/carrier evidence graph raises the identical information-exchange concern among competitors and has no such exemption or legal analysis on record | A written threat assessment — from counsel or a cited legal-research source, not an agent — addressing whether/how competitor data-pooling in the proposed architecture could raise Sherman Act Section 1 concerns, and what structural safeguards (e.g. the aggregation/anonymization pattern ASIAS uses, or an explicit exemption request) would be needed | Client + counsel |

### Medium

| ID | Gap | Why it matters | Acceptance criteria | Agent / owner |
|---|---|---|---|---|
| `GAP-006` | **Legacy citations are only partially promoted to per-source cards** | The source-card layer now exists and contains **37 cards**, but older embedded citations in evidence/programme prose have not all been promoted into reusable cards | Every load-bearing external citation used by reviewer/client-facing material has a `source-*.md` card with class, accessed/retrieval status, and downstream consumers | `source-scout` |
| `GAP-007` | **Glossary is a skeleton** | Terms of art (chameleon carrier, dwell vs. detention, provenance, NGAC, blocking, calibration, abstention) are used across the vault with no single sourced definition | Every term used in ≥2 notes has a cited definition, aliases, disambiguation, and links to dependents | `glossary-builder` |
| ~~`GAP-008`~~ | ~~Standards and association positions unresolved (G5, G6)~~ | **Closed 2026-08-08.** All 13 named bodies resolved: 8 hold documented positions (ATA, NASTC, TCA, OOIDA, NMFTA, NRF, CVSA, NGA — with varying directness), 2 are confirmed absences (National Grocers on freight specifically beyond CORCA; NAIT has no advocacy function), Food Shippers of America has guidance but no policy apparatus, NPTC unresolved behind a members-only wall. **NMFTA is the standout finding**: a live, paid, mandatory-at-renewal carrier identity-verification programme (SCAC Verified, launched 2026-02-26) — real incumbent prior art the proposal must name. **Time-sensitive:** CVSA is actively forming its cargo-theft/carrier-identity policy now, with a stated input-survey deadline of 2026-08-08 — flagged to the client directly, not resolvable by an agent | `source-scout` |
| `GAP-009` | **Competitor classification incomplete (G4)** | [[evidence]] carries 13 rows with one (RMJ) unidentified, and a count inconsistency (`DRIFT-009`) | All rows identified or explicitly marked unidentifiable; counts reconciled; each classified by architecture and focus from product documentation | `source-scout` |
| `GAP-010` | **Numeric targets remain bracketed across all three aims** | Correct today — no benchmark exists to set them against — but they must not still be brackets at submission | Either set post-benchmark, or a written statement of why a target cannot responsibly be set pre-Phase I | PI |
| ~~`GAP-011`~~ | ~~Vault is unmigrated to schema 1.0.0~~ | **Closed 2026-08-08 for team release v0.9.** All Markdown notes in the distribution validate for `type`, `status`, `schema_version`, and required tag layers. See [[release-audit]]. | Metadata/tag validation passes | `kb-schema-steward` + `kb-linker` |
| ~~`GAP-012`~~ | ~~Link graph has never been audited~~ | **Closed 2026-08-08 for team release v0.9.** The release audit found zero unresolved Markdown wikilinks, zero bad heading anchors, and every Markdown note reachable from [[start-here]] within two hops via [[vault-inventory]]. Mermaid source links were also checked as files. | Link/anchor/reachability validation passes | `kb-linker` |

### Low

| ID | Gap | Acceptance criteria | Agent |
|---|---|---|---|
| ~~`GAP-013`~~ | ~~Dataset index is new and not yet reconciled against the two scans and the eight dataset cards~~ | **Closed 2026-08-07.** Reconciled: 11 sources present in the scans but missing from the index were added, 4 dataset cards that had no index representation were given rows, 5 verification markers that overstated the scans were corrected, and 4 conflicts were filed rather than resolved — `DRIFT-038` – `DRIFT-041`. Two follow-ons remain open as drift, not as gap: the FMCSA data-dissemination page must be retrieved (`DRIFT-038`), and ten event-provenance rows need their `confirmed` markers re-earned by retrieval (`DRIFT-041`) | `dataset-registrar` |
| `GAP-014` | No diagram covers the meta layer or the agent architecture | A `.mmd` in `07-visuals/` plus an index entry | `visualization` |
| `GAP-015` | Cross-sector transfer notes (climate, energy, agriculture) do not exist | Gated on `DEC-003`. If confirmed: one note per sector describing which vault machinery transfers and which freight facts do not | `kb-schema-steward` |
| `GAP-016` | G9 interview status unconfirmed | A direct answer on whether the four exploratory interviews happened and what came of them | Human |

## Closure rules

1. A gap closes only when its acceptance criteria are met, or when it is downgraded with
   a written reason and a new owner. It never closes by writing prose around the hole.
2. A gap that turns out to be unresolvable closes as a **documented open question** — a
   note stating what was attempted, what was found, and what would resolve it. `GAP-004`
   will likely close this way, and that is a legitimate result.
3. Closing a gap that required a human choice requires a [[decision-log]] entry.
4. New gaps are appended, never renumbered.

## Related

[[meta-moc]] · [[agents-and-loops]] · [[drift-control]] · [[decision-log]] · [[goals]]

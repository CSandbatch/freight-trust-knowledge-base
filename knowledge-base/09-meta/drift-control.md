---
type: policy
status: active
owner: drift-controller
version: 1.1.0
schema_version: 1.0.0
updated: 2026-08-08
tags:
- type/policy
- domain/knowledge-engineering
- audience/internal
- action/blocker
- lifecycle/active
---
# Drift Control

What rots in a knowledge base, how it is detected, and what is currently broken.

Drift is the vault asserting two different things and giving a reader no way to tell which
is true. It is not untidiness. Every issue below was found by reading the actual files;
none is hypothetical.

## The seven drift classes

| Class | What it looks like | Detected by |
|---|---|---|
| **D1 Contradiction** | Two notes state the same fact differently — a different month, count, connective, or hedge | Cross-document claim comparison |
| **D2 Staleness** | A claim past its `review_by`, or a source never successfully retrieved | Date sweep + `verification` field |
| **D3 Schema violation** | Missing or out-of-vocabulary frontmatter, wrong filename, wrong folder | `kb-schema-steward` validation |
| **D4 Link rot** | Dead wikilink, orphaned note, MOC that has lost a member, broken identifier reference | `kb-linker` resolution pass |
| **D5 Placeholder leakage** | A `[PLACEHOLDER]`/`[TARGET]`/`[VERIFY]` with no row in a tracking register, or a register row with no owner | Bracket scan vs. register diff |
| **D6 Confidence creep** | A `secondary` or `unverified` claim quoted as fact downstream; a hedge present in one place and absent in another | Confidence-marker propagation check |
| **D7 Foreign object** | Content that does not belong to the vault, or was mangled by a bulk operation | Naming + convention scan |

## Severity

- **High** — a reviewer or client could read something false, or evidence integrity is
  damaged. Blocks external send.
- **Medium** — internally inconsistent; a careful reader notices and loses trust.
- **Low** — cosmetic or stylistic; fix when touching the file anyway.

## Current open issue queue — team release v0.9.2

The table below is the **current** queue after the 2026-08-08 release-hardening pass. The
longer issue tables that follow are retained as the historical finding record; their
original wording is not a statement that the issue remains open.

| ID | Sev | Current reason it remains open | Owner |
|---|---|---|---|
| `DRIFT-003` | Medium | `G#` still names research goals, protocol quality gates, and programme decision gates. Renaming is a semantic migration, not a safe editorial search/replace. | PI + `kb-schema-steward` |
| `DRIFT-004` | Medium | E5's trigger/feed relationship remains entangled with the unresolved gate namespace above. | Operations research lead |
| `DRIFT-005` | High | The ATRI FPM dataset-scan row still needs the lost access/licence qualifiers restored from an authoritative source/history or its summary weakened. | Research lead |
| `DRIFT-010` | High | Discovery interview counts remain genuinely human-dependent: historic “four exploratory interviews” vs. current 5–10 target and ≥3 small-carrier commitment. | Commercial lead |
| `DRIFT-019` | Low | E1/E4/E5 retain some deliberate structural repetition across thesis/design sections. | Publishing |
| `DRIFT-022` | Low | [[evidence]] goal ordering remains historically non-numeric; meaning is intact but presentation is odd. | Evidence registrar |
| `DRIFT-032` | Medium | Some control-layer rules are intentionally repeated for usability; canonical-home/link-only cleanup remains incomplete. | `kb-schema-steward` |
| `DRIFT-038` | Medium | FMCSA data-dissemination page retrieval status conflicts across two scans. | Research lead |
| `DRIFT-039` | Medium | FMCSA L&I/MCMIS access posture is still asserted more strongly on one dataset card than the underlying retrieval supports. | Research lead |
| `DRIFT-040` | Medium | SINTEF VRPTW remains an un-retrieved E5 dependency; remove or verify before E5 is activated. | Research lead |
| `DRIFT-041` | Medium | Roughly ten event-provenance index rows still need retrieval status re-earned rather than inferred from source class. | `dataset-registrar` |

### Historical issue register

Opened beginning 2026-08-06. Resolved items are preserved below because the finding and
its fix are useful provenance. For the release disposition, see [[release-audit]].

### High

| ID | Class | Where | Issue | Proposed fix | Owner |
|---|---|---|---|---|---|
| `DRIFT-001` | D1 | [[04-sbir/drafts/phase-1-project-description-draft]] §3 vs §7 | Aim 1's failure condition says failure makes "the work plan's Month 9 go/no-go" a no-go, but the milestone table assigns Aim 1 to **Month 6**; Month 9 is Aim 3's federation gate | Either correct the reference to Month 6, or reword to say Aim 1 failure forfeits the Month 9 *integration* gate. Check together with Aim 3's condition, which legitimately owns Month 9 | PI |
| `DRIFT-002` | D5 | Project description §1(a), §1(b), §5 vs §11 register | Three bracketed pre-submission obligations carry no register row: the `[VERIFY: … GAO-12-364, GAO-16-401R …]` block invoking "Blocking Finding #7", the `15 U.S.C. §1681i` confirm-before-citing hedge, and the `[confirm exact dwell-time figure …]` hedge | Add three rows with owners, or state that the register tracks only a defined subset | PI |
| `DRIFT-005` | D6 | [[dataset-scan-event-provenance-and-federation]] ATRI FPM row | Four evidentiary fragments were removed from that row in uncommitted working-tree edits **predating** the prose pass: the `of raw/per-truck data` qualifier, whose removal broadened "no self-service download" from the raw panel alone to all access, the case-by-case access clause carrying two adoption counts, the confidence reasoning, and a confirmed-vs-assumed marker. The file's own summary at the foot still depends on the deleted licence clause | Restore from git history, or accept the compression and weaken the summary claim to match | Research lead |
| ~~`DRIFT-007`~~ | D7 | [[nsf-sbir-sttr-process-and-readiness-guide]] | ~~"any committed 03-research-evidence/pilot partners"~~ | **Fixed 2026-08-06** — restored to "research/pilot partners" | — |
| ~~`DRIFT-008`~~ | D6 | Guide vs [[sbir-evidence-refresh]] | ~~Guide dropped "funding" from the verified TABA quote without an ellipsis~~ | **Fixed 2026-08-06** — guide now matches the refresh's verified quotation exactly | — |
| `DRIFT-010` | D1 | [[04-sbir/drafts/project-pitch-draft]], [[04-sbir/drafts/commercialization-plan-draft]], project description §9 | Discovery-interview counts are unreconciled: G9's "four exploratory interviews" vs. `[N — target five to ten]` vs. the §9 commitment that ≥3 be small carriers. The commercialization draft self-flags this | Settle one number and propagate; §9's dependent placeholders must move with it | Commercial lead |

### Medium

| ID | Class | Where | Issue | Proposed fix |
|---|---|---|---|---|
| `DRIFT-003` | D3 | [[kb-schema]], [[experiment-protocol-standard]], [[datasets-and-experiments-moc]] | `G0`–`G5` means three different things: research goals (G1–G14), protocol quality gates, and programme decision gates. All three appear in prose near each other | Rename two of the three namespaces. Suggested: `QG0`–`QG5` for quality gates, `DG0`–`DG5` for decision gates, leaving `G#` to goals |
| `DRIFT-004` | D1 | [[experiment-e5-orchestration-value]] vs [[datasets-and-experiments-moc]] | Circular gate: E5 says it is "executed when G5's gate is reached", but the decision-gate table lists "E5 bounded workflow result" as the evidence *required* to pass that gate | Resolve after `DRIFT-003`; state which gate triggers E5 and which one E5 feeds |
| `DRIFT-006` | D1 | [[04-sbir/drafts/phase-1-budget-and-justification-draft]] | Two directional references are inverted — "the two-thirds check **above**" points to a section below it, and "the worked allocation table **below**" points to a table above it. Both read as leftovers from a section reorder | Correct both directions |
| `DRIFT-009` | D1 | [[evidence]] G4/G5 | G4 is headed "Competitor classification (13 companies)" with 13 table rows and an intro saying "None of the thirteen"; G5 refers to "one of the twelve competitors on this programme's landscape list (see G4)". The 13th row, RMJ, is explicitly unidentified | State the rule — identified vs. total — or conform the counts |
| `DRIFT-011` | D6 | [[experiment-e4-participation-and-small-carrier-equity]] | The same claim is unhedged in one place ("A small carrier with one administrator **experiences** a different burden") and hedged in another ("**may experience**"). R-WN-05 found the programme's burden estimate unsupported, so the unhedged form asserts more than the evidence carries | Adopt the hedged form in both places |
| `DRIFT-012` | D1 | [[experiment-e2-facility-event-provenance-and-dwell-reconstruction]] | The thesis table lists dwell events as "appointment, arrival, gate, dock, **loading**, release, departure"; the interval decomposition elsewhere in the same file has no loading interval | Reconcile the event set with the interval set |
| `DRIFT-013` | D5 | Project description evidentiary-basis paragraph | It states that every claim is sourced to [[evidence]] or [[luna-wide-net-synthesis]] plus two dataset scans, but §1(a)/(b) repeatedly cite [[sbir-evidence-refresh]], which is never named in that sentence | Add the refresh file to the sourcing statement |
| `DRIFT-015` | D5 | [[experiment-e3-federated-access-and-policy-enforcement]] | "NIST's DP Synthetic Data Challenge assets" is relied on in a design-choice cell but has no row in that file's own "Provenance of each input" table and no verification status anywhere | Add a provenance row, or drop the reliance |
| `DRIFT-021` | D1 | [[04-sbir/drafts/data-management-plan-draft]] | A security bullet asks for confirmation of "the company's actual provider and **rate**". A rate is a budget concept; the DMP needs provider plus control implementation | Replace "rate" with the control-implementation requirement |
| `DRIFT-024` | D6 | [[04-sbir/drafts/project-pitch-draft]] | Two stated character counts were recomputed during the prose pass because editing the prose would otherwise have made the stated counts false. This is the one place a number changed. Recorded as `DEC-005` | Confirm the recomputation, or revert both prose and counts |

### Low

| ID | Class | Where | Issue |
|---|---|---|---|
| `DRIFT-014` | D1 | [[experiment-e3-federated-access-and-policy-enforcement]] | A near-duplicate sentence uses "**or** opaque secondary use" in one place and "**and**" in the other — different logical connectives on the same claim |
| `DRIFT-016` | D3 | E3 | "Failure mode F13-adjacent" — every other reference is a bare token. Confirm F13 fits, or drop the qualifier |
| `DRIFT-017` | D3 | E4 | The G7 row's status reads `⚪ Open, not started`; every other status in that column is a bare word. The emoji convention appears nowhere else |
| `DRIFT-018` | D1 | E1 | "the operational form of four specific, dated findings" introduces a seven-row table. Four are findings; three are a suggestions list, a scan, and a draft |
| `DRIFT-019` | D1 | E1, E4, E5 | Near-verbatim assertions repeat within single files, an artifact of the Thesis / What it adds / Why we use it template. Structural, but a whole-file reader will notice |
| `DRIFT-020` | D3 | E5 | British and American spellings alternate by section (`behaviour`/`modelled`/`licence` vs `behavior`/`modeling`/`labeled`). House preference is undeclared |
| `DRIFT-022` | D3 | [[evidence]] | G5 appears between G1b and G2, out of numeric order. Plausibly deliberate (three parallel threads separated by a rule) but undocumented |
| `DRIFT-023` | D7 | `knowledge-base/French Trans.md` | A French poem translation sits in the vault root. It is not programme content, violates the naming convention, and is unreferenced. Not deleted — it may be the user's | 
| `DRIFT-025` | D3 | Vault-wide | No note yet carries `schema_version: 1.0.0`. Every pre-existing note is unmigrated against [[kb-schema]] |

### Second pass, 2026-08-06 — client briefs, agent system, archive, review notes, meta layer

| ID | Sev | Class | Where | Issue | Proposed fix | Owner |
|---|---|---|---|---|---|---|
| `DRIFT-026` | High | D4 | [[04-sbir/drafts/commercialization-plan-draft]] | Two heading anchors into the master brief do not resolve: `#Stakeholders and pushback` and `#Dataset and experiment backbone`. The master brief has no numbered headings; the nearest is `## Stakeholders and pushback`, and the second section does not exist at all | Repoint both to real headings, or add the sections | Publishing |
| `DRIFT-027` | High | D1 | [[04-sbir/review/proposal-review-notes]] Blocking #2 | The finding contradicts itself: the Problem states the "2023" label "did not originate in `evidence.md` with that year attached", then the next parenthetical says "evidence.md's own G-item says 'ATRI's 2023 analysis'" | Establish which is true before anyone acts on the finding | Review owner |
| `DRIFT-028` | High | D1 | [[improvement-suggestions]] item 1 | Still prescribes "carrier onboarding **plus one facility-event dispute process**" — two workflows — while Blocking #1 records the resolution to a single Phase I beachhead with facility events demoted to Aim 2 context. Item 1 is cited **by number** from other notes, so the stale version propagates | Update item 1 to match the resolved decision, or mark it superseded in place. Do not renumber | PI |
| `DRIFT-029` | Med | D6 | [[05-agent-system/04-publishing-agent]] | The spec requires citations for "$15B detention", canonicalizing a figure that [[sbir-evidence-refresh]] flags as possible stale-figure risk pending primary-PDF confirmation. The client briefs use the $3.6B / $11.5B breakdown instead | Remove the figure from the spec, or point it at the refresh's caveat | Publishing |
| `DRIFT-030` | Med | D4 | [[05-agent-system/05-visualization-agent]] | Cites `AGENT_framework_plan.md` Modules 4–5 as the source for the stakeholder matrix. That file was deleted in the current staged changeset; the reference now points at nothing on disk | Repoint to the surviving source, or record the source as retired | Agent-system owner |
| `DRIFT-031` | Med | D7 | [[04-sbir/review/proposal-review-notes]] §4 | The consistency matrix is malformed: the header row has 8 columns, every data row has 9 cells. Most renderers will drop or misalign the trailing verdict cell — which is where `Inconsistent — see Blocking #1` lives | Add the missing header cell | Review owner |
| `DRIFT-032` | Med | D1 | `09-meta/` | Near-duplicate policy sentences across the new control layer: the stopped-agent rule appears in both [[methodology]] §7 and [[agents-and-loops]]; the "never closed by writing prose around the hole" rule in both [[gap-register]] and [[agents-and-loops]] L3; the entity-form reasoning in both [[decision-log]] DEC-002 and [[client-common-action]] | Pick a canonical home for each and link to it. This is the same D1 pattern the vault flags in its own content | `kb-schema-steward` |
| `DRIFT-033` | Low | D3 | [[08-archive/preliminary-freight-trust-brief]] | No YAML frontmatter, so it carries no `status: superseded` and appears in no status query, despite two MOCs labelling it historical. Also uses relative markdown links where the vault uses wikilinks | Add frontmatter only. Content stays frozen | `kb-schema-steward` |
| `DRIFT-034` | Low | D7 | [[05-agent-system/tools-and-skills]] | The document's introductory sentence sits *below* a later-added "Orchestration layer (new)" section, so the file opens mid-thought | Move the intro above the added section |
| `DRIFT-035` | Low | D4 | [[04-sbir/review/proposal-review-notes]] Blocking #7 | Refers to `LUNA_WIDE_NET_SYNTHESIS.md` in the pre-rename uppercase form while the same paragraph uses the current lowercase path | Conform to the current path |
| `DRIFT-036` | Low | D1 | [[operating-model]] | Says to "add `run-log.md` in the next implementation pass", but [[run-log]] already exists and is listed as current in [[research-evidence-moc]] | Update the two stale implementation items |
| `DRIFT-037` | Low | D1 | [[research-evidence-moc]], [[programme-strategy-moc]] | Both describe [[improvement-suggestions]] as "ten **prioritized** improvements"; the file is titled "Ten Improvements to Strengthen the Project" and states no priority ordering | Drop "prioritized", or add an ordering |

### Third pass, 2026-08-07 — dataset-index reconciliation against its source documents

Filed by `dataset-registrar` while closing `GAP-013`. Each is a conflict between two
source documents, or a claim in the index with no source behind it. None was resolved by
picking a side; `DRIFT-038` and `DRIFT-039` in particular need a retrieval, not an edit.

| ID | Sev | Class | Where | Issue | Proposed fix | Owner |
|---|---|---|---|---|---|---|
| `DRIFT-038` | Med | D6 | [[dataset-scan-entity-resolution]] footer vs. [[dataset-scan-event-provenance-and-federation]] Aim 2 table | The two scans record the **same page** — FMCSA's data-dissemination / Open Data Program page — incompatibly. The entity-resolution scan's fetch log lists it among the FMCSA pages that "returned HTTP 403 to automated fetch and are cited from search-result snippets only". The event-provenance scan lists it as `primary` public documentation with no failure noted. Both were compiled 2026-08-01. This is not cosmetic: it is the umbrella terms page for all FMCSA bulk data, so whether it was read determines whether the census-file, L&I and MCMIS access terms are known or inferred | Retrieve the page once, by browser if automated fetch still 403s, and correct whichever scan is wrong. Until then the index carries it as a retrieval failure, which is the more conservative of the two records | Research lead |
| `DRIFT-039` | Med | D6 | [[dataset-fmca-registration-insurance-safety-records]] vs. [[dataset-scan-entity-resolution]] | The card states "Access: public or permissioned by field" and carries `status: candidate`. The scan establishes neither. The L&I catalog page would not render past its JS shell (fields and cadence unconfirmed), the MCMIS catalog returned HTTP 403, and the scan explicitly declines to carry the census file's public-domain presumption across, calling L&I's licence "not independently confirmed... likely same public-domain posture as census file but not verified on this pass". The card asserts an access posture from the publisher's type — the inference the vault flags as confirm-do-not-assume | Either retrieve L&I and MCMIS terms and keep `candidate`, or downgrade the card's access line to record what is actually known. The card is another agent's to edit; this entry is the request | Research lead |
| `DRIFT-040` | Med | D5 | [[experiment-e5-orchestration-value]] vs. [[dataset-index]] | The SINTEF VRPTW benchmark is relied on in E5's method-provenance table as the solver-validation input, but appears in **neither dataset scan nor any dataset card**, and no retrieval of it is recorded anywhere in the vault. The index nonetheless carried it as `confirmed` with licence "Public research resource". Structurally identical to `DRIFT-015` | Index verification corrected to `not-attempted` on 2026-08-07. Still needs either a retrieval with licence text, or removal of E5's reliance | Research lead |
| `DRIFT-041` | Med | D6 | [[dataset-index]], ~10 rows sourced from [[dataset-scan-event-provenance-and-federation]] | Two vocabularies were collapsed in the 2026-08-06 consolidation. The event-provenance scan marks rows `primary`/`secondary`/`unverified` — evidence.md's **source-class** vocabulary — and publishes no fetch log. The index's `confirmed` means **retrieved directly**. Every `primary` row was mapped to `confirmed`, which converts a statement about who published something into a statement that someone read it. Affects GS1 EPCIS, OpenEPCIS, NIST Policy Machine, OASIS XACML, the three NIST SPs, PDC, ISOMORPH, IoT-23, NIST DP challenge assets, and LEAF. The entity-resolution scan does publish a fetch log, so its rows converted cleanly and five were corrected to `snippet-only` on 2026-08-07 | Re-fetch the ten rows in an L2 pass and set each marker from the result. The affected rows are flagged inline in the index in the meantime. Do not clear the flags without a retrieval | `dataset-registrar` (L2) |

## Standing checks

Run as loop L1 in [[agents-and-loops]]:

1. Every bracketed placeholder has a register row with an owner.
2. No two notes state the same figure, month, count, or identifier differently.
3. Every `verification: retrieval-failed` / `snippet-only` card is listed for L2 refresh.
4. Every wikilink resolves; no note is more than three hops from [[start-here]].
5. Frontmatter validates against [[kb-schema]]; identifiers are unique per namespace.
6. No `confidence/secondary` or `confidence/unverified` claim is cited unqualified in an
   `audience/reviewer` note.
7. No `action/` tag is older than 30 days without movement.

## Related

[[meta-moc]] · [[kb-schema]] · [[gap-register]] · [[decision-log]] · [[methodology]]

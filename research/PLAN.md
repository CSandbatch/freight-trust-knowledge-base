# Plan of Attack

Sequencing for `research/GOALS.md`, mapped to the agent roster (`agents/ROSTER.md`).
Phases 0–1 are underway as of this writing; everything after Phase 1 is blocked on it.

## Phase 0 — Scaffolding (done)

Convert source docs → `raw/`, build agent roster → `agents/`, consolidate into
`RESEARCH_PROGRAMME.md`, formalize goals → `research/GOALS.md`.

## Phase 1 — Tier 1 fact-finding (in progress)

Rabbit Agent work, run in parallel since G1–G3 are independent:
- **G1** SCOTUS/circuit-court broker duty-of-care decision — exact citation and holding.
- **G2** FMCSA/Duffy fraud initiative — primary-source confirmation.
- **G3** Current NSF SBIR/STTR solicitation — actual template, not assumed.

Output lands in `research/evidence.md`. Nothing in Phase 2+ should cite these topics
until Phase 1 entries exist with primary-source confidence.

Each G1-G3 branch should be a separate task packet. Run them in parallel, then run an
evidence-verification gate before Synthesis. A failed gate returns only the failed claim
to Rabbit with a concrete query and a maximum of two attempts.

**Exit criteria:** G1–G3 each have at least one primary-source evidence entry, or an
explicit "could not verify, here's the best secondary source" note if primary sources
don't exist publicly.

## Phase 2 — Landscape fill-in (parallel with late Phase 1)

- **G4** Competitor classification (13 companies).
- **G5** CAVRA Standard status.
- **G6** Association/standards-body positions.
- **G7** Data-sharing incentive precedent (analogous industries).
- **G8** Small-carrier equity angle (lead with OOIDA).

**Exit criteria:** `RESEARCH_PROGRAMME.md` §3 (stakeholder table) and §5 (competitive
landscape) can be rewritten from "asserted" to "sourced" language.

## Phase 3 — Direct questions back to the user/team

- **G9** Status of the four exploratory interviews (OKN pilot note) — not web-researchable.
- Confirm whether "destructively consolidate" instinct from earlier (archiving originals,
  one canonical programme doc) matches how the team wants to keep working, now that a
  `research/` working layer exists alongside it.

This phase is a short conversation, not agent work — flag it and move on rather than
blocking Phase 4 on it.

## Phase 4 — Synthesis

Synthesis Agent rewrites `RESEARCH_PROGRAMME.md` §3, §4, §5 from the now-populated
`research/evidence.md`, with named uncertainty preserved for anything still single-sourced.
Produces `research/briefing.md` per the roster's Synthesis Agent contract if the briefing
needs to diverge from the top-level programme doc (e.g., a longer-form ~50pp intelligence
report vs. the working programme doc) — otherwise the programme doc itself stays the
single briefing artifact. Default to the latter (one doc) unless deliverable format
requirements force a split.

## Phase 5 — Review

Review Agent runs the four adopted personas (NSF reviewer, transportation lawyer,
skeptical VC, FMCSA official) against the Phase 4 output. Priority objection to test
first: the data-sharing incentive assumption (G7) — this is the load-bearing assumption
the whole OKN model rests on and currently has zero direct evidence.

Output: `research/review-notes.md`, tagged open/resolved.

Every open finding must become a targeted Rabbit task, a Synthesis rewrite task, a
Publishing/Visualization correction, or a human decision. Findings without a route are
not complete review work.

## Phase 6 — Publishing

Only after G3 (actual SBIR template) is confirmed. Publishing Agent produces, in order of
dependency:
1. NSF SBIR Concept Memo (~5pp) — needs Phase 4+5 complete.
2. SBIR Draft Sections, mapped to whatever the real solicitation requires (structure is
   currently unknown pending G3 — don't draft against the assumed Problem/Innovation/
   Technical Approach/Market/Commercialization structure until confirmed).
3. Stakeholder one-pagers (FMCSA/regulator version, association version, pilot-partner
   version).
4. Regulatory timeline + technology landscape as standalone references.

## Phase 7 — Visualization

Can start as soon as Phase 4 briefing stabilizes for a given section — doesn't need to
wait for all of Phase 6. Priority order matches what Publishing needs first:
1. Stakeholder power/influence matrix (feeds the SBIR concept memo's "who benefits" case).
2. Regulatory timeline (feeds concept memo + one-pagers).
3. Duty-of-care chain diagram (Shipper → Broker → Carrier → Driver) — cannot be finalized
   until G1 is resolved, since the diagram's whole point is showing where liability
   attaches per the actual case holding.
4. Freight OKN architecture diagram.
5. Empty-mile/goods-movement process flow.
6. Competitive landscape map (needs G4 complete).

Publishing and Visualization may run in parallel after the relevant briefing section
passes review. Both outputs then pass the shared deliverable QA gate. New factual claims
discovered during production go back to Rabbit; they are not added ad hoc.

## Phase 8 - Cycle closeout

At the end of each research cycle, the Orchestrator records accepted, unverified,
contradicted, and blocked claims; open review findings and owners; retries and duplicate
work; source-freshness dates; and the next cycle's task packets. The cycle closes only
when every load-bearing claim has an explicit status and no high-severity finding is
silently omitted.

## What "done" looks like for this pass

Not a finished SBIR application — a programme doc where every load-bearing claim in
§1, §3, §4, §5 has a primary-source citation or is explicitly marked unverified, plus a
short list of questions that only the user/team can answer (Phase 3). That's the
deliverable to bring back for a go/no-go conversation on the SBIR angle itself.

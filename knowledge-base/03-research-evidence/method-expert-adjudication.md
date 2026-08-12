---
type: method
status: required
schema_version: 1.0.0
updated: 2026-08-08
tags:
- type/method
- lifecycle/required
- domain/freight
- domain/identity
- programme/e1
---
# Expert Adjudication

A blinded, multi-reviewer process for creating E1 gold labels without letting model output,
risk scores, or adverse-history information determine identity truth. The controlling human
procedure is [[e1-adjudication-decision-tree]] and the semantic contract is
[[e1-carrier-identity-and-relationship-standard]].

## Reviewer structure

- **Reviewer 1 and Reviewer 2** label every hard identity case independently.
- Reviewers receive the same evidence packet and source timestamps but no model prediction,
  model score, candidate-generation score, or other anchoring output.
- A **third adjudicator** reviews disagreements under the written standard. The third reviewer
  does not erase the first two votes; all labels, rationales, and disagreement codes remain in
  the benchmark.
- Reviewers may return `UNRESOLVED`; forced binary labeling is prohibited.
- Conflicts of interest and prior knowledge of a case are declared and recorded.

## Training and qualification

Before gold labeling, reviewers work a training set drawn from [[e1-edge-case-suite.csv]]. A
reviewer must demonstrate consistent use of the Task A/B/C distinctions, claimed-versus-
assigned identifiers, temporal cutoffs, and the regulatory-disposition boundary. Any case that
causes systematic reviewer disagreement is treated first as a specification defect, not as
reviewer error.

## Blinding and evidence separation

- Task A identity adjudicators are blinded to safety scores, enforcement/motive indicators,
  commercial fraud scores, and model outputs.
- Evidence created after the model's feature cutoff may be used for retrospective gold truth
  only when separately recorded under the adjudication cutoff.
- State-law legal status and FMCSA registration status remain different predicates.
- A final §386.73 disposition may establish a regulatory relationship/disposition; it does not
  retroactively collapse two legal-person nodes.

## Agreement and sensitivity reporting

Report raw agreement, a chance-corrected agreement statistic appropriate to the realized label
structure, label-specific disagreement rates, and adjudication rate. Preserve reviewer-level
votes so model metrics can be re-run under: (a) final adjudicated labels; (b) exclusion of
contested cases; and (c) reviewer-specific labels. Gupta et al. 2024 is retained as a
methodological precedent for two independent reviewers plus third-reviewer adjudication and for
examining sensitivity to reviewer variation; it is not a freight-domain authority.

## Outputs

For each case: reviewer ID, label, relationship states, evidence relied on, source timestamps,
rationale code, confidence, unresolved reason, COI flag, start/end time, third-review outcome,
and any post-adjudication correction.

## Controls

- Gold labels are versioned and frozen before final model evaluation.
- Any change to the identity standard after benchmark construction requires a versioned
  amendment, affected-case re-adjudication, and explicit metric restatement.
- Review-time comparisons use matched evidence packets and randomized order.
- Reviewer disagreement is a scientific result.

- Linked dataset: [[dataset-e1-adjudicated-carrier-identity-cases]], [[dataset-openepcis-generated-event-logs]].
- Linked experiments: [[experiment-e1-entity-resolution-and-identity-assurance]], [[experiment-e2-facility-event-provenance-and-dwell-reconstruction]].
- Evidence: [[source-gupta-2024-manual-record-linkage-gold-standard]], [[source-gao-12-364-chameleon-carrier-matching]], [[source-ecfr-386-73-reincarnated-carrier-standard]].

## Operational-review separation

Gold adjudicators are never reused as the C4 runtime review panel for the confirmatory workflow experiment. Operational reviewers are separately randomized to manual/assisted cases and evaluated against frozen gold, preventing the benchmark from partly grading itself. See [[e1-statistical-analysis-and-preregistration-plan]].

## Agreement statistics

Report observed agreement and label-specific agreement first. Also report Cohen's kappa and a prevalence-robust complement such as Gwet's AC1, with confidence intervals where feasible. No single chance-corrected statistic or arbitrary cutoff determines whether the gold standard is valid. Persistent disagreement triggers specification review and reference-standard sensitivity analysis.

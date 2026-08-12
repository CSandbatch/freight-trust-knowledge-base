---
type: method
status: candidate
schema_version: 1.0.0
updated: 2026-08-08
tags:
- type/method
- domain/identity
- domain/governance
- domain/legal
- confidence/mixed
- audience/internal
- programme/e1
- lifecycle/candidate
---
# E1 adjudicator governance and training protocol — RC1

## Purpose

Turn [[e1-carrier-identity-and-relationship-standard]] into a reproducible human labeling process. This protocol controls who may label cases, what they may see, how disagreements are handled, how conflicts are disclosed, and what evidence can be added after a case packet is frozen.

The methodological basis for multiple independent reviewers and third-reviewer adjudication is [[source-gupta-2024-manual-record-linkage-gold-standard]]. Domain semantics remain controlled by the E1 identity standard and its primary regulatory sources.

## Roles

### Protocol owner

Maintains the case schema, standard version, source manifests, reviewer instructions, audit log, and freeze status. The protocol owner may prepare cases but must not alter a gold label after seeing model test performance.

### Primary Reviewer A and Primary Reviewer B

Independently label each hard case. They do not confer before submitting their initial decisions. At least one primary reviewer on the adjudication panel should have demonstrated familiarity with FMCSA registration/operating-authority records and state corporate filings; the other may emphasize data/entity-resolution methodology, provided both have passed the same training protocol.

### Third adjudicator

Reviews a disagreement only after both primary votes are locked. The adjudicator may select either primary label, a third permissible label, or `UNRESOLVED`. The role is not to force consensus.

### PI

Approves the scientific target, reviewer qualification rule, amendment policy, and final freeze. The PI does not need to adjudicate every case.

### Model-development team

May propose candidate-generation strata and document feature requirements, but must not control held-out gold labels. A person who has inspected model predictions for a held-out case is ineligible to act as a blinded primary adjudicator for that case.

## Operational-review firewall

The gold-adjudication panel is distinct from the C0/C4 operational reviewer panel. Gold adjudicators do not perform runtime review on confirmatory workflow cases. Operational reviewers are randomized to manual or assisted cases and are scored only against frozen gold.

## Reviewer independence / conflict-of-interest rules

A reviewer must disclose and recuse from a case where the reviewer:

1. owns, works for, advises, represents, litigates against, insures, brokers for, contracts with, or has a material financial interest in a carrier or closely related party in the case;
2. has a close personal/familial relationship with a material owner/officer/manager in the case;
3. participated in the underlying FMCSA/state investigation, enforcement action, litigation, corporate transaction, or source-record creation in a way that gives material non-packet knowledge;
4. previously assigned or modified the benchmark gold label for the same case;
5. has seen a held-out model's prediction/score/explanation for the case before submitting the initial human label; or
6. cannot separate personal knowledge from evidence preserved in the packet.

Recusal is not an adverse event. It is logged as `REVIEWER_RECUSED` and a replacement reviewer receives the frozen packet.

## Reviewer packet

Every reviewer sees the same versioned packet containing only evidence permitted for the adjudication cutoff. At minimum:

- case ID/version and decision-as-of date;
- legal-name/name-history observations;
- authoritative state-entity records available for the case;
- authoritative FMCSA registration/USDOT assignment records;
- operating-authority records separately;
- source-specific addresses/phones/contacts with dates;
- ownership/management evidence where permitted;
- transaction filings/documents where available;
- equipment/insurance/employee/operational-continuity evidence where relevant to Task C;
- source IDs, retrieval dates, provenance, and authority-for-predicate flags;
- explicit conflicts/staleness/corrections;
- sensitivity/redaction flags; and
- a field identifying evidence that exists for retrospective adjudication but is later than the model feature cutoff.

The packet must not contain tested-model scores, model-generated clusters, model explanations, or candidate-generation ranks unless the case is explicitly a non-gold training exercise about leakage.

## Supplemental evidence requests

Reviewers do not independently browse the web while labeling a frozen benchmark case. If a reviewer believes essential evidence is missing, the reviewer submits an `EVIDENCE_REQUEST` stating the missing predicate and competent source class.

The protocol owner then either:

- retrieves the evidence through the documented source process and versions the packet for **all** reviewers; or
- records that the evidence is unavailable and leaves `UNRESOLVED` available.

This prevents one reviewer from silently creating a richer evidence universe than another.

## Labeling order

Reviewers answer in this order to reduce category bleed:

1. **Task A — legal-person identity** without motive/safety/adverse-history information.
2. **Task B — authoritative identifier/registrant continuity.**
3. **Task C — typed relationships among distinct persons.**
4. **Regulatory disposition** only from status-bearing authoritative agency/court material.
5. confidence/uncertainty and evidence-needed fields.

A Task C continuity relation must never be used retroactively to rewrite Task A legal-person identity unless independent legal-person evidence supports that result.

## Training stages

### Stage T0 — orientation

Reviewer reads:

- [[e1-carrier-identity-and-relationship-standard]];
- [[e1-adjudication-decision-tree]];
- [[e1-state-corporate-source-access-memo]];
- the source cards for §386.73, current USDOT/OA guidance, and the CMAK/Chazon final order.

### Stage T1 — worked synthetic cases

Use selected cases from [[e1-edge-case-suite.csv]] with answer/rationale discussion. Minimum coverage:

- identity/name/ownership: EC-001–010;
- weak shared fields and asset continuity: EC-011–020;
- claimed-versus-assigned identifiers: EC-021–030;
- affiliation/substantial continuity/disposition: EC-031–038 and EC-061–063;
- source conflict/time/status: EC-039–043, EC-053–055, EC-064–068;
- accounts/brands/role scope: EC-044–052, EC-070;
- protocol failures and leakage: EC-056–060, EC-069.

### Stage T2 — qualification set

Protocol owner selects a balanced subset of clear and ambiguous synthetic cases without showing the answer key during review. Qualification is procedural, not a claim that humans are infallible.

A reviewer qualifies only if:

- the reviewer makes **zero Critical category errors** (for example: merges affiliate into legal identity; treats OA as person identity; treats claimed USDOT as assignment; calls an analyst score a final reincarnation disposition; uses motive to decide Task A; forces an unresolved case); and
- any remaining disagreements are reviewed and retrained before real-case adjudication.

No arbitrary percentage score can override a Critical category error.

### Stage T3 — pilot real cases

Before full corpus construction, double-label a small stratified pilot. Measure disagreement by case type and identify rules that reviewers interpret differently. The pilot may revise RC1 before the held-out benchmark is frozen.

## Agreement reporting

Report raw observed agreement and label-specific agreement as the first-line reproducibility results. Because chance-corrected coefficients can behave differently under skewed prevalence, report Cohen's kappa together with a complementary statistic such as Gwet's AC1; do not use one arbitrary coefficient cutoff as a freeze gate. Preserve reviewer-level confusion matrices and bootstrap/design-aware uncertainty where feasible.


At minimum preserve and report:

- raw pairwise agreement;
- confusion/disagreement matrix by label;
- unresolved rate;
- disagreement rate by difficulty stratum and subgroup;
- third-adjudication rate;
- review time per case;
- evidence-request rate; and
- sensitivity analysis in which disputed cases are excluded or alternative plausible labels are tested.

A chance-corrected agreement statistic may be reported, but it does not replace the raw disagreement table, especially where label prevalence is highly imbalanced.

## Reviewer audit fields

For each decision preserve:

```yaml
review_id: ...
case_id: ...
case_version: ...
standard_version: 1.0.0-rc1
reviewer_pseudonym: ...
reviewer_role: primary_a | primary_b | adjudicator
training_version: ...
conflict_check: pass | recused
packet_hash: ...
started_at: ...
submitted_at: ...
task_a_label: ...
task_b_label: ...
task_c_labels: ...
disposition_label: ...
confidence: ...
evidence_request_ids: []
rationale: ...
```

Reviewer identity can remain internally controlled; public benchmark releases should not expose unnecessary personal information.

## Change control

If a real pilot reveals ambiguity in the standard:

1. pause affected labeling;
2. open a protocol issue;
3. retrieve controlling evidence;
4. run the hostile evaluator against the proposed amendment;
5. version the standard and training packet;
6. identify every already-labeled case affected;
7. relabel those cases under the new version; and
8. preserve the old labels/version in the audit history.

Once the held-out test set has been opened to model evaluation, no semantic amendment may be made merely because it improves a model result.

## Freeze gate satisfied by this artifact

This document satisfies the **written reviewer-panel/COI/training-protocol** portion of the Step 1 freeze gate. It does **not** satisfy the human execution gate: actual reviewers must still complete training and the pilot double-label exercise.

Related: [[method-expert-adjudication]] · [[e1-definition-freeze-review]] · [[dataset-e1-adjudicated-carrier-identity-cases]]

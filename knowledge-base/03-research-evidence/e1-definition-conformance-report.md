---
type: log
status: current
schema_version: 1.0.0
updated: 2026-08-08
tags:
- type/log
- domain/identity
- domain/knowledge-engineering
- confidence/primary
- audience/internal
- programme/e1
- lifecycle/current
---
# E1 definition conformance report — RC1

Automated structural/conformance validation of the Step 1 freeze-candidate package. **27/27 checks passed.** This validates internal consistency, not legal correctness or human adjudicator performance.

## Results

| Check | Result | Detail |
|---|---|---|
| Ontology parses as YAML | **PASS** |  |
| Ontology is RC1 freeze candidate | **PASS** | version=1.0.0-rc1 status=freeze-candidate |
| Same-legal-person relation is explicit equivalence | **PASS** |  |
| Operating authority does not entail identity | **PASS** |  |
| Substantial continuity does not entail identity | **PASS** |  |
| Substantial continuity does not entail final reincarnation | **PASS** |  |
| Task A has exactly the four frozen labels | **PASS** | ['SAME_LEGAL_PERSON', 'DISTINCT_LEGAL_PERSON', 'UNRESOLVED', 'OUT_OF_SCOPE'] |
| F0-F6 feature regimes all present | **PASS** | F0,F1,F2,F3,F4,F5,F6 |
| Anchor-visible F0 is not headline | **PASS** |  |
| F1-F6 carry headline eligibility | **PASS** |  |
| All critical hard prohibitions encoded | **PASS** | all present |
| Edge-case suite contains 70 cases | **PASS** | n=70 |
| Edge-case IDs are unique | **PASS** |  |
| Edge-case IDs are contiguous EC-001..EC-070 | **PASS** | first=['EC-001', 'EC-002'] last=['EC-069', 'EC-070'] |
| Research report declares S01-S16 | **PASS** | S01,S02,S03,S04,S05,S06,S07,S08,S09,S10,S11,S12,S13,S14,S15,S16 |
| Every edge-case source ID resolves in source map | **PASS** | all resolve |
| Claims ledger contains 64 unique claims | **PASS** | n=64 unique=64 |
| Claims ledger reaches ID-R-064 | **PASS** | ID-R-064 |
| Every S01-S16 source-map card exists | **PASS** | all exist |
| Complete RC1 Step 1 artifact set exists | **PASS** | all exist |
| Standard excludes F0 as headline | **PASS** |  |
| Standard explicitly permits unresolved | **PASS** |  |
| Standard separates analytical continuity from final reincarnation | **PASS** |  |
| Standard distinguishes vendor evidence from competent authority | **PASS** |  |
| Hostile review records initial failure | **PASS** |  |
| Hostile review records post-remediation pass to human review | **PASS** |  |
| Human execution remains explicitly pending | **PASS** |  |

## Artifact hashes

Hashes provide a reproducibility anchor for the two machine-readable RC1 artifacts before human freeze review.

```yaml
e1-identity-ontology.yaml: sha256:259471887c8ff21fb67c319f4ba31acbfdf0f3fb50e7c57fab31389aa28ffb08
e1-edge-case-suite.csv: sha256:34f067dae8c08b4785ab893027da7b524cf8037975cf710e8b5b0091431df910
```

## Disposition

**Structural conformance PASS.** RC1 may proceed to PI/domain/counsel and actual reviewer-training/pilot execution. It must not be called scientifically or legally validated until those human gates are complete.

Related: [[e1-carrier-identity-and-relationship-standard]] · [[e1-definition-freeze-review]] · [[e1-adjudicator-governance-and-training]] · [[e1-state-corporate-source-access-memo]]

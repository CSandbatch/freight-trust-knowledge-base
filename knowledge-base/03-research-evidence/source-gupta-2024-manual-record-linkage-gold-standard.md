---
type: source
status: active
schema_version: 1.0.0
source_class: peer-reviewed
verification: confirmed
accessed: 2026-08-08
updated: 2026-08-08
review_by: 2028-08-08
tags:
- type/source
- domain/identity
- confidence/peer-reviewed
- audience/internal
- programme/e1
- lifecycle/active
---
# Gupta et al. 2024 — manual review and adjudication for record-linkage gold standards

## Citation

Agrayan K. Gupta, Huiping Xu, Xiaochun Li, Joshua R. Vest, Shaun J. Grannis. “Manual Evaluation of Record Linkage Algorithm Performance in Four Real-World Datasets.” *Applied Clinical Informatics* 15(3), 2024, 620–628. DOI: 10.1055/a-2291-1391. PMCID: PMC11290950.

<https://pmc.ncbi.nlm.nih.gov/articles/PMC11290950/>

## What the study contributes methodologically

The paper is outside freight and therefore contributes **adjudication method**, not domain labels. Across four real-world record-linkage datasets, the study used trained reviewers, at least two independent reviewers per pair, and a third reviewer to adjudicate disagreements.

Reported discordance across datasets ranged from 1.8% to 13.6%, while one reviewer showed a 59% discordance rate in one dataset. The authors use this to demonstrate that reviewer variation can materially alter the apparent performance of the matching algorithm.

The paper also documents reviewer training, a standard review interface, reviewer characteristics, raw discordance, and sensitivity analyses that change labels on disputed pairs.

## E1 consequence

- two independent primary reviewers for hard E1 cases;
- a third independent adjudicator for disagreements;
- explicit reviewer training against a seed set;
- raw agreement plus a chance-corrected agreement statistic;
- preserve original reviewer votes and disagreement, rather than overwriting them with the final label;
- sensitivity analysis on disputed labels;
- capture reviewer characteristics/conflict rules where relevant to bias analysis;
- do not pretend expert review is infallible ground truth.

## Consumers

[[method-expert-adjudication]] · [[e1-carrier-identity-and-relationship-standard]] · [[e1-definition-freeze-review]]

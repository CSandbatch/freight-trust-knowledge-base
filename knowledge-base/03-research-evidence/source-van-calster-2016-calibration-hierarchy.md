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
- domain/data-science
- domain/identity
- confidence/peer-reviewed
- audience/internal
- programme/e1
- lifecycle/active
---
# Van Calster et al. — calibration hierarchy

## Citation

Ben Van Calster, Daan Nieboer, Yvonne Vergouwe, Bavo De Cock, Michael J. Pencina, Ewout W. Steyerberg. “A calibration hierarchy for risk models was defined: from utopia to empirical data.” *Journal of Clinical Epidemiology* 74, 2016, 167–176. DOI: 10.1016/j.jclinepi.2015.12.005.

<https://pubmed.ncbi.nlm.nih.gov/26772608/>

## Methodological contribution

Calibration is not a single scalar property. Calibration-in-the-large/intercept, calibration slope, and the shape of the calibration curve provide distinct information; probabilistic predictions should be assessed over their range rather than summarized only by an expected calibration error.

## E1 consequence

E1 reports calibration intercept, slope, smooth reliability curve and Brier score. ECE may be reported as a secondary descriptive statistic but is not the sole calibration criterion.

## Consumers

[[e1-statistical-analysis-and-preregistration-plan]] · [[method-probabilistic-entity-resolution]] · [[experiment-e1-entity-resolution-and-identity-assurance]]

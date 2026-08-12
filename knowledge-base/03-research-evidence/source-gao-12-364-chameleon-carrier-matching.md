---
type: source
status: active
schema_version: 1.0.0
source_class: primary
verification: confirmed
accessed: 2026-08-08
updated: 2026-08-08
review_by: 2027-08-08
tags:
- type/source
- domain/identity
- domain/regulatory
- confidence/primary
- audience/internal
- programme/e1
- lifecycle/active
---
# GAO-12-364 — chameleon-carrier matching as targeting, not ground truth

## Citation

U.S. Government Accountability Office, *Motor Carrier Safety: New Applicant Reviews Should Expand to Identify Freight Carriers Evading Detection*, GAO-12-364, March 2012.

Landing page: <https://www.gao.gov/products/gao-12-364>  
PDF: <https://www.gao.gov/assets/gao-12-364.pdf>

Direct PDF retrieval and text extraction succeeded 2026-08-08.

## What GAO did

GAO developed a data-matching method to identify new applicants with **chameleon attributes**. Its analysis required two components:

1. registration information matching a previously registered carrier; and
2. a prior carrier having a defined motive for evading detection, such as specified adverse safety/enforcement history or bankruptcy.

The matching fields included company/carrier name, company officers, SSN, EIN, Dun & Bradstreet number, phone, and address, with different weights. GAO used a match-score threshold as a targeting mechanism.

## The methodological caveat is load-bearing

GAO explicitly states that data analysis by itself cannot positively identify a chameleon carrier. Vehicle matches can arise from legitimate asset purchases, names can coincide, and further investigation/legal process is necessary to determine why an apparent relationship exists. GAO later reiterates that further investigation would be needed to confirm whether carriers on its list actually were chameleons.

This makes GAO's output a **screening / targeting construct**, not a legal-person identity gold standard.

## Why weak fields are dangerous

GAO's appendix shows the enormous difference in discriminating power among fields. Address matches occurred in more than ten million carrier-pair comparisons in its working universe, whereas strong numeric identifiers were far rarer. This is direct evidence against treating address or name overlap as identity-dispositive.

## E1 consequence: separate identity from motive

GAO's historical design used motive both to define “chameleon attributes” and to examine the match threshold. That is reasonable for a targeting exercise but inappropriate for E1 Task A. If adverse history enters the gold identity label, the identity benchmark becomes circular and can encode “bad history” as evidence of sameness.

Therefore:

- safety/enforcement/bankruptcy motive is **excluded** from Task A legal-person gold labels;
- it may be preserved in a separate regulatory-risk or “candidate for specialist review” layer;
- GAO's methodology is prior art for multi-field matching and targeting, not ground truth for entity identity.

## Prior-art implication

The project cannot claim novelty for the idea of combining carrier record similarity with motive/risk signals. The defensible research gap is reproducible measurement on a labeled, temporally explicit, provenance-bearing identity/relationship corpus, with abstention and contestability.

## Consumers

[[e1-carrier-identity-and-relationship-standard]] · [[e1-definition-freeze-review]] · [[experiment-e1-entity-resolution-and-identity-assurance]]

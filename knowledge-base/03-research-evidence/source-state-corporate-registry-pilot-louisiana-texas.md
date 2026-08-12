---
type: source
status: active
schema_version: 1.0.0
source_class: primary
verification: confirmed
accessed: 2026-08-08
updated: 2026-08-08
review_by: 2027-02-08
tags:
- type/source
- domain/identity
- domain/legal
- domain/data-access
- confidence/primary
- audience/internal
- programme/e1
- lifecycle/active
---
# State corporate-registry pilot — Louisiana and Texas official access paths

## Sources

### Louisiana Secretary of State

Official Commercial Division business-filing search:
<https://coraweb.sos.la.gov/commercialsearch/commercialsearch.aspx>

The public search supports lookup by:

- entity name;
- charter/trade-registration/name-reservation number; and
- officer or agent name.

Louisiana Business Services identifies the Secretary of State Commercial Division as the state service for business filings and the geauxBIZ/business-services ecosystem.

### Texas Secretary of State

Official Business & Public Filings Division / SOSDirect materials:

- <https://www.sos.state.tx.us/corp/searches.shtml>
- <https://www.sos.state.tx.us/corp/options.shtml>
- <https://www.sos.state.tx.us/corp/instructions-for-copies.shtml>

SOSDirect supports business-entity searches, entity information/status, filing history, document images, and copies/certificates. The official instructions state that a search can incur a $1 search fee and document copies can incur additional page/certification fees.

### Texas Comptroller

Official Franchise Tax Account Status materials:
<https://comptroller.texas.gov/taxes/franchise/account-status/search.php>
<https://comptroller.texas.gov/taxes/franchise/coas-instructions.php>

The Comptroller explicitly describes this status as the taxable entity's **right to transact business in Texas** and separately directs users to Secretary-of-State filings for formation/termination/reinstatement purposes.

## What this pilot establishes

There is no safe national assumption that state-law legal-person evidence can be acquired through one uniform public interface.

- Louisiana exposes a public official search interface but places a reCAPTCHA on the search flow.
- Texas makes authoritative filing history available through SOSDirect with session/account/payment mechanics and per-search/document fees.
- Texas Comptroller status is useful evidence but answers a **tax/right-to-transact** predicate, not the same predicate as legal formation, merger, conversion, or dissolution filings maintained by the Secretary of State.

## E1 consequences

1. `state_legal_person_id` must be jurisdiction-qualified; never treat a name alone as a national corporate identifier.
2. The benchmark acquisition pipeline needs **state adapters** and a per-jurisdiction source-access memo.
3. An official tax/franchise-status flag must not silently become a legal-existence label.
4. Vendor/aggregator records may help candidate generation but cannot override the relevant official state filing for legal-person adjudication.
5. Access method, fee, retrieval date, document identifier, and redistribution rights must be recorded separately from the adjudicated fact.
6. Automated/bulk retrieval must be reviewed against each official site's terms/access controls before implementation; this source card does not authorize scraping or bypassing reCAPTCHA/payment controls.

## Consumers

[[e1-state-corporate-source-access-memo]] · [[e1-identity-definition-research-report]] · [[e1-identity-claims-ledger]] · [[e1-carrier-identity-and-relationship-standard]] · [[dataset-e1-adjudicated-carrier-identity-cases]]

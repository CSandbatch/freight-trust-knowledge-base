---
type: source
status: active
schema_version: 1.0.0
source_class: primary
verification: confirmed
accessed: 2026-08-08
updated: 2026-08-08
review_by: 2026-11-08
tags:
- type/source
- domain/identity
- domain/regulatory
- confidence/primary
- audience/internal
- programme/e1
- lifecycle/active
---
# FMCSA Motus — user identity, company account, and business verification are distinct objects

## Citations

Federal Motor Carrier Safety Administration, current Motus materials retrieved 2026-08-08:

- *Move into Motus*: <https://www.fmcsa.dot.gov/registration/move-motus>
- *What is a user profile in Motus: USDOT Registration System?*: <https://www.fmcsa.dot.gov/faq/what-user-profile-motus-usdot-registration-system>
- *What is a company account in Motus: USDOT Registration System?*: <https://www.fmcsa.dot.gov/faq/what-company-account-motus-usdot-registration-system>
- *Motus Supporting Company Job Aid*: <https://www.fmcsa.dot.gov/registration/motus-supporting-company-job-aid>
- Policy notice: <https://www.fmcsa.dot.gov/regulations/federal-register-documents/2026-08334>

## What the source establishes

Motus now makes several identity layers explicit:

1. **User profile** — one profile belongs to an individual user, can access multiple company accounts, and requires Login.gov plus identity verification.
2. **Company account** — a business/organization account used to manage business information, users, registrations, and filings; creation requires business information and business verification.
3. **Registration record** — the regulated entity's USDOT/operating-authority records managed through the company account.

FMCSA also describes Motus as using identity verification and business-address validation as fraud-prevention controls.

## E1 consequence

A human who logs into Motus is not the carrier legal entity, and a Motus company account is not itself the legal person or USDOT registration. The ontology must therefore keep `HumanActor`, `CompanyAccount`, `LegalPerson`, and `FMCSARegistration` distinct.

## Novelty consequence

As of 2026, point-of-registration human identity proofing and business verification are active FMCSA capabilities. Freight Trust should not describe E1 as novel merely because it verifies an individual applicant or validates a business during registration. The stronger research target is **longitudinal entity and relationship reconstruction across records and time, with provenance, uncertainty, and contestability**.

## Consumers

[[e1-carrier-identity-and-relationship-standard]] · [[e1-identity-ontology.yaml]] · [[experiment-e1-entity-resolution-and-identity-assurance]]

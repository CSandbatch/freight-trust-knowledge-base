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
- domain/regulatory
- confidence/primary
- audience/internal
- programme/e1
- lifecycle/active
---
# FMCSA — USDOT identity continuity and operating-authority transfer guidance

## Citations

1. FMCSA, *DO NOT Sell, Purchase, or Lease a USDOT or MC Number*, 2026-03-19.  
   <https://www.fmcsa.dot.gov/newsroom/do-not-sell-purchase-or-lease-usdot-or-mc-number>
2. FMCSA, *Do I need a new USDOT number if I am changing my company's Legal Name or Form of Business?*, updated 2023-05-20.  
   <https://www.fmcsa.dot.gov/faq/do-i-need-new-usdot-number-if-i-am-changing-my-companys-legal-name-or-form-business>
3. FMCSA, *How do I notify FMCSA of my Operating Authority (OA) ownership change?*  
   <https://www.fmcsa.dot.gov/faq/how-do-i-notify-fmcsa-my-operating-authority-oa-ownership-change>

## USDOT identity rule

FMCSA's current bulletin states that a USDOT number belongs to the same legal person and is not transferable. Its examples sharply distinguish the legal person from the owner:

- a sole proprietor cannot sell the proprietor's USDOT number to a buyer;
- a corporation can be sold to new owners while the corporation, as the same legal person, retains its USDOT number;
- after a merger/acquisition, if the original corporation survives, its USDOT number stays with it;
- if the corporation is dissolved and operations continue only under another/new company, the continuing company requires its own USDOT number and the dissolved entity's number should be deactivated.

This is the strongest current operational guidance for the primary E1 identity anchor.

## The sole-proprietor form-change exception

The older but still published FMCSA FAQ creates an important exception to a naive one-USDOT/one-state-law-entity model. It says FMCSA will allow a sole proprietor to maintain the USDOT number when changing form of business if the new entity operates virtually identically, with no change in officials/address/demographics and identical operations, employees, and assets; the Tax ID may change.

**Consequence:** E1 needs both `legal_person_id` and `fmcsa_registrant_continuity_id`. They coincide in ordinary cases but must not be declared universally identical.

## Operating authority is a different object

FMCSA states that new entities ordinarily obtain their own operating authority, but operating authority may be transferred in a legitimate purchase of an entire operation, including mergers, acquisitions, and restructuring. The 2026 bulletin likewise distinguishes nontransferable USDOT identity from operating-authority transfer in legitimate corporate transactions.

**Consequence:** an MC/OA identifier is not a legal-person identity key. E1 must represent `OPERATING_AUTHORITY_HELD_BY` and `OPERATING_AUTHORITY_TRANSFERRED_TO` as time-bounded relationships.

## Claim versus authoritative assignment

The current bulletin states FMCSA may inactivate a USDOT number used by anyone other than the assigned legal person. Therefore an identifier printed on a tender, email, website, rate confirmation, or other source record is a **claim of identifier use**, not proof of authoritative assignment. The graph must preserve `CLAIMS_USDOT` separately from `USDOT_ASSIGNED_TO`.

## Consumers

[[e1-carrier-identity-and-relationship-standard]] · [[e1-identity-ontology.yaml]] · [[e1-edge-case-suite.csv]] · [[experiment-e1-entity-resolution-and-identity-assurance]]

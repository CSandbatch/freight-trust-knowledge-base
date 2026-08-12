---
type: moc
area: visuals
status: active
schema_version: 1.0.0
tags:
- type/moc
- domain/freight
- lifecycle/active
---
# Visual Index

The editable Mermaid source files are kept alongside this index. The diagrams below render natively in Obsidian; use the linked `.mmd` file to reuse a diagram outside a note.

## Freight-trust system

Source: [[01-freight-trust-system.mmd]]

```mermaid
flowchart LR
  subgraph Evidence sources
    R[Authoritative registrations]
    I[Insurance and safety records]
    F[Facility and telematics events]
    P[Partner workflow records]
  end
  subgraph Freight trust layer
    ER[Entity and evidence graph]
    PV[Provenance and permissions]
    HR[Human review and correction]
  end
  subgraph Decisions and outcomes
    V[Counterparty verification]
    D[Detention measurement and dispute resolution]
    O[Later: coordination and matching]
  end
  R --> ER
  I --> ER
  F --> ER
  P --> ER
  ER <--> PV
  PV <--> HR
  ER --> V
  ER --> D
  ER --> O
```

## Pilot roadmap

Source: [[03-pilot-roadmap.mmd]]

```mermaid
flowchart LR
  A[1. Establish facts] --> B[2. Recruit partners]
  B --> C[3. Set data rules]
  C --> D[4. Build evidence benchmark]
  D --> E[5. Run bounded pilot]
  E --> F{Pass thresholds?}
  F -->|Yes| G[6. Expand carefully]
  F -->|No| H[Revise or stop]
```

## Evidence-governance loop

Source: [[04-evidence-governance-loop.mmd]]

```mermaid
flowchart TD
  S[Source record] --> Q{Authoritative and current?}
  Q -->|No| U[Label secondary, stale, or unverified]
  Q -->|Yes| C[Create claim with source and timestamp]
  C --> A[Apply access and purpose rules]
  A --> H[Human review / decision support]
  H --> X{Participant challenges record?}
  X -->|Yes| R[Correct, annotate, or retain disagreement]
  R --> C
  X -->|No| L[Use within approved workflow]
  U --> H
```

## Phase I technical architecture

Source: [[06-phase1-technical-architecture.mmd]]

```mermaid
flowchart LR
  subgraph Evidence sources
    CR[Carrier records]
    FE[Facility events]
    PR[Public registries]
    TM[Telematics]
  end
  subgraph Aim1["Aim 1: Identity Resolution"]
    ER[Entity resolution engine]
    CB[Calibration benchmark]
  end
  subgraph Aim2["Aim 2: Event Provenance"]
    SA[Signed assertions]
    EC[Event claim schema]
    PV[Provenance verification]
  end
  subgraph Aim3["Aim 3: Governed Federation"]
    PP[Policy enforcement]
    AC[Access control]
    AU[Audit logging]
  end
  subgraph Decision and redress
    DO[Decision output]
    AB[Abstention logic]
    CF[Confidence score]
    CR_LOOP[Correction loop]
  end
  CR --> SA
  FE --> SA
  PR --> SA
  TM --> SA
  SA --> ER
  SA --> EC
  SA --> PP
  ER --> CB
  CB --> DO
  EC --> PV
  PV --> DO
  PP --> AC
  AC --> AU
  AU --> DO
  DO --> AB
  AB --> CF
  CF --> CR_LOOP
  CR_LOOP -.->|feedback| SA
```

## Phase I work plan

Source: [[07-phase1-work-plan.mmd]]

Gantt chart showing 12-month Phase I schedule across three research aims, integration and pilot, customer discovery, and reporting milestones (dates illustrative; shift to actual award start).

## Other reusable visuals

- [[02-stakeholder-pushback-map.mmd]] — stakeholder posture quadrant.
- [[05-regulatory-timeline.mmd]] — regulatory and funding timeline.
- [[08-sbir-submission-map.mmd]] — NSF SBIR proposal document flow and vault-note mapping.


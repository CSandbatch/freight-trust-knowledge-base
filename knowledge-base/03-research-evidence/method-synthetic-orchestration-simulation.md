---
type: method
status: stretch
schema_version: 1.0.0
tags:
- type/method
- lifecycle/stretch
- domain/freight
- domain/orchestration
---
# Synthetic Orchestration Simulation

Simulates loads, trucks, HOS constraints, dwell, service windows, and profit-service-risk weights to compare local and governed planning policies.

- Use: evaluate the later E5 backhaul or dwell-sensitive workflow.
- Strength: permits controlled comparison before partner-scale deployment.
- Limitation: simulated incentives and constraints must be validated against real operations.
- Linked datasets: [[dataset-openepcis-generated-event-logs]], [[dataset-bts-truck-travel-time-data]], [[dataset-permissioned-terminal-facility-event-feed]].
- Linked experiment: [[experiment-e5-orchestration-value]].

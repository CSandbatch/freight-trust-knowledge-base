---
type: source
status: active
schema_version: 1.0.0
source_class: peer-reviewed
verification: confirmed
accessed: 2026-08-18
updated: 2026-08-18
review_by: 2027-08-18
tags:
- type/source
- domain/identity
- domain/data-science
- confidence/peer-reviewed
- audience/internal
- programme/e1
- lifecycle/active
---
# Peeters, Steiner, and Bizer 2025 - entity matching with LLMs

## Citation and verification

Ralph Peeters, Aaron Steiner, and Christian Bizer. "Entity Matching using Large Language
Models." *Proceedings of the 28th International Conference on Extending Database
Technology (EDBT 2025)*, 529-541.

- Paper: <https://www.openproceedings.org/2025/conf/edbt/paper-81.pdf>
- Authors' code, prompts, and data: <https://github.com/wbsg-uni-mannheim/MatchGPT/tree/main/LLMForEM>
- Earlier authors' manuscript: <https://arxiv.org/abs/2310.11244>

The full EDBT paper and authors' artifact repository were retrieved on 2026-08-18. The
model versions, datasets, prompt families, comparison baselines, and cost/runtime analysis
were read directly.

## What the source supports

The study compares hosted and open-weight generative LLMs with fine-tuned RoBERTa and
Ditto matchers across product and bibliographic datasets. It tests zero-shot prompts,
in-context demonstrations, natural-language matching rules, and fine-tuning. It reports
that strong LLMs can be competitive with task-fine-tuned encoders with no or few task
examples and can transfer better to entities outside a PLM's training dataset.

The paper also establishes material prompt sensitivity: there is no prompt that is best
for every model/dataset combination, and demonstrations help some combinations while
hurting others. Few-shot and rule prompts consume substantially more tokens than a basic
zero-shot prompt. The released prompts and outputs make this an unusually reproducible
starting point for an E1 LLM condition.

## Limits

- The tested domains are products and publications, not freight legal persons.
- Evaluation is principally binary pair classification using precision, recall, and F1;
  it does not validate E1's cluster, temporal, `CREATE_NEW`, or abstention requirements.
- The paper parses generated text into yes/no decisions. It does not establish that model
  explanations are faithful evidence or that verbal confidence is calibrated.
- Hosted-model costs and model behavior are dated to the named versions used in the
  experiments; they are not current price or performance guarantees.
- Public benchmark exposure to model pretraining is not ruled out.

## E1 relevance

The source justifies adding a frozen generative-LLM challenger before preregistration,
especially for F6b novel entities and low-label development. E1 must tune prompt form only
on development data, freeze an exact model/provider/prompt, preserve C1 and C2, and judge
the LLM at E1's precision floor, review budget, temporal cutoff, and cluster metrics.

## Consumers

[[experiment-e1-entity-resolution-and-identity-assurance]] ·
[[method-probabilistic-entity-resolution]] ·
[[e1-statistical-analysis-and-preregistration-plan]]

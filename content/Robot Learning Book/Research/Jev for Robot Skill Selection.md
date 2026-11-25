---
type: research-idea
status: proposed
novelty: unverified
tags: [robot-learning, research-idea, jev]
---
# Jev for robot skill selection

[[Research Dashboard]] | Background: [[Jev - TypeSafe AI]], [[16 Evaluation and Uncertainty]]

## Question

Can a structured decision model improve skill selection or failure escalation for a small manipulation system under a fixed observation representation and latency budget?

The contribution would need to be an evaluation finding, an uncertainty method, or a well-characterized failure mechanism. Calling an API by itself does not establish novelty.

## Minimum viable study

Start with offline records from one SO-101 task. Create state descriptions containing only information available at decision time: object visible, gripper position, grasp status estimate, current skill, and elapsed time. Do not include future success or human labels in the input.

Have an explicit labeling rule for the correct next skill and whether the system should ask for help. Use independently checked labels where ambiguity matters; preserve ambiguous examples instead of silently removing them.

| Component | Proposed design |
|---|---|
| Candidate | Jev with a fixed typed skill set |
| Baseline 1 | Hand-written state-machine rules |
| Baseline 2 | Small classifier on the same state fields |
| Baseline 3 | Conventional structured-output model, if available |
| Split | Entire collection sessions held out |
| Primary outcome | Skill-selection error on held-out decisions |
| Secondary outcomes | Brier score, NLL, coverage-risk curve, median/p95 latency |
| Ablations | Remove history; perturb state fields; remove confidence-based abstention |

## Test the mechanism

Separate errors in perception from errors in decision-making. First test decisions with ground-truth state fields, then repeat with actual estimated fields. This reveals whether a promising decision model simply depends on unrealistic perfect input.

Select thresholds and prompts on a validation split. Freeze them before the final evaluation. Match observation content across baselines and count all preprocessing time in latency.

## What would change your mind?

If rules perform just as well and faster on the task, use rules. If Jev improves nominal accuracy but becomes overconfident under sensor corruption, its proposed escalation role is not supported. If a small classifier achieves equivalent performance with modest labels, the hosted model's data-efficiency advantage must be demonstrated rather than assumed.

Only after an offline result should you test a supervised skill wrapper around existing controllers. Measure successful completion, interventions, and failure severity, not just decision accuracy.

## Novelty search

Search primary literature on hierarchical control, skill selection, calibrated robot failure detection, selective prediction, and language-model task planning. Compare with prior systems using probability or value estimates to choose skills. Log sources in [[Reading Template]] with page or section evidence.

- [ ] Define one task and skill inventory
- [ ] Write the labeling rule
- [ ] Build a small offline dataset
- [ ] Run rules and classifier baselines
- [ ] Confirm model access and current interface
- [ ] Freeze the evaluation protocol
- [ ] Decide whether a physical trial is justified

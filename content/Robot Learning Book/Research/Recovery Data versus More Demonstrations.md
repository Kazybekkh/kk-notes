---
type: research-idea
status: proposed
novelty: unverified
tags: [robot-learning, research-idea, imitation-learning]
---
# Recovery data versus more demonstrations

[[Research Dashboard]] | [[06 Imitation and Distribution Shift]]

## Hypothesis

At a fixed collection-time budget, targeted recovery demonstrations improve recovery from held-out small perturbations more than extra nominal successes.

## Design

Choose a reproducible pick-and-place baseline. Compare equal total operator-minute budgets: nominal-only additions versus a mix including recoveries. Keep policy architecture, training steps, camera, and task fixed. Report the number of episodes as well as minutes, because recovery examples may be longer.

Define perturbations that are mild enough for supervised evaluation: an object initially offset within a bounded region or a temporarily occluded view. Keep final test perturbations separate from ones used to design the recovery set.

Primary outcome: task completion after perturbation. Secondary outcomes: nominal success, interventions, completion time, and failure categories. Record intervals and multiple training seeds where resources permit.

## Alternatives and confounders

Recovery data may help because it increases visual diversity rather than because it teaches corrective actions. An ablation can add visually diverse nominal demonstrations. Operator skill, retry selection, and initial-state distribution can also confound results.

## Useful result even if the hypothesis fails

A negative study can show which failures remain unrecoverable from the current observations or which perturbations require control changes. That provides a sharper next question.

Before claiming novelty, inspect data aggregation, human-intervention learning, active demonstration selection, and recovery-policy literature. Anchor the review in [[Reading Template]].

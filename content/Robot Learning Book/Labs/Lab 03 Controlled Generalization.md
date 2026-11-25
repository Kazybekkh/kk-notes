---
type: lab
status: not-started
tags: [robot-learning, lab, evaluation]
---
# Lab 03: controlled generalization

[[Home]] | [[16 Evaluation and Uncertainty]]

**Goal:** distinguish memorizing one setup from handling a defined change.

Start from [[Lab 02 Policy Baseline]]. Choose one variation: object position, object instance, lighting, or camera pose. Keep the others fixed. Write the train and test ranges before inspecting outcomes.

Evaluate a baseline and one intervention under the same reset conditions. Randomize evaluation order and record actual conditions. Use validation conditions for tuning; keep final test conditions untouched.

Report nominal and shifted success separately, with trial counts and uncertainty. Include intervention rate and failure categories. If trials share a session-specific disturbance, discuss that dependence rather than treating every frame as independent evidence.

**Pass condition:** the report states exactly what is new at test time and what remains familiar. It also explains at least one plausible alternative explanation for any observed improvement.

**Extension:** repeat the study on a new day. A result that disappears after recalibration or lighting changes may be revealing a systems dependency rather than a robust learning improvement.

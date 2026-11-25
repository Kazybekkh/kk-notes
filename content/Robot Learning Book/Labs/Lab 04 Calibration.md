---
type: lab
status: not-started
tags: [robot-learning, lab, uncertainty]
---
# Lab 04: calibration and abstention

[[Home]] | [[16 Evaluation and Uncertainty]] | [[Jev for Robot Skill Selection]]

**Goal:** evaluate whether confidence helps decide when to request assistance.

Begin offline with binary decision labels and predicted probabilities. A simple trained classifier is enough; Jev access is not required. Split by session or another meaningful unit.

Compute Brier score and negative log likelihood. Plot confidence versus observed correctness with bin counts. Report the handling of probabilities equal to zero or one; numerical clipping changes reported log loss.

Choose an abstention threshold on validation data. On the test set, report coverage, error among accepted cases, and error among abstained cases. A method that abstains everywhere has low accepted risk but no useful coverage.

Repeat with a specified distribution shift such as corrupted or missing state fields. Keep the corruption protocol fixed across methods.

**Pass condition:** explain the difference between accuracy and calibration, and show how the same threshold behaves under shift.

**Extension:** evaluate multiclass skill selection. State whether confidence is the maximum class probability, an entropy-based score, or another measure; do not silently change the definition between methods.

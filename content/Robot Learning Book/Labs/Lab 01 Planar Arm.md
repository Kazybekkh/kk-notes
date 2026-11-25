---
type: lab
status: not-started
tags: [robot-learning, lab]
---
# Lab 01: planar arm

[[Home]] | [[02 Geometry and Kinematics]]

**Goal:** understand geometry well enough to detect a frame or Jacobian bug. No physical robot is required.

1. Implement the two-link forward kinematics in NumPy.
2. Derive and implement the analytic Jacobian.
3. Approximate each Jacobian column with central finite differences at several nonsingular configurations.
4. Plot two configurations that reach the same point.
5. Implement damped least-squares inverse kinematics with a bounded update.
6. Test reachable, unreachable, and near-singular targets.

Use a small finite-difference step and report sensitivity to its value; floating-point error eventually dominates when the step becomes too small.

**Pass condition:** explain the dimensions of each matrix, demonstrate agreement between analytic and numerical derivatives, and show graceful handling of an unreachable target. “The picture looks right” is not enough.

**Extension:** express a target in a rotated camera frame, transform it to the arm frame, and verify the reach. Record one deliberately reversed transform and the resulting error.

Use [[Experiment Template]] to keep code version, plots, and observations together.

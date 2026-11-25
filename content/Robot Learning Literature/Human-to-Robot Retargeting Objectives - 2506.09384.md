# Analyzing Key Objectives in Human-to-Robot Retargeting

**Paper:** [arXiv abstract](https://arxiv.org/abs/2506.09384) | [PDF](https://arxiv.org/pdf/2506.09384)  
**Start with:** [[Robot Learning Primer]] | **Related:** [[DexCap - 2403.07788]], [[EgoMimic - 2410.24221]]

## In plain English

Retargeting tries to make a robot hand follow a human hand. Exact copying is impossible because the two hands have different joints and contact surfaces. An optimizer must choose which properties matter most: fingertip position, overall posture, object contact, or other constraints. This paper compares objectives experimentally instead of assuming one choice is best.

## Why it matters

If the retargeted pose looks human-like but cannot grasp the object, the downstream policy learns a bad example. The abstract describes an integrated objective and ablation studies in posture retargeting and real teleoperated tasks. An ablation removes one term at a time to test its effect.

## Terms to know

An **optimization objective** is the quantity a solver tries to minimize or maximize. A **kinematic posture** describes joint geometry without modeling forces. **Contact** describes where the hand touches an object, often crucial to manipulation success.

## What to inspect in the PDF

Read the exact objective terms, weights, robot hand, tasks, and failure cases. Decide which terms would still apply to a two-finger gripper; many human-finger details may not.

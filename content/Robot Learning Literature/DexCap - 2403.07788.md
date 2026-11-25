# DexCap: Scalable and Portable Mocap Data Collection

**Paper:** [arXiv abstract](https://arxiv.org/abs/2403.07788) | [PDF](https://arxiv.org/pdf/2403.07788)  
**Start with:** [[Robot Learning Primer]] | **Related:** [[EgoMimic - 2410.24221]], [[Human-to-Robot Retargeting Objectives - 2506.09384]], [[Dexterous Imitation Survey - 2504.03515]]

## In plain English

DexCap is a portable system for recording how a person's wrist and fingers move while handling objects. DexIL is the paired imitation-learning method that turns those records into robot-hand skills. The goal is to collect fine manipulation examples away from a fixed motion-capture studio.

## How the transfer works

The capture system combines SLAM-based tracking, electromagnetic sensing, and 3D environmental observations to reduce lost hand tracking. DexIL uses **inverse kinematics** to map tracked hand motion to a robot and **point clouds** to describe nearby object geometry. The abstract also describes optional human correction during robot rollouts. This is useful because a policy can fail in states that were missing from its original demonstrations.

## What the abstract establishes

It reports evaluation on six dexterous tasks, including learning from in-the-wild capture. It does not by itself establish that the system works with a simple two-finger SO-101 gripper; the hand and sensing assumptions may be different.

## What to inspect in the PDF

Read the hardware bill, calibration process, capture failure cases, retargeting constraints, amount of human correction, and the exact comparison to robot-only demonstrations. Separate the benefit of better capture from the benefit of the DexIL learning algorithm.

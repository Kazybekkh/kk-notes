# EgoEngine: From Egocentric Videos to Robot Demonstrations

**Paper:** [arXiv abstract](https://arxiv.org/abs/2606.12604) | [PDF](https://arxiv.org/pdf/2606.12604)  
**Start with:** [[Robot Learning Primer]] | **Related:** [[EgoMimic - 2410.24221]], [[Robot Learning from Human Videos Survey - 2604.27621]]

## In plain English

EgoEngine starts with first-person video of a human manipulating objects and tries to turn it into robot training data. It addresses two mismatches: the video shows a human rather than a robot, and observed human movement may not be a physically executable robot action.

## Two outputs

According to the abstract, the system creates a robot-style observation video that preserves the scene and timing, and a task-aligned robot action trajectory constrained for feasibility. Experiments in simulation and on physical robots test whether those converted demonstrations can train dexterous visuomotor policies without real-robot demonstrations for the target task.

## Terms to know

**Visual gap** is the difference between human and robot camera observations. **Action gap** is the difference between human motion and robot-executable commands. **Temporal alignment** means corresponding moments in the source and converted demonstration stay synchronized.

## What to inspect in the PDF

Check how robot-style video is generated, how actions are made feasible, what pretrained components or robot data the system still uses, and the exact meaning of its zero-shot claim. A simpler project could evaluate only one gap, such as whether changing the video appearance helps an SO-101 policy.

# ACT and ALOHA: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware

**Paper:** [arXiv abstract](https://arxiv.org/abs/2304.13705) | [PDF](https://arxiv.org/pdf/2304.13705)  
**Start with:** [[Robot Learning Primer]] | **Related:** [[Diffusion Policy - 2303.04137]], [[LeRobot - 2602.22818]], [[UMI - 2402.10329]]

## In plain English

Can comparatively inexpensive robot arms learn precise two-handed tasks from a short set of human demonstrations? This paper presents the ALOHA hardware and a learning method called ACT, **Action Chunking with Transformers**. A person teleoperates the robot to provide examples. The model then predicts a short *sequence* of actions rather than only the next motor command.

## Why action chunks help

A one-step imitator can drift: a small error changes the next observation, causing another error. Human demonstrations also vary in timing. ACT's sequence prediction gives the policy a coherent short plan. The abstract reports six real-world tasks and 80-90% success for two examples after about ten minutes of demonstrations; check the full paper for the exact training and evaluation setup behind those figures.

## Terms to know

**Bimanual** means two arms work together. **Closed-loop visual feedback** means the robot repeatedly uses camera images to correct its action. **End-to-end imitation** means the model is trained to map observations to actions from demonstrations, with relatively little hand-coded task logic.

## What to inspect in the PDF

Find the observation and action formats, teleoperation design, chunk length, temporal ensembling, demonstration count per task, and success-rate definition. Note what happens when objects or camera positions change. For a first project, try an ACT-style baseline on one SO-101 task before exploring human-video transfer.

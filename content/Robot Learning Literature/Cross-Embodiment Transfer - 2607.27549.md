# Cross-Embodiment Transfer via Behavior-Aligned Representations

**Paper:** [arXiv abstract](https://arxiv.org/abs/2607.27549) | [PDF](https://arxiv.org/pdf/2607.27549)  
**Start with:** [[Robot Learning Primer]] | **Related:** [[UMI-on-Air - 2510.02614]], [[EgoMimic - 2410.24221]], [[pi0 - 2410.24164]]

## In plain English

A model trained on one robot does not automatically work on another: their joint angles and reach differ. This paper studies **intermediate representations** that describe what the robot is doing in a way less tied to a particular body. Examples in the abstract include object boxes, language descriptions of motion, and end-effector traces.

## What was studied

The authors build a simulation benchmark for transfer to new embodiments and compare representations inside vision-language-action models. The abstract says end-effector traces are particularly useful and that representations help more when there is a larger prior dataset. This is an empirical claim about their benchmark; test whether it holds for a small dataset and an SO-101.

## Terms to know

An **invariant representation** preserves task-relevant information even when the robot body changes. An **end-effector trace** records where the robot's tool moves through space. An **object bounding box** is a rectangle locating an object in an image.

## What to inspect in the PDF

Check what changes between training and test robots, whether cameras are shared, how much data is used, and whether the representation is available at deployment. A feasible project could compare end-effector targets against joint targets when transferring between two arm configurations.

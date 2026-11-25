# Dexterous Cable Manipulation

**Paper:** [arXiv abstract](https://arxiv.org/abs/2502.00396) | [PDF](https://arxiv.org/pdf/2502.00396)  
**Start with:** [[Robot Learning Primer]] | **Related:** [[Dexterous Imitation Survey - 2504.03515]], [[ACT and ALOHA - 2304.13705]]

## In plain English

Cables are harder than rigid blocks because their shape changes continuously and part of the cable can be hidden or tangled. This paper studies cable tasks with multi-finger hands, including grasping, pulling, and bending. It argues that standard two-finger-gripper work misses some human-like cable operations and that clearer tasks and metrics are needed.

## What makes this distinctive

The abstract describes a taxonomy of cable actions, a task-oriented hand design, and long-horizon manipulation. A **taxonomy** names and separates task types. A **benchmark** defines repeatable tasks and measurements so different methods can be compared. The paper may be more useful for choosing a concrete task and metric than for directly copying its hardware.

## Terms to know

**Deformable object** changes shape under force. **Long-horizon** means success requires many coordinated steps. **Generalization** here could mean a new cable, initial shape, or task; confirm which one the experiments test.

## What to inspect in the PDF

Read the task definitions, hand design, baselines, evaluation metrics, and failure modes. A simpler SO-101 project might study one cable-routing action with a two-finger gripper and document where that hardware reaches its limit.

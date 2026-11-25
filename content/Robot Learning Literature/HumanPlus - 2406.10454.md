# HumanPlus: Humanoid Shadowing and Imitation from Humans

**Paper:** [arXiv abstract](https://arxiv.org/abs/2406.10454) | [PDF](https://arxiv.org/pdf/2406.10454)  
**Start with:** [[Robot Learning Primer]] | **Related:** [[DexCap - 2403.07788]], [[EgoMimic - 2410.24221]], [[Cross-Embodiment Transfer - 2607.27549]]

## In plain English

HumanPlus uses human motion to teach a humanoid in two steps. First, a low-level policy trained in simulation lets the physical humanoid follow a person's body and hand motions in real time. This is called **shadowing**. A person then uses shadowing to collect task demonstrations on the robot. Finally, behavior cloning trains autonomous skills from those robot recordings and egocentric vision.

## Why two steps matter

Directly copying a human pose is difficult: a humanoid has different joints, motors, balance limits, and perception. The low-level controller handles part of that physical translation. The later imitation policy then learns task behavior from demonstrations recorded on the actual machine. The abstract reports a 33-degree-of-freedom humanoid, multiple real-world tasks, and task-dependent success rates of 60-100% using up to 40 demonstrations.

## Terms to know

**Degree of freedom (DoF)** is an independent joint or movement variable. **Low-level policy** controls physical motion; a **skill policy** decides what task-directed motion to perform. **RGB camera** provides ordinary color images without direct depth measurements.

## What to inspect in the PDF

Check how simulation motion transfers to the real robot, which human motions are infeasible, how much task-specific engineering remains, and whether the reported success includes recovery from mistakes. This is conceptually valuable but the hardware scale makes direct reproduction unlikely for a small-arm project.

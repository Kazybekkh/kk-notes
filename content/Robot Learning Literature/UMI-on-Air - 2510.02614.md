# UMI-on-Air: Embodiment-Aware Guidance

**Paper:** [arXiv abstract](https://arxiv.org/abs/2510.02614) | [PDF](https://arxiv.org/pdf/2510.02614)  
**Start with:** [[Robot Learning Primer]] | **Related:** [[UMI - 2402.10329]], [[Diffusion Policy - 2303.04137]], [[Cross-Embodiment Transfer - 2607.27549]]

## In plain English

UMI can produce a manipulation policy from handheld demonstrations, but a deployment robot may have motion limits the human did not face. UMI-on-Air studies this problem for an aerial manipulator: a flying robot with an arm. It adds an embodiment-aware controller that steers the high-level diffusion policy toward motions the physical platform can follow.

## The mechanism

The high-level policy proposes trajectories. A lower-level controller estimates how hard each trajectory would be to track. Its feedback influences diffusion sampling at inference time, favoring feasible actions without requiring an entirely separate policy for every platform. The abstract reports better performance on long-horizon and high-precision aerial tasks.

## Terms to know

**Dynamics** describes how a machine actually moves under forces and motor commands. **Out-of-distribution behavior** means a policy is asked to handle a situation unlike its training data. **Tracking cost** measures how closely a controller can follow a target path.

## What to inspect in the PDF

Find the controller assumptions, how gradients are computed, inference latency, and comparisons to simpler action clipping or trajectory filtering. The general idea may apply to a low-cost arm even though the aerial hardware does not.

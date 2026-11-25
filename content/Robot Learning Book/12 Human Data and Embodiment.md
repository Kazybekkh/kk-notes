---
type: chapter
chapter: 12
status: not-started
tags: [robot-learning, embodiment, human-data]
---
# 12 Human data and embodiment

[[Home]] | Previous: [[11 World Models and Planning]] | Next: [[13 Vision Language Action Models]]

Human video is abundant, but most videos do not contain robot actions. A method must decide what information to transfer: task intent, visual features, hand motion, contact structure, or an executable action sequence.

## Three gaps to keep separate

The **observation gap** is what cameras see: human hands and robot grippers look different. The **kinematic gap** is how bodies can move. The **dynamic and contact gap** concerns forces, friction, compliance, and object interactions. Solving image appearance does not automatically solve physical execution.

~~~mermaid
flowchart LR
  Human["Human video or motion"] --> Perception["Track objects and hands"]
  Perception --> Representation["Shared task representation"]
  Representation --> Mapping["Robot feasibility and action mapping"]
  Mapping --> Policy["Train or condition robot policy"]
  Robot["Robot demonstrations"] --> Policy
~~~

A generic retargeting optimization might be

$$
q^\star=\arg\min_{q\in\mathcal Q}
\sum_j w_j\|f_j(q)-p_j^{\rm target}\|^2
+\lambda\|q-q_{\rm previous}\|^2.
$$

$f_j(q)$ locates robot landmark $j$, $p_j^{\rm target}$ is a desired position after alignment, and $\mathcal Q$ represents feasible configurations. The smoothness term discourages sudden changes. This teaching objective omits important contact and collision details; its weights encode what you care about preserving.

## Different paper families

[[UMI - 2402.10329]] designs a collection interface; [[DexCap - 2403.07788]] captures detailed hand motion; [[EgoMimic - 2410.24221]] aligns human and robot demonstrations; [[HumanPlus - 2406.10454]] connects humanoid motion tracking to task-data collection. Their shared motivation does not make their data requirements interchangeable.

For each method, record what a demonstration contains: RGB, depth, hand poses, robot states, language, force, or tactile readings. Check whether robot data is required during pretraining, calibration, adaptation, or evaluation. “No robot demonstrations” can refer only to one of these stages.

## A project you can actually isolate

For the SO-101, first study whether a simple shared coordinate representation helps across camera poses or small embodiment changes. Hold the task, dataset budget, and evaluation states fixed. A human-video project adds several coupled unknowns at once: perception, alignment, label quality, and policy learning.

**Exercise:** two robots have different link lengths but share an end-effector target. Does a shared Cartesian action automatically make transfer work?

> [!success]- Answer
> No. Reachability, orientation limits, timing, collision, and controller behavior can differ. A shared representation removes some mismatch, not all of it.

Research connection: [[Research Landscape]] and [[Human-to-Robot Retargeting Objectives - 2506.09384]].

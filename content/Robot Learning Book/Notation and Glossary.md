---
type: reference
tags: [robot-learning, glossary]
---
# Notation and glossary

[[Home]] | [[Equation Reference]]

## Symbols

| Symbol | Meaning | Typical units or shape |
|---|---|---|
| $q,\dot q,\ddot q$ | Joint positions, velocities, accelerations | radians, radians/s, radians/s squared for rotary joints |
| $x$ | Task-space position or generic state; context must say which | meters for position |
| $s,o$ | Environment state and sensor observation | model-dependent |
| $a,A$ | One action and an action sequence | controller-dependent |
| $\pi_\theta$ | Policy parameterized by weights $\theta$ | distribution or function |
| $r,\gamma$ | Reward and discount factor | reward units; dimensionless discount |
| $V,Q$ | State value and action value | expected discounted reward |
| $R,t,T$ | Rotation, translation, homogeneous transform | frame-dependent |
| $J(q)$ | Geometric or task Jacobian | relates joint to task velocity |
| $\mathbb E$ | Expectation | probability-weighted average |
| $\nabla$ | Gradient | derivative per parameter |
| $\|x\|_2$ | Euclidean norm | square root of squared-coordinate sum |
| $\mathcal D$ | Dataset | examples, episodes, or transitions |

Symbols are reused across fields. In dynamics, $\tau$ often means torque; in generative modeling it can mean artificial generation time. Always read the local definition.

## Concepts

| Term | Plain explanation | Learn it in |
|---|---|---|
| Action space | Commands the policy is allowed to issue | [[05 Training Neural Policies]] |
| Proprioception | Measurements of the robot's own configuration or motion | [[04 Perception and State]] |
| Forward kinematics | Joint configuration to tool pose | [[02 Geometry and Kinematics]] |
| Inverse kinematics | Desired tool pose to a feasible joint configuration | [[02 Geometry and Kinematics]] |
| Policy | Observation/state to action rule | [[05 Training Neural Policies]] |
| Behavior cloning | Fit actions from demonstrations | [[06 Imitation and Distribution Shift]] |
| Covariate shift | Inputs at deployment differ from training inputs | [[06 Imitation and Distribution Shift]] |
| Receding horizon | Replan after executing part of a predicted sequence | [[07 ACT and Action Sequences]] |
| Advantage | How much better an action is than the policy's usual value | [[09 Reinforcement Learning]] |
| Replay buffer | Stored transitions reused for training | [[10 Offline RL and Data Coverage]] |
| World model | Predictor of how actions change a state or representation | [[11 World Models and Planning]] |
| Embodiment | Robot geometry, actuators, sensors, and physical capabilities | [[12 Human Data and Embodiment]] |
| Retargeting | Map motion between different bodies | [[12 Human Data and Embodiment]] |
| Grounding | Connect symbols or representations to physical observations/actions | [[13 Vision Language Action Models]] |
| Ablation | Remove or alter a component to test its contribution | [[17 Finding a Research Question]] |
| Calibration | Agreement between predicted probabilities and observed frequencies | [[16 Evaluation and Uncertainty]] |
| Epistemic uncertainty | Uncertainty associated with limited knowledge/model evidence | [[16 Evaluation and Uncertainty]] |
| Aleatoric uncertainty | Variability or ambiguity in observations/outcomes under the model | [[04 Perception and State]] |
| Sim-to-real | Transfer from simulated training/testing to physical deployment | [[11 World Models and Planning]] |
| Latency | Time from a relevant observation/event to a usable response | [[15 Robot Systems and Deployment]] |

Distinguish “multimodal input” (images, text, audio) from “multimodal distribution” (multiple plausible output modes).

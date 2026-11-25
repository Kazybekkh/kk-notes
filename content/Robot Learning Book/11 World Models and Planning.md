---
type: chapter
chapter: 11
status: not-started
tags: [robot-learning, planning, simulation]
---
# 11 World models and planning

[[Home]] | Previous: [[10 Offline RL and Data Coverage]] | Next: [[12 Human Data and Embodiment]]

A world model predicts how a state or representation changes after an action. Planning uses that prediction to compare possible futures. It can use a known physics model, a learned transition model, or both.

## Planning over a finite horizon

With a learned deterministic dynamics model $\hat f_\phi$:

$$
a_{t:t+H-1}^\star=
\arg\min_{a_{t:t+H-1}}
\sum_{k=0}^{H-1}c(\hat s_{t+k},a_{t+k})+c_f(\hat s_{t+H}),
\quad
\hat s_{k+1}=\hat f_\phi(\hat s_k,a_k).
$$

$c$ is running cost and $c_f$ is terminal cost. Constraints may restrict joint limits, speed, collision, and contact. Model predictive control executes the first part of the plan, measures again, and replans.

## Why a good-looking video is not enough

A model can generate visually plausible futures that are physically wrong. More importantly, a useful action-conditioned model must predict *how different actions change outcomes*. A video predictor that ignores the proposed action may look convincing and still be useless for control.

If per-step model error is at most $\epsilon$ and error propagation has Lipschitz factor $L$, a simplified bound starting from zero error is

$$
e_H\le\epsilon\sum_{i=0}^{H-1}L^i.
$$

For $L>1$, this bound grows quickly. It requires uniform error and sensitivity assumptions that often do not hold globally; it illustrates why long rollouts can be unreliable.

![[model_error.png]]

*Analytic illustrative bound for different sensitivity factors.*

![[ch11_model_error_planning.mp4]]

*A puck on a tilted table. The learned model has the wrong friction (0.2 instead of 0.6 per second) and does not know about the tilt. A 30-step plan made with it predicts a stop at the goal, but executed open-loop the puck stops 1.65 m away. The state error grows step by step and stays under the bound above, with $\epsilon=0.062$ (the model's largest one-step error on the visited states) and $L=1.042$ (the spectral norm of its transition matrix). Model predictive control with the same model stops 0.11 m from the goal. Source: `Tools/animations/ch11_model_error_planning.py`.*

## Simulation is another model

Isaac Sim gives you a controllable environment, but friction, contact, cameras, latency, and actuator behavior may differ from reality. **Domain randomization** varies simulator parameters so a policy experiences a range of worlds. **System identification** estimates parameters from real measurements. Randomizing unrealistic ranges can make the training task unnecessarily hard.

Your first simulation project should answer a modest question you can test: does a policy's ranking under controlled camera shifts match its ranking on the real arm? Do not treat simulator success as proof of physical deployment.

**Exercise:** what tradeoff arises when you shorten a planning horizon?

> [!success]- Answer
> Shorter rollouts reduce accumulated model error and often computation, but may miss delayed consequences. Better terminal values or hierarchical plans can help, while introducing their own assumptions.

Connect [[VILP - 2502.01784]] to video-based planning and [[Multimodal Sim-to-Real Audio - 2507.02864]] to richer simulation. Deepen optimization using the [MIT manipulation text](https://manipulation.csail.mit.edu/).

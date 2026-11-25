---
type: reference
tags: [robot-learning, equations]
---
# Equation reference

[[Home]] | [[Notation and Glossary]]

This is a retrieval aid. Use the linked chapter for derivations, notation, and assumptions.

| Idea | Equation | Conditions and chapter |
|---|---|---|
| Gradient step | $\theta^+=\theta-\eta\nabla L$ | Differentiable loss; step size matters. [[01 Math for Learning]] |
| Bayes update | $p(s\mid o)\propto p(o\mid s)p(s)$ | Normalize over possible states. [[04 Perception and State]] |
| Rigid transform | $p_A=R_{AB}p_B+t_{AB}$ | Compatible frames; proper rotation. [[02 Geometry and Kinematics]] |
| Jacobian | $\dot x=J(q)\dot q$ | Local velocity relationship. [[02 Geometry and Kinematics]] |
| PD control | $\tau=K_p(q^\star-q)-K_d\dot q$ | Stationary target in this form. [[03 Dynamics and Feedback]] |
| Behavior cloning | $L=-\mathbb E_{\mathcal D}\log\pi_\theta(a\mid o)$ | Expert dataset; deployment shift remains. [[06 Imitation and Distribution Shift]] |
| Discounted return | $G_t=\sum_{k=0}^{T-t-1}\gamma^k r_{t+k}$ | Finite horizon shown. [[09 Reinforcement Learning]] |
| Bellman expectation | $Q^\pi=\mathbb E[r+\gamma Q^\pi(s',a')]$ | $a'$ sampled from $\pi$; terminal handling required. [[09 Reinforcement Learning]] |
| Friction bound | $\|f_t\|\le\mu f_n$ | Ideal sticking contact model. [[14 Contact and Dexterity]] |
| Brier score | $\frac1N\sum_i(p_i-y_i)^2$ | Binary outcomes and probabilities. [[16 Evaluation and Uncertainty]] |

## Generative-policy equations

Diffusion noise construction:

$$A_k=\sqrt{\bar\alpha_k}A_0+\sqrt{1-\bar\alpha_k}\epsilon.$$

Straight-path conditional flow matching:

$$x_\tau=(1-\tau)z+\tau A,\qquad v^\star=A-z.$$

Both use artificial generation time, not physical action time. See [[08 Diffusion and Flow Matching]].

## A check before using any equation

State the variables, units, assumptions, observable quantities, and failure cases. An equation can be mathematically correct but inappropriate for the hardware or data you have.

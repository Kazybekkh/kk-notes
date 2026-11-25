---
type: chapter
chapter: 8
status: not-started
tags: [robot-learning, generative-models]
---
# 08 Diffusion and flow matching

[[Home]] | Previous: [[07 ACT and Action Sequences]] | Next: [[09 Reinforcement Learning]]

When two action sequences are both valid, their average need not be valid. A robot can go around an obstacle on the left or right, but averaging those trajectories can hit it. Generative policies learn a distribution over candidate actions.

![[action_modes.png]]

*Toy mixture of two Gaussian action modes. The conditional mean falls between them.*

## Denoising intuition

Let $A_0$ be a demonstrated action chunk and $\epsilon\sim\mathcal N(0,I)$. A common diffusion training construction adds noise:

$$
A_k=\sqrt{\bar\alpha_k}A_0+\sqrt{1-\bar\alpha_k}\epsilon,
\qquad
L=\mathbb E\|\epsilon-\epsilon_\theta(A_k,k,o)\|_2^2.
$$

$k$ is a noise level, not robot time; $\bar\alpha_k$ controls retained signal. The model learns to predict noise conditioned on observation $o$. A chosen reverse sampler then generates actions through multiple denoising steps. Different parameterizations and schedulers give different implementations.

The [Diffusion Policy paper](https://arxiv.org/abs/2303.04137) brings diffusion-based action generation into visuomotor control with repeated replanning. Link it to [[Diffusion Policy - 2303.04137]] and [[UMI - 2402.10329]].

## Flow matching intuition

A simple conditional flow-matching teaching construction pairs noise $z$ with a data action $A$ and interpolates:

$$
x_\tau=(1-\tau)z+\tau A,\quad
L_{\rm FM}=\mathbb E\|v_\theta(x_\tau,\tau,o)-(A-z)\|_2^2.
$$

The learned velocity field moves a sample according to

$$
\frac{dx_\tau}{d\tau}=v_\theta(x_\tau,\tau,o),\qquad x_0\sim\mathcal N(0,I).
$$

$\tau\in[0,1]$ is generation time, separate from the physical controller's time. The endpoint at $\tau=1$ is the generated action. This straight-path formulation is an instructional example; a particular model may use different paths, weighting, or parameterizations. The original [Flow Matching paper](https://arxiv.org/abs/2210.02747) develops the general framework.

![[flow_paths.png]]

*Synthetic paired paths show the training construction, not the learned trajectories of pi0.*

![[ch08_flow_two_modes.mp4]]

*Demonstrations pass an obstacle on the left ($-1$) or right ($+1$). Samples follow the exact velocity field that minimises $L_{\rm FM}$ for this data, standing in for a perfectly trained model. With 32 Euler steps they split into the two modes and 0.07% of 20,000 samples hit the obstacle. Regression predicts the mean, 0, which hits it. Fewer steps drift toward that mean: one step lands every sample at 0, two steps send 33% into the obstacle, four steps 4.6%. Source: `Tools/animations/ch08_flow_two_modes.py`.*

## What matters on your robot

More sampling steps can improve generation but increase latency. A model that represents multiple action modes can still choose the wrong one under perceptual ambiguity. Evaluate controller timing, action bounds, and closed-loop success rather than judging generated trajectories by appearance alone.

**Exercise:** why should an experiment compare methods under both fixed training data and measured inference cost?

> [!success]- Answer
> Otherwise better results may come from more demonstrations or extra compute. A practical comparison must show what the robot gains per resource budget.

Next connect to [[13 Vision Language Action Models]].

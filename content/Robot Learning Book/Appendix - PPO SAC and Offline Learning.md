---
type: appendix
status: not-started
tags: [robot-learning, reinforcement-learning, algorithms]
---
# PPO, SAC, and offline learning

[[Home]] | [[09 Reinforcement Learning]] | [[10 Offline RL and Data Coverage]]

This appendix explains recognizable objectives so you can read implementations. Use a tested implementation for experiments and confirm its exact conventions.

## PPO: discourage overly large changes

Let

$$
r_t(\theta)=\frac{\pi_\theta(a_t\mid s_t)}
{\pi_{\theta_{\rm old}}(a_t\mid s_t)}.
$$

PPO's clipped surrogate is

$$
L^{\rm clip}(\theta)=
\mathbb E_t\left[
\min\left(r_t(\theta)\hat A_t,
\operatorname{clip}(r_t(\theta),1-\epsilon,1+\epsilon)\hat A_t\right)
\right].
$$

The objective is maximized. $\hat A_t$ estimates whether the sampled action was better than expected. Clipping limits the incentive to increase or decrease a sampled action's probability excessively. It is not an absolute guarantee of a bounded policy change. Implementations often add value and entropy terms. [Original PPO paper](https://arxiv.org/abs/1707.06347).

## SAC: reward and entropy

A maximum-entropy objective rewards task performance while encouraging a stochastic policy:

$$
J=\mathbb E\sum_t\gamma^t
\left[r_t+\alpha\mathcal H(\pi(\cdot\mid s_t))\right].
$$

$\alpha$ controls the entropy contribution. For a continuous action space this uses differential entropy, which depends on the action parameterization.

A common modern twin-critic SAC target is

$$
y=r+\gamma(1-d)
\left[
\min_{i=1,2}Q_{\bar\theta_i}(s',a')
-\alpha\log\pi_\phi(a'\mid s')
\right],
\qquad a'\sim\pi_\phi(\cdot\mid s').
$$

Critics regress toward $y$; the actor seeks actions with high estimated value and entropy. The minimum reduces one source of optimistic bias but does not guarantee accurate values. This is a commonly used later formulation; the [original SAC paper](https://arxiv.org/abs/1801.01290) and [SAC algorithms and applications](https://arxiv.org/abs/1812.05905) provide the development.

## Why replay is not enough for offline RL

A replay buffer permits reuse of previous interactions. In online training, new experience can sometimes correct bad estimates. With a fixed dataset, unsupported actions may remain untested indefinitely. Offline algorithms therefore change objectives or policy updates to handle coverage limitations.

Your practical decision is not “Which acronym is strongest?” Ask whether new interaction is available, whether rewards are meaningful, what actions the data covers, and whether the evaluation can reveal distribution shift.

**Exercise:** an environment ends because a data-collection timer expires, but the task state is not terminal. Should you always zero the value bootstrap?

> [!success]- Answer
> No. A time-limit truncation and a true terminal state have different semantics. Handle them according to the task's return definition and framework conventions.

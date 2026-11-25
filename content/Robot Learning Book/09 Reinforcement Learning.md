---
type: chapter
chapter: 9
status: not-started
tags: [robot-learning, reinforcement-learning]
---
# 09 Reinforcement learning

[[Home]] | Previous: [[08 Diffusion and Flow Matching]] | Next: [[10 Offline RL and Data Coverage]]

Reinforcement learning improves decisions using consequences. An agent takes an action, the environment changes, and a reward provides feedback. Unlike imitation, it need not have an expert action for every training example.

## The Markov decision process

An MDP contains states $\mathcal S$, actions $\mathcal A$, transition law $P$, reward $r$, and discount $\gamma$. Markov means the current state contains enough information to predict the next-state distribution given an action.

$$
J(\pi)=\mathbb E_\pi\left[\sum_{t=0}^{T-1}\gamma^t r_t\right].
$$

$\gamma$ weights future reward; it does not fix a badly specified reward. A robot rewarded only for approaching an object may learn never to grasp it.

The value $V^\pi(s)$ is expected return starting at state $s$. The action-value $Q^\pi(s,a)$ fixes the first action before following $\pi$. Their Bellman relationship is

$$
Q^\pi(s,a)=
\mathbb E_{s'}\left[r(s,a,s')+\gamma
\mathbb E_{a'\sim\pi(\cdot\mid s')}Q^\pi(s',a')\right].
$$

This decomposes a long prediction into immediate reward plus a future estimate. The [Spinning Up introduction](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html) is a primary teaching reference for the notation.

![[ch09_value_iteration.mp4]]

*Value iteration on one grid with two discounts. Each sweep applies the Bellman update to every cell, so value spreads one cell per sweep. From the start, the +1 is 2 moves away and the +10 is 10. At $\gamma=0.5$ the +10 is worth $0.5^9\cdot 10\approx0.02$, so the agent takes the +1 ($V=0.50$); at $\gamma=0.95$ it is worth $0.95^9\cdot10\approx6.30$, so the agent goes the long way. Source: `Tools/animations/ch09_value_iteration.py`.*

## Actor, critic, and policy gradient

The actor chooses actions; the critic estimates their usefulness. A common policy-gradient form is

$$
\nabla_\theta J=
\mathbb E\left[\nabla_\theta\log\pi_\theta(a\mid s)
A^\pi(s,a)\right],
$$

with the expectation using the appropriate discounted visitation weighting. The advantage $A^\pi=Q^\pi-V^\pi$ compares an action with the policy's usual performance at that state. Subtracting a state-only baseline can reduce estimator variance without changing its expectation.

~~~mermaid
flowchart LR
  Policy["Actor chooses action"] --> Env["Environment"]
  Env --> Data["State, reward, next state"]
  Data --> Critic["Critic estimates return"]
  Critic --> Policy
~~~

[PPO](https://arxiv.org/abs/1707.06347) limits the effect of large policy updates through a clipped objective. [SAC](https://arxiv.org/abs/1801.01290) learns from replay data and includes an entropy incentive. Neither acronym alone tells you which method fits your task.

## Exercise

A transition gives reward 1 and leads to a state valued at 5 with $\gamma=0.9$. Compute the one-step target.

> [!success]- Answer
> $1+0.9(5)=5.5$. A true terminal transition has no future return, so its target would be 1.

Learn first in a small simulator with a proven implementation. Compare learning across multiple random seeds and inspect reward exploitation. Your physical SO-101 should begin with supervised demonstrations and established controllers, not unrestricted trial-and-error exploration.

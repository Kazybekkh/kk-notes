---
type: chapter
chapter: 10
status: not-started
tags: [robot-learning, reinforcement-learning, datasets]
---
# 10 Offline RL and data coverage

[[Home]] | Previous: [[09 Reinforcement Learning]] | Next: [[11 World Models and Planning]]

Offline reinforcement learning uses a fixed dataset of transitions. This is attractive when robot interaction is costly: reuse logged experience instead of collecting every trial anew. The central difficulty is estimating the value of actions that the dataset barely contains.

## Why maximization can amplify error

A simple Q-learning target is

$$
y=r+\gamma(1-d)\max_{a'}Q_{\bar\theta}(s',a'),
$$

where $d=1$ indicates a true terminal state and $\bar\theta$ denotes target parameters. The maximization may select an unsupported action with an accidentally high predicted value. Training then propagates that error.

![[data_coverage.png]]

*Synthetic action values: a fitted estimate can look optimistic outside the region covered by data.*

![[ch10_offline_overestimation.mp4]]

*One state, logged actions only in $[-1,1]$. A degree-4 fit agrees with the data, but its maximum is at $a=3$, predicting 21.8 where the true reward is $-1.88$. Maximising an ensemble's mean minus two standard deviations, a simple pessimistic estimate, picks $a=0.84$ (true reward 0.97). Bootstrapping with $\gamma=0.9$ multiplies the error in the max by $1/(1-\gamma)=10$. Across 200 random datasets the greedy pick left the data 52% of the time. Source: `Tools/animations/ch10_offline_overestimation.py`.*

Offline methods address this through ideas such as pessimistic value estimates, restricting how far the policy departs from the data, or learning advantage-weighted imitation. The appropriate constraint depends on whether the dataset includes diverse successful behavior, recoveries, or mainly failures.

## Coverage is a physical question

Ask which states and actions your dataset contains. A hundred successful demonstrations from one initial pose may cover less useful variation than a smaller set spanning different poses and recoveries. More frames do not necessarily mean more independent experience.

If a dataset has only expert actions and no usable rewards, behavior cloning may be the clearer starting point. Offline RL needs a defensible reward or outcome signal and sufficient transition information. Reconstructing a reward after collection can introduce label noise.

## Practical distinctions

**Offline RL** improves reward using fixed logged transitions. **Off-policy online RL** learns from a replay buffer but can still collect new experience. **Offline evaluation** estimates deployment performance from logs; it is a separate problem and can be unreliable when the candidate policy differs greatly from the logging policy.

**Exercise:** your data contains only slow movements near the center of the workspace. A learned Q-function predicts very high return for fast movements at the edge. Is that evidence the fast policy works?

> [!success]- Answer
> No. Those predictions extrapolate outside coverage. You need either evidence in that region or an algorithm and evaluation protocol that explicitly address the uncertainty.

Connection: [[06 Imitation and Distribution Shift]] explains the related distribution mismatch for imitation. For deeper primary reading, see [Conservative Q-Learning](https://arxiv.org/abs/2006.04779) and [Implicit Q-Learning](https://arxiv.org/abs/2110.06169); these are further-reading links, not claims of implementation or replication here.

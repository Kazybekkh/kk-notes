---
type: chapter
chapter: 6
status: not-started
tags: [robot-learning, imitation-learning]
---
# 06 Imitation and distribution shift

[[Home]] | Previous: [[05 Training Neural Policies]] | Next: [[07 ACT and Action Sequences]]

Behavior cloning learns actions from demonstrations. The trap is that a robot's mistakes change which states it sees next. Demonstrations of successful grasps may never show the gripper slightly missing the object, so the policy may have no idea how to recover.

## The distribution you train on is not the one you create

Let $d_E(s)$ be the expert's state distribution and $d_\pi(s)$ the learner's. Behavior cloning minimizes error under $d_E$, but deployment runs under $d_\pi$. These distributions coincide only under restrictive conditions.

In a deliberately simplified model, suppose each of $T$ steps independently avoids an unrecoverable error with probability $1-\epsilon$. Then

$$
P(\text{no error over }T\text{ steps})=(1-\epsilon)^T.
$$

This explains why apparently small step errors can hurt long tasks. It is not a theorem for general robotic behavior: errors are often correlated, and recovery can be possible.

![[compounding_error.png]]

*Independent-error illustration, not an empirical success curve.*

## Improving the data distribution

The [DAgger paper](https://arxiv.org/abs/1011.0686) motivates repeatedly collecting expert labels on states visited by the learner and aggregating them into the dataset. Its theoretical guarantees rely on assumptions; applying the idea to hardware requires a practical expert and controlled execution.

![[ch06_compounding_dagger.mp4]]

*A toy lane-keeping task. The expert keeps the lateral error small, so its demonstrations barely show how to correct one, and a linear policy fitted with weight decay learns almost no correction (gain $-0.09$ against the expert's $-0.8$). Over 500 runs, its share still in the lane falls from 94% after 50 steps to 60% after 300. One DAgger round, with the expert labelling 142 off-centre states the learner reached, raises the gain to $-0.36$ and keeps every run in the lane. Noise and weight decay were chosen to make the effect visible. Source: `Tools/animations/ch06_compounding_dagger.py`.*

~~~mermaid
flowchart LR
  Demo["Expert data"] --> Train["Train learner"]
  Train --> Roll["Observe learner states"]
  Roll --> Label["Expert labels or corrections"]
  Label --> Merge["Aggregate data"]
  Merge --> Train
~~~

Corrections are not automatically better data. If a human intervenes only during the worst states, that subset has a different distribution from normal operation. Record when intervention happened and evaluate whether the resulting policy improves independent test rollouts.

## Your SO-101 interpretation

Start with one simple task, consistent resets, and a fixed camera. Collect examples of reasonable object variation and recovery from small, safe perturbations. Measure whether extra *diversity* helps more than more near-duplicate demonstrations.

An action policy can also be ambiguous because demonstrations encode several strategies. Better data collection, conditioning, and stochastic output models solve different parts of this problem.

**Exercise:** with $\epsilon=0.01$, compare the illustrative no-error probability for $T=10$ and $T=100$.

> [!success]- Answer
> About 0.904 and 0.366. The assumptions are independence, fixed error probability, and no recovery. Explain why each is unrealistic before treating the numbers as a prediction.

Paper bridges: [[ACT and ALOHA - 2304.13705]], [[EgoMimic - 2410.24221]]. Research connection: [[Recovery Data versus More Demonstrations]].

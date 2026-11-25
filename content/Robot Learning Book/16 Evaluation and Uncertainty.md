---
type: chapter
chapter: 16
status: not-started
tags: [robot-learning, evaluation, statistics]
---
# 16 Evaluation and uncertainty

[[Home]] | Previous: [[15 Robot Systems and Deployment]] | Next: [[17 Finding a Research Question]]

A research result needs a defined test distribution, a success rule, repeated trials, and honest uncertainty. A polished video can show possibility; it cannot establish a success rate.

## Success rates need denominators

With $k$ successes in $n$ independent Bernoulli trials, $\hat p=k/n$. A Wilson interval is often more useful than a naive normal interval near 0 or 1:

$$
\frac{\hat p+z^2/(2n)\ \pm\
z\sqrt{\hat p(1-\hat p)/n+z^2/(4n^2)}}
{1+z^2/n}.
$$

$z\approx1.96$ gives an approximate 95% interval under the model. Correlated trials, changing reset conditions, and repeated tuning on test cases weaken its interpretation.

![[success_intervals.png]]

*Illustrative 80% success estimates with different trial counts; intervals narrow with more independent evidence.*

## Design the split around the claim

Separate training, validation for model choices, and final test trials. Hold out whole sessions or objects when those are the claimed novelty. Record failures and interventions, including runs interrupted for system problems, with a predefined handling rule.

Compare paired conditions where possible: the same object placements and reset schedule for baseline and intervention, with randomized evaluation order. Multiple training seeds reveal optimization variability; multiple physical trials reveal rollout variability. They are not interchangeable sample counts.

## Calibration

If a model labels many decisions as 80% likely correct, about 80% should be correct in that group on the evaluated distribution. For binary predictions:

$$
\operatorname{Brier}=\frac1N\sum_i(p_i-y_i)^2,\qquad
\operatorname{NLL}=-\frac1N\sum_i[y_i\log p_i+(1-y_i)\log(1-p_i)].
$$

$y_i\in\{0,1\}$ is a ground-truth label. These proper scoring rules assess probabilistic quality. A reliability diagram compares confidence with empirical frequency; bins with few observations have substantial uncertainty.

![[calibration.png]]

*Synthetic reliability curves illustrate perfect calibration and overconfidence.*

## Abstaining is also a decision

A confidence threshold can trade coverage for error rate. Measure the risk among accepted cases and the fraction of cases accepted. Do not choose the threshold on the final test set.

![[risk_coverage.png]]

*Toy curves illustrate possible tradeoffs, not Jev or robot measurements.*

**Exercise:** two methods score 16/20 and 17/20. Is the second demonstrably better?

> [!success]- Answer
> Not from those counts alone. Specify the test design, variability, and uncertainty. Small differences with few trials should not be presented as decisive.

Connect to [[Lab 04 Calibration]], [[Jev for Robot Skill Selection]], and your existing [[Uncertainty and Explainability]].

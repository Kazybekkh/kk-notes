---
type: chapter
chapter: 5
status: not-started
tags: [robot-learning, deep-learning]
---
# 05 Training neural policies

[[Home]] | Previous: [[04 Perception and State]] | Next: [[06 Imitation and Distribution Shift]]

A neural policy is a parameterized function. Training finds parameters that reduce an objective on a dataset. Deployment tests whether that function remains useful when its outputs change the world.

## The simplest training objective

For demonstrations $\mathcal D=\{(o_i,a_i)\}_{i=1}^N$ and deterministic policy $f_\theta$,

$$
L(\theta)=\frac1N\sum_{i=1}^N\|f_\theta(o_i)-a_i\|_2^2.
$$

$o_i$ can contain an image, joint positions, and task information. Normalize each action coordinate using statistics from the training split only. Undo that normalization before physical deployment. Mixing meters, radians, and gripper units without care lets the largest numerical scale dominate the loss.

A probabilistic alternative minimizes negative log likelihood:

$$
L_{\rm NLL}=-\frac1N\sum_i\log\pi_\theta(a_i\mid o_i).
$$

For a Gaussian with fixed variance, this is closely related to squared error. A richer action distribution can represent ambiguity that a single mean cannot.

## The data split is part of the experiment

Adjacent video frames are almost duplicates. Randomly splitting frames can place nearly identical scenes in training and validation, creating misleading confidence. Split whole episodes, sessions, objects, or environments according to the generalization claim you intend to make.

![[learning_curves.png]]

*Synthetic curves illustrating overfitting; they are not measurements from a trained robot.*

Training loss answers whether the model fits supplied targets. Held-out loss answers how it predicts under a particular data split. Closed-loop task success answers something different: whether its actions lead to useful future observations.

## Debug in increasing complexity

First verify shapes, action units, image transformations, and chronological order. Try to overfit a tiny dataset to expose implementation errors. Then train a small baseline, inspect predictions visually, and only then enlarge the model. Record seeds and environment versions, but recognize that GPU and simulator nondeterminism can remain.

Connect this with [[Supervised Learning]], [[Evaluating ML Models]], and [[Transfer Learning and Pre-trained CNNs]] in your existing course notes.

**Exercise:** two demonstrations require steering left or right around an obstacle with equal frequency. What might a squared-error deterministic predictor do?

> [!success]- Answer
> It can predict their average, which may aim into the obstacle. A model that represents several valid action modes can avoid that particular averaging problem, although it still needs suitable observations and training data.

Deliverable: a diagram of the model's inputs and outputs, a dataset split manifest, and a script that overfits five episodes. Continue to [[Lab 02 Policy Baseline]].

---
type: chapter
chapter: 7
status: not-started
tags: [robot-learning, imitation-learning, sequence-models]
---
# 07 ACT and action sequences

[[Home]] | Previous: [[06 Imitation and Distribution Shift]] | Next: [[08 Diffusion and Flow Matching]]

Predicting a short action sequence can encode coordinated behavior better than independently predicting every motor command. Define an action chunk

$$
A_t=[a_t,a_{t+1},\ldots,a_{t+H-1}],
$$

where $H$ is the prediction horizon. The controller may execute only $h\le H$ actions before observing and replanning. Prediction horizon and execution horizon are different design choices.

## Why sequence modeling changes the problem

A longer chunk can provide coherent movement through a grasp. Executing more of it without observation also makes the robot slower to react to disturbances. Overlapping predictions can be combined, but averaging disagreeing strategies may create a poor intermediate action.

![[action_chunks.png]]

*Illustrative scheduling: eight actions predicted, two executed before replanning.*

![[ch07_chunking_latency.mp4]]

*A robot tracking a moving object at 20 Hz with 16-step chunks; each chunk carries its own small prediction error. The object is bumped at 0.85 s. Executing 2 actions per chunk reacts in 50 ms but switches plans 29 times in 3 s; executing all 16 switches only 3 times but keeps running the stale plan for 750 ms. Each switch jumps by about 0.06 whatever the horizon, so the horizon decides how often the robot looks again, not how good each plan is. Source: `Tools/animations/ch07_chunking_latency.py`.*

The original [ACT/ALOHA paper](https://arxiv.org/abs/2304.13705) combines affordable teleoperation with action-sequence imitation. Read [[ACT and ALOHA - 2304.13705]] for the paper entry. To understand latent action models more generally, consider a conditional variational autoencoder objective:

$$
L=\mathbb E_{z\sim q_\phi(z\mid A,o)}
[-\log p_\theta(A\mid o,z)]
+\beta D_{\rm KL}\!\left(q_\phi(z\mid A,o)\,\|\,p(z)\right).
$$

$z$ is a latent variable for variations not fully explained by observation $o$. The encoder $q_\phi$ sees the demonstrated sequence during training; the decoder predicts it. The KL term encourages a latent distribution compatible with the chosen prior. This is a generic conditional latent-model objective; consult the implementation for its exact reconstruction loss and inference convention.

## A deployment calculation

At 20 Hz, each action step lasts 50 ms. A 16-step chunk spans 0.8 seconds; executing four steps before replanning leaves about 0.2 seconds of open-loop execution, before additional compute and communication delays. A model with excellent prediction accuracy can still fail if it reacts too slowly.

## Experiment

Hold the dataset, model size, training budget, and reset distribution fixed. Vary the execution horizon while recording success, intervention count, action discontinuity, and observation-to-action latency. Do not change the horizon and collection policy simultaneously if you want to attribute the result.

**Exercise:** a policy predicts 12 actions at 30 Hz and executes three. What are its prediction and execution durations?

> [!success]- Answer
> Approximately 0.4 seconds and 0.1 seconds. Wall-clock inference may add delay, so measure the actual system.

Connect this chapter to [[15 Robot Systems and Deployment]] and [[Latency and Chunking Study]].

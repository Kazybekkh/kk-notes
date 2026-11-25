---
type: chapter
chapter: 13
status: not-started
tags: [robot-learning, vla, foundation-models]
---
# 13 Vision language action models

[[Home]] | Previous: [[12 Human Data and Embodiment]] | Next: [[14 Contact and Dexterity]]

A vision-language-action model conditions robot behavior on images, language, and sometimes robot state or history. It can combine broad semantic knowledge with data that grounds words and images in physical actions.

## Factor the system before comparing models

A generic policy is

$$
\pi_\theta(A_t\mid I_{t-k:t},q_{t-k:t},\ell),
$$

where $I$ is image history, $q$ is proprioception, $\ell$ is an instruction, and $A_t$ is an action chunk. A visual-language backbone encodes context; an action head or expert produces executable outputs. Actions may be discrete tokens, continuous vectors, or samples from a generative model.

~~~mermaid
flowchart LR
  Image["Images"] --> Backbone["Vision-language context"]
  Language["Instruction"] --> Backbone
  State["Robot state"] --> Action["Action model"]
  Backbone --> Action
  Action --> Controller["Embodiment-specific controller"]
~~~

This is a conceptual decomposition, not a specification of every VLA architecture. [[pi0 - 2410.24164]] introduces a flow-based action model built on a pretrained vision-language model. The [original pi0 paper](https://arxiv.org/abs/2410.24164) is the primary source for its architecture and experiments.

## What pretraining can and cannot supply

Internet data can help recognize objects and interpret instructions. It does not automatically supply calibrated robot poses, contact forces, or suitable motor commands. Robot datasets provide this physical grounding, but different datasets may use incompatible action conventions and contain inconsistent instructions.

Fine-tuning adapts a pretrained model to a narrower task or robot. Parameter-efficient adaptation can reduce trainable weights, but does not eliminate data quality, evaluation, or deployment requirements. Benchmark “generalization” must specify whether the novelty is an object, arrangement, instruction, task, or embodiment.

## A research engineer's questions

Before comparing two VLAs, write down their pretraining data access, adaptation budget, input cameras, action frequency, action units, and evaluation tasks. Otherwise an architecture comparison may actually compare dataset scale.

A realistic student contribution can study data selection, robustness, adaptation, or failure recovery with an existing model. Training a frontier model from scratch is not a prerequisite for meaningful work.

**Exercise:** a model follows “pick up the red cup” on an unseen cup, but only in its training room. Which generalization claim is supported?

> [!success]- Answer
> Potentially object-instance generalization under that setup. It does not establish new-room, new-task, or cross-embodiment transfer.

[[Jev - TypeSafe AI]] belongs in a related decision-layer discussion: structured skill selection is distinct from generating continuous robot actions.

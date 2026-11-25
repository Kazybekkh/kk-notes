# Inference-Time Attention Steering for VLA Driving Models

**Paper:** [arXiv abstract](https://arxiv.org/abs/2608.17095) | [PDF](https://arxiv.org/pdf/2608.17095)  
**Start with:** [[Robot Learning Primer]] | **Related:** [[pi0 - 2410.24164]]

## In plain English

This paper studies whether a vision-language-action model for driving can be steered toward important traffic actors at inference time. It changes attention scores on selected image tokens without retraining the model and observes how planned trajectories move in a set of lane-change scenarios.

## Scope warning

Its domain is driving, not robot-arm manipulation. The abstract reports controlled shifts in predicted trajectories, but a shifted trajectory is not by itself proof of safer driving. This paper is useful for learning how model attention can affect actions and how to audit such interventions.

## Terms to know

**Attention** is a model mechanism that weights information from different input tokens. **Visual token** is a model representation of part of an image. **Inference-time intervention** changes computation when using a trained model, without updating its learned weights.

## What to inspect in the PDF

Look for the zero-bias control, actor detection accuracy, safety metric, and failure modes. Treat it as an adjacent methodological example, not a direct SO-101 project recipe.

---
type: research-idea
status: proposed
novelty: unverified
tags: [robot-learning, research-idea, systems]
---
# Latency and chunking study

[[Research Dashboard]] | [[07 ACT and Action Sequences]] | [[15 Robot Systems and Deployment]]

## Hypothesis

Policy robustness depends on the interaction between observation-to-action delay and the duration executed before replanning. A shorter execution horizon may help only until inference and communication delays dominate.

## Factorial experiment

Choose a single trained policy and evaluate several added delays crossed with several execution horizons. Added delay is an experimental intervention on the timing path, not a change to training. Log actual observed delay rather than assuming the requested delay was achieved.

Use identical held-out reset conditions and randomize evaluation order. Keep task speed and controller limits fixed. Measure completion, interventions, time, and action discontinuity. A heatmap can show the interaction between delay and horizon.

## Important distinctions

Prediction horizon is the length of the model's output. Execution horizon is how much is used before replanning. Sensor latency, compute latency, and communication latency can have different effects if the system buffers or re-times actions.

## Feasibility and research value

This study can begin in recorded-data timing tests and simulation, then move to supervised low-speed hardware. Its novelty is unverified; first read prior work on asynchronous inference, real-time action chunking, latency compensation, and UMI deployment interfaces.

A useful outcome is a measured operating envelope for your system, even if the central hypothesis is not supported. Do not generalize from one task and arm to all robot policies.

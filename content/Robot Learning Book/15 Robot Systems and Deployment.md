---
type: chapter
chapter: 15
status: not-started
tags: [robot-learning, systems, deployment]
---
# 15 Robot systems and deployment

[[Home]] | Previous: [[14 Contact and Dexterity]] | Next: [[16 Evaluation and Uncertainty]]

Robot learning is a systems discipline. A policy depends on calibrated sensors, synchronized data, consistent units, available compute, and a controller that executes the intended action.

## Trace a single action

~~~mermaid
sequenceDiagram
  participant Cam as Camera
  participant P as Policy
  participant C as Controller
  participant R as Robot
  Cam->>P: Image with capture timestamp
  P->>P: Preprocess and infer
  P->>C: Bounded action and intended time
  C->>R: Execute command
  R->>P: Timestamped joint state
~~~

Measure end-to-end delay from image capture to physical command application. Timing only the neural network misses camera buffering, preprocessing, transfer, queuing, and motor communication.

$$
t_{\rm total}=t_{\rm capture}+t_{\rm preprocess}+t_{\rm inference}
+t_{\rm queue}+t_{\rm transport}+t_{\rm actuation}.
$$

This is an accounting model for sequential stages; overlapped pipelines require tracing timestamps rather than blindly summing timings. Report median and tail latency, such as the 95th percentile, because rare long delays can disrupt control.

![[latency_budget.png]]

*Invented example budget for teaching only. Measure your own hardware.*

## The deployment contract

Record which camera corresponds to each model input, image color order and resolution, joint names and ordering, action meaning, normalization statistics, timestep, and model checkpoint. A checkpoint without this contract may be impossible to reproduce.

Your existing [[lerobot]] note lists serial devices, but device names can change after reconnecting. Verify identity before commanding motors. Establish motion bounds, low-speed checks, an accessible stop, and supervision before policy rollouts. These are part of running an experiment, not replacements for the robot's hardware procedures.

## Resource-aware experiments

Use an existing framework for the core control and learning workflow. The official [LeRobot documentation](https://huggingface.co/docs/lerobot/index) describes integrated hardware, dataset, and policy tools; consult its [real-world imitation guide](https://huggingface.co/docs/lerobot/il_robots) for version-specific commands.

**Exercise:** your network takes 20 ms but observed end-to-end latency is 120 ms. Should you immediately use a smaller network?

> [!success]- Answer
> Profile the remaining stages first. Reducing inference to 10 ms saves only 10 ms if buffering or queuing dominates.

Portfolio deliverable: a reproducible setup guide and timing trace. Research connection: [[Latency and Chunking Study]].

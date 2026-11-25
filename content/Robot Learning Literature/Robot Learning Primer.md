# Robot learning primer

Return to [[Start Here]]. This page defines the words you need to understand the paper notes. You do not need to know control theory before starting.

## What is being learned?

A **robot policy** is a rule that takes an observation (for example camera images and joint positions) and chooses an action (for example a target gripper pose or joint command). A **trajectory** is a time-ordered sequence of observations and actions. A **demonstration** is a trajectory produced by a human or an existing controller. The robot's **embodiment** is its physical body: arm length, joints, gripper, sensors, and motion limits.

The basic learning problem is: given many demonstrations, can a policy act successfully in a new situation? Success needs both the right task choice and actions the actual robot can execute. A policy that works on saved data can still fail on the real robot when a tiny mistake changes the next camera image.

## Common learning approaches

**Imitation learning** trains from demonstrations. **Behavior cloning** is the simplest version: fit a model that predicts the demonstrator's action from the observation. It does not directly learn from its own mistakes. **Reinforcement learning** instead improves a policy using trial-and-error feedback from a reward; collecting those trials on real hardware can be expensive or unsafe.

An **action chunk** is a short sequence of future actions predicted together. The controller usually executes only part of it, observes again, and replans. This is **receding-horizon control**. A **diffusion policy** generates an action sequence by gradually removing noise, allowing more than one plausible way to complete a task. A **vision-language-action (VLA)** model uses images and language instructions to produce robot actions. A large VLA model is not automatically practical on a small arm: latency, data, compute, and action format matter.

## Moving from humans to robots

**Teleoperation** means a human controls a robot during data collection. **Retargeting** maps human motion or one robot's motion to a different body. It is hard because human hands and robot grippers have different joints, reach, force, and contact behavior. **Cross-embodiment transfer** asks whether data collected with one body can improve a policy for another. **Egocentric video** is first-person video, often from a head-mounted camera. Video alone usually does not give accurate 3D actions or contact forces; a method must infer, track, or separately capture them.

**Inverse kinematics** converts a desired hand or tool pose into joint angles. It may have multiple answers or no feasible answer. An **end-effector** is the tool at the arm's end, such as a gripper. A **point cloud** is a set of 3D points representing visible surfaces. **SLAM** estimates a sensor's motion while building a map of its surroundings. **Sim-to-real** means training in simulation and deploying on physical hardware; differences in friction, lighting, sound, and latency can break transfer.

## Reading claims carefully

Look for the task definition, inputs, action representation, number and diversity of demonstrations, robot hardware, baselines, evaluation environments, success metric, and failure cases. **Zero-shot** often means deployment to a test condition without task-specific retraining; inspect exactly what was unseen. **Generalization** can mean a new object, scene, camera, task, or embodiment, which are very different challenges. An **ablation** removes one component to test whether it contributed to performance.

For a final-year project, start with a narrow measurable question and a baseline you can run on your available robot. An SO-101 project that compares two data representations on one reproducible task can be more informative than trying to rebuild a very large generalist model.

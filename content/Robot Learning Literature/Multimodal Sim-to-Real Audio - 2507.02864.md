# The Sound of Simulation: Multimodal Sim-to-Real Policies

**Paper:** [arXiv abstract](https://arxiv.org/abs/2507.02864) | [PDF](https://arxiv.org/pdf/2507.02864)  
**Start with:** [[Robot Learning Primer]] | **Related:** [[LeRobot - 2602.22818]], [[Diffusion Policy - 2303.04137]]

## In plain English

Camera images do not reveal everything about a manipulation task. Sound may help a robot tell whether liquid is pouring or a container is filling. Simulation can generate images, but realistic sound is harder. This paper's MultiGen framework adds generated audio to simulated trajectories so a policy can train with both vision and sound.

## What the abstract reports

The authors focus on pouring and report transfer from simulation to real-world containers and liquids without real-robot training data for that setup. The key question is whether generated audio improves control rather than merely making a simulation look more realistic.

## Terms to know

**Modality** is a type of input, such as image, audio, or touch. **Multimodal policy** combines two or more modalities. **Sim-to-real gap** is the mismatch between simulation and physical deployment.

## What to inspect in the PDF

Look for vision-only and audio-only ablations, microphone placement, background noise, synchronization, and what the robot's action policy actually receives. This could inspire a modest SO-101 experiment comparing vision-only and vision-plus-cheap-microphone pouring, with careful repeatability and spill safety.

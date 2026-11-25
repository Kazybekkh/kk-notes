# Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

**Paper:** [arXiv abstract](https://arxiv.org/abs/2303.04137) | [PDF](https://arxiv.org/pdf/2303.04137)  
**Start with:** [[Robot Learning Primer]] | **Related:** [[ACT and ALOHA - 2304.13705]], [[UMI - 2402.10329]], [[VILP - 2502.01784]]

## In plain English

When a robot sees a scene, there may be several good ways to act. A simple model trained to predict an average action can choose a poor compromise between them. Diffusion Policy treats an action sequence as something to *generate*: it starts with noise and repeatedly refines it while conditioned on what the robot sees.

## The mechanism

Training teaches the model how to remove noise from successful action sequences. At run time it samples a candidate sequence, executes only the near-term actions, observes again, and replans. This is receding-horizon control. The paper also studies visual conditioning and a time-series diffusion transformer. The abstract reports results on 12 tasks in four benchmarks, with an average improvement of 46.9% over its compared methods; that is a benchmark-specific result, not a universal gain.

## Terms to know

**Multimodal actions** means more than one plausible action for the same observation. **Conditional generation** means the generated action depends on images or robot state. **Inference latency** is the time spent computing the next action, which matters on hardware.

## What to inspect in the PDF

Compare its action horizon, observation history, number of denoising steps, hardware experiments, and compute cost with [[ACT and ALOHA - 2304.13705]]. On an SO-101, test whether any improvement justifies slower inference and a more complex training setup.

---
type: research-map
tags: [robot-learning, research]
---
# Research landscape

[[Home]] | [[Research Dashboard]]

| Direction | Core question | What you would need | Likely first obstacle | Paper links |
|---|---|---|---|---|
| Data-efficient imitation | Which demonstrations improve recovery? | One reliable task and controlled data collection | Distinguishing diversity from data volume | [[ACT and ALOHA - 2304.13705]], [[Diffusion Policy - 2303.04137]] |
| Embodiment transfer | Which action representation survives a body change? | Known geometry and at least two conditions | Feasibility and calibration mismatch | [[UMI - 2402.10329]], [[Cross-Embodiment Transfer - 2607.27549]] |
| Human video | What useful supervision can be recovered from video? | Video, tracking, alignment, robot evaluation | Missing action/contact labels | [[EgoMimic - 2410.24221]], [[DexCap - 2403.07788]] |
| Deployment timing | How do latency and chunk execution interact? | Timestamped pipeline and reproducible delays | Separating timing from model quality | [[Latency and Chunking Study]] |
| Uncertainty and supervision | When should the robot abstain? | Labeled decisions, errors, and shift conditions | Miscalibrated confidence | [[Jev for Robot Skill Selection]] |
| Multimodal learning | Does another sensor provide missing information? | Synchronized sensors and an informative task | Sensor leakage or synchronization error | [[Multimodal Sim-to-Real Audio - 2507.02864]] |

## A decision rule for your first project

Start where you can collect data, run a baseline, and evaluate independently within a few weeks. Your SO-101 access makes deployment timing and demonstration quality particularly concrete. This is a feasibility judgment based on the current setup, not a novelty or publication prediction.

Use a 1-5 score for feasibility, evaluation clarity, available supervision, personal interest, and potential research value. Write one sentence of evidence for every score. Scores without reasons are decoration.

## Literature comparison table

When reading a paper, add a row to a project-specific table:

| Paper and section | Task | Data needed | Action format | Robot | Train/test difference | Claimed limitation | Your evidence |
|---|---|---|---|---|---|---|---|
| To fill after full reading | | | | | | | |

Search for both the proposed idea and simpler methods addressing the same failure. A paper can be relevant even when it uses different terminology.

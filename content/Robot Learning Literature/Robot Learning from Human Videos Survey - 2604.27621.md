# Robot Learning from Human Videos: A Survey

**Paper:** [arXiv abstract](https://arxiv.org/abs/2604.27621) | [PDF](https://arxiv.org/pdf/2604.27621)  
**Start with:** [[Robot Learning Primer]] | **Related:** [[EgoMimic - 2410.24221]], [[EgoEngine - 2606.12604]], [[VILP - 2502.01784]]

## In plain English

This survey organizes methods that learn robot skills from human video. Human recordings are abundant, but video does not directly provide robot joint commands. The abstract groups approaches by the level at which transfer happens: task intent, visual observation, or action.

## A useful reading framework

**Task-level transfer** asks *what goal* the person achieved. **Observation-level transfer** tries to make a robot learn from what the human saw or how the scene changed. **Action-level transfer** tries to recover motions the robot can execute. These categories help distinguish papers that all say they learn from video but actually solve different problems.

## Terms to know

**Data foundation** means the datasets, labels, and representations that make training possible. **Action inference** estimates hidden motions from visible video. A **taxonomy** is a classification scheme, useful for locating a manageable final-year research question.

## What to inspect in the PDF

Use the survey tables to identify public datasets, baselines, evaluation tasks, and open problems. Check each cited method's original paper before treating survey statements as experimental evidence. Build a comparison table for approaches feasible with your available camera and SO-101.

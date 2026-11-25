# LeRobot: An Open-Source Library for End-to-End Robot Learning

**Paper:** [arXiv abstract](https://arxiv.org/abs/2602.22818) | [PDF](https://arxiv.org/pdf/2602.22818)  
**Start with:** [[Robot Learning Primer]] | **Related:** [[ACT and ALOHA - 2304.13705]], [[UMI - 2402.10329]], [[lerobot]]

## In plain English

LeRobot is an open-source software stack covering more than policy training. It aims to connect motor control, affordable robot hardware, teleoperation, data collection, dataset storage, training, and evaluation. This matters because a learning algorithm is only useful when the entire data-to-deployment loop works reliably.

## What to take from it

The abstract emphasizes accessible hardware and support for several policy families. For an SO-101 final-year project, LeRobot can provide a reproducible baseline: record demonstrations, train a standard policy, run it on the robot, and measure success before adding a research contribution. The paper is about infrastructure and integration, so compare its claims to the exact hardware and software version you will use.

## Terms to know

**Middleware** connects software to motors and sensors. A **dataset pipeline** defines how demonstrations are recorded, timed, stored, and loaded. **Reproducibility** means another person can repeat the experiment with the same task, data split, and metrics.

## What to inspect in the PDF

Look for supported robots, dataset formats, policy implementations, timing assumptions, and evaluation protocol. Keep a separate lab note for actual SO-101 ports and calibration; the local [[lerobot]] note already records device names.

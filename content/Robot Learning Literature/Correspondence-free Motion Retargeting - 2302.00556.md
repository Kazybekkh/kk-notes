# Correspondence-free Online Human Motion Retargeting

**Paper:** [arXiv abstract](https://arxiv.org/abs/2302.00556) | [PDF](https://arxiv.org/pdf/2302.00556)  
**Start with:** [[Robot Learning Primer]] | **Related:** [[Human-to-Robot Retargeting Objectives - 2506.09384]]

## In plain English

This paper transfers human motion from one captured subject to another target shape without manually matching body points or aligning timelines. It combines information about the skeleton's motion over time with the visible surface shape and runs online, one frame at a time.

## Scope warning

The abstract describes *animation of a target subject*, not learning robot control or respecting robot torque, balance, and contact constraints. It appeared in the collection because it uses the word "retargeting." Keep it as a contrast case: visual motion transfer is not the same as executable human-to-robot retargeting.

## Terms to know

**Correspondence** is a match between points or time steps in two sequences. **Surface deformation** changes a shape's visible geometry. **Online inference** processes new data incrementally as it arrives.

## What to inspect in the PDF

Check the target representations, training data, and evaluation metrics. Only connect it to a robotics project if you can specify the additional feasibility and control layers needed to make the animated motion physically executable.

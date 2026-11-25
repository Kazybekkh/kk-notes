---
type: reproducibility
tags: [robot-learning, figures]
---
# Figure reproduction

[[Home]] | [[Visual Atlas]]

All figures in this edition were generated from the mathematical examples or synthetic curves in the book. None represents measured performance of SO-101, Jev, a paper's model, or a completed learning experiment.

The source is Tools/build_assets.py in this folder. It uses NumPy, Matplotlib, and Pillow. Requirements are listed beside the script. It produces PNG images for Obsidian, SVG versions for export, an inspection contact sheet, and the generated Book Map Canvas. Rerunning it replaces those generated assets; edit the script to preserve intended layout changes.

The existing paper-mining Python environment has the required packages installed. From a terminal:

~~~bash
/home/cal/paper-mining/.venv/bin/python \
  "/home/cal/Documents/My-Vault/Robot Learning Book/Tools/build_assets.py"
~~~

Animated scenes have their own pipeline; see [[Animations]].

Random illustrative flow paths use a fixed seed. Analytic figures include exact planar kinematics, second-order step responses, a scalar Bayesian update, and Wilson intervals. Other curves explicitly illustrate concepts and are not fitted to experimental data.

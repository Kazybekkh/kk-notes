# Dexterous Manipulation through Imitation Learning: A Survey

**Paper:** [arXiv abstract](https://arxiv.org/abs/2504.03515) | [PDF](https://arxiv.org/pdf/2504.03515)  
**Start with:** [[Robot Learning Primer]] | **Related:** [[DexCap - 2403.07788]], [[Dexterous Cable Manipulation - 2502.00396]]

## In plain English

Dexterous manipulation means controlling objects through coordinated finger movement and contact, sometimes repositioning an object within the hand. This survey explains why such tasks are hard: many joints, uncertain friction and contact, and a large variety of objects. It reviews imitation learning as a way to learn from expert demonstrations without manually coding every contact behavior.

## How to use the survey

Separate the data-collection method from the learning method and from the robot hand. A method that works with a multi-finger hand may not directly apply to a two-finger gripper. Compare how papers measure success, generalization, sample efficiency, and contact handling. The abstract contrasts imitation learning with model-based planning and reinforcement learning, but the full survey should give a more nuanced view.

## Terms to know

**Contact dynamics** is how objects move under touch, friction, and force. **In-hand manipulation** changes an object's pose while keeping it in the gripper or hand. **Sample efficiency** describes how much useful learning comes from a limited amount of data.

## What to inspect in the PDF

Find a task and benchmark you can reproduce, then follow its primary papers. Surveys are a map of the field, not evidence that every listed method will transfer to your hardware.

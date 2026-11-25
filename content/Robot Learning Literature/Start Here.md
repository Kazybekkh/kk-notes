# Robot learning literature: start here

For the personalized textbook, equations, labs, learning plan, and research dashboard, open [[Home]]. This page remains the entry point to the original 20-paper collection.

This is a reading map for a final-year project on learning robot skills from demonstrations. Start with [[Robot Learning Primer]], then read the papers below in order. Each paper note links to the official arXiv abstract and PDF. The notes explain what is clear from the paper's abstract; they are a guide to reading, not a substitute for checking the full experiments and limitations.

Open [[Robot Learning Map]] for a visual Canvas. Obsidian's built-in **Graph view** also shows these notes because the wiki links below and in each note connect them.

## A beginner's route

1. [[ACT and ALOHA - 2304.13705]]: collect demonstrations with affordable robot arms, then imitate them.
2. [[Diffusion Policy - 2303.04137]]: learn a policy that can produce several plausible action sequences.
3. [[UMI - 2402.10329]]: collect demonstrations away from the robot with a handheld gripper.
4. [[EgoMimic - 2410.24221]]: combine human first-person video with robot data.
5. [[DexCap - 2403.07788]]: capture detailed human hand motion for dexterous robot hands.
6. [[HumanPlus - 2406.10454]]: transfer human whole-body motion to a humanoid.
7. [[pi0 - 2410.24164]]: see how a large generalist vision-language-action policy is built.

## Data collection and embodiment

- [[LeRobot - 2602.22818]] connects the above ideas to an open-source robot-learning stack and affordable hardware. This is especially relevant to the SO-101 setup in [[lerobot]].
- [[RealDexUMI - 2606.06033]] keeps sensing and hand hardware shared between collection and deployment.
- [[UMI-on-Air - 2510.02614]] adapts a handheld-data policy to a robot with different physical constraints.
- [[Cross-Embodiment Transfer - 2607.27549]] studies representations that can carry behavior across robot bodies.
- [[Human-to-Robot Retargeting Objectives - 2506.09384]] compares objectives for mapping human hand motion to robot hands.

## Human video and dexterity

- [[Robot Learning from Human Videos Survey - 2604.27621]] gives a broad taxonomy; read this early if the field feels fragmented.
- [[EgoEngine - 2606.12604]] turns first-person human video into robot-style observations and feasible actions.
- [[VILP - 2502.01784]] uses predicted future video to help plan robot actions.
- [[Dexterous Imitation Survey - 2504.03515]] surveys learning multi-fingered manipulation from demonstrations.
- [[Dexterous Cable Manipulation - 2502.00396]] is a concrete task study for flexible objects.

## Adjacent or lower-priority papers

- [[Multimodal Sim-to-Real Audio - 2507.02864]] adds sound to simulated training, using pouring as a task.
- [[Correspondence-free Motion Retargeting - 2302.00556]] concerns animating target shapes from human motion; check its fit before treating it as robot-policy work.
- [[Attention Steering for VLA Driving - 2608.17095]] is about driving models rather than manipulation; useful mainly for thinking about model control and safety.

## Project directions to test

These are *questions*, not established gaps. Check each paper's full limitations and recent follow-up work before committing.

- Can SO-101 demonstrations collected with [[LeRobot - 2602.22818]] be augmented with cheap first-person video in a way that improves generalization? Compare against a robot-only [[ACT and ALOHA - 2304.13705]] baseline.
- How much does a shared action representation matter when transferring from a handheld device like [[UMI - 2402.10329]] to a low-cost arm? Compare relative end-effector targets with direct joint targets.
- Can simple audio or contact cues improve a small-arm pouring task over vision alone? [[Multimodal Sim-to-Real Audio - 2507.02864]] motivates a controlled test.

## Status

These 20 notes reflect the current local arXiv collection in `~/paper-mining/papers.sqlite` on 21 September 2026. Citation-based ranking and automated limitation extraction were not available yet: Semantic Scholar rate-limited the unauthenticated request, and Ollama is not installed here. The order above is pedagogical, not a computed ranking. New pipeline results may change which papers deserve attention.

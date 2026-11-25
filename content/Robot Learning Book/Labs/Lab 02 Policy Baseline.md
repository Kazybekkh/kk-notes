---
type: lab
status: not-started
tags: [robot-learning, lab, so101]
---
# Lab 02: your first policy baseline

[[Home]] | [[05 Training Neural Policies]] | [[15 Robot Systems and Deployment]] | [[lerobot]]

**Goal:** a repeatable SO-101 task with a transparent data-to-deployment loop.

Choose a simple pick-and-place with a clear success condition and bounded workspace. Verify robot identity, calibration, low-speed control, camera orientation, and stop behavior using the hardware's established setup process.

Record demonstrations using your installed LeRobot version. Keep raw episode boundaries and timestamps. Document joint ordering, camera settings, action meaning, and collection session. Hold out whole sessions or configurations appropriate to the intended claim.

Use an existing supported imitation-policy implementation. First overfit a tiny subset to check the pipeline; then train the baseline with a declared budget. Follow the [official real-world imitation guide](https://huggingface.co/docs/lerobot/il_robots) for current commands instead of copying commands for a different version.

Evaluate repeated supervised trials with a fixed reset procedure. Save failures as well as successes. Record interventions and latency.

**Deliverables:** setup description, dataset manifest, configuration, checkpoint identifier, short success/failure videos, and an evaluation table with denominators.

**Pass condition:** a second session can reproduce the procedure, and you can trace every policy output back to the action convention used during collection. Low success is acceptable at this stage if the experiment is interpretable.

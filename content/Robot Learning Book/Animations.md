---
type: reproducibility
tags: [robot-learning, figures, animation]
---
# Animations

[[Home]] | [[Visual Atlas]] | [[Figure Reproduction]]

Short animated scenes that show how a quantity changes, which a static figure cannot. Each is a Python file in `Tools/animations/` rendered with [ManimGX](https://github.com/academa-labs/manimgx), an open-source engine that uses the Manim Community Edition API. Like the static figures, these are analytic or simulated teaching examples, not measurements of SO-101 or any trained model.

## The scenes

| Video | Chapter | What to watch for |
|---|---|---|
| ![[ch01_gradient_descent.mp4]] | [[01 Math for Learning]] | The large step zig-zagging across the steep valley while the small step crawls along the shallow one |
| ![[ch02_arm_ik.mp4]] | [[02 Geometry and Kinematics]] | The velocity ellipse flattening as the arm straightens: that is a singularity |
| ![[ch02_frame_composition.mp4]] | [[02 Geometry and Kinematics]] | The same two transforms landing 2.55 apart when the product is swapped |
| ![[ch03_pd_control.mp4]] | [[03 Dynamics and Feedback]] | Overshoot and ringing at low damping; no overshoot at damping ratio 1 |
| ![[ch03_pendulum_delay.mp4]] | [[03 Dynamics and Feedback]] | Identical gains settling cleanly, wobbling at 100 ms of delay, and ringing at 120 ms |
| ![[ch04_pinhole_projection.mp4]] | [[04 Perception and State]] | The pixel offset halving each time depth doubles, and three depths sharing one pixel |
| ![[ch04_kalman_update.mp4]] | [[04 Perception and State]] | The posterior sliding toward whichever source has the smaller variance |
| ![[ch04_kalman_filter.mp4]] | [[04 Perception and State]] | Uncertainty growing on each predict, shrinking on each update, and settling |
| ![[ch06_compounding_dagger.mp4]] | [[06 Imitation and Distribution Shift]] | Cloned runs leaving the lane more often on longer tasks, and DAgger's recovery data fixing it |
| ![[ch07_chunking_latency.mp4]] | [[07 ACT and Action Sequences]] | The long-horizon rows running their stale plan after the bump, and the short one switching plans every 100 ms |
| ![[ch08_flow_two_modes.mp4]] | [[08 Diffusion and Flow Matching]] | Samples splitting into two modes, the mean landing in the obstacle, and coarse sampling collapsing toward it |
| ![[ch09_value_iteration.mp4]] | [[09 Reinforcement Learning]] | Value spreading one cell per sweep, and the discount alone deciding which goal the agent chases |
| ![[ch10_offline_overestimation.mp4]] | [[10 Offline RL and Data Coverage]] | The fitted max landing where no data exists, and bootstrapping multiplying that error tenfold |
| ![[ch11_model_error_planning.mp4]] | [[11 World Models and Planning]] | A plan made with a slightly wrong model drifting 1.65 m off target, under the chapter's error bound, while replanning lands within 0.11 m |
| ![[appendix_attention_mask.mp4]] | [[Appendix - Neural Networks and Attention]] | Scores, softmax weights and the causal mask on a six-token robot sequence, and an edit to a future token that leaks backwards only without the mask |
| ![[ch14_friction_cone.mp4]] | [[14 Contact and Dexterity]] | The friction cone in 3D: a sideways load that sticks, one that slides, and a harder press that holds it again |
| ![[ch14_impedance_wall.mp4]] | [[14 Contact and Dexterity]] | A stiff and a compliant impedance controller driven 2 cm into a wall: tracking error against contact force |

## Render or re-render

From a terminal in the vault:

~~~bash
"Robot Learning Book/Tools/animate.sh"            # all scenes
"Robot Learning Book/Tools/animate.sh" ch03       # only scenes whose file name contains ch03
QUALITY=high "Robot Learning Book/Tools/animate.sh"   # 1080p60 instead of 720p30
~~~

The first run creates a Python 3.13 environment in `~/.venvs/robot-anim` and installs ManimGX there, so nothing is added to the vault. Each video lands in `Assets/` under the scene's file name and updates in the chapter where it is embedded. A scene renders in a few seconds.

ManimGX also writes a storyboard for each video: the final frame of every animation step, saved in `Tools/animations/storyboards/` (not synced to git). Open it to check a scene without watching the video. The render output also lists layout problems such as overlapping text.

## Learn by changing the scene

The scenes are small on purpose. Editing one and predicting the result before rendering is the exercise:

- **ch01:** predict the rate where the red path stops converging, then set `ETAS = [0.08, 0.41]` and check. Then set `B = 1.0`: on a round bowl both paths head straight for the minimum, and neither zig-zags.
- **ch02:** set `LAMBDA = 0.0` (plain pseudo-inverse) and predict what happens near the unreachable target. Then try `LAMBDA = 0.5`.
- **ch02 frames:** before rendering, work out where C lands if ${}^BT_C$ only translates (set its angle to 0 in `T_BC`). Does the order still matter? Then make ${}^AT_B$ a pure translation and check again.
- **ch03:** set the gains to the chapter exercise, $K_p=4$, $K_d=4$, by changing `WN` and `ZETAS`. Check that the curve matches your $\omega_n$ and $\zeta$.
- **ch03 pendulum:** add a 130 ms case to `CASES` and watch it go unstable. Then predict whether halving `KP` and `KD` makes 120 ms of delay better or worse, and render to check.
- **ch04 pinhole:** set `FX = 300` and predict the three offsets before rendering. Do the three points on one ray still share a pixel? Why?
- **ch04 filter:** set `Q = 0` and predict where $P^+$ goes as steps continue. Then set `R = 0.2` and explain why the estimate now hugs the measurements.
- **ch06:** set `LAM = 0` and predict whether behaviour cloning still drifts. Then restore it and set `NOISE = 0.03`: what happens to the gap between the two curves, and why?
- **ch07:** move `T_BUMP` to 0.95 s and predict each row's reaction time before rendering. Then set `CHUNK_ERR = 0`: which row now looks best, and what does that say about when long chunks are safe?
- **ch08:** set `W = np.array([0.8, 0.2])` and predict where the one-step sample lands before rendering. Is it still inside the obstacle? Then set `S = 0.4` and explain the new hit rate at 32 steps.
- **ch09:** find by hand the discount at which the start values both goals equally, then set `GAMMAS` to values just below and above it and check the paths. Why do cells next to the +10 head for it even at $\gamma=0.5$?
- **ch10:** set `DEG = 2` and predict whether the greedy pick still leaves the data. Then restore it and widen the data to `D_LO, D_HI = -2.5, 2.5`: what happens to the survey line, and why?
- **ch11:** set `TILT = 0` so the only error is friction. Predict whether the open-loop miss shrinks more or less than half, then check. Next, set `C_MODEL = C_REAL` as well: what do the error line and the bound do?
- **Attention appendix:** set `CHANGED = 1` (act 1) and predict which masked bars stay at zero before rendering. Then set `D_K = 16` and check whether the rows of the weight matrix get sharper or flatter.
- **ch14 friction cone:** work out the smallest normal force that holds the 2.6 N load, set `F_N_HARD` to just below it, and predict the arrow's colour in the last phase before rendering.
- **ch14 impedance:** find the stiffness that settles at about 10 N against the wall, put it in place of the compliant case's 200, and compare its lag before contact with the two shown.

## Adding a scene

Create `Tools/animations/chNN_topic.py` with one scene class, run `animate.sh chNN`, then embed it in the chapter with `![[chNN_topic.mp4]]`. Compute the physics or probability with NumPy first; ManimGX only draws what you give it, so the computation is where the learning happens. Reuse the book colours: teal `#007f79`, red `#c3494e`, blue `#4872b8`, gold `#986b15`.

Claude Code can write a first draft. Ask, for example: *"Add a ManimGX scene in Tools/animations for chapter 06 showing compounding error in behaviour cloning, render it with animate.sh, check the storyboard, and embed it."*

Good next candidates:

- [[16 Evaluation and Uncertainty]]: the Wilson interval for a success rate narrowing as trials grow from 5 to 100.

## Limits

ManimGX is version 0.1.1 and needs Python 3.13 or newer. The script pins that version so a future release cannot break existing scenes without you choosing to upgrade (change `MANIMGX_VERSION` in `animate.sh`). It draws animations; it does not simulate physics. For contact-rich dynamics, use a simulator such as MuJoCo or Isaac Sim and use these scenes to explain the idea behind it.

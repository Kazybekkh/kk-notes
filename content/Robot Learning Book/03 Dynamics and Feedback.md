---
type: chapter
chapter: 3
status: not-started
tags: [robot-learning, control]
---
# 03 Dynamics and feedback

[[Home]] | Previous: [[02 Geometry and Kinematics]] | Next: [[04 Perception and State]]

A policy may request a target pose, but motors, gravity, friction, contact, and delay determine what actually happens. Dynamics models that relationship. Feedback corrects errors using repeated observations.

## The robot equation

For a rigid manipulator, a common model is

$$
M(q)\ddot q+C(q,\dot q)\dot q+g(q)
=\tau+J(q)^\top f_{\rm ext}.
$$

$M$ is the inertia matrix, $C\dot q$ collects velocity-dependent effects under this convention, $g$ is gravity torque, $\tau$ is actuator torque, and $f_{\rm ext}$ is an external wrench mapped through the matching Jacobian. Real models may add friction and actuator dynamics. A learned policy need not output torque: an internal position controller may convert its requested joint targets into motor effort.

## A simple closed loop

For a desired joint position $q^\star$, proportional-derivative control is

$$
\tau=K_p(q^\star-q)-K_d\dot q.
$$

The proportional term pulls toward the target; the derivative term damps motion. For a stationary target and ideal unit-mass scalar plant $\ddot q=\tau$, error dynamics are $\ddot e+K_d\dot e+K_p e=0$. Positive gains stabilize this ideal system, but actuator limits and delays can invalidate the simplified analysis.

![[feedback_response.png]]

*Analytic second-order step responses with unit natural frequency. These curves do not model your SO-101 motors.*

![[ch03_pd_control.mp4]]

*The same three damping ratios as a simulation of the ideal unit-mass plant. Change `ZETAS` or the gains in `Tools/animations/ch03_pd_control.py` and rerun to test your exercise answer.*

![[ch03_pendulum_delay.mp4]]

*A unit pendulum driven from 30° to 120° by PD plus a gravity-cancelling term, $K_p=25$, $K_d=10$. Without delay it settles cleanly. The same gains acting on 100 ms old measurements wobble, and at 120 ms they overshoot by 11° and are still ringing at 6 s. Past about 130 ms the loop is unstable. Source: `Tools/animations/ch03_pendulum_delay.py`.*

~~~mermaid
flowchart LR
  Target["Desired pose"] --> Controller["Controller"]
  Controller --> Motor["Actuator and robot"]
  Motor --> Sensor["Sensor"]
  Sensor --> Controller
  Disturbance["Contact or disturbance"] --> Motor
~~~

## Why robot learning needs control literacy

Changing the frequency at which a policy runs changes the physical action it produces. A 2 cm target increment sent ten times per second is not equivalent to the same increment sent fifty times per second. Low-level control frequency, sensor frequency, policy frequency, and action-horizon duration should all be recorded separately.

The policy's loss can decrease while physical tracking gets worse because the model predicts stale or overly aggressive commands. Diagnose timestamp errors, calibration, target units, and actuator saturation before blaming the architecture.

## Exercise and lab connection

With $K_p=4$ and $K_d=4$ for the ideal scalar plant, compute natural frequency and damping ratio.

> [!success]- Answer
> Comparing with $\ddot e+2\zeta\omega_n\dot e+\omega_n^2e=0$ gives $\omega_n=2$ radians per second and $\zeta=1$.

In [[Lab 02 Policy Baseline]], first verify repeatable low-speed target tracking and a working stop mechanism. Read the [MIT Underactuated Robotics notes](https://underactuated.mit.edu/) for deeper dynamics and control.

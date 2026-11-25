---
type: chapter
chapter: 14
status: not-started
tags: [robot-learning, manipulation, contact]
---
# 14 Contact and dexterity

[[Home]] | Previous: [[13 Vision Language Action Models]] | Next: [[15 Robot Systems and Deployment]]

Moving freely through the air is different from touching an object. Contact introduces abrupt changes: fingers stop moving freely, forces rise, objects slip or rotate, and tiny geometry errors matter.

## A first friction model

For a simple Coulomb contact,

$$
\|f_{\rm tangent}\|\le\mu f_{\rm normal},\qquad f_{\rm normal}\ge0.
$$

$\mu$ is the coefficient of friction. Forces inside this friction cone can be consistent with sticking under the idealized model; exceeding the bound leads to sliding behavior. Real materials, deformation, and contact geometry complicate the picture.

![[friction_cone.png]]

*Two-dimensional slice of an ideal friction cone with coefficient 0.5.*

![[ch14_friction_cone.mp4]]

*The full 3D cone for $\mu=0.5$. The arrow is the force a fingertip needs from the contact to stay put, and the ring marks $\|f_{\rm tangent}\|=\mu f_{\rm normal}$ at the arrow's height. With $f_{\rm normal}=4$ N, a 1.5 N sideways load in any direction sticks. A 2.6 N load exceeds the 2 N bound, so the fingertip slides; the slide is drawn, not simulated. Pressing with 6 N raises the bound to 3 N, and the same load sticks. Source: `Tools/animations/ch14_friction_cone.py`.*

If $f_{\rm normal}=4$ newtons and $\mu=0.5$, the ideal tangential bound is 2 newtons. This does not tell you how much force is safe for a fragile object or a particular gripper.

## Compliance and impedance

A compliant controller allows displacement under contact rather than trying to enforce a rigid trajectory at any cost. A simplified Cartesian impedance relation is

$$
F=K(x^\star-x)+D(\dot x^\star-\dot x).
$$

$K$ is stiffness and $D$ is damping in compatible coordinates. The relation expresses a desired interaction behavior; realizing it on hardware requires suitable sensing, control, and actuator support.

## Why sensing matters

Vision can show where fingers are, but may miss whether an object is securely grasped. Tactile sensing adds evidence about pressure, contact, or slip. Proprioceptive or motor-current signals can also help, though they are not interchangeable with calibrated force measurements.

[[DexCap - 2403.07788]] and [[RealDexUMI - 2606.06033]] explore richer dexterous data collection. [[Dexterous Cable Manipulation - 2502.00396]] illustrates deformable-object complexity.

## Your scope

A two-finger SO-101 gripper can support useful manipulation research without matching a human hand. Choose tasks whose difficulty is observable and repeatable, such as grasping across small position changes. Do not make a dexterity claim solely from a successful lift: specify orientation changes, contact transitions, or recovery behavior.

**Exercise:** why might increasing position-controller stiffness make insertion worse?

> [!success]- Answer
> Small alignment errors can produce large contact forces and jamming. Compliance may tolerate error, although too much compliance can reduce precision and must be designed for the task.

![[ch14_impedance_wall.mp4]]

*After the exercise: two impedance controllers, $K=2000$ and $K=200$ N/m, each with damping ratio 0.7 on a 1 kg end effector. Both get the same command, which ends 2 cm past a wall. The stiff one tracks within 0.3 mm before contact but settles at 36.4 N against the wall. The compliant one lags by up to 3.4 mm and settles at 4.0 N. Both see a short spike on impact (36.6 N and 22.2 N). Source: `Tools/animations/ch14_impedance_wall.py`.*

For contact mechanics and manipulation planning, continue with [MIT Robotic Manipulation](https://manipulation.csail.mit.edu/).

---
type: chapter
chapter: 2
status: not-started
tags: [robot-learning, foundations, geometry]
---
# 02 Geometry and kinematics

[[Home]] | Previous: [[01 Math for Learning]] | Next: [[03 Dynamics and Feedback]]

Kinematics describes motion geometry without asking which forces cause it. A point is meaningless without its coordinate frame: a target 10 cm to the camera's right is not necessarily 10 cm to the robot's right.

## Transforming coordinates

A rigid transform combines rotation $R$ and translation $t$:

$$
{}^A T_B=
\begin{bmatrix}{}^A R_B&{}^A t_B\\0&1\end{bmatrix},
\qquad
\begin{bmatrix}{}^A p\\1\end{bmatrix}
={}^A T_B\begin{bmatrix}{}^B p\\1\end{bmatrix}.
$$

The superscript says which frame expresses the coordinates; the matrix above maps coordinates in B into A. Rotation matrices satisfy $R^\top R=I$ and $\det R=1$. Transforms compose by matrix multiplication:

$$
{}^AT_C={}^AT_B{}^BT_C.
$$

The order matters.

![[ch02_frame_composition.mp4]]

*${}^BT_C$ is expressed in frame B, so it acts along B's axes after the move to B, and C lands at $(2,1.5,0.5)$. Swapping the product applies it along A's axes first, and the frame ends at $(3.5,-0.5,0)$, 2.55 away. Source: `Tools/animations/ch02_frame_composition.py`.*

## A two-link arm you can understand completely

For link lengths $l_1,l_2$ and revolute joint angles $q_1,q_2$ measured in radians:

$$
x=l_1\cos q_1+l_2\cos(q_1+q_2),\qquad
y=l_1\sin q_1+l_2\sin(q_1+q_2).
$$

These are **forward kinematics**: angles become a tool position. **Inverse kinematics** asks for angles that reach a target. It can have multiple solutions or no solution.

![[planar_arm.png]]

*Two exact configurations with unit-length links; different elbow configurations can reach the same point.*

For a target at distance $r=\sqrt{x^2+y^2}$, reaching requires $|l_1-l_2|\le r\le l_1+l_2$. This geometric condition ignores obstacles, joint limits, tool orientation, and collisions.

## The Jacobian connects small movements

$$
\dot x_{\rm task}=J(q)\dot q,\qquad
J=\begin{bmatrix}
-l_1\sin q_1-l_2\sin(q_1+q_2)&-l_2\sin(q_1+q_2)\\
l_1\cos q_1+l_2\cos(q_1+q_2)&l_2\cos(q_1+q_2)
\end{bmatrix}.
$$

Here $x_{\rm task}=[x,y]^\top$. At some configurations, $J$ loses rank: certain tool velocities cannot be produced instantaneously. This is a singularity. Near a singularity, solving for joint motion can amplify small target changes. A damped least-squares step uses

$$
\Delta q=J^\top(JJ^\top+\lambda^2 I)^{-1}\Delta x,
$$

where $\lambda>0$ trades exact tracking for bounded motion. It still needs joint and collision checks.

![[ch02_arm_ik.mp4]]

*Damped least-squares IK with $l_1=l_2=1$, $\lambda=0.1$. The gold ellipse is every tool velocity reachable with unit joint speed; watch it flatten as the arm straightens toward an unreachable target. Source: `Tools/animations/ch02_arm_ik.py`.*

## Exercise

Set $l_1=l_2=1$, $q_1=q_2=0$. Find the tool position and Jacobian. Which instantaneous direction is unavailable?

> [!success]- Answer
> The tool is at $(2,0)$ and $J=\bigl[\begin{smallmatrix}0&0\\2&1\end{smallmatrix}\bigr]$. First-order movement along the x axis is unavailable at this straight configuration.

Continue with [[Lab 01 Planar Arm]]. For formal treatment of frames, rigid motions, and kinematics, use the authors' [Modern Robotics materials](https://modernrobotics.northwestern.edu/nu-gm-book-resource/).

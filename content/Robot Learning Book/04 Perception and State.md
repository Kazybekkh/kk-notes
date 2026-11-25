---
type: chapter
chapter: 4
status: not-started
tags: [robot-learning, perception]
---
# 04 Perception and state

[[Home]] | Previous: [[03 Dynamics and Feedback]] | Next: [[05 Training Neural Policies]]

The **state** is everything needed to predict the world's future given an action. The **observation** is what sensors reveal. A camera cannot directly show an object's hidden side, friction, or exact velocity. Learning often happens under partial observability.

## From 3D to pixels

For a point expressed in camera coordinates, an ideal pinhole camera gives

$$
u=f_x X/Z+c_x,\qquad v=f_y Y/Z+c_y.
$$

$f_x,f_y$ are focal lengths in pixel units and $(c_x,c_y)$ is the principal point. Doubling depth $Z$ halves displacement from the principal point when $X,Y$ stay fixed. Real cameras require distortion calibration; a planar image location alone does not determine depth.

![[ch04_pinhole_projection.mp4]]

*A point 0.3 m off the optical axis with $f_x=600$ px: its offset is 180, 90 and 45 px at depths of 1, 2 and 4 m. Points at $(0.3,1)$, $(0.6,2)$ and $(0.9,3)$ m share one ray and one pixel. Source: `Tools/animations/ch04_pinhole_projection.py`.*

You need **intrinsic calibration** for the camera's imaging model and **extrinsic calibration** for its pose relative to the robot. Confusing those two leads to systematic reaching errors. Existing notes on [[Object Detection and Segmentation]] and [[Convolutional Neural Networks]] fit here.

## Estimation combines measurements with prediction

A simple linear model is

$$
x_{t+1}=Ax_t+Bu_t+w_t,\qquad y_t=Hx_t+v_t.
$$

$w_t$ is process noise and $v_t$ is measurement noise. For a scalar estimate with prior variance $P$ and measurement variance $R$, the Kalman gain is $K=P/(P+R)$. The update is $\hat x^+=\hat x^-+K(y-\hat x^-)$ with posterior variance $(1-K)P$ under the scalar Gaussian assumptions.

If the measurement is noisy, $R$ is large and you trust it less. If the prediction is uncertain, $P$ is large and the measurement matters more. Learned perception also has uncertainty, but a network's softmax output is not automatically a calibrated probability of physical correctness.

![[bayes_update.png]]

*Illustrative scalar Gaussian prior, likelihood, and posterior.*

![[ch04_kalman_update.mp4]]

*The scalar update as $P$ and $R$ change, with prior mean $-1$ and measurement $3$. The numbers differ from the exercise below, so the exercise is still yours. Source: `Tools/animations/ch04_kalman_update.py`.*

![[ch04_kalman_filter.mp4]]

*Ten predict-then-update cycles for a robot commanded +1 per step, with $Q=0.5$ and $R=2$. Each predict adds $Q$ to the variance and each update shrinks it; $P^+$ settles at $0.78$, the positive root of $P^2+QP-QR=0$, and the gain at $0.39$. Source: `Tools/animations/ch04_kalman_filter.py`.*

## What this means for a policy

Stacking recent images and joint states can reveal motion a single frame hides. A recurrent model can summarize a longer history. Neither guarantees that hidden physical quantities are identifiable. A transparent cup, occluded gripper, or shifted camera may create ambiguity that more training cannot fully remove without additional sensing.

**Exercise:** a prior mean of 0 has variance 4; a measurement of 3 has variance 1. Find the posterior mean and variance.

> [!success]- Answer
> $K=4/5$, posterior mean $2.4$, posterior variance $0.8$.

In your experiments, log camera pose, resolution, exposure changes, timestamp alignment, and whether proprioception (the robot's own joint measurements) is supplied. For manipulation perception and geometry, see [MIT Robotic Manipulation](https://manipulation.csail.mit.edu/).

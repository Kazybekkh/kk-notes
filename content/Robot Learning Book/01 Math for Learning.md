---
type: chapter
chapter: 1
status: not-started
tags: [robot-learning, foundations, mathematics]
---
# 01 Math for learning

[[Home]] | Next: [[02 Geometry and Kinematics]]

## Vectors describe a robot

A vector is an ordered list of numbers. An arm configuration is $q=[q_1,\ldots,q_n]^\top$: one joint position per coordinate. A velocity has different units from a position even when both use the same number of coordinates. Write units beside variables before combining them.

A matrix maps one vector to another. For $A\in\mathbb R^{m\times n}$ and $x\in\mathbb R^n$, $Ax\in\mathbb R^m$. The transpose $x^\top$ makes a column into a row. The Euclidean norm $\|x\|_2=\sqrt{\sum_i x_i^2}$ measures length. A dot product $u^\top v$ measures alignment, but only has a meaningful geometric interpretation when coordinates and units are compatible.

## Derivatives tell you what to change

A scalar derivative measures local sensitivity. A gradient collects derivatives of a scalar loss with respect to many parameters:

$$
\nabla_\theta L=
\begin{bmatrix}\partial L/\partial\theta_1&\cdots&\partial L/\partial\theta_d\end{bmatrix}^{\!\top},
\qquad
\theta_{k+1}=\theta_k-\eta\nabla_\theta L.
$$

$\theta$ holds learned weights; $\eta>0$ is the learning rate; $k$ counts optimizer updates. The chain rule propagates derivatives through composed functions and is the basis of backpropagation. Your existing [[Loss Functions and Backpropagation]] note connects here.

For the teaching example $L(w)=(w-3)^2$, $\partial L/\partial w=2(w-3)$. Starting at $w=0$ with $\eta=0.1$ gives $w_1=0.6$. The step moves toward 3. A learning rate of 1 oscillates between 0 and 6; choosing a step size is part of numerical stability.

![[gradient_descent.png]]

*Analytic teaching example generated locally; this is not a robot training result.*

![[ch01_gradient_descent.mp4]]

*Two learning rates on the bowl $L=\tfrac12(x^2+5y^2)$, where descent is stable only while $\eta<2/5$. Rate 0.37 bounces across the steep direction; rate 0.08 is smooth but slow along the shallow one. Source: `Tools/animations/ch01_gradient_descent.py`.*

## Probability represents uncertainty

A random variable $X$ may take different values. Its expectation is a probability-weighted average. For discrete outcomes:

$$
\mathbb E[X]=\sum_x x\,p(x),\qquad
\operatorname{Var}(X)=\mathbb E[(X-\mathbb E[X])^2].
$$

Conditional probability $p(a\mid o)$ describes actions given an observation. Bayes' rule updates a belief after evidence:

$$
p(s\mid o)=\frac{p(o\mid s)p(s)}{p(o)}.
$$

The prior $p(s)$ expresses belief before seeing $o$; the likelihood $p(o\mid s)$ models what you would observe if the state were $s$; the posterior is the updated belief. A probability of 0.9 is not a promise that a particular action succeeds.

## Learn by doing

1. Write the dimensions of camera features $z\in\mathbb R^{128}$, a linear policy $Wz+b$, and an action vector with six coordinates. What dimensions must $W,b$ have?
2. Derive one gradient step for $L(w)=(2w-4)^2$ at $w=0$, $\eta=0.05$.
3. Explain why averaging joint angles and camera pixels without normalization is problematic.

> [!success]- Check your answer
> $W\in\mathbb R^{6\times128}$ and $b\in\mathbb R^6$. The second loss has gradient $8w-16$, so $w_1=0.8$. Pixels and angles have incompatible scales and meanings; normalization aids optimization but does not make them physically interchangeable.

Build: implement linear regression with NumPy and compare your analytic gradient against central finite differences. Further mathematical study: [MIT OpenCourseWare linear algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/).

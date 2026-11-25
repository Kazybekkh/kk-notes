---
type: course-chapter
course: probability-statistics
chapter: 7
tags: [mathematics, probability, gaussian]
---

# Chapter 7: The multivariate Gaussian

Previous: [[PS 06 Joint Distributions and Covariance]] | [[PS 00 Course Map]] | Next: [[PS 08 Law of Large Numbers and Central Limit Theorem]]

> [!abstract] The big idea
> The multivariate Gaussian is a bell-shaped cloud in many dimensions, completely described by a **mean vector** (where the cloud is) and a **covariance matrix** (its size, shape and tilt). Its contours are ellipses whose axes are the covariance's eigenvectors. Its great practical virtue is that it **stays Gaussian** when you transform it linearly, look at part of it, or condition on part of it, and each of those operations has a simple closed formula. That is why it is the default model of uncertainty in robotics.

> [!info] In this chapter you will learn to
> 1. Read the multivariate Gaussian density and relate each part to the 1-D case.
> 2. Use Mahalanobis distance to measure how surprising a point is.
> 3. Draw the uncertainty ellipse from a covariance matrix.
> 4. Compute linear transformations, marginals and conditionals of Gaussians.
> 5. Sample from a Gaussian, and explain the reparameterization trick.
> 6. Recognize when a Gaussian is the wrong model.

> [!tip] Before you start
> You need the 1-D normal ([[PS 05 Continuous Random Variables]]), covariance matrices and $A\Sigma A^\top$ ([[PS 06 Joint Distributions and Covariance]]), and the spectral theorem and positive definite matrices ([[LA 09 Symmetric and Positive Definite Matrices]]).

---

## 7.1 The density

> [!note] Definition: multivariate Gaussian
> A random vector $x\in\mathbb R^n$ has distribution $\mathcal N(\mu,\Sigma)$ if its density is
> $$
> p(x)=\frac1{\sqrt{(2\pi)^n\det\Sigma}}\exp\!\left(-\tfrac12(x-\mu)^\top\Sigma^{-1}(x-\mu)\right),
> $$
> where $\mu\in\mathbb R^n$ is the mean and $\Sigma$ is a symmetric positive definite $n\times n$ covariance matrix.

### Compare with one dimension

The 1-D density is $\dfrac1{\sigma\sqrt{2\pi}}\exp\!\left(-\dfrac{(x-\mu)^2}{2\sigma^2}\right)$. Every piece has a matrix counterpart:

| 1-D | $n$-D | Role |
|---|---|---|
| mean $\mu$ | mean vector $\mu$ | centre of the cloud |
| variance $\sigma^2$ | covariance matrix $\Sigma$ | spread, shape and orientation |
| $\dfrac{(x-\mu)^2}{\sigma^2}$ | $(x-\mu)^\top\Sigma^{-1}(x-\mu)$ | squared distance in standard deviations |
| $\sigma$ | $\sqrt{\det\Sigma}$ | size (volume) of the cloud |

The structure is identical: a normalizing constant, then $e$ to the power of minus half a squared, standardized distance.

### A special case: independent coordinates

If $\Sigma$ is diagonal, $\Sigma=\operatorname{diag}(\sigma_1^2,\dots,\sigma_n^2)$, then $\Sigma^{-1}$ is diagonal too, and the exponent splits into a sum:

$$
(x-\mu)^\top\Sigma^{-1}(x-\mu)=\sum_i\frac{(x_i-\mu_i)^2}{\sigma_i^2}.
$$

The density becomes a **product** of 1-D normal densities: the coordinates are independent. A diagonal covariance means independent components.

---

## 7.2 Mahalanobis distance

The quantity in the exponent has a name:

> [!note] Definition: Mahalanobis distance
> $$
> d_M(x)=\sqrt{(x-\mu)^\top\Sigma^{-1}(x-\mu)}.
> $$

It is the distance from $x$ to the mean, **measured in standard deviations along each direction of the cloud**.

### Why ordinary distance is not enough

Suppose a cloud is long and thin: wide in the $x$-direction, narrow in $y$. A point 3 units to the right of the centre is ordinary (the cloud extends that far). A point 3 units **above** the centre is extremely unusual (the cloud is thin in that direction). Both have Euclidean distance 3. The Mahalanobis distance tells them apart.

**Worked example 7.1.** $\mu=0$, $\Sigma=\begin{bmatrix}9&0\\0&1\end{bmatrix}$ (standard deviation 3 in $x$, 1 in $y$).

- Point $(3,0)$: $d_M^2=\tfrac{9}{9}+0=1$. One standard deviation: ordinary.
- Point $(0,3)$: $d_M^2=0+\tfrac91=9$, so $d_M=3$. Three standard deviations: rare.

### Use: outlier rejection

A robot predicts where a landmark should appear, with some uncertainty $\Sigma$. A measurement arrives. If its Mahalanobis distance from the prediction is too large (say, beyond 3), it is probably a false detection and is discarded. This is called **gating**, and it is standard in tracking and localization.

---

## 7.3 The geometry: uncertainty ellipses

### Contours are ellipses

Points of equal density are points of equal Mahalanobis distance:

$$
(x-\mu)^\top\Sigma^{-1}(x-\mu)=c.
$$

From [[LA 09 Symmetric and Positive Definite Matrices]] (section 9.5), these are **ellipses** in 2-D and ellipsoids in higher dimensions. Use the spectral decomposition $\Sigma=Q\Lambda Q^\top$:

> [!important] Reading the ellipse
> - The **axes** of the ellipse point along the **eigenvectors** of $\Sigma$.
> - The **half-length** of the 1-sigma ellipse along eigenvector $q_i$ is $\sqrt{\lambda_i}$: the standard deviation in that direction.
> - The $k$-sigma ellipse is $k$ times larger.

### Worked example 7.2

$$
\Sigma=\begin{bmatrix}2&1\\1&2\end{bmatrix}.
$$

Eigenvalues 3 and 1, with eigenvectors $\tfrac1{\sqrt2}(1,1)$ and $\tfrac1{\sqrt2}(1,-1)$.

- Along the diagonal $(1,1)$: standard deviation $\sqrt3\approx1.73$. The long axis.
- Along the anti-diagonal $(1,-1)$: standard deviation $1$. The short axis.

The cloud is tilted upward at $45^\circ$. The correlation is $\rho=\dfrac1{\sqrt2\sqrt2}=0.5$, positive, matching the upward tilt.

### Reading a $2\times2$ covariance at a glance

| $\Sigma$ | Shape of the cloud |
|---|---|
| $\sigma^2I$ | circle |
| diagonal, unequal entries | ellipse aligned with the axes |
| positive off-diagonal | ellipse tilted upward (positive correlation) |
| negative off-diagonal | ellipse tilted downward (negative correlation) |
| nearly singular | very thin ellipse: the variables almost determine each other |

> [!warning] How much probability is inside?
> In 1-D, $\pm1\sigma$ holds 68%. In 2-D, the 1-sigma **ellipse** holds only about **39%**, and the 2-sigma ellipse about **86%**. To contain 95% in 2-D you need about **2.45** sigma. In higher dimensions the numbers drop further. Do not reuse the 1-D rule for ellipses.

---

## 7.4 Property 1: linear transformations

> [!important] Linear maps keep Gaussians Gaussian
> If $x\sim\mathcal N(\mu,\Sigma)$ and $y=Ax+b$, then
> $$
> y\sim\mathcal N\big(A\mu+b,\;A\Sigma A^\top\big).
> $$

The mean and covariance formulas hold for any distribution (chapter 6). What is special is that $y$ is **still Gaussian**, so these two quantities describe it completely.

**Worked example 7.3.** $x\sim\mathcal N(0,I)$ in 2-D, $y=Ax$ with $A=\begin{bmatrix}2&0\\1&1\end{bmatrix}$:

$$
\operatorname{Cov}(y)=AA^\top=\begin{bmatrix}4&2\\2&2\end{bmatrix}.
$$

A round cloud becomes a tilted ellipse.

**Worked example 7.4: sum of independent Gaussians.** $X\sim\mathcal N(1,4)$, $Y\sim\mathcal N(2,9)$ independent. Then $X+Y\sim\mathcal N(3,13)$.

---

## 7.5 Property 2: marginals

> [!important] Marginals of a Gaussian are Gaussian
> To get the distribution of some of the coordinates, simply **pick out** the matching entries of $\mu$ and the matching block of $\Sigma$. No integration needed.

**Worked example 7.5.**

$$
\mu=\begin{bmatrix}1\\2\\3\end{bmatrix},\quad\Sigma=\begin{bmatrix}4&1&0\\1&9&2\\0&2&1\end{bmatrix}.
$$

- $X_2\sim\mathcal N(2,9)$.
- $(X_1,X_3)\sim\mathcal N\!\left(\begin{bmatrix}1\\3\end{bmatrix},\begin{bmatrix}4&0\\0&1\end{bmatrix}\right)$.

(This is property 1 with a matrix $A$ that selects coordinates.)

---

## 7.6 Property 3: conditioning

### The formulas

Split $x$ into two parts, $x_1$ (what you want to know) and $x_2$ (what you observe):

$$
\mu=\begin{bmatrix}\mu_1\\\mu_2\end{bmatrix},\qquad\Sigma=\begin{bmatrix}\Sigma_{11}&\Sigma_{12}\\\Sigma_{21}&\Sigma_{22}\end{bmatrix}.
$$

> [!important] Conditioning a Gaussian
> Given the observation $x_2$, the distribution of $x_1$ is Gaussian with
> $$
> \mu_{1\mid2}=\mu_1+\Sigma_{12}\Sigma_{22}^{-1}(x_2-\mu_2),
> $$
> $$
> \Sigma_{1\mid2}=\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}.
> $$

### Read the formulas slowly

These two lines are the Kalman filter in miniature, so they are worth understanding word by word.

**The mean.**

- $x_2-\mu_2$ is the **surprise**: how far the observation is from what was expected.
- $\Sigma_{12}\Sigma_{22}^{-1}$ is a **gain**: how much to move the estimate of $x_1$ per unit of surprise.
  - Large when $x_1$ and $x_2$ are strongly correlated ($\Sigma_{12}$ large): the observation is informative.
  - Small when the observation itself is very noisy ($\Sigma_{22}$ large): don't trust it much.
- The new mean is the old mean plus gain times surprise.

**The covariance.**

- It **shrinks**: something is subtracted from $\Sigma_{11}$. Observing a correlated quantity always reduces uncertainty.
- It does **not depend on the value** of $x_2$. How much you learn depends on how informative the sensor is, not on what it happened to read.

### Worked example 7.6: two dimensions

$(X_1,X_2)$ with mean zero and $\Sigma=\begin{bmatrix}2&1\\1&2\end{bmatrix}$. You observe $X_2=2$.

$$
\mu_{1\mid2}=0+\frac12(2-0)=1,\qquad\sigma^2_{1\mid2}=2-\frac{1\cdot1}2=1.5.
$$

Before: $X_1$ had mean 0, variance 2. After: mean 1, variance 1.5. The estimate moved halfway toward the observation (gain $\tfrac12$) and the uncertainty dropped by a quarter.

### Worked example 7.7: strong correlation

Same, but $\Sigma=\begin{bmatrix}1&0.9\\0.9&1\end{bmatrix}$ and $X_2=1$:

$$
\mu_{1\mid2}=0.9,\qquad\sigma^2_{1\mid2}=1-0.81=0.19.
$$

High correlation means the observation pins $X_1$ down tightly.

### Uncorrelated means independent (for Gaussians)

If $\Sigma_{12}=0$, the gain is zero: observing $x_2$ tells you nothing about $x_1$. So for **jointly Gaussian** variables, uncorrelated implies independent. This is **special to the Gaussian**. In general it is false ([[PS 06 Joint Distributions and Covariance]], warning 1).

---

## 7.7 Sampling and the reparameterization trick

### How to draw samples

To draw $x\sim\mathcal N(\mu,\Sigma)$:

1. Factor $\Sigma=LL^\top$ (Cholesky, [[LA 09 Symmetric and Positive Definite Matrices]]).
2. Draw $z$ with independent standard normal entries: $z\sim\mathcal N(0,I)$.
3. Set $x=\mu+Lz$.

*Check with property 1:* the mean is $\mu$ and the covariance is $LIL^\top=\Sigma$ ✓.

### The reparameterization trick

In machine learning we often want to **differentiate through sampling**: for example, adjust $\mu$ and $\sigma$ to make sampled actions better. A random draw seems not to have a derivative.

The trick: write the sample as

$$
x=\mu+\sigma z,\qquad z\sim\mathcal N(0,1),
$$

where the randomness $z$ comes from a **fixed** source that does not depend on the parameters. Now $x$ is an ordinary differentiable function of $\mu$ and $\sigma$, and gradients flow through it: $\partial x/\partial\mu=1$, $\partial x/\partial\sigma=z$.

Variational autoencoders and soft actor-critic (SAC) policies rely on this ([[Appendix - PPO SAC and Offline Learning]]).

---

## 7.8 The log-density and squared error

$$
\log p(x)=-\tfrac12(x-\mu)^\top\Sigma^{-1}(x-\mu)-\tfrac12\log\det\Sigma-\tfrac n2\log2\pi.
$$

With $\Sigma=\sigma^2I$, the first term is $-\dfrac{\|x-\mu\|^2}{2\sigma^2}$. So:

> [!important] Gaussian likelihood = squared error
> Maximizing a Gaussian log-likelihood with fixed variance is the same as **minimizing squared error**. That is where the mean squared error loss comes from ([[PS 09 Estimation and Maximum Likelihood]]).

---

## 7.9 What a Gaussian cannot do

### One peak only

> [!warning] The mode-averaging problem
> A robot must pass an obstacle. Half the demonstrations go **left**, half go **right**. Fit a single Gaussian to the steering commands: its mean is the average, **straight ahead**, straight into the obstacle. Its variance is large, but no sample from it reliably represents either good choice.
>
> A Gaussian has **one** peak. When the data has several distinct good answers (**multimodal** data), a single Gaussian blends them into a bad one.

This is the core motivation for mixture models, **diffusion policies** and **action chunking** in robot learning ([[08 Diffusion and Flow Matching]], [[07 ACT and Action Sequences]]).

### Other limits

- **Thin tails**: outliers are far rarer under a Gaussian than in real data.
- **Symmetric**: it cannot represent skewed quantities such as positive-only times.
- **Linear relationships only**: conditioning formulas assume the dependence between variables is linear.

---

## Summary

| Idea | Formula or fact |
|---|---|
| density | $\propto\exp\!\left(-\tfrac12(x-\mu)^\top\Sigma^{-1}(x-\mu)\right)$ |
| Mahalanobis distance | $\sqrt{(x-\mu)^\top\Sigma^{-1}(x-\mu)}$ |
| ellipse axes | eigenvectors of $\Sigma$; half-lengths $\sqrt{\lambda_i}$ |
| linear map | $Ax+b\sim\mathcal N(A\mu+b,A\Sigma A^\top)$ |
| marginal | pick out the block |
| conditional mean | $\mu_1+\Sigma_{12}\Sigma_{22}^{-1}(x_2-\mu_2)$ |
| conditional covariance | $\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$ |
| sampling | $\mu+Lz$, $\Sigma=LL^\top$ |

**Three facts to remember:**

1. Mean = where; covariance = shape and tilt; its eigenvectors are the ellipse axes.
2. Conditioning moves the mean by gain × surprise and always shrinks the covariance.
3. A Gaussian has one peak: it averages away multiple good answers.

---

## Exercises

### Part A: warm-up

**A1.** For $\Sigma=\begin{bmatrix}4&0\\0&1\end{bmatrix}$, describe the 1-sigma ellipse.

**A2.** $x\sim\mathcal N(0,I_2)$ and $y=\begin{bmatrix}1&2\\0&1\end{bmatrix}x+\begin{bmatrix}3\\0\end{bmatrix}$. Find the mean and covariance of $y$.

**A3.** From $\mu=(0,5,-1)$ and $\Sigma=\begin{bmatrix}1&0.5&0\\0.5&2&0\\0&0&3\end{bmatrix}$, give the distribution of $X_3$, and of $(X_1,X_2)$. Is $X_3$ independent of $(X_1,X_2)$?

**A4.** Compute the Mahalanobis distance of $(2,2)$ from $\mu=0$ when $\Sigma=\begin{bmatrix}4&0\\0&1\end{bmatrix}$.

> [!success]- Solutions to Part A
> **A1.** Axis-aligned; half-length 2 along $x$, 1 along $y$.
>
> **A2.** Mean $(3,0)$. Covariance $AA^\top=\begin{bmatrix}5&2\\2&1\end{bmatrix}$.
>
> **A3.** $X_3\sim\mathcal N(-1,3)$. $(X_1,X_2)\sim\mathcal N\!\left((0,5),\begin{bmatrix}1&0.5\\0.5&2\end{bmatrix}\right)$. Yes: the covariances with $X_3$ are 0, and for Gaussians that means independent.
>
> **A4.** $\dfrac44+\dfrac41=5$, so $d_M=\sqrt5\approx2.24$.

### Part B: core

**B1.** With zero means and $\Sigma=\begin{bmatrix}1&0.8\\0.8&1\end{bmatrix}$, you observe $X_2=1$. Find the conditional mean and variance of $X_1$. Repeat for $X_2=-2$. What changes and what does not?

**B2.** For the same $\Sigma$, compute the Mahalanobis distances of $(1,1)$ and $(1,-1)$. Both are at Euclidean distance $\sqrt2$. Explain the difference using the ellipse.

**B3.** A robot's position estimate is $\mathcal N\!\left((0,0),\begin{bmatrix}0.04&0\\0&0.04\end{bmatrix}\right)$ m². A sensor measures $z=x+\text{noise}$ for the $x$-coordinate only, with noise variance $0.01$, and reads $z=0.1$. Model $(x,z)$ as jointly Gaussian and find the updated mean and variance of $x$. (Hint: $\operatorname{Var}(z)=0.05$, $\operatorname{Cov}(x,z)=0.04$.)

**B4.** Find a $2\times2$ matrix $L$ so that $L z$ with $z\sim\mathcal N(0,I)$ has covariance $\begin{bmatrix}4&2\\2&5\end{bmatrix}$.

**B5.** Demonstrations steer either $-1$ (left) or $+1$ (right) with equal probability, with small noise. A single Gaussian is fitted. What are its mean and (approximately) standard deviation? What fraction of its samples fall between $-0.5$ and $0.5$, where the obstacle is?

> [!success]- Solutions to Part B
> **B1.** Gain $0.8$. $X_2=1$: mean $0.8$, variance $1-0.64=0.36$. $X_2=-2$: mean $-1.6$, variance $0.36$. The mean follows the observation; the variance does not change.
>
> **B2.** $\Sigma^{-1}=\dfrac1{0.36}\begin{bmatrix}1&-0.8\\-0.8&1\end{bmatrix}$. $(1,1)$: $\dfrac{2-1.6}{0.36}\approx1.11$, $d_M\approx1.05$. $(1,-1)$: $\dfrac{2+1.6}{0.36}=10$, $d_M\approx3.16$. The cloud is stretched along $(1,1)$ and thin along $(1,-1)$, so the second point lies across the narrow direction.
>
> **B3.** Gain $0.04/0.05=0.8$. Mean $0+0.8(0.1-0)=0.08$. Variance $0.04-0.04^2/0.05=0.04-0.032=0.008$. The precise sensor (variance 0.01) dominates, so the estimate moves most of the way to the reading. (This is the Kalman update.)
>
> **B4.** Cholesky: $a^2=4$, $a=2$; $ab=2$, $b=1$; $b^2+c^2=5$, $c=2$. $L=\begin{bmatrix}2&0\\1&2\end{bmatrix}$.
>
> **B5.** Mean $0$, standard deviation about $1$. The fraction in $(-0.5,0.5)$ is $P(|Z|<0.5)\approx0.38$: almost 4 in 10 samples drive toward the obstacle, although no demonstration ever did.

### Part C: explain and prove

**C1.** Show that if $\Sigma$ is diagonal, the multivariate Gaussian density is a product of 1-D normal densities.

**C2.** Explain why the conditional covariance $\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$ can never be larger than $\Sigma_{11}$ (in 1-D: never larger as a number).

**C3.** Explain the reparameterization trick in your own words, and why it is needed to train a policy that outputs a mean and standard deviation.

> [!success]- Solutions to Part C
> **C1.** $\det\Sigma=\prod\sigma_i^2$ and the exponent is $\sum(x_i-\mu_i)^2/\sigma_i^2$; $e^{\text{sum}}$ is a product of exponentials, and the constant splits likewise.
>
> **C2.** In 1-D the subtracted term is $\Sigma_{12}^2/\Sigma_{22}\ge0$. In general it is positive semidefinite, so subtracting it can only shrink the uncertainty.
>
> **C3.** Sampling $x\sim\mathcal N(\mu,\sigma^2)$ directly hides how $x$ depends on $\mu,\sigma$. Writing $x=\mu+\sigma z$ with a parameter-free $z$ makes the dependence explicit and differentiable, so backpropagation can adjust $\mu$ and $\sigma$.

### Part D: practise with code

**D1.** Draw 2,000 samples from $\mathcal N\!\left(0,\begin{bmatrix}2&1\\1&2\end{bmatrix}\right)$ and plot them. Overlay the 1- and 2-sigma ellipses using the eigenvectors and eigenvalues. Count the fraction inside each (compare with 39% and 86%).

**D2.** Implement `condition_gaussian(mu, Sigma, idx_obs, x_obs)` returning the conditional mean and covariance. Test it on worked example 7.6.

**D3.** Generate the bimodal steering data of B5 (half from $\mathcal N(-1,0.1^2)$, half from $\mathcal N(1,0.1^2)$), fit a single Gaussian (sample mean and standard deviation), and plot the data histogram with the fitted density.

> [!success]- Hints for D1
> Points on the $k$-sigma ellipse are $\mu+k\,Q\sqrt\Lambda\,(\cos t,\sin t)$ for $t\in[0,2\pi]$, with $Q,\Lambda$ from `np.linalg.eigh`.

---

## Where this is used

- The **Kalman filter** is repeated Gaussian conditioning (B3) and linear transformation (property 1) ([[04 Perception and State]]).
- **Diffusion models** add and remove Gaussian noise ([[08 Diffusion and Flow Matching]]).
- **Gaussian policies** and the reparameterization trick are standard in continuous-control RL ([[Appendix - PPO SAC and Offline Learning]]).
- The mode-averaging problem explains why simple behaviour cloning fails on multimodal demonstrations ([[06 Imitation and Distribution Shift]]).

Next: [[PS 08 Law of Large Numbers and Central Limit Theorem]]: why averages settle down, and how fast.

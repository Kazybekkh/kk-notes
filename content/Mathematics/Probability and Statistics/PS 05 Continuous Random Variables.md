---
type: course-chapter
course: probability-statistics
chapter: 5
tags: [mathematics, probability]
---

# Chapter 5: Continuous random variables

Previous: [[PS 04 Expectation and Variance]] | [[PS 00 Course Map]] | Next: [[PS 06 Joint Distributions and Covariance]]

> [!abstract] The big idea
> A measurement such as a length, a time or a sensor reading can take **any** value in a range, so single values have probability zero and probability must live in **intervals**. A **density** curve describes how probability is spread out, and probability is **area under the curve**. Three continuous distributions cover most needs: uniform, exponential and, above all, the **normal** (Gaussian).

> [!info] In this chapter you will learn to
> 1. Explain why single points have probability zero, and what a density is.
> 2. Compute probabilities, means and variances from a density.
> 3. Use the CDF and quantiles.
> 4. Work with the uniform, exponential and normal distributions.
> 5. Standardize to z-scores and use the standard normal.
> 6. Transform a random variable and generate samples from a distribution.

> [!tip] Before you start
> You need expectation and variance ([[PS 04 Expectation and Variance]]) and basic integration: $\int_a^bx\,dx=\tfrac{b^2-a^2}2$, and the integral as area under a curve.

---

## 5.1 Why points have probability zero

A measured length could be 3.2 cm, 3.21 cm, 3.2137 cm, and so on without end. Between any two values there are infinitely many others.

If each of these infinitely many values had some positive probability, the total would be infinite, breaking the rule that probabilities sum to 1. So for a continuous random variable:

$$
P(X=x)=0\quad\text{for every single value }x.
$$

This is not a paradox. Think of a dart thrown at a board: the chance of hitting **one exact mathematical point** is zero, yet the dart lands somewhere. What has positive probability is landing in a **region**.

So the question is never "what is $P(X=3.2)$?" but "what is $P(3.15\le X\le3.25)$?"

---

## 5.2 Probability density functions

> [!note] Definition: probability density function
> A continuous random variable $X$ has a **density** $p(x)$ if, for all $a\le b$,
> $$
> P(a\le X\le b)=\int_a^bp(x)\,dx.
> $$
> A density satisfies $p(x)\ge0$ and $\displaystyle\int_{-\infty}^\infty p(x)\,dx=1$.

**Probability is area under the density curve.** The total area is 1.

### What the height means

> [!warning] A density is not a probability
> $p(x)$ can be **greater than 1**. The uniform density on $[0,\tfrac12]$ equals 2 on that interval: total area $2\times\tfrac12=1$.
>
> The height is probability **per unit length**. For a tiny interval of width $dx$,
> $$
> P(x\le X\le x+dx)\approx p(x)\,dx.
> $$
> Like a population density (people per square kilometre), it only becomes a count when multiplied by a size.

### Endpoints do not matter

Since single points have probability zero,

$$
P(a\le X\le b)=P(a<X<b)=P(a\le X<b).
$$

This is different from discrete variables, where including an endpoint can matter a lot.

### Expectation and variance

Replace sums with integrals:

$$
\mathbb E[X]=\int x\,p(x)\,dx,\qquad\mathbb E[g(X)]=\int g(x)\,p(x)\,dx,\qquad\operatorname{Var}(X)=\mathbb E[X^2]-(\mathbb E[X])^2.
$$

Everything from chapter 4 carries over: linearity, the variance rules, the square-root law.

### Worked example 5.1: a triangular density

$p(x)=cx$ on $[0,2]$, zero elsewhere.

**Find $c$.** Total area must be 1: $\int_0^2cx\,dx=c\cdot\tfrac{4}{2}=2c=1$, so $c=\tfrac12$.

**A probability.** $P(X\le1)=\int_0^1\tfrac x2\,dx=\tfrac14$. Only a quarter, because the density is low near 0.

**Mean.** $\mathbb E[X]=\int_0^2x\cdot\tfrac x2\,dx=\tfrac12\cdot\tfrac83=\tfrac43$.

**Variance.** $\mathbb E[X^2]=\int_0^2x^2\cdot\tfrac x2\,dx=\tfrac12\cdot\tfrac{16}4=2$. So $\operatorname{Var}=2-\tfrac{16}9=\tfrac29$.

> [!question]- Check yourself
> A density is $p(x)=3x^2$ on $[0,1]$. Find $P(X\le\tfrac12)$ and $\mathbb E[X]$.
>
> **Answer.** $\int_0^{1/2}3x^2\,dx=\tfrac18$. $\mathbb E[X]=\int_0^13x^3\,dx=\tfrac34$.

---

## 5.3 The CDF and quantiles

> [!note] Definition: CDF
> $$
> F(x)=P(X\le x)=\int_{-\infty}^xp(t)\,dt,\qquad p(x)=F'(x).
> $$

Unlike the density, $F(x)$ **is** a probability, always between 0 and 1. It rises from 0 to 1 and never decreases. Interval probabilities are differences:

$$
P(a\le X\le b)=F(b)-F(a).
$$

The **quantile** function runs the CDF backwards: the $q$-quantile is the value $x_q$ with $F(x_q)=q$.

- The **median** is the 0.5 quantile: half the probability below, half above.
- The 0.95 quantile is the value exceeded only 5% of the time.

**Worked example 5.2.** For example 5.1, $F(x)=\int_0^x\tfrac t2\,dt=\tfrac{x^2}4$ on $[0,2]$. Median: $\tfrac{x^2}4=\tfrac12$, so $x=\sqrt2\approx1.41$. That is slightly **above** the mean of $1.33$. The density has a long thin tail toward 0, which pulls the mean down more than the median. (A tail on one side always drags the mean toward it.)

---

## 5.4 The uniform distribution

> [!note] Uniform($a,b$)
> Every value in $[a,b]$ is equally dense:
> $$
> p(x)=\frac1{b-a}\text{ on }[a,b],\qquad\mathbb E[X]=\frac{a+b}2,\qquad\operatorname{Var}(X)=\frac{(b-a)^2}{12}.
> $$

The probability of a sub-interval is its **length divided by** $b-a$.

**Worked example 5.3.** A bus arrives uniformly at random within a 10-minute window. $P(\text{wait}\le3\text{ min})=3/10$. Mean wait 5 minutes, standard deviation $10/\sqrt{12}\approx2.89$ minutes.

**Why it matters:** computer random number generators produce Uniform(0,1) numbers, and every other distribution is built from them (section 5.8).

**Quantization noise.** Rounding a measurement to the nearest unit adds an error roughly uniform on $[-\tfrac12,\tfrac12]$, with standard deviation $1/\sqrt{12}\approx0.29$ units. That is the noise floor of any digital sensor.

---

## 5.5 The exponential distribution

> [!note] Exponential($\lambda$)
> The waiting time until an event that occurs at constant rate $\lambda$:
> $$
> p(x)=\lambda e^{-\lambda x}\ (x\ge0),\qquad F(x)=1-e^{-\lambda x},\qquad P(X>x)=e^{-\lambda x},
> $$
> $$
> \mathbb E[X]=\frac1\lambda,\qquad\operatorname{Var}(X)=\frac1{\lambda^2}.
> $$

It is the continuous cousin of the geometric distribution, and it is **memoryless** in the same way:

$$
P(X>s+t\mid X>s)=\frac{e^{-\lambda(s+t)}}{e^{-\lambda s}}=e^{-\lambda t}=P(X>t).
$$

A component with exponential lifetime does not "wear out": if it has survived 1,000 hours, it is as good as new. (Real components often do wear out, so this is a modelling assumption to check.)

**Link with Poisson.** If events arrive as a Poisson process with rate $\lambda$ per hour (chapter 3), the waiting times between them are Exponential($\lambda$).

**Worked example 5.4.** Faults occur at 2 per hour.

- $P(\text{no fault in the next 30 min})=e^{-2\times0.5}=e^{-1}\approx0.368$.
- Mean time between faults: $0.5$ hours.
- Median time between faults: $1-e^{-2x}=0.5$ gives $x=\ln2/2\approx0.347$ hours. Smaller than the mean, because the distribution has a long right tail.

---

## 5.6 The normal (Gaussian) distribution

### The formula

> [!note] Normal($\mu,\sigma^2$)
> $$
> p(x)=\frac1{\sigma\sqrt{2\pi}}\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right).
> $$
> Mean $\mu$, variance $\sigma^2$. Written $X\sim\mathcal N(\mu,\sigma^2)$.

### Reading the formula, piece by piece

1. $\dfrac{x-\mu}{\sigma}$: how far $x$ is from the mean, **measured in standard deviations**.
2. Squaring it: distance in either direction counts the same, so the curve is **symmetric**.
3. $\exp(-\tfrac12\cdot\text{that})$: the density falls off **very fast** as you move away. At $1\sigma$ it is $e^{-1/2}\approx0.61$ of the peak; at $2\sigma$, $e^{-2}\approx0.14$; at $3\sigma$, $e^{-4.5}\approx0.011$.
4. $\dfrac1{\sigma\sqrt{2\pi}}$: the constant that makes the total area 1. A wider curve (larger $\sigma$) must be lower.

The result is the familiar **bell curve**: a single peak at $\mu$, symmetric, with width set by $\sigma$.

### The 68-95-99.7 rule

| Within | Probability |
|---|---|
| $\mu\pm1\sigma$ | about 68% |
| $\mu\pm2\sigma$ | about 95% |
| $\mu\pm3\sigma$ | about 99.7% |

The exact multiplier for 95% is **1.96**. That number reappears constantly in statistics ([[PS 10 Confidence Intervals and Hypothesis Tests]]).

### Standardizing: z-scores

> [!important] Standardization
> If $X\sim\mathcal N(\mu,\sigma^2)$, then
> $$
> Z=\frac{X-\mu}\sigma\sim\mathcal N(0,1),
> $$
> the **standard normal**. Its CDF is written $\Phi(z)=P(Z\le z)$.

So **one table** (or one function) answers questions about every normal distribution. The **z-score** $z=(x-\mu)/\sigma$ says how many standard deviations $x$ is from the mean.

Useful values of $\Phi$:

| $z$ | 0 | 0.5 | 1 | 1.5 | 1.645 | 1.96 | 2 | 2.5 | 3 |
|---|---|---|---|---|---|---|---|---|---|
| $\Phi(z)$ | 0.500 | 0.691 | 0.841 | 0.933 | 0.950 | 0.975 | 0.977 | 0.994 | 0.9987 |

By symmetry, $\Phi(-z)=1-\Phi(z)$.

### Worked example 5.5

Adult heights are $\mathcal N(170,10^2)$ cm.

**$P(\text{height}>185)$.** $z=\dfrac{185-170}{10}=1.5$. $P=1-\Phi(1.5)=1-0.933=0.067$.

**$P(160<\text{height}<180)$.** $z$ from $-1$ to $1$: $\Phi(1)-\Phi(-1)=0.841-0.159=0.682$.

**The height exceeded by only 5%.** Need $\Phi(z)=0.95$, so $z=1.645$, and height $=170+1.645\times10\approx186.5$ cm.

### Why the normal is everywhere

1. **Sums of many small independent effects** are approximately normal (the central limit theorem, [[PS 08 Law of Large Numbers and Central Limit Theorem]]). Measurement noise is typically such a sum.
2. **Linear combinations of independent normals are normal:**
$$
aX+bY\sim\mathcal N\big(a\mu_X+b\mu_Y,\;a^2\sigma_X^2+b^2\sigma_Y^2\big).
$$
3. **Its log-density is a quadratic**, so maximizing a Gaussian likelihood is minimizing squared error ([[PS 09 Estimation and Maximum Likelihood]]).

### Its limits

> [!warning] Thin tails
> The normal assigns tiny probabilities to extreme values: about 1 in 3.5 million beyond $5\sigma$ on one side. Real data (financial returns, sensor glitches, human errors) often has **outliers far more often**. A model that assumes normal noise will be badly misled by them. Always look at a histogram before assuming normality.

> [!question]- Check yourself
> $X\sim\mathcal N(50,5^2)$. Find $P(X<40)$ and $P(45<X<60)$.
>
> **Answer.** $z=-2$: $1-0.977=0.023$. $z$ from $-1$ to $2$: $0.977-0.159=0.818$.

---

## 5.7 Transforming a random variable

If $Y=g(X)$ for an increasing, smooth function $g$, how is $Y$ distributed?

**Method 1: through the CDF (always works).**

$$
F_Y(y)=P(g(X)\le y)=P(X\le g^{-1}(y))=F_X(g^{-1}(y)).
$$

Differentiate to get the density.

**Method 2: the change-of-variables formula.**

$$
p_Y(y)=p_X(x)\left|\frac{dx}{dy}\right|,\qquad x=g^{-1}(y).
$$

**Why the factor $|dx/dy|$?** Probability in a tiny interval must be preserved: $p_Y(y)\,dy=p_X(x)\,dx$. If $g$ stretches the axis, the same probability is spread over a longer interval, so the density must drop.

**Worked example 5.6.** $X\sim$ Uniform(0,1) and $Y=X^2$. Then $x=\sqrt y$, $dx/dy=\tfrac1{2\sqrt y}$, so

$$
p_Y(y)=1\cdot\frac1{2\sqrt y},\qquad0<y<1.
$$

Squaring pushes values toward 0 (since $0.5^2=0.25$), so the density piles up near 0.

In several dimensions the factor becomes the absolute determinant of the Jacobian ([[LA 07 Determinants]]). This is exactly how **normalizing flows** compute densities.

---

## 5.8 Generating samples

### Inverse transform sampling

> [!important] Inverse transform method
> If $U\sim$ Uniform(0,1) and $F$ is a CDF, then $X=F^{-1}(U)$ has CDF $F$.

*Why:* $P(X\le x)=P(F^{-1}(U)\le x)=P(U\le F(x))=F(x)$.

**Worked example 5.7: exponential samples.** $F(x)=1-e^{-\lambda x}$. Solve $u=1-e^{-\lambda x}$: $x=-\dfrac{\ln(1-u)}\lambda$. So `x = -np.log(1 - rng.random()) / lam` produces exponential samples from uniform ones.

**Normal samples** are generated by other tricks (Box-Muller, or library routines), since $\Phi^{-1}$ has no simple formula. To get $\mathcal N(\mu,\sigma^2)$ from standard normal $Z$: $X=\mu+\sigma Z$.

---

## Summary

| Distribution | Density | Mean | Variance |
|---|---|---|---|
| Uniform($a,b$) | $\dfrac1{b-a}$ | $\dfrac{a+b}2$ | $\dfrac{(b-a)^2}{12}$ |
| Exponential($\lambda$) | $\lambda e^{-\lambda x}$ | $\dfrac1\lambda$ | $\dfrac1{\lambda^2}$ |
| Normal($\mu,\sigma^2$) | $\dfrac1{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$ | $\mu$ | $\sigma^2$ |

**Three facts to remember:**

1. Probability is area under the density; the height alone is not a probability.
2. Standardize with $z=(x-\mu)/\sigma$; 68-95-99.7 within 1, 2, 3 standard deviations.
3. Transforming a variable rescales its density by $|dx/dy|$.

---

## Exercises

### Part A: warm-up

**A1.** $X\sim$ Uniform(2,10). Find $P(3\le X\le5)$, the mean and the variance.

**A2.** A density is $p(x)=k(1-x)$ on $[0,1]$. Find $k$, $P(X\le\tfrac12)$ and $\mathbb E[X]$.

**A3.** $X\sim\mathcal N(100,15^2)$. Find $P(X>130)$ and $P(85<X<115)$.

**A4.** A component's lifetime is exponential with mean 1000 hours. Find $P(\text{survives 2000 hours})$ and the median lifetime.

> [!success]- Solutions to Part A
> **A1.** $2/8=0.25$. Mean $6$. Variance $64/12\approx5.33$.
>
> **A2.** $\int_0^1k(1-x)dx=k/2=1$, so $k=2$. $P(X\le\tfrac12)=\int_0^{1/2}2(1-x)dx=1-\tfrac14=\tfrac34$. $\mathbb E[X]=\int_0^12x(1-x)dx=2(\tfrac12-\tfrac13)=\tfrac13$.
>
> **A3.** $z=2$: $0.023$. $z$ from $-1$ to $1$: $0.683$.
>
> **A4.** $\lambda=0.001$. $e^{-2}\approx0.135$. Median $\ln2/0.001\approx693$ hours.

### Part B: core

**B1.** Exam scores are $\mathcal N(65,10^2)$. What score is needed to be in the top 10%? ($\Phi(1.28)\approx0.90$.)

**B2.** Two independent measurements of a length are $\mathcal N(\mu,4)$ and $\mathcal N(\mu,9)$ (variances in mm²). Their average $\tfrac12(X_1+X_2)$ has what variance? Is a weighted average $wX_1+(1-w)X_2$ better? Find the $w$ that minimizes the variance.

**B3.** A robot's position error in one axis is $\mathcal N(0,\,2^2)$ mm. The task tolerates errors up to 5 mm. What fraction of attempts are within tolerance? How small must $\sigma$ be for 99.7% to be within tolerance?

**B4.** $X\sim$ Uniform(0,1). Find the density of $Y=-\ln X$. Which distribution is it?

**B5.** Show that the median of Exponential($\lambda$) is $\ln2/\lambda$, and explain why it is less than the mean.

> [!success]- Solutions to Part B
> **B1.** $65+1.28\times10=77.8$.
>
> **B2.** Equal average: $\tfrac14(4+9)=3.25$. Weighted: $w^2\cdot4+(1-w)^2\cdot9$. Derivative $8w-18(1-w)=0$ gives $w=18/26\approx0.692$, variance $\approx0.479\cdot4+0.095\cdot9\approx2.77$. Better: give more weight to the more precise measurement (weights proportional to $1/\text{variance}$). This is the idea behind sensor fusion.
>
> **B3.** $z=5/2=2.5$: $P(|Z|<2.5)=2(0.994)-1\approx0.988$. For 99.7% we need $5\ge3\sigma$, so $\sigma\le1.67$ mm.
>
> **B4.** $y=-\ln x$, $x=e^{-y}$, $|dx/dy|=e^{-y}$. Density $1\cdot e^{-y}$ for $y>0$: Exponential(1). (This is inverse transform sampling in disguise.)
>
> **B5.** $1-e^{-\lambda m}=\tfrac12$ gives $m=\ln2/\lambda\approx0.69/\lambda$, less than $1/\lambda$. A few very long waits pull the mean up, but not the median.

### Part C: explain and prove

**C1.** Prove that for Uniform($a,b$), $\operatorname{Var}(X)=(b-a)^2/12$.

**C2.** Prove the memoryless property of the exponential distribution.

**C3.** Explain why a density value of 3 at some point does not contradict the axioms.

**C4.** Show that if $X\sim\mathcal N(\mu,\sigma^2)$ then $aX+b\sim\mathcal N(a\mu+b,\,a^2\sigma^2)$, using the change-of-variables formula.

> [!success]- Solutions to Part C
> **C1.** For Uniform(0,1): $\mathbb E[X^2]=\tfrac13$, $\mathbb E[X]=\tfrac12$, variance $\tfrac13-\tfrac14=\tfrac1{12}$. Uniform($a,b$) is $a+(b-a)U$, so by scaling the variance is $(b-a)^2/12$.
>
> **C2.** Shown in section 5.5.
>
> **C3.** Axioms constrain probabilities, which are areas. A height of 3 over an interval narrower than $1/3$ contributes area less than 1.
>
> **C4.** For $a>0$: $y=ax+b$, $x=(y-b)/a$, $|dx/dy|=1/a$. Substituting into the normal density gives $\dfrac1{a\sigma\sqrt{2\pi}}\exp\!\left(-\dfrac{(y-b-a\mu)^2}{2a^2\sigma^2}\right)$, the $\mathcal N(a\mu+b,a^2\sigma^2)$ density.

### Part D: practise with code

**D1.** Draw 100,000 samples from $\mathcal N(0,1)$ and check the 68-95-99.7 fractions.

**D2.** Generate exponential samples by inverse transform from uniform samples, and compare their histogram with the density $\lambda e^{-\lambda x}$.

**D3.** Use `scipy.stats.norm.cdf` and `norm.ppf` to reproduce the table of $\Phi$ values and the answer to B1.

**D4.** Simulate $Y=X^2$ for $X\sim$ Uniform(0,1) and compare the histogram with $1/(2\sqrt y)$.

---

## Where this is used

- **Sensor noise** is usually modelled as Gaussian ([[04 Perception and State]]).
- **Diffusion models** start from Gaussian noise and learn to reverse it ([[08 Diffusion and Flow Matching]]).
- **Gaussian policies** output a mean and a standard deviation for each action dimension ([[Appendix - PPO SAC and Offline Learning]]).
- **Domain randomization** samples simulation parameters from uniform ranges.

Next: [[PS 06 Joint Distributions and Covariance]]: two random quantities at once.

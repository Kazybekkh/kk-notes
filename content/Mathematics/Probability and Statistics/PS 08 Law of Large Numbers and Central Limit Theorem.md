---
type: course-chapter
course: probability-statistics
chapter: 8
tags: [mathematics, probability, statistics]
---

# Chapter 8: The law of large numbers and the central limit theorem

Previous: [[PS 07 The Multivariate Gaussian]] | [[PS 00 Course Map]] | Next: [[PS 09 Estimation and Maximum Likelihood]]

> [!abstract] The big idea
> Two theorems explain why data tells you anything at all. The **law of large numbers** says that the average of many independent samples settles down to the true mean. The **central limit theorem** says that the remaining random error of that average is approximately **normal**, with size $\sigma/\sqrt n$, **whatever the original distribution looked like**. Together they are the bridge from probability (models to data) to statistics (data to models).

> [!info] In this chapter you will learn to
> 1. Treat a sample average as a random variable with its own mean and spread.
> 2. State the law of large numbers, prove a version of it, and avoid the gambler's fallacy.
> 3. State the central limit theorem and use it to approximate probabilities about averages and sums.
> 4. Compute standard errors for means and for proportions.
> 5. Judge how large $n$ must be, and recognize when the theorems fail.

> [!tip] Before you start
> You need the square-root law and Chebyshev's inequality ([[PS 04 Expectation and Variance]]) and normal probabilities with z-scores ([[PS 05 Continuous Random Variables]]).

---

## 8.1 The sample average is a random variable

### Setup

Let $X_1,X_2,\dots,X_n$ be **i.i.d.**: **i**ndependent and **i**dentically **d**istributed. Each has the same mean $\mu$ and variance $\sigma^2$. Think of $n$ repeated measurements, $n$ robot trials, or $n$ data points.

> [!note] Definition: sample mean
> $$
> \bar X_n=\frac1n\sum_{i=1}^nX_i.
> $$

**Key mental shift.** $\bar X_n$ is itself **random**. Run the whole experiment again and you get a different set of samples, hence a different average. So $\bar X_n$ has its own distribution, called its **sampling distribution**.

From chapter 4:

$$
\mathbb E[\bar X_n]=\mu,\qquad\operatorname{Var}(\bar X_n)=\frac{\sigma^2}n,\qquad\operatorname{sd}(\bar X_n)=\frac\sigma{\sqrt n}.
$$

The average is centred on the truth, and its spread shrinks as $n$ grows. The two theorems describe what happens in the limit.

---

## 8.2 The law of large numbers

> [!important] Law of large numbers (weak form)
> For any tolerance $\varepsilon>0$,
> $$
> P\big(|\bar X_n-\mu|>\varepsilon\big)\longrightarrow0\quad\text{as }n\to\infty.
> $$
> The sample average converges to the true mean.

### Proof (it is short)

Apply Chebyshev's inequality ([[PS 04 Expectation and Variance]]) to $\bar X_n$, whose variance is $\sigma^2/n$:

$$
P\big(|\bar X_n-\mu|>\varepsilon\big)\le\frac{\operatorname{Var}(\bar X_n)}{\varepsilon^2}=\frac{\sigma^2}{n\varepsilon^2}.
$$

The right side goes to 0 as $n\to\infty$. $\blacksquare$

The bound also says **how many** samples are enough. To be within $\varepsilon=0.1$ of the mean with probability at least 95%, when $\sigma=1$: need $\dfrac1{n(0.01)}\le0.05$, so $n\ge2000$. (Chebyshev is pessimistic; the CLT below gives a much smaller number.)

### What it means

- **Frequencies settle to probabilities.** The fraction of heads in many fair flips approaches 0.5. This is what justifies the frequentist reading of probability.
- **Monte Carlo estimation.** To estimate an expectation you cannot compute exactly, draw samples and average:
$$
\mathbb E[g(X)]\approx\frac1n\sum_{i=1}^ng(x_i).
$$
Reinforcement learning estimates expected returns this way; training estimates the expected loss this way.

### What it does not mean: the gambler's fallacy

> [!warning] Deficits are diluted, not repaid
> After 10 tails in a row, the next flip of a fair coin is still 50/50. The law of large numbers does **not** work by producing extra heads to "make up" for the tails.
>
> It works by **dilution**. After 10 tails and then 1,000 more fair flips, the fraction of heads is about $\tfrac{500}{1010}\approx0.495$: close to 0.5, because the early streak is now a tiny part of the total. In fact the **absolute** difference between heads and tails typically **grows**, like $\sqrt n$. Only the **fraction** converges.

> [!question]- Check yourself
> A fair coin has shown 7 heads in the first 10 flips. What is the expected number of heads after 1,000 flips in total?
>
> **Answer.** $7+0.5\times990=502$. The early excess of 2 is not cancelled; it is diluted. The fraction is $0.502$.

---

## 8.3 The central limit theorem

### The statement

The law of large numbers says where $\bar X_n$ goes. The central limit theorem (CLT) describes the **shape** of its fluctuations around that limit.

> [!important] Central limit theorem
> If $X_1,\dots,X_n$ are i.i.d. with mean $\mu$ and finite variance $\sigma^2$, then for large $n$
> $$
> \frac{\bar X_n-\mu}{\sigma/\sqrt n}\;\approx\;\mathcal N(0,1),
> $$
> or equivalently
> $$
> \bar X_n\approx\mathcal N\!\left(\mu,\;\frac{\sigma^2}n\right),\qquad\sum_{i=1}^nX_i\approx\mathcal N(n\mu,\;n\sigma^2).
> $$

### Why it is astonishing

**The shape of the original distribution does not matter.** The $X_i$ can be coin flips (two values), dice (flat), exponential waiting times (very skewed): their averages all become bell-shaped. Only the mean and variance survive.

### Why it happens (intuition)

Consider the sum of dice:

- **One die**: flat, every value from 1 to 6 equally likely.
- **Two dice**: a triangle peaking at 7 (chapter 1). Middle sums can be made in more ways.
- **Five dice**: already looks like a bell.

Extreme totals need **every** die to be extreme in the same direction, which is rare. Middle totals can be reached in a huge number of ways. As more independent pieces are added, this effect overwhelms the shape of any single piece.

### Standard error

> [!note] Definition: standard error
> The **standard error** of the mean is
> $$
> \operatorname{SE}=\frac{\sigma}{\sqrt n}.
> $$
> It is the standard deviation of the **estimate** $\bar X_n$, as opposed to $\sigma$, the standard deviation of the **data**.

Mixing these two up is a very common error. The data stays just as spread out no matter how much you collect; the **estimate of its mean** becomes more precise.

---

## 8.4 Worked examples

### Worked example 8.1: averaging sensor readings

A sensor reading has mean 20 and standard deviation 4. You average 64 independent readings. What is $P(\bar X>21)$?

**Step 1: standard error.** $4/\sqrt{64}=0.5$.

**Step 2: CLT.** $\bar X\approx\mathcal N(20,0.5^2)$.

**Step 3: standardize.** $z=\dfrac{21-20}{0.5}=2$.

**Step 4: probability.** $P(Z>2)\approx1-0.977=0.023$.

A single reading exceeds 21 quite often (about 40% of the time, if readings are roughly normal: $z=0.25$). The average of 64 almost never does.

### Worked example 8.2: sum of dice

Roll 100 dice. $P(\text{total}>370)$?

Each die: $\mu=3.5$, $\sigma^2\approx2.917$. Total: mean $350$, variance $291.7$, sd $\approx17.1$.

$$
z\approx\frac{370-350}{17.1}\approx1.17,\qquad P\approx1-0.879=0.121.
$$

(A **continuity correction**, using 370.5 for a discrete total, gives $z\approx1.20$ and $P\approx0.115$, slightly more accurate.)

### Worked example 8.3: exponential waiting times

Task times are exponential with mean 30 s (so $\sigma=30$ s too: very skewed). The average of 36 tasks:

$$
\operatorname{SE}=30/6=5,\qquad\bar X\approx\mathcal N(30,5^2).
$$

$P(\bar X>40)\approx P(Z>2)=0.023$. Even though individual times are strongly skewed, their average is close to normal.

---

## 8.5 Proportions

### The setup

Each trial succeeds with probability $p$. The observed success rate in $n$ trials is

$$
\hat p=\frac{\text{successes}}n,
$$

an average of $n$ Bernoulli variables, each with variance $p(1-p)$.

> [!important] Sampling distribution of a proportion
> $$
> \hat p\approx\mathcal N\!\left(p,\;\frac{p(1-p)}n\right),\qquad\operatorname{SE}(\hat p)=\sqrt{\frac{p(1-p)}n}.
> $$

### Worked example 8.4: how precise is a success rate?

$p=0.5$, $n=100$: $\operatorname{SE}=\sqrt{0.25/100}=0.05$. About 95% of the time, $\hat p$ lands within $\pm2\times0.05=\pm0.10$ of the truth.

**Consequence.** A policy measured at 55% over 100 trials is **indistinguishable** from one at 50%. The difference is within ordinary noise.

### How many trials do you need?

For a standard error of $e$, solve $\sqrt{p(1-p)/n}=e$:

$$
n=\frac{p(1-p)}{e^2}\le\frac{0.25}{e^2}.
$$

| Desired SE | 0.10 | 0.05 | 0.02 | 0.01 |
|---|---|---|---|---|
| $n$ (worst case $p=0.5$) | 25 | 100 | 625 | 2500 |

This is why opinion polls use about 1,000 to 2,500 people, and why a robot evaluation with 10 or 20 trials can only detect **large** differences between policies.

---

## 8.6 How large is "large $n$"?

There is no single answer. Rules of thumb:

- If the underlying distribution is **roughly symmetric**, $n\approx10$ can already be fine.
- A common general rule is $n\ge30$.
- For **proportions**, require at least about 10 expected successes **and** 10 expected failures: $np\ge10$ and $n(1-p)\ge10$.
- For **strongly skewed** or **heavy-tailed** data, much larger $n$ may be needed.

When in doubt, **simulate**: draw many samples of size $n$ from a plausible distribution and look at the histogram of their averages.

---

## 8.7 When the theorems fail

Both theorems assume **independent** samples, from **the same** distribution, with **finite variance**.

### Dependence

Samples from the same robot episode, consecutive video frames, or many measurements of one object are **correlated**. Correlated errors do not cancel the way independent ones do ([[PS 06 Joint Distributions and Covariance]], exercise C4). The true uncertainty is larger than $\sigma/\sqrt n$, sometimes much larger.

> [!warning] Count independent units, not rows
> 10 robot episodes of 1,000 frames each is closer to **10** independent samples than to 10,000 for questions about task success. Treating it as 10,000 makes error bars about 30 times too small.

### Changing distribution

If the process **drifts** (a motor warms up, lighting changes, a policy is being trained), the samples are not identically distributed. The average tracks a moving target and may not mean anything simple.

### Infinite variance

Some distributions have such heavy tails that their variance is infinite (the Cauchy distribution is the standard example). Then averaging does **not** reduce noise: one enormous value can dominate any average, however large $n$ is. Real data with occasional extreme outliers can behave similarly in practice.

---

## Summary

| Idea | Fact |
|---|---|
| sample mean | random, with mean $\mu$ and sd $\sigma/\sqrt n$ |
| LLN | $\bar X_n\to\mu$ |
| CLT | $\bar X_n\approx\mathcal N(\mu,\sigma^2/n)$ for any shape |
| standard error | $\sigma/\sqrt n$ (spread of the estimate, not the data) |
| proportion | $\operatorname{SE}=\sqrt{p(1-p)/n}$ |
| required $n$ | $n\approx0.25/e^2$ for SE $e$ |

**Three facts to remember:**

1. Averages converge to the mean by diluting early luck, not by correcting it.
2. Averages are approximately normal with standard error $\sigma/\sqrt n$.
3. Count independent units; correlated samples overstate how much you know.

---

## Exercises

### Part A: warm-up

**A1.** Data has $\sigma=12$. What is the standard error of the mean for $n=36$? For $n=144$?

**A2.** A fair coin is flipped 400 times. Give an interval that contains the number of heads about 95% of the time.

**A3.** A policy's true success rate is 0.8. In 25 trials, what is the standard error of the observed rate?

**A4.** How many trials are needed to estimate a success rate near 0.9 with a standard error of 0.03?

> [!success]- Solutions to Part A
> **A1.** $12/6=2$ and $12/12=1$.
>
> **A2.** Mean 200, sd $\sqrt{400\times0.25}=10$. About $200\pm20$: 180 to 220.
>
> **A3.** $\sqrt{0.8\times0.2/25}=0.08$.
>
> **A4.** $n=0.9\times0.1/0.03^2=100$.

### Part B: core

**B1.** A robot's cycle time has mean 12 s and standard deviation 3 s. Over 100 cycles, what is the probability the total time exceeds 1,250 s?

**B2.** Two policies are evaluated on 50 independent trials each. A truly succeeds 70% of the time, B 60%. Approximately what is the probability that B's observed rate is **higher** than A's? (Hint: the difference $\hat p_A-\hat p_B$ is approximately normal; find its mean and standard deviation.)

**B3.** An election poll of 1,000 people finds 52% support. Is this convincing evidence of majority support? Use the standard error.

**B4.** Explain why the following claim is wrong: "My dataset has 50,000 frames from 20 demonstrations, so the standard error of my success estimate is tiny."

**B5.** Use Chebyshev to find how many samples guarantee $P(|\bar X-\mu|>0.5)\le0.01$ when $\sigma=2$. Then use the CLT to estimate the number needed. Compare.

> [!success]- Solutions to Part B
> **B1.** Total: mean 1,200, sd $3\times10=30$. $z=50/30\approx1.67$, probability $\approx0.048$.
>
> **B2.** Mean difference $0.10$. sd $\sqrt{0.21/50+0.24/50}=\sqrt{0.009}\approx0.095$. $P(\text{diff}<0)=P(Z<-1.05)\approx0.15$. About 15% of the time, the worse policy looks better.
>
> **B3.** SE $=\sqrt{0.25/1000}\approx0.016$. 52% is about $1.26$ SE above 50%, well within normal noise. Not convincing.
>
> **B4.** The frames within a demonstration are highly correlated; task success is decided per demonstration. The effective sample size is about 20, not 50,000.
>
> **B5.** Chebyshev: $\dfrac{4}{n(0.25)}\le0.01$ gives $n\ge1600$. CLT: need $0.5\ge2.576\times2/\sqrt n$, so $\sqrt n\ge10.3$ and $n\ge107$. Chebyshev is about 15 times more conservative, because it must hold for every distribution.

### Part C: explain and prove

**C1.** Prove that $\operatorname{Var}(\bar X_n)=\sigma^2/n$ for independent samples. Where exactly is independence used?

**C2.** Explain, using the formula for the variance of a sum with covariance, why positively correlated samples make $\operatorname{Var}(\bar X_n)$ larger than $\sigma^2/n$.

**C3.** Explain the difference between "the standard deviation of the data" and "the standard error of the mean" to a friend, with an example.

> [!success]- Solutions to Part C
> **C1.** $\operatorname{Var}(\sum X_i)=\sum\operatorname{Var}(X_i)=n\sigma^2$ requires all covariances to be zero, which is where independence is used. Dividing by $n^2$ gives $\sigma^2/n$.
>
> **C2.** $\operatorname{Var}(\sum X_i)=n\sigma^2+\sum_{i\neq j}\operatorname{Cov}(X_i,X_j)$. Positive covariances add extra variance that does not shrink with averaging.
>
> **C3.** Adult heights have a standard deviation of about 10 cm whatever the sample size: people genuinely differ. But the average height of 10,000 randomly chosen adults has a standard error of $10/100=0.1$ cm: the **estimate** of the population average is very precise.

### Part D: practise with code

**D1.** For dice, plot histograms of the average of $n=1,2,5,30$ dice (10,000 repetitions each). Watch the bell shape appear.

**D2.** Repeat D1 with exponential samples (`rng.exponential(1, ...)`), which are strongly skewed. How large must $n$ be before the histogram looks symmetric?

**D3.** Simulate 10 tails followed by 10,000 fair flips. Plot the running fraction of heads and the running difference (heads minus tails). One converges; one does not.

**D4.** Simulate averages of Cauchy samples (`rng.standard_cauchy`) for $n=10,100,1000,10000$. Do they settle down?

> [!success]- Hints for Part D
> **D2.** Around $n=30$ the shape is close to symmetric, later than for dice.
>
> **D4.** No. The running average keeps jumping, because occasional enormous values dominate. That is what infinite variance looks like.

---

## Where this is used

- **Monte Carlo returns** in reinforcement learning are sample averages ([[09 Reinforcement Learning]]).
- **Mini-batch gradients** are sample averages of per-example gradients, with noise shrinking like $1/\sqrt{\text{batch size}}$ ([[05 Training Neural Policies]]).
- **Every evaluation table** reports sample averages, and should report their standard errors ([[16 Evaluation and Uncertainty]]).

Next: [[PS 09 Estimation and Maximum Likelihood]]: turning data into fitted models.

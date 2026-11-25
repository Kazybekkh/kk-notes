---
type: course-chapter
course: probability-statistics
chapter: 11
tags: [mathematics, statistics, bayes]
---

# Chapter 11: Bayesian inference

Previous: [[PS 10 Confidence Intervals and Hypothesis Tests]] | [[PS 00 Course Map]] | Next: [[PS 12 Markov Chains and Information]]

> [!abstract] The big idea
> Bayesian inference treats an unknown parameter as a **random variable** that describes your knowledge. You start with a **prior** distribution, observe data, and use Bayes' rule to get a **posterior** distribution. The posterior states exactly what is still plausible and how uncertain you are, it improves smoothly as data arrives, and it gives sensible answers even with very little data. Regularization, Kalman filtering and uncertainty-aware robots all come from this one idea.

> [!info] In this chapter you will learn to
> 1. Write posterior ∝ likelihood × prior, and explain each part.
> 2. Update a Beta prior with success/failure data, and a Gaussian prior with a measurement.
> 3. Interpret the posterior mean as a weighted compromise between prior and data.
> 4. Summarize a posterior with its mean, mode (MAP) and a credible interval.
> 5. Show that MAP estimation with a Gaussian prior is L2-regularized maximum likelihood.
> 6. Make predictions that account for parameter uncertainty, and distinguish two kinds of uncertainty.

> [!tip] Before you start
> You need Bayes' rule ([[PS 02 Conditional Probability and Bayes Rule]]), likelihoods and MLE ([[PS 09 Estimation and Maximum Likelihood]]), and confidence intervals ([[PS 10 Confidence Intervals and Hypothesis Tests]]) for comparison.

---

## 11.1 The Bayesian idea

### Uncertainty about a parameter

In chapter 9, the parameter $\theta$ was a fixed unknown number and the answer was a single best guess. Here we describe our **knowledge** of $\theta$ with a probability distribution:

- Values we consider plausible get high probability.
- Values we consider implausible get low probability.

After seeing data, we update that distribution.

### Bayes' rule for parameters

> [!important] Bayesian updating
> $$
> \underbrace{p(\theta\mid D)}_{\text{posterior}}=\frac{\overbrace{p(D\mid\theta)}^{\text{likelihood}}\;\overbrace{p(\theta)}^{\text{prior}}}{\underbrace{p(D)}_{\text{evidence}}}.
> $$
> Usually written
> $$
> \text{posterior}\;\propto\;\text{likelihood}\times\text{prior}.
> $$

This is exactly Bayes' rule from chapter 2, with the hypothesis now a continuous parameter.

| Part | What it is |
|---|---|
| **prior** $p(\theta)$ | what you believe about $\theta$ before the data |
| **likelihood** $p(D\mid\theta)$ | how probable the data is for each $\theta$ (chapter 9) |
| **posterior** $p(\theta\mid D)$ | what you believe after the data |
| **evidence** $p(D)=\int p(D\mid\theta)p(\theta)\,d\theta$ | a constant that makes the posterior integrate to 1 |

Since the evidence does not depend on $\theta$, you can usually ignore it while working out the **shape** of the posterior, then normalize at the end.

### A picture

Plot the prior and the likelihood as curves over $\theta$. **Multiply them point by point.** Where both are high, the posterior is high; where either is near zero, the posterior is near zero. The posterior always sits between the two, pulled toward whichever is **narrower** (more informative).

---

## 11.2 Estimating a success rate: the Beta-Binomial model

### The prior: the Beta distribution

For an unknown probability $\theta\in[0,1]$, a convenient prior is the **Beta distribution**:

> [!note] Beta($a,b$)
> $$
> p(\theta)\propto\theta^{a-1}(1-\theta)^{b-1},\qquad0\le\theta\le1,
> $$
> $$
> \mathbb E[\theta]=\frac a{a+b},\qquad\text{mode}=\frac{a-1}{a+b-2}\;(a,b>1).
> $$

**Interpreting $a$ and $b$.** Think of $a-1$ as imaginary prior **successes** and $b-1$ as imaginary prior **failures**. The bigger $a+b$, the more confident the prior.

| Prior | Shape | Meaning |
|---|---|---|
| Beta(1,1) | flat | no preference: every $\theta$ equally plausible |
| Beta(2,2) | gentle hump at 0.5 | mild belief it is near 0.5 |
| Beta(8,2) | peaked near 0.8 | fairly confident it is high |
| Beta(50,50) | sharp spike at 0.5 | very confident it is 0.5 |

### The update

Observe $k$ successes in $n$ trials. The likelihood is $\theta^k(1-\theta)^{n-k}$. Multiply by the prior:

$$
p(\theta\mid D)\propto\theta^k(1-\theta)^{n-k}\cdot\theta^{a-1}(1-\theta)^{b-1}=\theta^{a+k-1}(1-\theta)^{b+n-k-1}.
$$

> [!important] Beta-Binomial update
> $$
> \text{Beta}(a,b)\;\xrightarrow{\;k\text{ successes},\;n-k\text{ failures}\;}\;\text{Beta}(a+k,\;b+n-k).
> $$
> **Updating is just adding counts.**

When the posterior has the same family as the prior, the prior is called **conjugate**. Conjugate pairs make the algebra trivial.

### Worked example 11.1: very little data

Flat prior Beta(1,1). A new policy succeeds in **3 of 3** trials.

- Posterior: Beta(4,1).
- Posterior mean: $4/5=0.8$.
- Compare MLE: $3/3=1$, a claim that the policy **never** fails.

The Bayesian answer is far more sensible. And the posterior is a full distribution: Beta(4,1) puts substantial probability on rates from about 0.4 to 1. A 95% credible interval is roughly $[0.40,\;0.99]$. Three successes simply cannot tell you much.

### Worked example 11.2: more data

Same flat prior, now **30 of 40** successes.

- Posterior: Beta(31,11), mean $31/42\approx0.738$, close to the MLE $0.75$.
- The posterior is now much narrower: its standard deviation is about $0.067$.

As data accumulates, the likelihood dominates and the choice of prior matters less and less.

### Sequential updating

Data can be added one batch at a time, and the result is the same as adding it all at once:

Beta(1,1) → (3 successes, 0 failures) → Beta(4,1) → (27 successes, 10 failures) → Beta(31,11).

Today's posterior is tomorrow's prior.

---

## 11.3 The posterior mean as a compromise

For the Beta-Binomial model,

$$
\mathbb E[\theta\mid D]=\frac{a+k}{a+b+n}.
$$

Rewrite it:

$$
\mathbb E[\theta\mid D]=\underbrace{\frac{a+b}{a+b+n}}_{\text{weight on prior}}\cdot\underbrace{\frac a{a+b}}_{\text{prior mean}}+\underbrace{\frac n{a+b+n}}_{\text{weight on data}}\cdot\underbrace{\frac kn}_{\text{observed rate}}.
$$

> [!important] Shrinkage
> The posterior mean is a **weighted average** of the prior mean and the observed frequency. The weights are the amounts of evidence behind each: $a+b$ imaginary observations against $n$ real ones.
> - With no data, you keep the prior.
> - With little data, you are pulled toward the prior ("shrunk").
> - With much data, you follow the data.

**Worked example 11.3.** Prior Beta(8,2) (mean 0.8, worth 10 observations). Data: 5 successes in 10 trials (rate 0.5).

$$
\mathbb E[\theta\mid D]=\frac{8+5}{10+10}=0.65=\frac{10}{20}(0.8)+\frac{10}{20}(0.5).
$$

Equal evidence on both sides, so the answer is halfway.

This shrinkage pattern recurs in every Bayesian model, and it is why Bayesian estimates are more stable than raw frequencies when data is scarce.

---

## 11.4 Gaussian prior, Gaussian measurement

### The update

The unknown is a quantity $\mu$ (a position, say).

- Prior: $\mu\sim\mathcal N(\mu_0,\sigma_0^2)$.
- One measurement: $x\sim\mathcal N(\mu,\sigma^2)$, with known noise variance $\sigma^2$.

The posterior is Gaussian, with

> [!important] Gaussian update
> $$
> \frac1{\sigma_{\text{post}}^2}=\frac1{\sigma_0^2}+\frac1{\sigma^2},\qquad
> \mu_{\text{post}}=\mu_0+K\,(x-\mu_0),\qquad K=\frac{\sigma_0^2}{\sigma_0^2+\sigma^2}.
> $$

### Reading it

**Precisions add.** **Precision** is $1/\text{variance}$: how much information a source carries. Combining the prior with the measurement **adds** their precisions. So the posterior is always **more certain** than either source alone.

**The gain $K$** is between 0 and 1:

- If the prior is vague ($\sigma_0^2$ large), $K\approx1$: trust the measurement.
- If the sensor is noisy ($\sigma^2$ large), $K\approx0$: keep the prior.

**The update** moves the estimate from the prior mean toward the measurement, by $K$ times the **surprise** $x-\mu_0$.

This is precisely the Gaussian conditioning formula of [[PS 07 The Multivariate Gaussian]] in one dimension, and it is the **measurement update of the Kalman filter**, with $K$ the Kalman gain.

### Worked example 11.4

A robot believes its position is $10\pm2$ m (prior variance 4). A sensor reads $12$ m with noise variance 1.

- $K=\dfrac4{4+1}=0.8$.
- $\mu_{\text{post}}=10+0.8(12-10)=11.6$ m.
- $\sigma^2_{\text{post}}=\dfrac1{1/4+1/1}=0.8$, so $\sigma_{\text{post}}\approx0.89$ m.

The sensor is more precise than the prior, so the estimate moves most of the way to the reading, and the uncertainty drops below both 4 and 1.

### Several measurements

With $n$ independent measurements, each of variance $\sigma^2$, precisions keep adding:

$$
\frac1{\sigma^2_{\text{post}}}=\frac1{\sigma_0^2}+\frac n{\sigma^2}.
$$

With a vague prior, this gives $\sigma^2_{\text{post}}\approx\sigma^2/n$: the square-root law again ([[PS 04 Expectation and Variance]]).

---

## 11.5 Summarizing a posterior

A posterior is a whole distribution. Common summaries:

| Summary | Definition | Best when |
|---|---|---|
| **posterior mean** | $\mathbb E[\theta\mid D]$ | you are scored by squared error |
| **posterior median** | middle of the posterior | you are scored by absolute error |
| **MAP** (maximum a posteriori) | the peak (mode) | you want one most-plausible value |
| **credible interval** | a range holding, say, 95% of the posterior | you want to state uncertainty |

> [!note] Credible interval
> A 95% **credible interval** $[l,u]$ satisfies $P(l\le\theta\le u\mid D)=0.95$.

This **does** mean what people often wrongly think a confidence interval means: "given the data (and my prior), there is a 95% probability that $\theta$ lies in this range." The price of that direct interpretation is that it depends on the prior.

---

## 11.6 MAP is regularized maximum likelihood

The MAP estimate maximizes the posterior, or equivalently its logarithm:

$$
\hat\theta_{\text{MAP}}=\arg\max_\theta\Big[\log p(D\mid\theta)+\log p(\theta)\Big].
$$

Now choose a Gaussian prior on the parameters, $\theta\sim\mathcal N(0,\tau^2I)$. Its log is $-\dfrac{\|\theta\|^2}{2\tau^2}+\text{const}$. Negating to get a loss:

> [!important] Priors are regularizers
> $$
> \hat\theta_{\text{MAP}}=\arg\min_\theta\Big[\underbrace{-\log p(D\mid\theta)}_{\text{usual loss}}+\underbrace{\lambda\|\theta\|^2}_{\text{L2 penalty}}\Big],\qquad\lambda=\frac1{2\tau^2}.
> $$
> **L2 regularization (weight decay) is a Gaussian prior that says "parameters are probably small".**

- A tighter prior (small $\tau$) means a stronger penalty (large $\lambda$).
- A **Laplace** prior gives an **L1** penalty, which pushes many parameters to exactly zero.
- A **flat** prior gives no penalty: MAP becomes MLE.

So regularization is not an arbitrary trick. Each regularizer is a stated belief about the parameters.

---

## 11.7 Prediction: averaging over uncertainty

To predict a new observation, do not plug in a single best $\theta$. Average the prediction over everything you still believe is plausible:

> [!note] Posterior predictive distribution
> $$
> p(x_{\text{new}}\mid D)=\int p(x_{\text{new}}\mid\theta)\,p(\theta\mid D)\,d\theta.
> $$

**Worked example 11.5.** After 3 successes in 3 trials with a flat prior, what is the probability that the **next** trial succeeds?

$$
P(\text{next succeeds}\mid D)=\mathbb E[\theta\mid D]=\frac45=0.8.
$$

Not 1, which is what plugging in the MLE would give. This is **Laplace's rule of succession**: after $k$ successes in $n$ trials, predict $(k+1)/(n+2)$.

Plugging in one value ignores parameter uncertainty and produces **overconfident** predictions. Averaging keeps that uncertainty, which matters most exactly when data is scarce.

---

## 11.8 Two kinds of uncertainty

| | Aleatoric | Epistemic |
|---|---|---|
| source | randomness in the world | lack of knowledge |
| example | a fair coin; sensor noise | a policy never tested in the dark |
| does more data reduce it? | **no** | **yes** |
| measured by | the likelihood's spread | the posterior's spread |

A robot should respond to them differently:

- **High epistemic uncertainty**: "I have not seen this situation before." Act cautiously, ask for help, or gather data.
- **High aleatoric uncertainty**: "This is as predictable as it gets." More data will not help; plan for the variability.

Ensembles of networks and Bayesian neural networks try to estimate epistemic uncertainty; disagreement between ensemble members signals unfamiliar inputs ([[16 Evaluation and Uncertainty]]).

---

## 11.9 Frequentist and Bayesian, side by side

| | Frequentist | Bayesian |
|---|---|---|
| parameter | fixed, unknown | random variable describing knowledge |
| answer | point estimate and confidence interval | posterior distribution |
| prior knowledge | not used formally | encoded in the prior |
| interval meaning | the procedure covers the truth 95% of the time | 95% probability given data and prior |
| weak point | indirect interpretation | answers depend on the prior when data is scarce |

With plenty of data the two approaches give nearly identical numbers. They differ when data is scarce, which is exactly when the choice of prior must be made carefully and **stated openly**.

---

## Summary

| Idea | Formula or fact |
|---|---|
| Bayes for parameters | posterior ∝ likelihood × prior |
| Beta-Binomial | Beta($a,b$) → Beta($a+k$, $b+n-k$) |
| posterior mean | weighted average of prior mean and data |
| Gaussian update | precisions add; $\mu_{\text{post}}=\mu_0+K(x-\mu_0)$ |
| MAP with Gaussian prior | MLE + L2 penalty |
| prediction | average over the posterior |
| credible interval | 95% posterior probability |

**Three facts to remember:**

1. Posterior ∝ likelihood × prior; today's posterior is tomorrow's prior.
2. With little data you shrink toward the prior; with much data you follow the data.
3. Every regularizer is a prior; every Kalman update is a Bayesian update.

---

## Exercises

### Part A: warm-up

**A1.** Prior Beta(2,2). Observe 7 successes in 10 trials. Give the posterior and its mean.

**A2.** With a flat prior, a new gripper succeeds in 0 of 5 trials. Give the posterior mean. What does the MLE say?

**A3.** Prior $\mathcal N(0,1)$. One measurement $x=3$ with noise variance 1. Find the posterior mean and variance.

**A4.** Which prior gives stronger weight decay: $\tau=0.1$ or $\tau=10$?

> [!success]- Solutions to Part A
> **A1.** Beta(9,5), mean $9/14\approx0.643$.
>
> **A2.** Beta(1,6), mean $1/7\approx0.143$. The MLE is 0, ruling out any future success.
>
> **A3.** $K=0.5$: mean $1.5$, variance $0.5$.
>
> **A4.** $\tau=0.1$ (larger $\lambda=1/(2\tau^2)$).

### Part B: core

**B1.** Two policies, flat priors. A: 9/10 successes. B: 45/50 successes. Both have MLE 0.9. Give each posterior, mean and standard deviation. Which estimate are you more confident in? (Beta($a,b$) has variance $\dfrac{ab}{(a+b)^2(a+b+1)}$.)

**B2.** A robot's prior on its $x$-position is $\mathcal N(5,\,0.25)$. Two independent sensors read $5.4$ (variance $0.25$) and $4.9$ (variance $1.0$). Find the posterior mean and variance, processing them one after the other. Check that the order does not matter.

**B3.** You believe a sensor's bias is near zero, prior $\mathcal N(0,0.01)$. Ten readings of a known zero signal average $0.05$, each with noise variance $0.04$. Find the posterior on the bias.

**B4.** Show that with prior Beta($a,b$), the posterior mean always lies between the prior mean and the observed rate $k/n$.

**B5.** A colleague reports "the success rate is 100%" after 4 trials. Using the rule of succession and a credible interval idea, write a one-paragraph reply.

> [!success]- Solutions to Part B
> **B1.** A: Beta(10,2), mean $0.833$, variance $\dfrac{20}{144\times13}\approx0.0107$, sd $\approx0.103$. B: Beta(46,6), mean $0.885$, variance $\dfrac{276}{2704\times53}\approx0.00193$, sd $\approx0.044$. B's estimate is far more certain, though the observed rates are the same.
>
> **B2.** First: $K=0.25/0.5=0.5$, mean $5.2$, variance $0.125$. Second: $K=0.125/1.125\approx0.111$, mean $5.2+0.111(4.9-5.2)\approx5.167$, variance $1/(8+1)\approx0.111$. Other order: precisions $4+1+4=9$ either way, so variance $0.111$; mean is the precision-weighted average $\dfrac{4(5)+4(5.4)+1(4.9)}{9}=\dfrac{46.5}{9}\approx5.167$ ✓.
>
> **B3.** The average of 10 readings has variance $0.004$ (precision 250). Prior precision 100. Posterior precision 350, variance $\approx0.00286$. Mean $\dfrac{250\times0.05}{350}\approx0.0357$.
>
> **B4.** Section 11.3 writes it as a weighted average with positive weights summing to 1, so it lies between the two.
>
> **B5.** "Four out of four is encouraging but weak evidence. With a flat prior, the best prediction for the next trial is $5/6\approx83\%$, not 100%, and rates as low as about 50% remain quite plausible. We need many more trials before claiming a high success rate."

### Part C: explain and prove

**C1.** Show that sequential updating (Beta(1,1) with 3/3, then 27/37) gives the same posterior as updating once with 30/40.

**C2.** Explain why MAP with a flat prior equals MLE.

**C3.** Explain the difference between a 95% confidence interval and a 95% credible interval in two sentences each.

**C4.** Explain why ensembles of networks that disagree on an input suggest epistemic, not aleatoric, uncertainty.

> [!success]- Solutions to Part C
> **C1.** Beta(1,1) → Beta(4,1) → Beta(4+27, 1+10)=Beta(31,11). Directly: Beta(1+30, 1+10)=Beta(31,11). Multiplication of likelihoods is order-independent.
>
> **C2.** A flat prior is constant, so $\log p(\theta)$ adds a constant that does not move the maximizer.
>
> **C3.** Confidence: the parameter is fixed and the interval is random; the method captures the truth in 95% of repeated experiments. Credible: the parameter is uncertain and the interval is fixed; given the data and prior, the parameter lies inside with probability 95%.
>
> **C4.** Each ensemble member is a plausible model given the training data. Disagreement means the data did not pin down the answer for this input, which is lack of knowledge. Noise in the world would make all members predict the same spread, not different answers.

### Part D: practise with code

**D1.** Plot the Beta posterior after 0, 1, 5, 20 and 100 trials of a simulated policy with true rate 0.7, starting from a flat prior. Watch it sharpen around 0.7.

**D2.** Compute a 95% credible interval for Beta(4,1) with `scipy.stats.beta.ppf([0.025, 0.975], 4, 1)`.

**D3.** Implement the 1-D Kalman measurement update and run it on 50 noisy readings of a fixed position, starting from a vague prior. Plot the estimate and its $\pm2\sigma$ band over time.

**D4.** Fit ridge regression for several $\lambda$ values to 15 noisy points with a degree-9 polynomial. Plot the fits. Relate $\lambda$ to the prior width $\tau$.

> [!success]- Hints for Part D
> **D2.** About $[0.40,\;0.99]$.
>
> **D3.** The band narrows roughly like $1/\sqrt t$, and the estimate settles near the true position.

---

## Where this is used

- **Recursive state estimation** (Kalman and particle filters) is Bayesian updating, step after step ([[04 Perception and State]]).
- **Uncertainty-aware policies** and ensembles estimate epistemic uncertainty to decide when to be careful ([[16 Evaluation and Uncertainty]]).
- **Conservative offline RL** penalizes actions where the data provides little evidence: a Bayesian idea in practice ([[10 Offline RL and Data Coverage]]).

Next: [[PS 12 Markov Chains and Information]]: sequences, long-run behaviour, and measuring surprise.

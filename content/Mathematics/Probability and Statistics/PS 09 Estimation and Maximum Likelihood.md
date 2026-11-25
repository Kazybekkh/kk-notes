---
type: course-chapter
course: probability-statistics
chapter: 9
tags: [mathematics, statistics, estimation]
---

# Chapter 9: Estimation and maximum likelihood

Previous: [[PS 08 Law of Large Numbers and Central Limit Theorem]] | [[PS 00 Course Map]] | Next: [[PS 10 Confidence Intervals and Hypothesis Tests]]

> [!abstract] The big idea
> To fit a model to data, choose the parameters under which **the data you actually observed would have been most probable**. That is **maximum likelihood**. It reproduces common-sense answers (the sample mean, the observed fraction) and also explains the loss functions of machine learning: with Gaussian noise it is **least squares**, and with categories it is **cross-entropy**.

> [!info] In this chapter you will learn to
> 1. Distinguish a parameter, an estimator and an estimate.
> 2. Judge estimators by bias, variance and mean squared error.
> 3. Explain why the sample variance divides by $n-1$.
> 4. Write a likelihood and log-likelihood, and maximize them.
> 5. Derive least squares and cross-entropy as maximum likelihood.
> 6. Recognize overfitting and explain regularization.

> [!tip] Before you start
> You need the named distributions ([[PS 03 Discrete Random Variables]], [[PS 05 Continuous Random Variables]]), standard error ([[PS 08 Law of Large Numbers and Central Limit Theorem]]), and finding a maximum with calculus: set the derivative to zero. Two log rules: $\log(ab)=\log a+\log b$ and $\log a^k=k\log a$.

---

## 9.1 From probability to statistics

**Probability** runs forward: given the parameter, what data will we see? "If the coin is fair, how likely are 7 heads in 10 flips?"

**Statistics** runs backward: given the data, what was the parameter? "I saw 7 heads in 10 flips. How biased is this coin?"

### Vocabulary

| Term | Meaning | Example |
|---|---|---|
| **parameter** $\theta$ | a fixed but unknown number describing the population | the coin's true heads probability $p$ |
| **estimator** $\hat\theta$ | a **rule** that turns data into a guess | "count heads, divide by $n$" |
| **estimate** | the number the rule gives on **your** data | $0.7$ |

Because data is random, an estimator is a **random variable**: different datasets would give different estimates. So it has a mean, a variance and a sampling distribution, and we can ask whether it is a good rule.

---

## 9.2 What makes an estimator good?

### Bias

> [!note] Definition: bias
> $$
> \operatorname{bias}(\hat\theta)=\mathbb E[\hat\theta]-\theta.
> $$
> If the bias is zero, the estimator is **unbiased**: on average it hits the right value.

### Variance

How much does the estimate jump around from one dataset to another? $\operatorname{Var}(\hat\theta)$, or its square root, the standard error.

### Mean squared error

> [!important] Bias-variance decomposition
> $$
> \operatorname{MSE}(\hat\theta)=\mathbb E\big[(\hat\theta-\theta)^2\big]=\operatorname{bias}^2+\operatorname{variance}.
> $$

*Proof sketch:* write $\hat\theta-\theta=(\hat\theta-\mathbb E\hat\theta)+(\mathbb E\hat\theta-\theta)$, square, and take expectations; the cross term vanishes because $\mathbb E[\hat\theta-\mathbb E\hat\theta]=0$.

**The darts picture.** Bias is how far the **centre** of your cluster of darts is from the bullseye. Variance is how **spread out** the cluster is. MSE measures the typical distance of a dart from the bullseye, combining both.

| | low variance | high variance |
|---|---|---|
| **low bias** | tight cluster on target: ideal | scattered around the target |
| **high bias** | tight cluster, off target | scattered and off target |

### The bias-variance tradeoff

An estimator with a **little** bias but **much** less variance can have lower MSE than an unbiased one. Accepting some bias to cut variance is a deliberate and very common strategy: it is what **regularization** does (section 9.8).

### Consistency

An estimator is **consistent** if $\hat\theta\to\theta$ as $n\to\infty$. With enough data it gets there. The sample mean is consistent by the law of large numbers.

---

## 9.3 Sample mean and sample variance

$$
\bar x=\frac1n\sum_{i=1}^nx_i,\qquad s^2=\frac1{n-1}\sum_{i=1}^n(x_i-\bar x)^2.
$$

- $\bar x$ is an **unbiased** estimator of $\mu$ ($\mathbb E[\bar x]=\mu$).
- $s^2$ is an **unbiased** estimator of $\sigma^2$, but **only** because it divides by $n-1$.

### Why $n-1$?

The deviations are measured from $\bar x$, which was itself computed from the same data. $\bar x$ is the number that **minimizes** $\sum(x_i-c)^2$ over all $c$ (it is the least squares fit of a constant, [[LA 06 Orthogonality and Least Squares]]). So the sum of squared deviations from $\bar x$ is always **smaller** than the sum from the true $\mu$. Dividing by $n$ would therefore **underestimate** $\sigma^2$ on average.

Exactly how much smaller? On average by one $\sigma^2$: $\mathbb E\big[\sum(x_i-\bar x)^2\big]=(n-1)\sigma^2$. Dividing by $n-1$ corrects it.

**Degrees of freedom.** The $n$ deviations $x_i-\bar x$ must sum to zero, so only $n-1$ of them are free. One degree of freedom was "used up" estimating the mean.

**Worked example 9.1.** Data $2,4,6$. $\bar x=4$. Squared deviations $4,0,4$, sum 8. $s^2=8/2=4$, $s=2$. (Dividing by $n$ would give $2.67$.)

---

## 9.4 Likelihood

### The definition

Suppose the data come from a model with density or mass function $p(x\mid\theta)$, and the observations $x_1,\dots,x_n$ are independent.

> [!note] Definition: likelihood
> $$
> L(\theta)=\prod_{i=1}^np(x_i\mid\theta).
> $$
> This is the probability (or density) of the observed data, **viewed as a function of $\theta$** with the data held fixed.

It is the same formula as the probability of the data, but read differently:

- As a function of the **data** (with $\theta$ fixed): a probability distribution.
- As a function of **$\theta$** (with data fixed): the likelihood. It scores how well each candidate $\theta$ explains what was actually seen.

> [!warning] Likelihood is not "the probability of $\theta$"
> $L(\theta)$ need not sum or integrate to 1 over $\theta$. It answers "how probable is this data if $\theta$ were true?", which is $P(\text{data}\mid\theta)$, not $P(\theta\mid\text{data})$. Getting the second requires a prior and Bayes' rule ([[PS 11 Bayesian Inference]]).

### Maximum likelihood estimation

> [!important] Maximum likelihood estimation (MLE)
> Choose the parameter value that makes the observed data most probable:
> $$
> \hat\theta_{\text{MLE}}=\arg\max_\theta L(\theta).
> $$

### Use the log-likelihood

In practice, maximize the **log-likelihood**:

$$
\ell(\theta)=\log L(\theta)=\sum_{i=1}^n\log p(x_i\mid\theta).
$$

Three reasons:

1. **Products become sums**, which are far easier to differentiate.
2. **Numerical safety.** A product of 10,000 probabilities each around 0.1 is $10^{-10000}$, which underflows to zero on a computer. The sum of logs is about $-23{,}000$, perfectly representable.
3. **Same answer.** $\log$ is increasing, so the $\theta$ that maximizes $\ell$ also maximizes $L$.

### The recipe

1. Write the likelihood $L(\theta)$ as a product.
2. Take logs to get $\ell(\theta)$.
3. Differentiate with respect to $\theta$ and set to zero.
4. Solve for $\theta$. (Check it is a maximum.)

---

## 9.5 Worked examples of MLE

### Worked example 9.2: a coin (Bernoulli)

$n$ flips give $k$ heads. Each flip has probability $p$ of heads.

**Step 1.** $L(p)=p^k(1-p)^{n-k}$ (one particular sequence; the binomial coefficient is a constant and does not affect the maximizer).

**Step 2.** $\ell(p)=k\log p+(n-k)\log(1-p)$.

**Step 3.**

$$
\frac{d\ell}{dp}=\frac kp-\frac{n-k}{1-p}=0.
$$

**Step 4.** Multiply out: $k(1-p)=(n-k)p$, so $k=np$ and

$$
\hat p=\frac kn.
$$

The **observed fraction**. With 7 heads in 10 flips, $\hat p=0.7$.

This is reassuring: the principle reproduces common sense in the simple case, which is evidence that it can be trusted in complicated cases where common sense gives no answer.

### Worked example 9.3: Poisson counts

Counts per hour $x_1,\dots,x_n$ from Poisson($\lambda$):

$$
\ell(\lambda)=\sum_i\left(x_i\log\lambda-\lambda-\log x_i!\right),\qquad\frac{d\ell}{d\lambda}=\frac{\sum x_i}\lambda-n=0,\qquad\hat\lambda=\bar x.
$$

The sample mean. For counts $3,1,2,2$: $\hat\lambda=2$.

### Worked example 9.4: Gaussian mean and variance

Data from $\mathcal N(\mu,\sigma^2)$:

$$
\ell(\mu,\sigma^2)=-\frac n2\log(2\pi\sigma^2)-\frac1{2\sigma^2}\sum_i(x_i-\mu)^2.
$$

**The mean.** Only the last term depends on $\mu$, and it is maximized by **minimizing** $\sum(x_i-\mu)^2$. That gives $\hat\mu=\bar x$.

**The variance.** Differentiate with respect to $\sigma^2$ and set to zero:

$$
\hat\sigma^2_{\text{MLE}}=\frac1n\sum_i(x_i-\bar x)^2.
$$

Note it divides by $n$, so it is slightly **biased** downward (section 9.3). MLE is not guaranteed to be unbiased. It is guaranteed (under mild conditions) to be **consistent**, and for large samples to have the **smallest possible variance** among well-behaved estimators. The bias here vanishes as $n$ grows.

### Worked example 9.5: exponential lifetimes

Lifetimes $x_1,\dots,x_n$ from Exponential($\lambda$): $\ell(\lambda)=n\log\lambda-\lambda\sum x_i$. Setting $n/\lambda-\sum x_i=0$ gives $\hat\lambda=1/\bar x$. If five parts lasted $200,450,100,800,450$ hours, $\bar x=400$ and $\hat\lambda=0.0025$ per hour.

> [!question]- Check yourself
> A policy succeeds 18 times in 24 trials. What is the MLE of its success rate?
>
> **Answer.** $18/24=0.75$.

---

## 9.6 Least squares is maximum likelihood

### The model

Suppose each output is a deterministic function of the input plus Gaussian noise:

$$
y_i=f_\theta(x_i)+\varepsilon_i,\qquad\varepsilon_i\sim\mathcal N(0,\sigma^2)\text{ independent}.
$$

Then $y_i\sim\mathcal N(f_\theta(x_i),\sigma^2)$, and the log-likelihood is

$$
\ell(\theta)=\text{const}-\frac1{2\sigma^2}\sum_i\big(y_i-f_\theta(x_i)\big)^2.
$$

> [!important] Gaussian noise ⟹ least squares
> Maximizing this likelihood is exactly **minimizing the sum of squared errors**.

So mean squared error is not an arbitrary choice. It is the correct loss **if the noise is Gaussian**. The linear regression of [[LA 06 Orthogonality and Least Squares]] is maximum likelihood under that assumption.

### Other noise, other losses

If the noise has heavier tails, a different loss is correct:

| Noise model | Maximum likelihood loss | Behaviour |
|---|---|---|
| Gaussian | squared error $\sum(y-\hat y)^2$ | sensitive to outliers |
| Laplace (double exponential) | absolute error $\sum\lvert y-\hat y\rvert$ | robust to outliers; fits the median |

This is why L1 (absolute) loss is used when data contains outliers.

---

## 9.7 Cross-entropy is maximum likelihood

### The model

A classifier (or a discrete-action policy) outputs a probability for each class: $q_\theta(c\mid x)$. Training data are pairs $(x_i,c_i)$ of inputs and true labels.

The likelihood of the observed labels is $\prod_iq_\theta(c_i\mid x_i)$. Take logs, negate, and average:

$$
\text{loss}(\theta)=-\frac1n\sum_{i=1}^n\log q_\theta(c_i\mid x_i).
$$

> [!important] Classification loss = negative log-likelihood
> This is the **cross-entropy loss** (also called the negative log-likelihood, NLL). Minimizing it is maximizing the likelihood of the training labels.

### What the loss rewards

| Probability given to the correct class | Loss $-\ln q$ |
|---|---|
| 0.99 | 0.010 |
| 0.9 | 0.105 |
| 0.5 | 0.693 |
| 0.1 | 2.303 |
| 0.01 | 4.605 |

Being right confidently costs almost nothing. Being **confidently wrong** is punished severely. The connection to information theory is explained in [[PS 12 Markov Chains and Information]].

**Behaviour cloning** with discrete actions is exactly this: the expert's actions are the labels, and the policy is trained to maximize their likelihood ([[06 Imitation and Distribution Shift]]).

---

## 9.8 Overfitting and regularization

### The problem

Maximum likelihood uses **only** the training data. With a flexible model and little data, it fits the noise as well as the signal.

**Extreme example.** A coin shows 3 heads in 3 flips. MLE says $\hat p=1$: the coin **never** shows tails. That is a confident and almost certainly wrong conclusion from tiny data. (High variance.)

A polynomial with as many parameters as data points passes through every point exactly, including the noise, and predicts wildly between them.

### Remedies

All of these accept a little bias in exchange for much lower variance:

1. **More data.** Variance shrinks.
2. **A simpler model.** Fewer parameters to fit noise with.
3. **Regularization.** Add a penalty for complexity to the loss:
$$
\text{loss}(\theta)+\lambda\|\theta\|^2.
$$
This pulls parameters toward zero. It has a Bayesian reading as a **prior belief** that parameters are small ([[PS 11 Bayesian Inference]]).
4. **Validation.** Hold out data the fit never saw, and measure error there. Training error always looks better than real performance.

> [!warning] Never report training error as performance
> The model was chosen to fit the training data, so it looks better there than it is. Performance must be measured on data that played no part in fitting or in choosing the model.

---

## Summary

| Idea | Formula or fact |
|---|---|
| bias | $\mathbb E[\hat\theta]-\theta$ |
| MSE | bias² + variance |
| sample variance | divide by $n-1$ to be unbiased |
| likelihood | $L(\theta)=\prod p(x_i\mid\theta)$ |
| MLE | $\arg\max\ell(\theta)$, $\ell=\sum\log p(x_i\mid\theta)$ |
| Bernoulli, Poisson, Gaussian mean | observed fraction, $\bar x$, $\bar x$ |
| Gaussian noise | MLE = least squares |
| categories | MLE = cross-entropy |
| overfitting | low bias, high variance; fix with data, simplicity, regularization |

**Three facts to remember:**

1. MLE picks the parameters that make the observed data most probable.
2. Your loss function is a hidden assumption about the noise.
3. Lower error on training data is not better performance; check on held-out data.

---

## Exercises

### Part A: warm-up

**A1.** Data $3,7,8,10,12$. Compute $\bar x$, the MLE of the variance, and $s^2$.

**A2.** In 40 grasp attempts, 34 succeed. What is the MLE of the success probability?

**A3.** An estimator has bias 0.1 and variance 0.04. Another has bias 0 and variance 0.09. Which has lower MSE?

**A4.** A classifier gives the true class probability 0.8 on one example and 0.3 on another. Compute the average cross-entropy loss (natural log).

> [!success]- Solutions to Part A
> **A1.** $\bar x=8$. Squared deviations $25,1,0,4,16$, sum 46. MLE $46/5=9.2$. $s^2=46/4=11.5$.
>
> **A2.** $34/40=0.85$.
>
> **A3.** $0.01+0.04=0.05$ versus $0.09$. The biased one.
>
> **A4.** $\tfrac12(-\ln0.8-\ln0.3)=\tfrac12(0.223+1.204)\approx0.714$.

### Part B: core

**B1.** Derive the MLE of $p$ for the geometric distribution, given observed waiting times $x_1,\dots,x_n$.

**B2.** Lifetimes (hours) of five components: $120,80,200,150,50$. Assuming an exponential model, find the MLE of the failure rate and of the mean lifetime.

**B3.** You fit $y=\theta x$ (a line through the origin) with Gaussian noise. Derive the MLE of $\theta$ for data $(x_i,y_i)$. Apply it to $(1,2)$, $(2,3)$, $(3,7)$.

**B4.** Explain why fitting a degree-9 polynomial to 10 noisy points typically has lower training error but higher test error than a degree-2 polynomial. Use the words bias and variance.

**B5.** Show that the MLE for the mean of $\mathcal N(\mu,\sigma^2)$ is the same whatever the value of $\sigma^2$. Why does that matter?

> [!success]- Solutions to Part B
> **B1.** $\ell(p)=\sum[(x_i-1)\log(1-p)+\log p]=(\sum x_i-n)\log(1-p)+n\log p$. Derivative $-\dfrac{\sum x_i-n}{1-p}+\dfrac np=0$ gives $\hat p=n/\sum x_i=1/\bar x$.
>
> **B2.** $\bar x=120$. $\hat\lambda=1/120\approx0.0083$ per hour; mean lifetime 120 hours.
>
> **B3.** Minimize $\sum(y_i-\theta x_i)^2$: derivative $-2\sum x_i(y_i-\theta x_i)=0$, so $\hat\theta=\dfrac{\sum x_iy_i}{\sum x_i^2}=\dfrac{2+6+21}{1+4+9}=\dfrac{29}{14}\approx2.07$.
>
> **B4.** The degree-9 polynomial has enough freedom to pass through all 10 points (low bias, near-zero training error) but it fits the noise, so it changes wildly with the particular sample (high variance) and predicts badly between points. The degree-2 polynomial cannot fit the noise (some bias) but is stable (low variance), so it generalizes better.
>
> **B5.** $\mu$ appears only in $-\tfrac1{2\sigma^2}\sum(x_i-\mu)^2$, and any positive constant factor does not move the minimizer. So you can estimate the mean without knowing the noise level, which is why least squares works without knowing $\sigma$.

### Part C: explain and prove

**C1.** Prove that $\bar x$ minimizes $\sum_i(x_i-c)^2$ over all numbers $c$.

**C2.** Prove the bias-variance decomposition $\operatorname{MSE}=\operatorname{bias}^2+\operatorname{variance}$.

**C3.** Explain why maximizing likelihood and maximizing log-likelihood give the same answer, and why the second is preferred in code.

**C4.** A colleague trains with squared error on data containing a few large sensor glitches. What do you suggest, and why, in terms of noise models?

> [!success]- Solutions to Part C
> **C1.** Derivative $-2\sum(x_i-c)=0$ gives $c=\bar x$; the second derivative $2n>0$ confirms a minimum.
>
> **C2.** Section 9.2's proof sketch, written out: $\mathbb E[(\hat\theta-\theta)^2]=\mathbb E[(\hat\theta-\mathbb E\hat\theta)^2]+2(\mathbb E\hat\theta-\theta)\mathbb E[\hat\theta-\mathbb E\hat\theta]+(\mathbb E\hat\theta-\theta)^2$, and the middle term is 0.
>
> **C3.** $\log$ is strictly increasing, so it preserves the location of the maximum. Logs turn products into sums (easier derivatives) and avoid numerical underflow.
>
> **C4.** Squared error assumes Gaussian noise, which makes large errors extremely unlikely, so the fit bends to explain the glitches. Use absolute error or Huber loss (Laplace-like heavy-tailed noise), or detect and remove the glitches.

### Part D: practise with code

**D1.** For a coin with 7 heads in 10 flips, plot $L(p)$ and $\ell(p)$ for $p\in(0,1)$. Mark the maximum.

**D2.** Draw 5 samples from $\mathcal N(0,1)$, compute the variance with `ddof=0` and `ddof=1`. Repeat 10,000 times and average each. Which one averages to 1?

**D3.** Fit polynomials of degree 1 to 9 to 12 noisy points from $y=\sin(2\pi x)$. Plot training error and error on 200 fresh points against degree. Find where test error is lowest.

**D4.** Fit a line by least squares to data with one huge outlier, then fit it by minimizing absolute error (`scipy.optimize.minimize`). Compare the two lines.

> [!success]- Hints for Part D
> **D2.** `ddof=1` (dividing by $n-1$) averages to about 1; `ddof=0` averages to about $0.8=(n-1)/n$.
>
> **D3.** Training error keeps falling with degree; test error falls, then rises sharply: the classic U-shape of overfitting.

---

## Where this is used

- **Every supervised loss** in [[05 Training Neural Policies]] is a negative log-likelihood under some noise model.
- **Behaviour cloning** is maximum likelihood on expert actions ([[06 Imitation and Distribution Shift]]).
- **The diffusion training objective** is derived from a likelihood bound ([[08 Diffusion and Flow Matching]]).
- **System identification**: fitting a robot's mass, friction and delay parameters from logged data.

Next: [[PS 10 Confidence Intervals and Hypothesis Tests]]: how sure are you, and is the effect real?

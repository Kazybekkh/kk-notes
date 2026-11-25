---
type: course-chapter
course: probability-statistics
chapter: 3
tags: [mathematics, probability]
---

# Chapter 3: Discrete random variables

Previous: [[PS 02 Conditional Probability and Bayes Rule]] | [[PS 00 Course Map]] | Next: [[PS 04 Expectation and Variance]]

> [!abstract] The big idea
> A **random variable** attaches a number to each outcome of an experiment, so we can do arithmetic with uncertainty. A handful of named distributions (Bernoulli, binomial, geometric, Poisson, categorical) describe most situations where you **count** things. Recognizing which one applies is half the work.

> [!info] In this chapter you will learn to
> 1. Define a random variable and describe it by its PMF and CDF.
> 2. Recognize Bernoulli, binomial, geometric, Poisson and categorical situations.
> 3. Derive the binomial formula from counting.
> 4. Compute probabilities with each distribution.
> 5. Choose the right model for a counting problem, and spot when the assumptions fail.

> [!tip] Before you start
> You need the axioms and independence ([[PS 01 Sample Spaces Events and Axioms]], [[PS 02 Conditional Probability and Bayes Rule]]) and binomial coefficients $\binom nk$ ([[DM 07 Counting]]): $\binom nk=\dfrac{n!}{k!(n-k)!}$ is the number of ways to choose $k$ items from $n$.

---

## 3.1 What is a random variable?

### Numbers from outcomes

Outcomes are often not numbers ($HT$, "card is the queen of hearts"). To compute averages, spreads and so on, we attach a number to each outcome.

> [!note] Definition: random variable
> A **random variable** $X$ is a function that assigns a real number to each outcome in the sample space.

**Example.** Flip two coins and let $X$ be the number of heads:

| Outcome | $HH$ | $HT$ | $TH$ | $TT$ |
|---|---|---|---|---|
| $X$ | 2 | 1 | 1 | 0 |

Despite the name, a random variable is not "random" in itself, nor a "variable" in the algebra sense. It is a fixed rule. The randomness comes from which outcome occurs.

### Notation

- Upper case $X$: the random quantity (the rule).
- Lower case $x$: a particular value it might take.
- "$X=1$" is an **event**: the set of outcomes where $X$ equals 1. Here it is $\{HT,TH\}$.

A random variable is **discrete** if its possible values can be listed: finitely many, or a countable sequence like $0,1,2,\dots$ (Continuous random variables are chapter 5.)

---

## 3.2 PMF and CDF

### Probability mass function

> [!note] Definition: PMF
> The **probability mass function** of a discrete random variable is
> $$
> p(x)=P(X=x).
> $$
> It satisfies $p(x)\ge0$ for all $x$, and $\sum_xp(x)=1$.

For the two coins:

| $x$ | 0 | 1 | 2 |
|---|---|---|---|
| $p(x)$ | $\tfrac14$ | $\tfrac12$ | $\tfrac14$ |

A PMF is often drawn as a bar chart: one bar per value, with height equal to its probability.

To find the probability of a set of values, add the PMF over that set: $P(X\ge1)=\tfrac12+\tfrac14=\tfrac34$.

### Cumulative distribution function

> [!note] Definition: CDF
> The **cumulative distribution function** is
> $$
> F(x)=P(X\le x).
> $$

For the two coins: $F(0)=\tfrac14$, $F(1)=\tfrac34$, $F(2)=1$. Between those values it stays flat (a staircase). Every CDF starts at 0 on the far left, ends at 1 on the far right, and never decreases.

Useful identity for integers: $P(a<X\le b)=F(b)-F(a)$.

> [!question]- Check yourself
> A random variable has PMF $p(0)=0.2$, $p(1)=0.5$, $p(2)=c$. Find $c$, $F(1)$ and $P(X\neq1)$.
>
> **Answer.** $c=0.3$. $F(1)=0.7$. $P(X\neq1)=0.5$.

---

## 3.3 Bernoulli: one yes/no trial

> [!note] Bernoulli($p$)
> $X$ takes the value 1 ("success") with probability $p$ and 0 ("failure") with probability $1-p$.
> $$
> P(X=1)=p,\qquad P(X=0)=1-p.
> $$

**Examples:** one coin flip, one grasp attempt, whether one prediction is correct, whether one email is spam.

Its mean is $p$ and its variance is $p(1-p)$ (computed in chapter 4). The variance is largest at $p=0.5$, where the outcome is hardest to predict, and zero at $p=0$ or $1$, where there is no uncertainty.

Bernoulli variables are the building blocks of everything else in this chapter.

---

## 3.4 Binomial: successes in $n$ trials

### The setting

Repeat a Bernoulli($p$) trial $n$ times, **independently**, with the **same** $p$ each time. Let $X$ be the number of successes.

> [!note] Binomial($n,p$)
> $$
> P(X=k)=\binom nk\,p^k(1-p)^{n-k},\qquad k=0,1,\dots,n.
> $$

### Where the formula comes from

Take $n=4$ and $k=2$. One particular sequence with 2 successes is $SSFF$. By independence its probability is

$$
p\cdot p\cdot(1-p)\cdot(1-p)=p^2(1-p)^2.
$$

Every other sequence with 2 successes ($SFSF$, $SFFS$, $FSSF$, $FSFS$, $FFSS$) has the **same** probability, just multiplied in a different order. How many such sequences are there? Choose which 2 of the 4 positions are successes: $\binom42=6$. These sequences are disjoint events, so add:

$$
P(X=2)=6\,p^2(1-p)^2.
$$

In general: $\binom nk$ arrangements, each with probability $p^k(1-p)^{n-k}$.

### Worked example 3.1: a policy evaluation

A robot policy succeeds with probability $p=0.8$ on each trial. You run $n=5$ trials. What is the distribution of the number of successes?

| $k$ | $\binom5k$ | $0.8^k\,0.2^{5-k}$ | $P(X=k)$ |
|---|---|---|---|
| 0 | 1 | $0.00032$ | 0.0003 |
| 1 | 5 | $0.00128$ | 0.0064 |
| 2 | 10 | $0.00512$ | 0.0512 |
| 3 | 10 | $0.02048$ | 0.2048 |
| 4 | 5 | $0.08192$ | 0.4096 |
| 5 | 1 | $0.32768$ | 0.3277 |

Check: the probabilities sum to 1.

**The lesson.** Even with a true success rate of 80%, a 5-trial evaluation shows 3 or fewer successes with probability $0.0003+0.0064+0.0512+0.2048\approx0.26$. **More than a quarter of the time**, a good policy looks mediocre. Small evaluations are noisy. Chapter 10 quantifies how many trials you need.

### Mean and variance

$$
\mathbb E[X]=np,\qquad\operatorname{Var}(X)=np(1-p).
$$

(Derived in chapter 4 by writing $X$ as a sum of $n$ Bernoulli variables.) For example 3.1: mean 4, variance 0.8.

### The binomial assumptions

> [!warning] Check all four before using the binomial
> 1. A **fixed** number of trials $n$.
> 2. Each trial has two outcomes.
> 3. The success probability $p$ is the **same** for every trial.
> 4. Trials are **independent**.
>
> If a robot's success rate drops as its battery drains (assumption 3 fails), or trials share the same tricky object placement (assumption 4 fails), the binomial is only an approximation.

> [!question]- Check yourself
> 1. A fair coin is flipped 4 times. Write the full PMF of the number of heads.
> 2. A 90% policy is run 10 times. What is $P(10\text{ out of }10)$?
>
> **Answers.** 1. $\tfrac1{16},\tfrac4{16},\tfrac6{16},\tfrac4{16},\tfrac1{16}$. 2. $0.9^{10}\approx0.349$: a perfect run happens only about a third of the time.

---

## 3.5 Geometric: waiting for the first success

### The setting

Repeat independent Bernoulli($p$) trials until the **first** success. Let $X$ be the number of trials needed (including the successful one).

> [!note] Geometric($p$)
> $$
> P(X=k)=(1-p)^{k-1}p,\qquad k=1,2,3,\dots
> $$

*Why:* the first $k-1$ trials must fail (probability $(1-p)^{k-1}$), then the $k$-th must succeed (probability $p$).

$$
\mathbb E[X]=\frac1p,\qquad\operatorname{Var}(X)=\frac{1-p}{p^2}.
$$

**In words:** if each attempt works 1 time in 10, expect 10 attempts on average.

### Worked example 3.2

Rolling a die until a six appears:

- $P(\text{exactly 3 rolls})=\left(\tfrac56\right)^2\tfrac16=\tfrac{25}{216}\approx0.116$.
- $P(\text{more than 10 rolls})=P(\text{first 10 all fail})=\left(\tfrac56\right)^{10}\approx0.162$.
- Expected number of rolls: 6.

### Memorylessness

> [!important] The geometric distribution has no memory
> $$
> P(X>s+t\mid X>s)=P(X>t).
> $$
> Having already failed $s$ times does not bring success any closer.

*Proof:* $P(X>s+t\mid X>s)=\dfrac{(1-p)^{s+t}}{(1-p)^s}=(1-p)^t=P(X>t)$.

This is the precise statement of why the **gambler's fallacy** is a fallacy: after 20 tails, a fair coin is not "due" a head.

> [!warning] Two conventions
> Some books count the number of **failures before** the first success ($0,1,2,\dots$), which shifts the mean to $(1-p)/p$. Check which version a source uses.

---

## 3.6 Poisson: counting rare events

### The setting

Count events that happen **independently** at a **constant average rate** over a fixed interval of time or space: emails per hour, faults per day, typos per page.

> [!note] Poisson($\lambda$)
> $$
> P(X=k)=\frac{\lambda^ke^{-\lambda}}{k!},\qquad k=0,1,2,\dots
> $$
> $$
> \mathbb E[X]=\lambda,\qquad\operatorname{Var}(X)=\lambda.
> $$

$\lambda$ is the average count in the interval. Mean and variance are equal, a quick check for whether count data is "Poisson-like".

### Where it comes from

Split an hour into $n$ tiny slots. In each slot an event happens with small probability $p=\lambda/n$, independently. The count is Binomial($n$, $\lambda/n$). As $n\to\infty$, this binomial tends to the Poisson formula. So:

> [!tip] Poisson approximation
> If $n$ is large and $p$ is small, Binomial($n,p$) is close to Poisson($np$).

### Worked example 3.3

A robot cell averages 2 faults per 8-hour shift.

- $P(\text{no faults in a shift})=e^{-2}\approx0.135$.
- $P(\text{exactly 2})=\dfrac{2^2e^{-2}}{2!}=2e^{-2}\approx0.271$.
- $P(\text{at least 3})=1-e^{-2}\left(1+2+\tfrac{4}{2}\right)=1-5e^{-2}\approx0.323$.

### Worked example 3.4: scaling the interval

The same cell, over **half** a shift: the rate scales to $\lambda=1$. $P(\text{no faults})=e^{-1}\approx0.368$.

### Worked example 3.5: approximation

A batch of 1,000 parts, each defective with probability 0.002. $P(\text{no defects})$?

- Exact binomial: $0.998^{1000}\approx0.1351$.
- Poisson with $\lambda=2$: $e^{-2}\approx0.1353$.

Almost identical, and the Poisson is much easier to compute for larger counts.

> [!question]- Check yourself
> Requests arrive at 3 per second on average. Find $P(\text{exactly 3 in a given second})$ and $P(\text{none in a given second})$.
>
> **Answer.** $\dfrac{27e^{-3}}{6}=4.5e^{-3}\approx0.224$. $e^{-3}\approx0.050$.

---

## 3.7 Categorical: one of several labels

> [!note] Categorical($p_1,\dots,p_k$)
> $X$ takes one of $k$ values (categories) with probabilities $p_1,\dots,p_k$, where $\sum p_i=1$.

A loaded die is categorical. So is the output of a classifier's **softmax** layer, and the distribution a discrete-action robot policy samples its next action from.

Repeating a categorical trial $n$ times and counting how many land in each category gives the **multinomial** distribution, the many-category version of the binomial.

---

## 3.8 Choosing a distribution

| Situation | Distribution |
|---|---|
| one trial, two outcomes | Bernoulli($p$) |
| number of successes in a **fixed** number of independent trials | Binomial($n,p$) |
| number of trials until the **first** success | Geometric($p$) |
| number of events in a fixed interval at a constant rate | Poisson($\lambda$) |
| one of $k$ labels | Categorical |
| draws **without replacement** from a finite group | Hypergeometric (not binomial) |

**Hypergeometric, briefly.** Drawing 5 cards and counting hearts is **not** binomial, because the probability changes as hearts are removed. The exact formula is $P(X=k)=\dfrac{\binom{13}k\binom{39}{5-k}}{\binom{52}5}$. When the population is much larger than the sample, the binomial is a good approximation.

---

## Summary

| Distribution | PMF | Mean | Variance |
|---|---|---|---|
| Bernoulli($p$) | $p^x(1-p)^{1-x}$ | $p$ | $p(1-p)$ |
| Binomial($n,p$) | $\binom nkp^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ |
| Geometric($p$) | $(1-p)^{k-1}p$ | $1/p$ | $(1-p)/p^2$ |
| Poisson($\lambda$) | $\lambda^ke^{-\lambda}/k!$ | $\lambda$ | $\lambda$ |

**Three facts to remember:**

1. A random variable is a rule that turns outcomes into numbers.
2. Binomial = count successes; geometric = wait for one; Poisson = count rare events in a window.
3. Check independence and constant probability before trusting any of them.

---

## Exercises

### Part A: warm-up

**A1.** A random variable has $p(1)=0.1$, $p(2)=0.3$, $p(3)=0.4$, $p(4)=c$. Find $c$, $P(X\ge3)$ and $F(2)$.

**A2.** A fair coin is flipped 6 times. Find $P(\text{exactly 3 heads})$ and $P(\text{at most 1 head})$.

**A3.** A die is rolled until a 1 appears. Find $P(\text{first 1 on roll 4})$ and the expected number of rolls.

**A4.** Calls arrive at a help desk at 4 per hour. Find $P(\text{no calls in an hour})$ and $P(\text{no calls in 15 minutes})$.

> [!success]- Solutions to Part A
> **A1.** $c=0.2$. $P(X\ge3)=0.6$. $F(2)=0.4$.
>
> **A2.** $\binom63/64=20/64=0.3125$. $(1+6)/64=7/64\approx0.109$.
>
> **A3.** $(5/6)^3(1/6)=125/1296\approx0.0965$. Expected: 6.
>
> **A4.** $e^{-4}\approx0.0183$. For 15 minutes $\lambda=1$: $e^{-1}\approx0.368$.

### Part B: core

**B1.** A grasping policy succeeds with probability 0.7. In 10 independent trials, find $P(X=7)$, $P(X\ge9)$ and the expected number of successes.

**B2.** A sensor gives a false reading with probability 0.01 per measurement. In 500 measurements, use the Poisson approximation to find $P(\text{at most 2 false readings})$.

**B3.** You keep running trials until the first failure, with success probability 0.95 per trial. What is the expected number of trials until a failure? What is $P(\text{no failure in the first 20})$?

**B4.** Two policies are each run 5 times. A succeeds 5 times, B succeeds 3 times. If both truly have success rate 0.8, how likely is a result at least as lopsided as "5 versus 3 or fewer"? (Compute $P(A=5)\times P(B\le3)$.) What does that suggest about comparing policies with 5 trials?

**B5.** From a deck, 5 cards are dealt. Compute $P(\text{exactly 2 hearts})$ exactly (hypergeometric) and with the binomial approximation ($p=1/4$). How far apart are they?

> [!success]- Solutions to Part B
> **B1.** $\binom{10}7(0.7)^7(0.3)^3=120\times0.0824\times0.027\approx0.267$. $P(X\ge9)=10(0.7)^9(0.3)+(0.7)^{10}\approx0.121+0.028=0.149$. Mean $7$.
>
> **B2.** $\lambda=5$. $e^{-5}(1+5+12.5)=18.5e^{-5}\approx0.125$.
>
> **B3.** Failure is the "success" of a geometric with $p=0.05$: expected $20$ trials. $P(\text{no failure in 20})=0.95^{20}\approx0.358$.
>
> **B4.** $P(A=5)=0.328$ and $P(B\le3)\approx0.263$ (from example 3.1). Product $\approx0.086$. So almost 9% of the time, two **identical** policies produce a result that looks like a clear win for one of them. Five trials cannot reliably separate policies.
>
> **B5.** Exact: $\dfrac{\binom{13}2\binom{39}3}{\binom{52}5}=\dfrac{78\times9139}{2598960}\approx0.274$. Binomial: $\binom52(0.25)^2(0.75)^3\approx0.264$. Close, because 5 is small compared with 52.

### Part C: explain and prove

**C1.** Show that the binomial probabilities sum to 1, using the binomial theorem $(a+b)^n=\sum_k\binom nka^kb^{n-k}$.

**C2.** Show that the geometric probabilities sum to 1, using the geometric series $\sum_{k=0}^\infty r^k=\dfrac1{1-r}$ for $|r|<1$.

**C3.** Explain in your own words why the number of heads in 10 flips of a coin whose bias was chosen at random (say, $p$ is 0.2 or 0.8 with equal chance) is **not** binomial.

**C4.** Prove that the Poisson probabilities sum to 1, using $e^\lambda=\sum_{k=0}^\infty\lambda^k/k!$.

> [!success]- Solutions to Part C
> **C1.** $\sum_k\binom nkp^k(1-p)^{n-k}=(p+(1-p))^n=1^n=1$.
>
> **C2.** $\sum_{k\ge1}(1-p)^{k-1}p=p\sum_{j\ge0}(1-p)^j=p\cdot\dfrac1p=1$.
>
> **C3.** Given the bias, flips are independent; but without knowing it, early flips tell you about the bias, which changes your prediction for later flips. The flips are dependent overall (conditionally independent given $p$, as in chapter 2), so assumption 4 fails.
>
> **C4.** $\sum_k\dfrac{\lambda^ke^{-\lambda}}{k!}=e^{-\lambda}e^\lambda=1$.

### Part D: practise with code

**D1.** Use `scipy.stats.binom.pmf(k, n, p)` to reproduce the table in example 3.1, and plot it as a bar chart.

**D2.** Simulate 10,000 evaluations of a 0.8-success policy with 5 trials each (`rng.binomial(5, 0.8, 10000)`). What fraction show 3 or fewer successes? Repeat with 50 trials each. How does the spread of the observed success **rate** change?

**D3.** Compare Binomial(1000, 0.003) with Poisson(3) for $k=0,\dots,10$ on one plot.

**D4.** Simulate the geometric distribution by repeatedly flipping a $p=0.2$ coin until success. Check that the average number of flips is close to 5, and that $P(X>3+2\mid X>3)\approx P(X>2)$.

> [!success]- Hints for Part D
> **D2.** With 5 trials, about 26% of runs show 3 or fewer. With 50 trials, the observed rate clusters much more tightly around 0.8 (spread shrinks like $1/\sqrt n$, chapter 8).

---

## Where this is used

- **Evaluation tables**: success counts are binomial, which is what makes confidence intervals for them possible ([[PS 10 Confidence Intervals and Hypothesis Tests]], [[16 Evaluation and Uncertainty]]).
- **Discrete action policies and classifiers** output categorical distributions ([[05 Training Neural Policies]]).
- **Reliability engineering**: faults per hour (Poisson) and attempts until success (geometric).

Next: [[PS 04 Expectation and Variance]]: summarizing a distribution with two numbers.

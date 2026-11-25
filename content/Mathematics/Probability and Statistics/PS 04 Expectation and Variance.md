---
type: course-chapter
course: probability-statistics
chapter: 4
tags: [mathematics, probability]
---

# Chapter 4: Expectation and variance

Previous: [[PS 03 Discrete Random Variables]] | [[PS 00 Course Map]] | Next: [[PS 05 Continuous Random Variables]]

> [!abstract] The big idea
> Two numbers summarize most of what you need about a random variable. The **expectation** is its probability-weighted average: the balance point, and the long-run average. The **variance** is the average squared distance from that average: how spread out it is. Expectation is **linear** even for dependent variables, which makes hard problems easy. And averaging $n$ independent measurements shrinks the noise by a factor of $\sqrt n$.

> [!info] In this chapter you will learn to
> 1. Compute expectations, including of functions of a random variable.
> 2. Use linearity of expectation and indicator variables to solve counting problems.
> 3. Compute variance and standard deviation, using the shortcut formula.
> 4. Apply the rules for variances of scaled and summed variables.
> 5. Explain and use the square-root law for averages.
> 6. Use Markov's and Chebyshev's inequalities, and conditional expectation.

> [!tip] Before you start
> You need PMFs and the named distributions from [[PS 03 Discrete Random Variables]].

---

## 4.1 Expectation

### Definition

> [!note] Definition: expectation
> The **expectation** (expected value, mean) of a discrete random variable is
> $$
> \mathbb E[X]=\sum_xx\,p(x).
> $$
> Each possible value, weighted by its probability, summed.

Often written $\mu$ (mu).

### Three ways to think about it

1. **Weighted average.** Values that are more likely count more.
2. **Balance point.** Draw the PMF as weights on a ruler; the expectation is where the ruler balances.
3. **Long-run average.** Repeat the experiment many times and average the results; you approach $\mathbb E[X]$ (made precise in [[PS 08 Law of Large Numbers and Central Limit Theorem]]).

### Worked examples

**Worked example 4.1: a die.**

$$
\mathbb E[X]=1\cdot\tfrac16+2\cdot\tfrac16+\cdots+6\cdot\tfrac16=\tfrac{21}6=3.5.
$$

You can never roll 3.5. The expectation is an average, **not a prediction of one outcome**, and not necessarily a possible value.

**Worked example 4.2: a bet.** Win 10 with probability 0.1; lose 1 with probability 0.9.

$$
\mathbb E[\text{gain}]=10(0.1)+(-1)(0.9)=0.1.
$$

On average you gain 0.1 per bet, even though you lose 90% of the time. The rare big win carries the average.

**Worked example 4.3: Bernoulli.** $\mathbb E[X]=1\cdot p+0\cdot(1-p)=p$.

> [!question]- Check yourself
> $X$ takes values $0,1,2$ with probabilities $0.5,0.3,0.2$. Find $\mathbb E[X]$.
>
> **Answer.** $0+0.3+0.4=0.7$.

---

## 4.2 Expectation of a function

To average $g(X)$, weight each $g(x)$ by the probability of $x$:

> [!note] Rule (law of the unconscious statistician)
> $$
> \mathbb E[g(X)]=\sum_xg(x)\,p(x).
> $$

You do not need to find the distribution of $g(X)$ first.

**Worked example 4.4.** For a die, $\mathbb E[X^2]=\tfrac16(1+4+9+16+25+36)=\tfrac{91}6\approx15.17$.

> [!warning] $\mathbb E[g(X)]\neq g(\mathbb E[X])$ in general
> $\mathbb E[X^2]\approx15.17$ but $(\mathbb E[X])^2=3.5^2=12.25$. "Average, then square" is not "square, then average".
>
> Equality holds when $g$ is **linear**, $g(x)=ax+b$. For other functions it usually fails. This is a frequent source of errors in reasoning about averages, for example averaging speeds or ratios.

---

## 4.3 Linearity of expectation

> [!important] Linearity of expectation
> For any random variables $X$, $Y$ and constants $a,b,c$:
> $$
> \mathbb E[aX+bY+c]=a\,\mathbb E[X]+b\,\mathbb E[Y]+c.
> $$
> **This holds whether or not $X$ and $Y$ are independent.**

It is the most useful fact in probability, because it lets you break a complicated quantity into simple pieces whose expectations you can find separately, without ever working out the full distribution.

**Worked example 4.5: sum of two dice.** $\mathbb E[X_1+X_2]=3.5+3.5=7$. No need for the 36-outcome table.

**Worked example 4.6: binomial mean.** A Binomial($n,p$) count is a sum of $n$ Bernoulli variables, $X=X_1+\cdots+X_n$, each with mean $p$. So $\mathbb E[X]=np$. One line, instead of a long sum with binomial coefficients.

### Indicator variables

An **indicator variable** $\mathbf 1_A$ is 1 if event $A$ happens and 0 otherwise. Its expectation is simply the probability of the event:

$$
\mathbb E[\mathbf 1_A]=1\cdot P(A)+0\cdot P(A^c)=P(A).
$$

> [!tip] The indicator method
> To find the expected **number** of things that happen: write the count as a sum of indicators, one per thing, then add up their probabilities.

**Worked example 4.7: the hat-check problem.** $n$ people check their hats; the hats are handed back in random order. What is the expected number of people who get their own hat?

Let $X_i=1$ if person $i$ gets their own hat. Each person is equally likely to receive any of the $n$ hats, so $P(X_i=1)=1/n$. The count is $X=X_1+\cdots+X_n$, and

$$
\mathbb E[X]=n\cdot\frac1n=1.
$$

**One person on average, whatever $n$ is.** The $X_i$ are dependent (if the first $n-1$ people got their own hats, so did the last), but linearity does not care.

**Worked example 4.8: distinct values.** Roll a die 6 times. Expected number of distinct faces seen? Let $Y_j=1$ if face $j$ appears at least once. $P(Y_j=1)=1-(5/6)^6\approx0.665$. So the expected number of distinct faces is $6\times0.665\approx3.99$. Rolling 6 times usually shows only about 4 different faces.

> [!question]- Check yourself
> In a class of 30, each student's birthday is one of 365 days at random. What is the expected number of pairs of students sharing a birthday?
>
> **Answer.** $\binom{30}2=435$ pairs, each matching with probability $1/365$: $435/365\approx1.19$.

---

## 4.4 Variance and standard deviation

### Why we need a second number

The values $\{4,6\}$ and $\{0,10\}$ (each equally likely) both have mean 5, but the second is far more spread out. Variance measures spread.

> [!note] Definition: variance
> $$
> \operatorname{Var}(X)=\mathbb E\big[(X-\mu)^2\big],\qquad\mu=\mathbb E[X].
> $$
> The **standard deviation** is $\sigma=\sqrt{\operatorname{Var}(X)}$.

**Why square the deviations?** Without squaring, positive and negative deviations cancel ($\mathbb E[X-\mu]=0$ always). Squaring makes them all count, and penalizes large deviations more.

**Why take the square root?** Variance has **squared units** (metres squared, if $X$ is in metres). The standard deviation is back in the original units, so it is the one to report.

### The shortcut formula

Expanding the square and using linearity:

$$
\mathbb E[(X-\mu)^2]=\mathbb E[X^2]-2\mu\,\mathbb E[X]+\mu^2=\mathbb E[X^2]-\mu^2.
$$

> [!important] Shortcut
> $$
> \operatorname{Var}(X)=\mathbb E[X^2]-\big(\mathbb E[X]\big)^2.
> $$
> "Mean of the square minus square of the mean."

### Worked examples

**Worked example 4.9: a die.** $\mathbb E[X^2]=\tfrac{91}6$, $\mu=3.5$:

$$
\operatorname{Var}(X)=15.167-12.25=2.917,\qquad\sigma\approx1.71.
$$

**Worked example 4.10: Bernoulli.** $X^2=X$ (since $0^2=0$, $1^2=1$), so $\mathbb E[X^2]=p$ and $\operatorname{Var}(X)=p-p^2=p(1-p)$.

**Worked example 4.11: the two spreads.** $\{4,6\}$: deviations $\pm1$, variance 1, $\sigma=1$. $\{0,10\}$: deviations $\pm5$, variance 25, $\sigma=5$.

---

## 4.5 Rules for variance

### Scaling and shifting

$$
\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X),\qquad\operatorname{sd}(aX+b)=|a|\operatorname{sd}(X).
$$

- **Shifting** by $b$ moves every value equally; the spread does not change.
- **Scaling** by $a$ stretches every deviation by $a$, so squared deviations by $a^2$.

**Example.** Temperatures in Celsius have $\sigma=5$. In Fahrenheit ($F=1.8C+32$), $\sigma=9$.

### Sums of independent variables

> [!important] Variances add for independent variables
> If $X$ and $Y$ are independent,
> $$
> \operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y),
> $$
> $$
> \operatorname{Var}(X-Y)=\operatorname{Var}(X)+\operatorname{Var}(Y).
> $$

Notice the second line: **variances add even when you subtract**. Uncertainty never cancels; combining two uncertain quantities, in either direction, makes the result more uncertain.

This rule needs independence (more precisely, zero covariance). The general formula with a covariance term is in [[PS 06 Joint Distributions and Covariance]].

**Standard deviations do not add.** They combine like the sides of a right triangle:

$$
\operatorname{sd}(X+Y)=\sqrt{\sigma_X^2+\sigma_Y^2}.
$$

**Worked example 4.12.** Two independent sensors each have noise $\sigma=3$ mm. The difference of their readings has $\sigma=\sqrt{9+9}\approx4.24$ mm, not 6 and not 0.

**Worked example 4.13: binomial variance.** $X=X_1+\cdots+X_n$, independent Bernoullis each with variance $p(1-p)$: $\operatorname{Var}(X)=np(1-p)$.

---

## 4.6 The square-root law for averages

This is one of the most important results in the course.

Take $n$ independent measurements $X_1,\dots,X_n$, each with mean $\mu$ and variance $\sigma^2$. Their average is

$$
\bar X=\frac1n(X_1+\cdots+X_n).
$$

**Mean:** by linearity, $\mathbb E[\bar X]=\tfrac1n\cdot n\mu=\mu$. The average aims at the right value.

**Variance:** the sum has variance $n\sigma^2$ (independence), and dividing by $n$ divides the variance by $n^2$:

$$
\operatorname{Var}(\bar X)=\frac{n\sigma^2}{n^2}=\frac{\sigma^2}n,\qquad\operatorname{sd}(\bar X)=\frac{\sigma}{\sqrt n}.
$$

> [!important] The square-root law
> Averaging $n$ independent measurements reduces the noise by a factor of $\sqrt n$.
> - To halve the error, you need **4 times** the data.
> - To gain one more decimal digit of accuracy, you need **100 times** the data.

This single fact explains why careful evaluation is expensive, why mini-batch gradients are noisy, and why more data gives diminishing returns.

**Worked example 4.14.** A sensor has noise $\sigma=2$ cm. To get the average's noise down to $0.5$ cm, solve $2/\sqrt n=0.5$: $n=16$ readings. To get to $0.1$ cm: $n=400$.

---

## 4.7 Two inequalities that need almost no assumptions

### Markov's inequality

For a **non-negative** random variable and any $a>0$:

$$
P(X\ge a)\le\frac{\mathbb E[X]}a.
$$

*Why:* $X\ge a\cdot\mathbf 1_{X\ge a}$ (when $X\ge a$ the right side is $a\le X$; otherwise it is $0\le X$). Take expectations: $\mathbb E[X]\ge a\,P(X\ge a)$.

**Example.** If a robot's average task time is 30 s, at most $30/120=25\%$ of tasks can take 120 s or more, whatever the distribution.

### Chebyshev's inequality

For any random variable with finite variance, and any $k>0$:

$$
P\big(|X-\mu|\ge k\sigma\big)\le\frac1{k^2}.
$$

*Why:* apply Markov to the non-negative variable $(X-\mu)^2$ with $a=k^2\sigma^2$.

| $k$ | at most this much probability lies $k\sigma$ or more from the mean |
|---|---|
| 2 | 25% |
| 3 | 11% |
| 10 | 1% |

These bounds are **weak** (for a normal distribution the true numbers are 5%, 0.3% and essentially 0), but they hold for **every** distribution, which makes them valuable in proofs.

---

## 4.8 Conditional expectation

$\mathbb E[X\mid Y=y]$ is the average of $X$ in the world where $Y=y$: compute it with the conditional distribution of $X$ given $Y=y$.

> [!important] Law of total expectation
> $$
> \mathbb E[X]=\sum_y\mathbb E[X\mid Y=y]\,P(Y=y).
> $$
> The overall average is the weighted average of the averages within each case.

**Worked example 4.15.** A robot handles light boxes (60% of jobs, average 20 s) and heavy boxes (40%, average 45 s). Average job time: $0.6(20)+0.4(45)=30$ s.

**Worked example 4.16 (geometric mean, by conditioning).** Let $X$ be the number of trials until the first success. Condition on the first trial: with probability $p$ it succeeds ($X=1$); with probability $1-p$ it fails, and because the process has no memory, you start over having used one trial:

$$
\mathbb E[X]=p\cdot1+(1-p)\,(1+\mathbb E[X]).
$$

Solve: $\mathbb E[X]=1/p$. This "condition on the first step" trick is the same idea as the Bellman equation in reinforcement learning ([[09 Reinforcement Learning]]).

---

## Summary

| Idea | Formula |
|---|---|
| expectation | $\mathbb E[X]=\sum xp(x)$ |
| function | $\mathbb E[g(X)]=\sum g(x)p(x)$ |
| linearity | $\mathbb E[aX+bY+c]=a\mathbb E[X]+b\mathbb E[Y]+c$ (always) |
| indicators | $\mathbb E[\mathbf 1_A]=P(A)$ |
| variance | $\mathbb E[X^2]-\mu^2$ |
| scaling | $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$ |
| independent sum | variances add |
| average of $n$ | sd $=\sigma/\sqrt n$ |
| Chebyshev | $P(\lvert X-\mu\rvert\ge k\sigma)\le1/k^2$ |

**Three facts to remember:**

1. Expectation is linear, always, even with dependence.
2. Variances add for independent variables; standard deviations do not.
3. Averaging $n$ samples cuts the noise by $\sqrt n$.

---

## Exercises

### Part A: warm-up

**A1.** $X$ takes values $-1,0,2$ with probabilities $0.2,0.5,0.3$. Find $\mathbb E[X]$, $\mathbb E[X^2]$ and $\operatorname{Var}(X)$.

**A2.** If $\operatorname{Var}(X)=4$, find $\operatorname{Var}(3X+7)$ and $\operatorname{sd}(3X+7)$.

**A3.** Roll 10 dice. Find the mean and variance of the total.

**A4.** $X\sim$ Binomial(20, 0.3). Find $\mathbb E[X]$ and $\operatorname{sd}(X)$.

> [!success]- Solutions to Part A
> **A1.** $\mathbb E[X]=-0.2+0+0.6=0.4$. $\mathbb E[X^2]=0.2+0+1.2=1.4$. $\operatorname{Var}=1.4-0.16=1.24$.
>
> **A2.** $36$; $6$.
>
> **A3.** Mean $35$; variance $10\times2.917\approx29.2$.
>
> **A4.** $6$; $\sqrt{20\times0.3\times0.7}=\sqrt{4.2}\approx2.05$.

### Part B: core

**B1.** A sensor has noise standard deviation 2 cm. How many independent readings must be averaged to reach 0.25 cm?

**B2.** A robot picks from a bin of 10 objects, 3 of which are fragile. It picks 4 at random without replacement. Find the expected number of fragile objects picked, using indicators.

**B3.** Two independent quantities: a link length with mean 30 cm and sd 0.2 cm, and a second link with mean 25 cm and sd 0.1 cm. Find the mean and sd of the total length.

**B4.** A game pays $X^2$ where $X$ is a die roll. What is a fair price to play? Compare with $(\mathbb E[X])^2$.

**B5.** Average task time is 40 s with standard deviation 5 s. Use Chebyshev to bound the probability that a task takes more than 55 s or less than 25 s.

**B6.** You flip a fair coin until you see two heads in a row. Using conditioning on the first one or two flips, find the expected number of flips.

> [!success]- Solutions to Part B
> **B1.** $2/\sqrt n=0.25$, so $\sqrt n=8$, $n=64$.
>
> **B2.** Indicator for each fragile object being picked: probability $4/10$. Expected: $3\times0.4=1.2$.
>
> **B3.** Mean $55$ cm; sd $\sqrt{0.04+0.01}=\sqrt{0.05}\approx0.224$ cm.
>
> **B4.** $\mathbb E[X^2]=91/6\approx15.17$. $(\mathbb E[X])^2=12.25$. The fair price is 15.17.
>
> **B5.** 55 and 25 are $3\sigma$ from the mean: probability at most $1/9\approx0.111$.
>
> **B6.** Let $E$ be the expected number. First flip T (prob $\tfrac12$): used 1, start over. First H then T (prob $\tfrac14$): used 2, start over. HH (prob $\tfrac14$): done in 2. So $E=\tfrac12(1+E)+\tfrac14(2+E)+\tfrac14(2)$. Then $E=\tfrac12+\tfrac E2+\tfrac12+\tfrac E4+\tfrac12$, so $\tfrac E4=1.5$ and $E=6$.

### Part C: explain and prove

**C1.** Prove $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$ from the definition.

**C2.** Prove that $\operatorname{Var}(X)\ge0$, and that it equals 0 only if $X$ is constant (with probability 1).

**C3.** Explain why $\mathbb E[1/X]\neq1/\mathbb E[X]$ in general, with a two-value example. Why does this matter when averaging speeds?

**C4.** Explain why the hat-check answer (1) does not depend on $n$, in your own words.

> [!success]- Solutions to Part C
> **C1.** $\mathbb E[aX+b]=a\mu+b$, so $(aX+b)-(a\mu+b)=a(X-\mu)$. Squaring and taking expectations: $a^2\mathbb E[(X-\mu)^2]$.
>
> **C2.** It is the expectation of a square, which is non-negative. It is zero only if $(X-\mu)^2=0$ with probability 1, i.e. $X=\mu$.
>
> **C3.** $X=1$ or $3$ equally: $\mathbb E[1/X]=\tfrac12(1+\tfrac13)=\tfrac23$, but $1/\mathbb E[X]=\tfrac12$. Driving equal **distances** at 30 and 90 km/h gives an average speed of 45, not 60, because the slow leg takes longer.
>
> **C4.** More people means more chances for a match, but each person's chance falls to $1/n$. The two effects cancel exactly.

### Part D: practise with code

**D1.** Simulate 100,000 die rolls and compare the sample mean and variance with 3.5 and 2.917.

**D2.** Simulate the hat-check problem for $n=5,10,100$ (shuffle with `rng.permutation(n)` and count fixed points). Check the average is close to 1.

**D3.** For $n=1,4,16,64,256$, draw 10,000 averages of $n$ standard normal samples and compute their standard deviation. Plot against $n$ on log-log axes. What slope do you see?

**D4.** Simulate B6 (flips until two heads in a row) and check that the average is near 6.

> [!success]- Hints for Part D
> **D3.** The points lie on a line of slope $-\tfrac12$: the standard deviation is proportional to $n^{-1/2}$.

---

## Where this is used

- A **training loss** is an expectation over data. A mini-batch gradient estimates it, with noise shrinking like $1/\sqrt{\text{batch size}}$ ([[05 Training Neural Policies]]).
- **Expected return** is the objective of reinforcement learning, and value functions are conditional expectations ([[09 Reinforcement Learning]]).
- **Error budgets**: independent error sources add in variance, which is how tolerances in a robot's kinematic chain are combined.

Next: [[PS 05 Continuous Random Variables]]: measurements that can take any value.

---
type: course-chapter
course: probability-statistics
chapter: 10
tags: [mathematics, statistics, inference]
---

# Chapter 10: Confidence intervals and hypothesis tests

Previous: [[PS 09 Estimation and Maximum Likelihood]] | [[PS 00 Course Map]] | Next: [[PS 11 Bayesian Inference]]

> [!abstract] The big idea
> A single estimate ("the success rate is 0.8") is incomplete without a statement of how uncertain it is. A **confidence interval** gives a range of parameter values that are compatible with the data. A **hypothesis test** asks whether an observed effect could plausibly be produced by chance alone. Both rest on the standard error from the central limit theorem, and both are frequently misread, so this chapter spends as much time on what they **do not** mean as on how to compute them.

> [!info] In this chapter you will learn to
> 1. Build and interpret confidence intervals for a mean and for a proportion.
> 2. Use the $t$ distribution for small samples, and better intervals for proportions.
> 3. Build intervals by the bootstrap when no formula exists.
> 4. Run a hypothesis test, compute a p-value, and interpret it correctly.
> 5. Understand Type I and II errors, power and sample size.
> 6. Compare two groups (independent or paired) and avoid the multiple-comparisons trap.

> [!tip] Before you start
> You need the CLT and standard errors ([[PS 08 Law of Large Numbers and Central Limit Theorem]]) and z-scores with the table of $\Phi$ ([[PS 05 Continuous Random Variables]]). Key values: $1.645$ (90%), $1.96$ (95%), $2.576$ (99%).

---

## 10.1 Confidence intervals for a mean

### The construction

By the CLT, the sample mean is approximately $\mathcal N(\mu,\sigma^2/n)$. So 95% of the time,

$$
|\bar x-\mu|\le1.96\,\frac{\sigma}{\sqrt n}.
$$

Read the same inequality the other way round: 95% of the time, **$\mu$ is within $1.96$ standard errors of $\bar x$**. Replacing the unknown $\sigma$ by the sample standard deviation $s$:

> [!important] Approximate 95% confidence interval for a mean
> $$
> \bar x\;\pm\;1.96\,\frac{s}{\sqrt n}.
> $$

Every confidence interval in this chapter has the same shape:

$$
\text{estimate}\;\pm\;(\text{critical value})\times(\text{standard error}).
$$

| Confidence level | 90% | 95% | 99% |
|---|---|---|---|
| critical value $z^*$ | 1.645 | 1.96 | 2.576 |

More confidence costs a **wider** interval. More data buys a **narrower** one (by $\sqrt n$).

### Worked example 10.1

100 cycle-time measurements give $\bar x=5.2$ s and $s=0.8$ s.

- Standard error: $0.8/\sqrt{100}=0.08$ s.
- Margin: $1.96\times0.08\approx0.157$ s.
- 95% interval: $5.2\pm0.157$, that is $[5.04,\;5.36]$ s.

---

## 10.2 What "95% confidence" means

> [!warning] The most misread statement in statistics
> It does **not** mean "there is a 95% probability that $\mu$ is in $[5.04,\,5.36]$".
>
> In this (frequentist) framework, $\mu$ is a fixed number. It is either in that particular interval or it is not. There is nothing random left about it.
>
> What is random is the **interval**: a different sample would give a different one.

**The correct meaning.** The **procedure** produces intervals that contain the true value in 95% of repeated experiments. Picture 100 research teams each collecting their own data and computing their own interval: about 95 of the intervals contain the truth, and about 5 miss it. You do not know which kind yours is.

**Practical reading.** Values inside the interval are **compatible** with the data. Values far outside are not. The width tells you how precisely you have measured.

(If you want a statement like "95% probability that $\mu$ is here", you need a prior and a **credible interval**, [[PS 11 Bayesian Inference]].)

---

## 10.3 Small samples: the $t$ distribution

With small $n$, replacing $\sigma$ by $s$ adds extra uncertainty: $s$ itself might be too small or too large. To account for it, use the **$t$ distribution with $n-1$ degrees of freedom**, which looks like a normal but with heavier tails.

$$
\bar x\pm t^*_{n-1}\,\frac s{\sqrt n}.
$$

| $n$ | 3 | 5 | 10 | 20 | 30 | large |
|---|---|---|---|---|---|---|
| 95% $t^*$ | 4.303 | 2.776 | 2.262 | 2.093 | 2.045 | 1.96 |

With $n=5$ the interval is about 40% wider than the normal version would claim. With 3 data points it is more than twice as wide. Small samples carry much less information than intuition suggests.

This interval assumes the data are roughly normal. With small, skewed samples, be cautious.

**Worked example 10.2.** Five measurements of a gripper force: $\bar x=12.0$ N, $s=1.5$ N. Standard error $1.5/\sqrt5\approx0.671$. Interval: $12.0\pm2.776\times0.671=12.0\pm1.86$, so $[10.14,\;13.86]$ N.

---

## 10.4 Intervals for a proportion

### The simple (Wald) interval

With $k$ successes in $n$ trials, $\hat p=k/n$, and the CLT gives

$$
\hat p\;\pm\;1.96\sqrt{\frac{\hat p(1-\hat p)}n}.
$$

**Worked example 10.3.** 40 successes in 50 trials: $\hat p=0.8$, SE $=\sqrt{0.16/50}\approx0.057$, interval $0.8\pm0.111=[0.69,\;0.91]$.

### When it fails

> [!warning] The Wald interval breaks near 0, near 1, and for small $n$
> With 10 successes in 10 trials, $\hat p=1$, the standard error is computed as $0$, and the interval is $[1,1]$: it claims **certainty** that the policy never fails, from only 10 tries.

### Better: the Wilson interval

The Wilson interval fixes this and should be the default for success rates:

$$
\frac{\hat p+\dfrac{z^2}{2n}\pm z\sqrt{\dfrac{\hat p(1-\hat p)}n+\dfrac{z^2}{4n^2}}}{1+\dfrac{z^2}n},\qquad z=1.96.
$$

For 10 out of 10 it gives roughly $[0.72,\;1]$: a perfect score on 10 trials is consistent with a true rate as low as about 72%.

### The rule of three

If you observe **zero** failures in $n$ independent trials, an approximate 95% upper bound on the failure rate is

$$
\frac3n.
$$

0 failures in 30 trials: the failure rate could still be as high as about 10%. 0 in 300: about 1%.

*Why:* the chance of 0 failures in $n$ trials at failure rate $q$ is $(1-q)^n\approx e^{-qn}$. Setting it to 0.05 gives $qn\approx3$.

---

## 10.5 The bootstrap: intervals without formulas

For statistics with no convenient standard-error formula (a median, a ratio, a model's accuracy, the difference in success rates on a benchmark), use the **bootstrap**:

1. From your $n$ data points, draw $n$ points **with replacement**. This is a "bootstrap sample": some points appear twice, some not at all.
2. Compute the statistic on it.
3. Repeat steps 1 and 2 a few thousand times.
4. Take the 2.5th and 97.5th percentiles of the results as a 95% interval.

**Why it works.** You cannot repeat the real experiment, so you use your sample as a stand-in for the population and repeat the **sampling** process on it. The spread of the resampled statistics imitates the spread you would see across real repeated experiments.

> [!tip] Resample independent units
> If each robot episode contains many frames, resample whole **episodes**, not frames. Resampling correlated pieces separately makes the interval far too narrow (the same mistake as in [[PS 08 Law of Large Numbers and Central Limit Theorem]]).

---

## 10.6 Hypothesis tests

### The question

You observe an effect: a coin gives 60 heads in 100 flips; a new policy scores higher than the old one. **Could chance alone produce an effect this large?**

### The setup

- **Null hypothesis $H_0$**: the "nothing interesting" explanation. The coin is fair; the policies are equally good.
- **Alternative hypothesis $H_1$**: what you suspect instead. The coin is biased; the new policy is better.

### The logic

It is **proof by contradiction, made probabilistic**:

1. Assume $H_0$ is true.
2. Compute how surprising the observed data would be under that assumption.
3. If the data would be very surprising, doubt $H_0$.

### The p-value

> [!note] Definition: p-value
> The **p-value** is the probability, **assuming $H_0$ is true**, of getting data **at least as extreme** as what was actually observed.

A small p-value says: "if $H_0$ were true, results like these would be rare."

### The decision

Choose a **significance level** $\alpha$ **before** looking at the data (commonly $\alpha=0.05$). If $p<\alpha$, **reject** $H_0$. Otherwise, **do not reject** it (which is not the same as accepting it).

### Worked example 10.4: is the coin fair?

60 heads in 100 flips.

**Step 1: $H_0$.** The coin is fair, $p=0.5$.

**Step 2: distribution under $H_0$.** Number of heads $\approx\mathcal N(50,\;100\times0.25)$, so mean 50, sd 5.

**Step 3: how extreme?** $z=\dfrac{60-50}5=2.0$.

**Step 4: p-value.** "At least as extreme" in **either** direction (a two-sided test, since a bias could go either way): $P(|Z|\ge2)=2\times0.0228\approx0.046$.

**Step 5: decide.** $0.046<0.05$: reject fairness at the 5% level, but only just.

With 55 heads instead: $z=1$, $p\approx0.32$. Entirely ordinary for a fair coin.

---

## 10.7 What a p-value is not

> [!warning] Three common misreadings
> 1. **It is not the probability that $H_0$ is true.** It is $P(\text{data}\mid H_0)$, not $P(H_0\mid\text{data})$. Confusing them is the same error as the prosecutor's fallacy ([[PS 02 Conditional Probability and Bayes Rule]]).
> 2. **A large p-value does not show $H_0$ is true.** It only says the data cannot rule it out. With small samples, real effects routinely produce large p-values. Absence of evidence is not evidence of absence.
> 3. **A small p-value does not mean the effect is large or important.** With enough data, a trivially small difference becomes "statistically significant". Always report the **size** of the effect with its confidence interval.

---

## 10.8 Errors and power

Every test can go wrong in two ways:

| | $H_0$ actually true | $H_0$ actually false |
|---|---|---|
| **reject $H_0$** | **Type I error** (false alarm). Rate $=\alpha$ | correct. Rate $=$ **power** |
| **do not reject** | correct | **Type II error** (missed effect). Rate $=\beta$ |

**Power** $=1-\beta$ is the probability of detecting an effect that really exists. It increases with:

- a **larger sample**,
- a **larger true effect**,
- **less noise**,
- a larger $\alpha$ (at the cost of more false alarms).

> [!warning] Underpowered studies mislead twice
> A study with low power usually misses real effects. Worse, the "significant" results it does produce tend to **exaggerate** the effect, because only lucky, unusually large estimates cross the threshold.

### How many trials do you need?

To detect a difference $\Delta$ between two success rates near $p$, with about 80% power at $\alpha=0.05$, a rough rule is

$$
n\approx\frac{16\,p(1-p)}{\Delta^2}\quad\text{per group}.
$$

To distinguish 70% from 80% ($\Delta=0.1$, $p\approx0.75$): $n\approx16\times0.1875/0.01=300$ trials **per policy**. Detecting a 10-point improvement is expensive.

---

## 10.9 Comparing two groups

### Independent groups

For two independent groups with means $\bar x_1,\bar x_2$, the standard error of the difference adds in variance ([[PS 04 Expectation and Variance]]):

$$
\operatorname{SE}(\bar x_1-\bar x_2)=\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}.
$$

Test statistic: $z=(\bar x_1-\bar x_2)/\operatorname{SE}$. Interval: $(\bar x_1-\bar x_2)\pm1.96\,\operatorname{SE}$.

For proportions, use $s^2=\hat p(1-\hat p)$ for each group.

**Worked example 10.5.** Policy A: 80/100. Policy B: 70/100.

- Difference $0.10$.
- SE $=\sqrt{\tfrac{0.16}{100}+\tfrac{0.21}{100}}=\sqrt{0.0037}\approx0.061$.
- $z\approx1.64$, two-sided $p\approx0.10$. Not significant at 5%.
- 95% interval for the difference: $0.10\pm0.12$, so $[-0.02,\;0.22]$. It includes zero: A might be no better at all, or up to 22 points better.

### Paired comparisons

If the **same units** are measured under both conditions (the same 50 object placements tried with policy A and with policy B), analyse the **differences** within each pair.

Pairing removes the variation **between units** (some placements are simply harder), which can be large. The test on differences is usually far more sensitive.

> [!tip] Design evaluations to be paired
> Test both policies on the same set of initial conditions. It costs nothing extra and can cut the required number of trials dramatically.

---

## 10.10 Tests and intervals agree

A two-sided test at level $\alpha=0.05$ rejects $H_0:\mu=\mu_0$ **exactly when** $\mu_0$ lies **outside** the 95% confidence interval.

So the interval contains everything the test tells you, plus the size of the effect and the precision of the measurement. **Prefer reporting intervals.**

---

## 10.11 The multiple-comparisons trap

If you test 20 hypotheses that are all actually null, at $\alpha=0.05$ each, you expect **one** false positive.

The same happens when you try many metrics, many random seeds, many checkpoints or many hyperparameter settings, and report the best one. Something will look significant by chance.

**Remedies:**

- Decide the main comparison **before** looking at the data.
- **Correct** for the number of tests. The simplest is **Bonferroni**: with $m$ tests, use $\alpha/m$ for each.
- Report **everything** you tried, not just the winner.
- Confirm the finding on **fresh** data.

---

## Summary

| Task | Formula |
|---|---|
| CI for a mean | $\bar x\pm1.96\,s/\sqrt n$ (or $t^*$ for small $n$) |
| CI for a proportion | Wilson interval (Wald: $\hat p\pm1.96\sqrt{\hat p(1-\hat p)/n}$) |
| zero failures in $n$ | upper bound $\approx3/n$ |
| test statistic | $z=(\text{estimate}-\text{null value})/\operatorname{SE}$ |
| difference of two groups | $\operatorname{SE}=\sqrt{s_1^2/n_1+s_2^2/n_2}$ |
| sample size (two proportions) | $n\approx16p(1-p)/\Delta^2$ per group |

**Three facts to remember:**

1. A 95% interval comes from a procedure that is right 95% of the time; it is not a probability about $\mu$.
2. A p-value is $P(\text{data this extreme}\mid H_0)$: not the chance $H_0$ is true, and not the size of the effect.
3. Pair your comparisons, plan your sample size, and report intervals.

---

## Exercises

### Part A: warm-up

**A1.** $n=64$, $\bar x=12$, $s=4$. Give a 95% confidence interval for the mean.

**A2.** A policy succeeds 45 times in 60 trials. Give a 95% Wald interval for its success rate.

**A3.** A new gripper has 0 failures in 50 trials. Give an approximate 95% upper bound on its failure rate.

**A4.** With $n=10$, $\bar x=3.4$, $s=0.6$, give a 95% interval using the $t$ distribution.

> [!success]- Solutions to Part A
> **A1.** $12\pm1.96\times0.5=[11.02,\;12.98]$.
>
> **A2.** $\hat p=0.75$, SE $=\sqrt{0.1875/60}\approx0.056$, interval $\approx[0.64,\;0.86]$.
>
> **A3.** $3/50=0.06$, i.e. 6%.
>
> **A4.** SE $=0.6/\sqrt{10}\approx0.190$. $3.4\pm2.262\times0.190=3.4\pm0.429$: $[2.97,\;3.83]$.

### Part B: core

**B1.** A coin gives 530 heads in 1,000 flips. Test fairness at $\alpha=0.05$ and give a 95% interval for $p$.

**B2.** Policy A succeeds 85/100; policy B succeeds 75/100. Test whether they differ, and give a 95% interval for the difference.

**B3.** The same 20 object placements are tried with two policies. In 6 placements only A succeeds; in 1 only B succeeds; in the other 13 both succeed or both fail. Is this evidence that A is better? (Hint: under $H_0$, each of the 7 "disagreeing" placements is equally likely to favour A or B. Compute $P(\text{6 or more of 7 favour A})$ with the binomial.)

**B4.** You want to detect an improvement from 60% to 70% success with 80% power. Roughly how many trials per policy are needed?

**B5.** A paper reports $p=0.03$ for an improvement of 0.2 percentage points on a benchmark with 100,000 test examples. What two questions should you ask?

> [!success]- Solutions to Part B
> **B1.** SE under $H_0$: $\sqrt{0.25/1000}\approx0.0158$. $z=0.03/0.0158\approx1.90$, $p\approx0.057$: not significant at 5%. Interval: $0.53\pm1.96\sqrt{0.53\times0.47/1000}=0.53\pm0.031$, so $[0.499,\;0.561]$, which just includes 0.5. Consistent with the test.
>
> **B2.** Difference $0.10$. SE $=\sqrt{0.1275/100+0.1875/100}\approx0.056$. $z\approx1.78$, $p\approx0.075$. Interval $0.10\pm0.11=[-0.01,\;0.21]$. Not significant at 5%.
>
> **B3.** $P(\ge6\text{ of }7)=\binom76(\tfrac12)^7+(\tfrac12)^7=\tfrac{8}{128}=0.0625$ one-sided; two-sided $0.125$. Suggestive but not significant. (This is McNemar's test. Note that only the disagreeing placements carry information.)
>
> **B4.** $p\approx0.65$, $\Delta=0.1$: $n\approx16\times0.2275/0.01\approx364$ per policy.
>
> **B5.** Is a 0.2-point effect of any practical importance? And how many models, seeds or settings were tried before this one was reported (multiple comparisons)?

### Part C: explain and prove

**C1.** Explain to a friend, without formulas, what a 95% confidence interval is.

**C2.** Explain why a test can be "significant" with a huge sample even when the effect is negligible, using the formula for the standard error.

**C3.** Why does pairing reduce the standard error of a comparison? Use the formula $\operatorname{Var}(X-Y)=\operatorname{Var}X+\operatorname{Var}Y-2\operatorname{Cov}(X,Y)$.

**C4.** Derive the rule of three from $(1-q)^n=0.05$ using $\ln(1-q)\approx-q$ for small $q$.

> [!success]- Solutions to Part C
> **C1.** "I used a method that, if everyone repeated my experiment with fresh data, would capture the true value about 95 times out of 100. This particular range is what the method gave for my data."
>
> **C2.** SE $=\sigma/\sqrt n$ shrinks without limit as $n$ grows, so any nonzero difference, however tiny, eventually becomes many standard errors from zero.
>
> **C3.** Outcomes of the same unit under two conditions are positively correlated (hard placements are hard for both). The covariance term is subtracted, shrinking the variance of the difference.
>
> **C4.** $n\ln(1-q)=\ln0.05\approx-3$, and $\ln(1-q)\approx-q$, so $nq\approx3$.

### Part D: practise with code

**D1.** Simulate 100 experiments, each drawing 30 samples from $\mathcal N(10,4)$ and computing a 95% interval. Plot the intervals and count how many contain 10.

**D2.** Implement the Wilson interval and compare it with the Wald interval for $k=0,1,\dots,10$ successes out of $n=10$.

**D3.** Implement a bootstrap interval for the **median** of a sample, and for the difference in success rates between two policies with per-episode results.

**D4.** Simulate the multiple-comparisons trap: 20 "metrics" that are pure noise for two identical policies, each tested at $\alpha=0.05$. Over 1,000 repetitions, how often is at least one metric "significant"?

> [!success]- Hints for Part D
> **D1.** About 95 of 100 intervals contain 10, but the exact count varies from run to run.
>
> **D4.** About $1-0.95^{20}\approx64\%$ of repetitions show at least one false positive.

---

## Where this is used

This chapter is the statistical core of [[16 Evaluation and Uncertainty]]. Before claiming one policy beats another, check: the interval on the **difference**, whether trials were **independent** and **paired**, whether the sample size gives enough **power**, and how many comparisons were made.

Next: [[PS 11 Bayesian Inference]]: keeping a full probability distribution over what you do not know.

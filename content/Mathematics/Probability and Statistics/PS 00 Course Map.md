---
type: course-home
course: probability-statistics
tags: [mathematics, probability, statistics, course]
created: 2026-11-17
---
# Probability and statistics: course map

[[Mathematics Courses]] | Start: [[PS 01 Sample Spaces Events and Axioms]]

**Probability** starts from a model and asks what data it will produce. **Statistics** runs the other way: it starts from data and asks which model produced it. The first half of this course is probability, the second half is statistics, and the last chapter covers two tools that robot learning uses constantly.

> [!tip] How to study this course
> Probability punishes intuition. For every worked example, write down the sample space or the distribution before computing anything. If a result surprises you, simulate it: ten lines of NumPy settle most arguments.

## Chapters

| Chapter | The question it answers |
|---|---|
| [[PS 01 Sample Spaces Events and Axioms]] | What is a probability, precisely? |
| [[PS 02 Conditional Probability and Bayes Rule]] | How should evidence change a belief? |
| [[PS 03 Discrete Random Variables]] | How do I describe a random count? |
| [[PS 04 Expectation and Variance]] | What is the typical value, and how spread out is it? |
| [[PS 05 Continuous Random Variables]] | How do I describe a random measurement? |
| [[PS 06 Joint Distributions and Covariance]] | How do two random quantities move together? |
| [[PS 07 The Multivariate Gaussian]] | What is the workhorse model of uncertainty in many dimensions? |
| [[PS 08 Law of Large Numbers and Central Limit Theorem]] | Why do averages settle down, and how fast? |
| [[PS 09 Estimation and Maximum Likelihood]] | How do I fit a model to data? |
| [[PS 10 Confidence Intervals and Hypothesis Tests]] | How sure am I, and is this effect real? |
| [[PS 11 Bayesian Inference]] | How do I keep a full distribution over what I do not know? |
| [[PS 12 Markov Chains and Information]] | How do I model sequences, and measure surprise? |

## Dependencies

- 1 to 6 in order. Chapter 3 uses counting from [[DM 07 Counting]].
- Chapter 7 needs [[LA 09 Symmetric and Positive Definite Matrices]].
- Chapters 9 to 11 need 8.
- Chapter 12 needs 2 and 4, plus [[LA 08 Eigenvalues and Eigenvectors]] for one section.

## Notation

| Symbol | Meaning |
|---|---|
| $P(A)$ | probability of event $A$ |
| $P(A\mid B)$ | probability of $A$ given that $B$ happened |
| $X,Y$ | random variables (upper case); $x,y$ are specific values |
| $p(x)$ | probability mass function, or density when $X$ is continuous |
| $F(x)$ | cumulative distribution function, $P(X\le x)$ |
| $\mathbb E[X]$, $\mu$ | expectation (mean) |
| $\operatorname{Var}(X)$, $\sigma^2$ | variance; $\sigma$ is the standard deviation |
| $X\sim\mathcal N(\mu,\sigma^2)$ | "$X$ is distributed as" a normal with that mean and variance |
| $\hat\theta$ | an estimate of the unknown $\theta$ computed from data |

## Checkpoint questions for the whole course

1. Why is $P(A\mid B)$ generally different from $P(B\mid A)$, and how does Bayes' rule connect them?
2. Why does variance add for independent variables but standard deviation does not?
3. Why does the error of an average shrink like $1/\sqrt n$?
4. What exactly does a 95% confidence interval promise?
5. Why is minimizing cross-entropy the same as maximizing likelihood?

Recommended companions: Blitzstein and Hwang, *Introduction to Probability* (free online), and Wasserman, *All of Statistics*.

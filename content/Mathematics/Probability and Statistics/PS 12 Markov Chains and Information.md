---
type: course-chapter
course: probability-statistics
chapter: 12
tags: [mathematics, probability, information-theory]
---
# PS 12 Markov chains and information

Previous: [[PS 11 Bayesian Inference]] | [[PS 00 Course Map]]

> [!abstract] One sentence
> A Markov chain models a sequence in which the next state depends only on the current one, and entropy, cross-entropy and KL divergence measure uncertainty and the mismatch between distributions.

These two topics finish the course because robot learning leans on both: decision problems are built on Markov chains, and nearly every loss function is an information quantity.

## Part 1: Markov chains

### The Markov property

A sequence of random states $X_0,X_1,X_2,\dots$ is a **Markov chain** when

$$
P(X_{t+1}\mid X_t,X_{t-1},\dots,X_0)=P(X_{t+1}\mid X_t).
$$

Given the present, the future is independent of the past. The current state contains everything relevant for predicting what comes next.

Whether this holds depends on what you put in the state. A ball's position alone is not Markov (you need to know which way it is moving); position and velocity together are. Choosing a state that makes the problem Markov is a central modelling decision.

### Transition matrix

For a finite set of states, collect the transition probabilities in a matrix:

$$
P_{ij}=P(X_{t+1}=j\mid X_t=i).
$$

Each **row** sums to 1 (from state $i$ you must go somewhere).

**Running example.** Weather with two states, sunny (S) and rainy (R):

$$
P=\begin{bmatrix}0.9&0.1\\0.5&0.5\end{bmatrix}.
$$

A sunny day is followed by sun with probability 0.9. A rainy day is followed by rain with probability 0.5.

### Evolving a distribution

Write the distribution over states at time $t$ as a row vector $\pi_t$. One step later:

$$
\pi_{t+1}=\pi_tP,\qquad\text{so}\qquad\pi_t=\pi_0P^t.
$$

Start sunny, $\pi_0=(1,0)$:

- $\pi_1=(0.9,\,0.1)$
- $\pi_2=(0.9\times0.9+0.1\times0.5,\;0.9\times0.1+0.1\times0.5)=(0.86,\,0.14)$
- $\pi_3=(0.844,\,0.156)$

The numbers are settling.

### Stationary distribution

A distribution $\pi$ is **stationary** when one more step leaves it unchanged:

$$
\pi=\pi P.
$$

For the example, $\pi=(s,r)$ with $s+r=1$: the first component gives $s=0.9s+0.5r$, so $0.1s=0.5r$, $s=5r$, and therefore

$$
\pi=\left(\tfrac56,\tfrac16\right)\approx(0.833,\,0.167).
$$

In the long run it is sunny five days in six, whatever the starting weather.

In the language of [[LA 08 Eigenvalues and Eigenvectors]], $\pi$ is a left eigenvector of $P$ with eigenvalue 1. The other eigenvalue here is $0.4$ (trace is $1.4$), and it controls the speed of convergence: the distance to stationarity shrinks by a factor of $0.4$ each step. Check: $0.9-0.833=0.067$, then $0.86-0.833=0.027$, then $0.844-0.833=0.011$.

A chain converges to a unique stationary distribution from any start when it is **irreducible** (every state can reach every other) and **aperiodic** (it does not cycle with a fixed period).

### From chains to decisions

Add actions that influence the transitions, and rewards, and you have a **Markov decision process**: $P(s'\mid s,a)$ and $r(s,a)$. A policy chooses actions; fixing the policy turns the MDP back into a Markov chain. This is the formal setting of [[09 Reinforcement Learning]], and the Bellman equation is the law of total expectation ([[PS 04 Expectation and Variance]]) applied to one step of that chain.

## Part 2: Information

### Surprise

How surprised should you be by an event of probability $p$? Define the **information content** as

$$
-\log p.
$$

Certain events ($p=1$) carry zero surprise; rare events carry a lot. The logarithm makes surprise *add* for independent events, since their probabilities multiply. With $\log_2$ the unit is bits: a fair coin flip is 1 bit.

### Entropy

The **entropy** of a distribution is its average surprise:

$$
H(p)=-\sum_xp(x)\log p(x).
$$

It measures uncertainty, and equals the minimum average number of bits needed to encode outcomes.

| Distribution | Entropy (bits) |
|---|---|
| fair coin | $1$ |
| coin with $p=0.9$ | $\approx0.469$ |
| certain outcome | $0$ |
| fair 8-sided die | $3$ |

**Compute the second.** $-(0.9\log_20.9+0.1\log_20.1)=0.9(0.152)+0.1(3.322)=0.137+0.332=0.469$.

Entropy is largest for the uniform distribution and zero when the outcome is certain. In reinforcement learning, an entropy bonus rewards a policy for staying uncertain, which encourages exploration.

### Cross-entropy

Suppose the truth is $p$ but you use a model $q$. Your average surprise is the **cross-entropy**:

$$
H(p,q)=-\sum_xp(x)\log q(x).
$$

It is always at least $H(p)$: using the wrong model can only increase average surprise.

When $p$ puts all its mass on the true label $c$ (a "one-hot" target), this collapses to $-\log q(c)$: the classification loss from [[PS 09 Estimation and Maximum Likelihood]]. A model that assigns probability 0.9 to the right class pays $-\ln0.9\approx0.105$; one that assigns 0.01 pays $-\ln0.01\approx4.6$. Confident mistakes are punished severely.

### KL divergence

The extra surprise caused by using $q$ in place of $p$:

$$
D_{\mathrm{KL}}(p\,\|\,q)=\sum_xp(x)\log\frac{p(x)}{q(x)}=H(p,q)-H(p).
$$

Properties:

- $D_{\mathrm{KL}}\ge0$, with equality only when $p=q$.
- It is **not symmetric**: $D_{\mathrm{KL}}(p\,\|\,q)\neq D_{\mathrm{KL}}(q\,\|\,p)$. So it is not a true distance.

Since $H(p)$ does not depend on the model, **minimizing cross-entropy, minimizing KL to the data distribution, and maximizing likelihood are the same thing.** Three names, one objective.

**The asymmetry matters.** $D_{\mathrm{KL}}(p\,\|\,q)$ is huge wherever $p$ has mass and $q$ has almost none, so minimizing it forces $q$ to *cover* everything the data does. If the data has two modes and $q$ is a single Gaussian, the best cover is a wide blob over both, with its peak in the empty middle. The reverse direction, $D_{\mathrm{KL}}(q\,\|\,p)$, instead makes $q$ lock onto one mode. This is the mathematics behind the mode-averaging problem of [[PS 07 The Multivariate Gaussian]].

**Worked example.** $p=(0.5,0.5)$, $q=(0.9,0.1)$, in bits:

$$
D_{\mathrm{KL}}(p\,\|\,q)=0.5\log_2\frac{0.5}{0.9}+0.5\log_2\frac{0.5}{0.1}=0.5(-0.848)+0.5(2.322)=0.737.
$$

Reverse: $0.9\log_2\tfrac{0.9}{0.5}+0.1\log_2\tfrac{0.1}{0.5}=0.763-0.232=0.531$. Different, as promised.

### Mutual information

How much does knowing $Y$ reduce uncertainty about $X$?

$$
I(X;Y)=H(X)-H(X\mid Y)=D_{\mathrm{KL}}\big(p(x,y)\,\|\,p(x)p(y)\big).
$$

It is zero exactly when $X$ and $Y$ are independent, and unlike correlation it detects *any* kind of dependence, not just linear ([[PS 06 Joint Distributions and Covariance]]). Contrastive representation learning maximizes a bound on it.

## Learn by doing

1. For $P=\begin{bmatrix}0.7&0.3\\0.2&0.8\end{bmatrix}$, find the stationary distribution.
2. Starting from state 1 in that chain, find the distribution after two steps.
3. Compute the entropy in bits of the distribution $(0.5,0.25,0.25)$.
4. A classifier gives the correct class probability 0.5. What is the cross-entropy loss in nats? What if it gives 0.99?

> [!success]- Check your answers
> 1. $0.3s=0.2r$ and $s+r=1$ give $\pi=(0.4,\,0.6)$.
> 2. $\pi_1=(0.7,0.3)$. $\pi_2=(0.49+0.06,\;0.21+0.24)=(0.55,\,0.45)$.
> 3. $0.5(1)+0.25(2)+0.25(2)=1.5$ bits.
> 4. $-\ln0.5\approx0.693$ and $-\ln0.99\approx0.010$.

## Where this shows up

Markov decision processes ([[09 Reinforcement Learning]]), KL-constrained policy updates and entropy bonuses ([[Appendix - PPO SAC and Offline Learning]]), the diffusion training bound ([[08 Diffusion and Flow Matching]]) and distribution shift measured as divergence between training and deployment state distributions ([[06 Imitation and Distribution Shift]]).

You have finished the course. Return to the checkpoint questions in [[PS 00 Course Map]].

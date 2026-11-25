---
type: course-chapter
course: probability-statistics
chapter: 6
tags: [mathematics, probability]
---

# Chapter 6: Joint distributions and covariance

Previous: [[PS 05 Continuous Random Variables]] | [[PS 00 Course Map]] | Next: [[PS 07 The Multivariate Gaussian]]

> [!abstract] The big idea
> Real problems involve several random quantities at once: position and velocity, temperature and success rate, every pixel of an image. A **joint distribution** describes them together. From it you can recover each one alone (**marginals**), one given another (**conditionals**), and a single number measuring how they move together (**covariance** and **correlation**). Covariance matrices then let you track uncertainty through any linear calculation.

> [!info] In this chapter you will learn to
> 1. Read joint, marginal and conditional distributions from a table.
> 2. Test independence of random variables.
> 3. Compute covariance and correlation, and interpret them correctly.
> 4. Recognize what correlation cannot tell you.
> 5. Compute the variance of sums of dependent variables.
> 6. Build covariance matrices and propagate them through linear maps with $A\Sigma A^\top$.

> [!tip] Before you start
> You need conditional probability ([[PS 02 Conditional Probability and Bayes Rule]]) and expectation and variance ([[PS 04 Expectation and Variance]]). Section 6.7 uses matrix multiplication ([[LA 03 Matrices as Linear Maps]]).

---

## 6.1 Joint distributions

### Discrete case: a table

> [!note] Definition: joint PMF
> For discrete random variables $X$ and $Y$,
> $$
> p(x,y)=P(X=x\text{ and }Y=y).
> $$
> All entries are non-negative and sum to 1.

**Running example.** Outdoor robot tests. $X$ is the weather, $Y$ is whether the test succeeds.

| | $Y=$ fail | $Y=$ success |
|---|---|---|
| $X=$ dry | 0.10 | 0.50 |
| $X=$ rain | 0.25 | 0.15 |

Each cell is the probability of that combination. Check: $0.10+0.50+0.25+0.15=1$ ✓.

### Continuous case: a surface

For continuous $X,Y$, the **joint density** $p(x,y)$ is a surface over the plane. Probabilities are **volumes** under it:

$$
P\big((X,Y)\in R\big)=\iint_Rp(x,y)\,dx\,dy.
$$

Everything below works the same way, with sums replaced by integrals.

---

## 6.2 Marginals: forget one variable

> [!note] Definition: marginal distribution
> $$
> p(x)=\sum_yp(x,y),\qquad p(y)=\sum_xp(x,y).
> $$
> (For densities: integrate out the other variable.)

Add across a row to get the row total; add down a column to get the column total. These totals are written in the **margins** of the table, hence the name.

| | fail | success | **$p(x)$** |
|---|---|---|---|
| dry | 0.10 | 0.50 | **0.60** |
| rain | 0.25 | 0.15 | **0.40** |
| **$p(y)$** | **0.35** | **0.65** | 1 |

So $P(\text{dry})=0.60$ and $P(\text{success})=0.65$.

**Why it works:** "dry" is the union of the disjoint events "dry and fail" and "dry and success", so their probabilities add (axiom 3).

> [!warning] Marginals do not determine the joint
> Knowing $P(\text{dry})=0.6$ and $P(\text{success})=0.65$ does **not** tell you $P(\text{dry and success})$. Many different tables have the same margins. The relationship between variables lives only in the joint.

---

## 6.3 Conditionals: fix one variable

> [!note] Definition: conditional distribution
> $$
> p(y\mid x)=\frac{p(x,y)}{p(x)}.
> $$

Take one row of the table and divide by its total, so it sums to 1.

| | fail | success |
|---|---|---|
| given dry | $0.10/0.60\approx0.167$ | $0.50/0.60\approx0.833$ |
| given rain | $0.25/0.40=0.625$ | $0.15/0.40=0.375$ |

Rain more than halves the success rate.

### How the three fit together

$$
\underbrace{p(x,y)}_{\text{joint}}=\underbrace{p(y\mid x)}_{\text{conditional}}\;\underbrace{p(x)}_{\text{marginal}}.
$$

This is the multiplication rule from chapter 2 for random variables. Bayes' rule follows immediately:

$$
p(x\mid y)=\frac{p(y\mid x)\,p(x)}{p(y)}.
$$

**Example.** $P(\text{rain}\mid\text{fail})=\dfrac{0.25}{0.35}\approx0.714$. Most failures happen in rain.

---

## 6.4 Independence of random variables

> [!note] Definition: independent random variables
> $X$ and $Y$ are **independent** if the joint factorizes for **every** pair of values:
> $$
> p(x,y)=p(x)\,p(y)\quad\text{for all }x,y.
> $$
> Equivalently, $p(y\mid x)=p(y)$: knowing $X$ never changes the distribution of $Y$.

**Check the example.** $p(\text{dry})\,p(\text{success})=0.6\times0.65=0.39$, but $p(\text{dry, success})=0.50$. **Dependent.**

One mismatched cell is enough to show dependence. To show independence you must check **every** cell.

**An independent table**, for contrast: if the margins were the same but every cell were the product of its margins:

| | fail | success |
|---|---|---|
| dry | $0.6\times0.35=0.21$ | $0.6\times0.65=0.39$ |
| rain | $0.4\times0.35=0.14$ | $0.4\times0.65=0.26$ |

Here success is 65% in both weathers.

---

## 6.5 Covariance

### The definition

We want **one number** saying whether two variables tend to be high together, or one high when the other is low.

> [!note] Definition: covariance
> $$
> \operatorname{Cov}(X,Y)=\mathbb E\big[(X-\mu_X)(Y-\mu_Y)\big]=\mathbb E[XY]-\mathbb E[X]\,\mathbb E[Y].
> $$

### Why this formula measures "moving together"

Look at the product $(X-\mu_X)(Y-\mu_Y)$:

| $X$ vs its mean | $Y$ vs its mean | product |
|---|---|---|
| above | above | positive |
| below | below | positive |
| above | below | negative |
| below | above | negative |

If high-high and low-low pairs dominate, the average product is positive. If high-low pairs dominate, it is negative. If there is no tendency either way, they cancel to about zero.

| Covariance | Meaning |
|---|---|
| positive | tend to move in the same direction |
| negative | tend to move in opposite directions |
| zero | no **linear** tendency |

Note that $\operatorname{Cov}(X,X)=\operatorname{Var}(X)$.

### Worked example 6.1

Code dry $=0$, rain $=1$, fail $=0$, success $=1$.

- $\mathbb E[X]=P(\text{rain})=0.40$.
- $\mathbb E[Y]=P(\text{success})=0.65$.
- $XY=1$ only for (rain, success), so $\mathbb E[XY]=0.15$.

$$
\operatorname{Cov}(X,Y)=0.15-0.40\times0.65=0.15-0.26=-0.11.
$$

Negative: rain goes with failure. (For the independent table it would be $0.26-0.26=0$.)

### Properties

| Property | Formula |
|---|---|
| symmetric | $\operatorname{Cov}(X,Y)=\operatorname{Cov}(Y,X)$ |
| constants vanish | $\operatorname{Cov}(X,c)=0$ |
| scaling | $\operatorname{Cov}(aX,bY)=ab\,\operatorname{Cov}(X,Y)$ |
| shifting does nothing | $\operatorname{Cov}(X+a,Y+b)=\operatorname{Cov}(X,Y)$ |
| bilinear | $\operatorname{Cov}(X+Z,Y)=\operatorname{Cov}(X,Y)+\operatorname{Cov}(Z,Y)$ |
| independence | independent $\Rightarrow\operatorname{Cov}=0$ |

---

## 6.6 Correlation

### Removing the units

Covariance depends on units: measure $X$ in centimetres instead of metres and the covariance grows 100 times, though the relationship is unchanged. Divide out the standard deviations to get a pure number:

> [!note] Definition: correlation
> $$
> \rho(X,Y)=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\,\sigma_Y},\qquad-1\le\rho\le1.
> $$

| $\rho$ | Picture of the scatter plot |
|---|---|
| $+1$ | points exactly on an upward line |
| around $+0.7$ | a clear upward cloud |
| $0$ | no linear trend |
| around $-0.7$ | a clear downward cloud |
| $-1$ | points exactly on a downward line |

**Why bounded by 1?** After subtracting the means, correlation is exactly the **cosine of the angle** between the two variables viewed as vectors ([[LA 02 Dot Product Length and Angle]]), and Cauchy-Schwarz bounds any cosine by 1.

**Worked example 6.2.** For the weather table: $\sigma_X=\sqrt{0.4\times0.6}\approx0.490$ and $\sigma_Y=\sqrt{0.65\times0.35}\approx0.477$. So

$$
\rho\approx\frac{-0.11}{0.490\times0.477}\approx\frac{-0.11}{0.234}\approx-0.47.
$$

A moderate negative relationship.

---

## 6.7 Three warnings about correlation

> [!warning] 1. Uncorrelated does not mean independent
> Let $X$ be equally likely to be $-1,0,1$, and $Y=X^2$. Then $Y$ is completely determined by $X$. But
> $$
> \operatorname{Cov}(X,Y)=\mathbb E[X^3]-\mathbb E[X]\,\mathbb E[X^2]=0-0\cdot\tfrac23=0.
> $$
> Correlation only detects **straight-line** relationships. A U-shaped relationship can have zero correlation.
>
> **Independent ⇒ uncorrelated. Uncorrelated ⇏ independent.**

> [!warning] 2. Correlation does not imply causation
> Ice cream sales and drownings are positively correlated. Ice cream does not cause drowning: hot weather drives both. A **confounder** (a common cause), **reverse causation**, or **selection effects** can all create correlation without the causal link you might assume.
>
> In robot learning: if successful demonstrations all happened to be recorded in the morning, a policy may learn that morning light "causes" success.

> [!warning] 3. One number hides the shape
> Datasets with completely different shapes (a line, a curve, a cloud with one outlier) can share the same correlation. **Always plot the data.**

---

## 6.8 Variance of a sum, in general

> [!important] Variance of a sum
> $$
> \operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y).
> $$
> More generally,
> $$
> \operatorname{Var}(aX+bY)=a^2\operatorname{Var}(X)+b^2\operatorname{Var}(Y)+2ab\operatorname{Cov}(X,Y).
> $$

*Proof:* expand $\mathbb E[(X-\mu_X+Y-\mu_Y)^2]$; the cross term is $2\,\mathbb E[(X-\mu_X)(Y-\mu_Y)]$.

**Meaning:**

- **Positive** covariance: fluctuations reinforce each other; the sum is more variable. Correlated risks add up badly.
- **Negative** covariance: fluctuations partly cancel; the sum is steadier. This is the principle behind **diversification** and **hedging**.
- **Zero** covariance: back to the simple rule of chapter 4.

**Worked example 6.3.** $\operatorname{Var}(X)=4$, $\operatorname{Var}(Y)=9$, $\operatorname{Cov}(X,Y)=3$.

- $\operatorname{Var}(X+Y)=4+9+6=19$.
- $\operatorname{Var}(X-Y)=4+9-6=7$.
- $\rho=3/(2\times3)=0.5$.

---

## 6.9 Random vectors and covariance matrices

### Stacking variables into a vector

Collect $n$ random variables into a random vector $x=(X_1,\dots,X_n)^\top$. Its **mean vector** is $\mu=\mathbb E[x]$, and its spread is described by the **covariance matrix**:

> [!note] Definition: covariance matrix
> $$
> \Sigma=\mathbb E\big[(x-\mu)(x-\mu)^\top\big],\qquad\Sigma_{ij}=\operatorname{Cov}(X_i,X_j).
> $$

- **Diagonal** entries are the variances.
- **Off-diagonal** entries are the covariances.
- $\Sigma$ is **symmetric** ($\operatorname{Cov}(X_i,X_j)=\operatorname{Cov}(X_j,X_i)$) and **positive semidefinite** ([[LA 09 Symmetric and Positive Definite Matrices]]).

**Example.** For worked example 6.3:

$$
\Sigma=\begin{bmatrix}4&3\\3&9\end{bmatrix}.
$$

### Propagating uncertainty through a linear map

> [!important] Linear transformation of a random vector
> If $y=Ax+b$, then
> $$
> \mathbb E[y]=A\mu+b,\qquad\operatorname{Cov}(y)=A\,\Sigma\,A^\top.
> $$

*Why:* $y-\mathbb E[y]=A(x-\mu)$, so $(y-\mathbb E y)(y-\mathbb E y)^\top=A(x-\mu)(x-\mu)^\top A^\top$; take expectations.

This one formula handles **all** linear error propagation. Check it on the sum: $X+Y=\begin{bmatrix}1&1\end{bmatrix}x$, so

$$
\operatorname{Var}(X+Y)=\begin{bmatrix}1&1\end{bmatrix}\begin{bmatrix}4&3\\3&9\end{bmatrix}\begin{bmatrix}1\\1\end{bmatrix}=4+3+3+9=19\;✓.
$$

**Worked example 6.4: sum and difference.** $X,Y$ independent with variances 1 and 4. Let $u=X+Y$, $v=X-Y$:

$$
A=\begin{bmatrix}1&1\\1&-1\end{bmatrix},\quad\Sigma=\begin{bmatrix}1&0\\0&4\end{bmatrix},\quad A\Sigma A^\top=\begin{bmatrix}5&-3\\-3&5\end{bmatrix}.
$$

Even though $X$ and $Y$ are independent, the sum and difference are **negatively correlated**. Transformations create correlations.

**Worked example 6.5: robot position.** A planar robot's estimated position $(x,y)$ has covariance $\Sigma=\begin{bmatrix}0.04&0\\0&0.01\end{bmatrix}$ m². What is the uncertainty in the distance travelled along the direction $d=(0.6,0.8)$? That distance is $d^\top p$, so its variance is

$$
d^\top\Sigma d=0.36(0.04)+0.64(0.01)=0.0144+0.0064=0.0208,
$$

a standard deviation of about 0.144 m.

---

## 6.10 The law of total variance

$$
\operatorname{Var}(Y)=\underbrace{\mathbb E\big[\operatorname{Var}(Y\mid X)\big]}_{\text{average spread within groups}}+\underbrace{\operatorname{Var}\big(\mathbb E[Y\mid X]\big)}_{\text{spread between group means}}.
$$

Total variation splits into variation **within** each group and variation **between** the groups' averages. The second term is the part "explained by" $X$.

**Worked example 6.6.** Task times: light boxes (60%) have mean 20 s and variance 4; heavy boxes (40%) have mean 45 s and variance 25.

- Within: $0.6(4)+0.4(25)=12.4$.
- Between: the group means 20 and 45 with weights 0.6, 0.4 have mean 30 and variance $0.6(10^2)+0.4(15^2)=60+90=150$.
- Total: $162.4$. Most of the spread comes from **which kind** of box it is, not from variation within a kind.

This decomposition is the basis of $R^2$ in regression and of the analysis of variance (ANOVA).

---

## Summary

| Idea | Formula |
|---|---|
| marginal | $p(x)=\sum_yp(x,y)$ |
| conditional | $p(y\mid x)=p(x,y)/p(x)$ |
| independence | $p(x,y)=p(x)p(y)$ for all $x,y$ |
| covariance | $\mathbb E[XY]-\mathbb E[X]\mathbb E[Y]$ |
| correlation | $\operatorname{Cov}/(\sigma_X\sigma_Y)\in[-1,1]$ |
| sum | $\operatorname{Var}(X+Y)=\operatorname{Var}X+\operatorname{Var}Y+2\operatorname{Cov}$ |
| covariance matrix | $\Sigma_{ij}=\operatorname{Cov}(X_i,X_j)$ |
| linear map | $\operatorname{Cov}(Ax+b)=A\Sigma A^\top$ |

**Three facts to remember:**

1. The relationship between variables lives in the joint, not in the marginals.
2. Correlation measures straight-line association only, and says nothing about causation.
3. $A\Sigma A^\top$ propagates uncertainty through any linear calculation.

---

## Exercises

### Part A: warm-up

**A1.** From the weather table, find $P(\text{rain}\mid\text{success})$ and $P(\text{success}\mid\text{rain})$.

**A2.** $\operatorname{Var}(X)=1$, $\operatorname{Var}(Y)=4$, $\rho=-0.5$. Find $\operatorname{Cov}(X,Y)$ and $\operatorname{Var}(X+Y)$.

**A3.** Is this table independent? $p(0,0)=0.12$, $p(0,1)=0.28$, $p(1,0)=0.18$, $p(1,1)=0.42$.

**A4.** Write the covariance matrix of $(X,Y)$ if $\operatorname{Var}X=2$, $\operatorname{Var}Y=5$, $\operatorname{Cov}=-1$.

> [!success]- Solutions to Part A
> **A1.** $0.15/0.65\approx0.231$ and $0.15/0.40=0.375$.
>
> **A2.** $\operatorname{Cov}=-0.5\times1\times2=-1$. $\operatorname{Var}(X+Y)=1+4-2=3$.
>
> **A3.** Margins: $p_X(0)=0.4$, $p_X(1)=0.6$, $p_Y(0)=0.3$, $p_Y(1)=0.7$. Products: $0.12,0.28,0.18,0.42$. All match: independent.
>
> **A4.** $\begin{bmatrix}2&-1\\-1&5\end{bmatrix}$.

### Part B: core

**B1.** Two dice. Let $X$ be the first die and $S$ the sum. Find $\operatorname{Cov}(X,S)$ and $\rho(X,S)$. (Hint: $S=X+Y$ with $Y$ independent of $X$.)

**B2.** A portfolio puts weight $w$ in asset A (variance 0.04) and $1-w$ in asset B (variance 0.09), with correlation $-0.3$. Write the variance as a function of $w$ and find the $w$ that minimizes it.

**B3.** A camera estimates an object's position with covariance $\Sigma=\begin{bmatrix}4&0\\0&1\end{bmatrix}$ mm² in the camera frame. The camera frame is rotated $90^\circ$ relative to the robot frame, $R=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$. Find the covariance in the robot frame. Interpret.

**B4.** Give a small joint table where $X$ and $Y$ are uncorrelated but not independent.

**B5.** Data shows that students who take more practice tests score higher. Give two explanations other than "practice tests cause higher scores".

> [!success]- Solutions to Part B
> **B1.** $\operatorname{Cov}(X,X+Y)=\operatorname{Var}X+\operatorname{Cov}(X,Y)=2.917+0$. $\operatorname{Var}S=5.833$. $\rho=\dfrac{2.917}{\sqrt{2.917}\sqrt{5.833}}=\sqrt{0.5}\approx0.707$.
>
> **B2.** $\operatorname{Cov}=-0.3\times0.2\times0.3=-0.018$. $V(w)=0.04w^2+0.09(1-w)^2-0.036w(1-w)$. Derivative: $0.08w-0.18(1-w)-0.036(1-2w)=0$, so $0.332w=0.216$ and $w\approx0.651$. Variance about $0.0197$: lower than either asset alone (0.04 and 0.09), because the negative correlation lets their fluctuations partly cancel.
>
> **B3.** $R\Sigma R^\top=\begin{bmatrix}1&0\\0&4\end{bmatrix}$. The large uncertainty that was along the camera's $x$-axis is now along the robot's $y$-axis: the uncertainty ellipse rotates with the frame.
>
> **B4.** The $Y=X^2$ example: $X\in\{-1,0,1\}$ each with probability $\tfrac13$; $p(-1,1)=p(1,1)=p(0,0)=\tfrac13$.
>
> **B5.** Motivated students both take more practice tests and study more in other ways (confounder). Or students who already score well enjoy taking tests (reverse causation).

### Part C: explain and prove

**C1.** Prove $\operatorname{Cov}(X,Y)=\mathbb E[XY]-\mathbb E[X]\mathbb E[Y]$ from the definition.

**C2.** Prove that if $X$ and $Y$ are independent then $\operatorname{Cov}(X,Y)=0$. (Use $\mathbb E[XY]=\mathbb E[X]\mathbb E[Y]$ for independent variables.)

**C3.** Prove that a covariance matrix is positive semidefinite. (Hint: for any fixed vector $a$, $a^\top\Sigma a$ is the variance of something.)

**C4.** Explain why averaging two **positively correlated** measurements reduces noise less than averaging two independent ones.

> [!success]- Solutions to Part C
> **C1.** Expand $(X-\mu_X)(Y-\mu_Y)=XY-\mu_XY-\mu_YX+\mu_X\mu_Y$ and take expectations: $\mathbb E[XY]-\mu_X\mu_Y-\mu_Y\mu_X+\mu_X\mu_Y$.
>
> **C2.** $\operatorname{Cov}=\mathbb E[XY]-\mathbb E[X]\mathbb E[Y]=0$.
>
> **C3.** $a^\top\Sigma a=\operatorname{Var}(a^\top x)\ge0$.
>
> **C4.** $\operatorname{Var}(\tfrac12(X+Y))=\tfrac14(\sigma^2+\sigma^2+2\rho\sigma^2)=\tfrac{\sigma^2}2(1+\rho)$. With $\rho>0$ this exceeds $\sigma^2/2$. Correlated errors do not cancel, because they tend to point the same way.

### Part D: practise with code

**D1.** Generate 10,000 pairs from the weather table (sample a cell index with `rng.choice(4, p=[...])`) and estimate the covariance and correlation. Compare with $-0.11$ and $-0.47$.

**D2.** Generate $X\sim\mathcal N(0,1)$ and $Y=X^2$. Compute `np.corrcoef(X, Y)` and make a scatter plot. What do you see?

**D3.** Draw 10,000 vectors with covariance $\begin{bmatrix}4&3\\3&9\end{bmatrix}$ (`rng.multivariate_normal`), apply $A=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$, and compare `np.cov` of the result with $A\Sigma A^\top$.

---

## Where this is used

- The **Kalman filter** propagates a covariance with $A\Sigma A^\top$ at every prediction step ([[04 Perception and State]]).
- **Correlated samples** (consecutive frames of a video, repeated trials on one object) carry less information than their count suggests ([[16 Evaluation and Uncertainty]]).
- **Spurious correlations** in demonstration data are one source of policies that fail when conditions change ([[06 Imitation and Distribution Shift]]).

Next: [[PS 07 The Multivariate Gaussian]]: the most important joint distribution.

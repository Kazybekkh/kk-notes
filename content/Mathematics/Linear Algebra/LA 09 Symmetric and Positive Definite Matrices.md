---
type: course-chapter
course: linear-algebra
chapter: 9
tags: [mathematics, linear-algebra]
---

# Chapter 9: Symmetric and positive definite matrices

Previous: [[LA 08 Eigenvalues and Eigenvectors]] | [[LA 00 Course Map]] | Next: [[LA 10 Singular Value Decomposition]]

> [!abstract] The big idea
> A **symmetric** matrix is the best-behaved kind of matrix: it is a pure stretch along **perpendicular** axes, with real stretch factors. When all those stretch factors are **positive**, the matrix is **positive definite**, and it describes a bowl-shaped function with exactly one lowest point. That is why these matrices run through optimization, statistics and control.

> [!info] In this chapter you will learn to
> 1. State the spectral theorem and explain it with a picture.
> 2. Diagonalize a symmetric matrix with an orthogonal matrix, $S=Q\Lambda Q^\top$.
> 3. Write and read a quadratic form $x^\top Sx$.
> 4. Test whether a matrix is positive definite in four different ways.
> 5. Use the Hessian to classify minima, maxima and saddle points.

> [!tip] Before you start
> You need eigenvalues and diagonalization ([[LA 08 Eigenvalues and Eigenvectors]]) and orthogonal matrices ([[LA 06 Orthogonality and Least Squares]]). One calculus idea is used in section 9.6: a minimum of $f(x)$ has $f'(x)=0$ and $f''(x)>0$.

---

## 9.1 Symmetric matrices

> [!note] Definition: symmetric
> A square matrix $S$ is **symmetric** if $S^\top=S$, meaning $s_{ij}=s_{ji}$ for all $i,j$. The matrix is a mirror image of itself across its main diagonal.

$$
\begin{bmatrix}2&1\\1&2\end{bmatrix},\qquad\begin{bmatrix}4&-1&0\\-1&3&2\\0&2&5\end{bmatrix}\quad\text{(symmetric)};\qquad\begin{bmatrix}1&2\\3&4\end{bmatrix}\quad\text{(not)}.
$$

### Where they come from

Symmetric matrices are not rare special cases. They appear whenever a matrix describes a **relationship between pairs** that does not depend on order:

| Source | Why symmetric |
|---|---|
| $A^\top A$ for any $A$ | $(A^\top A)^\top=A^\top A$ |
| covariance matrix | $\operatorname{Cov}(X_i,X_j)=\operatorname{Cov}(X_j,X_i)$ |
| Hessian (second derivatives) | $\dfrac{\partial^2f}{\partial x_i\partial x_j}=\dfrac{\partial^2f}{\partial x_j\partial x_i}$ |
| distance or similarity matrix | $d(i,j)=d(j,i)$ |
| undirected graph's adjacency matrix | edges have no direction |
| robot mass (inertia) matrix | from kinetic energy $\tfrac12\dot q^\top M\dot q$ |

---

## 9.2 The spectral theorem

> [!important] Spectral theorem
> Every real symmetric matrix $S$
> 1. has **only real eigenvalues**, and
> 2. has a full set of **orthonormal** eigenvectors (perpendicular, unit length).
>
> Therefore
> $$
> S=Q\Lambda Q^\top,
> $$
> where $Q$ is an orthogonal matrix whose columns are the eigenvectors, and $\Lambda$ is diagonal with the eigenvalues.

Compare with general diagonalization, $A=V\Lambda V^{-1}$:

| General matrix | Symmetric matrix |
|---|---|
| eigenvalues may be complex | always real |
| eigenvectors may be skewed | always perpendicular |
| may not be diagonalizable | always diagonalizable |
| need to compute $V^{-1}$ | $V^{-1}=Q^\top$, free |

"Spectral" refers to the **spectrum**, the set of eigenvalues.

### The picture

$S=Q\Lambda Q^\top$ says $S$ acts in three steps:

1. $Q^\top$ **rotates** space so the eigenvector directions line up with the coordinate axes.
2. $\Lambda$ **stretches** along each axis by its eigenvalue.
3. $Q$ **rotates back**.

So a symmetric matrix is a **pure stretch along perpendicular axes**. It never shears or twists. A unit circle becomes an ellipse whose axes are the eigenvectors.

### Why eigenvectors of different eigenvalues are perpendicular

Let $Sv=\lambda v$ and $Sw=\mu w$ with $\lambda\neq\mu$. Compute the number $w^\top Sv$ in two ways.

- Directly: $w^\top Sv=w^\top(\lambda v)=\lambda\,(w^\top v)$.
- Using symmetry, $w^\top S=(S^\top w)^\top=(Sw)^\top=\mu w^\top$, so $w^\top Sv=\mu\,(w^\top v)$.

Both are the same number, so $(\lambda-\mu)\,(w^\top v)=0$. Since $\lambda\neq\mu$, we must have $w^\top v=0$: perpendicular. $\blacksquare$

The proof used symmetry in exactly one place. For non-symmetric matrices the step fails, and so does perpendicularity (in chapter 8's example 8.1, the eigenvectors $(1,1)$ and $(1,-2)$ were not perpendicular).

### Worked example 9.1

$$
S=\begin{bmatrix}2&1\\1&2\end{bmatrix}.
$$

Trace 4, determinant 3, so $\lambda^2-4\lambda+3=0$: $\lambda=3$ and $\lambda=1$.

- $\lambda=3$: $S-3I=\begin{bmatrix}-1&1\\1&-1\end{bmatrix}$, eigenvector $(1,1)$.
- $\lambda=1$: $S-I=\begin{bmatrix}1&1\\1&1\end{bmatrix}$, eigenvector $(1,-1)$.

Perpendicular: $(1,1)\cdot(1,-1)=0$ ✓. Normalize to unit length:

$$
Q=\frac1{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix},\qquad\Lambda=\begin{bmatrix}3&0\\0&1\end{bmatrix}.
$$

**Interpretation.** $S$ stretches by 3 along the diagonal direction $(1,1)$ and leaves the anti-diagonal direction $(1,-1)$ unchanged.

### Sum of rank-one pieces

Multiplying out $Q\Lambda Q^\top$ column by column gives

$$
S=\lambda_1q_1q_1^\top+\lambda_2q_2q_2^\top+\cdots+\lambda_nq_nq_n^\top.
$$

Each $q_iq_i^\top$ is the projection onto the line through $q_i$ (chapter 6). So $S$ is "project onto each eigen-direction, scale by its eigenvalue, add up". For example 9.1:

$$
3\cdot\frac12\begin{bmatrix}1&1\\1&1\end{bmatrix}+1\cdot\frac12\begin{bmatrix}1&-1\\-1&1\end{bmatrix}=\begin{bmatrix}2&1\\1&2\end{bmatrix}\;✓
$$

> [!question]- Check yourself
> 1. Find the eigenvalues and orthonormal eigenvectors of $\begin{bmatrix}3&0\\0&5\end{bmatrix}$.
> 2. Find the eigenvalues of $\begin{bmatrix}1&2\\2&1\end{bmatrix}$. Are the eigenvectors perpendicular?
>
> **Answers.** 1. $3$ with $e_1$, $5$ with $e_2$. 2. $3$ and $-1$, with $(1,1)$ and $(1,-1)$: perpendicular, as the theorem promises.

---

## 9.3 Quadratic forms

### Definition

A symmetric matrix defines a **scalar function** of a vector:

$$
f(x)=x^\top Sx=\sum_i\sum_js_{ij}x_ix_j.
$$

This is called a **quadratic form**: every term has degree two.

**Worked example 9.2.** For $S=\begin{bmatrix}2&1\\1&2\end{bmatrix}$:

$$
x^\top Sx=\begin{bmatrix}x_1&x_2\end{bmatrix}\begin{bmatrix}2x_1+x_2\\x_1+2x_2\end{bmatrix}=2x_1^2+2x_1x_2+2x_2^2.
$$

### Reading a quadratic form off a matrix (and back)

- Each **diagonal** entry $s_{ii}$ gives the term $s_{ii}x_i^2$.
- Each **off-diagonal pair** $s_{ij}=s_{ji}$ gives the cross term $2s_{ij}x_ix_j$ (it appears twice).

**Going backwards.** $f=3x_1^2-4x_1x_2+5x_2^2$: put $3$ and $5$ on the diagonal, and **half** the cross coefficient, $-2$, in both off-diagonal spots:

$$
S=\begin{bmatrix}3&-2\\-2&5\end{bmatrix}.
$$

### Eigenvector coordinates remove the cross terms

Substitute $x=Qy$ (so $y=Q^\top x$ are the eigenvector coordinates):

$$
x^\top Sx=y^\top Q^\top(Q\Lambda Q^\top)Qy=y^\top\Lambda y=\lambda_1y_1^2+\lambda_2y_2^2+\cdots+\lambda_ny_n^2.
$$

**No cross terms.** In the right coordinates, a quadratic form is just a weighted sum of squares, and its shape is decided entirely by the **signs** of the eigenvalues.

For example 9.2: $2x_1^2+2x_1x_2+2x_2^2=3y_1^2+y_2^2$, where $y_1=\tfrac{x_1+x_2}{\sqrt2}$ and $y_2=\tfrac{x_1-x_2}{\sqrt2}$.

---

## 9.4 Positive definite matrices

### Definition

> [!note] Definition: positive definite
> A symmetric matrix $S$ is **positive definite** if
> $$
> x^\top Sx>0\quad\text{for every }x\neq0.
> $$
> It is **positive semidefinite** if $x^\top Sx\ge0$ for every $x$.

Think of $x^\top Sx$ as an "energy" or "cost". Positive definite means **every** nonzero $x$ has positive energy.

### Four equivalent tests

For a symmetric matrix, these are all equivalent. Any one of them proves positive definiteness:

| Test | Positive definite when |
|---|---|
| 1. eigenvalues | all $\lambda_i>0$ |
| 2. pivots | all pivots in elimination $>0$ (no row swaps) |
| 3. leading minors | determinants of the top-left $1\times1$, $2\times2$, ..., $n\times n$ blocks are all $>0$ |
| 4. factorization | $S=A^\top A$ for some $A$ with independent columns |

*Why test 1 works:* from section 9.3, $x^\top Sx=\sum\lambda_iy_i^2$. If all $\lambda_i>0$, this is positive unless every $y_i=0$, i.e. unless $x=0$.

*Why test 4 works:* $x^\top A^\top Ax=(Ax)^\top(Ax)=\|Ax\|^2\ge0$, and it is zero only if $Ax=0$, which (for independent columns) means $x=0$.

> [!tip] Which test to use by hand
> For $2\times2$: the minor test. $S=\begin{bmatrix}a&b\\b&c\end{bmatrix}$ is positive definite exactly when $a>0$ **and** $ac-b^2>0$.
> For bigger matrices: the pivot test (run elimination, check every pivot is positive).

### Worked examples

**Worked example 9.3.** $S=\begin{bmatrix}2&1\\1&2\end{bmatrix}$. Minors: $2>0$ and $4-1=3>0$. Positive definite. (Eigenvalues $3,1$ agree.)

**Worked example 9.4.** $S=\begin{bmatrix}1&2\\2&1\end{bmatrix}$. Minors: $1>0$ but $1-4=-3<0$. **Not** positive definite. Find a witness: $x=(1,-1)$ gives $x^\top Sx=1-4+1=-2<0$.

> [!warning] Positive entries are not enough
> Example 9.4 has all positive entries yet is not positive definite. What matters is that the diagonal "outweighs" the off-diagonal coupling.

**Worked example 9.5 (3×3, pivot test).**

$$
S=\begin{bmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{bmatrix}.
$$

Elimination: $R_2+\tfrac12R_1$ gives second pivot $2-\tfrac12=\tfrac32$. Then $R_3+\tfrac23R_2$ gives third pivot $2-\tfrac23=\tfrac43$. Pivots $2,\tfrac32,\tfrac43$, all positive: positive definite. (This matrix appears whenever you discretize a second derivative, for example in physics simulations and smoothing.)

> [!question]- Check yourself
> 1. Is $\begin{bmatrix}4&2\\2&3\end{bmatrix}$ positive definite?
> 2. For which $b$ is $\begin{bmatrix}1&b\\b&4\end{bmatrix}$ positive definite?
> 3. Is $\begin{bmatrix}1&1\\1&1\end{bmatrix}$ positive definite? Semidefinite?
>
> **Answers.** 1. $4>0$, $12-4=8>0$: yes. 2. $4-b^2>0$, so $-2<b<2$. 3. Minor $1-1=0$, not definite. Eigenvalues $2$ and $0$: semidefinite. $x=(1,-1)$ gives $0$.

---

## 9.5 The picture: bowls, troughs and saddles

Plot $z=x^\top Sx$ over the plane. The signs of the eigenvalues decide the shape:

| Eigenvalues | Name | Surface |
|---|---|---|
| all $>0$ | positive definite | **bowl**: unique lowest point at the origin |
| all $\ge0$, some $=0$ | positive semidefinite | **trough**: flat along some direction |
| some $>0$, some $<0$ | indefinite | **saddle**: up one way, down another |
| all $<0$ | negative definite | **dome**: unique highest point |

### Level sets are ellipses

For positive definite $S$, the curves $x^\top Sx=1$ are **ellipses** (ellipsoids in 3-D and beyond):

- The **axes** point along the eigenvectors.
- The **half-length** along eigenvector $q_i$ is $1/\sqrt{\lambda_i}$.

*Why:* in eigen-coordinates the curve is $\lambda_1y_1^2+\lambda_2y_2^2=1$. Setting $y_2=0$ gives $y_1=\pm1/\sqrt{\lambda_1}$.

So a **large eigenvalue means a steep wall and a short axis**; a small eigenvalue means a gentle slope and a long axis.

**Worked example 9.6.** For $S=\begin{bmatrix}2&1\\1&2\end{bmatrix}$, the ellipse $x^\top Sx=1$ has its short axis along $(1,1)$, of half-length $1/\sqrt3\approx0.58$, and its long axis along $(1,-1)$, of half-length $1$.

---

## 9.6 Why optimization cares: the Hessian

### The second derivative test in many dimensions

For a function $f(x)$ of one variable, a critical point ($f'=0$) is a minimum if $f''>0$. For a function of many variables, the second derivative is a **matrix**, the **Hessian**:

$$
H=\begin{bmatrix}\dfrac{\partial^2f}{\partial x_1^2}&\dfrac{\partial^2f}{\partial x_1\partial x_2}&\cdots\\\dfrac{\partial^2f}{\partial x_2\partial x_1}&\dfrac{\partial^2f}{\partial x_2^2}&\cdots\\\vdots&&\ddots\end{bmatrix}.
$$

It is symmetric. Near a critical point $x^*$ (where the gradient is zero), Taylor's theorem says

$$
f(x^*+d)\approx f(x^*)+\tfrac12\,d^\top Hd.
$$

So the function looks like a quadratic form near $x^*$, and:

| $H$ at the critical point | Type |
|---|---|
| positive definite | local **minimum** |
| negative definite | local **maximum** |
| indefinite | **saddle point** |
| semidefinite (some zero eigenvalue) | test is inconclusive |

**Worked example 9.7.** $f(x,y)=x^2+xy+y^2-3x$.

- Gradient: $(2x+y-3,\;x+2y)$. Set to zero: $x=-2y$, then $-4y+y=3$, so $y=-1$, $x=2$. Critical point $(2,-1)$.
- Hessian: $H=\begin{bmatrix}2&1\\1&2\end{bmatrix}$, positive definite (example 9.3).
- So $(2,-1)$ is a minimum, with value $4-2+1-6=-3$.

**Worked example 9.8.** $f(x,y)=x^2-y^2$. Critical point $(0,0)$. $H=\begin{bmatrix}2&0\\0&-2\end{bmatrix}$, eigenvalues $2,-2$: a **saddle**. Moving along $x$ goes up; moving along $y$ goes down. Saddle points are extremely common in the loss landscapes of neural networks.

### Conditioning: stretched bowls are slow

The ratio $\lambda_{\max}/\lambda_{\min}$ of the Hessian measures how **stretched** the bowl is. A round bowl (ratio 1) is easy for gradient descent: the steepest-descent direction points straight at the minimum. A long, narrow valley (large ratio) makes gradient descent zigzag across the steep walls while creeping along the flat floor.

The animation in [[01 Math for Learning]] shows exactly this for $L=\tfrac12(x^2+5y^2)$, whose Hessian has eigenvalues 1 and 5. Chapter 12 quantifies it.

---

## 9.7 Cholesky factorization

Every positive definite matrix can be written as

$$
S=LL^\top,
$$

with $L$ lower triangular with positive diagonal entries. Think of $L$ as a **matrix square root** of $S$.

**Worked example 9.9.** For $S=\begin{bmatrix}4&2\\2&3\end{bmatrix}$, try $L=\begin{bmatrix}a&0\\b&c\end{bmatrix}$:

$$
LL^\top=\begin{bmatrix}a^2&ab\\ab&b^2+c^2\end{bmatrix}=\begin{bmatrix}4&2\\2&3\end{bmatrix}.
$$

So $a=2$, $b=1$, $c=\sqrt2$.

**Uses.**

- **Solving $Sx=b$** about twice as fast as LU, and very stable.
- **Testing** positive definiteness: Cholesky succeeds exactly when $S$ is positive definite.
- **Sampling correlated noise**: if $z$ has independent standard normal entries, then $Lz$ has covariance $LL^\top=S$ ([[PS 07 The Multivariate Gaussian]]).

---

## Summary

| Idea | Fact |
|---|---|
| symmetric | $S^\top=S$ |
| spectral theorem | real eigenvalues, orthonormal eigenvectors, $S=Q\Lambda Q^\top$ |
| quadratic form | $x^\top Sx=\sum\lambda_iy_i^2$ in eigen-coordinates |
| positive definite | $x^\top Sx>0$; all $\lambda>0$; all pivots $>0$; all leading minors $>0$ |
| level sets | ellipses with half-axes $1/\sqrt{\lambda_i}$ along eigenvectors |
| Hessian test | PD: min; ND: max; indefinite: saddle |
| Cholesky | $S=LL^\top$ for positive definite $S$ |

**Three facts to remember:**

1. Symmetric means a pure stretch along perpendicular axes.
2. Positive definite means a bowl with a single bottom.
3. The eigenvalues of the Hessian tell you min, max, or saddle, and how hard the bowl is to descend.

---

## Exercises

### Part A: warm-up

**A1.** Write the symmetric matrix for $f(x,y)=5x^2+6xy+2y^2$.

**A2.** Is $\begin{bmatrix}3&1\\1&1\end{bmatrix}$ positive definite? Use two different tests.

**A3.** Find the eigenvalues of $\begin{bmatrix}5&0\\0&-2\end{bmatrix}$ and classify the shape of $x^\top Sx$.

**A4.** Find $Q$ and $\Lambda$ for $S=\begin{bmatrix}5&3\\3&5\end{bmatrix}$.

> [!success]- Solutions to Part A
> **A1.** $\begin{bmatrix}5&3\\3&2\end{bmatrix}$.
>
> **A2.** Minors: $3>0$ and $3-1=2>0$. Eigenvalues: trace 4, det 2, $\lambda=2\pm\sqrt2$, both positive. Yes.
>
> **A3.** $5$ and $-2$: indefinite, a saddle.
>
> **A4.** Eigenvalues $8$ and $2$ with eigenvectors $(1,1)$ and $(1,-1)$. $Q=\tfrac1{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix}$, $\Lambda=\operatorname{diag}(8,2)$.

### Part B: core

**B1.** Find and classify the critical points of $f(x,y)=x^3-3x+y^2$.

**B2.** For $S=\begin{bmatrix}3&1\\1&3\end{bmatrix}$, describe the ellipse $x^\top Sx=1$: axis directions and half-lengths.

**B3.** For which values of $c$ is $\begin{bmatrix}2&1&0\\1&2&1\\0&1&c\end{bmatrix}$ positive definite?

**B4.** Find the Cholesky factor of $\begin{bmatrix}9&3\\3&5\end{bmatrix}$.

**B5.** A covariance matrix is $\Sigma=\begin{bmatrix}4&2\\2&4\end{bmatrix}$. Find the directions of greatest and least spread, and the standard deviation in each.

> [!success]- Solutions to Part B
> **B1.** Gradient $(3x^2-3,\;2y)=0$ at $(1,0)$ and $(-1,0)$. Hessian $\begin{bmatrix}6x&0\\0&2\end{bmatrix}$. At $(1,0)$: $\operatorname{diag}(6,2)$, minimum. At $(-1,0)$: $\operatorname{diag}(-6,2)$, saddle.
>
> **B2.** Eigenvalues $4$ along $(1,1)$ and $2$ along $(1,-1)$. Half-lengths $1/2$ along $(1,1)$ and $1/\sqrt2\approx0.71$ along $(1,-1)$.
>
> **B3.** Leading minors: $2>0$; $4-1=3>0$; full determinant $2(2c-1)-1(c-0)=3c-2>0$. So $c>\tfrac23$.
>
> **B4.** $a^2=9$ so $a=3$; $ab=3$ so $b=1$; $b^2+c^2=5$ so $c=2$. $L=\begin{bmatrix}3&0\\1&2\end{bmatrix}$.
>
> **B5.** Eigenvalues $6$ along $(1,1)$ and $2$ along $(1,-1)$. Standard deviations $\sqrt6\approx2.45$ and $\sqrt2\approx1.41$. The data spreads most along the diagonal: the two variables are positively correlated.

### Part C: explain and prove

**C1.** Prove that if $S$ is positive definite then every diagonal entry is positive. (Hint: choose $x=e_i$.)

**C2.** Prove that if $S$ is positive definite, it is invertible, and $S^{-1}$ is also positive definite.

**C3.** Prove that $A^\top A$ is always positive semidefinite, for any matrix $A$.

**C4 (ridge regression).** Prove that $A^\top A+\lambda I$ is positive definite for any matrix $A$ and any $\lambda>0$. Explain why this means ridge regression, which solves $(A^\top A+\lambda I)x=A^\top b$, always has exactly one solution, even when the columns of $A$ are dependent.

**C5.** Show that the eigenvalues of a symmetric matrix are real, for $2\times2$ matrices, using the discriminant of the characteristic polynomial.

> [!success]- Solutions to Part C
> **C1.** $e_i^\top Se_i=s_{ii}$, and this must be positive.
>
> **C2.** All eigenvalues are positive, so none is zero and $S$ is invertible. $S^{-1}=Q\Lambda^{-1}Q^\top$ has eigenvalues $1/\lambda_i>0$.
>
> **C3.** $x^\top A^\top Ax=\|Ax\|^2\ge0$.
>
> **C4.** $x^\top(A^\top A+\lambda I)x=\|Ax\|^2+\lambda\|x\|^2$. The first term is at least 0 and the second is strictly positive when $x\neq0$. Positive definite matrices are invertible, so the system has exactly one solution. Adding $\lambda I$ lifts every eigenvalue of $A^\top A$ by $\lambda$, so none can be zero.
>
> **C5.** For $\begin{bmatrix}a&b\\b&c\end{bmatrix}$: $\lambda^2-(a+c)\lambda+(ac-b^2)=0$. Discriminant $(a+c)^2-4(ac-b^2)=(a-c)^2+4b^2\ge0$, a sum of squares. So the roots are real.

### Part D: practise with code

**D1.** `np.linalg.eigh(S)` is the eigen-solver for symmetric matrices. Use it on example 9.5 and confirm all eigenvalues are positive. Check that the eigenvector matrix $Q$ satisfies `Q.T @ Q ≈ I`.

**D2.** Use `np.linalg.cholesky` on a positive definite matrix and on $\begin{bmatrix}1&2\\2&1\end{bmatrix}$. What happens in the second case?

**D3.** Draw contour plots (`plt.contour`) of $x^\top Sx$ for $S=\begin{bmatrix}1&0\\0&1\end{bmatrix}$, $\begin{bmatrix}1&0\\0&10\end{bmatrix}$, $\begin{bmatrix}2&1\\1&2\end{bmatrix}$ and $\begin{bmatrix}1&2\\2&1\end{bmatrix}$. Label each as bowl, stretched bowl, tilted bowl, or saddle.

**D4.** Run gradient descent $x\leftarrow x-\eta Sx$ from $(1,1)$ on the bowls $S=\operatorname{diag}(1,1)$ and $S=\operatorname{diag}(1,10)$, with the largest stable step size for each ($\eta<2/\lambda_{\max}$). Count the steps needed to reach $\|x\|<10^{-3}$.

> [!success]- Hints for Part D
> **D2.** It raises `LinAlgError: Matrix is not positive definite`. That is a practical positive-definiteness test.
>
> **D4.** The round bowl converges in a few steps; the stretched bowl takes many more, because the safe step size is limited by the steep direction while progress is limited by the flat one.

---

## Where this is used

- **Covariance matrices** and their uncertainty ellipses ([[PS 07 The Multivariate Gaussian]], [[04 Perception and State]]).
- **Control costs** $x^\top Qx+u^\top Ru$ use positive definite weights so the cost has a unique minimum ([[03 Dynamics and Feedback]]).
- **Mass matrices** of robots are positive definite, because kinetic energy is positive for any motion.
- **Second-order optimizers** (Newton's method) use the Hessian directly.

Next: [[LA 10 Singular Value Decomposition]], which extends "stretch along perpendicular axes" to **every** matrix.

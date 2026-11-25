---
type: course-chapter
course: linear-algebra
chapter: 6
tags: [mathematics, linear-algebra]
---

# Chapter 6: Orthogonality and least squares

Previous: [[LA 05 Subspaces Basis and Rank]] | [[LA 00 Course Map]] | Next: [[LA 07 Determinants]]

> [!abstract] The big idea
> When $Ax=b$ has no solution, aim for the closest reachable point instead. The closest point in the column space is the **projection** of $b$, and "closest" means the leftover error is **perpendicular** to every column. That one condition gives the normal equations $A^\top A\hat x=A^\top b$, which is linear regression.

> [!info] In this chapter you will learn to
> 1. Explain why noisy data gives systems with no exact solution.
> 2. Derive and solve the normal equations.
> 3. Fit lines and curves to data by least squares.
> 4. Work with orthonormal vectors and orthogonal matrices.
> 5. Build an orthonormal basis with Gram-Schmidt, and understand $A=QR$.

> [!tip] Before you start
> You need projection onto a vector ([[LA 02 Dot Product Length and Angle]], section 2.6), column space ([[LA 05 Subspaces Basis and Rank]]), and transposes ([[LA 03 Matrices as Linear Maps]]).

---

## 6.1 The problem: too many equations

### Where it comes from

You measure a spring: hang a weight, record the stretch. Theory says stretch $=k\times$ weight. With 2 measurements you could solve exactly. With 20 noisy measurements, no single $k$ fits them all exactly.

In matrix form, you have **more equations than unknowns** (a tall $A$), and $b$ is almost never in the column space. $Ax=b$ has no solution.

Giving up is not an option. Instead we ask for the **best** $x$.

### What "best" means

For any guess $x$, the **residual** is the error vector

$$
r=b-Ax.
$$

Each entry is how far off one equation is. We choose $x$ to make the residual as short as possible:

> [!note] Least squares problem
> $$
> \hat x=\arg\min_x\|Ax-b\|^2=\arg\min_x\sum_i\big(b_i-(Ax)_i\big)^2.
> $$

"$\arg\min$" means "the $x$ that minimizes". "Least squares" because we minimize a **sum of squared errors**.

*Why squares?* Squares make every error positive, so errors cannot cancel; they punish big errors more than small ones; and, most importantly, they lead to a linear system you can solve exactly. (In probability terms, squared error is the right choice when noise is Gaussian: see [[PS 09 Estimation and Maximum Likelihood]].)

---

## 6.2 The geometric solution

### The picture

- As $x$ varies, $Ax$ sweeps out the **column space** $C(A)$: a flat subspace (a plane, say) inside $\mathbb R^m$.
- $b$ sits somewhere **off** that plane.
- We want the point $p=A\hat x$ in the plane **closest** to $b$.

From chapter 2: the closest point on a line is found by dropping a perpendicular. The same is true for a plane. The closest point is the **projection** of $b$ onto $C(A)$, and the error $b-p$ sticks straight out of the plane.

```
                 b
                 |
                 |  r = b - p   (perpendicular to the plane)
                 |
     ____________●______________
    /            p              /
   /     column space C(A)     /
  /___________________________/
```

### Why perpendicular means closest

Let $p$ be the point where $b-p$ is perpendicular to the plane, and let $q$ be any other point in the plane. Then $p-q$ lies in the plane, so it is perpendicular to $b-p$. By Pythagoras (chapter 2):

$$
\|b-q\|^2=\|b-p\|^2+\|p-q\|^2\ge\|b-p\|^2.
$$

So $q$ is never closer than $p$. Equality only when $q=p$.

### From perpendicular to equations

"The residual is perpendicular to the column space" means it is perpendicular to **every column** of $A$. Each column $a_j$ gives one equation:

$$
a_j\cdot(b-A\hat x)=0\quad\text{for every }j.
$$

Stacking all of these: the columns of $A$ are the rows of $A^\top$, so

$$
A^\top(b-A\hat x)=0.
$$

Rearranged:

> [!important] The normal equations
> $$
> A^\top A\,\hat x=A^\top b.
> $$

($A^\top A$ is square, $n\times n$, even though $A$ is tall.) They are called "normal" because "normal" is another word for perpendicular.

If the columns of $A$ are independent, $A^\top A$ is invertible (chapter 5, exercise C4) and

$$
\hat x=(A^\top A)^{-1}A^\top b.
$$

### Compare with projection onto one vector

In chapter 2, projecting $b$ onto a single vector $a$ gave $c=\dfrac{a\cdot b}{a\cdot a}$, that is $(a^\top a)\,c=a^\top b$. The normal equations are **exactly the same equation**, with the single vector $a$ replaced by the matrix $A$, and division replaced by solving a system. Least squares is projection, nothing more.

---

## 6.3 Worked examples

### Worked example 6.1: fitting a line

Fit $y=c+dt$ to the three points $(t,y)=(0,1)$, $(1,2)$, $(2,4)$.

**Step 1: write one equation per point.** We want $c+d\,t_i=y_i$:

$$
\begin{aligned}c+0d&=1\\c+1d&=2\\c+2d&=4\end{aligned}
\qquad\Longleftrightarrow\qquad
\underbrace{\begin{bmatrix}1&0\\1&1\\1&2\end{bmatrix}}_{A}\begin{bmatrix}c\\d\end{bmatrix}=\underbrace{\begin{bmatrix}1\\2\\4\end{bmatrix}}_{b}.
$$

The column of ones multiplies $c$ (the intercept); the column of $t$ values multiplies $d$ (the slope). The points are not on one line ($1\to2$ is a rise of 1, $2\to4$ a rise of 2), so there is no exact solution.

**Step 2: compute $A^\top A$ and $A^\top b$.**

$$
A^\top A=\begin{bmatrix}1&1&1\\0&1&2\end{bmatrix}\begin{bmatrix}1&0\\1&1\\1&2\end{bmatrix}=\begin{bmatrix}3&3\\3&5\end{bmatrix},\qquad
A^\top b=\begin{bmatrix}1+2+4\\0+2+8\end{bmatrix}=\begin{bmatrix}7\\10\end{bmatrix}.
$$

Notice what the entries mean: $3$ is the number of points, $3$ is $\sum t_i$, $5$ is $\sum t_i^2$, $7$ is $\sum y_i$, $10$ is $\sum t_iy_i$.

**Step 3: solve.**

$$
\begin{aligned}3c+3d&=7\\3c+5d&=10\end{aligned}
\quad\Longrightarrow\quad2d=3,\;d=1.5,\;c=\tfrac{7-4.5}3=\tfrac56\approx0.833.
$$

**Best line:** $y\approx0.833+1.5t$.

**Step 4: look at the residual.** Fitted values $p=A\hat x=(0.833,\;2.333,\;3.833)$. Residual $r=b-p=(0.167,\;-0.333,\;0.167)$.

**Step 5: verify perpendicularity.**

- $r\cdot(1,1,1)=0.167-0.333+0.167=0$ ✓
- $r\cdot(0,1,2)=0-0.333+0.333=0$ ✓

The residual is perpendicular to both columns, exactly as the theory promised. Its squared length, $0.0278+0.1111+0.0278\approx0.167$, is the smallest possible.

### Worked example 6.2: least squares generalizes averaging

You measure the same quantity three times: $x=1$, $x=3$, $x=5$. Best single value?

$$
A=\begin{bmatrix}1\\1\\1\end{bmatrix},\quad b=\begin{bmatrix}1\\3\\5\end{bmatrix},\quad A^\top A=3,\quad A^\top b=9,\quad\hat x=3.
$$

The **mean**. Least squares, applied to "one unknown measured several times", gives the average. Everything in this chapter is a generalization of averaging.

### Worked example 6.3: fitting a parabola

Fit $y=c_0+c_1t+c_2t^2$ to $(-1,2)$, $(0,1)$, $(1,2)$, $(2,5)$. The model is **linear in the unknowns** $c_0,c_1,c_2$, even though it is curved in $t$, so least squares still applies. Just add a column of $t^2$:

$$
A=\begin{bmatrix}1&-1&1\\1&0&0\\1&1&1\\1&2&4\end{bmatrix},\quad b=\begin{bmatrix}2\\1\\2\\5\end{bmatrix}.
$$

$$
A^\top A=\begin{bmatrix}4&2&6\\2&6&8\\6&8&18\end{bmatrix},\quad A^\top b=\begin{bmatrix}10\\10\\24\end{bmatrix}.
$$

Solving gives $c_0=1$, $c_1=0$, $c_2=1$: the parabola $y=1+t^2$, which passes through all four points exactly. When the data fits the model perfectly, least squares finds the exact answer and the residual is zero.

> [!tip] What "linear" means in linear regression
> The word refers to the **unknown coefficients**, not the input. $c_0+c_1t+c_2t^2$, $c_0+c_1\sin t$, and $c_0+c_1e^t$ are all fitted by linear least squares. $c_0e^{c_1t}$ is not (the unknown $c_1$ is inside the exponential).

> [!question]- Check yourself
> 1. For fitting $y=c+dt$, what are the two columns of $A$?
> 2. If the residual is not perpendicular to the columns, what does that tell you about your $\hat x$?
> 3. Fit $y=c$ (a horizontal line) to $(0,2)$, $(1,3)$, $(2,7)$.
>
> **Answers.** 1. A column of ones and a column of the $t$ values. 2. It is not the least squares solution; you made an error. 3. $c$ is the mean of the $y$ values, $4$.

---

## 6.4 The projection matrix

The projected point is $p=A\hat x=A(A^\top A)^{-1}A^\top b$. The matrix in front of $b$ is the **projection matrix**:

$$
P=A(A^\top A)^{-1}A^\top.
$$

It takes any $b$ to its shadow in the column space. Two properties:

- $P^2=P$: projecting twice is the same as projecting once (the shadow of a shadow is itself).
- $P^\top=P$: it is symmetric.

And $I-P$ projects onto the perpendicular complement: it gives the residual $r=(I-P)b$.

---

## 6.5 Orthonormal vectors and orthogonal matrices

### Definitions

> [!note] Definition: orthonormal
> Vectors $q_1,\dots,q_k$ are **orthonormal** if each has length 1 and each pair is perpendicular:
> $$
> q_i\cdot q_j=\begin{cases}1&i=j\\0&i\neq j\end{cases}
> $$

Put them as the columns of a matrix $Q$. Then entry $(i,j)$ of $Q^\top Q$ is $q_i\cdot q_j$, so

$$
Q^\top Q=I.
$$

If $Q$ is also **square**, it is called an **orthogonal matrix**, and then $Q^{-1}=Q^\top$. **The inverse costs nothing: just transpose.**

### What orthogonal matrices do

They **preserve lengths and angles**:

$$
\|Qx\|^2=(Qx)^\top(Qx)=x^\top Q^\top Qx=x^\top x=\|x\|^2.
$$

So they are exactly the **rotations and reflections**. Every rotation matrix in robotics is orthogonal, and checking $R^\top R=I$ is a standard sanity test on a computed rotation.

**Examples.** $R_\theta$ from chapter 3. Permutation matrices (which reorder coordinates). $\tfrac1{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix}$.

### Why orthonormal bases are so convenient

**Coordinates become dot products.** If $q_1,\dots,q_n$ is an orthonormal basis, then for any $v$,

$$
v=(q_1\cdot v)\,q_1+(q_2\cdot v)\,q_2+\cdots+(q_n\cdot v)\,q_n.
$$

*Why:* write $v=\sum c_jq_j$ and dot both sides with $q_i$. Every term vanishes except $c_i(q_i\cdot q_i)=c_i$. So $c_i=q_i\cdot v$. No system of equations to solve.

**Worked example 6.4.** $q_1=\tfrac1{\sqrt2}(1,1)$, $q_2=\tfrac1{\sqrt2}(1,-1)$, and $v=(3,1)$.

$c_1=q_1\cdot v=\tfrac4{\sqrt2}=2\sqrt2$ and $c_2=q_2\cdot v=\tfrac2{\sqrt2}=\sqrt2$.

Check: $2\sqrt2\cdot\tfrac1{\sqrt2}(1,1)+\sqrt2\cdot\tfrac1{\sqrt2}(1,-1)=(2,2)+(1,-1)=(3,1)$ ✓.

**Least squares becomes trivial.** If $A=Q$ has orthonormal columns, the normal equations $Q^\top Q\hat x=Q^\top b$ become simply

$$
\hat x=Q^\top b.
$$

---

## 6.6 Gram-Schmidt: making vectors orthonormal

### The idea

Given independent vectors $a_1,a_2,a_3,\dots$ we want orthonormal $q_1,q_2,q_3,\dots$ spanning the same space. Process them one at a time: **take the next vector, remove its components along the directions already found, and normalize what is left.**

### The procedure

$$
\begin{aligned}
q_1&=\frac{a_1}{\|a_1\|}\\[4pt]
u_2&=a_2-(q_1\cdot a_2)\,q_1,&q_2&=\frac{u_2}{\|u_2\|}\\[4pt]
u_3&=a_3-(q_1\cdot a_3)\,q_1-(q_2\cdot a_3)\,q_2,&q_3&=\frac{u_3}{\|u_3\|}
\end{aligned}
$$

Each subtraction removes a projection (chapter 2). What remains is perpendicular to everything before it.

### Worked example 6.5

$a_1=(1,1,0)$, $a_2=(1,0,1)$.

**Step 1.** $\|a_1\|=\sqrt2$, so $q_1=\tfrac1{\sqrt2}(1,1,0)$.

**Step 2.** Remove the $q_1$ component from $a_2$. $q_1\cdot a_2=\tfrac1{\sqrt2}$, so

$$
u_2=(1,0,1)-\tfrac1{\sqrt2}\cdot\tfrac1{\sqrt2}(1,1,0)=(1,0,1)-(0.5,0.5,0)=(0.5,-0.5,1).
$$

**Step 3.** Normalize: $\|u_2\|=\sqrt{0.25+0.25+1}=\sqrt{1.5}$, so $q_2=\dfrac{(0.5,-0.5,1)}{\sqrt{1.5}}$.

**Check:** $q_1\cdot q_2\propto(1)(0.5)+(1)(-0.5)+0=0$ ✓.

### QR factorization

Gram-Schmidt can be recorded as

$$
A=QR,
$$

where $Q$ has orthonormal columns and $R$ is **upper triangular** (because each $a_j$ is built only from $q_1,\dots,q_j$).

Least squares then becomes:

$$
A^\top A\hat x=A^\top b\;\Longrightarrow\;R^\top Q^\top QR\hat x=R^\top Q^\top b\;\Longrightarrow\;R\hat x=Q^\top b,
$$

solved by back-substitution. This is how software actually solves least squares, because it avoids forming $A^\top A$, which squares the sensitivity to rounding error (chapter 12).

---

## 6.7 Pitfalls of least squares

- **Outliers.** Squaring errors means one wild point can drag the whole fit. If your data has outliers, look at them, or use a robust loss (absolute error, Huber loss).
- **Dependent columns.** If two features are copies or combinations of each other, $A^\top A$ is singular and there is no unique answer. Remove the redundancy or add regularization (ridge regression, chapter 9 exercise C4).
- **Extrapolation.** A fit is trustworthy only near the data. A parabola fitted on $t\in[0,2]$ may be wildly wrong at $t=10$.
- **Overfitting.** With as many parameters as data points you can fit every point exactly, including the noise. More parameters is not always better.

---

## Summary

| Idea | Formula |
|---|---|
| residual | $r=b-Ax$ |
| least squares | minimize $\|Ax-b\|^2$ |
| condition | residual $\perp$ every column |
| normal equations | $A^\top A\hat x=A^\top b$ |
| projection matrix | $P=A(A^\top A)^{-1}A^\top$, $P^2=P$ |
| orthogonal matrix | $Q^\top Q=I$, $Q^{-1}=Q^\top$, preserves length |
| coordinates in an orthonormal basis | $c_i=q_i\cdot v$ |
| QR least squares | $R\hat x=Q^\top b$ |

**Three facts to remember:**

1. Closest point = projection = perpendicular error.
2. Least squares is the matrix version of averaging.
3. Orthonormal columns turn every hard step into a dot product.

---

## Exercises

### Part A: warm-up

**A1.** Project $b=(1,2,3)$ onto the line through $a=(1,1,1)$. Give the residual and check it is perpendicular to $a$.

**A2.** Find the least squares solution of $x=2$, $x=4$, $x=9$.

**A3.** Is $\dfrac15\begin{bmatrix}3&-4\\4&3\end{bmatrix}$ orthogonal? What is its inverse?

**A4.** Write the coordinates of $(2,5)$ in the orthonormal basis $q_1=(0.6,0.8)$, $q_2=(-0.8,0.6)$.

> [!success]- Solutions to Part A
> **A1.** $c=6/3=2$, $p=(2,2,2)$, $r=(-1,0,1)$, $r\cdot a=0$ ✓.
>
> **A2.** The mean, $5$.
>
> **A3.** Columns $(0.6,0.8)$ and $(-0.8,0.6)$ are unit length and perpendicular. Yes. Inverse is the transpose, $\tfrac15\begin{bmatrix}3&4\\-4&3\end{bmatrix}$.
>
> **A4.** $c_1=1.2+4=5.2$, $c_2=-1.6+3=1.4$. Check: $5.2(0.6,0.8)+1.4(-0.8,0.6)=(3.12-1.12,\;4.16+0.84)=(2,5)$ ✓.

### Part B: core

**B1.** Fit $y=c+dt$ to $(1,1)$, $(2,3)$, $(3,4)$, $(4,6)$. Give the fitted values and the residual, and verify perpendicularity.

**B2.** Fit $y=dt$ (a line through the origin) to the same data. Why is this a different answer from B1?

**B3.** Apply Gram-Schmidt to $a_1=(1,0,1)$, $a_2=(1,1,0)$, $a_3=(0,1,1)$.

**B4.** A spring stretches 2.1 cm, 3.9 cm and 6.2 cm under weights of 1, 2 and 3 kg. Fit stretch $=k\cdot$weight by least squares.

**B5.** Compute the projection matrix onto the line through $a=(1,2)$, and check that $P^2=P$.

> [!success]- Solutions to Part B
> **B1.** $A$ has a column of ones and the column $(1,2,3,4)$.
> $$A^\top A=\begin{bmatrix}4&10\\10&30\end{bmatrix},\qquad A^\top b=\begin{bmatrix}\sum y_i\\\sum t_iy_i\end{bmatrix}=\begin{bmatrix}14\\43\end{bmatrix}.$$
> So $4c+10d=14$ and $10c+30d=43$. Multiply the first by 2.5 and subtract it from the second: $5d=8$, so $d=1.6$ and $c=(14-16)/4=-0.5$.
>
> Fitted values $(1.1,\,2.7,\,4.3,\,5.9)$; residual $(-0.1,\,0.3,\,-0.3,\,0.1)$.
>
> Checks: $r\cdot(1,1,1,1)=0$ ✓ and $r\cdot(1,2,3,4)=-0.1+0.6-0.9+0.4=0$ ✓.
>
> A common slip here is computing $\sum t_iy_i$ wrongly; the perpendicularity check catches it immediately, because the residual will not come out perpendicular.
>
> **B2.** $A=(1,2,3,4)^\top$, $A^\top A=30$, $A^\top b=43$, $d=43/30\approx1.433$. Different because the intercept is forced to be 0: the model has one fewer column, so its column space is smaller.
>
> **B3.** $q_1=\tfrac1{\sqrt2}(1,0,1)$. $u_2=(1,1,0)-\tfrac12(1,0,1)=(0.5,1,-0.5)$, $q_2=u_2/\sqrt{1.5}$. $u_3=(0,1,1)-\tfrac12(1,0,1)-\dfrac{(0,1,1)\cdot u_2}{\|u_2\|^2}u_2=(-0.5,1,0.5)-\dfrac{0.5}{1.5}(0.5,1,-0.5)=(-\tfrac23,\tfrac23,\tfrac23)$, $q_3=\tfrac1{\sqrt3}(-1,1,1)$.
>
> **B4.** $k=\dfrac{1(2.1)+2(3.9)+3(6.2)}{1+4+9}=\dfrac{28.5}{14}\approx2.04$ cm per kg.
>
> **B5.** $P=\dfrac{aa^\top}{a^\top a}=\dfrac15\begin{bmatrix}1&2\\2&4\end{bmatrix}$. $P^2=\dfrac1{25}\begin{bmatrix}5&10\\10&20\end{bmatrix}=P$ ✓.

### Part C: explain and prove

**C1.** Prove that $P=A(A^\top A)^{-1}A^\top$ satisfies $P^2=P$ and $P^\top=P$.

**C2.** Prove that if $Q$ is orthogonal, then $(Qx)\cdot(Qy)=x\cdot y$. What does this say about angles?

**C3.** Explain why the least squares residual must sum to zero whenever the model includes an intercept (a column of ones).

**C4.** Prove that the product of two orthogonal matrices is orthogonal. Interpret for rotations.

> [!success]- Solutions to Part C
> **C1.** $P^2=A(A^\top A)^{-1}(A^\top A)(A^\top A)^{-1}A^\top=A(A^\top A)^{-1}A^\top=P$. $P^\top=A\big((A^\top A)^{-1}\big)^\top A^\top=P$, because $A^\top A$ is symmetric, so its inverse is too.
>
> **C2.** $(Qx)^\top(Qy)=x^\top Q^\top Qy=x^\top y$. Dot products are preserved, so lengths and angles are too.
>
> **C3.** The residual is perpendicular to every column, including $(1,1,\dots,1)$, and $r\cdot(1,\dots,1)=\sum r_i$.
>
> **C4.** $(Q_1Q_2)^\top(Q_1Q_2)=Q_2^\top Q_1^\top Q_1Q_2=Q_2^\top Q_2=I$. Doing one rotation after another is still a rotation (or reflection).

### Part D: practise with code

**D1.** Solve B1 with `np.linalg.lstsq(A, b, rcond=None)`. Compare with solving the normal equations by `np.linalg.solve(A.T @ A, A.T @ b)`.

**D2.** Generate 50 points from $y=2+0.5t+\text{noise}$ with $t\in[0,10]$. Fit a line, plot the data and the fit, and plot the residuals against $t$. What should a good residual plot look like?

**D3.** Fit polynomials of degree 1, 3 and 15 to 20 noisy points from $y=\sin t$. Plot them. Which one overfits? Compute the error on 100 fresh points.

**D4.** Use `np.linalg.qr(A)` on a random $5\times3$ matrix. Check that `Q.T @ Q` is the identity and that `R` is upper triangular.

> [!success]- Hints for Part D
> **D2.** A good residual plot is a shapeless cloud around zero. A curve or a funnel shape means the model is missing something.
>
> **D3.** Degree 15 passes close to every training point but swings wildly between them, so its error on fresh points is much larger. Degree 3 is usually best here.

---

## Where this is used

- **Calibration.** Camera intrinsics, hand-eye calibration and sensor offsets are fitted by (often nonlinear) least squares ([[04 Perception and State]]).
- **Kalman filter.** Each update is a weighted least squares problem balancing prediction and measurement.
- **Training networks.** Minimizing squared loss with gradient descent is the nonlinear version of this chapter ([[05 Training Neural Policies]]).

Next: [[LA 07 Determinants]]: one number that says how much a matrix scales volume.

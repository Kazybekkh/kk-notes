---
type: course-chapter
course: linear-algebra
chapter: 10
tags: [mathematics, linear-algebra]
---

# Chapter 10: The singular value decomposition

Previous: [[LA 09 Symmetric and Positive Definite Matrices]] | [[LA 00 Course Map]] | Next: [[LA 11 Change of Basis]]

> [!abstract] The big idea
> **Every** matrix, of any shape, can be broken into three simple steps: a rotation, a stretch along perpendicular axes, and another rotation. The stretch factors are the **singular values**. They tell you the rank, how much the matrix can amplify things, which directions matter most, and how to approximate the matrix with far less data. The SVD is the most useful single factorization in applied mathematics.

> [!info] In this chapter you will learn to
> 1. State the SVD, $A=U\Sigma V^\top$, and explain each factor with a picture.
> 2. Compute the SVD of a small matrix by hand from $A^\top A$.
> 3. Read rank, norm, condition number and the four subspaces off the SVD.
> 4. Build the best low-rank approximation of a matrix.
> 5. Explain principal component analysis (PCA) and the pseudoinverse in terms of the SVD.

> [!tip] Before you start
> This chapter leans on the spectral theorem ([[LA 09 Symmetric and Positive Definite Matrices]]), the four subspaces ([[LA 05 Subspaces Basis and Rank]]), and orthogonal matrices ([[LA 06 Orthogonality and Least Squares]]).

---

## 10.1 Why eigenvalues are not enough

Eigen-decomposition $A=V\Lambda V^{-1}$ is powerful, but:

- it only works for **square** matrices,
- it can involve **complex** numbers (rotations),
- it can **fail** entirely (defective matrices like the shear),
- the eigenvectors are generally **not perpendicular**, so $V^{-1}$ can be badly behaved.

Symmetric matrices had none of these problems (chapter 9). The SVD gets the same clean behaviour for **every** matrix, by allowing the input directions and output directions to be **different** sets of perpendicular axes.

---

## 10.2 The statement

> [!important] Singular value decomposition
> Any real $m\times n$ matrix $A$ can be written
> $$
> A=U\Sigma V^\top,
> $$
> where
> - $V$ is an $n\times n$ orthogonal matrix. Its columns $v_1,\dots,v_n$ are the **right singular vectors** (perpendicular **input** directions).
> - $U$ is an $m\times m$ orthogonal matrix. Its columns $u_1,\dots,u_m$ are the **left singular vectors** (perpendicular **output** directions).
> - $\Sigma$ is $m\times n$, zero except on its diagonal, which holds the **singular values** $\sigma_1\ge\sigma_2\ge\cdots\ge0$.

### One direction at a time

Multiply $A=U\Sigma V^\top$ on the right by $V$: $AV=U\Sigma$. Column by column:

$$
Av_i=\sigma_iu_i.
$$

**$A$ takes the input direction $v_i$ to the output direction $u_i$, stretched by $\sigma_i$.**

Compare with eigenvectors, $Av=\lambda v$, where the output had to point the **same** way as the input. The SVD allows the output to point somewhere else, and in exchange guarantees that everything is perpendicular, real and non-negative.

### The picture: a sphere becomes an ellipsoid

Feed the **unit sphere** (all vectors of length 1) into $A$. The output is an **ellipsoid**.

- Its axes point along $u_1,u_2,\dots$
- Its semi-axis lengths are $\sigma_1,\sigma_2,\dots$
- The inputs that land on those axes are $v_1,v_2,\dots$

Reading $A=U\Sigma V^\top$ right to left as three steps:

1. **$V^\top$ rotates** the sphere. A rotated sphere is still a sphere. (It lines the $v_i$ up with the coordinate axes.)
2. **$\Sigma$ stretches** along the coordinate axes by $\sigma_1,\sigma_2,\dots$ Now it is an axis-aligned ellipsoid. (If $m\neq n$, it also adds or removes dimensions.)
3. **$U$ rotates** the ellipsoid into its final position.

So **every linear map is: rotate, stretch along axes, rotate.** Nothing else is possible.

---

## 10.3 How to compute it

### The connection to $A^\top A$

$A^\top A$ is symmetric and positive semidefinite (chapter 9), so the spectral theorem applies to it. Substitute the SVD:

$$
A^\top A=(U\Sigma V^\top)^\top(U\Sigma V^\top)=V\Sigma^\top U^\top U\Sigma V^\top=V(\Sigma^\top\Sigma)V^\top.
$$

This is exactly a spectral decomposition. So:

- the $v_i$ are the **eigenvectors of $A^\top A$**,
- the eigenvalues of $A^\top A$ are $\sigma_i^2$, so $\sigma_i=\sqrt{\lambda_i(A^\top A)}$.

Similarly the $u_i$ are eigenvectors of $AA^\top$.

### The recipe

1. Compute $A^\top A$.
2. Find its eigenvalues $\lambda_i$ (sorted largest first) and orthonormal eigenvectors $v_i$.
3. Singular values: $\sigma_i=\sqrt{\lambda_i}$.
4. For each nonzero $\sigma_i$: $u_i=\dfrac{Av_i}{\sigma_i}$.
5. If you need a full $U$, complete the $u_i$ to an orthonormal basis of $\mathbb R^m$.

### Worked example 10.1

$$
A=\begin{bmatrix}3&0\\4&5\end{bmatrix}.
$$

**Step 1.**

$$
A^\top A=\begin{bmatrix}3&4\\0&5\end{bmatrix}\begin{bmatrix}3&0\\4&5\end{bmatrix}=\begin{bmatrix}25&20\\20&25\end{bmatrix}.
$$

**Step 2.** Trace 50, determinant $625-400=225$. So $\lambda^2-50\lambda+225=0$, giving $\lambda=45$ and $\lambda=5$. Eigenvectors (this is the familiar $\begin{bmatrix}a&b\\b&a\end{bmatrix}$ pattern):

$$
v_1=\tfrac1{\sqrt2}(1,1),\qquad v_2=\tfrac1{\sqrt2}(1,-1).
$$

**Step 3.**

$$
\sigma_1=\sqrt{45}=3\sqrt5\approx6.71,\qquad\sigma_2=\sqrt5\approx2.24.
$$

**Step 4.**

$$
Av_1=\tfrac1{\sqrt2}(3,9),\qquad u_1=\frac{Av_1}{\sigma_1}=\frac{(3,9)}{\sqrt2\cdot3\sqrt5}=\frac{(1,3)}{\sqrt{10}}.
$$

$$
Av_2=\tfrac1{\sqrt2}(3,-1),\qquad u_2=\frac{Av_2}{\sigma_2}=\frac{(3,-1)}{\sqrt2\cdot\sqrt5}=\frac{(3,-1)}{\sqrt{10}}.
$$

**Checks.**

- $u_1\cdot u_2=\tfrac1{10}(3-3)=0$ ✓ (perpendicular).
- $\|u_1\|=\|u_2\|=1$ ✓.
- $\sigma_1\sigma_2=\sqrt{225}=15=|\det A|=|15-0|$ ✓. (The product of the stretches is the area scaling factor, chapter 7.)

**Meaning.** The input direction $(1,1)$ is stretched the most, by 6.71, and comes out along $(1,3)$. The direction $(1,-1)$ is stretched least, by 2.24, and comes out along $(3,-1)$.

### Worked example 10.2: a non-square matrix

$$
A=\begin{bmatrix}1&1\\0&0\\1&1\end{bmatrix}\quad(3\times2).
$$

$A^\top A=\begin{bmatrix}2&2\\2&2\end{bmatrix}$, eigenvalues $4$ and $0$, eigenvectors $\tfrac1{\sqrt2}(1,1)$ and $\tfrac1{\sqrt2}(1,-1)$.

So $\sigma_1=2$, $\sigma_2=0$. Then $u_1=Av_1/2=\tfrac1{2\sqrt2}(2,0,2)=\tfrac1{\sqrt2}(1,0,1)$.

One nonzero singular value: the rank is 1. The direction $v_2=(1,-1)/\sqrt2$ is sent to zero: it spans the null space.

> [!question]- Check yourself
> 1. What are the singular values of $\begin{bmatrix}2&0\\0&-3\end{bmatrix}$? How do they differ from the eigenvalues?
> 2. If $A=Q$ is orthogonal, what are its singular values?
> 3. A matrix has singular values $5,3,0$. What is its rank?
>
> **Answers.** 1. $3$ and $2$ (sizes of the stretches, sorted). Eigenvalues are $2$ and $-3$. 2. All 1: no stretching. 3. 2.

---

## 10.4 What the SVD tells you

| Quantity | From the SVD |
|---|---|
| rank | number of nonzero $\sigma_i$ |
| largest stretch (spectral norm) | $\|A\|_2=\sigma_1$, so $\|Ax\|\le\sigma_1\|x\|$ |
| smallest stretch (square, invertible) | $\sigma_n$ |
| condition number | $\kappa=\sigma_1/\sigma_r$ |
| volume scaling (square) | $\lvert\det A\rvert=\sigma_1\sigma_2\cdots\sigma_n$ |

### The four subspaces, with perfect bases

If the rank is $r$:

| Subspace | Orthonormal basis |
|---|---|
| row space | $v_1,\dots,v_r$ |
| null space | $v_{r+1},\dots,v_n$ |
| column space | $u_1,\dots,u_r$ |
| left null space | $u_{r+1},\dots,u_m$ |

This is the complete picture from chapter 5, now with perpendicular unit-length bases for every piece, and with the exact stretch factor $\sigma_i$ linking $v_i$ to $u_i$.

---

## 10.5 Low-rank approximation

### The SVD as a sum

Multiplying out $U\Sigma V^\top$ gives a sum of rank-one pieces:

$$
A=\sigma_1u_1v_1^\top+\sigma_2u_2v_2^\top+\cdots+\sigma_ru_rv_r^\top.
$$

Each piece $u_iv_i^\top$ is a simple matrix (every row is a multiple of $v_i^\top$). The pieces are ordered by importance: $\sigma_1$ is the biggest.

### Keeping the important pieces

Keep only the first $k$ terms:

$$
A_k=\sigma_1u_1v_1^\top+\cdots+\sigma_ku_kv_k^\top.
$$

> [!important] Eckart-Young theorem
> $A_k$ is the **best** rank-$k$ approximation to $A$. No other matrix of rank $k$ is closer to $A$ (in the spectral norm or in the sum of squared entries). The error is controlled by the discarded singular values: $\|A-A_k\|_2=\sigma_{k+1}$.

### Why this is compression

An $m\times n$ matrix has $mn$ numbers. $A_k$ needs only $k(m+n+1)$: $k$ vectors $u_i$, $k$ vectors $v_i$, and $k$ numbers $\sigma_i$.

**Worked example 10.3.** A $1000\times1000$ greyscale image has $10^6$ numbers. Keeping $k=50$ singular values needs $50\times2001\approx10^5$: a tenth of the storage. If the singular values decay quickly (as they do for natural images, which are smooth and repetitive), the image looks almost the same.

**Worked example 10.4 (by hand).** For $A$ in example 10.1, the best rank-1 approximation is

$$
A_1=\sigma_1u_1v_1^\top=3\sqrt5\cdot\frac{1}{\sqrt{10}}\begin{bmatrix}1\\3\end{bmatrix}\cdot\frac1{\sqrt2}\begin{bmatrix}1&1\end{bmatrix}=\frac{3\sqrt5}{\sqrt{20}}\begin{bmatrix}1&1\\3&3\end{bmatrix}=1.5\begin{bmatrix}1&1\\3&3\end{bmatrix}=\begin{bmatrix}1.5&1.5\\4.5&4.5\end{bmatrix}.
$$

Compare with $A=\begin{bmatrix}3&0\\4&5\end{bmatrix}$: the rough shape (bottom row larger) is kept, and the error has spectral norm $\sigma_2=\sqrt5$.

---

## 10.6 Principal component analysis (PCA)

### The goal

You have $N$ data points, each with $d$ features: a data matrix $X$ ($N\times d$), one point per row. You want the few directions that capture most of the variation, so you can visualize, compress or denoise the data.

### The method

1. **Centre** the data: subtract the mean of each column, so every feature has mean zero.
2. Compute the SVD: $X=U\Sigma V^\top$.
3. The columns of $V$ are the **principal components**:
   - $v_1$ is the direction along which the data varies **most**,
   - $v_2$ is the direction of greatest remaining variation, perpendicular to $v_1$, and so on.
4. The variance of the data along $v_i$ is $\sigma_i^2/(N-1)$.
5. To reduce to $k$ dimensions, keep the coordinates $XV_k$ (project each point onto the first $k$ components).

### Why the SVD gives this

The covariance matrix of centred data is $C=\dfrac1{N-1}X^\top X$ ([[PS 06 Joint Distributions and Covariance]]). From section 10.3, the eigenvectors of $X^\top X$ are the $v_i$ with eigenvalues $\sigma_i^2$. And from chapter 9, the eigenvectors of a covariance matrix are the axes of its uncertainty ellipse, with variance $\lambda_i$ along each. So PCA is "find the axes of the data's ellipse", and the SVD finds them directly without forming $X^\top X$ (which is numerically better).

**Worked example 10.5.** Five points: $(2,1)$, $(3,3)$, $(4,4)$, $(5,6)$, $(6,6)$. Mean $(4,4)$. Centred:

$$
X=\begin{bmatrix}-2&-3\\-1&-1\\0&0\\1&2\\2&2\end{bmatrix},\qquad X^\top X=\begin{bmatrix}10&13\\13&18\end{bmatrix}.
$$

Eigenvalues: trace 28, det $180-169=11$, so $\lambda=14\pm\sqrt{196-11}=14\pm13.6$: about $27.6$ and $0.40$. The first direction carries $27.6/28\approx98.6\%$ of the variance. Its eigenvector solves $(10-27.6)a+13b=0$, so $b\approx1.35a$: the direction $(1,1.35)$ normalized, about $(0.59,0.80)$.

The data is almost one-dimensional: the points lie close to a line through $(4,4)$ in direction $(0.59,0.80)$.

> [!warning] Two PCA mistakes
> - **Forgetting to centre.** Without centring, the first "component" mostly points at the mean.
> - **Mixing units.** If one feature is in millimetres and another in kilometres, the millimetre feature dominates purely because its numbers are bigger. Standardize features first when units differ.

---

## 10.7 The pseudoinverse

For any matrix, define

$$
A^+=V\Sigma^+U^\top,
$$

where $\Sigma^+$ is $n\times m$ and holds $1/\sigma_i$ for each **nonzero** $\sigma_i$, with zeros elsewhere.

Then $\hat x=A^+b$ is:

| Situation | $A^+b$ gives |
|---|---|
| square, invertible | the exact solution $A^{-1}b$ |
| tall, independent columns | the least squares solution |
| rank deficient | the least squares solution with the **smallest length** |

One formula covers every case of chapter 5.

*Why it works:* $A$ maps $v_i\mapsto\sigma_iu_i$. $A^+$ maps $u_i\mapsto v_i/\sigma_i$, undoing it on the column space, and sends the left null space (unreachable outputs) to zero. Null space directions are never added, which is why the answer is the shortest one.

> [!warning] Tiny singular values
> Dividing by a very small $\sigma_i$ amplifies noise enormously. In practice, singular values below a threshold are treated as zero (truncated SVD), or regularization is added. `np.linalg.pinv` has an `rcond` parameter for this.

---

## Summary

| Idea | Fact |
|---|---|
| SVD | $A=U\Sigma V^\top$ for every matrix |
| one direction | $Av_i=\sigma_iu_i$ |
| picture | rotate, stretch along axes, rotate |
| compute | $v_i$, $\sigma_i^2$ from $A^\top A$; $u_i=Av_i/\sigma_i$ |
| rank | number of nonzero $\sigma_i$ |
| norm, condition | $\sigma_1$; $\sigma_1/\sigma_r$ |
| best rank-$k$ | keep the top $k$ terms |
| PCA | centre, SVD, columns of $V$ |
| pseudoinverse | $V\Sigma^+U^\top$ |

**Three facts to remember:**

1. Every matrix is rotate, stretch, rotate.
2. Singular values rank the directions by importance.
3. Truncating the SVD is the best possible compression.

---

## Exercises

### Part A: warm-up

**A1.** Find the singular values of $\begin{bmatrix}0&2\\-3&0\end{bmatrix}$.

**A2.** A $4\times6$ matrix has singular values $5,2,0,0$. Give its rank and the dimension of its null space.

**A3.** Singular values $10,1,0.01$. What is the condition number? What does the best rank-1 approximation keep?

**A4.** Why are singular values never negative?

> [!success]- Solutions to Part A
> **A1.** $A^\top A=\begin{bmatrix}9&0\\0&4\end{bmatrix}$, so $\sigma=3,2$.
>
> **A2.** Rank 2; null space dimension $6-2=4$.
>
> **A3.** $\kappa=1000$. The rank-1 approximation keeps only the $\sigma=10$ direction.
>
> **A4.** They are square roots of eigenvalues of $A^\top A$, which is positive semidefinite (eigenvalues $\ge0$). Any sign is absorbed into $u_i$ or $v_i$.

### Part B: core

**B1.** Compute the full SVD of $A=\begin{bmatrix}1&1\\1&1\end{bmatrix}$.

**B2.** Compute the SVD of $A=\begin{bmatrix}2&2\\-1&1\end{bmatrix}$ and verify $\sigma_1\sigma_2=|\det A|$.

**B3.** For the data $(1,2)$, $(2,4)$, $(3,6)$, $(4,8)$, find the first principal component and the fraction of variance it explains. Why?

**B4.** Use the pseudoinverse idea to find the shortest solution of $x_1+x_2=2$.

**B5.** Explain why the condition number of an orthogonal matrix is 1, and why that makes orthogonal matrices numerically ideal.

> [!success]- Solutions to Part B
> **B1.** $A^\top A=\begin{bmatrix}2&2\\2&2\end{bmatrix}$, eigenvalues $4,0$. $\sigma_1=2$, $\sigma_2=0$. $v_1=\tfrac1{\sqrt2}(1,1)$, $v_2=\tfrac1{\sqrt2}(1,-1)$. $u_1=Av_1/2=\tfrac1{\sqrt2}(1,1)$, and complete with $u_2=\tfrac1{\sqrt2}(1,-1)$. So $A=2\,u_1v_1^\top$: rank 1.
>
> **B2.** $A^\top A=\begin{bmatrix}5&3\\3&5\end{bmatrix}$, eigenvalues $8,2$. $\sigma=2\sqrt2,\sqrt2$. $v_1=\tfrac1{\sqrt2}(1,1)$: $Av_1=\tfrac1{\sqrt2}(4,0)$, $u_1=(1,0)$. $v_2=\tfrac1{\sqrt2}(1,-1)$: $Av_2=\tfrac1{\sqrt2}(0,-2)$, $u_2=(0,-1)$. $\sigma_1\sigma_2=4=|2+2|$ ✓.
>
> **B3.** All points lie on the line $y=2x$. After centring, every point is a multiple of $(1,2)$, so the first component is $\tfrac1{\sqrt5}(1,2)$ and it explains 100% of the variance. The second singular value is 0.
>
> **B4.** $A=\begin{bmatrix}1&1\end{bmatrix}$, $\sigma_1=\sqrt2$, $v_1=\tfrac1{\sqrt2}(1,1)$, $u_1=1$. $A^+b=v_1\cdot\tfrac1{\sqrt2}\cdot2=(1,1)$. Among all solutions $(t,2-t)$, $(1,1)$ is the shortest.
>
> **B5.** All singular values are 1, so $\kappa=1/1=1$. Errors are never amplified: $\|Qe\|=\|e\|$.

### Part C: explain and prove

**C1.** Prove that $\|Ax\|\le\sigma_1\|x\|$ for all $x$. (Hint: write $x=\sum c_iv_i$ and use orthonormality.)

**C2.** Show that if $A$ is symmetric positive semidefinite, its SVD and its spectral decomposition coincide.

**C3.** Prove that the singular values of $A$ and $A^\top$ are the same.

**C4.** Explain in words why truncating the SVD removes noise in a dataset whose true signal is low-rank.

> [!success]- Solutions to Part C
> **C1.** $Ax=\sum c_i\sigma_iu_i$, so $\|Ax\|^2=\sum c_i^2\sigma_i^2\le\sigma_1^2\sum c_i^2=\sigma_1^2\|x\|^2$, using that the $u_i$ are orthonormal and $\|x\|^2=\sum c_i^2$.
>
> **C2.** $S=Q\Lambda Q^\top$ with all $\lambda_i\ge0$ is already of the form $U\Sigma V^\top$ with $U=V=Q$ and $\Sigma=\Lambda$.
>
> **C3.** $A^\top=V\Sigma^\top U^\top$ is an SVD of $A^\top$ with the same diagonal entries.
>
> **C4.** The signal concentrates in a few large singular values. Random noise spreads its energy thinly over all directions, adding small amounts to every singular value. Keeping only the top few keeps nearly all the signal and discards most of the noise.

### Part D: practise with code

**D1.** `U, s, Vt = np.linalg.svd(A)`. Run it on example 10.1 and compare with the hand computation (signs may differ: explain why that is allowed).

**D2.** Load a greyscale image as a 2-D array (for example `scipy.datasets.face(gray=True)`). Plot its singular values on a log scale, and show reconstructions with $k=5,20,50,100$. How many values do you need before it looks right?

**D3.** Generate 200 points along the line $y=0.5x$ plus small noise in 2-D. Run PCA with `np.linalg.svd` on the centred data and draw the first component on the scatter plot.

**D4.** Compare `np.linalg.pinv(A) @ b` with `np.linalg.lstsq(A, b)` on a tall random matrix. They should agree.

> [!success]- Hints for Part D
> **D1.** Flipping the signs of both $u_i$ and $v_i$ leaves $\sigma_iu_iv_i^\top$ unchanged, so either sign is a valid SVD.
>
> **D2.** The singular values usually fall off steeply; 50 values typically give a recognizable image with a small fraction of the storage.

---

## Where this is used

- **Manipulability.** The singular values of a robot's Jacobian give the **manipulability ellipsoid**: how easily the hand moves in each direction. A singular value near zero means a near-singularity ([[02 Geometry and Kinematics]]).
- **Representation learning.** Learned representations, embeddings and low-rank adaptation (LoRA) of large models rely on useful structure being low rank ([[Appendix - Representation Learning]]).
- **Recommendation systems, denoising, data compression and PCA** throughout data science.

Next: [[LA 11 Change of Basis]]: the same vector, described from different viewpoints.

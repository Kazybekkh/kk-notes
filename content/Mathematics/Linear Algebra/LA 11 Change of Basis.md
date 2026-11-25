---
type: course-chapter
course: linear-algebra
chapter: 11
tags: [mathematics, linear-algebra]
---

# Chapter 11: Change of basis

Previous: [[LA 10 Singular Value Decomposition]] | [[LA 00 Course Map]] | Next: [[LA 12 Matrix Calculus and Numerical Practice]]

> [!abstract] The big idea
> A vector is a geometric object; its coordinates are only a **description** of it, relative to a chosen set of axes. Change the axes and the numbers change, but the object does not. The same is true of linear maps. Choosing good axes (a good **basis**) can turn a hard problem into an easy one. Diagonalization, PCA and every coordinate-frame calculation in robotics are applications of this one idea.

> [!info] In this chapter you will learn to
> 1. Find the coordinates of a vector in any basis, and convert back.
> 2. Rewrite a linear map in a new basis using $B^{-1}AB$.
> 3. Explain diagonalization as "choosing the eigenvector basis".
> 4. Convert points and directions between robot coordinate frames, and chain frames.
> 5. Write matrices for linear maps on spaces of polynomials and functions.

> [!tip] Before you start
> You need bases ([[LA 05 Subspaces Basis and Rank]]), inverses ([[LA 03 Matrices as Linear Maps]]), diagonalization ([[LA 08 Eigenvalues and Eigenvectors]]) and orthonormal bases ([[LA 06 Orthogonality and Least Squares]]).

---

## 11.1 Coordinates depend on the basis

### The same arrow, different numbers

When we write $v=(3,2)$, we secretly mean

$$
v=3e_1+2e_2,
$$

"3 steps along the first standard axis and 2 along the second". The numbers $3,2$ are **coordinates relative to the standard basis**.

Now pick different axes: $b_1=(1,1)$ and $b_2=(1,-1)$. These form a basis of $\mathbb R^2$ (two independent vectors). The same arrow $v$ can be written as

$$
v=c_1b_1+c_2b_2
$$

for some unique numbers $c_1,c_2$. Those are the **coordinates of $v$ in the basis $\{b_1,b_2\}$**, written $[v]_B=(c_1,c_2)$.

### Finding the new coordinates

Put the new basis vectors as columns of a matrix $B$. Then

$$
c_1b_1+c_2b_2=B\begin{bmatrix}c_1\\c_2\end{bmatrix},
$$

so the equation $c_1b_1+c_2b_2=v$ is just $Bc=v$, and

> [!important] Converting coordinates
> $$
> v=B\,[v]_B\qquad\text{(new coordinates to standard)},
> $$
> $$
> [v]_B=B^{-1}v\qquad\text{(standard to new coordinates)}.
> $$

**Worked example 11.1.** $v=(3,2)$, $b_1=(1,1)$, $b_2=(1,-1)$.

Solve $c_1+c_2=3$ and $c_1-c_2=2$: adding gives $2c_1=5$, so $c_1=2.5$, $c_2=0.5$.

So $[v]_B=(2.5,0.5)$. Check: $2.5(1,1)+0.5(1,-1)=(2.5+0.5,\;2.5-0.5)=(3,2)$ ✓.

The arrow is the same. Its description changed from $(3,2)$ to $(2.5,0.5)$.

### A way not to mix up the directions

The two formulas are easy to swap by accident. Test with a basis vector: $b_1$ itself must have new coordinates $(1,0)$. And indeed $B(1,0)=$ first column of $B=b_1$ ✓. So $B$ takes **new** coordinates to **standard** ones.

### Orthonormal bases: no inverse needed

If the new basis is orthonormal, $B$ is an orthogonal matrix and $B^{-1}=B^\top$. Then each new coordinate is a single dot product:

$$
c_i=b_i\cdot v.
$$

**Worked example 11.2.** Orthonormal basis $q_1=(0.6,0.8)$, $q_2=(-0.8,0.6)$, and $v=(1,0)$:

$c_1=q_1\cdot v=0.6$ and $c_2=q_2\cdot v=-0.8$. So $[v]_Q=(0.6,-0.8)$.

> [!question]- Check yourself
> 1. Find the coordinates of $(4,2)$ in the basis $\{(1,1),(1,-1)\}$.
> 2. In the basis $\{(2,0),(0,5)\}$, a vector has coordinates $(3,1)$. What is it in standard coordinates?
> 3. A vector has coordinates $(1,0)$ in some basis. What vector is it?
>
> **Answers.** 1. $c_1+c_2=4$, $c_1-c_2=2$: $(3,1)$. 2. $3(2,0)+1(0,5)=(6,5)$. 3. The first basis vector.

---

## 11.2 The same linear map in a new basis

### The question

A matrix $A$ describes a linear map **in standard coordinates**: feed it standard coordinates, get standard coordinates out. What matrix $A'$ describes **the same map** if we work in $B$-coordinates throughout?

### Follow a vector through

Start with a vector given in $B$-coordinates, $c$. To apply the map:

1. Convert to standard coordinates: $Bc$.
2. Apply the map (which we know in standard coordinates): $ABc$.
3. Convert the result back to $B$-coordinates: $B^{-1}ABc$.

So

> [!important] Change of basis for a map
> $$
> A'=B^{-1}AB.
> $$

Read it right to left: **into** standard coordinates, **apply** $A$, **back out** to $B$-coordinates.

### Similar matrices

Two matrices related by $A'=B^{-1}AB$ (for some invertible $B$) are called **similar**. They are the **same map seen from different viewpoints**. So they share every property that belongs to the map rather than to the description:

| Shared by similar matrices | Why |
|---|---|
| eigenvalues | same stretch factors (chapter 8, exercise C5) |
| determinant | same volume scaling (chapter 7, exercise C2) |
| trace | sum of eigenvalues |
| rank | same number of independent output directions |

What is **not** shared: the individual entries, and the eigenvectors' coordinates (they are re-described in the new basis).

---

## 11.3 Diagonalization is choosing the right basis

Take the basis of **eigenvectors** of $A$, so $B=V$. Then

$$
A'=V^{-1}AV=\Lambda.
$$

In the eigenvector basis, the map is **diagonal**: each coordinate is scaled independently, with no mixing.

That is what diagonalization really means. The matrix $A$ was never complicated; it only looked complicated because we were describing it with axes that did not match its natural directions.

**Worked example 11.3.** $A=\begin{bmatrix}2&1\\1&2\end{bmatrix}$ with the basis $b_1=(1,1)$, $b_2=(1,-1)$ (its eigenvectors, eigenvalues 3 and 1).

$$
B=\begin{bmatrix}1&1\\1&-1\end{bmatrix},\qquad B^{-1}=\frac12\begin{bmatrix}1&1\\1&-1\end{bmatrix}.
$$

$$
AB=\begin{bmatrix}3&1\\3&-1\end{bmatrix},\qquad B^{-1}AB=\frac12\begin{bmatrix}6&0\\0&2\end{bmatrix}=\begin{bmatrix}3&0\\0&1\end{bmatrix}.
$$

In standard coordinates, the map mixes $x$ and $y$. In eigen-coordinates, it is "triple the first coordinate, keep the second".

**Worked example 11.4 (a non-eigen basis, for contrast).** Same $A$, but with basis $b_1=(1,0)$, $b_2=(1,1)$:

$$
B=\begin{bmatrix}1&1\\0&1\end{bmatrix},\quad B^{-1}=\begin{bmatrix}1&-1\\0&1\end{bmatrix},\quad AB=\begin{bmatrix}2&3\\1&3\end{bmatrix},\quad B^{-1}AB=\begin{bmatrix}1&0\\1&3\end{bmatrix}.
$$

Not diagonal, but it is still the same map: trace $4$ ✓, determinant $3$ ✓, eigenvalues $1,3$ ✓.

---

## 11.4 Coordinate frames in robotics

### Frames

A robot uses many coordinate frames: the **world** frame, the robot **base**, each **link**, the **camera**, the **gripper**, the **object**. The same physical point has different coordinates in each.

Writing the frame next to every quantity prevents most bugs. Notation: $p_A$ means "point $p$ described in frame $A$".

### Rotations between frames

A rotation matrix $R_{AB}$ is built so that its **columns are the axes of frame $B$, written in frame $A$**. Then

$$
p_A=R_{AB}\,p_B.
$$

This is exactly $v=B[v]_B$ from section 11.1: frame $B$'s axes play the role of the new basis.

Because rotation matrices are orthogonal, going the other way is free:

$$
R_{BA}=R_{AB}^{-1}=R_{AB}^\top.
$$

### Chaining frames

To go from frame $C$ to frame $A$ via frame $B$:

$$
p_A=R_{AB}\,p_B=R_{AB}R_{BC}\,p_C,\qquad\text{so}\qquad R_{AC}=R_{AB}R_{BC}.
$$

The **inner labels cancel**, like fractions: $\tfrac AB\cdot\tfrac BC=\tfrac AC$. If adjacent labels do not match, the product is a bug.

### Worked example 11.5

A camera is mounted rotated $90^\circ$ counterclockwise relative to the world (in 2-D). The camera sees an object at $p_C=(2,0)$: two units straight ahead along the camera's own $x$-axis. Where is it in the world?

The camera's $x$-axis, written in world coordinates, is $(0,1)$; its $y$-axis is $(-1,0)$. So

$$
R_{WC}=\begin{bmatrix}0&-1\\1&0\end{bmatrix},\qquad p_W=R_{WC}\,p_C=\begin{bmatrix}0\\2\end{bmatrix}.
$$

"Straight ahead of the camera" is "north" in the world, because the camera faces north.

### Adding translation: homogeneous coordinates

Frames are usually **shifted** as well as rotated: $p_A=R_{AB}\,p_B+t_{AB}$, where $t_{AB}$ is the position of $B$'s origin in $A$. Adding a shift is not linear (chapter 3), but a trick makes it linear: append a 1 to every point and use a $4\times4$ (in 3-D) matrix:

$$
\begin{bmatrix}p_A\\1\end{bmatrix}=\underbrace{\begin{bmatrix}R_{AB}&t_{AB}\\0&1\end{bmatrix}}_{T_{AB}}\begin{bmatrix}p_B\\1\end{bmatrix}.
$$

Now chaining frames is again matrix multiplication, $T_{AC}=T_{AB}T_{BC}$. This is the language of [[02 Geometry and Kinematics]].

> [!tip] Points versus directions
> Points get the shift; directions (velocities, surface normals) do not. In homogeneous coordinates, append 1 to a point and 0 to a direction: the 0 automatically removes the shift.

---

## 11.5 Why change basis at all?

| Purpose | Chosen basis | Effect |
|---|---|---|
| decouple a dynamical system | eigenvectors | $x_{k+1}=Ax_k$ becomes $n$ separate scalar equations |
| remove correlation | eigenvectors of the covariance | variables become uncorrelated: PCA |
| compress signals | Fourier or wavelet basis | smooth signals need few coefficients (JPEG, MP3) |
| simplify a task description | gripper or object frame | "move forward 5 cm" is one coordinate |
| numerical stability | orthonormal basis | no amplification of errors |

---

## 11.6 Beyond arrows: polynomials and functions

Vectors do not have to be lists of numbers. Anything you can add and scale, with the usual rules, forms a **vector space**.

### Polynomials as vectors

Polynomials of degree at most 2, such as $3+2t-t^2$, can be added and scaled, and they form a vector space with basis $\{1,t,t^2\}$. The coordinates of $3+2t-t^2$ in this basis are $(3,2,-1)$.

### A linear map: differentiation

Differentiation $D$ is linear: $(f+g)'=f'+g'$ and $(cf)'=cf'$. Find its matrix by the chapter 3 recipe: where does each basis vector go?

- $D(1)=0$, coordinates $(0,0,0)$.
- $D(t)=1$, coordinates $(1,0,0)$.
- $D(t^2)=2t$, coordinates $(0,2,0)$.

Write these as columns:

$$
D=\begin{bmatrix}0&1&0\\0&0&2\\0&0&0\end{bmatrix}.
$$

**Check.** $D\,(3,2,-1)=(2,-2,0)$, which is the polynomial $2-2t$. And indeed $\dfrac d{dt}(3+2t-t^2)=2-2t$ ✓.

Notice: $D$ has a null space (constants differentiate to zero) and is not invertible, matching the fact that you cannot recover the constant term after differentiating. Integration "inverts" it only up to that constant.

> [!important] The general principle
> Once you choose a basis, **every** linear map between finite-dimensional spaces becomes a matrix. That is why linear algebra applies to signals, images, functions and quantum states, not just to arrows.

---

## Summary

| Idea | Formula |
|---|---|
| new to standard | $v=B[v]_B$ |
| standard to new | $[v]_B=B^{-1}v$ |
| orthonormal basis | $c_i=b_i\cdot v$ |
| map in new basis | $A'=B^{-1}AB$ |
| similar matrices | same eigenvalues, det, trace, rank |
| diagonalization | eigenvector basis makes $A'$ diagonal |
| frames | $p_A=R_{AB}p_B$, $R_{AC}=R_{AB}R_{BC}$, $R_{BA}=R_{AB}^\top$ |

**Three facts to remember:**

1. Coordinates describe a vector; they are not the vector.
2. $B^{-1}AB$: into standard, apply, back out.
3. Label every frame; adjacent labels must match before you multiply.

---

## Exercises

### Part A: warm-up

**A1.** Find the coordinates of $(5,1)$ in the basis $\{(1,1),(2,-1)\}$.

**A2.** The orthonormal basis $q_1=\tfrac1{\sqrt2}(1,1)$, $q_2=\tfrac1{\sqrt2}(-1,1)$. Find the coordinates of $(3,1)$ using dot products.

**A3.** If $A'=B^{-1}AB$ and $\det A=6$, $\operatorname{tr}A=5$, what are $\det A'$ and $\operatorname{tr}A'$?

**A4.** Write the matrix of differentiation on polynomials of degree at most 3, in the basis $\{1,t,t^2,t^3\}$.

> [!success]- Solutions to Part A
> **A1.** $c_1+2c_2=5$ and $c_1-c_2=1$. Subtract: $3c_2=4$, $c_2=\tfrac43$, $c_1=\tfrac73$.
>
> **A2.** $c_1=\tfrac4{\sqrt2}=2\sqrt2$, $c_2=\tfrac{-2}{\sqrt2}=-\sqrt2$.
>
> **A3.** $6$ and $5$.
>
> **A4.** $\begin{bmatrix}0&1&0&0\\0&0&2&0\\0&0&0&3\\0&0&0&0\end{bmatrix}$.

### Part B: core

**B1.** Let $A=\begin{bmatrix}4&1\\2&3\end{bmatrix}$. Using its eigenvectors $(1,1)$ and $(1,-2)$ as a basis, compute $B^{-1}AB$ and confirm it is diagonal.

**B2.** A robot base frame $B$ is rotated $30^\circ$ counterclockwise from the world frame $W$ and its origin is at $(2,1)$ in the world. A point is at $(1,0)$ in base coordinates. Find its world coordinates.

**B3.** In the situation of B2, a point is at $(2,1)$ in the world. Where is it in base coordinates?

**B4.** The map "reflect across the line $y=x$" has matrix $\begin{bmatrix}0&1\\1&0\end{bmatrix}$. Write it in the basis $\{(1,1),(1,-1)\}$. Why is the result so simple?

**B5.** Show that the trace of $B^{-1}AB$ equals the trace of $A$, using the fact $\operatorname{tr}(XY)=\operatorname{tr}(YX)$.

> [!success]- Solutions to Part B
> **B1.** $B=\begin{bmatrix}1&1\\1&-2\end{bmatrix}$, $B^{-1}=\tfrac13\begin{bmatrix}2&1\\1&-1\end{bmatrix}$. $AB=\begin{bmatrix}5&2\\5&-4\end{bmatrix}$. $B^{-1}AB=\tfrac13\begin{bmatrix}15&0\\0&6\end{bmatrix}=\begin{bmatrix}5&0\\0&2\end{bmatrix}$ ✓.
>
> **B2.** $R=\begin{bmatrix}\cos30^\circ&-\sin30^\circ\\\sin30^\circ&\cos30^\circ\end{bmatrix}\approx\begin{bmatrix}0.866&-0.5\\0.5&0.866\end{bmatrix}$. $p_W=R(1,0)+(2,1)=(0.866,0.5)+(2,1)=(2.866,1.5)$.
>
> **B3.** $p_B=R^\top(p_W-t)=R^\top(0,0)=(0,0)$. The point is the base's origin.
>
> **B4.** $(1,1)$ is kept and $(1,-1)$ is flipped, so in that basis the matrix is $\begin{bmatrix}1&0\\0&-1\end{bmatrix}$. These are the reflection's eigenvectors.
>
> **B5.** $\operatorname{tr}(B^{-1}(AB))=\operatorname{tr}((AB)B^{-1})=\operatorname{tr}(A)$.

### Part C: explain and prove

**C1.** Prove that if $A'=B^{-1}AB$, then $A'^k=B^{-1}A^kB$. Why is this useful?

**C2.** Explain why the **same** vector $v$ can be an eigenvector of $A$ but have different coordinates in different bases, and how its coordinates in the new basis relate to the eigenvectors of $A'$.

**C3.** Explain why, in robotics code, writing `R_world_cam @ R_gripper_world` is a warning sign.

**C4.** Is "the set of all polynomials of degree exactly 2" a vector space? Why or why not?

> [!success]- Solutions to Part C
> **C1.** $(B^{-1}AB)^k=B^{-1}AB\,B^{-1}AB\cdots=B^{-1}A^kB$, since each inner $BB^{-1}=I$. It means you can compute powers in whichever basis is easiest (such as the eigenbasis, where they are trivial), then convert.
>
> **C2.** If $Av=\lambda v$, then $A'(B^{-1}v)=B^{-1}AB\,B^{-1}v=B^{-1}Av=\lambda B^{-1}v$. So $B^{-1}v$, the coordinates of $v$ in the new basis, is an eigenvector of $A'$. It is the same geometric direction, described differently.
>
> **C3.** Adjacent labels "cam" and "gripper" do not match; the product does not correspond to any meaningful chain of frames.
>
> **C4.** No. It does not contain the zero polynomial, and it is not closed under addition: $t^2+(-t^2+t)=t$ has degree 1.

### Part D: practise with code

**D1.** Write `to_basis(v, B)` using `np.linalg.solve(B, v)` and `from_basis(c, B)` using `B @ c`. Check that they undo each other on random inputs.

**D2.** Build 2-D homogeneous transforms `T(theta, tx, ty)` as $3\times3$ matrices. Compose three of them and check that applying them one at a time gives the same result as applying the product.

**D3.** For a random symmetric matrix $S$, compute `Q.T @ S @ Q` where `Q` comes from `np.linalg.eigh(S)`. Confirm it is diagonal (up to rounding).

> [!success]- Hints for Part D
> **D2.** For angle $\theta$ and shift $(t_x,t_y)$ the rows are `[c, -s, tx]`, `[s, c, ty]` and `[0, 0, 1]`, with `c, s = cos(theta), sin(theta)`. Points are `[x, y, 1]`.

---

## Where this is used

- Every pose computation in [[02 Geometry and Kinematics]] is a change of basis.
- Choosing whether a policy outputs actions in the camera, gripper or base frame changes how well it generalizes ([[12 Human Data and Embodiment]]).
- Fourier analysis, PCA and modal analysis of vibrations are all changes to a well-chosen basis.

Next: [[LA 12 Matrix Calculus and Numerical Practice]]: derivatives with vectors and matrices, and computing safely.

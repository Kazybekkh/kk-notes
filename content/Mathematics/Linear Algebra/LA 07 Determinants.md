---
type: course-chapter
course: linear-algebra
chapter: 7
tags: [mathematics, linear-algebra]
---

# Chapter 7: Determinants

Previous: [[LA 06 Orthogonality and Least Squares]] | [[LA 00 Course Map]] | Next: [[LA 08 Eigenvalues and Eigenvectors]]

> [!abstract] The big idea
> The determinant of a square matrix is **one number that says how much the matrix scales area (or volume)**. Its sign says whether the matrix flips space over like a mirror. It is zero exactly when the matrix flattens space, and so exactly when the matrix has no inverse.

> [!info] In this chapter you will learn to
> 1. Explain what a determinant measures, using pictures.
> 2. Compute determinants of $2\times2$ and $3\times3$ matrices, and of any size by elimination.
> 3. Use the properties of determinants to compute quickly and to reason.
> 4. Use the determinant to test invertibility.
> 5. Recognize where determinants appear: change of variables, cross products, Gaussians.

> [!tip] Before you start
> You need matrices as maps and the $2\times2$ inverse ([[LA 03 Matrices as Linear Maps]]), and elimination ([[LA 04 Solving Linear Systems]]).

---

## 7.1 What a determinant measures

### Start with a picture

Take the **unit square**, with corners $(0,0)$, $(1,0)$, $(1,1)$, $(0,1)$. Its area is 1.

Apply a $2\times2$ matrix $A$. From chapter 3, $e_1$ lands on the first column of $A$ and $e_2$ on the second. Because $A$ keeps lines straight and parallel lines parallel, the square becomes a **parallelogram** with the two columns as its sides.

> [!note] Definition (geometric): determinant
> The **determinant** $\det A$ is the **signed area** of the parallelogram that the unit square becomes. In 3-D, it is the signed volume of the box (parallelepiped) that the unit cube becomes.

Since every region can be cut into tiny squares, and every tiny square is scaled the same way, **$A$ multiplies the area of every region by $|\det A|$.**

### Reading the number

| $\det A$ | What happens to space |
|---|---|
| $3$ | areas tripled |
| $0.5$ | areas halved |
| $1$ | areas kept (but shapes may change, as with a shear) |
| $-1$ | areas kept, and the plane is **flipped** like a mirror image |
| $0$ | everything squashed onto a line or a point: area zero |

### What the sign means

Walk from $e_1$ to $e_2$: that is a counterclockwise turn. After the map, walk from column 1 to column 2. If that is still counterclockwise, orientation is kept and $\det A>0$. If it became clockwise, the map flipped space over and $\det A<0$.

A reflection in a mirror flips orientation (your left hand becomes a right hand). A rotation never does.

### Why zero matters most

> [!important] The invertibility test
> $$
> A\text{ is invertible}\iff\det A\neq0.
> $$

*Why.* If $\det A=0$, the matrix flattens space into something lower-dimensional. Many different points land on the same spot, so no map can send them back: information was lost. If $\det A\neq0$, nothing is flattened and the map can be undone.

This adds another line to the list of equivalent conditions from chapter 4: a square matrix is invertible exactly when its determinant is nonzero, exactly when its columns are independent, exactly when it has full rank.

---

## 7.2 Computing $2\times2$ determinants

$$
\det\begin{bmatrix}a&b\\c&d\end{bmatrix}=ad-bc.
$$

"Down-right diagonal minus up-right diagonal."

**Worked example 7.1.** $\det\begin{bmatrix}3&1\\1&2\end{bmatrix}=6-1=5$. Areas are multiplied by 5.

**Worked example 7.2.** $\det\begin{bmatrix}1&2\\2&4\end{bmatrix}=4-4=0$. The columns $(1,2)$ and $(2,4)$ are parallel; the parallelogram is flat.

**Worked example 7.3.** Rotation by $\theta$: $\det R_\theta=\cos^2\theta+\sin^2\theta=1$. Rotations keep area and orientation.

**Worked example 7.4.** Reflection across the $x$-axis: $\det\begin{bmatrix}1&0\\0&-1\end{bmatrix}=-1$. Area kept, orientation flipped.

### Why $ad-bc$ is the area

Here is an argument using the fact that **shears do not change area** (sliding the top of a parallelogram sideways keeps its base and height).

Start with columns $(a,c)$ and $(b,d)$, and suppose $a\neq0$.

1. Subtract $\tfrac ba$ times column 1 from column 2. This is a shear, so the area is unchanged. Column 2 becomes $\big(0,\;d-\tfrac{bc}a\big)$.
2. Now subtract a multiple of the new column 2 from column 1 to clear its second entry. Another shear. Column 1 becomes $(a,0)$.
3. The shape is now a rectangle with sides $a$ and $d-\tfrac{bc}a$. Its signed area is $a\left(d-\tfrac{bc}a\right)=ad-bc$.

> [!question]- Check yourself
> 1. Compute $\det\begin{bmatrix}5&2\\3&1\end{bmatrix}$. Does the map flip orientation?
> 2. For which $k$ is $\begin{bmatrix}k&4\\1&k\end{bmatrix}$ not invertible?
> 3. What is $\det$ of the shear $\begin{bmatrix}1&7\\0&1\end{bmatrix}$?
>
> **Answers.** 1. $5-6=-1$. Yes, it flips (and keeps area). 2. $k^2-4=0$, so $k=\pm2$. 3. $1$: shears keep area.

---

## 7.3 Computing $3\times3$ determinants

### Cofactor expansion

$$
\det\begin{bmatrix}a&b&c\\d&e&f\\g&h&i\end{bmatrix}
=a\det\begin{bmatrix}e&f\\h&i\end{bmatrix}
-b\det\begin{bmatrix}d&f\\g&i\end{bmatrix}
+c\det\begin{bmatrix}d&e\\g&h\end{bmatrix}.
$$

**How to read it.** Go along the top row. For each entry:

1. cross out its row and column,
2. take the $2\times2$ determinant of what is left (the **minor**),
3. multiply by the entry,
4. attach the sign from the checkerboard pattern:

$$
\begin{bmatrix}+&-&+\\-&+&-\\+&-&+\end{bmatrix}.
$$

Add the three results.

**Worked example 7.5.**

$$
\det\begin{bmatrix}1&2&3\\0&1&4\\5&6&0\end{bmatrix}.
$$

- Entry 1: minor $\det\begin{bmatrix}1&4\\6&0\end{bmatrix}=0-24=-24$. Sign $+$. Contribution $1\times(-24)=-24$.
- Entry 2: minor $\det\begin{bmatrix}0&4\\5&0\end{bmatrix}=0-20=-20$. Sign $-$. Contribution $-2\times(-20)=+40$.
- Entry 3: minor $\det\begin{bmatrix}0&1\\5&6\end{bmatrix}=0-5=-5$. Sign $+$. Contribution $3\times(-5)=-15$.

Total: $-24+40-15=1$.

### Expand along the easiest row or column

You may expand along **any** row or column, as long as you use the checkerboard signs for that row or column. Choose the one with the most zeros, since zero entries contribute nothing.

**Worked example 7.6.**

$$
\det\begin{bmatrix}2&0&1\\3&0&5\\1&4&2\end{bmatrix}.
$$

Column 2 has two zeros. Expand down it: only the entry 4 (row 3, column 2) contributes, with sign $-$:

$$
-4\det\begin{bmatrix}2&1\\3&5\end{bmatrix}=-4(10-3)=-28.
$$

### Triangular matrices

> [!tip] The fastest case
> The determinant of a **triangular** matrix (all zeros above, or all zeros below, the diagonal) is the **product of its diagonal entries**.

$$
\det\begin{bmatrix}2&5&-1\\0&3&7\\0&0&4\end{bmatrix}=2\cdot3\cdot4=24.
$$

*Why:* expand down the first column. Only the top entry is nonzero, leaving a smaller triangular matrix. Repeat.

> [!question]- Check yourself
> 1. Compute $\det\begin{bmatrix}1&0&2\\3&1&0\\0&2&1\end{bmatrix}$ by expanding along the first row.
> 2. Compute $\det\begin{bmatrix}5&0&0\\2&-1&0\\7&3&2\end{bmatrix}$.
>
> **Answers.** 1. $1(1-0)-0+2(6-0)=13$. 2. Lower triangular: $5\cdot(-1)\cdot2=-10$.

---

## 7.4 Properties

These are the rules that make determinants useful. Each one has a geometric reason.

| Property | Formula | Why it makes sense |
|---|---|---|
| identity | $\det I=1$ | doing nothing keeps volume |
| product | $\det(AB)=\det A\cdot\det B$ | scale by one factor, then the other |
| inverse | $\det(A^{-1})=1/\det A$ | undoing a scaling |
| transpose | $\det(A^\top)=\det A$ | rows and columns play equal roles |
| scalar | $\det(cA)=c^n\det A$ for $n\times n$ | each of the $n$ edges is scaled by $c$ |
| row swap | changes the sign | orientation flips |
| row replacement | (add a multiple of one row to another) no change | it is a shear |
| row scaling | multiplying one row by $c$ multiplies $\det$ by $c$ | one edge scaled |
| repeated row | $\det=0$ | the box is flat |

### The product rule in action

**Worked example 7.7.** If $\det A=3$ and $\det B=-2$ (both $3\times3$):

- $\det(AB)=-6$
- $\det(A^{-1})=\tfrac13$
- $\det(A^2B)=3\cdot3\cdot(-2)=-18$
- $\det(2A)=2^3\cdot3=24$ (not $6$)
- $\det(A^\top B^{-1})=3\cdot(-\tfrac12)=-1.5$

> [!warning] No rule for sums
> $\det(A+B)\neq\det A+\det B$ in general. Example: $\det(I+I)=\det(2I)=4$ for $2\times2$, but $\det I+\det I=2$.

### Orthogonal matrices

If $Q^\top Q=I$, then $\det(Q^\top)\det(Q)=1$, so $(\det Q)^2=1$ and $\det Q=\pm1$.

- **Rotations** have $\det=+1$.
- **Reflections** have $\det=-1$.

A rotation matrix computed in robotics code must have determinant exactly $+1$. If you get $-1$, a sign or axis convention is wrong somewhere: you have built a mirror image.

---

## 7.5 Determinants by elimination

Cofactor expansion of an $n\times n$ matrix needs about $n!$ multiplications. For $n=20$ that is about $2.4\times10^{18}$: hopeless. Elimination is far faster.

**Method.**

1. Row reduce to triangular form using only row replacements and swaps.
2. Each **swap** flips the sign. Replacements change nothing.
3. Multiply the diagonal entries (the pivots).

$$
\det A=(-1)^{\text{number of swaps}}\times(\text{product of the pivots}).
$$

**Worked example 7.8.** From chapter 4, elimination on

$$
A=\begin{bmatrix}1&1&1\\2&3&1\\1&2&3\end{bmatrix}
$$

used only replacements and gave pivots $1,1,3$. So $\det A=3$.

**Worked example 7.9.**

$$
\begin{bmatrix}0&2&1\\1&3&2\\2&4&7\end{bmatrix}
\xrightarrow{\text{swap }R_1,R_2}
\begin{bmatrix}1&3&2\\0&2&1\\2&4&7\end{bmatrix}
\xrightarrow{R_3-2R_1}
\begin{bmatrix}1&3&2\\0&2&1\\0&-2&3\end{bmatrix}
\xrightarrow{R_3+R_2}
\begin{bmatrix}1&3&2\\0&2&1\\0&0&4\end{bmatrix}.
$$

One swap; pivots $1,2,4$. So $\det=-(1\cdot2\cdot4)=-8$.

This also shows the invertibility test from another angle: $\det A\neq0$ exactly when all $n$ pivots are nonzero.

---

## 7.6 Where determinants appear

### Change of variables in integrals

When you change variables in a double integral, a tiny rectangle $dx\,dy$ is mapped to a tiny parallelogram. Its area is scaled by the absolute determinant of the **Jacobian** matrix (the matrix of partial derivatives). For polar coordinates $x=r\cos\theta$, $y=r\sin\theta$:

$$
\det\begin{bmatrix}\partial x/\partial r&\partial x/\partial\theta\\\partial y/\partial r&\partial y/\partial\theta\end{bmatrix}
=\det\begin{bmatrix}\cos\theta&-r\sin\theta\\\sin\theta&r\cos\theta\end{bmatrix}=r.
$$

That is why $dx\,dy=r\,dr\,d\theta$. The same factor appears when transforming probability densities ([[PS 05 Continuous Random Variables]]).

### Cross product in 3-D

The cross product $u\times v$ is perpendicular to both, and its length is the area of the parallelogram they span. It can be written as a determinant:

$$
u\times v=\det\begin{bmatrix}e_1&e_2&e_3\\u_1&u_2&u_3\\v_1&v_2&v_3\end{bmatrix}
=(u_2v_3-u_3v_2,\;u_3v_1-u_1v_3,\;u_1v_2-u_2v_1).
$$

The **triple product** $w\cdot(u\times v)=\det[\,w\;u\;v\,]$ is the volume of the box with those three edges. Torque ($\tau=r\times F$) and angular velocity use cross products throughout robotics.

### Gaussians

The density of a multivariate Gaussian has $\sqrt{\det\Sigma}$ in its normalizing constant. $\det\Sigma$ is the squared volume of the uncertainty ellipsoid ([[PS 07 The Multivariate Gaussian]]).

### Robot singularities

For a square Jacobian $J$, $\det J=0$ marks a **singularity**: the arm cannot move its hand in some direction. For a 2-link planar arm, $\det J=l_1l_2\sin q_2$, which is zero when the elbow is straight or fully folded ([[02 Geometry and Kinematics]]).

---

## 7.7 A common trap: "small determinant" is not "nearly singular"

It is tempting to think a tiny determinant means a matrix is almost singular. **It does not.** Take $A=0.1I$ in 100 dimensions:

$$
\det A=0.1^{100}=10^{-100}.
$$

Yet $A$ is perfectly well behaved: its inverse is $10I$, and solving $Ax=b$ is trivial and accurate. The determinant is tiny only because it multiplies a mild shrinking over 100 dimensions.

To measure how close a matrix is to singular, use the **condition number** (chapter 12), which compares the largest and smallest stretching factors.

---

## Summary

| Idea | Fact |
|---|---|
| meaning | signed area/volume scaling factor |
| $2\times2$ | $ad-bc$ |
| $3\times3$ | cofactor expansion with $+-+$ signs |
| triangular | product of the diagonal |
| any size | elimination: $\pm$ product of pivots |
| product | $\det(AB)=\det A\det B$ |
| invertible | $\iff\det A\neq0$ |
| rotation / reflection | $+1$ / $-1$ |

**Three facts to remember:**

1. Determinant = volume scaling factor, with a sign for flipping.
2. $\det A=0\iff$ space is flattened $\iff$ no inverse.
3. Determinants multiply: $\det(AB)=\det A\det B$. They do not add.

---

## Exercises

### Part A: warm-up

**A1.** Compute $\det\begin{bmatrix}4&2\\1&3\end{bmatrix}$. What does the matrix do to the area of a region of area 2?

**A2.** Compute $\det\begin{bmatrix}2&0&1\\1&3&0\\0&1&1\end{bmatrix}$.

**A3.** Compute $\det\begin{bmatrix}1&2&3&4\\0&5&6&7\\0&0&8&9\\0&0&0&-1\end{bmatrix}$.

**A4.** $A$ and $B$ are $3\times3$ with $\det A=4$, $\det B=-\tfrac12$. Find $\det(AB)$, $\det(B^{-1})$, $\det(3A)$, $\det(A^\top A)$.

> [!success]- Solutions to Part A
> **A1.** $12-2=10$. The area becomes 20.
>
> **A2.** First row: $2(3-0)-0+1(1-0)=7$.
>
> **A3.** Upper triangular: $1\cdot5\cdot8\cdot(-1)=-40$.
>
> **A4.** $-2$; $-2$; $27\cdot4=108$; $4\cdot4=16$.

### Part B: core

**B1.** Find all $\lambda$ with $\det\begin{bmatrix}2-\lambda&1\\1&2-\lambda\end{bmatrix}=0$. (You are finding the eigenvalues of chapter 8.)

**B2.** Compute by elimination: $\det\begin{bmatrix}2&4&1\\1&2&3\\3&1&2\end{bmatrix}$.

**B3.** Without computing, explain why $\det\begin{bmatrix}1&2&3\\4&5&6\\5&7&9\end{bmatrix}=0$.

**B4.** Find the area of the triangle with vertices $(1,1)$, $(4,2)$, $(2,5)$. (Hint: use two edge vectors and halve a determinant.)

**B5.** Compute the cross product $(1,2,0)\times(0,1,3)$ and check it is perpendicular to both.

**B6.** For the 2-link arm with $l_1=l_2=1$, $\det J=\sin q_2$. At which elbow angles is the arm singular? At which is the determinant largest?

> [!success]- Solutions to Part B
> **B1.** $(2-\lambda)^2-1=0$, so $2-\lambda=\pm1$, giving $\lambda=1$ or $3$.
>
> **B2.** Swap $R_1,R_2$ (sign flips): $(1,2,3),(2,4,1),(3,1,2)$. $R_2-2R_1=(0,0,-5)$, $R_3-3R_1=(0,-5,-7)$. Swap $R_2,R_3$ (flips again): pivots $1,-5,-5$. Two swaps, so $\det=+1\cdot(-5)\cdot(-5)=25$. Check by cofactors on the original: $2(4-3)-4(2-9)+1(1-6)=2+28-5=25$ ✓.
>
> **B3.** Row 3 equals row 1 plus row 2. The rows are dependent, so the box they span is flat.
>
> **B4.** Edges $(3,1)$ and $(1,4)$. $\det=12-1=11$. Triangle area $=11/2=5.5$.
>
> **B5.** $(2\cdot3-0\cdot1,\;0\cdot0-1\cdot3,\;1\cdot1-2\cdot0)=(6,-3,1)$. Dot products: $6-6+0=0$ and $0-3+3=0$ ✓.
>
> **B6.** Singular at $q_2=0$ (straight) and $q_2=180^\circ$ (folded back). Largest $|\det J|=1$ at $q_2=\pm90^\circ$.

### Part C: explain and prove

**C1.** Use the product rule to prove that if $A$ is invertible, $\det(A^{-1})=1/\det A$.

**C2.** Prove that similar matrices ($B=P^{-1}AP$) have the same determinant.

**C3.** Show that if a square matrix has a row of zeros, its determinant is zero, in two ways: by cofactor expansion, and geometrically.

**C4.** Prove that $\det(cA)=c^n\det A$ for an $n\times n$ matrix, using the row-scaling property.

**C5.** Explain why a $3\times3$ matrix with real entries and $\det<0$ cannot be a rotation.

> [!success]- Solutions to Part C
> **C1.** $\det(A)\det(A^{-1})=\det(AA^{-1})=\det I=1$.
>
> **C2.** $\det(P^{-1}AP)=\det(P^{-1})\det A\det P=\tfrac1{\det P}\det A\det P=\det A$.
>
> **C3.** Expanding along the zero row, every term contains a zero factor. Geometrically, one edge of the box is the zero vector, so the box is flat.
>
> **C4.** $cA$ multiplies each of the $n$ rows by $c$. Each row scaling multiplies the determinant by $c$, giving $c^n$ in total.
>
> **C5.** Rotations are orthogonal with $\det=+1$. A negative determinant means orientation is reversed, which requires a reflection.

### Part D: practise with code

**D1.** Check your answers to A2, B2 and example 7.5 with `np.linalg.det`.

**D2.** Make the matrices `0.1 * np.eye(n)` for `n = 10, 50, 100, 400`. Print `det` and `np.linalg.cond`. What happens to each, and what does that show about using the determinant to detect near-singularity?

**D3.** Draw the unit square and its image under $\begin{bmatrix}2&1\\1&1\end{bmatrix}$. Use the "shoelace" polygon area formula to measure the image's area numerically, and compare with the determinant.

**D4.** For large `n`, time `np.linalg.det` on a random `n x n` matrix for `n = 100, 200, 400, 800`. How does the time grow? Compare with how $n!$ grows.

> [!success]- Hints for Part D
> **D2.** The determinant underflows to $0.0$ for large $n$, but the condition number stays exactly 1: perfectly well conditioned.
>
> **D4.** Time grows roughly like $n^3$ (doubling $n$ multiplies time by about 8), because NumPy uses LU elimination, not cofactors.

---

## Where this is used

- Singularities of robot arms ([[02 Geometry and Kinematics]]).
- Normalizing flows and density transformations, which track $\log|\det J|$ ([[PS 05 Continuous Random Variables]]).
- Uncertainty volume of Gaussians ([[PS 07 The Multivariate Gaussian]]).
- The characteristic equation of the next chapter, $\det(A-\lambda I)=0$.

Next: [[LA 08 Eigenvalues and Eigenvectors]]: the directions a matrix only stretches.

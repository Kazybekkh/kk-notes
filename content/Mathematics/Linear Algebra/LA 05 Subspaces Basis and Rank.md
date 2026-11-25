---
type: course-chapter
course: linear-algebra
chapter: 5
tags: [mathematics, linear-algebra]
---

# Chapter 5: Subspaces, basis and rank

Previous: [[LA 04 Solving Linear Systems]] | [[LA 00 Course Map]] | Next: [[LA 06 Orthogonality and Least Squares]]

> [!abstract] The big idea
> Every matrix has a set of outputs it **can reach** (the column space) and a set of inputs it **destroys** (the null space). One number, the **rank**, tells you the size of both. Together they explain everything about when $Ax=b$ can be solved and how many solutions it has.

> [!info] In this chapter you will learn to
> 1. Decide whether a set of vectors is a subspace.
> 2. Find a basis and the dimension of a subspace.
> 3. Compute the column space, null space and rank of a matrix.
> 4. Use rank-nullity to count dimensions without solving anything.
> 5. Describe all four fundamental subspaces and how they fit together.

> [!tip] Before you start
> You need span and linear independence ([[LA 01 Vectors and Linear Combinations]]) and elimination with free variables ([[LA 04 Solving Linear Systems]]).

---

## 5.1 Subspaces

### Motivation

In chapter 1, spans always came out as lines, planes, or bigger flat pieces **through the origin**. In chapter 4, the solutions of $Ax=0$ had the same kind of shape. We want a name for this kind of set, and a quick test for it.

### The definition

> [!note] Definition: subspace
> A set $V$ of vectors in $\mathbb R^n$ is a **subspace** if
> 1. it contains the zero vector,
> 2. adding any two vectors in $V$ gives a vector in $V$ (**closed under addition**),
> 3. scaling any vector in $V$ gives a vector in $V$ (**closed under scaling**).

In words: **you can never leave $V$ by adding or scaling.** It is a self-contained world for linear combinations.

### What subspaces look like

In $\mathbb R^3$ there are exactly four kinds:

| Dimension | Subspace |
|---|---|
| 0 | just the origin $\{0\}$ |
| 1 | a line through the origin |
| 2 | a plane through the origin |
| 3 | all of $\mathbb R^3$ |

**Not subspaces:**

- **A line that misses the origin**, such as $\{(x,y):y=x+1\}$. It fails rule 1.
- **The first quadrant** $\{(x,y):x\ge0,y\ge0\}$. Scaling $(1,1)$ by $-1$ leaves it. Fails rule 3.
- **Two crossing lines**, such as the $x$-axis together with the $y$-axis. $(1,0)+(0,1)=(1,1)$ is on neither. Fails rule 2.
- **A circle.** Fails all three.

### How to test

To **show** a set is a subspace, check all three rules for arbitrary members. To show it is **not**, give one counterexample.

**Worked example 5.1.** Is $V=\{(x,y,z):x+2y-z=0\}$ a subspace?

1. $(0,0,0)$ satisfies $0+0-0=0$. ✓
2. Take $u,v$ in $V$, so $u_1+2u_2-u_3=0$ and $v_1+2v_2-v_3=0$. Adding the equations: $(u_1+v_1)+2(u_2+v_2)-(u_3+v_3)=0$, so $u+v\in V$. ✓
3. Multiplying $u_1+2u_2-u_3=0$ by $c$ gives $cu_1+2cu_2-cu_3=0$, so $cu\in V$. ✓

Yes, it is a subspace: a plane through the origin.

**Worked example 5.2.** Is $W=\{(x,y,z):x+2y-z=1\}$ a subspace? No: $(0,0,0)$ gives $0\neq1$. It is a plane, but shifted off the origin.

> [!tip] The shortcut
> Any solution set of a **homogeneous** system $Ax=0$ is a subspace. Any span is a subspace. Those two facts cover almost every subspace you will meet.

> [!question]- Check yourself
> 1. Is $\{(x,y):x=0\}$ a subspace of $\mathbb R^2$?
> 2. Is $\{(x,y):xy=0\}$ a subspace?
> 3. Is $\{(x,y,z):x=y=z\}$ a subspace? What does it look like?
>
> **Answers.** 1. Yes, the $y$-axis. 2. No: it is the union of the two axes, and $(1,0)+(0,1)=(1,1)$ fails. 3. Yes, the line through the origin in direction $(1,1,1)$.

---

## 5.2 Basis and dimension

### Basis

> [!note] Definition: basis
> A **basis** of a subspace $V$ is a set of vectors that
> 1. **spans** $V$ (enough vectors to build everything), and
> 2. is **linearly independent** (no wasted vectors).

A basis is a **minimal complete** set of building blocks.

**Uniqueness of coordinates.** If $v_1,\dots,v_k$ is a basis, every vector in $V$ can be written as $c_1v_1+\cdots+c_kv_k$ in **exactly one** way.

*Why exactly one?* Spanning guarantees at least one way. If there were two, $\sum c_iv_i=\sum d_iv_i$, then $\sum(c_i-d_i)v_i=0$, and independence forces every $c_i-d_i=0$. So the two ways are the same.

### Dimension

A subspace has many different bases, but they always contain the **same number** of vectors. That number is the **dimension**.

| Subspace | A basis | Dimension |
|---|---|---|
| $\mathbb R^2$ | $(1,0),(0,1)$ | 2 |
| $\mathbb R^2$ (another basis) | $(1,1),(1,-1)$ | 2 |
| line through $(1,2,3)$ | $(1,2,3)$ | 1 |
| plane $x+2y-z=0$ | $(1,0,1),(0,1,2)$ | 2 |
| $\{0\}$ | none (empty basis) | 0 |

**Why is the number always the same?** The key fact (proved in most textbooks; we state it) is:

> [!important] Counting fact
> In a space of dimension $d$:
> - any set of **more than $d$** vectors is **dependent**,
> - any set of **fewer than $d$** vectors **cannot span**.
>
> So a basis, being both independent and spanning, has exactly $d$ vectors.

A useful consequence: in a space of dimension $d$, **any $d$ independent vectors automatically span**, and any $d$ spanning vectors are automatically independent. You only need to check one condition.

### Finding a basis of a plane

**Worked example 5.3.** Find a basis of $V=\{(x,y,z):x+2y-z=0\}$.

Solve for one variable: $z=x+2y$. The free choices are $x$ and $y$:

$$
\begin{bmatrix}x\\y\\x+2y\end{bmatrix}=x\begin{bmatrix}1\\0\\1\end{bmatrix}+y\begin{bmatrix}0\\1\\2\end{bmatrix}.
$$

So $(1,0,1)$ and $(0,1,2)$ span $V$. They are independent (neither is a multiple of the other). Basis found; dimension 2.

> [!question]- Check yourself
> 1. Is $\{(1,2),(3,4),(5,6)\}$ a basis of $\mathbb R^2$?
> 2. Is $\{(1,0,0),(0,1,0)\}$ a basis of $\mathbb R^3$?
> 3. Find a basis of the line $\{(x,y):3x-y=0\}$.
>
> **Answers.** 1. No: three vectors in a 2-D space are dependent. 2. No: two vectors cannot span 3-D space. 3. $y=3x$, so the basis is $\{(1,3)\}$.

---

## 5.3 The column space: what the matrix can reach

> [!note] Definition: column space
> The **column space** $C(A)$ of an $m\times n$ matrix is the span of its columns. Equivalently, it is the set of all outputs $Ax$. It is a subspace of $\mathbb R^m$ (the **output** space).

> [!important] The solvability rule
> $Ax=b$ has a solution **if and only if** $b$ is in the column space of $A$.

This is just the column view from chapter 3 restated: $Ax$ **is** a combination of the columns, so $b$ must be one.

### Finding a basis for the column space

1. Row reduce $A$ to echelon form.
2. Note which columns contain pivots.
3. The **corresponding columns of the original $A$** form a basis of $C(A)$.

> [!warning] Use the original columns
> Row operations change the column space (they mix the rows, which changes every column). They do **not** change which columns are independent. So elimination tells you **which** columns to take, but you must take them from $A$ itself.

**Worked example 5.4.**

$$
A=\begin{bmatrix}1&2&0&1\\2&4&1&4\\3&6&1&5\end{bmatrix}
\;\longrightarrow\;
\begin{bmatrix}1&2&0&1\\0&0&1&2\\0&0&0&0\end{bmatrix}.
$$

(Steps: $R_2-2R_1$, $R_3-3R_1$, then $R_3-R_2$.)

Pivots are in columns 1 and 3. So a basis of $C(A)$ is

$$
\begin{bmatrix}1\\2\\3\end{bmatrix},\;\begin{bmatrix}0\\1\\1\end{bmatrix}\quad\text{(columns 1 and 3 of the original }A\text{)}.
$$

The column space is a plane in $\mathbb R^3$. The other columns are combinations of these: column 2 is twice column 1, and column 4 is column 1 plus twice column 3.

---

## 5.4 The null space: what the matrix destroys

> [!note] Definition: null space
> The **null space** $N(A)$ is the set of all $x$ with $Ax=0$. It is a subspace of $\mathbb R^n$ (the **input** space).

If $N(A)=\{0\}$, different inputs always give different outputs, so no information is lost. If $N(A)$ is bigger, whole directions of input are flattened to zero and can never be recovered from the output.

### Finding a basis for the null space

1. Row reduce $A$ (the right side stays 0, so you need not write it).
2. Identify the free variables.
3. Set **one** free variable to 1 and the others to 0; solve for the pivot variables. Repeat for each free variable.
4. The vectors you get form a basis of $N(A)$.

**Worked example 5.5.** Continue with $A$ from example 5.4. The echelon form gives

$$
x_1+2x_2+x_4=0,\qquad x_3+2x_4=0.
$$

Free variables: $x_2$ and $x_4$ (no pivots in columns 2 and 4).

- $x_2=1$, $x_4=0$: then $x_3=0$ and $x_1=-2$. Vector $(-2,1,0,0)$.
- $x_2=0$, $x_4=1$: then $x_3=-2$ and $x_1=-1$. Vector $(-1,0,-2,1)$.

$$
N(A)=\operatorname{span}\left\{\begin{bmatrix}-2\\1\\0\\0\end{bmatrix},\begin{bmatrix}-1\\0\\-2\\1\end{bmatrix}\right\}.
$$

Check the first: $A(-2,1,0,0)=-2(\text{col }1)+(\text{col }2)=-2(1,2,3)+(2,4,6)=0$. ✓

Each null space vector is a **recipe for zero** using the columns, which is a **dependency** among the columns. The null space records every way the columns are redundant.

---

## 5.5 Rank and the rank-nullity theorem

> [!note] Definition: rank
> The **rank** of $A$ is the dimension of its column space: the number of independent columns. It equals the **number of pivots** found by elimination.

In example 5.4 the rank is 2.

### Row rank equals column rank

A remarkable fact: the number of independent **rows** always equals the number of independent **columns**. So

$$
\operatorname{rank}(A)=\operatorname{rank}(A^\top),\qquad\operatorname{rank}(A)\le\min(m,n).
$$

*Why (sketch):* elimination does not change the row space, and the nonzero rows of the echelon form are independent, so the number of independent rows is the number of pivots. The number of independent columns is also the number of pivots (section 5.3). Both equal the pivot count.

### Rank-nullity

> [!important] Rank-nullity theorem
> For an $m\times n$ matrix:
> $$
> \underbrace{\operatorname{rank}(A)}_{\dim C(A)}+\underbrace{\dim N(A)}_{\text{nullity}}=n\quad(\text{the number of columns}).
> $$

**Why it is true.** Every column is either a **pivot** column or a **free** column. Pivot columns count the rank. Each free column contributes one basis vector of the null space. Together they account for all $n$ columns.

**Meaning.** Each of the $n$ input dimensions is either **kept** (it contributes to the output) or **destroyed** (it lands in the null space). Nothing else can happen. It is a conservation law for dimensions.

**Check with example 5.4:** rank 2, nullity 2, columns 4. $2+2=4$ ✓.

**Worked example 5.6 (using it without solving).** A $5\times8$ matrix has rank 3. Then:

- the column space is a 3-dimensional subspace of $\mathbb R^5$, so most $b$ in $\mathbb R^5$ are **not** reachable;
- the null space has dimension $8-3=5$, so every solvable system has a 5-parameter family of solutions.

> [!question]- Check yourself
> 1. A $4\times4$ matrix has a 1-dimensional null space. What is its rank? Is it invertible?
> 2. Can a $3\times7$ matrix have rank 4?
> 3. A $6\times4$ matrix has rank 4. What is its null space?
>
> **Answers.** 1. Rank 3. Not invertible (it destroys a direction). 2. No: rank $\le\min(3,7)=3$. 3. Dimension $4-4=0$: only the zero vector.

---

## 5.6 The four fundamental subspaces

Every $m\times n$ matrix $A$ comes with four subspaces:

| Subspace | Lives in | Dimension | Meaning |
|---|---|---|---|
| column space $C(A)$ | $\mathbb R^m$ (outputs) | $r$ | outputs you can reach |
| null space $N(A)$ | $\mathbb R^n$ (inputs) | $n-r$ | inputs sent to zero |
| row space $C(A^\top)$ | $\mathbb R^n$ (inputs) | $r$ | input directions that matter |
| left null space $N(A^\top)$ | $\mathbb R^m$ (outputs) | $m-r$ | output directions never reached |

### How they fit together

> [!important] Orthogonality of the subspaces
> - The **row space** is perpendicular to the **null space**.
> - The **column space** is perpendicular to the **left null space**.

*Why the first.* $Ax=0$ means every row of $A$ has zero dot product with $x$. So $x$ is perpendicular to every row, and therefore (chapter 2, exercise C3) to every combination of rows: the whole row space.

So the **input space** splits into two perpendicular pieces, row space and null space, whose dimensions add to $n$. The **output space** splits into column space and left null space, whose dimensions add to $m$.

### The complete picture of what a matrix does

Take any input $x$. Split it into a row-space part $x_r$ and a null-space part $x_n$. Then

$$
Ax=Ax_r+Ax_n=Ax_r+0=Ax_r.
$$

So:

1. The null-space part is **thrown away**.
2. The row-space part is mapped **one-to-one** onto the column space.
3. The left null space is **never reached**.

Every matrix, of any shape, works this way. Chapter 10 (SVD) gives perfect perpendicular bases for all four pieces.

---

## 5.7 What rank tells you about $Ax=b$

| Shape and rank | Name | Solutions of $Ax=b$ |
|---|---|---|
| $r=m=n$ | square, invertible | exactly one, for every $b$ |
| $r=n<m$ | tall, full column rank | zero or one |
| $r=m<n$ | wide, full row rank | infinitely many, for every $b$ |
| $r<m$ and $r<n$ | rank deficient | zero or infinitely many |

**Why each row holds.**

- $r=m$ means the column space is all of $\mathbb R^m$: **every $b$ is reachable**.
- $r=n$ means the null space is $\{0\}$: **at most one solution**.
- Combine the two conditions as needed.

**Two common real cases.**

- **Tall (more equations than unknowns)**: data fitting. 100 measurements, 3 parameters. Usually no exact solution, which is where chapter 6 (least squares) comes in.
- **Wide (more unknowns than equations)**: a redundant robot arm. A 7-joint arm controlling a 6-D hand pose has a 1-dimensional null space: joint motions that move the elbow without moving the hand.

---

## Summary

| Concept | How to compute | Dimension |
|---|---|---|
| column space | pivot columns of the **original** $A$ | $r$ |
| null space | one vector per free variable | $n-r$ |
| row space | nonzero rows of the echelon form | $r$ |
| rank | number of pivots | $r$ |

**Three facts to remember:**

1. $Ax=b$ is solvable exactly when $b$ is in the column space.
2. Rank + nullity = number of columns.
3. Row space $\perp$ null space: a matrix keeps the row-space part of $x$ and throws away the rest.

---

## Exercises

### Part A: warm-up

**A1.** Which are subspaces of $\mathbb R^3$? (a) $\{(x,y,z):z=0\}$ (b) $\{(x,y,z):z=1\}$ (c) $\{(x,y,z):x\le y\}$ (d) $\{(t,2t,-t):t\in\mathbb R\}$

**A2.** Find a basis and the dimension of $\{(x,y,z):x-y+3z=0\}$.

**A3.** Find the rank of $\begin{bmatrix}1&3\\2&6\\-1&-3\end{bmatrix}$ and a basis of its null space.

**A4.** A $6\times9$ matrix has rank 4. Give the dimensions of all four fundamental subspaces.

> [!success]- Solutions to Part A
> **A1.** (a) yes, the $xy$-plane. (b) no, it misses the origin. (c) no, $(0,1,0)$ is in it but $-1\cdot(0,1,0)$ is not. (d) yes, a line through the origin.
>
> **A2.** $x=y-3z$. Free $y,z$: $(1,1,0)$ and $(-3,0,1)$. Dimension 2.
>
> **A3.** Column 2 is 3 times column 1, so rank 1. Null space: $x_1+3x_2=0$, basis $\{(-3,1)\}$.
>
> **A4.** Column space 4, row space 4, null space $9-4=5$, left null space $6-4=2$.

### Part B: core

**B1.** For
$$
A=\begin{bmatrix}1&2&1&0\\2&4&3&1\\1&2&2&1\end{bmatrix},
$$
find a basis of the column space, a basis of the null space, and the rank. Verify rank-nullity.

**B2.** Is $b=(1,3,2)$ in the column space of the $A$ in B1? Is $b=(1,0,0)$?

**B3.** Find a basis of the row space of the $A$ in B1, and check that each basis vector is perpendicular to each null space basis vector you found.

**B4.** Find a matrix whose null space is spanned by $(1,1,1)$.

**B5.** A 7-joint arm has a $6\times7$ Jacobian $J$ of rank 6. What is the dimension of the set of joint velocities $\dot q$ with $J\dot q=0$? Interpret.

**B6.** Show that $(1,1,0)$, $(1,0,1)$, $(0,1,1)$ form a basis of $\mathbb R^3$, and find the coordinates of $(2,3,5)$ in this basis.

> [!success]- Solutions to Part B
> **B1.** $R_2-2R_1$: $(0,0,1,1)$. $R_3-R_1$: $(0,0,1,1)$. $R_3-R_2$: $0$. Pivots in columns 1 and 3, so rank 2, and a column space basis is $(1,2,1)$, $(1,3,2)$. Equations: $x_1+2x_2+x_3=0$ and $x_3+x_4=0$. Free $x_2,x_4$. $x_2=1,x_4=0$: $(-2,1,0,0)$. $x_2=0,x_4=1$: $x_3=-1$, $x_1=1$: $(1,0,-1,1)$. Rank-nullity: $2+2=4$ ✓.
>
> **B2.** Solve $c_1(1,2,1)+c_2(1,3,2)=b$. For $(1,3,2)$: it is the second basis vector itself, so yes. For $(1,0,0)$: $c_1+c_2=1$, $2c_1+3c_2=0$ give $c_2=-2$, $c_1=3$; third entry $3-4=-1\neq0$. Not in the column space.
>
> **B3.** Nonzero echelon rows: $(1,2,1,0)$ and $(0,0,1,1)$. Dot products with $(-2,1,0,0)$: $-2+2=0$ and $0$. With $(1,0,-1,1)$: $1-1=0$ and $-1+1=0$. All zero ✓.
>
> **B4.** The rows must be perpendicular to $(1,1,1)$, and there must be two independent ones (so rank is 2 and nullity 1). For example $\begin{bmatrix}1&-1&0\\0&1&-1\end{bmatrix}$.
>
> **B5.** $7-6=1$. There is a one-parameter family of joint motions that leave the hand still: the "self-motion" of a redundant arm, often used to move the elbow away from obstacles.
>
> **B6.** Three vectors in $\mathbb R^3$: check independence. $c_1+c_2=0$, $c_1+c_3=0$, $c_2+c_3=0$ forces all zero, so they are a basis. For $(2,3,5)$: $c_1+c_2=2$, $c_1+c_3=3$, $c_2+c_3=5$. Adding all: $2(c_1+c_2+c_3)=10$, so the sum is 5. Then $c_3=3$, $c_2=2$, $c_1=0$.

### Part C: explain and prove

**C1.** Prove that the null space of any matrix is a subspace.

**C2.** Prove that if $A$ is $m\times n$ with $n>m$, then $Ax=0$ has a nonzero solution.

**C3.** Explain why row operations do not change the null space but can change the column space. Give a $2\times2$ example where the column space changes.

**C4.** Prove that if the columns of $A$ are independent, then $A^\top A$ is invertible. (Hint: suppose $A^\top Ax=0$, dot both sides with $x$.)

> [!success]- Solutions to Part C
> **C1.** $A0=0$. If $Ax=0$ and $Ay=0$, then $A(x+y)=0$ and $A(cx)=0$.
>
> **C2.** Rank is at most $m<n$, so the nullity $n-r\ge n-m>0$. The null space contains nonzero vectors.
>
> **C3.** Row operations do not change the solutions of $Ax=0$ (chapter 4), so the null space is unchanged. They do change the columns. Example: $\begin{bmatrix}1&1\\1&1\end{bmatrix}$ has column space spanned by $(1,1)$. Subtracting row 1 from row 2 gives $\begin{bmatrix}1&1\\0&0\end{bmatrix}$, whose column space is spanned by $(1,0)$, a different line.
>
> **C4.** If $A^\top Ax=0$, then $x^\top A^\top Ax=\|Ax\|^2=0$, so $Ax=0$. Independent columns mean $x=0$. So $A^\top A$ (which is square) has trivial null space and is invertible. This fact is the foundation of least squares in chapter 6.

### Part D: practise with code

**D1.** Use `np.linalg.matrix_rank` to check your ranks in A3 and B1.

**D2.** `scipy.linalg.null_space(A)` returns an orthonormal basis of the null space. Compare it with your hand-computed basis for B1. They will look different. Explain why both are correct (hint: check that each SciPy vector is a combination of yours).

**D3.** `sympy.Matrix(A).rref()` returns the reduced row echelon form and the pivot columns. Use it on B1 and on example 5.4.

**D4.** Generate a $5\times3$ matrix `A = np.random.randn(5, 3)`, then make a new matrix whose fourth column is `A[:,0] + 2*A[:,1]`. What is the rank before and after? What is a vector in the null space of the new matrix?

> [!success]- Hints for Part D
> **D2.** A subspace has many bases. SciPy chooses perpendicular unit vectors; you chose vectors with convenient 0s and 1s. Both span the same 2-dimensional subspace.
>
> **D4.** The rank stays 3. The null space contains $(1,2,0,-1)$, the recipe "col 1 + 2 col 2 − col 4 = 0".

---

## Where this is used

- **Robot Jacobians.** A drop in rank is a **singularity**: the hand loses the ability to move in some direction ([[02 Geometry and Kinematics]]). The null space of a redundant arm's Jacobian is used for secondary goals like avoiding joint limits.
- **Data.** If a feature is a combination of others, the data matrix is rank deficient and a regression has no unique answer.
- **Low-rank structure.** Many real datasets are close to low rank, which is what makes compression and PCA work ([[LA 10 Singular Value Decomposition]]).

Next: [[LA 06 Orthogonality and Least Squares]]: what to do when $b$ is **not** in the column space.

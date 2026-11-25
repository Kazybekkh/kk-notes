---
type: course-chapter
course: linear-algebra
chapter: 4
tags: [mathematics, linear-algebra]
---

# Chapter 4: Solving linear systems

Previous: [[LA 03 Matrices as Linear Maps]] | [[LA 00 Course Map]] | Next: [[LA 05 Subspaces Basis and Rank]]

> [!abstract] The big idea
> Solving $Ax=b$ means finding the weights that combine the columns of $A$ into $b$. **Gaussian elimination** finds them by turning the system into a staircase shape you can solve from the bottom up. Every system ends in exactly one of three ways: one solution, none, or infinitely many.

> [!info] In this chapter you will learn to
> 1. Read a system of equations in three ways: rows, columns, and as a matrix map.
> 2. Run Gaussian elimination and back-substitution by hand.
> 3. Recognize from the final staircase whether there is one solution, none, or infinitely many.
> 4. Write the full solution set using free variables.
> 5. Compute inverses by elimination, and record elimination as $A=LU$.

> [!tip] Before you start
> You need the column view of $Ax$ from [[LA 03 Matrices as Linear Maps]], and comfort solving two equations in two unknowns.

---

## 4.1 Three views of the same problem

Take the system

$$
\begin{aligned}x+2y&=5\\3x+4y&=11\end{aligned}
$$

**View 1: rows (equations as lines).** Each equation describes a line in the plane. The solution is the point where the two lines cross. Here they cross at $(1,2)$.

**View 2: columns (finding a recipe).** Rewrite as one vector equation:

$$
x\begin{bmatrix}1\\3\end{bmatrix}+y\begin{bmatrix}2\\4\end{bmatrix}=\begin{bmatrix}5\\11\end{bmatrix}.
$$

Now the question is: what amounts of the two column vectors build $(5,11)$? Answer: 1 of the first and 2 of the second.

**View 3: matrix (running a map backwards).**

$$
\underbrace{\begin{bmatrix}1&2\\3&4\end{bmatrix}}_{A}\underbrace{\begin{bmatrix}x\\y\end{bmatrix}}_{x}=\underbrace{\begin{bmatrix}5\\11\end{bmatrix}}_{b}.
$$

The matrix $A$ sends inputs to outputs. Which input did it send to $b$?

All three views describe one problem. The row view is easy to draw in 2-D. The column view and matrix view are the ones that scale to hundreds of unknowns.

### Vocabulary

| Word | Meaning |
|---|---|
| coefficient matrix | $A$, the numbers multiplying the unknowns |
| right-hand side | $b$ |
| augmented matrix | $[\,A\mid b\,]$: $A$ with $b$ attached as an extra column |
| solution | a vector $x$ that makes every equation true |
| solution set | the set of **all** solutions |
| consistent | has at least one solution |

---

## 4.2 Gaussian elimination

### The idea

The easiest systems are **triangular**:

$$
\begin{aligned}x+y+z&=6\\y-z&=-1\\3z&=9\end{aligned}
$$

Solve the last equation first ($z=3$), substitute upward ($y=2$), then again ($x=1$). This is **back-substitution**.

Elimination is a method for turning **any** system into a triangular one without changing its solutions.

### The three allowed moves

> [!note] Elementary row operations
> 1. **Replace** a row by itself plus a multiple of another row.
> 2. **Swap** two rows.
> 3. **Scale** a row by a nonzero number.
>
> None of these changes the solution set.

*Why they are safe.* Each move can be undone by another move of the same kind (subtract the multiple back; swap again; divide by the same number). So any solution of the new system is a solution of the old one and vice versa. Nothing is gained or lost.

### The procedure

1. Write the augmented matrix $[\,A\mid b\,]$.
2. Take the first column. Use the top entry (the **pivot**) to create zeros **below** it.
3. Move to the next row and the next column. Use its pivot to create zeros below it.
4. Continue until the left part is a staircase (**echelon form**).
5. Back-substitute from the bottom.

### Worked example 4.1 (step by step)

$$
\begin{aligned}
x+y+z&=6\\
2x+3y+z&=11\\
x+2y+3z&=14
\end{aligned}
\qquad\longrightarrow\qquad
\left[\begin{array}{ccc|c}1&1&1&6\\2&3&1&11\\1&2&3&14\end{array}\right]
$$

**Column 1.** The pivot is the 1 in row 1. We need zeros below it.

- Row 2 has a 2 there. Subtract **2 times** row 1: $(2,3,1,11)-2(1,1,1,6)=(0,1,-1,-1)$.
- Row 3 has a 1 there. Subtract **1 times** row 1: $(1,2,3,14)-(1,1,1,6)=(0,1,2,8)$.

$$
\left[\begin{array}{ccc|c}1&1&1&6\\0&1&-1&-1\\0&1&2&8\end{array}\right]
$$

The **multiplier** is always (entry to eliminate) $\div$ (pivot). Here $2\div1=2$ and $1\div1=1$.

**Column 2.** The pivot is now the 1 in row 2. Row 3 has a 1 below it. Subtract 1 times row 2: $(0,1,2,8)-(0,1,-1,-1)=(0,0,3,9)$.

$$
\left[\begin{array}{ccc|c}1&1&1&6\\0&1&-1&-1\\0&0&3&9\end{array}\right]
$$

This is echelon form. The pivots are $1,1,3$.

**Back-substitution.**

- Row 3 says $3z=9$, so $z=3$.
- Row 2 says $y-z=-1$, so $y=-1+3=2$.
- Row 1 says $x+y+z=6$, so $x=6-2-3=1$.

**Check** in all three original equations: $1+2+3=6$ ✓; $2+6+3=11$ ✓; $1+4+9=14$ ✓.

> [!tip] Always check
> Arithmetic slips are the main source of wrong answers. Substituting back into the **original** equations takes a minute and catches nearly all of them.

### When a pivot is zero

If the entry you want to use as a pivot is 0, you cannot divide by it. **Swap** with a lower row that has a nonzero entry in that column.

**Worked example 4.2.**

$$
\left[\begin{array}{cc|c}0&2&4\\3&1&5\end{array}\right]
\xrightarrow{\text{swap rows}}
\left[\begin{array}{cc|c}3&1&5\\0&2&4\end{array}\right]
$$

Already triangular: $2y=4$ gives $y=2$; $3x+2=5$ gives $x=1$.

If there is **no** nonzero entry anywhere below in that column, the column has no pivot. Move on to the next column. That situation leads to free variables (section 4.3).

> [!question]- Check yourself
> 1. Solve by elimination: $x+y=3$, $2x-y=0$.
> 2. What multiplier eliminates the 6 below a pivot of 3?
> 3. Solve $\left[\begin{array}{ccc|c}2&1&-1&3\\0&1&2&5\\0&0&2&4\end{array}\right]$.
>
> **Answers.** 1. Row 2 minus 2 row 1: $-3y=-6$, so $y=2$, $x=1$. 2. $6\div3=2$. 3. $z=2$, $y=5-4=1$, $2x+1-2=3$ so $x=2$.

---

## 4.3 The three possible outcomes

### Outcome 1: no solution

**Worked example 4.3.**

$$
\begin{aligned}x+y&=2\\x+y&=3\end{aligned}
\qquad\longrightarrow\qquad
\left[\begin{array}{cc|c}1&1&2\\0&0&1\end{array}\right]
$$

The last row says $0x+0y=1$, that is $0=1$. Impossible. **No solution.**

- *Row picture:* two parallel lines that never meet.
- *Column picture:* both columns equal $(1,1)$, so every combination has equal entries. The target $(2,3)$ does not, so it cannot be built.

> [!important] Test for no solution
> A row of the form $[\,0\;0\;\cdots\;0\mid c\,]$ with $c\neq0$ means the system is **inconsistent**.

### Outcome 2: infinitely many solutions

**Worked example 4.4.**

$$
\begin{aligned}x+y&=2\\2x+2y&=4\end{aligned}
\qquad\longrightarrow\qquad
\left[\begin{array}{cc|c}1&1&2\\0&0&0\end{array}\right]
$$

The second row says $0=0$: always true, no information. Only one real equation remains, $x+y=2$, with two unknowns.

Column 2 has **no pivot**, so $y$ is a **free variable**: it can be anything. Call it $t$. Then $x=2-t$.

$$
\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}2-t\\t\end{bmatrix}=\begin{bmatrix}2\\0\end{bmatrix}+t\begin{bmatrix}-1\\1\end{bmatrix},\qquad t\in\mathbb R.
$$

Every value of $t$ gives a solution: $t=0$ gives $(2,0)$, $t=1$ gives $(1,1)$, $t=5$ gives $(-3,5)$. Geometrically, the two equations describe the same line, and the whole line is the solution set.

### Outcome 3: exactly one solution

When there is a pivot in **every** column of $A$ and no impossible row, every variable is determined: exactly one solution, as in example 4.1.

### Summary of outcomes

| After elimination | Outcome |
|---|---|
| a row $[\,0\cdots0\mid c\,]$ with $c\neq0$ | **no** solution |
| consistent, and every column of $A$ has a pivot | **exactly one** solution |
| consistent, and some column of $A$ has no pivot | **infinitely many** solutions |

**Pivot variables** are determined by the equations; **free variables** (columns without pivots) can be chosen freely.

### Why never exactly two?

Suppose $x_1$ and $x_2$ are two different solutions: $Ax_1=b$ and $Ax_2=b$. Take any point on the line between them, $x=tx_1+(1-t)x_2$. By linearity,

$$
Ax=tAx_1+(1-t)Ax_2=tb+(1-t)b=b.
$$

So every point on that line is also a solution. Two solutions force infinitely many.

> [!question]- Check yourself
> 1. After elimination you get $\left[\begin{array}{ccc|c}1&2&0&3\\0&0&1&2\\0&0&0&0\end{array}\right]$. Which variables are free? Write the solution.
> 2. After elimination you get $\left[\begin{array}{cc|c}1&4&2\\0&0&-3\end{array}\right]$. Solutions?
>
> **Answers.** 1. Pivots in columns 1 and 3, so $y$ is free. $z=2$, $x=3-2t$, $y=t$: $(3,0,2)+t(-2,1,0)$. 2. None: the last row says $0=-3$.

---

## 4.4 The structure of the solution set

### Homogeneous systems

A system with right-hand side zero, $Ax=0$, is called **homogeneous**. It is always consistent, since $x=0$ works. The question is whether there are **other** solutions.

The set of all solutions of $Ax=0$ is the **null space** of $A$ (the main topic of the next chapter).

### Particular plus homogeneous

> [!important] Structure of solutions
> If $x_p$ is any **one** solution of $Ax=b$, then **every** solution has the form
> $$
> x=x_p+x_h,
> $$
> where $x_h$ is a solution of $Ax=0$.

*Why.*

- *Every $x_p+x_h$ is a solution:* $A(x_p+x_h)=Ax_p+Ax_h=b+0=b$.
- *Every solution has this form:* if $Ax=b$, set $x_h=x-x_p$. Then $Ax_h=b-b=0$.

In example 4.4, $x_p=(2,0)$ and $x_h=t(-1,1)$.

**Picture.** The solutions of $Ax=0$ form a line (or plane, ...) through the origin. The solutions of $Ax=b$ are that same line, **shifted** to pass through $x_p$. Same shape, moved.

**Worked example 4.5 (a 3-unknown system).**

$$
\begin{aligned}x+2y+3z&=6\\2x+4y+7z&=13\end{aligned}
\longrightarrow
\left[\begin{array}{ccc|c}1&2&3&6\\0&0&1&1\end{array}\right]
$$

Pivots in columns 1 and 3; $y$ is free. Set $y=t$. Row 2: $z=1$. Row 1: $x=6-2t-3=3-2t$.

$$
\begin{bmatrix}x\\y\\z\end{bmatrix}=\underbrace{\begin{bmatrix}3\\0\\1\end{bmatrix}}_{x_p}+t\underbrace{\begin{bmatrix}-2\\1\\0\end{bmatrix}}_{x_h}.
$$

Check $t=1$: $(1,1,1)$ gives $1+2+3=6$ ✓ and $2+4+7=13$ ✓.

---

## 4.5 Reduced row echelon form

Echelon form needs back-substitution at the end. If you keep eliminating **upward** as well, and scale each pivot to 1, you reach **reduced row echelon form** (RREF), where the answer can be read off directly.

> [!note] Reduced row echelon form
> 1. Every pivot is 1.
> 2. Each pivot is the only nonzero entry in its column.
> 3. Pivots move right as you go down; zero rows are at the bottom.

**Worked example 4.6.** Continue from the echelon form of example 4.1.

$$
\left[\begin{array}{ccc|c}1&1&1&6\\0&1&-1&-1\\0&0&3&9\end{array}\right]
\xrightarrow{R_3\div3}
\left[\begin{array}{ccc|c}1&1&1&6\\0&1&-1&-1\\0&0&1&3\end{array}\right]
$$

Clear above the third pivot: $R_2+R_3$ and $R_1-R_3$:

$$
\left[\begin{array}{ccc|c}1&1&0&3\\0&1&0&2\\0&0&1&3\end{array}\right]
$$

Clear above the second pivot: $R_1-R_2$:

$$
\left[\begin{array}{ccc|c}1&0&0&1\\0&1&0&2\\0&0&1&3\end{array}\right]
$$

Read off: $x=1$, $y=2$, $z=3$.

This full process is **Gauss-Jordan elimination**. By hand, echelon form plus back-substitution is usually less work. RREF is useful for understanding structure and for computing inverses.

---

## 4.6 Inverses by elimination

To find $A^{-1}$, you want $X$ with $AX=I$. Each column of $X$ solves $Ax=e_j$. Solve all of them at once by eliminating on the wide matrix $[\,A\mid I\,]$:

> [!note] Gauss-Jordan for inverses
> Row reduce $[\,A\mid I\,]$. If the left half becomes $I$, the right half is $A^{-1}$. If the left half develops a zero row, $A$ is not invertible.

**Worked example 4.7.** Invert $A=\begin{bmatrix}2&1\\5&3\end{bmatrix}$.

$$
\left[\begin{array}{cc|cc}2&1&1&0\\5&3&0&1\end{array}\right]
\xrightarrow{R_2-\frac52R_1}
\left[\begin{array}{cc|cc}2&1&1&0\\0&\tfrac12&-\tfrac52&1\end{array}\right]
$$

$$
\xrightarrow{R_2\times2}
\left[\begin{array}{cc|cc}2&1&1&0\\0&1&-5&2\end{array}\right]
\xrightarrow{R_1-R_2}
\left[\begin{array}{cc|cc}2&0&6&-2\\0&1&-5&2\end{array}\right]
\xrightarrow{R_1\div2}
\left[\begin{array}{cc|cc}1&0&3&-1\\0&1&-5&2\end{array}\right]
$$

So $A^{-1}=\begin{bmatrix}3&-1\\-5&2\end{bmatrix}$, matching the $2\times2$ formula from chapter 3.

> [!warning] In code, do not invert to solve
> To solve $Ax=b$ in software, use `np.linalg.solve(A, b)`, never `np.linalg.inv(A) @ b`. Solving directly does about a third of the work and is more accurate. You almost never need the inverse itself.

### Invertibility in one list

For a **square** $n\times n$ matrix, these statements are all equivalent. If one is true, all are:

1. $A$ is invertible.
2. Elimination finds $n$ pivots.
3. $Ax=b$ has exactly one solution for every $b$.
4. $Ax=0$ has only the solution $x=0$.
5. The columns of $A$ are linearly independent.
6. The columns of $A$ span $\mathbb R^n$.
7. $\det A\neq0$ (chapter 7).

This list keeps growing through the course. It is worth rereading after each chapter.

---

## 4.7 LU factorization: elimination as a matrix product

Elimination can be recorded as a factorization

$$
A=LU,
$$

- $U$ is the **upper triangular** matrix you end with.
- $L$ is **lower triangular**, with 1s on the diagonal and the **multipliers** you used in the positions they eliminated.

For example 4.1 the multipliers were 2 (row 2, column 1), 1 (row 3, column 1), and 1 (row 3, column 2):

$$
\underbrace{\begin{bmatrix}1&1&1\\2&3&1\\1&2&3\end{bmatrix}}_{A}=
\underbrace{\begin{bmatrix}1&0&0\\2&1&0\\1&1&1\end{bmatrix}}_{L}
\underbrace{\begin{bmatrix}1&1&1\\0&1&-1\\0&0&3\end{bmatrix}}_{U}.
$$

Multiply it out to check; it works.

**Why bother?** Elimination on an $n\times n$ matrix costs about $\tfrac23n^3$ operations. Once you have $L$ and $U$, solving $Ax=b$ for a **new** $b$ is two triangular solves, about $2n^2$ operations:

1. Solve $Lc=b$ by forward substitution (top to bottom).
2. Solve $Ux=c$ by back-substitution.

If you solve with the same $A$ many times (a simulation step, a control loop), you factor once and reuse.

When row swaps are needed, the factorization becomes $PA=LU$ with a **permutation matrix** $P$ recording the swaps. Software also swaps deliberately to put the **largest** available entry in each pivot position (**partial pivoting**), because dividing by tiny pivots magnifies rounding errors.

---

## Summary

| Step | What you do |
|---|---|
| set up | write $[\,A\mid b\,]$ |
| eliminate | create zeros below each pivot (multiplier = entry ÷ pivot) |
| inspect | $0=c$ row? no solution. Free columns? infinitely many. Else one |
| solve | back-substitute; free variables become parameters |
| write | $x=x_p+t_1h_1+t_2h_2+\cdots$ |
| check | substitute into the **original** equations |

**Three facts to remember:**

1. Row operations never change the solutions.
2. One, none, or infinitely many: never exactly two.
3. All solutions = one particular solution + all solutions of $Ax=0$.

---

## Exercises

### Part A: warm-up

**A1.** Solve $3x+y=7$, $x-2y=0$.

**A2.** Solve by elimination:
$$
\begin{aligned}x+2y-z&=2\\2x+5y+z&=9\\x+3y+3z&=10\end{aligned}
$$

**A3.** Solve $\left[\begin{array}{ccc|c}1&0&2&5\\0&1&-1&1\\0&0&0&0\end{array}\right]$ and describe the solution set geometrically.

**A4.** Decide whether $x+2y=1$, $2x+4y=3$ has solutions.

**A5.** Find the inverse of $\begin{bmatrix}1&2\\3&7\end{bmatrix}$ by Gauss-Jordan.

> [!success]- Solutions to Part A
> **A1.** From the second, $x=2y$. Then $7y=7$, so $y=1$, $x=2$.
>
> **A2.** $R_2-2R_1$: $(0,1,3\mid5)$. $R_3-R_1$: $(0,1,4\mid8)$. Then $R_3-R_2$: $(0,0,1\mid3)$. So $z=3$, $y=5-9=-4$, $x=2+8+3=13$. Check equation 3: $13-12+9=10$ ✓.
>
> **A3.** $z$ is free, $z=t$. $x=5-2t$, $y=1+t$. Solution $(5,1,0)+t(-2,1,1)$: a line in $\mathbb R^3$.
>
> **A4.** $R_2-2R_1$ gives $0=1$. No solution.
>
> **A5.** $[\,1\;2\mid1\;0\,;\;3\;7\mid0\;1\,]\to R_2-3R_1:[\,0\;1\mid-3\;1\,]\to R_1-2R_2:[\,1\;0\mid7\;-2\,]$. Inverse $\begin{bmatrix}7&-2\\-3&1\end{bmatrix}$.

### Part B: core

**B1.** For which values of $k$ does the system $x+ky=2$, $kx+4y=4$ have (a) exactly one solution, (b) no solution, (c) infinitely many?

**B2.** Find all solutions of
$$
\begin{aligned}x_1+x_2+x_3+x_4&=4\\x_1+2x_2+3x_3+4x_4&=10\end{aligned}
$$
in the form $x_p+s\,h_1+t\,h_2$.

**B3.** Find the $LU$ factorization of $A=\begin{bmatrix}2&1\\6&8\end{bmatrix}$ and use it to solve $Ax=(3,18)$.

**B4.** A small factory makes chairs and tables. A chair uses 2 hours of cutting and 1 of finishing; a table uses 3 of cutting and 4 of finishing. This week there are 70 cutting hours and 60 finishing hours, and you want to use them all. How many of each should be made?

**B5.** Find a quadratic $y=a+bt+ct^2$ through the points $(0,1)$, $(1,3)$, $(2,7)$ by setting up and solving a $3\times3$ system.

**B6.** Explain why the system in A2 has exactly one solution for **any** right-hand side, not only $(2,9,10)$.

> [!success]- Solutions to Part B
> **B1.** $R_2-kR_1$ gives $(4-k^2)y=4-2k$. (a) $k\neq\pm2$: one solution. (b) $k=-2$: $0=8$, none. (c) $k=2$: $0=0$, infinitely many.
>
> **B2.** $R_2-R_1$: $x_2+2x_3+3x_4=6$. Free: $x_3=s$, $x_4=t$. Then $x_2=6-2s-3t$ and $x_1=4-x_2-s-t=-2+s+2t$. So $x=(-2,6,0,0)+s(1,-2,1,0)+t(2,-3,0,1)$.
>
> **B3.** Multiplier $6/2=3$. $L=\begin{bmatrix}1&0\\3&1\end{bmatrix}$, $U=\begin{bmatrix}2&1\\0&5\end{bmatrix}$. Forward: $c_1=3$, $3c_1+c_2=18$ so $c_2=9$. Back: $5x_2=9$, $x_2=1.8$; $2x_1+1.8=3$, $x_1=0.6$.
>
> **B4.** $2c+3t=70$ and $c+4t=60$. From the second, $c=60-4t$. Substituting: $120-8t+3t=70$, so $t=10$ and $c=20$. Twenty chairs and ten tables.
>
> **B5.** Equations: $a=1$; $a+b+c=3$; $a+2b+4c=7$. So $b+c=2$ and $2b+4c=6$, giving $c=1$, $b=1$. The quadratic is $y=1+t+t^2$.
>
> **B6.** Elimination found three pivots in a $3\times3$ matrix. The pivots depend only on $A$, not on $b$, so for any $b$ there is no impossible row and no free variable.

### Part C: explain and prove

**C1.** Prove that adding a multiple of one equation to another does not change the solution set. (Show both directions: old solutions solve the new system, and new solutions solve the old.)

**C2.** Prove: if $Ax=0$ has only the zero solution, then $Ax=b$ has **at most** one solution for each $b$.

**C3.** A system has 3 equations and 5 unknowns. Explain why, if it has any solution, it has infinitely many.

**C4.** Explain why the solution set of $Ax=b$ with $b\neq0$ never contains the zero vector, and so is never a "span".

> [!success]- Solutions to Part C
> **C1.** Suppose rows $r_1,r_2$ become $r_1$ and $r_2+cr_1$. If $x$ satisfies $r_1$ and $r_2$, it satisfies $r_2+cr_1$ (add $c$ times one true equation to another). Conversely, if $x$ satisfies $r_1$ and $r_2+cr_1$, subtract $c$ times $r_1$ to get $r_2$. The solution sets are identical.
>
> **C2.** If $Ax_1=b=Ax_2$, then $A(x_1-x_2)=0$, so $x_1-x_2=0$ by assumption.
>
> **C3.** At most 3 pivots (one per row) among 5 columns, so at least 2 columns are free. A consistent system with a free variable has infinitely many solutions.
>
> **C4.** $A\cdot0=0\neq b$, so $0$ is not a solution. Every span contains $0$ (chapter 1), so the solution set is a shifted copy of the null space, not a span itself.

### Part D: practise with code

**D1.** Solve A2 with `np.linalg.solve`. Then check with `A @ x`.

**D2.** Write your own `gaussian_elimination(A, b)` that reduces $[\,A\mid b\,]$ to echelon form with partial pivoting and back-substitutes. Test it on example 4.1 and A2.

**D3.** Use `scipy.linalg.lu(A)` on the matrix of example 4.1. It returns `P, L, U`. Compare with the $L$ and $U$ in section 4.7, and explain any differences.

**D4.** Make the "nearly singular" system $x+y=2$, $x+1.0001y=2.0001$. Solve it, then change the last right-hand side to $2.0002$ and solve again. How much did the answer move? (Chapter 12 explains why.)

> [!success]- Hints for Part D
> **D2.** In each column, find the row with the largest absolute value at or below the diagonal (`np.argmax(abs(...))`), swap it up, then eliminate below.
>
> **D3.** SciPy uses partial pivoting, so it may swap rows to put the largest entry first. Then $L$ and $U$ differ from the hand version, and $P$ records the swaps, but $PLU$ still equals $A$.
>
> **D4.** The first gives $(1,1)$; the second gives $(0,2)$. A change of $0.0001$ in the data moved the solution by $1$. The two equations describe nearly parallel lines, so their crossing point is very sensitive.

---

## Where this is used

- **Inverse kinematics** linearized around a pose: solve $J\,\Delta q=\Delta p$ for the joint change that produces a desired hand motion ([[02 Geometry and Kinematics]]).
- **Calibration and fitting**: every least squares problem ends in a linear system ([[LA 06 Orthogonality and Least Squares]]).
- **Circuits and physics**: Kirchhoff's laws and balance equations are linear systems.

Next: [[LA 05 Subspaces Basis and Rank]], which explains **why** a system has one, none, or infinitely many solutions, using the shape of the column space and null space.

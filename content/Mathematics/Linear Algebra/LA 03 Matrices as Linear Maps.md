---
type: course-chapter
course: linear-algebra
chapter: 3
tags: [mathematics, linear-algebra]
---

# Chapter 3: Matrices as linear maps

Previous: [[LA 02 Dot Product Length and Angle]] | [[LA 00 Course Map]] | Next: [[LA 04 Solving Linear Systems]]

> [!abstract] The big idea
> A matrix is a **machine that transforms vectors**: it takes a vector in and gives a vector out. It keeps lines straight and the origin fixed. Its columns tell you exactly where the basic directions $e_1,e_2,\dots$ end up, and that is all you need to know to describe it.

> [!info] In this chapter you will learn to
> 1. Multiply a matrix by a vector in two ways (column view and row view), and know why both work.
> 2. Explain what "linear" means, and what linear maps can and cannot do to space.
> 3. Build the matrix of a rotation, scaling, shear, reflection or projection from a description.
> 4. Multiply matrices, and explain the rule as "do one map, then the other".
> 5. Compute $2\times2$ inverses and transposes, and know when an inverse exists.

> [!tip] Before you start
> You need linear combinations ([[LA 01 Vectors and Linear Combinations]]) and dot products ([[LA 02 Dot Product Length and Angle]]).

---

## 3.1 What is a matrix?

A **matrix** is a rectangular grid of numbers:

$$
A=\begin{bmatrix}1&2\\3&4\\5&6\end{bmatrix}.
$$

- It has **3 rows** (horizontal) and **2 columns** (vertical), so it is a **$3\times2$ matrix**. Always rows first, then columns.
- The entry in row $i$, column $j$ is written $a_{ij}$. Here $a_{12}=2$ and $a_{31}=5$.
- The set of all $m\times n$ matrices is written $\mathbb R^{m\times n}$.

You can view a matrix as a stack of rows, or as columns placed side by side. **Both views matter**, and switching between them is a core skill:

$$
A=\begin{bmatrix}|&|\\a_1&a_2\\|&|\end{bmatrix}\;\text{(columns)},\qquad
A=\begin{bmatrix}\text{---}\;r_1\;\text{---}\\\text{---}\;r_2\;\text{---}\\\text{---}\;r_3\;\text{---}\end{bmatrix}\;\text{(rows)}.
$$

For the $A$ above: columns $a_1=(1,3,5)$ and $a_2=(2,4,6)$; rows $r_1=(1,2)$, $r_2=(3,4)$, $r_3=(5,6)$.

Adding matrices of the same shape and scaling a matrix work entry by entry, exactly like vectors. The interesting operation is multiplication.

---

## 3.2 Matrix times vector

### The column view (the important one)

> [!note] Definition: matrix-vector product
> If $A$ has columns $a_1,\dots,a_n$ and $x=(x_1,\dots,x_n)$, then
> $$
> Ax=x_1a_1+x_2a_2+\cdots+x_na_n.
> $$
> **$Ax$ is a linear combination of the columns of $A$, using the entries of $x$ as the weights.**

**Worked example 3.1.**

$$
\begin{bmatrix}1&2\\3&4\\5&6\end{bmatrix}\begin{bmatrix}1\\1\end{bmatrix}
=1\begin{bmatrix}1\\3\\5\end{bmatrix}+1\begin{bmatrix}2\\4\\6\end{bmatrix}
=\begin{bmatrix}3\\7\\11\end{bmatrix}.
$$

**Worked example 3.2.**

$$
\begin{bmatrix}2&0\\1&3\end{bmatrix}\begin{bmatrix}4\\-1\end{bmatrix}
=4\begin{bmatrix}2\\1\end{bmatrix}+(-1)\begin{bmatrix}0\\3\end{bmatrix}
=\begin{bmatrix}8\\4\end{bmatrix}+\begin{bmatrix}0\\-3\end{bmatrix}
=\begin{bmatrix}8\\1\end{bmatrix}.
$$

Why is this view so important? Because it connects matrices back to chapter 1. **Asking "is there an $x$ with $Ax=b$?" is asking "is $b$ a linear combination of the columns of $A$?"** That single sentence organizes chapters 4 to 6.

### The row view (how you compute by hand)

Each entry of $Ax$ is the **dot product of one row of $A$ with $x$**:

$$
Ax=\begin{bmatrix}r_1\cdot x\\r_2\cdot x\\\vdots\\r_m\cdot x\end{bmatrix}.
$$

**Worked example 3.1 again, by rows.** $r_1\cdot x=1+2=3$, $r_2\cdot x=3+4=7$, $r_3\cdot x=5+6=11$. Same answer.

### Why the two views agree

Write out entry $i$ of the column view: it is $x_1a_{i1}+x_2a_{i2}+\cdots+x_na_{in}$. That is exactly row $i$ dotted with $x$. They are the same sum, collected two ways: by columns, or by rows.

### Shapes must fit

An $m\times n$ matrix needs a vector with $n$ entries (one weight per column) and returns a vector with $m$ entries (one per row):

$$
\underbrace{A}_{m\times n}\;\underbrace{x}_{n}\;=\;\underbrace{Ax}_{m}.
$$

So $A$ is a function from $\mathbb R^n$ to $\mathbb R^m$. The $3\times2$ matrix above takes 2-D vectors and returns 3-D vectors.

> [!question]- Check yourself
> 1. Compute $\begin{bmatrix}1&-1\\2&0\end{bmatrix}\begin{bmatrix}3\\5\end{bmatrix}$ both ways.
> 2. A matrix is $4\times7$. What size vector does it take, and what size does it return?
> 3. Without multiplying, what is $A\begin{bmatrix}0\\1\end{bmatrix}$ for any $m\times2$ matrix $A$?
>
> **Answers.** 1. Column view: $3(1,2)+5(-1,0)=(-2,6)$. Row view: $3-5=-2$ and $6+0=6$. 2. Takes $\mathbb R^7$, returns $\mathbb R^4$. 3. The second column of $A$.

---

## 3.3 What "linear" means

### The definition

> [!note] Definition: linear map
> A function $T$ from vectors to vectors is **linear** if, for all vectors $u,v$ and scalars $c$:
> 1. $T(u+v)=T(u)+T(v)$ (it respects addition),
> 2. $T(cu)=c\,T(u)$ (it respects scaling).

In words: you can add or scale **before** applying $T$, or **after**, and you get the same thing. $T$ "passes through" linear combinations:

$$
T(c_1v_1+c_2v_2)=c_1T(v_1)+c_2T(v_2).
$$

**Every matrix is linear.** $A(u+v)=Au+Av$ and $A(cu)=c\,Au$, because the column view is built from additions and scalings.

**Every linear map is a matrix** (between $\mathbb R^n$ and $\mathbb R^m$). Section 3.4 shows how to find it.

### What linear maps do to space

Because of the two rules, a linear map:

- **keeps the origin fixed**: $T(0)=T(0\cdot v)=0\cdot T(v)=0$.
- **keeps straight lines straight**: the line $p+tv$ maps to $T(p)+tT(v)$, another line (or a single point).
- **keeps evenly spaced points evenly spaced**: a square grid becomes a grid of parallelograms.

It **can** rotate, stretch, squash, shear, reflect, and flatten.
It **cannot** bend lines, or move the origin.

**Not linear:**

- $T(x)=x+1$ (a shift): $T(0)=1\neq0$.
- $T(x)=x^2$: $T(2\cdot1)=4$ but $2T(1)=2$.
- $T(x,y)=(xy,y)$: multiplies entries together.

> [!warning] "Linear" here is stricter than in school
> The school function $y=2x+1$ is called linear because its graph is a line, but in linear algebra it is **not** linear: it moves the origin. Such "linear plus a shift" maps are called **affine**. Robotics handles shifts with a trick (homogeneous coordinates) described in [[02 Geometry and Kinematics]].

> [!question]- Check yourself
> 1. Is $T(x,y)=(3x,\;x-y)$ linear?
> 2. Is $T(x,y)=(x,\;y+2)$ linear?
> 3. If $T$ is linear with $T(e_1)=(1,4)$ and $T(e_2)=(2,-1)$, find $T(3,2)$.
>
> **Answers.** 1. Yes (it is the matrix $\begin{bmatrix}3&0\\1&-1\end{bmatrix}$). 2. No: $T(0,0)=(0,2)$. 3. $T(3e_1+2e_2)=3(1,4)+2(2,-1)=(7,10)$.

---

## 3.4 The columns are where the basis vectors land

### The key fact

Multiply any matrix by $e_1=(1,0,\dots,0)$. In the column view the weights are "1 of column 1, none of the others", so

$$
Ae_1=\text{column 1 of }A,\qquad Ae_2=\text{column 2 of }A,\qquad\dots
$$

> [!important] The recipe for building a matrix
> **Column $j$ of $A$ is where $A$ sends $e_j$.**
> To find the matrix of a linear map: ask where each basic direction $e_1,e_2,\dots$ goes, and write the answers as columns.

Why is that enough information? Every vector is a combination of the $e_j$, and a linear map passes through combinations (section 3.3). So once you know where the $e_j$ go, you know where everything goes.

### A gallery of 2-D maps

For each one, track $e_1=(1,0)$ (east) and $e_2=(0,1)$ (north).

**Scaling.** Stretch east-west by 2 and north-south by 3. $e_1\mapsto(2,0)$, $e_2\mapsto(0,3)$:

$$
S=\begin{bmatrix}2&0\\0&3\end{bmatrix}.
$$

A **diagonal** matrix scales each axis independently.

**Rotation by $90^\circ$ counterclockwise.** East turns to north: $e_1\mapsto(0,1)$. North turns to west: $e_2\mapsto(-1,0)$.

$$
R_{90}=\begin{bmatrix}0&-1\\1&0\end{bmatrix}.
$$

Check on $(2,1)$: $R_{90}(2,1)=(-1,2)$. Draw both arrows; the second is the first turned a quarter-turn left.

**Rotation by any angle $\theta$.** On the unit circle, $e_1$ rotated by $\theta$ lands at $(\cos\theta,\sin\theta)$. $e_2$ starts at $90^\circ$ and lands at angle $90^\circ+\theta$, which is $(-\sin\theta,\cos\theta)$:

$$
R_\theta=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}.
$$

Plug in $\theta=90^\circ$ and you recover $R_{90}$.

**Reflection across the $x$-axis.** $e_1$ stays, $e_2$ flips: $\begin{bmatrix}1&0\\0&-1\end{bmatrix}$.

**Reflection across the line $y=x$.** $e_1$ and $e_2$ swap: $\begin{bmatrix}0&1\\1&0\end{bmatrix}$.

**Shear.** $e_1$ stays, $e_2$ leans over to $(1,1)$:

$$
H=\begin{bmatrix}1&1\\0&1\end{bmatrix}.
$$

Points slide sideways by an amount equal to their height, like pushing the top of a deck of cards.

**Projection onto the $x$-axis.** $e_1$ stays, $e_2$ is flattened to $(0,0)$:

$$
P=\begin{bmatrix}1&0\\0&0\end{bmatrix}.
$$

This one **destroys information**: every point on a vertical line lands on the same spot. You can never recover the original height. Keep this example in mind; chapter 5 is about measuring exactly this kind of loss.

| Map | Matrix | Keeps lengths? | Can be undone? |
|---|---|---|---|
| scale by (2,3) | $\begin{bmatrix}2&0\\0&3\end{bmatrix}$ | no | yes |
| rotation | $R_\theta$ | yes | yes |
| reflection | e.g. $\begin{bmatrix}1&0\\0&-1\end{bmatrix}$ | yes | yes |
| shear | $\begin{bmatrix}1&1\\0&1\end{bmatrix}$ | no | yes |
| projection | $\begin{bmatrix}1&0\\0&0\end{bmatrix}$ | no | **no** |

> [!question]- Check yourself
> 1. Write the matrix for rotation by $180^\circ$.
> 2. Write the matrix that doubles every vector.
> 3. A map sends $e_1\mapsto(1,2,0)$ and $e_2\mapsto(0,1,1)$. What is its matrix, and what are its input and output spaces?
>
> **Answers.** 1. $\begin{bmatrix}-1&0\\0&-1\end{bmatrix}$. 2. $\begin{bmatrix}2&0\\0&2\end{bmatrix}=2I$. 3. $\begin{bmatrix}1&0\\2&1\\0&1\end{bmatrix}$, from $\mathbb R^2$ to $\mathbb R^3$.

---

## 3.5 Matrix multiplication is composition

### Doing one map after another

Suppose you first apply $B$, then $A$. A vector $x$ becomes $Bx$, then $A(Bx)$. The combined map is also linear, so it has a matrix. We **define** the product $AB$ to be that matrix:

$$
(AB)x=A(Bx).
$$

That is the whole reason matrix multiplication looks the way it does. It is not an arbitrary rule; it is "composition of maps" written out.

### How to compute it

Apply the recipe from section 3.4: column $j$ of $AB$ is where $AB$ sends $e_j$:

$$
(AB)e_j=A(Be_j)=A\,(\text{column }j\text{ of }B).
$$

> [!note] Rule: matrix product
> **Column view:** column $j$ of $AB$ is $A$ times column $j$ of $B$.
> **Entry view:** $(AB)_{ij}=(\text{row }i\text{ of }A)\cdot(\text{column }j\text{ of }B)$.

**Worked example 3.3.**

$$
A=\begin{bmatrix}1&2\\3&4\end{bmatrix},\qquad B=\begin{bmatrix}0&1\\1&0\end{bmatrix}.
$$

Column 1 of $B$ is $(0,1)$, and $A(0,1)=(2,4)$. Column 2 of $B$ is $(1,0)$, and $A(1,0)=(1,3)$. So

$$
AB=\begin{bmatrix}2&1\\4&3\end{bmatrix}.
$$

Check one entry by the entry view: $(AB)_{21}=(3,4)\cdot(0,1)=4$. ✓

**Worked example 3.4 (non-square).**

$$
\begin{bmatrix}1&0&2\\0&1&1\end{bmatrix}\begin{bmatrix}1&2\\0&1\\3&0\end{bmatrix}
=\begin{bmatrix}1+0+6&2+0+0\\0+0+3&0+1+0\end{bmatrix}
=\begin{bmatrix}7&2\\3&1\end{bmatrix}.
$$

### Shapes

$$
\underbrace{A}_{m\times n}\;\underbrace{B}_{n\times p}=\underbrace{AB}_{m\times p}.
$$

The **inner** sizes must match (the output of $B$ must fit the input of $A$). The result takes the **outer** sizes. A $2\times3$ times a $3\times2$ gives $2\times2$, as in example 3.4.

### Order matters

$AB$ means **$B$ first, then $A$**. Read right to left, the same way as function notation $f(g(x))$.

In general $AB\neq BA$. Using example 3.3:

$$
BA=\begin{bmatrix}0&1\\1&0\end{bmatrix}\begin{bmatrix}1&2\\3&4\end{bmatrix}=\begin{bmatrix}3&4\\1&2\end{bmatrix}\neq AB.
$$

$B$ swaps the two coordinates. Applied **after** $A$ ($BA$) it swaps the rows of $A$; applied **before** ($AB$) it swaps the columns.

**Geometric example.** Rotate $90^\circ$ then reflect across the $x$-axis, versus reflect then rotate. Track $e_1$: rotate first sends it to $(0,1)$, then reflection gives $(0,-1)$. Reflect first leaves $e_1$ alone, then rotation gives $(0,1)$. Different results.

### Rules that do hold

| Rule | Formula |
|---|---|
| associative | $(AB)C=A(BC)$ |
| distributive | $A(B+C)=AB+AC$ |
| identity | $AI=IA=A$ |
| transpose of product | $(AB)^\top=B^\top A^\top$ (order reverses) |

Associativity is why long chains like $ABCx$ need no brackets: it is just "apply $C$, then $B$, then $A$".

> [!question]- Check yourself
> 1. Compute $\begin{bmatrix}1&1\\0&1\end{bmatrix}\begin{bmatrix}1&0\\2&1\end{bmatrix}$.
> 2. $A$ is $3\times5$ and $B$ is $5\times2$. Is $AB$ defined? $BA$?
> 3. Compute $R_{90}R_{90}$. What single map is it?
>
> **Answers.** 1. $\begin{bmatrix}3&1\\2&1\end{bmatrix}$. 2. $AB$ yes, $3\times2$. $BA$ no: $2\neq3$. 3. $\begin{bmatrix}-1&0\\0&-1\end{bmatrix}$, rotation by $180^\circ$.

---

## 3.6 The identity and the inverse

### Identity

The **identity matrix** $I$ has ones on the diagonal and zeros elsewhere:

$$
I=\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}.
$$

It sends every $e_j$ to itself, so it does nothing: $Ix=x$. It plays the role of the number 1.

### Inverse

> [!note] Definition: inverse
> A square matrix $A$ is **invertible** if there is a matrix $A^{-1}$ with
> $$
> A^{-1}A=I\quad\text{and}\quad AA^{-1}=I.
> $$
> $A^{-1}$ **undoes** $A$.

**Examples you can see.**

- Rotation by $\theta$ is undone by rotation by $-\theta$.
- Scaling by $(2,3)$ is undone by scaling by $(1/2,1/3)$.
- Shear $\begin{bmatrix}1&1\\0&1\end{bmatrix}$ is undone by $\begin{bmatrix}1&-1\\0&1\end{bmatrix}$ (slide back).
- The projection $P$ **has no inverse**: it sent many points to the same place, so no map can know which one to send each back to.

### The $2\times2$ formula

$$
\begin{bmatrix}a&b\\c&d\end{bmatrix}^{-1}=\frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix},\qquad\text{valid when }ad-bc\neq0.
$$

To remember it: **swap** the diagonal entries, **negate** the off-diagonal entries, **divide** by $ad-bc$.

**Worked example 3.5.** Invert $A=\begin{bmatrix}2&1\\5&3\end{bmatrix}$. Here $ad-bc=6-5=1$, so

$$
A^{-1}=\begin{bmatrix}3&-1\\-5&2\end{bmatrix}.
$$

Check: $AA^{-1}=\begin{bmatrix}6-5&-2+2\\15-15&-5+6\end{bmatrix}=I$. ✓

**Worked example 3.6.** $\begin{bmatrix}1&2\\2&4\end{bmatrix}$ has $ad-bc=4-4=0$: no inverse. Its columns are parallel, so it flattens the plane onto a line, just like a projection.

The number $ad-bc$ is the **determinant**, and chapter 7 ([[LA 07 Determinants]]) explains that it measures how the map scales area. Zero area means flattening, which means no inverse.

### Inverse of a product

$$
(AB)^{-1}=B^{-1}A^{-1}.
$$

Undo the **last** step **first**. You put on socks, then shoes; to undo, you take off shoes, then socks.

*Check:* $(AB)(B^{-1}A^{-1})=A(BB^{-1})A^{-1}=AIA^{-1}=AA^{-1}=I$.

> [!question]- Check yourself
> 1. Invert $\begin{bmatrix}4&7\\2&6\end{bmatrix}$.
> 2. Does $\begin{bmatrix}3&6\\1&2\end{bmatrix}$ have an inverse?
> 3. What is the inverse of $R_\theta$?
>
> **Answers.** 1. $ad-bc=10$; $\dfrac1{10}\begin{bmatrix}6&-7\\-2&4\end{bmatrix}$. 2. No: $6-6=0$. 3. $R_{-\theta}=\begin{bmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{bmatrix}$.

---

## 3.7 The transpose

> [!note] Definition: transpose
> The **transpose** $A^\top$ turns rows into columns: $(A^\top)_{ij}=a_{ji}$.
> $$
> \begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}^\top=\begin{bmatrix}1&4\\2&5\\3&6\end{bmatrix}.
> $$

An $m\times n$ matrix becomes $n\times m$.

**The dot product is a matrix product.** A column vector $x$ is an $n\times1$ matrix, so $x^\top$ is $1\times n$ (a row). Then

$$
x^\top y=\begin{bmatrix}x_1&\cdots&x_n\end{bmatrix}\begin{bmatrix}y_1\\\vdots\\y_n\end{bmatrix}=x_1y_1+\cdots+x_ny_n=x\cdot y.
$$

That is why the dot product is often written $x^\top y$.

**Symmetric matrices.** If $A^\top=A$, the matrix is **symmetric**: mirror-image across its diagonal, such as $\begin{bmatrix}2&1\\1&3\end{bmatrix}$. Covariance matrices and many others are symmetric, and they get their own chapter ([[LA 09 Symmetric and Positive Definite Matrices]]).

**A useful identity.** $(Ax)\cdot y=x\cdot(A^\top y)$. Moving a matrix across a dot product turns it into its transpose. This appears in backpropagation, where gradients flow backwards through $W^\top$ ([[LA 12 Matrix Calculus and Numerical Practice]]).

---

## Summary

| Idea | Key fact |
|---|---|
| $Ax$ | combination of the columns of $A$, weights from $x$ |
| shapes | $m\times n$ takes $\mathbb R^n$ to $\mathbb R^m$ |
| linear | respects addition and scaling; origin fixed, lines straight |
| building a matrix | column $j$ = image of $e_j$ |
| $AB$ | do $B$, then $A$; order matters |
| inverse | undoes $A$; exists only if nothing is flattened |
| $2\times2$ inverse | swap, negate, divide by $ad-bc$ |
| transpose | rows become columns; $x\cdot y=x^\top y$ |

**Three facts to remember:**

1. $Ax$ is a combination of columns. "Solve $Ax=b$" means "build $b$ from the columns".
2. To find a matrix, ask where $e_1,e_2,\dots$ go.
3. $AB$ is $B$ then $A$, and $(AB)^{-1}=B^{-1}A^{-1}$.

---

## Exercises

### Part A: warm-up

**A1.** Compute $\begin{bmatrix}2&-1&0\\1&3&2\end{bmatrix}\begin{bmatrix}1\\2\\-1\end{bmatrix}$ using both the column view and the row view.

**A2.** Compute $\begin{bmatrix}1&2\\0&1\end{bmatrix}\begin{bmatrix}3&0\\1&2\end{bmatrix}$ and the product in the other order.

**A3.** Find the inverse of $\begin{bmatrix}3&2\\4&3\end{bmatrix}$ and check it.

**A4.** Write the transpose of $\begin{bmatrix}1&0&4\\2&5&-1\end{bmatrix}$.

**A5.** Write the matrix of rotation by $45^\circ$ (use $\cos45^\circ=\sin45^\circ=\tfrac{\sqrt2}2$) and apply it to $(1,0)$.

> [!success]- Solutions to Part A
> **A1.** Column view: $1(2,1)+2(-1,3)+(-1)(0,2)=(2,1)+(-2,6)+(0,-2)=(0,5)$. Row view: $2-2+0=0$ and $1+6-2=5$.
>
> **A2.** $\begin{bmatrix}5&4\\1&2\end{bmatrix}$. Other order: $\begin{bmatrix}3&6\\1&4\end{bmatrix}$. Different.
>
> **A3.** $ad-bc=1$. Inverse $\begin{bmatrix}3&-2\\-4&3\end{bmatrix}$. Product: $\begin{bmatrix}9-8&-6+6\\12-12&-8+9\end{bmatrix}=I$.
>
> **A4.** $\begin{bmatrix}1&2\\0&5\\4&-1\end{bmatrix}$.
>
> **A5.** $\dfrac{\sqrt2}2\begin{bmatrix}1&-1\\1&1\end{bmatrix}$. Applied to $(1,0)$: $(\tfrac{\sqrt2}2,\tfrac{\sqrt2}2)\approx(0.707,0.707)$, which is $(1,0)$ turned $45^\circ$.

### Part B: core

**B1.** Find the matrix of the linear map that reflects across the line $y=-x$.

**B2.** A linear map has $T(1,1)=(3,1)$ and $T(1,-1)=(1,5)$. Find $T(e_1)$, $T(e_2)$, and the matrix of $T$. (Hint: write $e_1$ and $e_2$ as combinations of $(1,1)$ and $(1,-1)$.)

**B3.** Show that $R_\alpha R_\beta=R_{\alpha+\beta}$ by multiplying the matrices. Which trigonometric identities appear?

**B4.** Find a $2\times2$ matrix $A$, not the zero matrix, with $A^2=0$. What does it do geometrically?

**B5.** For $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$, compute $A^\top A$ and $AA^\top$. Are they equal? Are they symmetric?

**B6.** Robot frames: a planar robot's base is rotated $30^\circ$ relative to the world, and its arm is rotated a further $60^\circ$ relative to the base. Using B3, what single rotation takes arm coordinates to world coordinates? Write its matrix.

> [!success]- Solutions to Part B
> **B1.** $e_1=(1,0)\mapsto(0,-1)$ and $e_2=(0,1)\mapsto(-1,0)$. Matrix $\begin{bmatrix}0&-1\\-1&0\end{bmatrix}$.
>
> **B2.** $e_1=\tfrac12(1,1)+\tfrac12(1,-1)$, so $T(e_1)=\tfrac12(3,1)+\tfrac12(1,5)=(2,3)$. $e_2=\tfrac12(1,1)-\tfrac12(1,-1)$, so $T(e_2)=\tfrac12(3,1)-\tfrac12(1,5)=(1,-2)$. Matrix $\begin{bmatrix}2&1\\3&-2\end{bmatrix}$. Check: $T(1,1)=(3,1)$ ✓.
>
> **B3.** The top-left entry of the product is $\cos\alpha\cos\beta-\sin\alpha\sin\beta=\cos(\alpha+\beta)$, and the bottom-left is $\sin\alpha\cos\beta+\cos\alpha\sin\beta=\sin(\alpha+\beta)$. These are the angle-addition formulas. Rotating twice adds the angles, as you would expect.
>
> **B4.** $A=\begin{bmatrix}0&1\\0&0\end{bmatrix}$. It sends $e_1\mapsto0$ and $e_2\mapsto e_1$. Applying it twice sends everything to $0$: the first application lands in the $x$-axis, and the second kills the $x$-axis.
>
> **B5.** $A^\top A=\begin{bmatrix}10&14\\14&20\end{bmatrix}$ and $AA^\top=\begin{bmatrix}5&11\\11&25\end{bmatrix}$. Not equal, but both symmetric. (In general $(A^\top A)^\top=A^\top A^{\top\top}=A^\top A$.)
>
> **B6.** $R_{30}R_{60}=R_{90}=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$.

### Part C: explain and prove

**C1.** Prove that every matrix map is linear: $A(u+v)=Au+Av$ and $A(cu)=cAu$. Use the column view.

**C2.** Prove that $(AB)^\top=B^\top A^\top$ by comparing entry $(i,j)$ of each side.

**C3.** Explain, without computing, why a $2\times3$ matrix cannot have an inverse that works on both sides.

**C4.** Explain why, if $AB=AC$ and $A$ is invertible, then $B=C$. Then give an example with a non-invertible $A$ where $AB=AC$ but $B\neq C$.

**C5.** Prove that a rotation matrix keeps lengths: $\|R_\theta x\|=\|x\|$. (Hint: compute $\|R_\theta x\|^2$ directly for $x=(x_1,x_2)$.)

> [!success]- Solutions to Part C
> **C1.** With columns $a_j$: $A(u+v)=\sum_j(u_j+v_j)a_j=\sum_ju_ja_j+\sum_jv_ja_j=Au+Av$. And $A(cu)=\sum_j(cu_j)a_j=c\sum_ju_ja_j=cAu$.
>
> **C2.** Entry $(i,j)$ of $(AB)^\top$ is entry $(j,i)$ of $AB$, which is (row $j$ of $A$) $\cdot$ (column $i$ of $B$). Entry $(i,j)$ of $B^\top A^\top$ is (row $i$ of $B^\top$) $\cdot$ (column $j$ of $A^\top$) $=$ (column $i$ of $B$) $\cdot$ (row $j$ of $A$). Same dot product.
>
> **C3.** It maps $\mathbb R^3$ to $\mathbb R^2$. Squeezing 3 dimensions into 2 must send some different inputs to the same output (chapter 5 makes this precise), so it cannot be undone. A two-sided inverse needs a square matrix.
>
> **C4.** Multiply both sides on the left by $A^{-1}$: $A^{-1}AB=A^{-1}AC$, so $B=C$. Counterexample: $A=\begin{bmatrix}1&0\\0&0\end{bmatrix}$, $B=\begin{bmatrix}1&0\\0&1\end{bmatrix}$, $C=\begin{bmatrix}1&0\\0&5\end{bmatrix}$. Then $AB=AC=\begin{bmatrix}1&0\\0&0\end{bmatrix}$: $A$ erases the second row, where $B$ and $C$ differ.
>
> **C5.** $R_\theta x=(x_1\cos\theta-x_2\sin\theta,\;x_1\sin\theta+x_2\cos\theta)$. Squaring and adding, the cross terms $\mp2x_1x_2\sin\theta\cos\theta$ cancel, leaving $(x_1^2+x_2^2)(\cos^2\theta+\sin^2\theta)=x_1^2+x_2^2$.

### Part D: practise with code

**D1.** In NumPy, `A @ x` multiplies a matrix by a vector and `A @ B` multiplies matrices. Confirm that `A * B` gives something different for $2\times2$ matrices, and describe what it computes.

**D2.** Draw the unit square (corners $(0,0),(1,0),(1,1),(0,1)$) and its image under each matrix in the gallery of section 3.4. Plot both with Matplotlib. Which maps keep its area?

**D3.** Write `rotation(theta)` returning $R_\theta$. Verify numerically that `rotation(a) @ rotation(b)` equals `rotation(a + b)`, and that `rotation(t).T @ rotation(t)` is the identity.

**D4.** Make a random $3\times3$ matrix, compute `np.linalg.inv(A)`, and check `A @ inv(A)` against `np.eye(3)` with `np.allclose`. Why use `allclose` rather than `==`?

> [!success]- Hints for Part D
> **D1.** `A * B` multiplies matching entries (the Hadamard product). It is not composition.
>
> **D2.** Rotations, reflections and the shear keep area 1. The scaling multiplies it by 6. The projection flattens it to area 0. Chapter 7 turns this into the determinant.
>
> **D4.** Floating-point arithmetic leaves tiny rounding errors such as $10^{-16}$, so exact equality usually fails even when the answer is mathematically correct.

---

## Where this is used

- **Kinematics.** Chaining rotations for each joint of an arm is multiplying matrices in the right order ([[02 Geometry and Kinematics]]).
- **Neural networks.** A layer computes $\sigma(Wx+b)$: a linear map, a shift, then a nonlinearity. Without $\sigma$, stacking layers would be pointless, because a product of matrices is just another matrix ([[05 Training Neural Policies]]).
- **Graphics and cameras.** Every 3-D view on a screen is built from rotations, scalings and projections.

Next: [[LA 04 Solving Linear Systems]], where we run a matrix backwards: given the output, find the input.

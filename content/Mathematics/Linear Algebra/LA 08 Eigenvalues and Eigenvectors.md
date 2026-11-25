---
type: course-chapter
course: linear-algebra
chapter: 8
tags: [mathematics, linear-algebra]
---

# Chapter 8: Eigenvalues and eigenvectors

Previous: [[LA 07 Determinants]] | [[LA 00 Course Map]] | Next: [[LA 09 Symmetric and Positive Definite Matrices]]

> [!abstract] The big idea
> Most vectors get turned when a matrix acts on them. A few special directions do not turn: they only get **stretched**. Those are the **eigenvectors**, and the stretch factors are the **eigenvalues**. If you describe vectors using eigenvector coordinates, a complicated matrix becomes simple scaling, and repeated application ($A^{100}$, long-run behaviour, stability) becomes easy to understand.

> [!info] In this chapter you will learn to
> 1. Explain what eigenvectors and eigenvalues are, with pictures.
> 2. Find them by hand for $2\times2$ (and simple $3\times3$) matrices.
> 3. Use the trace and determinant to check your answers.
> 4. Diagonalize a matrix, $A=V\Lambda V^{-1}$, and use it to compute powers.
> 5. Predict whether a repeated process grows, decays or oscillates.

> [!tip] Before you start
> You need determinants ([[LA 07 Determinants]]), null spaces ([[LA 05 Subspaces Basis and Rank]]), and solving quadratic equations: $\lambda^2+b\lambda+c=0$ gives $\lambda=\dfrac{-b\pm\sqrt{b^2-4c}}2$.

---

## 8.1 The idea

### A picture

Apply $A=\begin{bmatrix}2&0\\0&3\end{bmatrix}$ to a few vectors:

| $v$ | $Av$ | Did it turn? |
|---|---|---|
| $(1,0)$ | $(2,0)$ | no, just doubled |
| $(0,1)$ | $(0,3)$ | no, just tripled |
| $(1,1)$ | $(2,3)$ | **yes**: it now points more steeply |

$(1,0)$ and $(0,1)$ are special: $A$ stretches them without changing their direction. Every other direction gets turned.

### The definition

> [!note] Definition: eigenvector and eigenvalue
> A **nonzero** vector $v$ is an **eigenvector** of a square matrix $A$ if
> $$
> Av=\lambda v
> $$
> for some number $\lambda$. That number is the corresponding **eigenvalue**.

"Eigen" is German for "own" or "characteristic": these are the matrix's own directions.

### What different eigenvalues mean

| $\lambda$ | What $A$ does to $v$ |
|---|---|
| $\lambda>1$ | stretches it |
| $0<\lambda<1$ | shrinks it |
| $\lambda=1$ | leaves it exactly alone |
| $\lambda=0$ | destroys it: $v$ is in the null space |
| $\lambda<0$ | flips it to point the opposite way, and scales by $\lvert\lambda\rvert$ |

### Two details

- **The zero vector is excluded.** $A0=\lambda0$ is true for every $\lambda$, so allowing it would make the idea meaningless. (But $\lambda=0$ **is** allowed.)
- **Only the direction matters.** If $v$ is an eigenvector, so is $2v$, $-v$, or any nonzero multiple, with the same $\lambda$: $A(cv)=cAv=c\lambda v=\lambda(cv)$. When we say "the eigenvector", we mean "the eigen-direction", and we pick a convenient representative.

### Eigenvectors you can see without computing

- **Diagonal matrix**: the axes $e_1,e_2,\dots$ are eigenvectors, and the diagonal entries are the eigenvalues.
- **Projection onto a line**: vectors on the line are kept ($\lambda=1$); vectors perpendicular to it are destroyed ($\lambda=0$).
- **Reflection across a line**: vectors on the line are kept ($\lambda=1$); perpendicular vectors are flipped ($\lambda=-1$).
- **Rotation by $90^\circ$**: every vector is turned, so there are **no real eigenvectors** (section 8.5).

> [!question]- Check yourself
> 1. Is $(1,1)$ an eigenvector of $\begin{bmatrix}4&1\\2&3\end{bmatrix}$? If so, with what eigenvalue?
> 2. What are the eigenvalues of $\begin{bmatrix}-1&0\\0&5\end{bmatrix}$?
> 3. Reflection across the line $y=x$: name an eigenvector for $\lambda=1$ and one for $\lambda=-1$.
>
> **Answers.** 1. $A(1,1)=(5,5)=5(1,1)$. Yes, $\lambda=5$. 2. $-1$ and $5$. 3. $(1,1)$ lies on the line: $\lambda=1$. $(1,-1)$ is perpendicular: $\lambda=-1$.

---

## 8.2 Finding eigenvalues: the characteristic equation

### Turning the definition into an equation

Start from $Av=\lambda v$. Write $\lambda v$ as $\lambda Iv$ so both sides involve matrices, and move everything to one side:

$$
(A-\lambda I)\,v=0.
$$

We need a **nonzero** $v$ satisfying this. That means $A-\lambda I$ must have a nonzero null space, which means it must be **singular**. From chapter 7, singular means determinant zero:

> [!important] Characteristic equation
> $$
> \det(A-\lambda I)=0.
> $$
> The eigenvalues are exactly its solutions.

For an $n\times n$ matrix, $\det(A-\lambda I)$ is a polynomial of degree $n$ in $\lambda$, the **characteristic polynomial**. So an $n\times n$ matrix has $n$ eigenvalues, counted with repetition and allowing complex numbers.

### The procedure

1. Write $A-\lambda I$ (subtract $\lambda$ from each diagonal entry).
2. Compute its determinant: a polynomial in $\lambda$.
3. Set it to zero and solve: these are the eigenvalues.
4. For each eigenvalue, solve $(A-\lambda I)v=0$ to find its eigenvectors (a null space calculation, chapter 5).

### Worked example 8.1

$$
A=\begin{bmatrix}4&1\\2&3\end{bmatrix}.
$$

**Step 1.**

$$
A-\lambda I=\begin{bmatrix}4-\lambda&1\\2&3-\lambda\end{bmatrix}.
$$

**Step 2.**

$$
\det(A-\lambda I)=(4-\lambda)(3-\lambda)-(1)(2)=12-7\lambda+\lambda^2-2=\lambda^2-7\lambda+10.
$$

**Step 3.** Factor: $\lambda^2-7\lambda+10=(\lambda-5)(\lambda-2)$. Eigenvalues $\lambda_1=5$, $\lambda_2=2$.

**Step 4a: eigenvector for $\lambda=5$.**

$$
A-5I=\begin{bmatrix}-1&1\\2&-2\end{bmatrix}.
$$

The rows are multiples of each other (as they must be, since this matrix is singular). One equation remains: $-v_1+v_2=0$, so $v_2=v_1$. Choose $v_1=1$: eigenvector $(1,1)$.

**Step 4b: eigenvector for $\lambda=2$.**

$$
A-2I=\begin{bmatrix}2&1\\2&1\end{bmatrix}.
$$

Equation: $2v_1+v_2=0$, so $v_2=-2v_1$. Eigenvector $(1,-2)$.

**Check.** $A(1,1)=(5,5)=5(1,1)$ ✓. $A(1,-2)=(4-2,\;2-6)=(2,-4)=2(1,-2)$ ✓.

> [!tip] A built-in error check
> When you compute $A-\lambda I$ for a genuine eigenvalue, its rows **must** be dependent. If elimination gives you a pivot in every column, your eigenvalue is wrong.

### A $2\times2$ shortcut

For any $2\times2$ matrix,

$$
\det(A-\lambda I)=\lambda^2-(\operatorname{tr}A)\,\lambda+\det A,
$$

where the **trace** $\operatorname{tr}A$ is the sum of the diagonal entries. In example 8.1: trace 7, determinant 10, giving $\lambda^2-7\lambda+10$ directly.

---

## 8.3 Trace and determinant: free checks

For any square matrix:

> [!important] Two identities
> $$
> \lambda_1+\lambda_2+\cdots+\lambda_n=\operatorname{tr}A,\qquad\lambda_1\lambda_2\cdots\lambda_n=\det A.
> $$

Example 8.1: $5+2=7=4+3$ ✓ and $5\times2=10=12-2$ ✓.

These catch most arithmetic mistakes in seconds. They also give quick facts:

- **A matrix is singular exactly when 0 is an eigenvalue** (the product of eigenvalues is $\det A$).
- For a $2\times2$ matrix, knowing the trace and determinant is enough to find both eigenvalues.

> [!question]- Check yourself
> 1. A $2\times2$ matrix has trace 6 and determinant 8. Find its eigenvalues.
> 2. A $3\times3$ matrix has eigenvalues $2$, $-1$, $4$. What are its trace and determinant? Is it invertible?
>
> **Answers.** 1. $\lambda^2-6\lambda+8=(\lambda-2)(\lambda-4)$: $2$ and $4$. 2. Trace $5$, determinant $-8$. Invertible, since no eigenvalue is 0.

---

## 8.4 Diagonalization

### The idea

Suppose an $n\times n$ matrix $A$ has $n$ independent eigenvectors $v_1,\dots,v_n$ with eigenvalues $\lambda_1,\dots,\lambda_n$. Put the eigenvectors as columns of $V$, and the eigenvalues on the diagonal of $\Lambda$ (capital lambda):

$$
V=\begin{bmatrix}|&&|\\v_1&\cdots&v_n\\|&&|\end{bmatrix},\qquad\Lambda=\begin{bmatrix}\lambda_1&&\\&\ddots&\\&&\lambda_n\end{bmatrix}.
$$

The equations $Av_i=\lambda_iv_i$, all at once, say $AV=V\Lambda$. Since the columns are independent, $V$ is invertible, so

> [!important] Diagonalization
> $$
> A=V\Lambda V^{-1}.
> $$

### What it means: three steps

Read $Ax=V\Lambda V^{-1}x$ from right to left:

1. **$V^{-1}x$**: rewrite $x$ in eigenvector coordinates (how much of each $v_i$ it contains).
2. **$\Lambda$**: scale each coordinate by its own eigenvalue. No mixing between coordinates.
3. **$V$**: convert back to ordinary coordinates.

So in the right coordinate system, **every diagonalizable matrix is just independent scaling along a set of axes.** The difficulty of a matrix is only that its natural axes are not the standard ones. (Chapter 11 develops this "change of viewpoint" idea.)

### Worked example 8.2

For $A=\begin{bmatrix}4&1\\2&3\end{bmatrix}$:

$$
V=\begin{bmatrix}1&1\\1&-2\end{bmatrix},\qquad\Lambda=\begin{bmatrix}5&0\\0&2\end{bmatrix},\qquad V^{-1}=\frac1{-3}\begin{bmatrix}-2&-1\\-1&1\end{bmatrix}=\frac13\begin{bmatrix}2&1\\1&-1\end{bmatrix}.
$$

You can check that $V\Lambda V^{-1}$ multiplies out to $A$.

### The payoff: powers

$$
A^2=(V\Lambda V^{-1})(V\Lambda V^{-1})=V\Lambda(V^{-1}V)\Lambda V^{-1}=V\Lambda^2V^{-1},
$$

and in general

$$
A^k=V\Lambda^kV^{-1},\qquad\Lambda^k=\begin{bmatrix}\lambda_1^k&&\\&\ddots&\\&&\lambda_n^k\end{bmatrix}.
$$

Powers of a diagonal matrix are trivial: raise each diagonal entry to the power. Computing $A^{100}$ directly needs 99 matrix products; this way needs a handful of operations.

**Worked example 8.3.** Compute $A^kx$ for $x=(2,-1)$ with $A$ from example 8.1.

*Step 1: write $x$ in eigenvector coordinates.* Solve $c_1(1,1)+c_2(1,-2)=(2,-1)$: $c_1+c_2=2$ and $c_1-2c_2=-1$. Subtract: $3c_2=3$, so $c_2=1$, $c_1=1$. So $x=v_1+v_2$.

*Step 2: apply $A^k$.* Each eigenvector is simply scaled:

$$
A^kx=5^kv_1+2^kv_2=5^k\begin{bmatrix}1\\1\end{bmatrix}+2^k\begin{bmatrix}1\\-2\end{bmatrix}.
$$

For $k=3$: $125(1,1)+8(1,-2)=(133,109)$.

*Step 3: long-run behaviour.* As $k$ grows, $5^k$ dwarfs $2^k$. So $A^kx$ points more and more along $v_1=(1,1)$, and grows by a factor of about 5 each step.

### When is a matrix diagonalizable?

- If the $n$ eigenvalues are **all different**, the eigenvectors are automatically independent, and $A$ is diagonalizable. (Most matrices you meet.)
- If some eigenvalue is **repeated**, it may or may not work (section 8.5).
- **Symmetric** matrices are always diagonalizable, with perpendicular eigenvectors (chapter 9).

---

## 8.5 When things are less tidy

### Complex eigenvalues: rotation

$$
R_{90}=\begin{bmatrix}0&-1\\1&0\end{bmatrix},\qquad\det(R_{90}-\lambda I)=\lambda^2+1=0,\qquad\lambda=\pm i.
$$

No real solutions, because a quarter-turn changes the direction of **every** real vector. The complex eigenvalues are not meaningless: **complex eigenvalues signal rotation or oscillation.** For a general rotation $R_\theta$ the eigenvalues are $\cos\theta\pm i\sin\theta$: their size $|\lambda|=1$ says "no growth", and their angle $\theta$ says "turn by $\theta$ each step".

For real matrices, complex eigenvalues always come in conjugate pairs $a\pm bi$.

### Repeated eigenvalues

**The harmless case.** $I$ has eigenvalue 1 twice, and **every** vector is an eigenvector. Plenty of independent eigenvectors; diagonalizable (it already is diagonal).

**The defective case.** The shear

$$
H=\begin{bmatrix}1&1\\0&1\end{bmatrix}
$$

has $\det(H-\lambda I)=(1-\lambda)^2$, so $\lambda=1$ twice. But $H-I=\begin{bmatrix}0&1\\0&0\end{bmatrix}$ has a **one**-dimensional null space: only multiples of $(1,0)$. There is only one eigen-direction, not two. $H$ is **defective** and cannot be diagonalized.

Geometrically: the shear leaves the horizontal direction alone, but tilts every other direction. There is no second direction that it merely stretches.

> [!question]- Check yourself
> 1. Find the eigenvalues of $\begin{bmatrix}0&-2\\2&0\end{bmatrix}$. What does the matrix do?
> 2. Is $\begin{bmatrix}3&0\\0&3\end{bmatrix}$ diagonalizable? Is $\begin{bmatrix}3&1\\0&3\end{bmatrix}$?
>
> **Answers.** 1. $\lambda^2+4=0$, $\lambda=\pm2i$. It rotates by $90^\circ$ and doubles lengths. 2. The first yes (already diagonal). The second no: only $(1,0)$ is an eigenvector.

---

## 8.6 Why this matters: dynamics and stability

### Discrete time

Many systems evolve by repeated multiplication:

$$
x_{k+1}=Ax_k\quad\Longrightarrow\quad x_k=A^kx_0.
$$

Population models, Markov chains, iterative algorithms, and robot controllers sampled at fixed time steps all look like this. Write the starting state in eigenvector coordinates, $x_0=c_1v_1+\cdots+c_nv_n$. Then, as in example 8.3,

$$
x_k=c_1\lambda_1^kv_1+c_2\lambda_2^kv_2+\cdots+c_n\lambda_n^kv_n.
$$

**Each eigen-direction evolves on its own, by its own factor.** So:

| Eigenvalues | Long-run behaviour |
|---|---|
| all $\lvert\lambda_i\rvert<1$ | everything decays to $0$: **stable** |
| some $\lvert\lambda_i\rvert>1$ | that component explodes: **unstable** |
| largest $\lvert\lambda\rvert=1$ | settles to a steady pattern (Markov chains) |
| negative or complex $\lambda$ | oscillation |

The eigenvalue with the largest $|\lambda|$, the **dominant eigenvalue**, wins in the end, and $x_k$ lines up with its eigenvector.

### Worked example 8.4: a two-stage population

Each year, juveniles $j$ and adults $a$ change as follows: each adult produces 2 juveniles; half the juveniles survive to become adults; adults survive with probability $0.5$.

$$
\begin{bmatrix}j\\a\end{bmatrix}_{k+1}=\begin{bmatrix}0&2\\0.5&0.5\end{bmatrix}\begin{bmatrix}j\\a\end{bmatrix}_k.
$$

Trace $0.5$, determinant $-1$, so $\lambda^2-0.5\lambda-1=0$ and $\lambda=\dfrac{0.5\pm\sqrt{0.25+4}}2=\dfrac{0.5\pm2.06}2$: $\lambda_1\approx1.28$ and $\lambda_2\approx-0.78$.

Since $1.28>1$, the population grows about 28% per year in the long run. The negative eigenvalue produces a dying-out oscillation in the early years.

### Continuous time

For a system described by $\dot x=Ax$ (rate of change proportional to state), each eigen-direction evolves as $e^{\lambda t}$. Now the test is the **real part**:

- every eigenvalue with negative real part: decays, **stable**;
- any with positive real part: grows, **unstable**;
- imaginary parts produce oscillation.

This is how control engineers check that a feedback controller keeps a robot stable ([[03 Dynamics and Feedback]]).

---

## Summary

| Idea | Formula or fact |
|---|---|
| definition | $Av=\lambda v$, $v\neq0$ |
| find $\lambda$ | $\det(A-\lambda I)=0$ |
| find $v$ | null space of $A-\lambda I$ |
| checks | $\sum\lambda_i=\operatorname{tr}A$, $\prod\lambda_i=\det A$ |
| diagonalize | $A=V\Lambda V^{-1}$ |
| powers | $A^k=V\Lambda^kV^{-1}$ |
| stability (discrete) | all $\lvert\lambda\rvert<1$ |
| stability (continuous) | all $\operatorname{Re}\lambda<0$ |

**Three facts to remember:**

1. Eigenvectors are the directions a matrix only stretches.
2. In eigenvector coordinates, a matrix is just scaling, so powers are easy.
3. The largest $|\lambda|$ controls long-run growth or decay.

---

## Exercises

### Part A: warm-up

**A1.** Find the eigenvalues and eigenvectors of $\begin{bmatrix}2&1\\1&2\end{bmatrix}$. Check with trace and determinant.

**A2.** Find the eigenvalues of $\begin{bmatrix}3&7\\0&-2\end{bmatrix}$ without computing a determinant.

**A3.** If $Av=4v$, what is $A^3v$? What is $(A-I)v$? What is $A^{-1}v$ (assuming $A$ invertible)?

**A4.** A $2\times2$ matrix has trace 1 and determinant $-6$. Find its eigenvalues.

> [!success]- Solutions to Part A
> **A1.** $(2-\lambda)^2-1=0$ gives $\lambda=3,1$. For 3: $(1,1)$. For 1: $(1,-1)$. Trace $4=3+1$ ✓, det $3=3\times1$ ✓.
>
> **A2.** Triangular: the diagonal entries $3$ and $-2$.
>
> **A3.** $64v$; $3v$; $\tfrac14v$. The eigenvector is the same; the eigenvalue is transformed.
>
> **A4.** $\lambda^2-\lambda-6=(\lambda-3)(\lambda+2)$: $3$ and $-2$.

### Part B: core

**B1.** Diagonalize $A=\begin{bmatrix}1&2\\2&1\end{bmatrix}$ and use it to compute $A^{10}\begin{bmatrix}1\\0\end{bmatrix}$.

**B2.** Find the eigenvalues and eigenvectors of $\begin{bmatrix}2&0&0\\1&3&0\\0&0&1\end{bmatrix}$.

**B3.** Show that $\begin{bmatrix}2&1\\0&2\end{bmatrix}$ is not diagonalizable.

**B4.** For $x_{k+1}=\begin{bmatrix}0.5&0.4\\0.2&0.6\end{bmatrix}x_k$, find the eigenvalues. Does $x_k$ go to zero, grow, or settle?

**B5.** Fibonacci numbers satisfy $\begin{bmatrix}F_{k+1}\\F_k\end{bmatrix}=\begin{bmatrix}1&1\\1&0\end{bmatrix}\begin{bmatrix}F_k\\F_{k-1}\end{bmatrix}$. Find the eigenvalues of the matrix, and explain why $F_{k+1}/F_k$ approaches the larger one.

**B6.** A controller produces closed-loop matrix $\begin{bmatrix}1&0.1\\-k&0.9\end{bmatrix}$ (discrete time). For $k=0.5$, are both eigenvalues inside the unit circle? (Hint: compute them; they may be complex, and $|a+bi|=\sqrt{a^2+b^2}$.)

> [!success]- Solutions to Part B
> **B1.** Eigenvalues $3$ and $-1$, eigenvectors $(1,1)$ and $(1,-1)$. $(1,0)=\tfrac12(1,1)+\tfrac12(1,-1)$. So $A^{10}(1,0)=\tfrac12\,3^{10}(1,1)+\tfrac12(-1)^{10}(1,-1)=\tfrac12(59049+1,\;59049-1)=(29525,\;29524)$.
>
> **B2.** Lower triangular: $\lambda=2,3,1$. For $3$: $(A-3I)v=0$ gives $-v_1=0$, $v_1+0v_2=0$, $-2v_3=0$, so $v=(0,1,0)$. For $1$: $v_1=0$, then $v_2=0$, so $v=(0,0,1)$. For $2$: $v_3=0$ and $v_1+v_2=0$, so $v=(1,-1,0)$.
>
> **B3.** $\lambda=2$ twice. $A-2I=\begin{bmatrix}0&1\\0&0\end{bmatrix}$ has null space spanned by $(1,0)$ only. One eigenvector, two needed.
>
> **B4.** Trace $1.1$, det $0.30-0.08=0.22$. $\lambda^2-1.1\lambda+0.22=0$: $\lambda=\dfrac{1.1\pm\sqrt{1.21-0.88}}2=\dfrac{1.1\pm0.574}2$: $0.837$ and $0.263$. Both below 1: $x_k\to0$.
>
> **B5.** $\lambda^2-\lambda-1=0$: $\lambda=\dfrac{1\pm\sqrt5}2\approx1.618,\;-0.618$. The $1.618^k$ component dominates, so consecutive terms grow by a factor approaching $1.618$, the golden ratio.
>
> **B6.** Trace $1.9$, det $0.9+0.05=0.95$. $\lambda=\dfrac{1.9\pm\sqrt{3.61-3.8}}2=0.95\pm0.218i$. $|\lambda|=\sqrt{0.9025+0.0475}=\sqrt{0.95}\approx0.975<1$. Stable, with slowly decaying oscillation.

### Part C: explain and prove

**C1.** Prove that if $Av=\lambda v$, then $A^kv=\lambda^kv$ for every positive integer $k$.

**C2.** Prove that eigenvectors for two different eigenvalues are independent. (Hint: suppose $c_1v_1+c_2v_2=0$; apply $A$; subtract $\lambda_1$ times the original equation.)

**C3.** Prove that $A$ and $A^\top$ have the same eigenvalues. (Hint: determinant of a transpose.)

**C4.** Explain why a matrix with an eigenvalue of 0 cannot be invertible, in two ways: using the determinant, and using the definition of an eigenvector.

**C5.** Show that similar matrices $A$ and $B=P^{-1}AP$ have the same eigenvalues. How are their eigenvectors related?

> [!success]- Solutions to Part C
> **C1.** By induction: $A^{k+1}v=A(A^kv)=A(\lambda^kv)=\lambda^kAv=\lambda^{k+1}v$.
>
> **C2.** Apply $A$: $c_1\lambda_1v_1+c_2\lambda_2v_2=0$. Subtract $\lambda_1(c_1v_1+c_2v_2)=0$: $c_2(\lambda_2-\lambda_1)v_2=0$. Since $\lambda_2\neq\lambda_1$ and $v_2\neq0$, $c_2=0$; then $c_1v_1=0$ gives $c_1=0$.
>
> **C3.** $\det(A^\top-\lambda I)=\det\big((A-\lambda I)^\top\big)=\det(A-\lambda I)$. Same characteristic polynomial.
>
> **C4.** Determinant: $\det A=\prod\lambda_i=0$. Definition: $Av=0$ for some $v\neq0$, so $A$ sends two different vectors ($v$ and $0$) to the same output and cannot be undone.
>
> **C5.** $\det(P^{-1}AP-\lambda I)=\det\big(P^{-1}(A-\lambda I)P\big)=\det(A-\lambda I)$. If $Av=\lambda v$, then $B(P^{-1}v)=P^{-1}Av=\lambda P^{-1}v$: eigenvectors of $B$ are $P^{-1}$ times those of $A$.

### Part D: practise with code

**D1.** `vals, vecs = np.linalg.eig(A)`. Run it on example 8.1. NumPy normalizes eigenvectors to length 1: check that its vectors are multiples of $(1,1)$ and $(1,-2)$.

**D2.** Implement **power iteration**: start from a random $x$, repeat `x = A @ x; x = x / np.linalg.norm(x)` 50 times. Compare $x$ with the dominant eigenvector, and estimate $\lambda$ by `x @ A @ x`. Why does it work?

**D3.** Simulate the population of example 8.4 for 30 years from $(10,10)$. Plot total population on a log scale. What is the slope, and how does it relate to $\lambda_1$?

**D4.** Plot the trajectories $x_k$ for $A=\begin{bmatrix}0.9&-0.3\\0.3&0.9\end{bmatrix}$ starting from $(1,0)$. Compute its eigenvalues and explain the spiral.

> [!success]- Hints for Part D
> **D2.** Repeated multiplication amplifies the dominant eigen-component most (section 8.6). Normalizing just stops the numbers overflowing.
>
> **D3.** The log of the population grows by about $\ln1.28\approx0.247$ per year after the first few years.
>
> **D4.** $\lambda=0.9\pm0.3i$, $|\lambda|=\sqrt{0.9}\approx0.949$. Each step rotates by $\arctan(0.3/0.9)\approx18.4^\circ$ and shrinks by about 5%: an inward spiral.

---

## Where this is used

- **Stability of controllers** ([[03 Dynamics and Feedback]]).
- **Markov chains**: the long-run distribution is an eigenvector with eigenvalue 1 ([[PS 12 Markov Chains and Information]]).
- **Optimization**: the speed of gradient descent depends on the eigenvalues of the Hessian ([[LA 12 Matrix Calculus and Numerical Practice]]).
- **PageRank**, vibration modes of structures, and principal component analysis all reduce to eigenvectors.

Next: [[LA 09 Symmetric and Positive Definite Matrices]], where eigenvectors become perpendicular and everything becomes cleaner.

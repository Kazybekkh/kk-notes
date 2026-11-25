---
type: course-chapter
course: linear-algebra
chapter: 12
tags: [mathematics, linear-algebra, optimization]
---

# Chapter 12: Matrix calculus and numerical practice

Previous: [[LA 11 Change of Basis]] | [[LA 00 Course Map]]

> [!abstract] The big idea
> Derivatives of functions with many inputs and outputs are organized as vectors (**gradients**) and matrices (**Jacobians**). With that organization, the chain rule becomes matrix multiplication, which is exactly how neural networks are trained. The second half of the chapter is about trust: the **condition number** tells you whether a computed answer means anything.

> [!info] In this chapter you will learn to
> 1. Compute gradients of functions of a vector, and know what the gradient means.
> 2. Memorize and use the three most common matrix-calculus gradients.
> 3. Compute Jacobians, and apply the chain rule as a matrix product.
> 4. Explain backpropagation through a linear layer.
> 5. Analyse gradient descent on a quadratic using eigenvalues.
> 6. Use the condition number, and follow safe numerical habits.

> [!tip] Before you start
> You need partial derivatives from calculus: $\partial f/\partial x$ means "differentiate with respect to $x$, treating the other variables as constants". For $f=x^2y$, $\partial f/\partial x=2xy$ and $\partial f/\partial y=x^2$. From this course you need symmetric matrices and eigenvalues ([[LA 09 Symmetric and Positive Definite Matrices]]) and the SVD ([[LA 10 Singular Value Decomposition]]).

---

## 12.1 The gradient

### Definition

For a function that takes a vector and returns a number, $f:\mathbb R^n\to\mathbb R$, the **gradient** collects all its partial derivatives into a vector:

> [!note] Definition: gradient
> $$
> \nabla f(x)=\begin{bmatrix}\partial f/\partial x_1\\\partial f/\partial x_2\\\vdots\\\partial f/\partial x_n\end{bmatrix}.
> $$
> It has the same shape as $x$.

**Worked example 12.1.** $f(x_1,x_2)=x_1^2+3x_1x_2+5x_2^2$.

$$
\frac{\partial f}{\partial x_1}=2x_1+3x_2,\qquad\frac{\partial f}{\partial x_2}=3x_1+10x_2,\qquad\nabla f=\begin{bmatrix}2x_1+3x_2\\3x_1+10x_2\end{bmatrix}.
$$

At $x=(1,1)$: $\nabla f=(5,13)$.

### What the gradient means

The gradient gives the best **linear approximation** of $f$ near a point:

$$
f(x+d)\approx f(x)+\nabla f(x)^\top d.
$$

For a small step $d$, the change in $f$ is (approximately) the **dot product** of the gradient with the step. From chapter 2, a dot product $g\cdot d$ with $\|d\|$ fixed is:

- **largest** when $d$ points along $g$,
- **zero** when $d$ is perpendicular to $g$,
- **most negative** when $d$ points opposite to $g$.

> [!important] Three facts about the gradient
> 1. $\nabla f$ points in the direction of **steepest increase**.
> 2. $-\nabla f$ points in the direction of **steepest decrease**. That is the direction gradient descent steps in.
> 3. $\nabla f$ is **perpendicular to level curves** (moving along a level curve does not change $f$, so that direction has zero dot product with the gradient).

**Worked example 12.2.** Using example 12.1 at $(1,1)$, $f(1,1)=9$. Take a small step $d=(0.01,0)$: the approximation gives $9+5(0.01)=9.05$. The exact value is $f(1.01,1)=1.0201+3.03+5=9.0501$. Very close.

> [!question]- Check yourself
> 1. Find $\nabla f$ for $f(x,y,z)=xy+yz+zx$.
> 2. At a point, $\nabla f=(3,-4)$. In which unit direction does $f$ decrease fastest, and at what rate?
>
> **Answers.** 1. $(y+z,\;x+z,\;x+y)$. 2. Direction $-\nabla f/\|\nabla f\|=(-0.6,0.8)$. The rate is $\|\nabla f\|=5$ per unit step.

---

## 12.2 Three gradients to memorize

Matrix calculus looks intimidating, but nearly everything reduces to three rules. Each mirrors a rule from single-variable calculus.

| Function of $x$ | Gradient | Scalar analogue |
|---|---|---|
| $a^\top x$ | $a$ | $(ax)'=a$ |
| $x^\top x=\|x\|^2$ | $2x$ | $(x^2)'=2x$ |
| $x^\top Sx$, $S$ symmetric | $2Sx$ | $(sx^2)'=2sx$ |

For a non-symmetric $A$, the third becomes $\nabla(x^\top Ax)=(A+A^\top)x$.

### Why they are true

**Rule 1.** $a^\top x=a_1x_1+\cdots+a_nx_n$. Differentiating with respect to $x_i$ leaves $a_i$. So the gradient is $a$.

**Rule 2.** $x^\top x=x_1^2+\cdots+x_n^2$. The derivative with respect to $x_i$ is $2x_i$.

**Rule 3**, checked in 2-D. With $S=\begin{bmatrix}a&b\\b&c\end{bmatrix}$, $x^\top Sx=ax_1^2+2bx_1x_2+cx_2^2$. Then

$$
\frac{\partial}{\partial x_1}=2ax_1+2bx_2,\qquad\frac{\partial}{\partial x_2}=2bx_1+2cx_2,
$$

which is $2\begin{bmatrix}a&b\\b&c\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix}=2Sx$ ✓.

> [!tip] Shape check
> A gradient always has the same shape as the variable. If $x$ is $n\times1$, so is $\nabla f$. If your answer has the wrong shape, it is wrong. This catches most errors.

---

## 12.3 Least squares again, now by calculus

Minimize

$$
f(x)=\|Ax-b\|^2=(Ax-b)^\top(Ax-b)=x^\top A^\top Ax-2b^\top Ax+b^\top b.
$$

(The middle term: $x^\top A^\top b$ and $b^\top Ax$ are the same number, so they combine into $2b^\top Ax$.)

Apply the rules:

- $x^\top(A^\top A)x$: rule 3 with the symmetric $S=A^\top A$ gives $2A^\top Ax$.
- $-2b^\top Ax=-2(A^\top b)^\top x$: rule 1 gives $-2A^\top b$.
- $b^\top b$: a constant, gradient 0.

$$
\nabla f=2A^\top Ax-2A^\top b=2A^\top(Ax-b).
$$

Set it to zero: $A^\top Ax=A^\top b$. **The normal equations**, exactly as in chapter 6 from geometry. Two completely different routes, one answer.

The second derivative (Hessian) is $2A^\top A$, positive semidefinite (chapter 9), so this critical point is a minimum.

---

## 12.4 The Jacobian

### Definition

For a function with vector inputs **and** vector outputs, $g:\mathbb R^n\to\mathbb R^m$, the derivative is a matrix:

> [!note] Definition: Jacobian
> $$
> J=\begin{bmatrix}\dfrac{\partial g_1}{\partial x_1}&\cdots&\dfrac{\partial g_1}{\partial x_n}\\\vdots&&\vdots\\\dfrac{\partial g_m}{\partial x_1}&\cdots&\dfrac{\partial g_m}{\partial x_n}\end{bmatrix}\qquad(m\times n).
> $$

- **Row $i$** is the gradient of output $i$ (transposed).
- **Column $j$** shows how all outputs respond to input $j$.

And the linear approximation becomes

$$
g(x+d)\approx g(x)+J\,d.
$$

**The Jacobian is the matrix that the function looks like, up close.** Every smooth function is approximately linear on a small enough scale, and $J$ is that linear map.

**Worked example 12.3.** $g(x,y)=(x^2y,\;x+\sin y)$.

$$
J=\begin{bmatrix}2xy&x^2\\1&\cos y\end{bmatrix}.
$$

At $(1,0)$: $J=\begin{bmatrix}0&1\\1&1\end{bmatrix}$.

**Linear functions.** $g(x)=Ax$ has Jacobian $A$ everywhere. A linear map is its own best linear approximation.

### Worked example 12.4: a two-link robot arm

Link lengths $l_1,l_2$, joint angles $q_1,q_2$. The hand position is

$$
x=l_1\cos q_1+l_2\cos(q_1+q_2),\qquad y=l_1\sin q_1+l_2\sin(q_1+q_2).
$$

Differentiate each with respect to each joint angle:

$$
J(q)=\begin{bmatrix}-l_1\sin q_1-l_2\sin(q_1+q_2)&-l_2\sin(q_1+q_2)\\l_1\cos q_1+l_2\cos(q_1+q_2)&l_2\cos(q_1+q_2)\end{bmatrix}.
$$

It maps joint velocities to hand velocity: $\dot p=J(q)\,\dot q$.

Its determinant simplifies (use $\sin(a-b)$ identities) to

$$
\det J=l_1l_2\sin q_2.
$$

That is zero at $q_2=0$ (arm straight) and $q_2=\pi$ (folded back): the **singularities**, where the hand cannot move in some direction no matter how the joints turn (chapters 5 and 7).

---

## 12.5 The chain rule is matrix multiplication

If $h(x)=f(g(x))$, with $g:\mathbb R^n\to\mathbb R^m$ and $f:\mathbb R^m\to\mathbb R^p$, then

$$
J_h(x)=J_f\big(g(x)\big)\;J_g(x).
$$

Derivatives of composed functions **multiply**, in the same order as the functions compose. Shapes: $(p\times m)(m\times n)=p\times n$ ✓.

*Why:* near $x$, $g$ looks like $J_g$ and near $g(x)$, $f$ looks like $J_f$. A linear map followed by a linear map is their product (chapter 3).

**Worked example 12.5.** $g(x,y)=(x+y,\;xy)$ and $f(u,v)=u^2+v$. So $h(x,y)=(x+y)^2+xy$.

$$
J_g=\begin{bmatrix}1&1\\y&x\end{bmatrix},\qquad J_f=\begin{bmatrix}2u&1\end{bmatrix}=\begin{bmatrix}2(x+y)&1\end{bmatrix}.
$$

$$
J_h=\begin{bmatrix}2(x+y)+y&2(x+y)+x\end{bmatrix}=\begin{bmatrix}2x+3y&3x+2y\end{bmatrix}.
$$

Check directly: $h=x^2+3xy+y^2$, so $\partial h/\partial x=2x+3y$ ✓.

---

## 12.6 Backpropagation through a linear layer

A neural network is a long chain $x\to y_1\to y_2\to\cdots\to L$, ending in a scalar loss $L$. By the chain rule, $\partial L/\partial x$ is a long product of Jacobians.

**Key idea of backpropagation:** because the final output is a **scalar**, multiply the chain starting from the loss end. Then every intermediate result is a **vector** (a gradient), never a large matrix. That makes training affordable.

### One linear layer

Let $y=Wx$, with $W$ of shape $m\times n$. Suppose the layers above have already computed the **upstream gradient** $g=\partial L/\partial y$ (a vector of length $m$). We need the gradients with respect to the layer's input $x$ (to pass further down) and its weights $W$ (to update them):

> [!important] Linear layer gradients
> $$
> \frac{\partial L}{\partial x}=W^\top g,\qquad\frac{\partial L}{\partial W}=g\,x^\top.
> $$

**Why $W^\top g$.** Each $x_j$ affects every $y_i$ through the weight $W_{ij}$. So $\dfrac{\partial L}{\partial x_j}=\sum_i\dfrac{\partial L}{\partial y_i}W_{ij}=\sum_iW_{ij}g_i$, which is entry $j$ of $W^\top g$. Gradients flow **backwards** through the **transpose**.

**Why $gx^\top$.** $W_{ij}$ affects only $y_i$, with $\partial y_i/\partial W_{ij}=x_j$. So $\dfrac{\partial L}{\partial W_{ij}}=g_ix_j$, which is entry $(i,j)$ of the outer product $gx^\top$.

**Shape check.** $\partial L/\partial W$ must be $m\times n$, like $W$. $g$ is $m\times1$ and $x^\top$ is $1\times n$, so $gx^\top$ is $m\times n$ ✓. This is the only way to combine $g$ and $x$ into the right shape, which makes the formula easy to rebuild from scratch.

**Worked example 12.6.** $W=\begin{bmatrix}1&2\\0&1\end{bmatrix}$, $x=(3,1)$, so $y=(5,1)$. Loss $L=\tfrac12\|y\|^2$, so $g=\partial L/\partial y=y=(5,1)$.

$$
\frac{\partial L}{\partial x}=W^\top g=\begin{bmatrix}1&0\\2&1\end{bmatrix}\begin{bmatrix}5\\1\end{bmatrix}=\begin{bmatrix}5\\11\end{bmatrix},\qquad
\frac{\partial L}{\partial W}=\begin{bmatrix}5\\1\end{bmatrix}\begin{bmatrix}3&1\end{bmatrix}=\begin{bmatrix}15&5\\3&1\end{bmatrix}.
$$

Gradient descent would then update $W\leftarrow W-\eta\begin{bmatrix}15&5\\3&1\end{bmatrix}$.

---

## 12.7 Gradient descent on a quadratic

### The setup

Take the quadratic bowl

$$
f(x)=\tfrac12x^\top Sx-b^\top x,
$$

with $S$ symmetric positive definite. Then $\nabla f=Sx-b$, and the minimum $x^*$ solves $Sx^*=b$.

Gradient descent repeats

$$
x_{k+1}=x_k-\eta\,\nabla f(x_k)=x_k-\eta(Sx_k-b),
$$

where $\eta>0$ is the **step size** (learning rate).

### Analysing the error

Let $e_k=x_k-x^*$ be the error. Subtracting $x^*=x^*-\eta(Sx^*-b)$ from the update:

$$
e_{k+1}=(I-\eta S)\,e_k.
$$

Each step multiplies the error by the matrix $I-\eta S$. In the eigenvector basis of $S$ (chapter 11), this is diagonal: the error component along eigenvector $i$ is multiplied by

$$
1-\eta\lambda_i
$$

at every step.

### Consequences

> [!important] Gradient descent on a quadratic
> - **Convergence requires** $|1-\eta\lambda_i|<1$ for every $i$, which means
> $$
> 0<\eta<\frac2{\lambda_{\max}}.
> $$
> - **Progress in the flattest direction** is slow: its error shrinks by $1-\eta\lambda_{\min}$ per step, which is close to 1 when $\lambda_{\min}$ is small.
> - With the best step size, the error shrinks per step by about
> $$
> \frac{\kappa-1}{\kappa+1},\qquad\kappa=\frac{\lambda_{\max}}{\lambda_{\min}}.
> $$

The step size is **limited by the steepest direction** (too big and it overshoots and diverges there), while **progress is limited by the flattest direction**. A large ratio $\kappa$ (a long, narrow valley) means slow, zigzagging convergence.

**Worked example 12.7.** The loss $L=\tfrac12(x^2+5y^2)$ from [[01 Math for Learning]] has $S=\operatorname{diag}(1,5)$.

- $\lambda_{\max}=5$, so descent is stable only for $\eta<2/5=0.4$.
- At $\eta=0.37$: the $y$ error is multiplied by $1-0.37\times5=-0.85$ each step (it flips sign and shrinks slowly, which is the bouncing in the animation). The $x$ error is multiplied by $0.63$.
- At $\eta=0.08$: $y$ multiplied by $0.6$ (smooth), $x$ by $0.92$ (slow).
- $\kappa=5$, best-case rate about $4/6\approx0.67$ per step.

This is exactly why the animation shows one rate bouncing and the other crawling.

---

## 12.8 Conditioning: can you trust the answer?

### The condition number

> [!note] Definition: condition number
> $$
> \kappa(A)=\frac{\sigma_{\max}}{\sigma_{\min}}\ge1,
> $$
> the ratio of the largest to the smallest singular value (chapter 10).

When solving $Ax=b$, a small **relative** error in $b$ can cause a relative error in $x$ up to $\kappa$ times larger.

**Rule of thumb.** Double-precision arithmetic carries about 16 significant digits. If $\kappa\approx10^k$, expect to lose about $k$ of them.

### Worked example 12.8: an ill-conditioned system

$$
A=\begin{bmatrix}1&1\\1&1.0001\end{bmatrix}.
$$

- With $b=(2,\;2)$: solution $x=(2,\;0)$.
- With $b=(2,\;2.0001)$: solution $x=(1,\;1)$.

A change in the **fifth significant digit** of $b$ completely changed the answer. The columns are almost parallel, so $\sigma_{\min}$ is tiny and $\kappa\approx4\times10^4$.

**Picture.** Each equation is a line. These two lines are nearly parallel, so moving one slightly slides their crossing point a long way.

### Why not use the determinant?

Recall chapter 7: $0.1I$ in 100 dimensions has determinant $10^{-100}$ but $\kappa=1$, perfectly conditioned. The determinant measures volume; the condition number measures **distortion**. Only distortion matters for accuracy.

---

## 12.9 Practical rules

> [!tip] Numerical habits worth keeping
> 1. **Solve, do not invert.** `np.linalg.solve(A, b)`, not `np.linalg.inv(A) @ b`.
> 2. **Least squares via QR or SVD.** `np.linalg.lstsq(A, b)`. Forming $A^\top A$ **squares** the condition number: $\kappa(A^\top A)=\kappa(A)^2$.
> 3. **Scale your features.** Columns in wildly different units inflate $\kappa$.
> 4. **Regularize ill-conditioned problems.** Ridge regression solves $(A^\top A+\lambda I)x=A^\top b$, lifting every eigenvalue by $\lambda$ (chapter 9, exercise C4).
> 5. **Check gradients numerically.** Compare your formula with the central difference
> $$
> \frac{\partial f}{\partial x_i}\approx\frac{f(x+\varepsilon e_i)-f(x-\varepsilon e_i)}{2\varepsilon},\qquad\varepsilon\approx10^{-5}.
> $$
> 6. **Never compare floats with `==`.** Use `np.allclose` or a tolerance.
> 7. **Use specialized solvers** for special matrices: `eigh` for symmetric, Cholesky for positive definite.

---

## Summary

| Idea | Fact |
|---|---|
| gradient | vector of partials; steepest ascent |
| key gradients | $a^\top x\to a$; $\|x\|^2\to2x$; $x^\top Sx\to2Sx$ |
| least squares | $\nabla=2A^\top(Ax-b)=0$ |
| Jacobian | $m\times n$ matrix of partials; local linear map |
| chain rule | $J_{f\circ g}=J_fJ_g$ |
| linear layer | $\partial L/\partial x=W^\top g$, $\partial L/\partial W=gx^\top$ |
| GD on a quadratic | error factor $1-\eta\lambda_i$; need $\eta<2/\lambda_{\max}$ |
| condition number | $\sigma_{\max}/\sigma_{\min}$; lose about $\log_{10}\kappa$ digits |

**Three facts to remember:**

1. The gradient points uphill; the Jacobian is the local linear map.
2. Chain rule = multiply Jacobians; backprop does it from the loss end.
3. Eigenvalues set the speed of gradient descent; singular values set the accuracy of solving.

---

## Exercises

### Part A: warm-up

**A1.** Find $\nabla f$ for $f(x)=3x_1^2+2x_1x_2+x_2^2$, and evaluate it at $(1,1)$.

**A2.** Find the gradient of $f(x)=\|x-c\|^2$ for a fixed vector $c$. Where is it zero?

**A3.** Write the Jacobian of $g(x_1,x_2)=(x_1x_2,\;x_1+x_2,\;x_1^2)$.

**A4.** $S$ has eigenvalues 1 and 100. What is the largest stable learning rate, and what is $\kappa$?

> [!success]- Solutions to Part A
> **A1.** $(6x_1+2x_2,\;2x_1+2x_2)=(8,4)$ at $(1,1)$.
>
> **A2.** $2(x-c)$, zero at $x=c$: the closest point to $c$ is $c$ itself.
>
> **A3.** $\begin{bmatrix}x_2&x_1\\1&1\\2x_1&0\end{bmatrix}$ ($3\times2$).
>
> **A4.** $\eta<0.02$. $\kappa=100$.

### Part B: core

**B1.** Find the gradient of $f(x)=\tfrac12x^\top Sx-b^\top x$ and its minimizer, for $S=\begin{bmatrix}2&1\\1&3\end{bmatrix}$ and $b=(1,2)$.

**B2.** For the two-link arm with $l_1=l_2=1$, evaluate $J$ and $\det J$ at $q=(0,\pi/2)$. Interpret.

**B3.** A layer computes $y=Wx$ with $W=\begin{bmatrix}1&-1\\2&0\\0&3\end{bmatrix}$ and $x=(1,2)$. The upstream gradient is $g=(1,0,-1)$. Compute $\partial L/\partial x$ and $\partial L/\partial W$.

**B4.** Run three steps of gradient descent by hand on $f(x)=\tfrac12(x_1^2+4x_2^2)$ from $(1,1)$ with $\eta=0.2$. Predict, using the factors $1-\eta\lambda_i$, what happens to each coordinate.

**B5.** Use the chain rule to find $\nabla h$ for $h(x)=\|Ax-b\|^2$, viewing it as $f(g(x))$ with $g(x)=Ax-b$ and $f(u)=\|u\|^2$.

> [!success]- Solutions to Part B
> **B1.** $\nabla f=Sx-b$. Solve $\begin{bmatrix}2&1\\1&3\end{bmatrix}x=\begin{bmatrix}1\\2\end{bmatrix}$: det 5, $x=\tfrac15\begin{bmatrix}3&-1\\-1&2\end{bmatrix}\begin{bmatrix}1\\2\end{bmatrix}=\tfrac15(1,3)=(0.2,0.6)$.
>
> **B2.** $q_1=0$, $q_1+q_2=\pi/2$. $J=\begin{bmatrix}-0-1&-1\\1+0&0\end{bmatrix}=\begin{bmatrix}-1&-1\\1&0\end{bmatrix}$, $\det J=1=\sin(\pi/2)$. The elbow is bent at a right angle, the best-conditioned configuration: the hand can move freely in every direction.
>
> **B3.** $W^\top g=\begin{bmatrix}1&2&0\\-1&0&3\end{bmatrix}\begin{bmatrix}1\\0\\-1\end{bmatrix}=(1,\;-4)$. $gx^\top=\begin{bmatrix}1&2\\0&0\\-1&-2\end{bmatrix}$.
>
> **B4.** $\lambda=1,4$. Factors: $1-0.2=0.8$ for $x_1$, $1-0.8=0.2$ for $x_2$. So $x_1$: $0.8,0.64,0.512$; $x_2$: $0.2,0.04,0.008$. The steep coordinate collapses fast, the shallow one slowly.
>
> **B5.** $J_g=A$, $\nabla f(u)=2u$, so $J_f=2u^\top$. $J_h=2(Ax-b)^\top A$, and the gradient is its transpose: $2A^\top(Ax-b)$. Same as section 12.3.

### Part C: explain and prove

**C1.** Prove that $\nabla(x^\top Ax)=(A+A^\top)x$ for any square $A$, by computing $\partial/\partial x_k$ of $\sum_i\sum_jA_{ij}x_ix_j$.

**C2.** Explain why the gradient is perpendicular to the level curves of $f$.

**C3.** Show that $\kappa(A^\top A)=\kappa(A)^2$ using the SVD. Why does this make the normal equations risky?

**C4.** In gradient descent on a quadratic, what happens if $\eta=2/\lambda_{\max}$ exactly? What if $\eta$ is a little larger?

> [!success]- Solutions to Part C
> **C1.** $\dfrac{\partial}{\partial x_k}\sum_{i,j}A_{ij}x_ix_j=\sum_jA_{kj}x_j+\sum_iA_{ik}x_i=(Ax)_k+(A^\top x)_k$.
>
> **C2.** Along a level curve $f$ is constant, so the directional derivative $\nabla f\cdot d$ in the tangent direction $d$ is zero: the gradient is perpendicular to $d$.
>
> **C3.** $A^\top A=V\Sigma^\top\Sigma V^\top$ has singular values $\sigma_i^2$, so $\kappa=\sigma_{\max}^2/\sigma_{\min}^2$. If $\kappa(A)=10^6$, then $\kappa(A^\top A)=10^{12}$, losing about 12 of 16 digits.
>
> **C4.** At exactly $2/\lambda_{\max}$, the factor in the steepest direction is $-1$: the error flips sign forever without shrinking. Slightly larger, its size exceeds 1 and the error grows without bound: divergence.

### Part D: practise with code

**D1.** Implement `numerical_grad(f, x, eps=1e-5)` using central differences. Compare it with your formula for A1 at several points.

**D2.** Implement gradient descent on $f(x)=\tfrac12x^\top Sx$ for $S=\operatorname{diag}(1,\kappa)$ with $\kappa=1,10,100$, using $\eta=1/\kappa$. Plot $\log\|x_k\|$ against $k$. How does the slope depend on $\kappa$?

**D3.** Build the Hilbert matrix (`scipy.linalg.hilbert(n)`) for $n=4,8,12$. Print its condition number. Solve $Hx=Hx_{\text{true}}$ for $x_{\text{true}}$ all ones, and report the error. What happens as $n$ grows?

**D4.** Write a tiny two-layer network by hand in NumPy (`y = W2 @ np.tanh(W1 @ x)`), compute the gradient of a squared loss with respect to `W1` using the chain rule, and verify it with `numerical_grad`.

> [!success]- Hints for Part D
> **D2.** With $\eta=1/\kappa$, the slow direction shrinks by $1-1/\kappa$ per step, so $\log\|x_k\|$ falls with slope about $-1/\kappa$: 100 times slower at $\kappa=100$.
>
> **D3.** The condition number explodes (about $10^{16}$ by $n=12$), and the computed $x$ becomes garbage even though the problem looks innocent.
>
> **D4.** For $h=\tanh(W_1x)$, the upstream gradient into $W_1x$ is $(W_2^\top g)\odot(1-h^2)$, where $\odot$ is entry-wise multiplication. Then $\partial L/\partial W_1$ is that vector times $x^\top$.

---

## Where this is used

Everything in [[05 Training Neural Policies]] is this chapter at scale. Jacobians drive velocity kinematics and operational-space control ([[02 Geometry and Kinematics]]), and linearizing a nonlinear system around an operating point, the starting move of [[03 Dynamics and Feedback]], is computing a Jacobian.

**You have finished the linear algebra course.** Go back to the checkpoint questions in [[LA 00 Course Map]] and answer them without notes.

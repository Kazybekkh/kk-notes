---
type: course-chapter
course: linear-algebra
chapter: 1
tags: [mathematics, linear-algebra]
---

# Chapter 1: Vectors and linear combinations

[[LA 00 Course Map]] | Next: [[LA 02 Dot Product Length and Angle]]

> [!abstract] The big idea
> A vector is a list of numbers that you are allowed to **add** and **scale**. Almost all of linear algebra comes from one question: *if I add and scale a few vectors, what can I build?*

> [!info] In this chapter you will learn to
> 1. Read and write vectors, and switch between the "arrow" picture and the "list of data" picture.
> 2. Add vectors and multiply them by numbers, by hand and geometrically.
> 3. Write one vector as a **linear combination** of others, and find the weights.
> 4. Describe the **span** of a set of vectors (a line, a plane, or more).
> 5. Decide whether vectors are **linearly independent**, and explain what that means.

> [!tip] Before you start
> You only need school algebra: solving two equations in two unknowns, such as $a+b=5$, $a-b=1$. If you can do that, you are ready.

---

## 1.1 What is a vector?

### Why we need them

Many things in the world need **more than one number** to describe them:

- A point on a map needs two numbers: how far east, how far north.
- A robot arm with three joints needs three angles.
- A colour on a screen needs three numbers: red, green, blue.
- A $28\times28$ greyscale image is $784$ brightness values.

We want one object that holds all those numbers together, in a fixed order, so that we can do maths with the whole thing at once. That object is a **vector**.

### The definition

> [!note] Definition: vector
> A **vector** with $n$ entries is an ordered list of $n$ real numbers. We write it as a column:
> $$
> v=\begin{bmatrix}v_1\\v_2\\\vdots\\v_n\end{bmatrix}.
> $$
> The numbers $v_1,\dots,v_n$ are the **entries** (or components). The set of all such vectors is called $\mathbb R^n$ ("R-n").

Let's unpack each word.

- **"Ordered"** means position matters. $\begin{bmatrix}3\\1\end{bmatrix}$ and $\begin{bmatrix}1\\3\end{bmatrix}$ are different vectors, the same way "3 east, 1 north" is a different place from "1 east, 3 north".
- **"$n$ entries"** is the **dimension** of the space the vector lives in. $\begin{bmatrix}3\\1\end{bmatrix}$ lives in $\mathbb R^2$, the plane. $\begin{bmatrix}1\\0\\2\end{bmatrix}$ lives in $\mathbb R^3$, ordinary 3-D space.
- **$\mathbb R$** stands for the real numbers. $\mathbb R^2$ means "pairs of real numbers", $\mathbb R^3$ means "triples", and so on.

To save space in writing, people also write a vector on one line, such as $v=(3,1)$. It means the same column. Later you will meet the **transpose**, $v^\top=\begin{bmatrix}3&1\end{bmatrix}$, which really is a row; for now, treat $(3,1)$ as a shorthand for the column.

### Two ways to picture a vector

You should get comfortable switching between these two pictures. Each one is good for different things.

**Picture 1: an arrow.** The vector $v=(3,1)$ is an arrow that starts at the origin $(0,0)$ and ends at the point 3 units right and 1 unit up.

```
  y
  2 |
  1 |        ● (3,1)
    |     _/
    |  _/
  0 +----------------- x
    0  1  2  3
```

The arrow has a **direction** (where it points) and a **length** (how long it is). This picture is wonderful in 2-D and 3-D, because you can draw it.

**Picture 2: a record of data.** The vector $q=(0.2,\,-1.1,\,0.7)$ might hold the three joint angles of a robot arm, in radians. Nobody draws it as an arrow; it is just three numbers kept together.

This picture is the one you need in high dimensions. A 784-entry image vector cannot be drawn, but every rule you learn with 2-D arrows still works on it.

> [!tip] The habit to build
> Learn each new idea with a 2-D arrow you can draw. Then trust that the same algebra works in any number of dimensions.

### Equality

Two vectors are equal exactly when they have the same number of entries and every entry matches:

$$
\begin{bmatrix}a\\b\end{bmatrix}=\begin{bmatrix}3\\1\end{bmatrix}\quad\Longleftrightarrow\quad a=3\text{ and }b=1.
$$

So **one vector equation is really several ordinary equations**, one per entry. Keep this in mind; you will use it constantly.

### The zero vector

The vector with every entry equal to zero is the **zero vector**, written $0$ (sometimes $\mathbf 0$):

$$
0=\begin{bmatrix}0\\0\\\vdots\\0\end{bmatrix}.
$$

As an arrow it has no length and no direction: it is just the origin.

> [!question]- Check yourself
> 1. Which space does $(4,-2,0,7)$ live in?
> 2. Are $(1,2)$ and $(2,1)$ equal?
> 3. Write $\begin{bmatrix}x+1\\2y\end{bmatrix}=\begin{bmatrix}5\\6\end{bmatrix}$ as two ordinary equations and solve.
>
> **Answers.** 1. $\mathbb R^4$, since it has four entries. 2. No, order matters. 3. $x+1=5$ and $2y=6$, so $x=4$, $y=3$.

---

## 1.2 Adding vectors

### The rule

> [!note] Definition: vector addition
> To add two vectors **of the same size**, add matching entries:
> $$
> \begin{bmatrix}u_1\\u_2\\\vdots\\u_n\end{bmatrix}+\begin{bmatrix}v_1\\v_2\\\vdots\\v_n\end{bmatrix}=\begin{bmatrix}u_1+v_1\\u_2+v_2\\\vdots\\u_n+v_n\end{bmatrix}.
> $$

**Worked example 1.1.**

$$
\begin{bmatrix}3\\1\end{bmatrix}+\begin{bmatrix}-1\\2\end{bmatrix}=\begin{bmatrix}3+(-1)\\1+2\end{bmatrix}=\begin{bmatrix}2\\3\end{bmatrix}.
$$

**Worked example 1.2.**

$$
\begin{bmatrix}1\\0\\4\end{bmatrix}+\begin{bmatrix}2\\-5\\-4\end{bmatrix}=\begin{bmatrix}3\\-5\\0\end{bmatrix}.
$$

You **cannot** add vectors of different sizes. $(1,2)+(1,2,3)$ is not defined, just as you cannot add a map location to a colour.

### What addition means: walking

Think of a vector as an instruction to walk: $(3,1)$ means "3 steps east, 1 step north".

Adding $u+v$ means: follow $u$, then **from where you ended up**, follow $v$. The sum is where you finish.

```
           ● end = (2,3)
          /|
       v / |
        /  |
(3,1) ●    |   u = (3,1), then v = (-1,2)
     /     |
  u /      |
   /       |
  ●--------+
origin
```

This is the **tip-to-tail** rule: place the tail of $v$ at the tip of $u$.

Why does it match the entry-by-entry rule? Walking east 3 and then east $-1$ (that is, west 1) puts you at east $3+(-1)=2$. The east-west numbers simply add, and so do the north-south numbers. Each coordinate adds on its own.

### The parallelogram

If you instead walk $v$ first and then $u$, you finish at the same point, because $u+v=v+u$ (ordinary addition does not care about order). The two routes form the sides of a **parallelogram**, and $u+v$ is its diagonal.

### Rules that addition obeys

These all follow directly from the same rules for ordinary numbers, entry by entry:

| Rule | Formula | In words |
|---|---|---|
| commutative | $u+v=v+u$ | order does not matter |
| associative | $(u+v)+w=u+(v+w)$ | grouping does not matter |
| zero | $v+0=v$ | adding nothing changes nothing |
| negative | $v+(-v)=0$ | walking there and back returns you home |

Here $-v$ is the vector with every entry negated, for example $-(3,1)=(-3,-1)$. It points the opposite way with the same length.

**Subtraction** is adding the negative: $u-v=u+(-v)$.

> [!example] Subtraction as "from $v$ to $u$"
> $u-v$ is the arrow that goes **from the tip of $v$ to the tip of $u$**. Check: start at $v$, add $u-v$, and you get $v+(u-v)=u$.
>
> With $u=(5,4)$ and $v=(2,1)$: $u-v=(3,3)$. If a robot's hand is at $v$ and the target is at $u$, then $u-v$ is exactly the move it must make.

> [!question]- Check yourself
> 1. Compute $(2,-1,0)+(1,1,1)$.
> 2. Compute $(4,4)-(1,3)$ and say in words what it represents if the points are positions.
> 3. Why is $(1,2)+(3,4,5)$ not allowed?
>
> **Answers.** 1. $(3,0,1)$. 2. $(3,1)$: the step needed to get from $(1,3)$ to $(4,4)$. 3. The vectors have different sizes, so entries cannot be matched.

---

## 1.3 Scaling vectors

### The rule

> [!note] Definition: scalar multiplication
> To multiply a vector by a number $c$ (a **scalar**), multiply every entry by $c$:
> $$
> c\begin{bmatrix}v_1\\\vdots\\v_n\end{bmatrix}=\begin{bmatrix}cv_1\\\vdots\\cv_n\end{bmatrix}.
> $$

"Scalar" just means "a single ordinary number", as opposed to a vector. The name comes from what it does: it **scales**.

**Worked example 1.3.**

$$
2\begin{bmatrix}3\\1\end{bmatrix}=\begin{bmatrix}6\\2\end{bmatrix},\qquad
-1\begin{bmatrix}3\\1\end{bmatrix}=\begin{bmatrix}-3\\-1\end{bmatrix},\qquad
\tfrac12\begin{bmatrix}3\\1\end{bmatrix}=\begin{bmatrix}1.5\\0.5\end{bmatrix}.
$$

### What scaling means

| Scalar $c$ | Effect on the arrow |
|---|---|
| $c>1$ | same direction, longer |
| $0<c<1$ | same direction, shorter |
| $c=1$ | unchanged |
| $c=0$ | collapses to the zero vector |
| $c<0$ | flips to the opposite direction, then stretches by $\lvert c\rvert$ |

The important thing: **scaling never turns a vector sideways**. Every multiple $cv$ lies on the same line through the origin as $v$. We will use this fact many times.

### Rules

| Rule | Formula |
|---|---|
| distributes over vectors | $c(u+v)=cu+cv$ |
| distributes over scalars | $(c+d)v=cv+dv$ |
| associative | $c(dv)=(cd)v$ |
| one | $1v=v$ |

**Why is $c(u+v)=cu+cv$ true?** Look at one entry. On the left the entry is $c(u_i+v_i)$; on the right it is $cu_i+cv_i$. Those are equal by ordinary algebra. Since every entry matches, the vectors are equal. This "check one entry" argument proves all the rules in this chapter.

> [!question]- Check yourself
> 1. Compute $-3(1,0,-2)$.
> 2. Is $(6,3)$ a multiple of $(2,1)$? Is $(6,4)$?
> 3. Simplify $2(u+v)-u$.
>
> **Answers.** 1. $(-3,0,6)$. 2. Yes, $3(2,1)$. No: you would need $c=3$ from the first entry and $c=4$ from the second. 3. $u+2v$.

---

## 1.4 Linear combinations

### Putting the two operations together

Now combine both operations. Take some vectors, scale each one, and add the results.

> [!note] Definition: linear combination
> A **linear combination** of the vectors $v_1,v_2,\dots,v_k$ is any vector of the form
> $$
> c_1v_1+c_2v_2+\cdots+c_kv_k,
> $$
> where $c_1,\dots,c_k$ are scalars, called the **weights** (or coefficients).

The word "linear" signals that only these two operations are used. No squaring, no multiplying vectors together, no square roots.

**Worked example 1.4.** With $v_1=(1,0)$, $v_2=(1,1)$ and weights $c_1=2$, $c_2=3$:

$$
2\begin{bmatrix}1\\0\end{bmatrix}+3\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}2\\0\end{bmatrix}+\begin{bmatrix}3\\3\end{bmatrix}=\begin{bmatrix}5\\3\end{bmatrix}.
$$

### The recipe picture

A good way to think about it: the vectors are **ingredients**, and the weights are **amounts**.

> [!example] Mixing paint
> Suppose each paint is described by (red, green, blue) amounts per litre:
> - paint A $=(1,0,0)$ (pure red)
> - paint B $=(0,0,1)$ (pure blue)
>
> Mixing 2 litres of A with 1 litre of B gives $2A+1B=(2,0,1)$. Every colour you can mix is a linear combination of A and B. Notice you can never get any green, because neither ingredient has any. That observation is the seed of the idea of **span** in the next section.

### The reverse question: finding the weights

The interesting question goes backwards: **given a target vector, which weights produce it?**

**Worked example 1.5.** Can we write $b=(3,2)$ as a combination of $v_1=(1,0)$ and $v_2=(1,1)$?

*Step 1: write what we want.* We need numbers $c_1,c_2$ with

$$
c_1\begin{bmatrix}1\\0\end{bmatrix}+c_2\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}3\\2\end{bmatrix}.
$$

*Step 2: compute the left side.* It equals $\begin{bmatrix}c_1+c_2\\c_2\end{bmatrix}$.

*Step 3: match entries* (remember: one vector equation is several ordinary equations):

$$
\begin{aligned}
c_1+c_2&=3\quad\text{(top entry)}\\
c_2&=2\quad\text{(bottom entry)}
\end{aligned}
$$

*Step 4: solve.* The second equation gives $c_2=2$. Then the first gives $c_1=1$.

*Step 5: check.* $1(1,0)+2(1,1)=(1,0)+(2,2)=(3,2)$. Correct.

> [!important] The key connection
> Finding weights for a linear combination **is the same thing as solving a system of linear equations**. This link between vectors and equation systems is the backbone of the whole course. Chapter 4 ([[LA 04 Solving Linear Systems]]) gives a method that works for any size.

**Worked example 1.6 (no solution).** Can $b=(1,5)$ be written as a combination of $v_1=(1,2)$ and $v_2=(2,4)$?

Matching entries:

$$
\begin{aligned}
c_1+2c_2&=1\\
2c_1+4c_2&=5
\end{aligned}
$$

Multiply the first equation by 2: $2c_1+4c_2=2$. But the second equation says the same left side equals 5. Since $2\neq5$, **there is no solution**.

Why? Look at the ingredients: $v_2=2v_1$. Both point along the same line, so every combination stays on that line. The target $(1,5)$ is not on it.

**Worked example 1.7 (many solutions).** Write $b=(3,6)$ using the same $v_1=(1,2)$, $v_2=(2,4)$. The equations are $c_1+2c_2=3$ and $2c_1+4c_2=6$. The second is just twice the first, so we only really have one equation with two unknowns. Choose any $c_2$, say $c_2=t$, then $c_1=3-2t$. For example $t=0$ gives $3v_1$, and $t=1$ gives $v_1+v_2$. Both equal $(3,6)$. There are infinitely many ways.

These three examples show the only three possibilities: **exactly one way, no way, or infinitely many ways**. Chapter 4 explains why there is never "exactly two".

> [!question]- Check yourself
> 1. Compute $3(1,-1)+(-2)(0,1)$.
> 2. Write $(5,1)$ as a combination of $(1,1)$ and $(1,-1)$.
> 3. Can $(1,0,0)$ be written as a combination of $(0,1,0)$ and $(0,0,1)$? Why or why not?
>
> **Answers.** 1. $(3,-3)+(0,-2)=(3,-5)$. 2. $c_1+c_2=5$ and $c_1-c_2=1$, so $c_1=3$, $c_2=2$. 3. No. Every combination has first entry $0c_1+0c_2=0$, but the target has first entry 1.

---

## 1.5 Span: everything you can build

### The definition

> [!note] Definition: span
> The **span** of vectors $v_1,\dots,v_k$ is the set of **all** their linear combinations:
> $$
> \operatorname{span}\{v_1,\dots,v_k\}=\{c_1v_1+\cdots+c_kv_k\;:\;c_1,\dots,c_k\in\mathbb R\}.
> $$

Read the set notation as: "all vectors of the form $c_1v_1+\cdots+c_kv_k$, where the $c$'s can be any real numbers."

In the paint analogy, the span is **every colour you could possibly mix**.

So "is $b$ a linear combination of the $v$'s?" and "is $b$ in the span of the $v$'s?" are the same question.

### What spans look like

Let's build up one vector at a time, in $\mathbb R^3$.

**One nonzero vector.** The span of $v$ is all multiples $cv$. From section 1.3, all multiples lie on one line. So:

$$
\operatorname{span}\{v\}=\text{the line through the origin in the direction of }v.
$$

**Two vectors pointing in different directions.** Combinations $c_1v_1+c_2v_2$ can move along $v_1$ and along $v_2$ freely, so they sweep out a whole flat **plane** through the origin.

**Two vectors on the same line.** If $v_2=3v_1$, then $c_1v_1+c_2v_2=(c_1+3c_2)v_1$. That is just a multiple of $v_1$. The span is still only a **line**. The second vector added nothing new.

**Three vectors in $\mathbb R^3$.** If the third points out of the plane of the first two, the span is all of $\mathbb R^3$. If it lies in that plane, the span is still just the plane.

| Vectors | Typical span | Exception |
|---|---|---|
| one nonzero vector | a line | none |
| two vectors | a plane | a line, if they are parallel |
| three vectors in $\mathbb R^3$ | all of $\mathbb R^3$ | a plane or line, if one is "redundant" |

### Two facts that always hold

1. **The span always contains the zero vector.** Choose all weights equal to zero.
2. **The span always passes through the origin.** That follows from fact 1. A line that misses the origin, such as $y=x+1$, can never be a span.

**Worked example 1.8.** Is $(2,3,5)$ in the span of $v_1=(1,0,1)$ and $v_2=(0,1,1)$?

We need $c_1(1,0,1)+c_2(0,1,1)=(c_1,\,c_2,\,c_1+c_2)$ to equal $(2,3,5)$. The first two entries force $c_1=2$, $c_2=3$. The third entry then must be $2+3=5$. It is. So yes: $(2,3,5)=2v_1+3v_2$.

Now try $(2,3,4)$. The same first two entries force $c_1=2$, $c_2=3$, but then the third entry would be $5\neq4$. So $(2,3,4)$ is **not** in the span. The span is a plane, and this point lies just off it.

> [!question]- Check yourself
> 1. Describe the span of $(1,1)$ in $\mathbb R^2$.
> 2. Describe the span of $(1,0)$ and $(0,1)$.
> 3. Describe the span of $(1,2,3)$ and $(-2,-4,-6)$.
>
> **Answers.** 1. The diagonal line $y=x$. 2. All of $\mathbb R^2$: $(a,b)=a(1,0)+b(0,1)$. 3. A line, because the second vector is $-2$ times the first.

---

## 1.6 Linear independence: spotting redundancy

### Motivation

In section 1.5, sometimes adding a vector made the span bigger and sometimes it did nothing. A vector that adds nothing is **redundant**: it can already be built from the others. We want a precise test for this.

### The definition

> [!note] Definition: linear independence
> Vectors $v_1,\dots,v_k$ are **linearly independent** if the only way to make the zero vector from them is to use all-zero weights:
> $$
> c_1v_1+\cdots+c_kv_k=0\quad\text{only when}\quad c_1=c_2=\cdots=c_k=0.
> $$
> Otherwise they are **linearly dependent**.

### Why this definition captures "no redundancy"

The definition looks strange at first: why talk about making **zero**? Here is the reasoning.

Suppose some vector is redundant, say $v_1=2v_2+5v_3$. Move everything to one side:

$$
v_1-2v_2-5v_3=0.
$$

That is a way to make zero with weights $(1,-2,-5)$, which are not all zero. So **redundancy produces a nonzero recipe for zero**.

It works the other way too. If $c_1v_1+\cdots+c_kv_k=0$ with, say, $c_1\neq0$, divide by $c_1$ and rearrange:

$$
v_1=-\frac{c_2}{c_1}v_2-\cdots-\frac{c_k}{c_1}v_k,
$$

so $v_1$ is built from the others: it is redundant.

So "some vector is redundant" and "zero can be made with nonzero weights" mean exactly the same thing. The zero-based definition is preferred because it treats all the vectors equally, and it turns the question into a system of equations we can solve.

### How to test for independence

1. Write $c_1v_1+\cdots+c_kv_k=0$.
2. Turn it into equations, one per entry.
3. Solve. If the **only** solution is all zeros, the vectors are independent. If any other solution exists, they are dependent.

**Worked example 1.9.** Are $(1,0)$ and $(1,1)$ independent?

$c_1(1,0)+c_2(1,1)=(c_1+c_2,\;c_2)=(0,0)$. The second entry gives $c_2=0$; then the first gives $c_1=0$. Only the zero solution: **independent**.

**Worked example 1.10.** Are $(1,2)$ and $(2,4)$ independent?

$(2,4)=2(1,2)$, so $2(1,2)-1(2,4)=(0,0)$ with weights $(2,-1)$. A nonzero recipe for zero exists: **dependent**.

**Worked example 1.11.** Are $u=(1,0,1)$, $v=(0,1,1)$, $w=(1,1,2)$ independent?

Set $c_1u+c_2v+c_3w=0$:

$$
\begin{aligned}
c_1+c_3&=0\quad\text{(entry 1)}\\
c_2+c_3&=0\quad\text{(entry 2)}\\
c_1+c_2+2c_3&=0\quad\text{(entry 3)}
\end{aligned}
$$

From the first two, $c_1=-c_3$ and $c_2=-c_3$. Substitute into the third: $-c_3-c_3+2c_3=0$, which is $0=0$, always true. So $c_3$ can be anything. Take $c_3=1$: then $c_1=c_2=-1$, and indeed $-u-v+w=0$, that is $w=u+v$. **Dependent.**

### Quick tests you can do in your head

- **Two vectors** are dependent exactly when one is a multiple of the other.
- **Any set containing the zero vector** is dependent: $1\cdot0=0$ is a nonzero recipe.
- **Too many vectors**: more than $n$ vectors in $\mathbb R^n$ are always dependent. For example, any 3 vectors in $\mathbb R^2$ are dependent. (Chapter 5 proves this.)

> [!warning] Independence is about the whole set
> Three vectors can be dependent even when no two of them are multiples of each other, as example 1.11 shows. Checking pairs is not enough.

> [!question]- Check yourself
> 1. Are $(2,0)$ and $(0,3)$ independent?
> 2. Are $(1,2,3)$, $(0,0,0)$, $(4,5,6)$ independent?
> 3. Without calculating, are $(1,2)$, $(3,1)$, $(5,5)$ independent?
>
> **Answers.** 1. Yes: neither is a multiple of the other. 2. No: the set contains the zero vector. 3. No: three vectors in $\mathbb R^2$ are always dependent. (In fact $(5,5)=(1,2)\cdot2+(3,1)\cdot1$.)

---

## 1.7 The standard basis

In $\mathbb R^3$ there are three especially simple vectors:

$$
e_1=\begin{bmatrix}1\\0\\0\end{bmatrix},\qquad e_2=\begin{bmatrix}0\\1\\0\end{bmatrix},\qquad e_3=\begin{bmatrix}0\\0\\1\end{bmatrix}.
$$

Each has a single 1 and zeros elsewhere. They point along the $x$, $y$ and $z$ axes.

Every vector is a combination of them, and the weights are just its entries:

$$
\begin{bmatrix}4\\-2\\7\end{bmatrix}=4e_1-2e_2+7e_3.
$$

They have two properties:

1. **They span $\mathbb R^3$**: everything can be built.
2. **They are independent**: none can be built from the other two.

A set with both properties is called a **basis**. Spanning means "enough vectors"; independence means "no wasted vectors". So a basis is a minimal, complete set of building blocks.

The standard basis is not the only basis. $(1,1)$ and $(1,-1)$ also form a basis of $\mathbb R^2$. Choosing a clever basis is often the key to solving a problem, and that is the subject of [[LA 11 Change of Basis]].

---

## Summary

| Idea | Meaning | How to compute or test |
|---|---|---|
| vector | ordered list of numbers | write as a column |
| addition | walk one, then the other | add matching entries |
| scaling | stretch, shrink or flip | multiply every entry |
| linear combination | scale, then add | $c_1v_1+\cdots+c_kv_k$ |
| finding weights | which recipe makes $b$? | match entries, solve the equations |
| span | everything you can build | a line, plane, ... through the origin |
| independent | no redundant vector | only the zero recipe makes $0$ |
| basis | spans, and independent | e.g. $e_1,\dots,e_n$ |

**Three facts to remember:**

1. A vector equation is a system of ordinary equations, one per entry.
2. A span always passes through the origin.
3. Redundancy means a nonzero recipe for the zero vector.

---

## Exercises

Work in order. Part A builds fluency, B builds understanding, C asks for short proofs, D connects to code. Try every question before opening its solution.

### Part A: warm-up

**A1.** Compute $(2,-1,4)+(3,3,-1)$.

**A2.** Compute $-2(1,0,-3)+4(0,1,1)$.

**A3.** Find $x$ and $y$ if $\begin{bmatrix}2x\\x+y\end{bmatrix}=\begin{bmatrix}6\\10\end{bmatrix}$.

**A4.** A robot hand is at $(0.30,\,0.10,\,0.25)$ metres and must move to $(0.45,\,0.10,\,0.05)$. What displacement vector does it need?

**A5.** Simplify $3(u-v)+2(v+w)-u$.

> [!success]- Solutions to Part A
> **A1.** $(5,2,3)$.
>
> **A2.** $(-2,0,6)+(0,4,4)=(-2,4,10)$.
>
> **A3.** $2x=6$ gives $x=3$. Then $3+y=10$ gives $y=7$.
>
> **A4.** Target minus start: $(0.15,\,0,\,-0.20)$. Move 15 cm in $x$ and 20 cm down in $z$.
>
> **A5.** $3u-3v+2v+2w-u=2u-v+2w$.

### Part B: core

**B1.** Write $(7,4)$ as a linear combination of $(1,2)$ and $(3,0)$.

**B2.** Is $(1,1,1)$ in the span of $(1,0,1)$ and $(0,1,0)$? If so, give the weights.

**B3.** Is $(1,2,4)$ in the span of $(1,0,1)$ and $(0,1,1)$?

**B4.** Decide whether each set is independent:
(a) $(3,6),\ (1,2)$
(b) $(1,0,0),\ (1,1,0),\ (1,1,1)$
(c) $(1,2,0),\ (0,1,1),\ (1,3,1)$

**B5.** For which value of $k$ are $(1,k)$ and $(2,6)$ dependent?

**B6.** Describe geometrically the span of $(1,0,0)$ and $(0,0,1)$ in $\mathbb R^3$.

**B7.** Give three different vectors in the span of $(1,2,-1)$ and $(0,1,1)$.

> [!success]- Solutions to Part B
> **B1.** $c_1(1,2)+c_2(3,0)=(c_1+3c_2,\;2c_1)$. Matching: $2c_1=4$ so $c_1=2$; then $2+3c_2=7$ so $c_2=5/3$. Check: $(2,4)+(5,0)=(7,4)$.
>
> **B2.** $c_1(1,0,1)+c_2(0,1,0)=(c_1,\;c_2,\;c_1)$. Need $c_1=1$, $c_2=1$, and third entry $c_1=1$. Consistent, so yes: $(1,1,1)=1\cdot(1,0,1)+1\cdot(0,1,0)$.
>
> **B3.** Combinations look like $(c_1,\;c_2,\;c_1+c_2)$. Matching the first two entries gives $c_1=1$, $c_2=2$, so the third would be $3$, not $4$. Not in the span.
>
> **B4.**
> (a) Dependent: $(3,6)=3(1,2)$.
> (b) Independent. Set $c_1(1,0,0)+c_2(1,1,0)+c_3(1,1,1)=0$. The third entry gives $c_3=0$, the second then gives $c_2=0$, the first gives $c_1=0$.
> (c) Dependent: $(1,2,0)+(0,1,1)=(1,3,1)$.
>
> **B5.** Dependent when $(1,k)$ is a multiple of $(2,6)$. Since $(2,6)=2(1,3)$, we need $k=3$.
>
> **B6.** All vectors $(a,0,b)$: the $xz$-plane (the plane $y=0$).
>
> **B7.** Any choices of weights work. For example $(0,0,0)$ (both weights zero), $(1,2,-1)$ (weights $1,0$), $(1,3,0)$ (weights $1,1$).

### Part C: explain and prove

**C1.** Prove that $c(u+v)=cu+cv$ for vectors in $\mathbb R^n$.

**C2.** Prove that any set of vectors containing the zero vector is linearly dependent.

**C3.** Suppose $u$ and $v$ are independent. Prove that $u+v$ and $u-v$ are also independent.

**C4.** Explain in your own words why the span of any set of vectors must contain the origin, and why the line $y=2x+1$ is therefore not a span.

**C5.** True or false, with a reason: "If $v_3$ is not a multiple of $v_1$, and not a multiple of $v_2$, then $v_1,v_2,v_3$ are independent."

> [!success]- Solutions to Part C
> **C1.** Entry $i$ of the left side is $c(u_i+v_i)$. Entry $i$ of the right side is $cu_i+cv_i$. These are equal by the distributive law for real numbers. Since every entry agrees, the vectors are equal.
>
> **C2.** Suppose the set is $\{0,v_2,\dots,v_k\}$. Then $1\cdot0+0\cdot v_2+\cdots+0\cdot v_k=0$. The weights $(1,0,\dots,0)$ are not all zero, so this is a nonzero recipe for zero. By definition the set is dependent.
>
> **C3.** Suppose $a(u+v)+b(u-v)=0$. Rearranging gives $(a+b)u+(a-b)v=0$. Since $u,v$ are independent, both weights must be zero: $a+b=0$ and $a-b=0$. Adding gives $2a=0$, so $a=0$, and then $b=0$. Only the zero recipe works, so $u+v$ and $u-v$ are independent.
>
> **C4.** Choosing every weight equal to zero always gives the zero vector, so $0$ is in every span. The line $y=2x+1$ does not contain $(0,0)$, because at $x=0$ it has $y=1$. So it cannot be a span.
>
> **C5.** False. Example 1.11: $w=(1,1,2)$ is not a multiple of $u=(1,0,1)$ or of $v=(0,1,1)$, yet $w=u+v$, so the set is dependent. Independence is a property of the whole set, not of pairs.

### Part D: practise with code

Use Python with NumPy (`import numpy as np`).

**D1.** Create `u = np.array([3, 1])` and `v = np.array([-1, 2])`. Compute `u + v`, `2 * u`, and `u - v`, and check them against your hand calculations from this chapter.

**D2.** Write a function `combo(weights, vectors)` that returns the linear combination $\sum_ic_iv_i$. Test it on worked example 1.4.

**D3.** Generate 1000 random weight pairs `c1, c2` from $[-2,2]$, compute `c1 * (1, 0, 1) + c2 * (0, 1, 1)`, and plot the points in 3-D with Matplotlib. What shape do you see, and which section explains it?

**D4.** NumPy can test independence with `np.linalg.matrix_rank`. Put vectors as columns of a matrix (`np.column_stack([u, v, w])`). If the rank equals the number of vectors, they are independent. Test the three sets in exercise B4.

> [!success]- Hints for Part D
> **D2.** `return sum(c * np.array(v) for c, v in zip(weights, vectors))`.
>
> **D3.** You should see a flat sheet: the plane spanned by the two vectors (section 1.5). Use `ax = plt.figure().add_subplot(projection="3d")` and `ax.scatter(x, y, z)`.
>
> **D4.** Expected ranks: (a) 1 of 2, dependent. (b) 3 of 3, independent. (c) 2 of 3, dependent. Rank is explained fully in [[LA 05 Subspaces Basis and Rank]].

---

## Where this is used

- **Robot configurations.** A robot's joint angles form a vector $q$; a motion is a displacement $q_{\text{target}}-q_{\text{now}}$ ([[02 Geometry and Kinematics]]).
- **Neural networks.** The output of a linear layer is a linear combination of its weight columns, with the inputs as weights ([[05 Training Neural Policies]]).
- **Data.** If one feature in a dataset is a combination of others (for example "total = part A + part B"), the features are dependent, and a regression has no unique answer. Chapter 6 deals with this.

Next: [[LA 02 Dot Product Length and Angle]], where we measure lengths and angles between vectors.

---
type: course-chapter
course: linear-algebra
chapter: 2
tags: [mathematics, linear-algebra]
---

# Chapter 2: Dot product, length and angle

Previous: [[LA 01 Vectors and Linear Combinations]] | [[LA 00 Course Map]] | Next: [[LA 03 Matrices as Linear Maps]]

> [!abstract] The big idea
> The **dot product** takes two vectors and returns one number that measures **how much they point the same way**. From that single operation you get length, distance, angle, perpendicularity and projection.

> [!info] In this chapter you will learn to
> 1. Compute a dot product, and know its algebraic rules.
> 2. Compute the length of a vector and the distance between two points.
> 3. Find the angle between two vectors, and test whether they are perpendicular.
> 4. Use cosine similarity to compare directions.
> 5. Project one vector onto another, and explain why the formula works.

> [!tip] Before you start
> You need vectors, addition and scaling from [[LA 01 Vectors and Linear Combinations]]. You also need two facts from school geometry: **Pythagoras' theorem** ($a^2+b^2=c^2$ for a right triangle) and the meaning of **cosine** ($\cos0^\circ=1$, $\cos90^\circ=0$, $\cos180^\circ=-1$).

---

## 2.1 The dot product

### Why we need it

Chapter 1 gave us ways to *build* vectors. It said nothing about *measuring* them. How long is a vector? Do two vectors point in similar directions? Are they at right angles? All of these questions are answered by one tool.

### The definition

> [!note] Definition: dot product
> For two vectors of the same size, $u,v\in\mathbb R^n$,
> $$
> u\cdot v=u_1v_1+u_2v_2+\cdots+u_nv_n=\sum_{i=1}^nu_iv_i.
> $$
> Multiply matching entries, then add everything up.

You will also see it written $u^\top v$ (a row times a column, explained in chapter 3) or $\langle u,v\rangle$. All three notations mean the same thing.

> [!important] The result is a number, not a vector
> Adding vectors gives a vector. Scaling gives a vector. The dot product gives a **single number** (a scalar). This is the first operation in the course that does that.

**Worked example 2.1.**

$$
\begin{bmatrix}1\\2\\3\end{bmatrix}\cdot\begin{bmatrix}4\\-5\\6\end{bmatrix}=(1)(4)+(2)(-5)+(3)(6)=4-10+18=12.
$$

**Worked example 2.2.**

$$
(3,4)\cdot(4,-3)=12-12=0.
$$

Keep that zero in mind. It turns out to mean these two vectors are at right angles (section 2.4).

**Worked example 2.3: a dot product as a weighted total.** You buy 3 apples at 0.50, 2 loaves at 1.20 and 5 eggs at 0.25. Put the quantities in $q=(3,2,5)$ and the prices in $p=(0.50,1.20,0.25)$. The total bill is

$$
q\cdot p=1.50+2.40+1.25=5.15.
$$

This is the most common everyday reading: **a dot product is a weighted sum**. One vector holds amounts; the other holds what each amount is worth.

### Rules

Each of these comes straight from the definition by looking at the sum term by term.

| Rule | Formula | Why |
|---|---|---|
| symmetric | $u\cdot v=v\cdot u$ | $u_iv_i=v_iu_i$ |
| distributive | $u\cdot(v+w)=u\cdot v+u\cdot w$ | $u_i(v_i+w_i)=u_iv_i+u_iw_i$ |
| scalars come out | $(cu)\cdot v=c\,(u\cdot v)$ | $(cu_i)v_i=c(u_iv_i)$ |
| positive | $v\cdot v\ge0$, and $=0$ only if $v=0$ | $v\cdot v=\sum v_i^2$, a sum of squares |

These let you expand dot products like ordinary brackets:

$$
(u+v)\cdot(u+v)=u\cdot u+2\,u\cdot v+v\cdot v.
$$

This expansion is used in the proof in section 2.3, so make sure you can derive it: distribute the left bracket over the right, giving $u\cdot u+u\cdot v+v\cdot u+v\cdot v$, then use symmetry to combine the middle terms.

> [!question]- Check yourself
> 1. Compute $(2,0,-1)\cdot(3,5,4)$.
> 2. Compute $(1,1,1,1)\cdot(a,b,c,d)$. What does it represent?
> 3. Expand $(u-v)\cdot(u-v)$.
>
> **Answers.** 1. $6+0-4=2$. 2. $a+b+c+d$: the sum of the entries. 3. $u\cdot u-2\,u\cdot v+v\cdot v$.

---

## 2.2 Length and distance

### Length from Pythagoras

How long is the arrow $v=(3,4)$? It goes 3 across and 4 up. Those two moves are the two short sides of a right triangle, and the arrow is the long side. By Pythagoras,

$$
\text{length}=\sqrt{3^2+4^2}=\sqrt{25}=5.
$$

Notice that $3^2+4^2$ is exactly $v\cdot v$. That is no accident.

> [!note] Definition: length (norm)
> The **length** or **norm** of $v\in\mathbb R^n$ is
> $$
> \|v\|=\sqrt{v\cdot v}=\sqrt{v_1^2+v_2^2+\cdots+v_n^2}.
> $$

The double bars $\|v\|$ distinguish it from the absolute value $|x|$ of a single number, although for a 1-entry vector the two agree.

**In 3-D**, Pythagoras is used twice. For $v=(1,2,2)$: the floor diagonal under the arrow has length $\sqrt{1^2+2^2}=\sqrt5$. The arrow rises 2 above the end of that diagonal, so its length is $\sqrt{(\sqrt5)^2+2^2}=\sqrt{1+4+4}=3$. The formula just adds all the squares at once, in any dimension.

**Worked example 2.4.** $\|(2,-1,2)\|=\sqrt{4+1+4}=3$.

**Worked example 2.5.** $\|(1,1,1,1)\|=\sqrt4=2$. In $\mathbb R^n$, the all-ones vector has length $\sqrt n$, which grows with dimension. This is one reason distances behave strangely in very high dimensions.

### Scaling and length

Scaling a vector by $c$ scales its length by $|c|$:

$$
\|cv\|=|c|\,\|v\|.
$$

*Why:* $\|cv\|=\sqrt{\sum(cv_i)^2}=\sqrt{c^2\sum v_i^2}=|c|\sqrt{\sum v_i^2}$. The absolute value appears because $\sqrt{c^2}=|c|$; a negative scale flips direction but cannot make a length negative.

### Unit vectors

> [!note] Definition: unit vector
> A **unit vector** has length 1. To turn any nonzero $v$ into a unit vector pointing the same way, divide by its length:
> $$
> \hat v=\frac{v}{\|v\|}.
> $$
> This is called **normalizing** $v$.

**Worked example 2.6.** $v=(3,4)$, $\|v\|=5$, so $\hat v=(0.6,0.8)$. Check: $0.36+0.64=1$.

Unit vectors describe **pure direction**, with the size stripped away. A robot "approach direction" or a camera's viewing direction is a unit vector.

### Distance

The distance between two points $u$ and $v$ is the length of the arrow joining them, which (chapter 1) is $u-v$:

$$
\operatorname{dist}(u,v)=\|u-v\|.
$$

**Worked example 2.7.** Points $(1,2,3)$ and $(4,6,3)$: difference $(-3,-4,0)$, distance $\sqrt{9+16+0}=5$.

> [!question]- Check yourself
> 1. Find $\|(1,-2,2)\|$ and the unit vector in its direction.
> 2. If $\|v\|=4$, what is $\|-3v\|$?
> 3. Distance between $(0,0)$ and $(5,12)$?
>
> **Answers.** 1. $3$; $(1/3,-2/3,2/3)$. 2. $12$. 3. $\sqrt{25+144}=13$.

---

## 2.3 The angle between two vectors

### The key formula

> [!important] Geometric meaning of the dot product
> $$
> u\cdot v=\|u\|\,\|v\|\cos\theta,
> $$
> where $\theta$ is the angle between the two arrows (between $0^\circ$ and $180^\circ$).

Read it as: **the dot product is the product of the lengths, multiplied by a factor that measures alignment.** That factor, $\cos\theta$, is 1 when the vectors point the same way and shrinks as they turn apart.

Rearranged, it gives a way to compute angles:

$$
\cos\theta=\frac{u\cdot v}{\|u\|\,\|v\|}.
$$

### Why the formula is true

This proof uses only the dot product rules from section 2.1 and the **law of cosines** from trigonometry. The law of cosines says that in a triangle with sides $a$, $b$, $c$, where $\theta$ is the angle between sides $a$ and $b$:

$$
c^2=a^2+b^2-2ab\cos\theta.
$$

(When $\theta=90^\circ$, $\cos\theta=0$ and this is Pythagoras.)

*Step 1: draw the triangle.* Put $u$ and $v$ tail to tail at the origin. The third side joins their tips, and from chapter 1 that side is $u-v$.

*Step 2: apply the law of cosines* with $a=\|u\|$, $b=\|v\|$, $c=\|u-v\|$:

$$
\|u-v\|^2=\|u\|^2+\|v\|^2-2\|u\|\|v\|\cos\theta.
$$

*Step 3: expand the left side with dot products.* Since $\|w\|^2=w\cdot w$,

$$
\|u-v\|^2=(u-v)\cdot(u-v)=u\cdot u-2\,u\cdot v+v\cdot v=\|u\|^2-2\,u\cdot v+\|v\|^2.
$$

*Step 4: compare.* Both lines equal $\|u-v\|^2$. Cancel $\|u\|^2+\|v\|^2$ from both, then divide by $-2$:

$$
u\cdot v=\|u\|\|v\|\cos\theta.\qquad\blacksquare
$$

### Reading the sign of a dot product

Lengths are always positive, so the **sign** of $u\cdot v$ is the sign of $\cos\theta$:

| $u\cdot v$ | Angle | Meaning |
|---|---|---|
| positive | less than $90^\circ$ | roughly the same direction |
| zero | exactly $90^\circ$ | perpendicular |
| negative | more than $90^\circ$ | roughly opposite directions |

**Worked example 2.8.** Angle between $u=(1,0)$ and $v=(1,1)$:

- $u\cdot v=1$
- $\|u\|=1$, $\|v\|=\sqrt2$
- $\cos\theta=\dfrac1{\sqrt2}\approx0.707$, so $\theta=45^\circ$.

That matches the picture: $(1,1)$ points along the diagonal, halfway between the axes.

**Worked example 2.9.** Angle between $u=(1,2,2)$ and $v=(2,-1,2)$:

- $u\cdot v=2-2+4=4$
- $\|u\|=3$, $\|v\|=3$
- $\cos\theta=4/9\approx0.444$, so $\theta\approx63.6^\circ$.

**Worked example 2.10.** Angle between $(1,1)$ and $(-1,-1)$: dot product $-2$, lengths $\sqrt2$ each, $\cos\theta=-2/2=-1$, so $\theta=180^\circ$. Exactly opposite, as expected.

> [!question]- Check yourself
> 1. Find the angle between $(1,0,0)$ and $(0,1,0)$.
> 2. Two vectors have lengths 2 and 5 and dot product $-5$. What is the angle?
> 3. Without computing an angle, is the angle between $(3,-1)$ and $(1,4)$ acute or obtuse?
>
> **Answers.** 1. Dot product 0, so $90^\circ$. 2. $\cos\theta=-5/10=-0.5$, so $120^\circ$. 3. Dot product $3-4=-1<0$: obtuse.

---

## 2.4 Perpendicular (orthogonal) vectors

> [!note] Definition: orthogonal
> Two vectors $u$ and $v$ are **orthogonal** (perpendicular) when
> $$
> u\cdot v=0.
> $$

In 2-D and 3-D this matches the usual right angle, because $\cos90^\circ=0$. In higher dimensions there is no picture, so this equation **is** the definition. That is a common pattern in linear algebra: a geometric idea from 2-D becomes an algebraic definition that works everywhere.

By this definition the zero vector is orthogonal to every vector. That is a harmless convention.

**Worked example 2.11.** Find all vectors orthogonal to $(2,3)$. We need $(x,y)$ with $2x+3y=0$, that is $y=-\tfrac23x$. All multiples of $(3,-2)$ work. In 2-D, the perpendicular directions to a given vector form a line.

**Worked example 2.12.** Find $k$ so that $(1,k,2)$ is orthogonal to $(3,1,-1)$. We need $3+k-2=0$, so $k=-1$.

**Worked example 2.13: a useful trick.** In 2-D, $(a,b)$ is always orthogonal to $(-b,a)$, since $-ab+ab=0$. Swapping entries and negating one rotates a vector by $90^\circ$.

### Pythagoras in any dimension

If $u$ and $v$ are orthogonal, the cross term in the expansion vanishes:

$$
\|u+v\|^2=\|u\|^2+2\,u\cdot v+\|v\|^2=\|u\|^2+\|v\|^2.
$$

That is Pythagoras' theorem, now proved in any number of dimensions. It will be the key step in least squares ([[LA 06 Orthogonality and Least Squares]]).

> [!question]- Check yourself
> 1. Are $(1,2,-1)$ and $(3,-1,1)$ orthogonal?
> 2. Give a nonzero vector orthogonal to $(5,2)$.
> 3. If $u\perp v$, $\|u\|=6$ and $\|v\|=8$, what is $\|u+v\|$?
>
> **Answers.** 1. $3-2-1=0$. Yes. 2. $(-2,5)$ (or any multiple). 3. $\sqrt{36+64}=10$.

---

## 2.5 Cosine similarity

Sometimes you care only about **direction**, not size. Two documents might use the same words in the same proportions, but one is twice as long. Two camera images might show the same scene at different brightness.

Divide out the lengths and you get a pure alignment score:

> [!note] Definition: cosine similarity
> $$
> \operatorname{sim}(u,v)=\frac{u\cdot v}{\|u\|\,\|v\|}=\cos\theta,\qquad-1\le\operatorname{sim}(u,v)\le1.
> $$

| Value | Meaning |
|---|---|
| $1$ | identical direction |
| $0$ | unrelated (perpendicular) |
| $-1$ | opposite direction |

**Worked example 2.14.** Word counts for the words (robot, learning, cake): document A $=(4,2,0)$, document B $=(2,1,0)$, document C $=(0,1,5)$.

- $\operatorname{sim}(A,B)=\dfrac{8+2}{\sqrt{20}\sqrt5}=\dfrac{10}{10}=1$. Same topic; B is just shorter.
- $\operatorname{sim}(A,C)=\dfrac{0+2+0}{\sqrt{20}\sqrt{26}}\approx0.088$. Almost unrelated.

### Why it is always between $-1$ and $1$

That fact is the **Cauchy-Schwarz inequality**:

$$
|u\cdot v|\le\|u\|\,\|v\|.
$$

In 2-D and 3-D it follows from $|\cos\theta|\le1$. In general, here is a proof that does not need angles.

*Proof.* If $v=0$ both sides are 0. Otherwise, for every real number $t$, the length squared of $u-tv$ cannot be negative:

$$
0\le\|u-tv\|^2=\|u\|^2-2t\,(u\cdot v)+t^2\|v\|^2.
$$

The right side is a quadratic in $t$ that never goes below zero. Choose the $t$ at its minimum, $t=\dfrac{u\cdot v}{\|v\|^2}$. Substituting:

$$
0\le\|u\|^2-\frac{(u\cdot v)^2}{\|v\|^2}.
$$

Multiply by $\|v\|^2$ and rearrange: $(u\cdot v)^2\le\|u\|^2\|v\|^2$. Take square roots. $\blacksquare$

Equality holds exactly when $u-tv=0$, that is when $u$ and $v$ lie on the same line.

### The triangle inequality

A close relative:

$$
\|u+v\|\le\|u\|+\|v\|.
$$

*In words:* walking along $u$ then $v$ can never be shorter than going straight to the end. *Proof:* $\|u+v\|^2=\|u\|^2+2u\cdot v+\|v\|^2\le\|u\|^2+2\|u\|\|v\|+\|v\|^2=(\|u\|+\|v\|)^2$, using Cauchy-Schwarz in the middle step.

---

## 2.6 Projection: the shadow of one vector on another

### The question

How much of $b$ points in the direction of $a$? Imagine light shining straight down onto the line through $a$. The **shadow** that $b$ casts on that line is the **projection** of $b$ onto $a$.

```
            b
           /|
          / |
         /  |  e = b - p   (perpendicular to a)
        /   |
       /    |
 -----●-----●---------> a
   origin   p  (projection)
```

### Deriving the formula

We do not memorize this formula; we build it from one idea.

*Step 1.* The shadow lies on the line through $a$, so it is a multiple of $a$:

$$
p=c\,a\quad\text{for some number }c.
$$

*Step 2.* The leftover piece $e=b-p$ (the "error", from the tip of the shadow up to $b$) must be **perpendicular** to $a$. That is what "shining straight down" means:

$$
a\cdot(b-ca)=0.
$$

*Step 3.* Expand using the dot product rules:

$$
a\cdot b-c\,(a\cdot a)=0\quad\Longrightarrow\quad c=\frac{a\cdot b}{a\cdot a}.
$$

*Step 4.* So:

> [!note] Projection formula
> $$
> p=\operatorname{proj}_a(b)=\frac{a\cdot b}{a\cdot a}\,a.
> $$
> If $a$ is a unit vector, $a\cdot a=1$ and this simplifies to $p=(a\cdot b)\,a$.

The last line says something important: **dotting with a unit vector measures how far you go in that direction.** $a\cdot b$ is the signed length of the shadow.

### Worked examples

**Worked example 2.15.** Project $b=(2,3)$ onto $a=(1,0)$.

- $a\cdot b=2$, $a\cdot a=1$, so $c=2$ and $p=(2,0)$.
- Leftover $e=b-p=(0,3)$. Check: $e\cdot a=0$. ✓

That matches intuition: the shadow on the horizontal axis keeps only the horizontal part.

**Worked example 2.16.** Project $b=(1,2)$ onto $a=(1,1)$.

- $a\cdot b=3$, $a\cdot a=2$, so $c=1.5$ and $p=(1.5,1.5)$.
- Leftover $e=(1,2)-(1.5,1.5)=(-0.5,0.5)$.
- Check: $e\cdot a=-0.5+0.5=0$. ✓

So $b$ splits into two perpendicular pieces: $(1.5,1.5)$ along $a$ and $(-0.5,0.5)$ across it.

**Worked example 2.17: a physical reading.** A force $F=(3,4)$ newtons pushes a cart that can only roll along the unit direction $d=(1,0)$. Only the component along the track does useful work: $F\cdot d=3$ newtons. The 4 newtons pushing sideways do nothing to move the cart. Work done over a displacement $s$ is exactly $F\cdot s$.

### Splitting any vector into two perpendicular parts

Projection always splits $b$ into

$$
b=\underbrace{p}_{\text{along }a}+\underbrace{e}_{\text{perpendicular to }a}.
$$

And because $p\perp e$, Pythagoras (section 2.4) gives $\|b\|^2=\|p\|^2+\|e\|^2$. In example 2.16: $\|b\|^2=5$, $\|p\|^2=4.5$, $\|e\|^2=0.5$. ✓

### Why this matters later

$p$ is the point on the line through $a$ that is **closest** to $b$. Any other point $ca$ on the line is further away, by Pythagoras again. Hold on to this: least squares in chapter 6 is this exact argument, with a whole plane (or higher-dimensional space) in place of the line.

> [!question]- Check yourself
> 1. Project $(4,2)$ onto $(1,1)$.
> 2. Project $(0,5)$ onto $(3,4)$.
> 3. What is the projection of $b$ onto $a$ if $b\perp a$?
>
> **Answers.** 1. $c=6/2=3$, $p=(3,3)$. 2. $c=20/25=0.8$, $p=(2.4,3.2)$. 3. The zero vector, since $a\cdot b=0$.

---

## Summary

| Idea | Formula | Remember it as |
|---|---|---|
| dot product | $u\cdot v=\sum u_iv_i$ | multiply matching entries, add |
| length | $\|v\|=\sqrt{v\cdot v}$ | Pythagoras |
| unit vector | $v/\|v\|$ | direction only |
| distance | $\|u-v\|$ | length of the gap |
| angle | $\cos\theta=\dfrac{u\cdot v}{\|u\|\|v\|}$ | alignment score |
| orthogonal | $u\cdot v=0$ | right angle |
| projection | $\dfrac{a\cdot b}{a\cdot a}a$ | shadow; leftover is perpendicular |

**Three facts to remember:**

1. A dot product is one number: a weighted sum, and an alignment score.
2. Zero dot product means perpendicular, in any dimension.
3. Projection is found by demanding that the leftover is perpendicular.

---

## Exercises

### Part A: warm-up

**A1.** Compute $(1,-2,3)\cdot(4,0,-1)$.

**A2.** Find the length of $(2,3,6)$ and the unit vector in its direction.

**A3.** Find the distance between $(1,1,1)$ and $(3,-1,2)$.

**A4.** Find the angle between $(1,1,0)$ and $(0,1,1)$.

**A5.** Are $(2,-1,3)$ and $(1,5,1)$ orthogonal?

> [!success]- Solutions to Part A
> **A1.** $4+0-3=1$.
>
> **A2.** $\sqrt{4+9+36}=7$. Unit vector $(2/7,3/7,6/7)$.
>
> **A3.** Difference $(2,-2,1)$; distance $\sqrt{4+4+1}=3$.
>
> **A4.** Dot product $1$, lengths $\sqrt2$ each, $\cos\theta=1/2$, so $\theta=60^\circ$.
>
> **A5.** $2-5+3=0$. Yes.

### Part B: core

**B1.** Find all values of $k$ for which $(k,2,1)$ and $(k,-k,3)$ are orthogonal.

**B2.** Find a unit vector orthogonal to both $(1,0,1)$ and $(0,1,1)$.

**B3.** Project $b=(3,1,2)$ onto $a=(1,1,1)$. Write $b$ as the sum of a part along $a$ and a part perpendicular to $a$, and check that the second part really is perpendicular.

**B4.** A robot gripper approaches along the unit direction $d=(0,0,-1)$ (straight down). The object's surface normal is $n=(0,0.6,0.8)$. Find the angle between $-d$ and $n$. Is the approach close to head-on?

**B5.** Using cosine similarity, which of the vectors $(1,2,0)$, $(2,4,1)$, $(-1,-2,0)$ is most similar in direction to $(3,6,0)$? Which is least similar?

**B6.** Show by example that $u\cdot v=u\cdot w$ does **not** imply $v=w$. (So you cannot "cancel" $u$ from a dot product.)

> [!success]- Solutions to Part B
> **B1.** $k^2-2k+3=0$ has discriminant $4-12<0$. No real solutions: these vectors are never orthogonal.
>
> **B2.** Need $x+z=0$ and $y+z=0$. Take $z=1$: $x=y=-1$. So $(-1,-1,1)$, with length $\sqrt3$. Unit vector: $\dfrac1{\sqrt3}(-1,-1,1)$ (or its negative).
>
> **B3.** $c=6/3=2$, so $p=(2,2,2)$ and $e=(1,-1,0)$. Check: $e\cdot a=1-1+0=0$. So $b=(2,2,2)+(1,-1,0)$.
>
> **B4.** $-d=(0,0,1)$, and $(-d)\cdot n=0.8$, both unit vectors, so $\cos\theta=0.8$ and $\theta\approx36.9^\circ$. Not head-on; the approach is tilted about $37^\circ$ from the surface normal.
>
> **B5.** $(1,2,0)$ has similarity exactly 1 (it is a multiple). $(2,4,1)$: $\dfrac{30}{\sqrt{21}\sqrt{45}}\approx0.976$. $(-1,-2,0)$: $-1$, the least similar (opposite).
>
> **B6.** $u=(1,0)$, $v=(5,1)$, $w=(5,7)$. Then $u\cdot v=u\cdot w=5$ but $v\neq w$. The dot product only "sees" the part of $v$ along $u$.

### Part C: explain and prove

**C1.** Prove that $\|cv\|=|c|\,\|v\|$.

**C2.** Prove the **parallelogram law**: $\|u+v\|^2+\|u-v\|^2=2\|u\|^2+2\|v\|^2$. Describe what it says about the diagonals of a parallelogram.

**C3.** Prove that if $u$ is orthogonal to both $v$ and $w$, then $u$ is orthogonal to every linear combination $av+bw$.

**C4.** Explain why $\|u+v\|=\|u\|+\|v\|$ holds only when $u$ and $v$ point in the same direction (or one is zero).

**C5.** Using the projection formula, prove that the leftover $e=b-p$ is orthogonal to $a$. (That is, check the derivation works.)

> [!success]- Solutions to Part C
> **C1.** $\|cv\|^2=(cv)\cdot(cv)=c^2(v\cdot v)=c^2\|v\|^2$. Take square roots; $\sqrt{c^2}=|c|$.
>
> **C2.** Expand both: $\|u+v\|^2=\|u\|^2+2u\cdot v+\|v\|^2$ and $\|u-v\|^2=\|u\|^2-2u\cdot v+\|v\|^2$. Adding cancels the cross terms. In words: the squares of the two diagonals of a parallelogram add up to the squares of all four sides.
>
> **C3.** $u\cdot(av+bw)=a(u\cdot v)+b(u\cdot w)=a\cdot0+b\cdot0=0$. Consequence: a vector perpendicular to two vectors is perpendicular to the whole plane they span.
>
> **C4.** From the proof of the triangle inequality, equality requires $u\cdot v=\|u\|\|v\|$, so $\cos\theta=1$, that is $\theta=0$: the same direction. (If either is zero, both sides are equal trivially.)
>
> **C5.** $a\cdot e=a\cdot b-\dfrac{a\cdot b}{a\cdot a}(a\cdot a)=a\cdot b-a\cdot b=0$.

### Part D: practise with code

**D1.** In NumPy, `np.dot(u, v)` (or `u @ v`) computes a dot product and `np.linalg.norm(v)` a length. Recompute worked examples 2.1, 2.9 and 2.16.

**D2.** Write `angle_deg(u, v)` returning the angle in degrees. Use `np.clip` on the cosine before `np.arccos`. Why is the clip needed?

**D3.** Write `project(b, a)` and `perp(b, a)`. Test that `project(b, a) + perp(b, a)` equals `b` and that `perp(b, a) @ a` is (nearly) zero.

**D4 (high dimensions).** Draw two random vectors with 1000 entries each from a standard normal (`np.random.randn(1000)`). Compute their cosine similarity. Repeat 100 times and look at the values. What do you notice, and why might that be?

> [!success]- Hints for Part D
> **D2.** Rounding can push the computed cosine slightly outside $[-1,1]$, for example $1.0000000002$, and `arccos` then returns `nan`.
>
> **D4.** The similarities cluster tightly around 0. Random high-dimensional vectors are almost always nearly perpendicular, because the many independent positive and negative products in the sum cancel out. This is why cosine similarity between learned embeddings is informative: unrelated items score near 0 by default.

---

## Where this is used

- **Neurons.** A neuron computes $w\cdot x+b$: how well the input aligns with a learned direction $w$ ([[05 Training Neural Policies]]).
- **Attention.** Attention scores in transformers are dot products between "query" and "key" vectors ([[Appendix - Neural Networks and Attention]]).
- **Loss functions.** Mean squared error is a squared distance $\|y-\hat y\|^2$ divided by the number of entries.
- **Grasping.** Comparing an approach direction with a surface normal is a dot product between unit vectors.

Next: [[LA 03 Matrices as Linear Maps]], where we start transforming vectors.

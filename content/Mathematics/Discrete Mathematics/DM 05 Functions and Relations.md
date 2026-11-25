---
type: course-chapter
course: discrete-mathematics
chapter: 5
tags: [mathematics, discrete-mathematics, functions, relations]
---
# DM 05 Functions and relations

Previous: [[DM 04 Sets]] | [[DM 00 Course Map]] | Next: [[DM 06 Induction and Recursion]]

> [!abstract] One sentence
> A relation is any set of pairs connecting two sets; a function is the special relation that gives every input exactly one output, and the questions "can outputs collide?" and "is every target hit?" classify functions.

## Functions

A **function** $f:A\to B$ assigns to **each** element of $A$ **exactly one** element of $B$.

- $A$ is the **domain** (allowed inputs).
- $B$ is the **codomain** (declared type of the outputs).
- The **range** or **image** is the set of outputs actually produced: $\{f(a)\mid a\in A\}\subseteq B$.

Two requirements: every input has an output (nothing left out), and no input has two outputs (no ambiguity). Two different inputs sharing an output is allowed.

**Example.** $f:\mathbb Z\to\mathbb Z$, $f(n)=n^2$. Domain $\mathbb Z$, codomain $\mathbb Z$, range $\{0,1,4,9,\dots\}$.

A function is its domain, its codomain *and* its rule. $n\mapsto n^2$ from $\mathbb Z$ to $\mathbb Z$ and from $\mathbb N$ to $\mathbb N$ are different functions with different properties.

## Injective, surjective, bijective

**Injective (one-to-one):** different inputs give different outputs.

$$
f(a_1)=f(a_2)\;\Longrightarrow\;a_1=a_2.
$$

No collisions. You can recover the input from the output.

**Surjective (onto):** every element of the codomain is hit.

$$
\forall b\in B\;\exists a\in A\;\;f(a)=b.
$$

Range equals codomain.

**Bijective:** both. A perfect pairing between $A$ and $B$.

| $f$ | Injective? | Surjective? |
|---|---|---|
| $\mathbb Z\to\mathbb Z$, $n\mapsto n^2$ | no ($f(2)=f(-2)$) | no ($-1$ is never hit) |
| $\mathbb N\to\mathbb N$, $n\mapsto n^2$ | yes | no ($2$ is never hit) |
| $\mathbb Z\to\mathbb Z$, $n\mapsto2n$ | yes | no (odd numbers missed) |
| $\mathbb R\to\mathbb R$, $x\mapsto x^3$ | yes | yes: bijective |
| $\mathbb Z\to\{0,1\}$, $n\mapsto n\bmod2$ | no | yes |

**How to prove each.**

- Injective: assume $f(a_1)=f(a_2)$, deduce $a_1=a_2$.
- Surjective: take an arbitrary $b$, construct an $a$ with $f(a)=b$.
- Not injective: exhibit two inputs with equal outputs. Not surjective: exhibit a target that is never hit.

**Worked example.** $f:\mathbb R\to\mathbb R$, $f(x)=3x+2$. Injective: $3x_1+2=3x_2+2$ gives $x_1=x_2$. Surjective: given $y$, take $x=(y-2)/3$; then $f(x)=y$. So $f$ is a bijection.

**For finite sets, sizes constrain everything.**

- An injection $A\to B$ requires $|A|\le|B|$.
- A surjection requires $|A|\ge|B|$.
- A bijection requires $|A|=|B|$. This is the principle behind counting by correspondence ([[DM 07 Counting]]).

The first line, read backwards, is the **pigeonhole principle**: if $|A|>|B|$, no function $A\to B$ is injective, so some two inputs collide. Hash functions map a huge set to a small one, so collisions are unavoidable.

## Composition and inverse

Given $f:A\to B$ and $g:B\to C$, the **composition** $g\circ f:A\to C$ is

$$
(g\circ f)(a)=g(f(a)).
$$

$f$ acts first. Composition is associative but not commutative: with $f(x)=x+1$ and $g(x)=x^2$, $(g\circ f)(x)=(x+1)^2$ while $(f\circ g)(x)=x^2+1$. The same rule governed matrix products in [[LA 03 Matrices as Linear Maps]].

$f$ has an **inverse** $f^{-1}:B\to A$, with $f^{-1}(f(a))=a$ and $f(f^{-1}(b))=b$, **exactly when $f$ is bijective**. Injectivity makes the answer unambiguous; surjectivity makes it defined for every $b$.

In linear algebra: an $n\times n$ matrix is injective exactly when its null space is trivial, surjective exactly when its column space is everything, and for square matrices each implies the other ([[LA 05 Subspaces Basis and Rank]]).

## Relations

A **relation** $R$ from $A$ to $B$ is any subset of $A\times B$. Write $a\,R\,b$ when $(a,b)\in R$. A function is a relation with the "exactly one output" property; a general relation may relate an element to none, one or many.

A relation **on** $A$ is a subset of $A\times A$. Examples on the integers: $<$, $\le$, $=$, "divides", "has the same parity as".

A relation on a finite set can be drawn as a directed graph ([[DM 10 Graphs]]): an arrow from $a$ to $b$ whenever $a\,R\,b$.

## Properties of a relation on $A$

| Property | Definition | Example | Non-example |
|---|---|---|---|
| reflexive | $a\,R\,a$ for every $a$ | $\le$ | $<$ |
| symmetric | $a\,R\,b\Rightarrow b\,R\,a$ | "is a sibling of" | $\le$ |
| antisymmetric | $a\,R\,b$ and $b\,R\,a\Rightarrow a=b$ | $\le$ | "is a sibling of" |
| transitive | $a\,R\,b$ and $b\,R\,c\Rightarrow a\,R\,c$ | $<$ | "is a friend of" |

Antisymmetric is not the opposite of symmetric. Equality is both; "is a friend of" on some groups is neither.

## Equivalence relations

A relation that is **reflexive, symmetric and transitive** is an **equivalence relation**. It captures "the same in some respect".

**Examples.** Equality. "Has the same birthday as". "Has the same remainder when divided by 3" (congruence mod 3, [[DM 08 Number Theory and Modular Arithmetic]]). "Is similar to" for matrices ([[LA 11 Change of Basis]]).

The **equivalence class** of $a$ is everything equivalent to it:

$$
[a]=\{x\in A\mid x\,R\,a\}.
$$

> [!important] Equivalence relations and partitions are the same thing
> The equivalence classes of an equivalence relation partition $A$: every element is in exactly one class. Conversely, every partition defines an equivalence relation ("is in the same block as").

**Worked example.** Congruence mod 3 on $\mathbb Z$ has three classes:

$$
[0]=\{\dots,-3,0,3,6,\dots\},\quad[1]=\{\dots,-2,1,4,7,\dots\},\quad[2]=\{\dots,-1,2,5,8,\dots\}.
$$

They are disjoint and cover every integer.

**Checking the three properties** for "$a\sim b$ when $a-b$ is even": reflexive, since $a-a=0$ is even. Symmetric, since if $a-b$ is even so is $b-a$. Transitive, since $a-c=(a-b)+(b-c)$ is a sum of two even numbers. The classes are the evens and the odds.

Equivalence is how mathematics builds new objects: a rational number *is* an equivalence class of fractions ($\tfrac12=\tfrac24=\tfrac36$).

## Partial orders

A relation that is **reflexive, antisymmetric and transitive** is a **partial order**. It captures "comes before or equals".

**Examples.** $\le$ on numbers. $\subseteq$ on sets. "Divides" on positive integers. "Must be completed before" on tasks.

"Partial" because some pairs may be **incomparable**: neither $\{1\}\subseteq\{2\}$ nor $\{2\}\subseteq\{1\}$; neither $2\mid3$ nor $3\mid2$. If every pair is comparable it is a **total order**, like $\le$ on numbers.

A partial order on tasks ("put on socks before shoes") can always be extended to a total order that respects it. Finding one is **topological sorting**, used by build systems, package managers and course prerequisite planning ([[DM 11 Trees and Graph Algorithms]]).

## Common mistakes

- **Confusing codomain with range.** Surjectivity depends on the declared codomain.
- **Reading "one-to-one" as "one-to-one correspondence".** The first means injective; the second means bijective.
- **Checking a property on a few pairs** and concluding it holds for all.
- **Thinking symmetric and antisymmetric are opposites.**

## Learn by doing

1. Is $f:\mathbb R\to\mathbb R$, $f(x)=x^2+1$ injective? Surjective? What if the codomain is $[1,\infty)$ and the domain $[0,\infty)$?
2. With $f(x)=2x$ and $g(x)=x+3$, find $g\circ f$ and $f\circ g$.
3. On $\mathbb Z$, define $a\,R\,b$ when $a+b$ is even. Is $R$ an equivalence relation?
4. Is "divides" on $\{1,2,3,4,6,12\}$ a total order? Name two incomparable elements.

> [!success]- Check your answers
> 1. Neither: $f(1)=f(-1)$ and $0$ is never hit. With the restricted domain and codomain it becomes a bijection, with inverse $y\mapsto\sqrt{y-1}$.
> 2. $(g\circ f)(x)=2x+3$; $(f\circ g)(x)=2x+6$.
> 3. Yes. $a+a=2a$ is even; $a+b=b+a$; and if $a+b$ and $b+c$ are even then $a+c=(a+b)+(b+c)-2b$ is even. Classes: evens and odds.
> 4. No. $2$ and $3$ are incomparable (also $4$ and $6$).

## Where this shows up

A policy is a function from observations to actions; if two different states produce the same observation, the observation map is not injective and the state cannot be recovered from a single frame. That is partial observability ([[04 Perception and State]]). Task dependencies in a robot's plan form a partial order.

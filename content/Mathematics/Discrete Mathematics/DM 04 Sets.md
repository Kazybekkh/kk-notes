---
type: course-chapter
course: discrete-mathematics
chapter: 4
tags: [mathematics, discrete-mathematics, sets]
---
# DM 04 Sets

Previous: [[DM 03 Proof Techniques]] | [[DM 00 Course Map]] | Next: [[DM 05 Functions and Relations]]

> [!abstract] One sentence
> A set is an unordered collection of distinct objects, and the operations on sets mirror the connectives of logic exactly.

## What a set is

A **set** is a collection of objects, called its **elements**. Write $x\in A$ for "$x$ is an element of $A$" and $x\notin A$ otherwise.

Two things do not matter: **order** and **repetition**.

$$
\{1,2,3\}=\{3,1,2\}=\{1,1,2,3\}.
$$

A set is completely determined by which objects are in it. In Python this is `set`, as opposed to `list`.

## Describing sets

**Roster:** list the elements. $A=\{2,4,6,8\}$.

**Set-builder:** state a property.

$$
A=\{x\in\mathbb Z\mid x\text{ is even and }0<x<10\}.
$$

Read: "the set of integers $x$ such that $x$ is even and between 0 and 10". In Python: `{x for x in range(1, 10) if x % 2 == 0}`.

**Standard sets:**

| Symbol | Set |
|---|---|
| $\mathbb N$ | natural numbers $0,1,2,\dots$ (some books start at 1) |
| $\mathbb Z$ | integers |
| $\mathbb Q$ | rational numbers |
| $\mathbb R$ | real numbers |
| $\emptyset$ | the empty set, with no elements |

The **cardinality** $|A|$ is the number of elements. $|\{2,4,6,8\}|=4$ and $|\emptyset|=0$.

## Subsets

$A\subseteq B$ ("$A$ is a subset of $B$") means every element of $A$ is also in $B$:

$$
A\subseteq B\iff\forall x\,(x\in A\to x\in B).
$$

Facts:

- $\emptyset\subseteq A$ for every set $A$. (Vacuously true: there is no element of $\emptyset$ to fail the test.)
- $A\subseteq A$.
- $A=B$ exactly when $A\subseteq B$ and $B\subseteq A$. **This is how you prove two sets are equal:** show each is contained in the other.

> [!warning] $\in$ versus $\subseteq$
> $\in$ relates an element to a set; $\subseteq$ relates a set to a set. With $A=\{1,2,\{3\}\}$: $1\in A$, $\{1\}\subseteq A$, $\{3\}\in A$, but $3\notin A$. Also $\emptyset\neq\{\emptyset\}$: an empty box is not the same as a box containing an empty box.

## Operations

Let $U$ be the universe of discourse.

| Operation | Notation | Definition | Logic |
|---|---|---|---|
| union | $A\cup B$ | in $A$ or in $B$ | $\lor$ |
| intersection | $A\cap B$ | in $A$ and in $B$ | $\land$ |
| difference | $A\setminus B$ | in $A$ and not in $B$ | $\land\neg$ |
| complement | $A^c$ | not in $A$ (within $U$) | $\neg$ |
| symmetric difference | $A\triangle B$ | in exactly one | $\oplus$ |

**Example.** $A=\{1,2,3,4\}$, $B=\{3,4,5\}$, $U=\{1,\dots,6\}$.

$$
A\cup B=\{1,2,3,4,5\},\quad A\cap B=\{3,4\},\quad A\setminus B=\{1,2\},\quad A^c=\{5,6\},\quad A\triangle B=\{1,2,5\}.
$$

$A$ and $B$ are **disjoint** when $A\cap B=\emptyset$.

Venn diagrams (overlapping circles) are the right picture for two or three sets. Draw one whenever a set identity looks doubtful.

## Laws

Because set operations are defined by logical connectives, every logical law has a set version:

| Law | Statement |
|---|---|
| De Morgan | $(A\cup B)^c=A^c\cap B^c$ |
| De Morgan | $(A\cap B)^c=A^c\cup B^c$ |
| distributive | $A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$ |
| distributive | $A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$ |
| absorption | $A\cup(A\cap B)=A$ |
| difference | $A\setminus B=A\cap B^c$ |

**Worked proof** of the first De Morgan law, by showing both inclusions through a chain of equivalences:

$$
x\in(A\cup B)^c\iff\neg(x\in A\lor x\in B)\iff(x\notin A)\land(x\notin B)\iff x\in A^c\cap B^c.
$$

The middle step is De Morgan's law for propositions ([[DM 01 Logic and Propositions]]). Since each step is an "if and only if", both inclusions are proved at once.

## Counting elements: inclusion-exclusion

$$

|A\cup B|=|A|+|B|-|A\cap B|.
$$

Adding the sizes counts the overlap twice. For three sets:

$$

|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|.
$$

**Example.** How many integers from 1 to 100 are divisible by 2 or by 5? $50+20-10=60$, where 10 counts the multiples of 10.

The identical formula holds for probabilities ([[PS 01 Sample Spaces Events and Axioms]]).

## Power set

The **power set** $\mathcal P(A)$ is the set of all subsets of $A$.

$$
\mathcal P(\{a,b\})=\{\emptyset,\{a\},\{b\},\{a,b\}\}.
$$

If $|A|=n$ then $|\mathcal P(A)|=2^n$. Reason: to build a subset, make a yes/no decision for each of the $n$ elements. $2\times2\times\cdots\times2=2^n$ outcomes. This is the same as the $2^n$ rows of a truth table, and the $2^n$ bit strings of length $n$.

## Cartesian product

The **Cartesian product** $A\times B$ is the set of all **ordered pairs**:

$$
A\times B=\{(a,b)\mid a\in A,\;b\in B\},\qquad|A\times B|=|A|\cdot|B|.
$$

Unlike sets, pairs are ordered: $(1,2)\neq(2,1)$.

**Example.** $\{0,1\}\times\{x,y,z\}$ has $2\times3=6$ pairs. $\mathbb R\times\mathbb R=\mathbb R^2$ is the plane, and $\mathbb R^n$ is the space of vectors from [[LA 01 Vectors and Linear Combinations]]. A database table is a subset of a Cartesian product of its column domains.

## Partitions

A **partition** of $A$ is a collection of non-empty subsets that are pairwise disjoint and whose union is $A$. Every element lands in exactly one block.

Example: the integers split into evens and odds. Partitions are how "proof by cases" and the law of total probability organize their cases, and they correspond exactly to equivalence relations ([[DM 05 Functions and Relations]]).

## Infinite sets: a glimpse

Two sets have the same cardinality when their elements can be paired off one-to-one. By this measure the even numbers are as numerous as all natural numbers (pair $n$ with $2n$), and so are the rationals. Such sets are **countable**. The real numbers are not: Cantor's diagonal argument shows no list can contain them all. So there are different sizes of infinity, and consequently there are more functions than there are programs to compute them.

## A warning: Russell's paradox

Let $R=\{x\mid x\notin x\}$, the set of all sets that are not members of themselves. Is $R\in R$? If yes, then by definition $R\notin R$. If no, then $R\in R$. Contradiction either way. The lesson: "the set of all things with property $P$" is not always a legitimate set. Building sets as subsets of an existing set, as in $\{x\in A\mid P(x)\}$, is safe.

## Learn by doing

1. With $A=\{1,2,3\}$, $B=\{2,3,4\}$, $C=\{3,4,5\}$: find $A\cap B\cap C$, $(A\cup B)\setminus C$ and $A\triangle B$.
2. List $\mathcal P(\{1,2,3\})$. How many elements?
3. In a class of 40, 25 take maths, 20 take physics and 8 take neither. How many take both?
4. True or false: $\{\emptyset\}\subseteq\{\emptyset,\{1\}\}$; $\emptyset\in\{1,2\}$; $\emptyset\subseteq\{1,2\}$.

> [!success]- Check your answers
> 1. $\{3\}$; $\{1,2\}$; $\{1,4\}$.
> 2. $\emptyset,\{1\},\{2\},\{3\},\{1,2\},\{1,3\},\{2,3\},\{1,2,3\}$: $2^3=8$.
> 3. $40-8=32$ take at least one. $25+20-32=13$.
> 4. True; false; true.

## Where this shows up

Events are sets ([[PS 01 Sample Spaces Events and Axioms]]). State spaces and action spaces in reinforcement learning are sets, and a policy is a function between them. SQL's `UNION`, `INTERSECT` and `EXCEPT` are the set operations above.

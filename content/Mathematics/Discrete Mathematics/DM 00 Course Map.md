---
type: course-home
course: discrete-mathematics
tags: [mathematics, discrete-mathematics, course]
created: 2026-11-17
---
# Discrete mathematics: course map

[[Mathematics Courses]] | Start: [[DM 01 Logic and Propositions]]

Discrete mathematics studies things you can count and list: true/false statements, whole numbers, sets, sequences, networks. It is the mathematics of computer science. It also teaches the skill underneath every other course: reading a precise statement and proving that it is true.

> [!tip] How to study this course
> - Proofs are learned by writing them. For each theorem, cover the proof and try it first, even if you fail.
> - When a definition is abstract, build the smallest example you can (a set with two elements, a graph with three vertices) and test the definition on it.
> - Chapters 1 to 3 are the grammar. Everything later is written in it, so do not rush them.

## Chapters

| Chapter | The question it answers |
|---|---|
| [[DM 01 Logic and Propositions]] | How do I combine true/false statements exactly? |
| [[DM 02 Predicates and Quantifiers]] | How do I say "for all" and "there exists" without ambiguity? |
| [[DM 03 Proof Techniques]] | How do I establish that a statement is true? |
| [[DM 04 Sets]] | How do I talk about collections of objects? |
| [[DM 05 Functions and Relations]] | How do I describe connections between objects? |
| [[DM 06 Induction and Recursion]] | How do I prove something for infinitely many cases? |
| [[DM 07 Counting]] | How many ways are there? |
| [[DM 08 Number Theory and Modular Arithmetic]] | How do whole numbers divide, and how does clock arithmetic work? |
| [[DM 09 Recurrences and Asymptotics]] | How fast does an algorithm's cost grow? |
| [[DM 10 Graphs]] | How do I model and search a network? |
| [[DM 11 Trees and Graph Algorithms]] | How do I find shortest paths and cheapest connections? |
| [[DM 12 Boolean Algebra and Automata]] | How do circuits and simple machines compute? |

## Dependencies

- 1, 2, 3 in order, then 4, 5, 6.
- 7 needs 4. It feeds directly into [[PS 01 Sample Spaces Events and Axioms]] and [[PS 03 Discrete Random Variables]].
- 8 needs 3 and 6.
- 9 needs 6.
- 10 and 11 need 4, 5 and 6.
- 12 needs 1 and 10.

## Notation

| Symbol | Meaning |
|---|---|
| $\neg p$, $p\land q$, $p\lor q$ | not, and, or |
| $p\to q$, $p\leftrightarrow q$ | if-then, if and only if |
| $\forall$, $\exists$ | for all, there exists |
| $\in$, $\subseteq$ | is an element of, is a subset of |
| $\cup$, $\cap$, $\setminus$ | union, intersection, difference |
| $\mathbb N,\mathbb Z,\mathbb Q,\mathbb R$ | natural numbers, integers, rationals, reals |
| $a\mid b$ | $a$ divides $b$ |
| $a\equiv b\pmod n$ | $a$ and $b$ leave the same remainder on division by $n$ |
| $\binom nk$ | number of ways to choose $k$ items from $n$ |
| $O(\cdot)$ | grows no faster than |

## Checkpoint questions for the whole course

1. Why is "if $p$ then $q$" true whenever $p$ is false?
2. What is the negation of "for every $x$ there exists a $y$ such that $P(x,y)$"?
3. Why does proving a base case and an inductive step prove a statement for every natural number?
4. Why is $\binom nk=\binom n{n-k}$, with a counting argument rather than algebra?
5. Why does a connected graph with $n$ vertices and $n-1$ edges have no cycle?

Recommended companions: Rosen, *Discrete Mathematics and Its Applications*; Epp, *Discrete Mathematics with Applications* (your earlier notes in this folder follow its first chapter); Lehman, Leighton and Meyer, *Mathematics for Computer Science* (free online).

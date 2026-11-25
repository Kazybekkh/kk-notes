---
type: course-home
course: linear-algebra
tags: [mathematics, linear-algebra, course]
created: 2026-11-17
---
# Linear Algebra: course map

[[Mathematics Courses]] | Start: [[LA 01 Vectors and Linear Combinations]]

Linear algebra is the study of two operations, adding vectors and scaling them, and of the functions that respect those operations. Almost everything in machine learning and robotics is written in this language: a robot pose, an image, a batch of data, a neural network layer and a covariance are all vectors or matrices.

> [!tip] How to study this course
> Each chapter is written like a textbook chapter. It opens with the big idea and a list of what you will be able to do, then builds the topic in numbered sections. Every section explains *why* before *how*, works several examples step by step, and ends with a short **Check yourself** question. The chapter closes with a summary and a graded exercise set:
>
> - **Part A, warm-up**: mechanical practice until the method is automatic.
> - **Part B, core**: problems that need understanding, including applied ones.
> - **Part C, explain and prove**: short arguments in your own words.
> - **Part D, practise with code**: small NumPy experiments that make the ideas visible.
>
> Full worked solutions are folded under each part.
>
> 1. One section at a time. Redo every worked example on paper before reading its solution.
> 2. Answer each **Check yourself** before opening it. If you get it wrong, reread that section only.
> 3. Do Parts A and B of the exercises at minimum. C and D are where understanding becomes solid.
> 4. One chapter takes two or three sittings. The order matters: each chapter uses the ones before it.

## The one picture to keep

A matrix $A$ is a machine that takes a vector $x$ and returns a vector $Ax$. Every chapter asks one question about that machine.

| Chapter | The question it answers |
|---|---|
| [[LA 01 Vectors and Linear Combinations]] | What can I build by adding and scaling a few vectors? |
| [[LA 02 Dot Product Length and Angle]] | How long is a vector, and how aligned are two vectors? |
| [[LA 03 Matrices as Linear Maps]] | What does a matrix do to space? |
| [[LA 04 Solving Linear Systems]] | Given $A$ and $b$, how do I find $x$ with $Ax=b$? |
| [[LA 05 Subspaces Basis and Rank]] | Which outputs are reachable, and which inputs are lost? |
| [[LA 06 Orthogonality and Least Squares]] | If $Ax=b$ has no solution, what is the best approximate one? |
| [[LA 07 Determinants]] | By what factor does a matrix scale volume? |
| [[LA 08 Eigenvalues and Eigenvectors]] | Which directions does a matrix only stretch? |
| [[LA 09 Symmetric and Positive Definite Matrices]] | When is a matrix a pure stretch along perpendicular axes? |
| [[LA 10 Singular Value Decomposition]] | What is the simplest description of any matrix? |
| [[LA 11 Change of Basis]] | How does the same map look in different coordinates? |
| [[LA 12 Matrix Calculus and Numerical Practice]] | How do I differentiate with matrices and compute safely? |

## Dependencies

- Chapters 1 to 5 are the core. Do not skip them.
- Chapter 6 needs 2 and 5.
- Chapters 8, 9 and 10 build on each other in that order.
- Chapter 12 needs 6, 9 and 10 and connects to [[01 Math for Learning]] and [[05 Training Neural Policies]].

## Notation used throughout

| Symbol | Meaning |
|---|---|
| $x, v, b$ | column vectors (lower case) |
| $A, B, Q$ | matrices (upper case) |
| $A^\top$ | transpose: rows become columns |
| $\mathbb R^n$ | all lists of $n$ real numbers |
| $A\in\mathbb R^{m\times n}$ | $m$ rows, $n$ columns; takes vectors in $\mathbb R^n$, returns vectors in $\mathbb R^m$ |
| $I$ | identity matrix, $Ix=x$ |
| $e_1,\dots,e_n$ | standard basis vectors: a single 1, zeros elsewhere |

## Checkpoint questions for the whole course

You understand the course when you can answer these without notes.

1. Why is $Ax$ a combination of the columns of $A$?
2. Why does $Ax=b$ have a solution exactly when $b$ is in the column space?
3. Why is the least squares solution given by $A^\top A\hat x=A^\top b$?
4. Why do symmetric matrices have perpendicular eigenvectors?
5. What do the singular values of a matrix tell you about what it does to a sphere?

Recommended companions: Gilbert Strang, *Introduction to Linear Algebra*, and the video series [Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) for pictures.

---
type: index
tags: [mathematics, course]
created: 2026-11-17
---
# Mathematics courses

Three self-contained courses covering the mathematics underneath robot learning and computer science. Each chapter states its main idea in one sentence, builds it from definitions, works through examples by hand, lists common mistakes, and ends with exercises that have hidden answers.

| Course | Chapters | Start |
|---|---|---|
| Linear algebra | 12 | [[LA 00 Course Map]] |
| Probability and statistics | 12 | [[PS 00 Course Map]] |
| Discrete mathematics | 12 | [[DM 00 Course Map]] |

## Suggested order

You do not need to finish one course before starting another. This interleaving respects every dependency:

| Week | Read |
|---|---|
| 1 | [[DM 01 Logic and Propositions]], [[DM 02 Predicates and Quantifiers]], [[DM 03 Proof Techniques]] |
| 2 | [[LA 01 Vectors and Linear Combinations]], [[LA 02 Dot Product Length and Angle]], [[LA 03 Matrices as Linear Maps]] |
| 3 | [[DM 04 Sets]], [[DM 05 Functions and Relations]], [[DM 06 Induction and Recursion]] |
| 4 | [[LA 04 Solving Linear Systems]], [[LA 05 Subspaces Basis and Rank]], [[LA 06 Orthogonality and Least Squares]] |
| 5 | [[DM 07 Counting]], [[PS 01 Sample Spaces Events and Axioms]], [[PS 02 Conditional Probability and Bayes Rule]] |
| 6 | [[PS 03 Discrete Random Variables]], [[PS 04 Expectation and Variance]], [[PS 05 Continuous Random Variables]] |
| 7 | [[LA 07 Determinants]], [[LA 08 Eigenvalues and Eigenvectors]], [[LA 09 Symmetric and Positive Definite Matrices]] |
| 8 | [[PS 06 Joint Distributions and Covariance]], [[PS 07 The Multivariate Gaussian]], [[PS 08 Law of Large Numbers and Central Limit Theorem]] |
| 9 | [[LA 10 Singular Value Decomposition]], [[LA 11 Change of Basis]], [[LA 12 Matrix Calculus and Numerical Practice]] |
| 10 | [[PS 09 Estimation and Maximum Likelihood]], [[PS 10 Confidence Intervals and Hypothesis Tests]], [[PS 11 Bayesian Inference]] |
| 11 | [[DM 08 Number Theory and Modular Arithmetic]], [[DM 09 Recurrences and Asymptotics]], [[PS 12 Markov Chains and Information]] |
| 12 | [[DM 10 Graphs]], [[DM 11 Trees and Graph Algorithms]], [[DM 12 Boolean Algebra and Automata]] |

## How these connect to the robot learning book

- [[01 Math for Learning]] summarizes vectors, gradients and Bayes' rule in a few pages. These courses are the full version.
- Kinematics ([[02 Geometry and Kinematics]]) needs LA 03, LA 11 and LA 12.
- State estimation ([[04 Perception and State]]) needs PS 02, PS 07 and PS 11.
- Training ([[05 Training Neural Policies]]) needs LA 12 and PS 09.
- Evaluation ([[16 Evaluation and Uncertainty]]) needs PS 08 and PS 10.
- Reinforcement learning ([[09 Reinforcement Learning]]) needs PS 04, PS 12 and DM 06.

## How to study

1. One chapter per sitting.
2. Redo every worked example on paper before reading its solution.
3. Answer the exercises before opening the answers.
4. Close the note and say its one-sentence summary aloud. If you cannot, reread the first section.
5. After each course, answer its checkpoint questions without notes.

## Earlier notes

Your earlier discrete mathematics notes (Epp, chapter 1) are in `Discrete Mathematics/Chapter 1 Speaking Mathematically`. University course notes are in `Computer Science/University/Year 1/DIscrete Mathematics`.

---
type: course-chapter
course: discrete-mathematics
chapter: 6
tags: [mathematics, discrete-mathematics, proof, induction]
---
# DM 06 Induction and recursion

Previous: [[DM 05 Functions and Relations]] | [[DM 00 Course Map]] | Next: [[DM 07 Counting]]

> [!abstract] One sentence
> Induction proves a statement for every natural number by proving the first case and proving that each case forces the next; recursion is the same idea used to define and compute.

## The principle

To prove that $P(n)$ holds for all integers $n\ge n_0$:

1. **Base case.** Prove $P(n_0)$.
2. **Inductive step.** Prove that for every $k\ge n_0$, **if** $P(k)$ **then** $P(k+1)$.

The assumption $P(k)$ in step 2 is the **inductive hypothesis**.

**Why it works: dominoes.** The base case knocks over the first domino. The inductive step says each falling domino knocks over the next. So all fall. Both parts are essential: without the base case nothing starts; without the step the chain breaks.

> [!warning] You are not assuming what you want to prove
> You assume $P(k)$ for one arbitrary $k$ and derive $P(k+1)$. That is proving the *implication* $P(k)\to P(k+1)$, which is a different statement from "$P(n)$ for all $n$".

## Worked example 1: a sum

**Claim.** For all $n\ge1$,

$$
1+2+\cdots+n=\frac{n(n+1)}2.
$$

**Base case** $n=1$: left side $1$, right side $\tfrac{1\cdot2}2=1$. True.

**Inductive step.** Assume $1+2+\cdots+k=\dfrac{k(k+1)}2$. Then

$$
1+2+\cdots+k+(k+1)=\frac{k(k+1)}2+(k+1)=(k+1)\left(\frac k2+1\right)=\frac{(k+1)(k+2)}2.
$$

That is the formula with $n=k+1$. By induction it holds for all $n\ge1$. $\blacksquare$

The key move: split off the last term so the inductive hypothesis can be applied to the rest. Always write down what $P(k+1)$ says before you start, so you know your target.

## Worked example 2: divisibility

**Claim.** $n^3-n$ is divisible by 3 for all $n\ge0$.

**Base:** $0^3-0=0$, divisible by 3.

**Step.** Assume $k^3-k=3m$. Then

$$
(k+1)^3-(k+1)=k^3+3k^2+3k+1-k-1=(k^3-k)+3(k^2+k)=3(m+k^2+k).
$$

Divisible by 3. $\blacksquare$

## Worked example 3: an inequality

**Claim.** $2^n>n^2$ for all $n\ge5$.

**Base:** $2^5=32>25$.

**Step.** Assume $2^k>k^2$ with $k\ge5$. Then $2^{k+1}=2\cdot2^k>2k^2$. It remains to show $2k^2\ge(k+1)^2$, that is $k^2-2k-1\ge0$, that is $(k-1)^2\ge2$, true for $k\ge3$. So $2^{k+1}>(k+1)^2$. $\blacksquare$

The base case starts at 5 for a reason: the claim is false at $n=2,3,4$. Induction can begin anywhere.

## Strong induction

Sometimes $P(k+1)$ depends on cases earlier than $P(k)$. **Strong induction** lets you assume **all** of $P(n_0),\dots,P(k)$ when proving $P(k+1)$. It is logically equivalent to ordinary induction, just more convenient.

**Theorem.** Every integer $n\ge2$ is a product of primes.

*Proof.* Base: 2 is prime. Step: assume every integer from 2 to $k$ is a product of primes. If $k+1$ is prime, done. Otherwise $k+1=ab$ with $2\le a,b\le k$. By hypothesis $a$ and $b$ are products of primes, so $ab$ is too. $\blacksquare$

Ordinary induction fails here because the factors $a,b$ are not $k$; they are somewhere smaller.

**Example with several base cases.** Every amount of 12 or more can be paid with 4- and 5-unit coins. Bases: $12=4+4+4$, $13=4+4+5$, $14=4+5+5$, $15=5+5+5$. Step: for $k+1\ge16$, the amount $k+1-4\ge12$ is payable by hypothesis; add one 4. You need four base cases because the step reaches back four.

## A famous false proof

"All horses are the same colour." Base: one horse, trivially true. Step: take $k+1$ horses. The first $k$ share a colour; the last $k$ share a colour; the two groups overlap, so all $k+1$ match.

The flaw: the step fails for $k=1$. With two horses, "the first one" and "the last one" do not overlap. The chain breaks between the first and second domino. **Check that your inductive step really works for the smallest $k$.**

## Recursion

A **recursive definition** gives base values and a rule for building later values from earlier ones.

$$
n!=\begin{cases}1&n=0\\n\cdot(n-1)!&n\ge1\end{cases}
\qquad\qquad
F_n=\begin{cases}0&n=0\\1&n=1\\F_{n-1}+F_{n-2}&n\ge2\end{cases}
$$

The Fibonacci numbers run $0,1,1,2,3,5,8,13,\dots$

Recursion and induction are two faces of one idea: recursion *defines* by reduction to smaller cases; induction *proves* by reduction to smaller cases. Facts about recursively defined objects are proved by induction.

```python
def factorial(n):
    if n == 0:                       # base case
        return 1
    return n * factorial(n - 1)      # recursive case
```

**Correctness by induction.** Base: `factorial(0)` returns $1=0!$. Step: if `factorial(k)` returns $k!$, then `factorial(k+1)` returns $(k+1)\cdot k!=(k+1)!$.

Every recursive function needs a base case and must move toward it. Otherwise it never stops.

## Worked example: Tower of Hanoi

Move $n$ disks from one peg to another, one at a time, never placing a larger disk on a smaller. Strategy: move the top $n-1$ disks out of the way, move the largest, move the $n-1$ back on top. The number of moves satisfies

$$
T(1)=1,\qquad T(n)=2T(n-1)+1.
$$

First values: $1,3,7,15,31$. Guess: $T(n)=2^n-1$.

*Proof by induction.* Base: $2^1-1=1$. Step: $T(k+1)=2(2^k-1)+1=2^{k+1}-1$. $\blacksquare$

Guess the pattern from small cases, then prove it by induction. That is the standard workflow for solving recurrences ([[DM 09 Recurrences and Asymptotics]]).

## Structural induction

Induction also works on recursively built structures such as lists, trees and formulas. Prove the property for the base objects, then show that each construction rule preserves it.

**Example.** A binary tree is either a single leaf or a root with two subtrees. *Claim:* a binary tree in which every internal node has two children has one more leaf than internal nodes. Base: one leaf, zero internal. Step: if the subtrees have $l_1=i_1+1$ and $l_2=i_2+1$, the whole tree has $l_1+l_2$ leaves and $i_1+i_2+1$ internal nodes, and $l_1+l_2=(i_1+i_2+1)+1$.

## Loop invariants

A **loop invariant** is a statement that is true before the loop and stays true after each iteration. Proving it is induction on the number of iterations. When the loop ends, the invariant plus the exit condition gives correctness.

```python
total = 0
for i in range(1, n + 1):
    total += i
```

Invariant: after the iteration with index $i$, `total` equals $1+\cdots+i$. At exit, $i=n$, so `total` is $n(n+1)/2$.

## Common mistakes

- **Skipping the base case**, or proving the wrong one.
- **Assuming $P(k+1)$** somewhere inside the step.
- **Not using the inductive hypothesis.** If you never used it, either the proof is wrong or induction was unnecessary.
- **Too few base cases** when the step reaches back more than one.

## Learn by doing

1. Prove $1+3+5+\cdots+(2n-1)=n^2$.
2. Prove $1+2+4+\cdots+2^n=2^{n+1}-1$ for $n\ge0$.
3. Prove that $5^n-1$ is divisible by 4 for $n\ge1$.
4. A sequence has $a_1=3$, $a_{n}=a_{n-1}+4$. Guess a formula and prove it.

> [!success]- Check your answers
> 1. Base $1=1^2$. Step: $k^2+(2k+1)=(k+1)^2$.
> 2. Base $1=2^1-1$. Step: $(2^{k+1}-1)+2^{k+1}=2^{k+2}-1$.
> 3. Base $5-1=4$. Step: $5^{k+1}-1=5(5^k-1)+4$, a sum of two multiples of 4.
> 4. $a_n=4n-1$. Base $a_1=3$. Step: $a_{k+1}=(4k-1)+4=4(k+1)-1$.

## Where this shows up

Dynamic programming is recursion with stored results. The Bellman equation defines the value of a state in terms of the values of its successors, and value iteration is proved to converge by an inductive argument ([[09 Reinforcement Learning]]). Backpropagation walks a computation graph recursively.

---
type: course-chapter
course: discrete-mathematics
chapter: 9
tags: [mathematics, discrete-mathematics, algorithms]
---
# DM 09 Recurrences and asymptotics

Previous: [[DM 08 Number Theory and Modular Arithmetic]] | [[DM 00 Course Map]] | Next: [[DM 10 Graphs]]

> [!abstract] One sentence
> Big-O notation describes how a cost grows when the input gets large, ignoring constants, and recurrences let you compute that growth for recursive algorithms.

## Why asymptotics

Running time depends on the machine, the language and the input. What survives all of that is how the cost **scales**: does doubling the input double the time, quadruple it, or add one step?

| $n$ | $\log_2n$ | $n$ | $n\log_2n$ | $n^2$ | $2^n$ |
|---|---|---|---|---|---|
| 10 | 3.3 | 10 | 33 | 100 | 1,024 |
| 1,000 | 10 | 1,000 | 10,000 | $10^6$ | about $10^{301}$ |
| $10^6$ | 20 | $10^6$ | $2\times10^7$ | $10^{12}$ | hopeless |

At a billion operations per second, $n^2$ for $n=10^6$ takes about 17 minutes; $n\log n$ takes 0.02 seconds. No constant-factor tuning bridges a gap like that.

## Big-O, Big-Omega, Big-Theta

**Big-O (upper bound).** $f(n)=O(g(n))$ if there are constants $c>0$ and $n_0$ such that

$$
f(n)\le c\,g(n)\quad\text{for all }n\ge n_0.
$$

"Eventually, $f$ grows no faster than a constant multiple of $g$."

**Big-Omega (lower bound).** $f(n)=\Omega(g(n))$ if $f(n)\ge c\,g(n)$ eventually.

**Big-Theta (tight bound).** $f(n)=\Theta(g(n))$ if both hold: same growth rate.

**Worked example.** Show $3n^2+5n+2=O(n^2)$. For $n\ge1$: $5n\le5n^2$ and $2\le2n^2$, so $3n^2+5n+2\le10n^2$. Take $c=10$, $n_0=1$. It is also $\Omega(n^2)$ (since it is at least $3n^2$), hence $\Theta(n^2)$.

**Rules of thumb.**

- Keep the fastest-growing term, drop the rest, drop the constant: $7n^3+100n^2\log n+10^6=\Theta(n^3)$.
- Logarithm bases do not matter: $\log_2n=\log_{10}n/\log_{10}2$ differs only by a constant, so just write $\log n$.
- Growth order: $1\ll\log n\ll\sqrt n\ll n\ll n\log n\ll n^2\ll n^3\ll2^n\ll n!$

> [!warning] Big-O is an upper bound
> $n=O(n^2)$ is a true statement, just a weak one. People often write $O$ when they mean $\Theta$. When precision matters, say which.

**Limit test.** If $\lim_{n\to\infty}f(n)/g(n)$ is a positive constant, then $f=\Theta(g)$. If it is 0, $f$ grows strictly slower.

## Counting operations in code

```python
for i in range(n):          # n iterations
    for j in range(n):      # n iterations each
        work()              # constant time
```

$n\cdot n=\Theta(n^2)$.

```python
for i in range(n):
    for j in range(i):      # i iterations
        work()
```

$0+1+\cdots+(n-1)=\dfrac{n(n-1)}2=\Theta(n^2)$, by the sum formula from [[DM 06 Induction and Recursion]]. Half the work, same growth.

```python
while n > 1:
    n = n // 2
```

The value halves each time, so the loop runs about $\log_2n$ times: $\Theta(\log n)$. Whenever a problem is cut by a constant factor per step, expect a logarithm.

## Recurrences

A recursive algorithm's cost is naturally described by a **recurrence**.

**Binary search.** Look at the middle, recurse into one half:

$$
T(n)=T(n/2)+1.
$$

**Merge sort.** Sort each half recursively, then merge in linear time:

$$
T(n)=2T(n/2)+n.
$$

**Naive Fibonacci.** `fib(n)` calls `fib(n-1)` and `fib(n-2)`:

$$
T(n)=T(n-1)+T(n-2)+1.
$$

## Solving recurrences by unrolling

**Binary search.** $T(n)=T(n/2)+1=T(n/4)+2=\cdots=T(n/2^k)+k$. The size reaches 1 when $k=\log_2n$, so $T(n)=\Theta(\log n)$.

**Merge sort, as a recursion tree.**

- Level 0: one problem of size $n$, merge cost $n$.
- Level 1: two problems of size $n/2$, total merge cost $2\cdot n/2=n$.
- Level $j$: $2^j$ problems of size $n/2^j$, total cost $n$.
- Levels until size 1: $\log_2n$.

Total: $n$ per level times $\log_2n$ levels, so $T(n)=\Theta(n\log n)$. This is why merge sort beats the $\Theta(n^2)$ of simple sorts.

**Tower of Hanoi.** $T(n)=2T(n-1)+1$ gave $2^n-1$ in [[DM 06 Induction and Recursion]]: exponential.

## The master theorem

For divide-and-conquer recurrences of the form

$$
T(n)=a\,T(n/b)+\Theta(n^d)
$$

($a$ subproblems, each of size $n/b$, plus $n^d$ work to split and combine), compare $d$ with $\log_ba$:

| Case | Result | Intuition |
|---|---|---|
| $d>\log_ba$ | $\Theta(n^d)$ | the top-level work dominates |
| $d=\log_ba$ | $\Theta(n^d\log n)$ | every level contributes equally |
| $d<\log_ba$ | $\Theta(n^{\log_ba})$ | the many tiny subproblems dominate |

**Check.** Merge sort: $a=2$, $b=2$, $d=1$, and $\log_22=1=d$, so $\Theta(n\log n)$. Binary search: $a=1$, $b=2$, $d=0$, and $\log_21=0=d$, so $\Theta(\log n)$.

**Example.** $T(n)=4T(n/2)+n$: $\log_24=2>1$, so $\Theta(n^2)$. Splitting into four half-size problems is no better than brute force here. Karatsuba's multiplication trick reduces 4 subproblems to 3, giving $\Theta(n^{\log_23})\approx\Theta(n^{1.585})$.

## Linear recurrences

For a recurrence like $a_n=c_1a_{n-1}+c_2a_{n-2}$, try $a_n=r^n$. Substituting gives the **characteristic equation**

$$
r^2=c_1r+c_2.
$$

If its roots $r_1\neq r_2$, the general solution is $a_n=\alpha r_1^n+\beta r_2^n$, with $\alpha,\beta$ fixed by the initial values.

**Fibonacci.** $r^2=r+1$ gives $r=\dfrac{1\pm\sqrt5}2$. The larger root is the golden ratio $\varphi\approx1.618$. So

$$
F_n=\frac{\varphi^n-\psi^n}{\sqrt5},\qquad\psi=\frac{1-\sqrt5}2\approx-0.618.
$$

Since $|\psi|<1$, $F_n\approx\varphi^n/\sqrt5$: Fibonacci numbers grow exponentially. So does naive recursive `fib`, because its call tree mirrors the recurrence. Storing results (memoization) makes it $\Theta(n)$. That change, from exponential to linear, is dynamic programming in one example.

The method is the eigenvalue analysis of [[LA 08 Eigenvalues and Eigenvectors]] in disguise: write $(F_n,F_{n-1})$ as a vector updated by a $2\times2$ matrix, and the roots are its eigenvalues.

## Best, worst and average case

Cost often depends on the particular input, not just its size.

- **Worst case**: guaranteed upper bound. The usual default.
- **Average case**: expected cost under some input distribution ([[PS 04 Expectation and Variance]]).
- **Best case**: rarely informative.

Quicksort is $\Theta(n^2)$ in the worst case but $\Theta(n\log n)$ on average, and fast in practice.

## Space

Memory obeys the same notation. Merge sort uses $\Theta(n)$ extra space; recursion uses stack space proportional to its depth. A $\Theta(n^2)$ attention matrix over a sequence of length $n$ is the reason long contexts are expensive ([[Appendix - Neural Networks and Attention]]).

## Common mistakes

- **Counting a nested loop as $n^2$** when the inner loop is short or the outer halves.
- **Ignoring the cost of library calls.** `x in list` is $\Theta(n)$; `x in set` is $\Theta(1)$ on average.
- **Treating Big-O as exact time.** Constants matter for small $n$, and real hardware rewards memory locality.
- **Assuming recursion is cheap.** Overlapping subproblems can explode.

## Learn by doing

1. Give a $\Theta$ bound for $5n\log n+2n+100$.
2. What is the running time of a loop where `i` starts at 1 and doubles until it exceeds $n$, with a nested loop of $n$ steps inside?
3. Solve with the master theorem: $T(n)=3T(n/3)+n$ and $T(n)=8T(n/2)+n^2$.
4. Rank: $n^2$, $2^n$, $n\log n$, $\sqrt n$, $100n$.

> [!success]- Check your answers
> 1. $\Theta(n\log n)$.
> 2. The outer loop runs $\log n$ times; total $\Theta(n\log n)$.
> 3. First: $\log_33=1=d$, $\Theta(n\log n)$. Second: $\log_28=3>2$, $\Theta(n^3)$.
> 4. $\sqrt n$, $100n$, $n\log n$, $n^2$, $2^n$.

## Where this shows up

Sampling-based planners, nearest-neighbour searches over demonstration datasets, and attention layers each have a growth rate that decides what is feasible on a robot's compute budget ([[15 Robot Systems and Deployment]]).

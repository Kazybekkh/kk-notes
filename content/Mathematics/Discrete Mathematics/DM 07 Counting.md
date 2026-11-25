---
type: course-chapter
course: discrete-mathematics
chapter: 7
tags: [mathematics, discrete-mathematics, combinatorics]
---
# DM 07 Counting

Previous: [[DM 06 Induction and Recursion]] | [[DM 00 Course Map]] | Next: [[DM 08 Number Theory and Modular Arithmetic]]

> [!abstract] One sentence
> Counting comes down to two rules (multiply for "and then", add for "or") and two questions about any selection: does order matter, and is repetition allowed?

## The two basic rules

**Product rule.** If a task is a sequence of steps, with $n_1$ ways to do the first, $n_2$ ways to do the second whatever was chosen first, and so on, there are $n_1\cdot n_2\cdots n_k$ ways in total.

*Example.* 3 shirts and 4 trousers: $3\times4=12$ outfits. A 4-digit PIN: $10^4=10{,}000$. Bit strings of length 8: $2^8=256$.

**Sum rule.** If a task can be done in one of several ways that **cannot overlap**, add.

*Example.* Choose one dessert from 5 cakes or 3 ice creams: $5+3=8$.

If the options overlap, subtract the overlap (inclusion-exclusion, [[DM 04 Sets]]).

**Complement.** Sometimes counting what you do *not* want is easier: wanted $=$ total $-$ unwanted. "At least one" almost always means: total minus "none".

*Example.* 8-bit strings with at least one 1: $2^8-1=255$.

## Permutations: order matters

The number of ways to arrange $n$ distinct objects in a row:

$$
n!=n\cdot(n-1)\cdots2\cdot1.
$$

$n$ choices for the first position, $n-1$ for the second, and so on. $0!=1$ by convention (there is one way to arrange nothing).

The number of ways to pick and arrange $k$ of $n$ distinct objects:

$$
P(n,k)=n(n-1)\cdots(n-k+1)=\frac{n!}{(n-k)!}.
$$

*Example.* Gold, silver and bronze among 8 runners: $8\cdot7\cdot6=336$.

## Combinations: order does not matter

The number of ways to choose a set of $k$ objects from $n$:

$$
\binom nk=\frac{n!}{k!\,(n-k)!}.
$$

**Where the formula comes from.** Count ordered selections: $P(n,k)$. Each unordered set of $k$ objects was counted once for each of its $k!$ orderings. Divide:

$$
\binom nk=\frac{P(n,k)}{k!}.
$$

"Count with order, then divide by the overcounting" is one of the most useful ideas in combinatorics.

*Example.* A committee of 3 from 8 people: $\dfrac{8\cdot7\cdot6}{3\cdot2\cdot1}=56$. Compare with 336 for the medals: each committee corresponds to $3!=6$ podium orders.

## The four cases

Choosing $k$ items from $n$ types:

| | Order matters | Order does not matter |
|---|---|---|
| No repetition | $\dfrac{n!}{(n-k)!}$ | $\dbinom nk$ |
| Repetition allowed | $n^k$ | $\dbinom{n+k-1}{k}$ |

The bottom right is **stars and bars**. To choose $k$ items from $n$ types with repetition, write $k$ stars (the items) and $n-1$ bars (dividers between types). Each arrangement of the $n+k-1$ symbols is one selection, and an arrangement is fixed by choosing which positions hold stars.

*Example.* 3 scoops from 4 flavours, repeats allowed: $\binom{6}{3}=20$. The picture `**|*||` means two of flavour 1, one of flavour 2, none of 3 or 4.

Before using any formula, ask the two questions. Most counting errors come from answering them wrongly.

## Arrangements with identical objects

The number of distinct arrangements of $n$ objects where $n_1$ are identical of one kind, $n_2$ of another, and so on:

$$
\frac{n!}{n_1!\,n_2!\cdots n_r!}.
$$

*Example.* Arrangements of the letters of MISSISSIPPI (11 letters: 1 M, 4 I, 4 S, 2 P):

$$
\frac{11!}{1!\,4!\,4!\,2!}=34{,}650.
$$

Same idea again: pretend all are distinct ($11!$), then divide by the rearrangements that make no visible difference.

## Properties of binomial coefficients

**Symmetry.**

$$
\binom nk=\binom n{n-k}.
$$

Choosing the $k$ to include is the same as choosing the $n-k$ to leave out.

**Pascal's rule.**

$$
\binom nk=\binom{n-1}{k-1}+\binom{n-1}k.
$$

*Counting proof.* Single out one object. A set of $k$ either contains it (choose the other $k-1$ from the remaining $n-1$) or does not (choose all $k$ from the remaining $n-1$). The two cases do not overlap, so add.

This rule builds **Pascal's triangle**, each entry the sum of the two above:

```
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
```

**Row sum.**

$$
\sum_{k=0}^n\binom nk=2^n.
$$

Both sides count all subsets of an $n$-element set: the left by size, the right by a yes/no decision per element.

Arguments like these, showing two expressions are equal because they count the same thing, are called **combinatorial proofs**. They explain *why* an identity is true, not merely that it is.

## The binomial theorem

$$
(x+y)^n=\sum_{k=0}^n\binom nkx^{n-k}y^k.
$$

**Why.** Expanding $(x+y)(x+y)\cdots(x+y)$ means picking $x$ or $y$ from each of the $n$ brackets. A term $x^{n-k}y^k$ arises once for each way to choose which $k$ brackets supply the $y$: $\binom nk$ ways.

*Example.* $(x+y)^4=x^4+4x^3y+6x^2y^2+4xy^3+y^4$, with coefficients from row 4 of the triangle.

Setting $x=y=1$ recovers the row sum. Setting $x=1-p$, $y=p$ shows the binomial probabilities sum to 1 ([[PS 03 Discrete Random Variables]]).

## Pigeonhole principle

If $n$ objects are placed in $m$ boxes and $n>m$, some box holds at least two. More generally, some box holds at least $\lceil n/m\rceil$.

*Examples.* Among 13 people, two share a birth month. Among 367 people, two share a birthday. In any group of 6 socks drawn from 5 colours, two match.

*A less obvious one.* Among any 5 points in a unit square, two are at most $\sqrt2/2$ apart. Divide the square into four half-size squares; two points share one, and the diagonal of a half-size square is $\sqrt2/2$.

The principle proves that something exists without finding it. It is the reason lossless compression cannot shrink every file, and hash functions must have collisions.

## Worked example: poker hands

A hand is 5 cards from 52, order irrelevant: $\binom{52}5=2{,}598{,}960$.

**Full house** (three of one rank, two of another): choose the rank of the triple (13), its three suits ($\binom43=4$), the rank of the pair (12), its two suits ($\binom42=6$):

$$
13\cdot4\cdot12\cdot6=3{,}744,\qquad P=\frac{3744}{2598960}\approx0.00144.
$$

**Flush** (all one suit, including straight flushes): $4\cdot\binom{13}5=4\cdot1287=5{,}148$.

Break the object into a sequence of independent choices, then multiply.

## Common mistakes

- **Using permutations when order is irrelevant**, or the reverse.
- **Double counting.** Choosing "one ace, then four other cards" counts hands with two aces twice.
- **Adding when you should multiply.** "And then" multiplies; "or" adds.
- **Forgetting that the options in a sum must be disjoint.**

## Learn by doing

1. How many 5-letter strings over 26 letters have no repeated letter?
2. A team of 4 is chosen from 6 engineers and 5 designers. How many teams have exactly 2 of each?
3. How many 8-bit strings contain exactly three 1s? At least one 0?
4. How many ways can 10 identical sweets be shared among 3 children?
5. How many integers must you pick to guarantee two with the same remainder mod 7?

> [!success]- Check your answers
> 1. $26\cdot25\cdot24\cdot23\cdot22=7{,}893{,}600$.
> 2. $\binom62\binom52=15\cdot10=150$.
> 3. $\binom83=56$. And $2^8-1=255$ (all except the all-ones string).
> 4. Stars and bars: $\binom{12}{2}=66$.
> 5. 8, by pigeonhole (7 possible remainders).

## Where this shows up

Probability with equally likely outcomes is counting ([[PS 01 Sample Spaces Events and Axioms]]), and the binomial distribution is built from $\binom nk$. Counting the states or action sequences of a problem tells you immediately whether exhaustive search is feasible: $k$ actions over a horizon of $T$ steps give $k^T$ sequences, which is why planning needs something cleverer than enumeration ([[11 World Models and Planning]]).

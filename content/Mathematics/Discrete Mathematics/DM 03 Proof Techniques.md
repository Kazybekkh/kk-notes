---
type: course-chapter
course: discrete-mathematics
chapter: 3
tags: [mathematics, discrete-mathematics, proof]
---
# DM 03 Proof techniques

Previous: [[DM 02 Predicates and Quantifiers]] | [[DM 00 Course Map]] | Next: [[DM 04 Sets]]

> [!abstract] One sentence
> A proof is a chain of steps, each justified by a definition or an earlier result, that leaves no way for the statement to be false; a small set of standard strategies covers most proofs.

## What a proof is

Evidence persuades; a proof guarantees. A thousand examples leave a universal claim unproven, and one counterexample destroys it.

A proof starts from **definitions** and already-established facts, and moves by valid logical steps ([[DM 01 Logic and Propositions]]) to the conclusion. Most of the work in a beginner's proof is writing out definitions precisely. These are used throughout this chapter:

- $n$ is **even** if $n=2k$ for some integer $k$.
- $n$ is **odd** if $n=2k+1$ for some integer $k$.
- $a$ **divides** $b$, written $a\mid b$, if $b=ak$ for some integer $k$.
- $r$ is **rational** if $r=a/b$ for integers $a,b$ with $b\neq0$.

## Direct proof

To prove $p\to q$: assume $p$, unpack the definitions, compute, arrive at $q$.

**Theorem.** The sum of two odd integers is even.

*Proof.* Let $m$ and $n$ be odd. By definition, $m=2a+1$ and $n=2b+1$ for some integers $a,b$. Then

$$
m+n=2a+2b+2=2(a+b+1).
$$

Since $a+b+1$ is an integer, $m+n$ is twice an integer, hence even. $\blacksquare$

Template: *assume the hypothesis; write what it means; manipulate; recognize the conclusion's definition.* Note the use of two different letters $a$ and $b$: the two odd numbers need not be equal.

## Proof by contrapositive

Since $p\to q\equiv\neg q\to\neg p$, you may prove the contrapositive instead. Use it when "not $q$" gives you more to work with than $p$.

**Theorem.** If $n^2$ is even, then $n$ is even.

A direct attempt stalls: from $n^2=2k$ you would need a square root. Flip it.

*Proof.* We prove the contrapositive: if $n$ is odd, then $n^2$ is odd. Let $n=2k+1$. Then

$$
n^2=4k^2+4k+1=2(2k^2+2k)+1,
$$

which is odd. $\blacksquare$

## Proof by contradiction

Assume the statement is **false** and derive something impossible. Since the assumption leads to nonsense, the statement must be true.

**Theorem.** $\sqrt2$ is irrational.

*Proof.* Suppose, for contradiction, that $\sqrt2$ is rational. Then $\sqrt2=a/b$ where $a,b$ are integers with no common factor (cancel any common factors first). Squaring, $a^2=2b^2$, so $a^2$ is even, so $a$ is even by the previous theorem. Write $a=2c$. Then $4c^2=2b^2$, so $b^2=2c^2$, so $b$ is even too. Now $a$ and $b$ share the factor 2, contradicting the choice of $a/b$ in lowest terms. Hence $\sqrt2$ is irrational. $\blacksquare$

**Theorem (Euclid).** There are infinitely many primes.

*Proof.* Suppose there are only finitely many: $p_1,p_2,\dots,p_k$. Let $N=p_1p_2\cdots p_k+1$. Dividing $N$ by any $p_i$ leaves remainder 1, so no $p_i$ divides $N$. But $N>1$ has some prime factor, and that prime is not on the list. Contradiction. $\blacksquare$

Contradiction is powerful and slightly dangerous: an arithmetic slip also produces a "contradiction". Prefer a direct or contrapositive proof when one is available.

## Proof by cases

Split into cases that together cover every possibility and prove each.

**Theorem.** For every integer $n$, $n^2+n$ is even.

*Proof.* $n^2+n=n(n+1)$.
*Case 1:* $n$ is even, $n=2k$. Then $n(n+1)=2k(n+1)$ is even.
*Case 2:* $n$ is odd, $n=2k+1$. Then $n+1=2k+2=2(k+1)$, so $n(n+1)=2n(k+1)$ is even.
These cases cover all integers. $\blacksquare$

The cases must be **exhaustive**. Forgetting a case (often zero, or negatives) is the standard error.

## Existence and uniqueness

**Constructive existence.** Exhibit the object. "There is an even prime": 2.

**Non-constructive existence.** Show that one must exist without saying which.

**Theorem.** There exist irrational $x,y$ with $x^y$ rational.

*Proof.* Consider $\sqrt2^{\sqrt2}$. If it is rational, take $x=y=\sqrt2$. If it is irrational, take $x=\sqrt2^{\sqrt2}$ and $y=\sqrt2$; then $x^y=\sqrt2^{\,2}=2$. Either way such a pair exists. $\blacksquare$

The proof does not tell you which case holds.

**Uniqueness.** Suppose two objects both have the property and show they are equal.

*Example.* The additive identity is unique: if $0$ and $0'$ both satisfy $x+0=x$ and $x+0'=x$ for all $x$, then $0=0+0'=0'$.

## Disproof by counterexample

To disprove $\forall x\,P(x)$, give one $x$ where $P(x)$ fails.

*Claim:* every prime is odd. *Counterexample:* 2.
*Claim:* if $a\mid bc$ then $a\mid b$ or $a\mid c$. *Counterexample:* $6\mid2\cdot3$ but $6\nmid2$ and $6\nmid3$. (The claim is true when $a$ is prime.)

## If and only if

Prove both directions separately. Label them.

**Theorem.** $n$ is even if and only if $n^2$ is even.

*Proof.* ($\Rightarrow$) If $n=2k$ then $n^2=2(2k^2)$ is even. ($\Leftarrow$) Proved above by contrapositive. $\blacksquare$

## Choosing a strategy

| The statement looks like | Try |
|---|---|
| if $p$ then $q$, and $p$ is easy to unpack | direct |
| the conclusion is a negative ("is not", "has no") | contrapositive or contradiction |
| "irrational", "infinitely many", "no such object exists" | contradiction |
| natural split (even/odd, sign, remainder) | cases |
| "for all $n\ge n_0$" over the natural numbers | induction ([[DM 06 Induction and Recursion]]) |
| "there exists" | construct an example |
| you suspect it is false | hunt for a small counterexample |

## How to write a proof

1. State what you are assuming and what you will show.
2. Introduce every variable: "Let $n$ be an integer."
3. Write in full sentences. Equations are part of sentences.
4. Justify each step ("by definition", "by the previous theorem").
5. End by stating that the conclusion has been reached.

## Common mistakes

- **Assuming what you want to prove.** Starting from the conclusion and reaching "$1=1$" proves nothing unless every step is reversible.
- **Proving by example.**
- **Reusing a letter.** Writing both odd numbers as $2k+1$ assumes they are equal.
- **Proving the converse** instead of the statement.
- **Dividing by something that might be zero.**

## Learn by doing

1. Prove directly: the product of two odd integers is odd.
2. Prove by contrapositive: if $3n+2$ is odd then $n$ is odd.
3. Prove by contradiction: there is no largest even integer.
4. Disprove: for all real $x$, $x^2\ge x$.

> [!success]- Check your answers
> 1. $(2a+1)(2b+1)=4ab+2a+2b+1=2(2ab+a+b)+1$, odd.
> 2. Contrapositive: if $n$ is even then $3n+2$ is even. $n=2k$ gives $3n+2=6k+2=2(3k+1)$.
> 3. Suppose $N$ is the largest even integer. Then $N+2$ is even and larger. Contradiction.
> 4. $x=0.5$: $0.25<0.5$.

## Where this shows up

Proofs of algorithm correctness, convergence guarantees in optimization, and stability arguments in control are all built from these moves. Reading a research paper's theorem starts with identifying its quantifiers ([[DM 02 Predicates and Quantifiers]]) and its proof strategy.

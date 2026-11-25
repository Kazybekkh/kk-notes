---
type: course-chapter
course: discrete-mathematics
chapter: 8
tags: [mathematics, discrete-mathematics, number-theory]
---
ata# DM 08 Number theory and modular arithmetic

Previous: [[DM 07 Counting]] | [[DM 00 Course Map]] | Next: [[DM 09 Recurrences and Asymptotics]]

> [!abstract] One sentence
> Number theory studies how integers divide one another, and modular arithmetic, the arithmetic of remainders, turns that study into a number system where cryptography and hashing live.

## Divisibility

For integers $a\neq0$ and $b$, $a$ **divides** $b$, written $a\mid b$, when $b=ak$ for some integer $k$.

$3\mid12$, $5\nmid12$, and $a\mid0$ for every $a$.

Basic facts, each a one-line proof from the definition:

- If $a\mid b$ and $b\mid c$ then $a\mid c$.
- If $a\mid b$ and $a\mid c$ then $a\mid(bx+cy)$ for any integers $x,y$.

The second says a common divisor of two numbers divides every integer combination of them. It powers everything below.

## Division with remainder

**Division algorithm.** For any integer $a$ and positive integer $n$, there are unique integers $q$ (quotient) and $r$ (remainder) with

$$
a=qn+r,\qquad0\le r<n.
$$

$17=3\cdot5+2$, so $17\bmod5=2$. For negatives, the remainder is still non-negative: $-7=(-2)\cdot5+3$, so $-7\bmod5=3$.

> [!warning] Negative remainders in code
> Python's `%` follows the mathematical convention (`-7 % 5 == 3`). C, C++ and Java return `-2`. Know which your language does.

## Primes

A **prime** is an integer greater than 1 whose only positive divisors are 1 and itself: $2,3,5,7,11,13,\dots$ Other integers greater than 1 are **composite**.

**Fundamental theorem of arithmetic.** Every integer greater than 1 is a product of primes in exactly one way, apart from the order of the factors.

$$
360=2^3\cdot3^2\cdot5.
$$

Existence was proved by strong induction in [[DM 06 Induction and Recursion]]. Primes are the atoms of multiplication. There are infinitely many of them ([[DM 03 Proof Techniques]]).

**Testing primality by hand.** If $n$ is composite it has a factor at most $\sqrt n$, so check divisibility by primes up to $\sqrt n$. Is 97 prime? $\sqrt{97}<10$; it is not divisible by 2, 3, 5 or 7. Yes.

## Greatest common divisor

$\gcd(a,b)$ is the largest integer dividing both. $\gcd(12,18)=6$. If $\gcd(a,b)=1$ the numbers are **coprime**: they share no prime factor.

The **least common multiple** satisfies $\gcd(a,b)\cdot\operatorname{lcm}(a,b)=ab$ for positive integers. $\operatorname{lcm}(12,18)=216/6=36$.

## The Euclidean algorithm

Factoring large numbers is hard, but the gcd can be found quickly without factoring.

**Key fact.** $\gcd(a,b)=\gcd(b,\;a\bmod b)$.

*Why.* Write $a=qb+r$. Any common divisor of $a$ and $b$ divides $r=a-qb$. Any common divisor of $b$ and $r$ divides $a=qb+r$. So the pairs $(a,b)$ and $(b,r)$ have exactly the same common divisors.

Repeat until the remainder is 0. The last nonzero remainder is the gcd.

**Worked example.** $\gcd(252,198)$:

$$
\begin{aligned}
252&=1\cdot198+54\\
198&=3\cdot54+36\\
54&=1\cdot36+18\\
36&=2\cdot18+0
\end{aligned}
$$

So $\gcd(252,198)=18$.

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

The remainder at least halves every two steps, so the number of steps is proportional to the number of digits. It is one of the oldest algorithms still in daily use.

## Bézout's identity

For any integers $a,b$ there exist integers $x,y$ with

$$
ax+by=\gcd(a,b).
$$

Find them by running the Euclidean algorithm backwards (the **extended** Euclidean algorithm). From the example:

$$
18=54-36=54-(198-3\cdot54)=4\cdot54-198=4(252-198)-198=4\cdot252-5\cdot198.
$$

Check: $1008-990=18$.

Consequence (**Euclid's lemma**): if a prime $p$ divides $ab$, then $p\mid a$ or $p\mid b$. This is what makes prime factorization unique.

## Modular arithmetic

$a$ and $b$ are **congruent modulo $n$** when they leave the same remainder on division by $n$, equivalently when $n\mid(a-b)$:

$$
a\equiv b\pmod n.
$$

$17\equiv2\pmod5$. $-1\equiv4\pmod5$. $38\equiv2\pmod{12}$: 38 hours after 12 o'clock the clock shows 2.

Congruence mod $n$ is an equivalence relation ([[DM 05 Functions and Relations]]) with $n$ classes, represented by the remainders $0,1,\dots,n-1$.

**Arithmetic respects congruence.** If $a\equiv a'$ and $b\equiv b'\pmod n$ then

$$
a+b\equiv a'+b',\qquad a-b\equiv a'-b',\qquad ab\equiv a'b'\pmod n.
$$

So you may reduce at any stage of a calculation. Numbers never need to get large.

**Worked example.** Last digit of $7^{100}$, that is $7^{100}\bmod10$. Powers of 7 mod 10: $7,9,3,1,7,\dots$, repeating with period 4. Since $100=4\cdot25$, $7^{100}=(7^4)^{25}\equiv1^{25}=1$. The last digit is 1.

**Worked example.** Is 123456 divisible by 9? Since $10\equiv1\pmod9$, every power of 10 is $\equiv1$, so a number is congruent to its digit sum mod 9. $1+2+3+4+5+6=21\equiv3$. Not divisible; the remainder is 3. This is the old trick of "casting out nines".

## Division: modular inverses

Addition, subtraction and multiplication work freely. Division does not: $2\cdot1\equiv2\cdot4\pmod6$, but $1\not\equiv4$. You cannot cancel the 2.

An **inverse** of $a$ modulo $n$ is a number $a^{-1}$ with $a\,a^{-1}\equiv1\pmod n$.

> [!important] When inverses exist
> $a$ has an inverse modulo $n$ exactly when $\gcd(a,n)=1$.

*Why.* By Bézout, $\gcd(a,n)=1$ gives $ax+ny=1$, so $ax\equiv1\pmod n$ and $x$ is the inverse. The extended Euclidean algorithm computes it.

**Example.** Inverse of 3 mod 7: $3\cdot5=15\equiv1$, so $3^{-1}\equiv5$. To solve $3x\equiv4\pmod7$, multiply by 5: $x\equiv20\equiv6$. Check: $18\equiv4$.

If $n=p$ is prime, every nonzero residue has an inverse. The integers mod $p$ then form a **field**: a number system where all four operations work, like the rationals or the reals, but finite.

## Fast exponentiation

To compute $a^e\bmod n$ for huge $e$, use **repeated squaring**. Example: $3^{13}\bmod7$, with $13=8+4+1$:

$$
3^1\equiv3,\quad3^2\equiv2,\quad3^4\equiv4,\quad3^8\equiv16\equiv2,
$$

$$
3^{13}=3^8\cdot3^4\cdot3^1\equiv2\cdot4\cdot3=24\equiv3\pmod7.
$$

About $\log_2e$ squarings instead of $e$ multiplications. In Python: `pow(3, 13, 7)`.

## Fermat's little theorem

If $p$ is prime and $p\nmid a$:

$$
a^{p-1}\equiv1\pmod p.
$$

Check: $3^6=729=104\cdot7+1$. A consequence is that $a^{p-2}$ is the inverse of $a$ mod $p$, and exponents can be reduced mod $p-1$: $3^{13}\equiv3^{13\bmod6}=3^1=3$, matching the calculation above.

## Why this matters: public-key cryptography

RSA in outline:

1. Pick two large primes $p,q$. Publish $n=pq$. Keep $p$ and $q$ secret.
2. Pick a public exponent $e$ coprime to $(p-1)(q-1)$. Compute the private $d$ as the inverse of $e$ modulo $(p-1)(q-1)$.
3. Encrypt a message $m$ as $c=m^e\bmod n$. Decrypt as $m=c^d\bmod n$.

Every tool in this chapter appears: primes, the extended Euclidean algorithm for $d$, fast exponentiation, and a generalization of Fermat's theorem to show decryption undoes encryption. Security rests on an asymmetry: multiplying two primes is easy, while factoring their product is believed to be infeasible at sufficient size.

## Common mistakes

- **Dividing in a congruence** without checking that the divisor is coprime to the modulus.
- **Forgetting that remainders are non-negative** in the mathematical convention.
- **Confusing $a\bmod n$ (a number) with $a\equiv b\pmod n$ (a relationship).**
- **Calling 1 a prime.** It is excluded so that factorization is unique.

## Learn by doing

1. Find $\gcd(84,36)$ with the Euclidean algorithm, and integers $x,y$ with $84x+36y=\gcd$.
2. Compute $2^{10}\bmod11$ and $-17\bmod5$.
3. Find the inverse of 5 modulo 12, and solve $5x\equiv3\pmod{12}$.
4. Does 4 have an inverse modulo 10? Why?
5. What is the last digit of $3^{2026}$?

> [!success]- Check your answers
> 1. $84=2\cdot36+12$, $36=3\cdot12+0$: gcd 12. $12=84-2\cdot36$, so $x=1$, $y=-2$.
> 2. $1024=93\cdot11+1$, so $1$ (as Fermat predicts). $-17=-4\cdot5+3$, so $3$.
> 3. $5\cdot5=25\equiv1$, so the inverse is 5. $x\equiv15\equiv3$. Check: $15\equiv3\pmod{12}$.
> 4. No: $\gcd(4,10)=2\neq1$. Multiples of 4 mod 10 are only $0,2,4,6,8$.
> 5. Powers of 3 mod 10 cycle $3,9,7,1$ with period 4. $2026\bmod4=2$, so the last digit is 9.

## Where this shows up

Hash tables, checksums, random number generators and all of public-key cryptography. Angles wrap around modulo $2\pi$, which is modular arithmetic on the reals: a joint at $359^\circ$ and one at $1^\circ$ are $2^\circ$ apart, a detail that breaks naive angle losses in robot learning ([[02 Geometry and Kinematics]]).

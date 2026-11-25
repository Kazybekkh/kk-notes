---
type: course-chapter
course: discrete-mathematics
chapter: 2
tags: [mathematics, discrete-mathematics, logic]
---
# DM 02 Predicates and quantifiers

Previous: [[DM 01 Logic and Propositions]] | [[DM 00 Course Map]] | Next: [[DM 03 Proof Techniques]]

> [!abstract] One sentence
> A predicate is a statement with a blank in it, and the quantifiers "for all" and "there exists" turn it into a definite claim; the order of quantifiers changes the meaning, and negation swaps them.

## Predicates

"$x>3$" is neither true nor false until $x$ has a value. It is a **predicate**: a statement containing variables that becomes a proposition once values are substituted.

Write $P(x)$ for "$x>3$". Then $P(5)$ is true and $P(1)$ is false. A predicate can have several variables: $Q(x,y)$ for "$x<y$".

The **domain** is the set of values the variable may take. It must be stated or clear from context, because the truth of a quantified statement depends on it.

## The two quantifiers

**Universal: $\forall$ ("for all", "for every").**

$$
\forall x\,P(x)
$$

True when $P(x)$ holds for **every** $x$ in the domain. A single failure makes it false.

**Existential: $\exists$ ("there exists", "for some").**

$$
\exists x\,P(x)
$$

True when $P(x)$ holds for **at least one** $x$ in the domain.

**Examples** with domain $\mathbb R$:

- $\forall x\,(x^2\ge0)$: true.
- $\forall x\,(x^2>0)$: false. Counterexample: $x=0$.
- $\exists x\,(x^2=2)$: true ($x=\sqrt2$).
- $\exists x\,(x^2=-1)$: false.

Change the domain to the integers and $\exists x\,(x^2=2)$ becomes false. The domain is part of the statement.

On a finite domain $\{a,b,c\}$, $\forall$ is a big "and" and $\exists$ is a big "or":

$$
\forall x\,P(x)\equiv P(a)\land P(b)\land P(c),\qquad\exists x\,P(x)\equiv P(a)\lor P(b)\lor P(c).
$$

In Python: `all(P(x) for x in domain)` and `any(P(x) for x in domain)`.

## How to prove or disprove

| Statement | To prove it | To disprove it |
|---|---|---|
| $\forall x\,P(x)$ | argue for an arbitrary $x$ | exhibit one **counterexample** |
| $\exists x\,P(x)$ | exhibit one example | argue that every $x$ fails |

Examples never prove a universal statement. Checking that $n^2+n+41$ is prime for $n=0,1,\dots,39$ does not prove it for all $n$; it fails at $n=40$, which gives $41^2$.

## Negating quantifiers

Negation flips the quantifier and negates the inside:

$$
\neg\,\forall x\,P(x)\;\equiv\;\exists x\,\neg P(x),\qquad
\neg\,\exists x\,P(x)\;\equiv\;\forall x\,\neg P(x).
$$

These are De Morgan's laws stretched over a whole domain.

- "Not everyone passed" $\equiv$ "Someone did not pass."
- "Nobody passed" (there does not exist someone who passed) $\equiv$ "Everyone failed."

> [!warning] The negation of "all are" is not "none are"
> The negation of "all swans are white" is "at least one swan is not white", not "no swans are white".

## Restricted quantifiers

"Every positive number has a positive square root" restricts the domain. The translations differ for the two quantifiers:

$$
\forall x>0\;P(x)\quad\text{means}\quad\forall x\,(x>0\to P(x)),
$$

$$
\exists x>0\;P(x)\quad\text{means}\quad\exists x\,(x>0\land P(x)).
$$

"All" pairs with **implies**; "some" pairs with **and**. Mixing them up is a classic error: $\exists x\,(x>0\to P(x))$ is true as soon as any non-positive number exists, which says nothing useful.

## Nested quantifiers: order matters

With two variables, the order of different quantifiers changes the meaning. Let the domain be the real numbers.

$$
\forall x\,\exists y\,(x+y=0)
$$

"For every $x$ there is a $y$ (which may depend on $x$) with $x+y=0$." True: take $y=-x$.

$$
\exists y\,\forall x\,(x+y=0)
$$

"There is one single $y$ that works for every $x$." False: no number is the negative of all numbers.

**Read left to right, as a game.** For $\forall x\,\exists y$, an opponent picks $x$ first and then you pick $y$ knowing their choice. For $\exists y\,\forall x$, you must commit to $y$ first, and then the opponent picks $x$ to defeat you. Going first is harder, so $\exists y\,\forall x$ is the stronger claim: it implies $\forall x\,\exists y$ but not the reverse.

**Everyday example.** "Everyone has a mother" is $\forall p\,\exists m$: true. "There is someone who is everyone's mother" is $\exists m\,\forall p$: false.

Two quantifiers of the *same* kind can be swapped freely: $\forall x\,\forall y\equiv\forall y\,\forall x$.

## Negating nested quantifiers

Work from the outside in, flipping each quantifier, and negate the innermost statement.

$$
\neg\,\forall x\,\exists y\,P(x,y)\;\equiv\;\exists x\,\forall y\,\neg P(x,y).
$$

**Worked example: the definition of a limit.** "$f(x)\to L$ as $x\to a$" means

$$
\forall\varepsilon>0\;\exists\delta>0\;\forall x\;\big(0<|x-a|<\delta\to|f(x)-L|<\varepsilon\big).
$$

Its negation ("$f$ does not tend to $L$"):

$$
\exists\varepsilon>0\;\forall\delta>0\;\exists x\;\big(0<|x-a|<\delta\;\land\;|f(x)-L|\ge\varepsilon\big).
$$

Each quantifier flipped, and the implication became "hypothesis and not conclusion" ([[DM 01 Logic and Propositions]]). In words: there is some tolerance that cannot be met, however close you look.

## Translating English

| English | Logic |
|---|---|
| Every student passed. | $\forall x\,(S(x)\to P(x))$ |
| Some student passed. | $\exists x\,(S(x)\land P(x))$ |
| No student passed. | $\forall x\,(S(x)\to\neg P(x))$ |
| Not every student passed. | $\exists x\,(S(x)\land\neg P(x))$ |
| Exactly one $x$ satisfies $P$. | $\exists x\,\big(P(x)\land\forall y\,(P(y)\to y=x)\big)$ |

English is often ambiguous. "Every robot has a sensor that failed" could mean each has its own failed sensor ($\forall r\,\exists s$) or one shared sensor failed on all ($\exists s\,\forall r$). Writing the quantifiers forces you to decide.

## Common mistakes

- **Swapping $\forall\exists$ with $\exists\forall$.**
- **Using $\land$ with $\forall$ or $\to$ with $\exists$** when restricting the domain.
- **Negating only the predicate** and forgetting to flip the quantifier.
- **Proving a universal claim with examples.**

## Learn by doing

1. Domain: integers. True or false? (a) $\forall x\,\exists y\,(y>x)$ (b) $\exists y\,\forall x\,(y>x)$ (c) $\forall x\,\exists y\,(xy=1)$.
2. Negate: "Every robot in the lab has at least one working camera."
3. Translate using predicates $R(x)$ "x is a robot" and $C(x)$ "x has a camera": "Some robots do not have a camera."
4. Find a counterexample to $\forall n\in\mathbb N\;(2^n\ge n^2)$.

> [!success]- Check your answers
> 1. (a) True, $y=x+1$. (b) False, there is no largest integer. (c) False: $x=2$ has no integer inverse (and $x=0$ has none at all).
> 2. "Some robot in the lab has no working camera."
> 3. $\exists x\,(R(x)\land\neg C(x))$.
> 4. $n=3$: $8<9$.

## Where this shows up

Every definition and theorem in the [[LA 00 Course Map]] and [[PS 00 Course Map]] courses is a quantified statement: "linearly independent" hides a $\forall$ over coefficients, and "there is a solution" is an $\exists$. Specifications such as "for every start state, the controller eventually reaches the goal" are nested quantifiers.

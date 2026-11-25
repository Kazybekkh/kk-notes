---
type: course-chapter
course: discrete-mathematics
chapter: 1
tags: [mathematics, discrete-mathematics, logic]
---
# DM 01 Logic and propositions

[[DM 00 Course Map]] | Next: [[DM 02 Predicates and Quantifiers]]

> [!abstract] One sentence
> Propositional logic gives exact meanings to "not", "and", "or" and "if-then", so that the truth of a compound statement can be computed from the truth of its parts.

## Propositions

A **proposition** is a statement that is either true or false, never both.

- "7 is prime." Proposition (true).
- "$2+2=5$." Proposition (false).
- "Close the door." Not a proposition (a command).
- "$x>3$." Not a proposition until $x$ is given a value ([[DM 02 Predicates and Quantifiers]]).

We name propositions with letters $p,q,r$ and build larger ones with **connectives**.

## The basic connectives

| Name | Symbol | Read as | True when |
|---|---|---|---|
| negation | $\neg p$ | not $p$ | $p$ is false |
| conjunction | $p\land q$ | $p$ and $q$ | both are true |
| disjunction | $p\lor q$ | $p$ or $q$ | at least one is true |
| exclusive or | $p\oplus q$ | $p$ xor $q$ | exactly one is true |

A **truth table** lists the value of a compound statement for every combination of inputs. With $n$ variables there are $2^n$ rows.

| $p$ | $q$ | $p\land q$ | $p\lor q$ | $p\oplus q$ |
|---|---|---|---|---|
| T | T | T | T | F |
| T | F | F | T | T |
| F | T | F | T | T |
| F | F | F | F | F |

Mathematical "or" is **inclusive**: $p\lor q$ is true when both are. English "or" is often exclusive ("tea or coffee?"). When in doubt, the mathematical default is inclusive.

## Implication

$p\to q$ reads "if $p$ then $q$". $p$ is the **hypothesis**, $q$ the **conclusion**.

| $p$ | $q$ | $p\to q$ |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

It is false in exactly one case: the hypothesis holds and the conclusion fails.

**Why is it true when $p$ is false?** Think of a promise: "If it rains, I will bring an umbrella." The only way I break it is if it rains and I bring none. If it does not rain, I have kept my word whatever I carry. An implication makes a claim only about the cases where the hypothesis holds; elsewhere it is **vacuously true**.

A second way to see it: "every multiple of 4 is even" should be true. Written as "if $n$ is a multiple of 4 then $n$ is even", it must hold for $n=3$ (F, F) and $n=6$ (F, T) as well. Those rows have to be T.

Useful equivalent form:

$$
p\to q\;\equiv\;\neg p\lor q.
$$

**Many phrasings, one meaning.** All of these say $p\to q$: "if $p$ then $q$"; "$p$ implies $q$"; "$q$ if $p$"; "$p$ only if $q$"; "$p$ is sufficient for $q$"; "$q$ is necessary for $p$".

## Converse, inverse, contrapositive

Starting from $p\to q$:

| Name | Form | Equivalent to the original? |
|---|---|---|
| contrapositive | $\neg q\to\neg p$ | **yes, always** |
| converse | $q\to p$ | no |
| inverse | $\neg p\to\neg q$ | no (it is the contrapositive of the converse) |

**Example.** "If it is a dog, then it is a mammal." (True.)

- Contrapositive: "If it is not a mammal, then it is not a dog." True.
- Converse: "If it is a mammal, then it is a dog." False.

Confusing a statement with its converse is the most common logical error in everyday reasoning. The equivalence with the contrapositive is a proof technique in its own right ([[DM 03 Proof Techniques]]).

## Biconditional

$p\leftrightarrow q$, "$p$ if and only if $q$" (often written "iff"), is true when $p$ and $q$ have the same truth value. It means $(p\to q)\land(q\to p)$. To prove an "if and only if", prove both directions.

## Logical equivalence

Two statements are **logically equivalent**, written $\equiv$, when they have the same truth table. The important laws:

| Law | Statement |
|---|---|
| double negation | $\neg\neg p\equiv p$ |
| De Morgan | $\neg(p\land q)\equiv\neg p\lor\neg q$ |
| De Morgan | $\neg(p\lor q)\equiv\neg p\land\neg q$ |
| distributive | $p\land(q\lor r)\equiv(p\land q)\lor(p\land r)$ |
| distributive | $p\lor(q\land r)\equiv(p\lor q)\land(p\lor r)$ |
| implication | $p\to q\equiv\neg p\lor q$ |
| negated implication | $\neg(p\to q)\equiv p\land\neg q$ |
| contrapositive | $p\to q\equiv\neg q\to\neg p$ |

**De Morgan in words.** "It is not the case that both are true" means "at least one is false". "It is not the case that either is true" means "both are false". Negation flips *and* into *or*.

In code: `not (a and b)` is `(not a) or (not b)`.

**Negating an implication.** The negation of "if $p$ then $q$" is **not** another if-then. It is "$p$ holds and yet $q$ fails": a counterexample.

**Worked example: verify by truth table** that $p\to q\equiv\neg p\lor q$.

| $p$ | $q$ | $\neg p$ | $\neg p\lor q$ | $p\to q$ |
|---|---|---|---|---|
| T | T | F | T | T |
| T | F | F | F | F |
| F | T | T | T | T |
| F | F | T | T | T |

The last two columns match.

## Tautologies and contradictions

A **tautology** is true in every row: $p\lor\neg p$. A **contradiction** is false in every row: $p\land\neg p$. A statement is **satisfiable** if at least one row makes it true. Deciding satisfiability for large formulas (SAT) is a famous hard problem and the basis of modern verification tools.

## Valid arguments

An argument is **valid** when the conclusion is true in every case where all the premises are true. Two valid patterns and two invalid look-alikes:

| Pattern | Form | Valid? |
|---|---|---|
| modus ponens | $p\to q$, $p$, therefore $q$ | yes |
| modus tollens | $p\to q$, $\neg q$, therefore $\neg p$ | yes |
| affirming the consequent | $p\to q$, $q$, therefore $p$ | **no** |
| denying the antecedent | $p\to q$, $\neg p$, therefore $\neg q$ | **no** |

"If it rains, the ground is wet. The ground is wet. So it rained." Invalid: a sprinkler would do.

Validity concerns form, not truth. A valid argument with a false premise can have a false conclusion.

## Common mistakes

- **Reading $p\to q$ as "$p$ causes $q$".** It is only a statement about truth values.
- **Assuming the converse.**
- **Negating "and" without flipping it to "or".**
- **Treating "or" as exclusive.**

## Learn by doing

1. Build the truth table of $(p\land q)\to p$. What kind of statement is it?
2. Write the contrapositive and the negation of "If a number is divisible by 6, then it is divisible by 3."
3. Simplify $\neg(p\lor\neg q)$ using De Morgan.
4. "If the sensor fails, the robot stops. The robot stopped." What can you conclude?

> [!success]- Check your answers
> 1. True in all four rows: a tautology.
> 2. Contrapositive: "If a number is not divisible by 3, then it is not divisible by 6." Negation: "Some number is divisible by 6 and not divisible by 3."
> 3. $\neg p\land q$.
> 4. Nothing about the sensor. Concluding that it failed would be affirming the consequent.

## Where this shows up

Every `if` condition, database query and safety interlock is a propositional formula. Logic gates implement these connectives in hardware ([[DM 12 Boolean Algebra and Automata]]).

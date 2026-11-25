## Predicate Logic 

- Variables
- Predicates
- Quantifiers

- E.g: (Predicate Logic)
	- Let P(x) denote "x>0", then
		- $P(3) \lor P(-1)$ is true
		- $P(3) \land P(-1)$ is false
		- $P(3) \lor P(y)$ is NOT a proposition

- (E.g. 2) Predicate Logic
	- Let Q(x, y) denote "x = y + 3", then
		- Q(1,2) is false
		- Q(3,0) is true

## Quantifiers

We need **quantifiers** to express the meaning of words including **all** and **some**.
- Universal Quantifiers $\forall x$. $P(x)$ asserts P(x) is true for every x in the domain
- Existential Quantifier $\exists x$ asserts P(x) is true for some x in the domain
 
E.g (quantifier):
If P(x) denotes "x is even" and U the integers, then
- $\forall x$. P(x) is false. but
- $\exists x$. P(x) is true

The domain is often denoted by U for universe of discourse

Example (precedence)
$\forall x. P(x) \lor Q(x)$ means  $(\forall x. P(x)\lor Q(x)$)

## Domain

The truth values of $\exists x. P(x)$ and $\forall x$. P(x) depend on both
- the predicate P(x) and
- the domain U
Example (Quantifiers):
- If U is the positive integers and P(x) is the statement "x<2", then $\exists x. P(x)$ is true, but $\forall x. P(x)$ is false.
-  If U is the negative integers and P(x) is the statement "x<2", then both $\exists x. P(x)$ is and $\forall x. P(x)$ are true.

## Nested Quantifiers

Nested Quantifiers are often necessary to express the meaning of sentences in English as well as important concepts in Computer Science and mathematics

E.g:
$$\forall x \exists y. (x+y=0)$$
where the domains of x and y are the integers.

Let $Q(x,y)$ denote "x+y=0" and assume that U is the integers. What is truth value of $$\exists\ y \forall x. Q(x, y)$$
it is False

- $\forall x \exists y$ Q(x, y) is true, but
- $\exists y\forall x$ Q(x, y) is false

## Equivalences in Predicate Logic

Two statements S and T involving predicates and quanrtifiers are logically equivalent, denoted S \equiv T, if and only if they have the same truth value
- for every predicate substitute statements
- for every domain of discourse used for the variables in the expressions

E.g( Equivalences)
- If U consists of the integers 1,2 and 3:
	- $\forall x P(x) \equiv P(1) \land P(2) \land P(3)$
	- $\exists x P(x) \equiv P(1) \lor P(2) \lor P(3)$

## De Morgan's Laws for Quantifiers
$$\neg(\forall x. P(x))\equiv \exists x. \neg P(x)$$
$$\neg(\exists x. P(x))\equiv \forall x. \neg P(x)$$

**Example (De Morgan's Laws for Quantifiers)**
- **Not every** student in your class who **has** taken a course in Java
- means **every** student in your class **has not** taken Java


# Propositions 

*A proposition is a declarative statement that is either true or false*
- **is a proposition**
	- "The moon is made of green cheese"
	- 1+0=1
	- 0+0=2
- **Is NOT a proposition**
	- "Sit down"
	- "x+1 = 2" (because x is unknown, not enough info to be assigned true or false)

- **Atomic Propositions**
	- Variables: $p, q, r, s, ...$
	- Constants: $X, Y, Z$
- **Compound Propositions**
	- Negation: $\neg$
	- Conjunction: $P\land Q$
	- Disjunction: $P\lor Q$
	- Implication: $P \implies Q$
	- Bi-conditional: $P \Leftrightarrow Q$

Negation: "not"

| $P$ | $\neg P$ |     |
| --- | -------- | --- |
| T   | F        |     |
| T   | F        |     |

Disjunction: $OR$

| $P$ | $Q$ | $P \lor Q$ |     |
| --- | --- | ---------- | --- |
| T   | T   | T          |     |
| T   | F   | T          |     |
| F   | T   | T          |     |
| F   | F   | F          |     |

Conjunction: $AND$

| $P$ | $Q$ | $P \land Q$ |
| --- | --- | ----------- |
| T   | T   | T           |
| T   | F   | F           |
| F   | T   | F           |
| F   | F   | F           |

Exclusive OR ($XOR$):

| $P$ | $Q$ | $P \oplus Q$ |
| --- | --- | ------------ |
| T   | T   | F            |
| T   | F   | T            |
| F   | T   | T            |
| F   | F   | F            |

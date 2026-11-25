date: (23/09/2024)

# Compound Propositions

*Implication*

- If $p$ and $q$ are propositions, then $p \to q$ is a **conditional statement** or **implication**.
	- $p$ is the hypothesis (antecedent or premise)
	- $q$ is the conclusion (or consequence)

| $p$ | $q$ | $p \to q$ |
| --- | --- | --------- |
| T   | T   | T         |
| T   | F   | F         |
| F   | T   | T         |
| F   | F   | T         |

*Converse, Contrapositive and Inverse*
From $p \to q$ we can form new conditional statements:
- $p\to q$ is its **converse**
- $\neg q \to \neg p$ is its **contrapositive**
- $\neg p \to \neg q$ is its **inverse**

*Example:*

| **Converse**       | "If I do not go to town, then it is raining"   |
| ------------------ | ---------------------------------------------- |
| **Inverse**        | "If it is not raining, then I will go to town" |
| **Contrapositive** | "If I go to town, then it is not raining"      |

*Biconditional*
if  $p$ and $q$ are propositions, then we can form the **bi-conditional** proposition $p\Leftrightarrow q$
with this truth table

| $p$ | $q$ | $p \leftrightarrow q$ |
| --- | --- | --------------------- |
| T   | T   | T                     |
| T   | F   | F                     |
| F   | T   | F                     |
| F   | F   | T                     |

## Truth tables for compound propositions

We can construct a truth table for compound propositions as follows:
- Create a **row** for ever combo of values for **atomic propositions**
- Create a **column** containing truth value for each sub-expressions
Example( Truth table for $p \lor q \to \neg r$)

| $p$ | $q$ | $r$ | $\neg r$ | $p \lor q$ | $p \lor q \to \neg r$ |
| --- | --- | --- | -------- | ---------- | --------------------- |
| T   | T   | T   | F        | T          | F                     |
| T   | T   | F   | T        | T          | T                     |
| T   | F   | T   | F        | T          | F                     |
| T   | F   | F   | T        | T          | T                     |
| F   | T   | T   | F        | T          | F                     |
| F   | F   | T   | F        | F          | T                     |
| F   | F   | F   | T        | F          | T                     |

Note: (if (False) $\to$ (True))

## Terminology and Precedence

- A **tautology** is a preposition which is always **true**, such as $P \lor \neg P$
- A **contradiction** is a preposition which is always **false**, such as $P\land \neg P$
- A **contingency** is a proposition which is neither a tautology nor a contradiction, such as $P$

## Precedence of Logical Operators 

- Negation > Conjunction > Disjunction > Implication > Bi-conditional
E.g $P \lor Q \implies \neg R$ is equivalent to $(P\lor Q)\implies (\neg R)$

## Equivalent Propositions

Two propositions $P$ and $Q$ are equivalent, denoted as $P\equiv Q$, if they always have the same truth value.
- This is the same as saying $P\leftrightarrow Q$ is a **tautology**
- Note the there are $2^n$ rows in a truth table with $n$ propositional variables\

| $p$ | $q$ | $\neg p$ | $\neg q$ | $p\to q$ | Contrapositive<br>$\neg q \to \neg p$ | Inverse<br>$\neg p \to \neg q$ | Converse<br>$q\to p$ |     |
| --- | --- | -------- | -------- | -------- | ------------------------------------- | ------------------------------ | -------------------- | --- |
| T   | T   | F        | F        | T        | T                                     | T                              | T                    |     |
| T   | F   | F        | T        | F        | F                                     | T                              | T                    |     |
| F   | T   | T        | F        | T        | T                                     | F                              | F                    |     |
| F   | F   | T        | T        | T        | T                                     | T                              | T                    |     |

## Key logical Equivalences

- Identity Law: $$p \land \textbf{T} \equiv p, (\text{where \textbf{T=True, or F=False}})$$
- Domination Law: $$p \lor \textbf{T} \equiv \textbf{T}$$
- Idempotent Law: $$p \lor p \equiv p$$
- Double Negation Law: $$\neg(\neg p)\equiv p$$
- Negation Law: $$p\lor \neg p \equiv \textbf{T}$$
- Commutative Law: $$p\lor q \equiv q \lor p$$
- Associative Law: $$(p\land q)\land r\equiv p \land(q \land r)$$
- Distributive Law: $$p\lor(q\land r)\equiv (p\lor q)\land(p\lor r)$$
- Absorption Law: $$p \lor (q \land q)\equiv p$$
- De Morgan's Law: $$\neg(p\land q)\equiv \neg p \lor \neg q$$

## More logical Equivalences

### Conditional Statements

- $p\to q \equiv \neg p \lor q$
- $p\to q \equiv \neg q \to \neg p$
- $p\lor q \equiv \neg p \to q$
- $p \land q  \equiv \neg (p \to \neg q)$
- $(p\to q) \land (p\to r) \equiv p \to (q \land r)$
- $(p\to r) \land (q\to r) \equiv (p\land q)\to r$
- $(p \to q) \lor (p \to r) \equiv p \to (q \lor r)$
- $(p \to r) \lor (q \to r) \equiv (p \land q) \to r$

### Bi-conditional Statements

- $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$
- $p \leftrightarrow q \equiv \neg p \leftrightarrow \neg q$
- $p \leftrightarrow q \equiv (p\land q)\lor (\neg p \land \neg q)$
- $\neg (p\leftrightarrow q)\equiv p \leftrightarrow \neg q$

### Properties of Equality

- If $p \equiv q$ and $q \equiv r$, then $p\equiv r$
- If $q$ is a sub-expression of $p$ and $q \equiv q'$ and $p'$ the expression in which $q$ is replaced by $q'$  in p, then $p\equiv p'$

To prove that $A\equiv B$
	$$(\neg(p\lor(\neg p \land q))\equiv \neg p\land \neg q)$$


---
type: course-chapter
course: probability-statistics
chapter: 2
tags: [mathematics, probability, bayes]
---

# Chapter 2: Conditional probability and Bayes' rule

Previous: [[PS 01 Sample Spaces Events and Axioms]] | [[PS 00 Course Map]] | Next: [[PS 03 Discrete Random Variables]]

> [!abstract] The big idea
> Learning something new shrinks the set of possibilities. **Conditional probability** is probability recomputed inside that smaller world. **Bayes' rule** lets you turn "how likely is the evidence if the hypothesis is true?" into "how likely is the hypothesis, now that I have seen the evidence?". It is the engine of every system that updates its beliefs from data, from spam filters to robot localization.

> [!info] In this chapter you will learn to
> 1. Compute conditional probabilities from the definition and from tables.
> 2. Use the multiplication rule and probability trees for multi-step experiments.
> 3. Decide whether two events are independent.
> 4. Use the law of total probability to split a problem into cases.
> 5. Apply Bayes' rule, and avoid base-rate neglect and the prosecutor's fallacy.
> 6. Update beliefs repeatedly as evidence arrives.

> [!tip] Before you start
> You need events, the axioms and counting from [[PS 01 Sample Spaces Events and Axioms]].

---

## 2.1 Conditional probability

### The idea: shrinking the world

You roll a die. Before looking, $P(\text{roll}=2)=\tfrac16$. Now a friend peeks and says "it's even". The possible outcomes are now just $\{2,4,6\}$, all still equally likely. So the chance it is 2 becomes $\tfrac13$.

What happened: the new information **removed** the outcomes 1, 3, 5. We recomputed the probability **inside the remaining set**.

### The definition

> [!note] Definition: conditional probability
> For events $A$ and $B$ with $P(B)>0$,
> $$
> P(A\mid B)=\frac{P(A\cap B)}{P(B)}.
> $$
> Read: "the probability of $A$ **given** $B$".

**Why this formula.** Knowing $B$ happened, only the part of $A$ that lies **inside** $B$ can still happen: that is $A\cap B$. Then we **rescale** by $P(B)$ so that the new world $B$ has total probability 1 (axiom 2 in the new world).

In the sand picture: throw away all the sand outside $B$, then scale up what remains so it is one unit again.

**Die example:** $A=\{2\}$, $B=\{2,4,6\}$, $A\cap B=\{2\}$: $P(A\mid B)=\dfrac{1/6}{1/2}=\dfrac13$ ✓.

### Worked example 2.1: from a table

A survey of 200 robot test runs:

| | success | failure | total |
|---|---|---|---|
| bright lighting | 90 | 10 | 100 |
| dim lighting | 50 | 50 | 100 |
| total | 140 | 60 | 200 |

- $P(\text{success})=140/200=0.70$.
- $P(\text{success}\mid\text{bright})=90/100=0.90$: restrict to the bright row.
- $P(\text{success}\mid\text{dim})=50/100=0.50$.
- $P(\text{dim}\mid\text{failure})=50/60\approx0.83$: restrict to the failure column.

Conditioning means **choosing a row or column of the table and working only inside it**.

> [!warning] The order matters
> $P(\text{success}\mid\text{bright})=0.90$ but $P(\text{bright}\mid\text{success})=90/140\approx0.64$. These answer different questions. Confusing $P(A\mid B)$ with $P(B\mid A)$ is the single most common probability error.

> [!question]- Check yourself
> 1. Two dice. Given that the sum is 8, find the probability that the first die shows 3.
> 2. From the table, find $P(\text{bright}\mid\text{failure})$.
>
> **Answers.** 1. Sum 8: $(2,6),(3,5),(4,4),(5,3),(6,2)$. One has first die 3: $1/5$. 2. $10/60=1/6$.

---

## 2.2 The multiplication rule and trees

### The rule

Rearrange the definition:

> [!important] Multiplication rule
> $$
> P(A\cap B)=P(B)\,P(A\mid B)=P(A)\,P(B\mid A).
> $$
> For a chain of events:
> $$
> P(A\cap B\cap C)=P(A)\,P(B\mid A)\,P(C\mid A\cap B).
> $$

**In words:** the probability that several things all happen is the probability of the first, times the probability of the second **given the first**, and so on.

### Worked example 2.2: drawing without replacement

Draw two cards from a deck without putting the first back. $P(\text{both aces})$?

$$
P(\text{first ace})\times P(\text{second ace}\mid\text{first ace})=\frac4{52}\times\frac3{51}=\frac{12}{2652}=\frac1{221}.
$$

After one ace is drawn, 3 aces remain among 51 cards. The second probability is **conditional** on the first draw.

### Probability trees

For multi-stage experiments, draw a tree. Each branch is labelled with a conditional probability. **Multiply along a path** to get the probability of that path. **Add across paths** to combine outcomes.

**Worked example 2.3.** A bag has 3 red and 2 blue balls. Draw two without replacement.

```
                 R2  2/4   →  P(R,R) = 3/5 × 2/4 = 6/20
        R1  3/5 <
       /         B2  2/4   →  P(R,B) = 3/5 × 2/4 = 6/20
start <
       \         R2  3/4   →  P(B,R) = 2/5 × 3/4 = 6/20
        B1  2/5 <
                 B2  1/4   →  P(B,B) = 2/5 × 1/4 = 2/20
```

The four paths sum to $20/20=1$ ✓. $P(\text{one of each colour})=6/20+6/20=0.6$.

---

## 2.3 Independence

### The definition

Two events are independent when knowing one tells you **nothing** about the other.

> [!note] Definition: independence
> $A$ and $B$ are **independent** if
> $$
> P(A\cap B)=P(A)\,P(B).
> $$
> Equivalently (when $P(B)>0$): $P(A\mid B)=P(A)$.

The product form is preferred as the definition because it is symmetric and works even when a probability is zero.

**Examples.**

- Two coin flips: $P(HH)=\tfrac14=\tfrac12\times\tfrac12$. Independent.
- Two cards without replacement: not independent (the first draw changes the deck).
- In the lighting table: $P(\text{success})=0.7$ but $P(\text{success}\mid\text{dim})=0.5$. Not independent: lighting matters.

### Checking independence

**Worked example 2.4.** Roll one die. $A=\{2,4,6\}$ (even), $B=\{1,2,3,4\}$ (at most 4).

$P(A)=\tfrac12$, $P(B)=\tfrac23$, $A\cap B=\{2,4\}$ so $P(A\cap B)=\tfrac13$. And $\tfrac12\times\tfrac23=\tfrac13$ ✓. **Independent**, even though both events are about the same die. Knowing the roll is at most 4 leaves even and odd equally likely (2 of each).

> [!warning] Disjoint is not independent
> If $A$ and $B$ are disjoint with positive probabilities, then $P(A\cap B)=0\neq P(A)P(B)$. They are strongly **dependent**: if one happens, the other cannot.

### Independence of several events

Events $A_1,\dots,A_n$ are (mutually) independent if the product rule holds for **every** sub-collection. Then

$$
P(A_1\cap A_2\cap\cdots\cap A_n)=P(A_1)P(A_2)\cdots P(A_n).
$$

This is what makes "5 independent tests each passing with probability 0.9" give $0.9^5$.

> [!tip] Independence is an assumption
> In real data it is usually an **approximation**, and often a bad one. Consecutive video frames, repeated trials with the same object, or measurements from one sensor over time are typically correlated. Check the assumption before relying on a calculation that uses it.

> [!question]- Check yourself
> 1. $P(A)=0.5$, $P(B)=0.4$, $P(A\cap B)=0.2$. Independent?
> 2. If $A$ and $B$ are independent, are $A$ and $B^c$ independent?
>
> **Answers.** 1. $0.5\times0.4=0.2$. Yes. 2. Yes: $P(A\cap B^c)=P(A)-P(A)P(B)=P(A)(1-P(B))=P(A)P(B^c)$.

---

## 2.4 The law of total probability

### The idea: split into cases

Often $P(A)$ is hard to find directly, but easy once you know which "case" you are in. Split the world into cases $B_1,\dots,B_k$ that are **disjoint and cover everything** (a partition), then average.

> [!important] Law of total probability
> $$
> P(A)=\sum_{i=1}^kP(A\mid B_i)\,P(B_i).
> $$

**In words:** the overall probability is a **weighted average** of the probability in each case, weighted by how likely each case is.

*Why:* $A$ is the disjoint union of the pieces $A\cap B_i$, and $P(A\cap B_i)=P(A\mid B_i)P(B_i)$ by the multiplication rule.

### Worked example 2.5: two machines

A factory has two machines. Machine 1 makes 60% of parts, with a 2% defect rate. Machine 2 makes 40%, with a 5% defect rate.

$$
P(\text{defect})=P(\text{def}\mid M_1)P(M_1)+P(\text{def}\mid M_2)P(M_2)=0.02(0.6)+0.05(0.4)=0.012+0.020=0.032.
$$

The overall rate, 3.2%, lies between 2% and 5%, closer to 2% because machine 1 makes more parts.

---

## 2.5 Bayes' rule

### Turning a conditional around

Often you know $P(\text{evidence}\mid\text{hypothesis})$ (how a cause produces effects) but want $P(\text{hypothesis}\mid\text{evidence})$ (how to infer the cause from what you see). Write the multiplication rule both ways and divide:

> [!important] Bayes' rule
> $$
> P(H\mid E)=\frac{P(E\mid H)\,P(H)}{P(E)},
> $$
> where the denominator usually comes from the law of total probability:
> $$
> P(E)=P(E\mid H)P(H)+P(E\mid H^c)P(H^c).
> $$

### The names

| Term | Name | Meaning |
|---|---|---|
| $P(H)$ | **prior** | your belief before seeing the evidence |
| $P(E\mid H)$ | **likelihood** | how well $H$ predicts the evidence |
| $P(E)$ | **evidence** | the total probability of what you saw |
| $P(H\mid E)$ | **posterior** | your belief after seeing the evidence |

$$
\text{posterior}=\frac{\text{likelihood}\times\text{prior}}{\text{evidence}}.
$$

### Worked example 2.6: the factory, reversed

A part is defective. Which machine made it?

$$
P(M_2\mid\text{def})=\frac{P(\text{def}\mid M_2)P(M_2)}{P(\text{def})}=\frac{0.05\times0.4}{0.032}=\frac{0.020}{0.032}=0.625.
$$

Machine 2 makes only 40% of the parts but 62.5% of the defects.

---

## 2.6 The medical test: base rates matter

### The problem

A disease affects **1%** of people. A test detects it **95%** of the time when present (sensitivity), and gives a false positive for **5%** of healthy people. You test positive. What is the probability you have the disease?

Most people (including many doctors, in studies) answer about 95%. Let us compute.

### The calculation

- Prior: $P(D)=0.01$, so $P(D^c)=0.99$.
- Likelihoods: $P(+\mid D)=0.95$, $P(+\mid D^c)=0.05$.
- Evidence: $P(+)=0.95(0.01)+0.05(0.99)=0.0095+0.0495=0.059$.
- Posterior:

$$
P(D\mid+)=\frac{0.0095}{0.059}\approx0.161.
$$

**About 16%.** Not 95%.

### Why: count people

> [!tip] Use natural frequencies
> When a Bayes problem is confusing, imagine a concrete number of cases and count.

Take **10,000 people**.

- **100** have the disease. The test catches **95** of them.
- **9,900** are healthy. The test wrongly flags 5% of them: **495**.
- Total positives: $95+495=590$. Of these, only **95** are ill.

$$
P(\text{ill}\mid\text{positive})=\frac{95}{590}\approx16\%.
$$

The disease is rare, so the healthy group is enormous, and even a small false-positive rate applied to an enormous group produces more false alarms than there are real cases. Ignoring the prior (the 1%) is called **base-rate neglect**.

### A second test

You take a second, independent test, and it is also positive. Now your prior is yesterday's posterior, 0.161:

$$
P(D\mid++)=\frac{0.95\times0.161}{0.95\times0.161+0.05\times0.839}=\frac{0.153}{0.153+0.042}\approx0.785.
$$

> [!important] Yesterday's posterior is today's prior
> Bayes' rule can be applied repeatedly, each time using the latest belief as the prior. This **recursive updating** is how robots track their position, how spam filters learn, and how the Kalman filter works ([[04 Perception and State]]).

---

## 2.7 Two traps

### $P(A\mid B)$ is not $P(B\mid A)$

$P(\text{positive}\mid\text{ill})=0.95$, but $P(\text{ill}\mid\text{positive})=0.16$.

In court this is the **prosecutor's fallacy**: "If the defendant were innocent, there would be only a 1 in a million chance of this DNA match. So there is a 1 in a million chance the defendant is innocent." The first number is $P(\text{evidence}\mid\text{innocent})$; the conclusion claims $P(\text{innocent}\mid\text{evidence})$. In a city of 10 million people, about 10 innocent people would also match.

### Conditional independence

Two events can be **dependent** overall but **independent once you know a third thing**.

> [!note] Definition: conditional independence
> $A$ and $B$ are conditionally independent given $C$ if
> $$
> P(A\cap B\mid C)=P(A\mid C)\,P(B\mid C).
> $$

**Example.** Two thermometers in the same room. Their readings are correlated (both rise when the room warms up). But **given the true temperature**, their errors are unrelated: knowing one thermometer's error tells you nothing about the other's. The readings are conditionally independent given the temperature.

This is exactly the assumption behind combining multiple sensors, and behind the Markov property in [[PS 12 Markov Chains and Information]].

---

## Summary

| Idea | Formula |
|---|---|
| conditional probability | $P(A\mid B)=P(A\cap B)/P(B)$ |
| multiplication rule | $P(A\cap B)=P(A)P(B\mid A)$ |
| independence | $P(A\cap B)=P(A)P(B)$ |
| total probability | $P(A)=\sum_iP(A\mid B_i)P(B_i)$ |
| Bayes' rule | $P(H\mid E)=P(E\mid H)P(H)/P(E)$ |

**Three facts to remember:**

1. Conditioning = restrict to the known part, then rescale.
2. $P(A\mid B)\neq P(B\mid A)$. Bayes' rule converts one into the other.
3. Rare hypotheses stay unlikely after weak evidence: always include the prior.

---

## Exercises

### Part A: warm-up

**A1.** $P(A)=0.4$, $P(B)=0.5$, $P(A\cap B)=0.1$. Find $P(A\mid B)$ and $P(B\mid A)$. Are $A$ and $B$ independent?

**A2.** Two cards are drawn without replacement. Find $P(\text{both hearts})$.

**A3.** A die is rolled. Given that the result is greater than 3, what is the probability it is even?

**A4.** A box has 4 good and 2 faulty fuses. Two are drawn without replacement. Find $P(\text{both good})$ and $P(\text{exactly one faulty})$ using a tree.

> [!success]- Solutions to Part A
> **A1.** $P(A\mid B)=0.2$, $P(B\mid A)=0.25$. $P(A)P(B)=0.2\neq0.1$: not independent.
>
> **A2.** $\dfrac{13}{52}\cdot\dfrac{12}{51}=\dfrac1{17}\approx0.059$.
>
> **A3.** Given $\{4,5,6\}$, the even ones are $\{4,6\}$: $2/3$.
>
> **A4.** $\tfrac46\cdot\tfrac35=\tfrac{12}{30}=0.4$. Exactly one faulty: $\tfrac46\cdot\tfrac25+\tfrac26\cdot\tfrac45=\tfrac{16}{30}\approx0.533$.

### Part B: core

**B1.** 20% of email is spam. The word "prize" appears in 30% of spam and 1% of legitimate email. An email contains "prize". What is the probability it is spam?

**B2.** A robot's grasp detector reports "success". Grasps actually succeed 70% of the time. The detector reports success for 90% of real successes and 20% of real failures. Find $P(\text{real success}\mid\text{reported success})$ and $P(\text{real failure}\mid\text{reported failure})$.

**B3.** In the medical test of section 2.6, how high would the prior need to be for a single positive test to give at least a 50% chance of disease?

**B4.** Three machines make 50%, 30% and 20% of a product, with defect rates 1%, 2% and 4%. A defective item is found. Which machine most likely made it, and with what probability?

**B5.** A robot localizes itself in a corridor with 3 doors among 10 equally likely positions. Its door sensor says "door" with probability 0.8 at a door and 0.1 elsewhere. It senses "door". What is the probability it is actually at a door? It then moves one position (assume, for simplicity, that it is equally likely to arrive at a door or not as before) and senses "door" again. Update again.

> [!success]- Solutions to Part B
> **B1.** $\dfrac{0.3\times0.2}{0.3\times0.2+0.01\times0.8}=\dfrac{0.06}{0.068}\approx0.882$.
>
> **B2.** $P(\text{rep. success})=0.9(0.7)+0.2(0.3)=0.69$. $P(\text{success}\mid\text{rep. success})=0.63/0.69\approx0.913$. $P(\text{rep. failure})=0.31$; real failure and reported failure: $0.8\times0.3=0.24$; so $0.24/0.31\approx0.774$.
>
> **B3.** Need $0.95p\ge0.05(1-p)$, so $p\ge0.05/1.00=0.05$. A prior of 5% or more.
>
> **B4.** $P(\text{def})=0.005+0.006+0.008=0.019$. Posteriors: $0.263$, $0.316$, $0.421$. Machine 3, with probability about 42%, despite making the fewest items.
>
> **B5.** Prior $0.3$. $P(\text{door reading})=0.8(0.3)+0.1(0.7)=0.31$. Posterior $0.24/0.31\approx0.774$. Second update using $0.774$ as prior: $\dfrac{0.8\times0.774}{0.8\times0.774+0.1\times0.226}=\dfrac{0.619}{0.642}\approx0.965$. (A real robot would also model how the motion changes its position; this is the idea behind particle filters.)

### Part C: explain and prove

**C1.** Prove that if $A$ and $B$ are independent, then so are $A^c$ and $B^c$.

**C2.** Show that $P(A\mid B)+P(A^c\mid B)=1$. Interpret.

**C3.** Explain, using the 10,000-people method, why a test with 99% sensitivity and 99% specificity is still unreliable for a disease with prevalence 1 in 10,000.

**C4.** Give an example of two events that are dependent but conditionally independent given a third event.

> [!success]- Solutions to Part C
> **C1.** $P(A^c\cap B^c)=1-P(A\cup B)=1-P(A)-P(B)+P(A)P(B)=(1-P(A))(1-P(B))$.
>
> **C2.** $\dfrac{P(A\cap B)+P(A^c\cap B)}{P(B)}=\dfrac{P(B)}{P(B)}=1$. Conditioning on $B$ produces a genuine probability distribution in the world $B$.
>
> **C3.** Take 1,000,000 people: 100 ill, 99 test positive. 999,900 healthy, 1% = 9,999 false positives. Positive predictive value $99/(99+9999)\approx1\%$.
>
> **C4.** Two thermometers in one room (section 2.7), or two children's test results given their shared teacher's quality, or two coin flips from a coin that might be biased: the flips are dependent (both tell you about the bias) but independent once the bias is known.

### Part D: practise with code

**D1.** Simulate the medical test for 1,000,000 people with NumPy. Estimate $P(D\mid+)$ and compare with $0.161$.

**D2.** Write `bayes_update(prior, p_e_given_h, p_e_given_not_h)` and apply it 5 times in a row for the test. Plot the posterior after each positive result.

**D3.** Simulate drawing two cards without replacement 100,000 times and estimate $P(\text{second card is an ace}\mid\text{first card is an ace})$. Compare with $3/51$.

> [!success]- Hints for Part D
> **D1.** `ill = rng.random(N) < 0.01`; `pos = np.where(ill, rng.random(N) < 0.95, rng.random(N) < 0.05)`; then `ill[pos].mean()`.
>
> **D2.** The posterior climbs $0.161\to0.785\to0.986\to0.999\to\dots$. Independent repeated evidence quickly overwhelms a small prior.

---

## Where this is used

- **State estimation**: prior belief about the state, likelihood of the sensor reading, posterior belief, repeated every time step ([[04 Perception and State]]).
- **Policies**: a policy $\pi(a\mid o)$ is a conditional distribution of actions given observations ([[06 Imitation and Distribution Shift]]).
- **Evaluation**: "success given this lighting condition" is a conditional probability, and comparing conditions is how you find failure modes ([[16 Evaluation and Uncertainty]]).

Next: [[PS 03 Discrete Random Variables]]: attaching numbers to outcomes.

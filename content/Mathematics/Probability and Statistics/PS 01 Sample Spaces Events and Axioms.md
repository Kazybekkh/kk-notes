---
type: course-chapter
course: probability-statistics
chapter: 1
tags: [mathematics, probability]
---

# Chapter 1: Sample spaces, events and axioms

[[PS 00 Course Map]] | Next: [[PS 02 Conditional Probability and Bayes Rule]]

> [!abstract] The big idea
> Probability assigns a number between 0 and 1 to **sets of possible outcomes**. Three simple rules about those numbers (the axioms) generate the entire theory. When all outcomes are equally likely, computing a probability becomes **counting**.

> [!info] In this chapter you will learn to
> 1. Write down the sample space of an experiment and describe events as sets.
> 2. State the three axioms and derive the complement rule, inclusion-exclusion and the union bound from them.
> 3. Compute probabilities by counting equally likely outcomes, and know when that is allowed.
> 4. Use the complement trick for "at least one" questions.
> 5. Explain the two interpretations of probability.

> [!tip] Before you start
> You need basic set language: union, intersection, complement ([[DM 04 Sets]]). For counting questions, [[DM 07 Counting]] helps, but this chapter only uses simple multiplication.

---

## 1.1 Experiments and sample spaces

### The setting

Probability studies **experiments with uncertain outcomes**: rolling a die, flipping a coin, measuring a sensor, running a robot trial. Before the experiment, you do not know what will happen; afterwards, exactly one outcome has occurred.

> [!note] Definition: sample space
> The **sample space** $\Omega$ (capital omega) is the set of all possible outcomes of an experiment. Each run of the experiment produces **exactly one** element of $\Omega$.

### Examples

| Experiment | Sample space $\Omega$ | Size |
|---|---|---|
| flip a coin | $\{H,T\}$ | 2 |
| roll a die | $\{1,2,3,4,5,6\}$ | 6 |
| flip two coins | $\{HH,HT,TH,TT\}$ | 4 |
| roll two dice | all pairs $(i,j)$ with $i,j\in\{1,\dots,6\}$ | 36 |
| number of emails today | $\{0,1,2,\dots\}$ | infinite (countable) |
| time until a motor fails | $[0,\infty)$ | infinite (continuous) |

### Choosing the sample space carefully

Two coins can be described as $\{HH,HT,TH,TT\}$ (which coin shows what) or as $\{\text{0 heads},\text{1 head},\text{2 heads}\}$ (just the count). Both are valid sample spaces, but they are **not equally convenient**:

- In the first, all four outcomes are equally likely (each has probability $\tfrac14$).
- In the second, "1 head" is twice as likely as "0 heads", because it can happen two ways ($HT$ or $TH$).

> [!tip] Rule of thumb
> Choose a sample space whose outcomes are **as detailed as needed to be equally likely**. Usually that means keeping track of order and of which object is which, even if you only care about a summary in the end.

> [!question]- Check yourself
> 1. Write the sample space for flipping a coin and rolling a die.
> 2. How many outcomes are there when flipping 5 coins?
>
> **Answers.** 1. $\{H1,H2,\dots,H6,T1,\dots,T6\}$, 12 outcomes. 2. $2^5=32$.

---

## 1.2 Events

> [!note] Definition: event
> An **event** is a subset of the sample space: a collection of outcomes that you are interested in. The event **occurs** if the actual outcome belongs to it.

**Examples with one die.**

| In words | As a set |
|---|---|
| the roll is even | $A=\{2,4,6\}$ |
| the roll is at least 5 | $B=\{5,6\}$ |
| the roll is 7 | $\emptyset$ (impossible event) |
| the roll is between 1 and 6 | $\Omega$ (certain event) |

If the die shows 4, then $A$ occurs and $B$ does not.

### Combining events

Because events are sets, set operations describe combinations of events:

| In words | Set notation | Example with $A,B$ above |
|---|---|---|
| $A$ **or** $B$ (or both) | $A\cup B$ | $\{2,4,5,6\}$ |
| $A$ **and** $B$ | $A\cap B$ | $\{6\}$ |
| **not** $A$ | $A^c$ | $\{1,3,5\}$ |
| $A$ but not $B$ | $A\setminus B=A\cap B^c$ | $\{2,4\}$ |

Two events are **disjoint** (mutually exclusive) when they cannot both happen: $A\cap B=\emptyset$. For example, "even" and "odd" are disjoint.

> [!question]- Check yourself
> With two dice, let $S$ = "sum is 7" and $D$ = "both dice equal". Are $S$ and $D$ disjoint?
>
> **Answer.** Yes. Equal dice give an even sum ($2,4,\dots,12$), never 7.

---

## 1.3 The axioms of probability

### The idea

We want a function $P$ that assigns each event a number measuring how likely it is. What properties must such a function have? Remarkably, three are enough.

> [!note] Kolmogorov's axioms
> 1. **Non-negativity:** $P(A)\ge0$ for every event $A$.
> 2. **Normalization:** $P(\Omega)=1$. (Something certainly happens.)
> 3. **Additivity:** if $A$ and $B$ are disjoint, then $P(A\cup B)=P(A)+P(B)$. (The same holds for any countable list of pairwise disjoint events.)

### A picture to keep in mind

Think of probability as **one unit of sand spread over the sample space**. The probability of an event is the amount of sand sitting on it.

- Sand amounts are never negative (axiom 1).
- The total is one unit (axiom 2).
- The sand on two separate regions is the sum of the sand on each (axiom 3).

Every rule below follows from this picture, and from the axioms by short proofs.

---

## 1.4 Rules derived from the axioms

### Rule 1: complement

$$
P(A^c)=1-P(A).
$$

*Proof.* $A$ and $A^c$ are disjoint and together make up $\Omega$. By axioms 3 and 2, $P(A)+P(A^c)=P(\Omega)=1$.

> [!tip] The complement trick
> "At least one" is usually hard to count directly and easy to count through its complement, "none".
> $$
> P(\text{at least one})=1-P(\text{none}).
> $$

### Rule 2: the impossible event

$$
P(\emptyset)=0.
$$

*Proof.* $\emptyset$ is the complement of $\Omega$, so $P(\emptyset)=1-1=0$.

### Rule 3: probabilities are at most 1

$0\le P(A)\le1$. *Proof:* $P(A)=1-P(A^c)\le1$ since $P(A^c)\ge0$.

### Rule 4: monotonicity

If $A\subseteq B$, then $P(A)\le P(B)$.

*Proof.* $B$ splits into the disjoint pieces $A$ and $B\setminus A$, so $P(B)=P(A)+P(B\setminus A)\ge P(A)$.

**In words:** a more specific event can never be more likely. "It rains and is windy" cannot be more probable than "it rains".

> [!example] The conjunction fallacy
> People are often asked: "Linda is 31, outspoken and was active in social justice causes. Which is more likely: (a) Linda is a bank teller, or (b) Linda is a bank teller and active in a feminist movement?" Many choose (b), because it fits the description. But (b) is a subset of (a), so by monotonicity it can never be more probable.

### Rule 5: inclusion-exclusion

For **any** two events (disjoint or not):

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B).
$$

*Why.* Adding $P(A)+P(B)$ counts the sand on the overlap $A\cap B$ **twice**. Subtracting it once corrects the double count.

*Proof.* Split $A\cup B$ into three disjoint pieces: $A\setminus B$, $A\cap B$, $B\setminus A$. Also $P(A)=P(A\setminus B)+P(A\cap B)$ and $P(B)=P(B\setminus A)+P(A\cap B)$. Add the last two and compare.

For three events:

$$
P(A\cup B\cup C)=P(A)+P(B)+P(C)-P(A\cap B)-P(A\cap C)-P(B\cap C)+P(A\cap B\cap C).
$$

### Rule 6: the union bound

$$
P(A\cup B)\le P(A)+P(B).
$$

This follows from inclusion-exclusion, since $P(A\cap B)\ge0$. It is crude but needs no knowledge of the overlap, which makes it a favourite tool in proofs: "the chance that **any** of these 10 bad things happens is at most the sum of their chances".

> [!question]- Check yourself
> 1. $P(A)=0.6$, $P(B)=0.5$, $P(A\cup B)=0.8$. Find $P(A\cap B)$.
> 2. Can $P(A)=0.7$ and $P(B)=0.6$ if $A$ and $B$ are disjoint?
>
> **Answers.** 1. $0.6+0.5-0.8=0.3$. 2. No: disjoint would give $P(A\cup B)=1.3>1$.

---

## 1.5 Equally likely outcomes: probability as counting

### The rule

When $\Omega$ is finite and every outcome is **equally likely**, each outcome has probability $1/|\Omega|$, and additivity gives

> [!important] Classical probability
> $$
> P(A)=\frac{|A|}{|\Omega|}=\frac{\text{number of outcomes in }A}{\text{total number of outcomes}}.
> $$

### Worked example 1.1: two dice, sum 7

$|\Omega|=36$ ordered pairs, all equally likely. The pairs with sum 7 are

$$
(1,6),(2,5),(3,4),(4,3),(5,2),(6,1),
$$

six of them. So $P(\text{sum}=7)=6/36=1/6$.

> [!warning] Why ordered pairs?
> If you list unordered results ($\{1,6\}$, $\{2,5\}$, $\{3,4\}$, ...), outcomes like "$\{3,3\}$" (one way) and "$\{3,4\}$" (two ways: $(3,4)$ or $(4,3)$) are **not** equally likely, and counting them as equal gives wrong answers. Imagine the dice are different colours: then the 36 ordered pairs are clearly equally likely.

### The distribution of the sum of two dice

| Sum | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ways | 1 | 2 | 3 | 4 | 5 | 6 | 5 | 4 | 3 | 2 | 1 |
| Probability | $\tfrac1{36}$ | $\tfrac2{36}$ | $\tfrac3{36}$ | $\tfrac4{36}$ | $\tfrac5{36}$ | $\tfrac6{36}$ | $\tfrac5{36}$ | $\tfrac4{36}$ | $\tfrac3{36}$ | $\tfrac2{36}$ | $\tfrac1{36}$ |

The middle sums are most likely because they can be made in the most ways. This "triangle" is the first hint of the central limit theorem ([[PS 08 Law of Large Numbers and Central Limit Theorem]]).

### Worked example 1.2: at least one six in two rolls

**Direct, wrong attempt:** $\tfrac16+\tfrac16=\tfrac13$. This double counts $(6,6)$.

**Complement:** "no six" means each die shows 1 to 5: $5\times5=25$ outcomes. So

$$
P(\text{at least one six})=1-\frac{25}{36}=\frac{11}{36}\approx0.306.
$$

**Inclusion-exclusion (check):** $\tfrac6{36}+\tfrac6{36}-\tfrac1{36}=\tfrac{11}{36}$ ✓.

### Worked example 1.3: at least one six in four rolls

Complement: $P(\text{no six in four rolls})=\left(\tfrac56\right)^4=\tfrac{625}{1296}\approx0.482$. So $P(\text{at least one six})\approx0.518$. Slightly better than even. (This was a famous gambling bet in 17th-century France.)

### Worked example 1.4: drawing cards

A standard deck has 52 cards: 4 suits (hearts, diamonds, clubs, spades) of 13 ranks each.

$P(\text{heart or king})$: hearts 13, kings 4, the king of hearts counted in both:

$$
\frac{13}{52}+\frac4{52}-\frac1{52}=\frac{16}{52}=\frac4{13}.
$$

> [!question]- Check yourself
> 1. Three fair coins. Find $P(\text{exactly two heads})$ and $P(\text{at least one head})$.
> 2. Two dice. Find $P(\text{sum}\ge10)$.
> 3. Two dice. Find $P(\text{the two dice differ})$.
>
> **Answers.** 1. $HHT,HTH,THH$: $3/8$. Complement of $TTT$: $7/8$. 2. Sums 10, 11, 12: $3+2+1=6$ ways, $1/6$. 3. Complement of "equal" (6 ways): $1-6/36=5/6$.

---

## 1.6 A famous surprise: the birthday problem

**Question.** In a room of $n$ people, what is the probability that at least two share a birthday? (Assume 365 equally likely days, and ignore leap years.)

**Step 1: complement.** Compute $P(\text{all birthdays different})$.

**Step 2: count.** Line the people up. The first can have any birthday. The second must avoid one day. The third must avoid two days. And so on:

$$
P(\text{all different})=\frac{365}{365}\cdot\frac{364}{365}\cdot\frac{363}{365}\cdots\frac{365-n+1}{365}.
$$

**Step 3: compute.**

| $n$ | 10 | 20 | 23 | 30 | 50 | 70 |
|---|---|---|---|---|---|---|
| $P(\text{shared})$ | 0.117 | 0.411 | 0.507 | 0.706 | 0.970 | 0.999 |

With just **23 people**, a shared birthday is more likely than not.

**Why so few?** The intuition "23 is much less than 365" compares the wrong things. What matters is the number of **pairs** of people, each of which is a chance for a match: $\binom{23}2=253$ pairs. Each pair matches with probability $1/365$, and 253 chances at $1/365$ add up quickly.

> [!example] Why this matters in computing
> The same arithmetic explains **hash collisions**. With a hash of $N$ possible values, collisions become likely after only about $\sqrt N$ items, not $N$. A 32-bit hash ($N\approx4\times10^9$) starts colliding after roughly 77,000 items.

---

## 1.7 What does a probability mean?

Two interpretations are in common use. They use the **same mathematics**; they differ in what the numbers are about.

**Frequentist.** $P(A)$ is the **long-run fraction** of times $A$ occurs if the experiment is repeated many times under the same conditions. "A fair coin has $P(H)=0.5$" means that in many flips, about half are heads. This suits dice, sensor noise and repeatable trials.

**Bayesian.** $P(A)$ is a **degree of belief** in $A$, given what you know. "The probability that this grasp succeeds is 0.9" describes your confidence about a single event that will happen only once. This suits one-off questions and is the basis of [[PS 11 Bayesian Inference]].

> [!warning] A probability is not a promise
> A probability of 0.9 does not mean the next trial will succeed. It means that, among many situations like this one, about 9 in 10 succeed, or that you should be about as confident as you would be of drawing a red ball from a bag with 9 red and 1 blue.

---

## Summary

| Idea | Formula or meaning |
|---|---|
| sample space $\Omega$ | all possible outcomes |
| event | a subset of $\Omega$ |
| axioms | $P\ge0$; $P(\Omega)=1$; additive for disjoint events |
| complement | $P(A^c)=1-P(A)$ |
| inclusion-exclusion | $P(A\cup B)=P(A)+P(B)-P(A\cap B)$ |
| union bound | $P(A\cup B)\le P(A)+P(B)$ |
| equally likely | $P(A)=\lvert A\rvert/\lvert\Omega\rvert$ |

**Three facts to remember:**

1. Choose a sample space whose outcomes are equally likely (usually: keep track of order).
2. "At least one" = 1 minus "none".
3. When adding probabilities of overlapping events, subtract the overlap.

---

## Exercises

### Part A: warm-up

**A1.** A card is drawn from a standard deck. Find $P(\text{red})$, $P(\text{face card})$ (J, Q, K) and $P(\text{red face card})$.

**A2.** Two dice are rolled. Find $P(\text{sum}=8)$ and $P(\text{product}=12)$.

**A3.** $P(A)=0.3$, $P(B)=0.5$, $P(A\cap B)=0.1$. Find $P(A\cup B)$, $P(A^c)$ and $P(A\cap B^c)$.

**A4.** A coin is flipped 6 times. Find $P(\text{all heads})$ and $P(\text{at least one tail})$.

> [!success]- Solutions to Part A
> **A1.** $26/52=1/2$; $12/52=3/13$; $6/52=3/26$.
>
> **A2.** Sum 8: $(2,6),(3,5),(4,4),(5,3),(6,2)$, so $5/36$. Product 12: $(2,6),(3,4),(4,3),(6,2)$, so $4/36=1/9$.
>
> **A3.** $0.3+0.5-0.1=0.7$; $0.7$; $P(A)-P(A\cap B)=0.2$.
>
> **A4.** $1/64$; $1-1/64=63/64$.

### Part B: core

**B1.** In a class of 40, 25 study maths, 20 study physics, and 8 study neither. What is the probability that a randomly chosen student studies both?

**B2.** Three dice are rolled. Find $P(\text{all three different})$ and $P(\text{at least two the same})$.

**B3.** A robot test suite has 5 independent tests, each passing with probability 0.9. Find $P(\text{all pass})$ and $P(\text{at least one fails})$.

**B4.** A 4-digit PIN is chosen uniformly at random (digits 0 to 9, repeats allowed). Find $P(\text{no repeated digit})$.

**B5.** Use the union bound to show that if each of 20 components fails with probability at most 0.001, the probability that any fails is at most 0.02. Does this need independence?

**B6.** In a room of 5 people, find the probability that at least two share a birth **month** (assume 12 equally likely months).

> [!success]- Solutions to Part B
> **B1.** At least one subject: $40-8=32$. Both: $25+20-32=13$. Probability $13/40=0.325$.
>
> **B2.** All different: $\dfrac{6\cdot5\cdot4}{216}=\dfrac{120}{216}=\dfrac59$. At least two the same: $\dfrac49$.
>
> **B3.** $0.9^5\approx0.590$. At least one fails: $\approx0.410$. Even with 90% per test, a 5-test suite fails 41% of the time.
>
> **B4.** $\dfrac{10\cdot9\cdot8\cdot7}{10^4}=0.504$.
>
> **B5.** $P(\text{any fails})\le\sum P(\text{component }i\text{ fails})\le20\times0.001=0.02$. No independence needed: that is the power of the union bound.
>
> **B6.** All different: $\dfrac{12\cdot11\cdot10\cdot9\cdot8}{12^5}=\dfrac{95040}{248832}\approx0.382$. Shared: $\approx0.618$.

### Part C: explain and prove

**C1.** Prove from the axioms that if $A\subseteq B$, then $P(B\setminus A)=P(B)-P(A)$.

**C2.** Prove the three-event inclusion-exclusion formula from the two-event one. (Hint: apply it to $A\cup B$ and $C$.)

**C3.** Someone says: "There are three possible outcomes for two coin flips: two heads, two tails, or one of each. So $P(\text{two heads})=1/3$." Explain the error.

**C4.** Explain why disjoint events with positive probabilities cannot be "unrelated" to each other. (What does learning that $A$ happened tell you about $B$?)

> [!success]- Solutions to Part C
> **C1.** $B$ is the disjoint union of $A$ and $B\setminus A$, so $P(B)=P(A)+P(B\setminus A)$.
>
> **C2.** $P((A\cup B)\cup C)=P(A\cup B)+P(C)-P((A\cup B)\cap C)$. Expand $P(A\cup B)$, and note $(A\cup B)\cap C=(A\cap C)\cup(B\cap C)$, whose probability is $P(A\cap C)+P(B\cap C)-P(A\cap B\cap C)$. Collect terms.
>
> **C3.** The three outcomes are not equally likely. "One of each" happens two ways ($HT$, $TH$). The correct answer is $1/4$.
>
> **C4.** If $A$ happened, $B$ certainly did not. So knowing $A$ changes the probability of $B$ from positive to zero: the events are strongly dependent. (Independence is defined in the next chapter.)

### Part D: practise with code

**D1.** Simulate rolling two dice 100,000 times (`np.random.randint(1, 7, size=(100000, 2))`). Estimate $P(\text{sum}=7)$ and compare with $1/6$.

**D2.** Simulate the birthday problem for $n=23$: in each of 10,000 trials, draw 23 random birthdays and check for a repeat (`len(set(b)) < 23`). Compare with 0.507.

**D3.** Write a function that computes the exact birthday probability for any $n$ using the product formula. Plot it for $n=1$ to $80$. Find the smallest $n$ with probability above 0.99.

**D4.** Estimate $P(\text{at least one six in four rolls})$ and $P(\text{at least one double six in 24 rolls of two dice})$ by simulation. (This was the Chevalier de Méré's puzzle.) Which bet is better?

> [!success]- Hints for Part D
> **D3.** $n=57$ is the first value above 0.99.
>
> **D4.** About $0.518$ versus about $0.491$. The first bet is slightly favourable, the second slightly unfavourable, even though "naive" reasoning ($4\times\tfrac16$ and $24\times\tfrac1{36}$, both $\tfrac23$) suggests they are the same.

---

## Where this is used

- A robot's **success rate** is an estimate of a probability, and comparing two policies means comparing two unknown probabilities from finite trials ([[16 Evaluation and Uncertainty]]).
- **Reliability**: the chance that a multi-step task completes is (at least roughly) a product of the per-step success chances, which falls fast as tasks get longer.
- The union bound appears in proofs of how much data a learning algorithm needs.

Next: [[PS 02 Conditional Probability and Bayes Rule]]: how probabilities change when you learn something.

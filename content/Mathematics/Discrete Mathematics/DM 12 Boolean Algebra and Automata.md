---
type: course-chapter
course: discrete-mathematics
chapter: 12
tags: [mathematics, discrete-mathematics, logic, computation]
---
# DM 12 Boolean algebra and automata

Previous: [[DM 11 Trees and Graph Algorithms]] | [[DM 00 Course Map]]

> [!abstract] One sentence
> Boolean algebra is propositional logic written as arithmetic on 0 and 1, which is how circuits compute; a finite automaton is the simplest machine with memory, and it recognizes exactly the patterns that regular expressions describe.

## Part 1: Boolean algebra

### Logic as arithmetic

Write 1 for true and 0 for false. The connectives of [[DM 01 Logic and Propositions]] become operations:

| Logic | Boolean | Gate | Python bit operator |
|---|---|---|---|
| $p\land q$ | $pq$ (or $p\cdot q$) | AND | `p & q` |
| $p\lor q$ | $p+q$ | OR | `p \| q` |
| $\neg p$ | $\bar p$ | NOT | `~p` (or `1 - p`) |
| $p\oplus q$ | $p\oplus q$ | XOR | `p ^ q` |

Caution: in Boolean algebra $1+1=1$ (true or true is true). With XOR, $1\oplus1=0$, which is addition modulo 2 ([[DM 08 Number Theory and Modular Arithmetic]]).

### Laws

The logical equivalences become algebraic identities:

| Law | Identity |
|---|---|
| identity | $x+0=x$, $\;x\cdot1=x$ |
| domination | $x+1=1$, $\;x\cdot0=0$ |
| idempotent | $x+x=x$, $\;xx=x$ |
| complement | $x+\bar x=1$, $\;x\bar x=0$ |
| De Morgan | $\overline{x+y}=\bar x\,\bar y$, $\;\overline{xy}=\bar x+\bar y$ |
| absorption | $x+xy=x$, $\;x(x+y)=x$ |
| distributive | $x(y+z)=xy+xz$, $\;x+yz=(x+y)(x+z)$ |

The second distributive law is false for ordinary numbers. Boolean algebra is its own system.

**Worked simplification.**

$$
xy+x\bar y=x(y+\bar y)=x\cdot1=x.
$$

A two-gate expression collapses to a wire. Fewer gates mean cheaper, faster, cooler chips.

### From truth table to formula

Any truth table can be written as a formula: for each row where the output is 1, write the AND of the inputs (negated where the input is 0), then OR those terms together. This is the **sum of products** (disjunctive normal form).

**Example.** Majority of three inputs: output 1 when at least two inputs are 1. Rows with output 1: $011,101,110,111$.

$$
M=\bar xyz+x\bar yz+xy\bar z+xyz.
$$

Simplify: $xyz$ can be absorbed into each of the others. Using $xyz+\bar xyz=yz$ and similar,

$$
M=xy+yz+xz.
$$

Consequence: AND, OR and NOT together can compute *any* Boolean function. Even NAND alone ($\overline{xy}$) suffices, since $\bar x=\overline{xx}$ and the rest follows by De Morgan. Real chips are built mostly from NAND gates.

### A circuit that adds

Adding two bits $a,b$ gives a sum bit and a carry bit:

| $a$ | $b$ | carry | sum |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 |

So $\text{sum}=a\oplus b$ and $\text{carry}=ab$: a **half adder**. Chain full adders (which also take an incoming carry) and you add 64-bit numbers. Every calculation a computer does reduces to gates like these.

## Part 2: Finite automata

### The machine

A **deterministic finite automaton** (DFA) reads a string one symbol at a time. It has:

- a finite set of **states**,
- a **start** state,
- a **transition function**: from each state, each input symbol leads to exactly one next state,
- a set of **accepting** states.

After the last symbol, the string is **accepted** if the machine is in an accepting state. The DFA's only memory is which state it is in.

**Example: binary strings with an even number of 1s.** Two states: $E$ (even so far, start, accepting) and $O$ (odd so far).

| State | on `0` | on `1` |
|---|---|---|
| $E$ | $E$ | $O$ |
| $O$ | $O$ | $E$ |

Run on `1011`: $E\xrightarrow1O\xrightarrow0O\xrightarrow1E\xrightarrow1O$. Ends in $O$: rejected (three 1s).

The DFA is a directed graph ([[DM 10 Graphs]]) with labelled edges, and running it is following a path.

**Example: binary numbers divisible by 3.** Track the value mod 3. Reading bit $b$ turns value $v$ into $2v+b$, so the state $r$ moves to $(2r+b)\bmod3$:

| State $r$ | on `0` | on `1` |
|---|---|---|
| 0 (start, accept) | 0 | 1 |
| 1 | 2 | 0 |
| 2 | 1 | 2 |

`110` (six): $0\to1\to0\to0$. Accepted. Three states can test divisibility of numbers of any length.

### Regular expressions

A **regular expression** describes a set of strings:

| Pattern | Matches |
|---|---|
| `ab` | `a` followed by `b` |
| `a\|b` | `a` or `b` |
| `a*` | zero or more `a`s |
| `(ab)*` | `""`, `ab`, `abab`, ... |
| `0*10*` | strings with exactly one `1` |

**Kleene's theorem.** A language can be described by a regular expression exactly when some DFA recognizes it. These are the **regular languages**. Regex engines work by compiling the expression into an automaton.

### What a DFA cannot do

A DFA has finitely many states, so it can only remember a bounded amount. It **cannot** recognize

$$
\{a^nb^n\mid n\ge0\}=\{\varepsilon,ab,aabb,aaabbb,\dots\}.
$$

*Proof by pigeonhole* ([[DM 07 Counting]]). Suppose a DFA with $k$ states recognizes it. Feed it $a^0,a^1,\dots,a^k$: that is $k+1$ prefixes, so two of them, $a^i$ and $a^j$ with $i\neq j$, leave the machine in the same state. Then appending $b^i$ must give the same verdict for both. But $a^ib^i$ should be accepted and $a^jb^i$ rejected. Contradiction. $\blacksquare$

Matching brackets is the same problem: you must count how many are open. Recognizing such languages needs extra memory, such as a stack (pushdown automata and context-free grammars, the basis of parsers). With unbounded memory you reach the **Turing machine**, the model of all computation, and its limits: some problems, such as deciding whether an arbitrary program halts, no algorithm can solve.

### State machines in practice

Robots, protocols and user interfaces are routinely written as finite state machines:

| State | Event | Next state |
|---|---|---|
| idle | task received | approach |
| approach | object in reach | grasp |
| grasp | grip confirmed | lift |
| grasp | grip failed | approach |
| any | emergency stop | halt |

Explicit states make behaviour testable: you can list every state and check that every event is handled in each. Behaviour trees, common in robotics, extend the same idea with hierarchy.

## Common mistakes

- **Treating Boolean $+$ as numeric addition.** $1+1=1$.
- **Leaving a transition undefined.** A DFA needs exactly one transition per state per symbol; add an explicit "dead" state for invalid input.
- **Trying to match nested structure with a regular expression.** Regex cannot balance brackets in general; use a parser.

## Learn by doing

1. Simplify $x+\bar xy$.
2. Write the sum of products for $f(x,y)$ that is 1 only when $x\neq y$, and name the function.
3. Design a DFA over $\{0,1\}$ accepting strings that end in `1`.
4. Trace the divisible-by-3 DFA on `1001` (nine). Accepted?

> [!success]- Check your answers
> 1. $x+\bar xy=(x+\bar x)(x+y)=x+y$ (second distributive law).
> 2. $\bar xy+x\bar y$, which is XOR.
> 3. Two states: $A$ (last symbol was not 1, start) and $B$ (last symbol was 1, accepting). From either state, `0` goes to $A$ and `1` goes to $B$.
> 4. $0\xrightarrow11\xrightarrow02\xrightarrow01\xrightarrow10$. Ends in 0: accepted.

## Where this shows up

Task-level robot control is often a state machine or behaviour tree wrapped around learned skills ([[15 Robot Systems and Deployment]]). Neural network hardware is built from these gates, and tokenizers for language models are built on regular-expression rules ([[13 Vision Language Action Models]]).

You have finished the course. Return to the checkpoint questions in [[DM 00 Course Map]].

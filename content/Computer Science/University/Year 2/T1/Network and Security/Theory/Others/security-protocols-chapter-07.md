# Security Protocols - Chapter 7

**Course:** ECM2426: Network and Computer Security  
**Chapter:** 7 - Security Protocols  
**Author:** Achim D. Brucker  
**Email:** a.brucker@exeter.ac.uk  
**Website:** https://brucker.ch/  
**Affiliation:** Software Assurance & Security Research, Department of Computer Science, University of Exeter  
**Version:** 1.0  

*Source: 2025-ecm2426-handout_chapter-07_security-protocols.pdf*  
*Generated on: Mon Oct 20 16:49:27 BST 2025*

---

## Table of Contents

1. [Motivation](#motivation)
2. [Designing a Key-Establishment Protocol](#designing-a-key-establishment-protocol)
3. [Notation Used in Protocol Modeling](#notation-used-in-protocol-modeling)
4. [Attacks on Security Protocols](#attacks-on-security-protocols)

### Changelog
- Initial release

---

## 1. Motivation

### Why Security Protocols Matter

**Cryptographic Primitives vs. Secure Applications:**
- RSA, AES, etc. provide (probably) very good cryptographic primitives
- **Challenge:** How can we construct secure distributed applications with these primitives?

### Applications Requiring Security Protocols

- **E-commerce** - Secure online transactions
- **E-banking** - Financial transaction security  
- **E-voting** - Electoral integrity and privacy
- **Mobile communication** - Secure mobile networks
- **Digital contract signing** - Legal document authentication

### Key Insight
> Even if cryptography is hard to break, constructing secure distributed applications is not a trivial task.

---

## 2. Case Study: Needham-Schroeder Public Key Protocol (NSPK)

### Problem: Establishing an Authentic Channel

**Scenario:** Alice wants to be sure that she talks to Bob (authenticity)

```
Alice ←--→ Eve ←--→ Bob
```

### The NSPK Protocol (1978)

Needham and Schroeder proposed the following protocol:

**Message Flow:**

1. $$A \rightarrow B: \{A, N_A\}_{K_B}$$
   - *"I am Alice and here is my nonce $N_A$."*

2. $$B \rightarrow A: \{N_A, N_B\}_{K_A}$$
   - *"Here is your nonce $N_A$ and I have one for you."*

3. $$A \rightarrow B: \{N_B\}_{K_B}$$
   - *"I got it! It is $N_B$."*

**Definition:** A **Nonce** (short for: number used once) is a fresh secret only known to the person generating it.

### Correctness Analysis

**Goal:** Mutual Authentication (Two-way Authentication)

After executing the protocol successfully, Alice and Bob can be sure to talk to each other (and not to somebody else).

**Correctness Argument (Informal):**

1. **Step 1:** $$\{A, N_A\}_{K_B}$$
   - "This is Alice and I have chosen a nonce $N_A$."

2. **Step 2:** $$\{N_A, N_B\}_{K_A}$$
   - "Here is your nonce $N_A$. Since I could read it, I must be Bob."
   - "I also have a challenge $N_B$ for you."

3. **Step 3:** $$\{N_B\}_{K_B}$$
   - "You sent me $N_B$. Since only Alice can read this and I sent it back, I must be Alice."

### Attack Scenario: Man-in-the-Middle

Let's examine what happens with an attacker Eve:

```
Alice ←--→ Eve ←--→ Bob
```

**Attack Flow:**
1. $$A \rightarrow E: \{A, N_A\}_{K_E}$$ (Alice thinks she's talking to Bob)
2. $$E \rightarrow A: \{N_A, N_E\}_{K_A}$$ (Eve responds with her own nonce)
3. $$A \rightarrow E: \{N_E\}_{K_E}$$ (Alice completes the protocol with Eve)

**Result:** Alice thinks she established a secure channel with Bob, but actually established one with Eve!

---

## 3. Security Protocol Definitions

### Definition: Protocol
A **protocol** consists of a set of rules (conventions) that determine the exchange of messages between two or more principals.

*In short, a distributed algorithm with emphasis on communication.*

### Definition: Security Protocol  
**Security (or cryptographic) protocols** use cryptographic mechanisms to achieve security objectives, such as:

- **Entity authentication** - Verifying the identity of communicating parties
- **Message authentication** - Ensuring message integrity and origin
- **Key establishment** - Securely distributing cryptographic keys
- **Integrity** - Ensuring data hasn't been tampered with
- **Timeliness** - Preventing replay attacks
- **Fair exchange** - Ensuring both parties receive what they expect
- **Non-repudiation** - Preventing denial of actions

> **Note:** Implementing/designing security protocols can sometimes feel like programming Satan's computer...

---

## 4. Designing a Key-Establishment Protocol

### Problem Statement

**Scenario Overview:**
Let's design a good security protocol from first principles!

**Communication Architecture:**
- A set of users, any two of whom may wish to establish a new session key for subsequent secure communications
- Successful completion of key establishment (& entity authentication) is only the start
- Further communication may be based on this established key
- **Important:** Users are not necessarily honest!

**Server Requirements:**
- An **honest server** (often called "trusted server", but trust ≠ honesty!)
- We assume that an honest server never cheats and never gives out secrets of users

### The Details

**Protocol Roles:**
1. **Initiator role** $A$ (Alice)
2. **Responder role** $B$ (Bob)  
3. **Server role** $S$

**Agents vs. Roles:**
- In a concrete execution of a protocol, roles are played by **agents (principals)**: $a, b, c$ (Charly), $s$, ...
- We use $i$ as the name of the **intruder**
- **Important:** No agent in our model knows that $i$ is not honest

**Protocol Aims:**
- At the end of the protocol, $K_{AB}$ should be known to $A$ and $B$
- Possibly known to $S$ (who forgets it immediately), but to no other parties
- $A$ and $B$ can assume that $K_{AB}$ is newly generated

```
    A ←--→ S ←--→ B
```

**Formalization Questions (for later consideration):**
- How do we formalize the protocol steps and goals?
- How do we formalize "knowledge", "secrecy", "newly", etc.?

---

## 5. First Attempt at Key Establishment

### Specification

Our first attempt consists of three messages:

1. $$A \rightarrow S: A, B$$
   - $A$ contacts $S$ by sending the identities of the two parties who are going to share the session key

2. $$S \rightarrow A: K_{AB}$$
   - $S$ sends the key $K_{AB}$ to $A$

3. $$A \rightarrow B: K_{AB}, A$$
   - $A$ passes $K_{AB}$ on to $B$

```
Message Flow:
A ←--→ S ←--→ B

1) A,B →
2) ← K_{AB}
3) K_{AB}, A →
```

**Note:** $K_{AB}$ does not contain any "information" about $A$ or $B$, but is simply a name for the bit-string representing the session key.

### Specification Discussion

This is a **significantly incomplete** protocol specification:

**Limitations:**
1. **Only successful runs specified**
   - No description of what happens when a message of wrong format is received
   - No description when no message is received at all
   - This is often done for security protocols, since error messages are often not relevant for security

2. **No specification of internal actions**
   - e.g., "create fresh $K_{AB}$" and store that it is a key for $A$ and $B$
   - $A$ and $B$ "know" that received messages are part of the protocol
   - Common to omit details required for networked computer implementation

### More Specification Details

**Additional Considerations:**
- Details of which key should be used to decrypt a received message which has been encrypted
- Tracking the progress of a particular protocol run

> **Note:** Despite its limitations, specifying protocols by showing only the messages of a successful run remains the most popular method of describing security protocols.

### Alternative Notation: Alice & Bob Notation

**Equivalent representation:**

1. $$A \rightarrow S: A, B$$
2. $$S \rightarrow A: K_{AB}$$
3. $$A \rightarrow B: K_{AB}, A$$

**Important Notes:**
- Sender/receiver names (e.g., "$A \rightarrow B$") are not part of messages
- Messages do not automatically reach their destination (securely)

---

## 6. First Problem: Security Analysis

### The Issue
**Question:** This protocol is not secure. What is the problem?

The session key $K_{AB}$ must be transported to $A$ and $B$ but to **no other parties**.

### Security Assumption 1
> **Definition:** The intruder is able to eavesdrop on all messages sent in a security protocol.

```
Message Flow (with eavesdropping):
A ←--→ S ←--→ B
  ↓       ↓       ↓
  Intruder can see all messages
```

**Analysis:**
1. $$A \rightarrow S: A, B$$ ✓ (No sensitive data)
2. $$S \rightarrow A: K_{AB}$$ ❌ (Key exposed!)
3. $$A \rightarrow B: K_{AB}, A$$ ❌ (Key exposed again!)

**Problem:** The intruder can read $K_{AB}$ from messages 2 and 3, completely compromising the protocol.

---

## 7. Second Attempt: Using Pre-shared Keys

### Specification with Encryption

Let us assume that $S$ initially shares a secret key $sk(U,S)$ with each user $U$ of the system:
- $sk(A,S)$ with $A$
- $sk(B,S)$ with $B$

**Improved Protocol:**

1. $$A \rightarrow S: A, B$$
2. $$S \rightarrow A: \{K_{AB}\}_{sk(A,S)}, \{K_{AB}\}_{sk(B,S)}$$
3. $$A \rightarrow B: \{K_{AB}\}_{sk(B,S)}, A$$

**Improvement:** $S$ uses the pre-shared keys to encrypt the message in step 2. Eavesdropping $K_{AB}$ is no longer possible.

### Perfect Cryptography Assumption
> **Definition:** Encrypted messages may only be read by the legitimate recipients who have the keys required to decrypt them.

```
Message Flow (with encryption):
A ←--→ S ←--→ B

1) A,B →
2) ← {K_{AB}}_{sk(A,S)}, {K_{AB}}_{sk(B,S)}
3) {K_{AB}}_{sk(B,S)}, A →
```

### Problems with Second Attempt

**Issue:** The protocol is (still) not secure. What is the problem?

The information about **who else has $K_{AB}$** is not protected. The intruder could capture messages and alter them.

### Security Assumption 2
> **Definition:** The intruder is able to intercept messages on the network and send messages to anybody (under any sender name).

**In other words:** The intruder has complete control over the network.

**Worst-case scenario:**
- Although there may be no more than 4 or 5 messages involved in a legitimate run of the protocol
- There are an infinite number of variations in which the intruder can participate  
- These variations involve an unbounded number of messages
- Each must satisfy the protocol's security requirements

### Attack 1: Identity Substitution

**Simple Attack:**
The intruder simply intercepts the message from $a$ to $b$ and substitutes $D$ for $a$'s identity ($D$ is any agent name).

**Attack Flow:**

1. $$a \rightarrow s: a, b$$
2. $$s \rightarrow a: \{k_{ab}\}_{sk(a,s)}, \{k_{ab}\}_{sk(b,s)}$$
3. $$a \rightarrow i: \{k_{ab}\}_{sk(b,s)}, a$$ (intercepted)
3'. $$i \rightarrow b: \{k_{ab}\}_{sk(b,s)}, D$$ (altered)

**Result:** $b$ believes that they are sharing the key with $D$, whereas in fact they are sharing it with $a$.

**Assessment:**
- Severity depends on the scenario, but may include $b$ giving away information to $a$ which should have been shared only with $D$
- Although $i$ does not obtain $k_{ab}$, we can still regard the protocol as broken since it does not satisfy the requirement that users should know who else knows the session key

### Attack 2: Key Redirection

**More Serious Attack:**
$i$ alters the message from $a$ to $s$ so that $s$ generates a key $k_{ai}$ for $a$ and $i$, and encrypts it with the key $sk(i,s)$.

**Attack Flow:**

1. $$a \rightarrow s: a, b$$ (intercepted)
1'. $$i \rightarrow s: a, i$$ (altered request)
2. $$s \rightarrow a: \{k_{ai}\}_{sk(a,s)}, \{k_{ai}\}_{sk(i,s)}$$

**Problem:** Since $a$ cannot distinguish between encrypted messages $\{k_{ab}\}_{sk(a,s)}$ and $\{k_{ai}\}_{sk(a,s)}$, $a$ will accept the key $k_{ai}$ thinking it's for communication with $b$.

**Result:** The intruder $i$ now shares a key with $a$, while $a$ believes the key is for communication with $b$.

---

## 8. Protocol Notation and Modeling

### Standard Notation Elements

**Message Components:**
- **Principals:** $A, B, S$ (Alice, Bob, Server)
- **Keys:** $K_{AB}$ (shared key), $sk(A,S)$ (secret key between A and S)
- **Nonces:** $N_A, N_B$ (fresh random numbers)
- **Encryption:** $\{M\}_K$ (message M encrypted with key K)

**Message Transmission:**
- $$A \rightarrow B: M$$ means "A sends message M to B"
- $$A \leftarrow B: M$$ means "A receives message M from B"

### Security Assumptions Summary

1. **Eavesdropping:** Intruder can read all network traffic
2. **Active Attacks:** Intruder can intercept, alter, and inject messages
3. **Perfect Cryptography:** Only key holders can decrypt messages
4. **Network Control:** Intruder has complete control over the network

### Common Attack Patterns

1. **Man-in-the-Middle:** Intercepting and relaying communications
2. **Identity Substitution:** Changing sender/receiver identities
3. **Key Redirection:** Forcing key establishment with attacker
4. **Replay Attacks:** Reusing old messages
5. **Parallel Session Attacks:** Using multiple protocol runs

---

## Mathematical Notation Reference

### Common Symbols Used
- $A, B, S$ - Agents (Alice, Bob, Server)
- $K_{AB}$ - Session key between A and B
- $sk(A,S)$ - Pre-shared secret key between A and S
- $N_A, N_B$ - Nonces (numbers used once)
- $\{M\}_K$ - Message M encrypted with key K
- $\rightarrow$ - Message transmission
- $i$ - Intruder/Attacker

### Protocol Notation

- $$A \rightarrow B: M$$ means "A sends message M to B"
- Messages can be intercepted, altered, or blocked by attackers
- Perfect cryptography assumption: only holders of correct keys can decrypt messages

### Key Concepts

**Freshness:** Ensures that keys and nonces are newly generated for each protocol run

**Authentication:** Verifying the identity of communication partners

**Secrecy:** Ensuring that sensitive information (like session keys) is only known to authorized parties

**Integrity:** Guaranteeing that messages haven't been tampered with during transmission

---

## Summary

This chapter introduces the fundamental concepts of security protocols:

1. **Motivation:** Even with strong cryptographic primitives, building secure distributed systems is challenging
2. **Protocol Design:** Systematic approach to designing key establishment protocols
3. **Security Analysis:** Understanding common attack patterns and vulnerabilities
4. **Formal Methods:** Mathematical notation for precise protocol specification

### Key Takeaways

- Security protocols are distributed algorithms with emphasis on secure communication
- Multiple iterations and security analysis are needed to develop robust protocols
- Attackers have significant capabilities (eavesdropping, message manipulation, network control)
- Formal analysis tools are essential for proving protocol security

### Next Steps

The following topics build on this foundation:
- Formal verification methods
- BAN logic for protocol analysis
- Modern protocols (TLS, SSH, etc.)
- Implementation security considerations

---

**© 2025 Logical Hacking. ECM2426 Student Notes**
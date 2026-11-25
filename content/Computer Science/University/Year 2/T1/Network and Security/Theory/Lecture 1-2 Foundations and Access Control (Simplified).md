---
tags: [network-security, access-control, exam]
aliases: [NS Lecture 1-2 Simplified]
---

# Lecture 1-2 Foundations and Access Control (Simplified)

> [!summary] Quick map
> - CIA goals and tradeoffs
> - Identity -> authentication -> authorization -> access control
> - Authentication factors and examples
> - ACM, RBAC, hierarchical RBAC
> - Compartments, labels, lattices
> - Bell-LaPadula rules
> - DAC, break-glass, usage control

## 1) CIA triad (core goals)

| Goal | Plain meaning | If broken | Example |
| --- | --- | --- | --- |
| Confidentiality | Keep information secret from unauthorized parties | Data leak | Unencrypted database dump |
| Integrity | Prevent unauthorized modification | Tampered records | Grades changed |
| Availability | Keep information accessible to authorized parties | Downtime | DDoS knocks service offline |

> [!note] Tradeoffs
> These goals can conflict (e.g., more confidentiality can reduce availability).

## 2) Identity and access control pipeline

| Term | Plain meaning | Example |
| --- | --- | --- |
| Subject | The actor (human or process) | User or running process |
| Object | The resource | File, data, function, device |
| Identification | Claim an identity | Username |
| Authentication | Prove the claim | Password, OTP |
| Authorization | Decide permissions | Allow read, deny write |
| Access control | Enforce the policy | ACL check |

Flow to remember:
Identification -> Authentication -> Authorization -> Access control enforcement.

> [!tip] Memory hook
> Think: "Who are you?" -> "Prove it." -> "What can you do?" -> "Enforce it."

## 3) Authentication mechanisms (4 factors)

| Factor | What it is | Examples | Notes |
| --- | --- | --- | --- |
| Something you know | Secret knowledge | Password, PIN | Widely used |
| Something you have | A token/device | Smart card, OTP generator, UniCard, phone app | Physical or soft token |
| Something you are | Biometric trait | Fingerprint, face, retina | Can be spoofed |
| Context/location | Where you are | Inside secure building | "You are here" |

### Passwords
- Widely used but hard to remember.
- Good passwords are long and random.
- Good systems allow arbitrary length and store passwords hashed and salted.
- Key questions: how to store/validate safely and how to access systems securely.

### Hardware tokens
- Examples: chip cards, OTP generators, UniCard.
- Trend toward soft tokens (apps on phones).

### Biometrics
- Promising but not perfect.
- Sensors can be tricked.
- Legal/privacy issues (e.g., is a fingerprint protected speech?).

## 4) Access control basics

- Access control specifies who can do what and must be enforced.
- Real systems are complex: context/state matters, permissions change over time,
  obligations may be required, and bugs exist.

### Simple access control relation
$$AC=\text{Subject} \times \text{Object} \times \text{Request} $$
Example permission check:
$$\text{(Achim, Exam2426, set)} \in AC$$

## 5) Forms of access control

| Layer | Example |
| --- | --- |
| Physical | Gates, turnstiles |
| Network | Firewalls |
| Hardware | Memory management |
| Operating system | File system permissions |
| Application | Logins, database permissions |

## 6) Policy vs model

| Concept | Plain meaning |
| --- | --- |
| Security policy | Rules of what is allowed or forbidden |
| Security model | Formal representation to reason about policies |

## 7) Access Control Matrix (ACM)

- Think of a table: subjects x objects, entries are privileges.
- Protection state (relative to privileges P) is a triple $(S,O, M)$ with:
  - A set of current subjects $S$
  - A set of current objects $O$
  - A access control matrix $M$, defining privileges for each $(s,o)$

Formally, $M$ can be seen as:
- a relation $S\times O \times P$
- equivalently, a function $S \times O \implies \rho (P)$

> [!warning] Scaling issue
> The matrix is conceptually clear but does not scale to millions of subjects/objects.

## 8) Role-Based Access Control (RBAC)

- Core idea: users get roles; roles get permissions.
- Decouples users from permissions, so it scales better.

Formalization:
- a set of *ROLES*
- a set of *USERS*
- a relation $UA\subset USER \times ROLES$
- a relation $PA \subset ROLES \times PERMISSION$

The access control model is:
$$AC:=PA\circ UA$$
i.e
$$AC:=\{(u,c)\in\text{Users} \times \text{Permissions}\space |\space \exists r\in ROLES.(u, r)\in UA \land (r, p)\in PA\}$$

Example:
$$ROLES = \{\text{User, SuperUser}\}$$
$$USERS = \{\text{Alice, Bob, John}\}$$
$$UA = \{(\text{Alice, User}), (\text{Alice, SuperUser}), (\text{Bob, User}), (\text{John, User})\}$$
$$PA=\{(\text{User, read file 1}, (\text{Superuser, write file 1}))\}$$

> [!example] Practice
> What are the permissions of John? What are the permissions of Alice?

### Extending RBAC
- Role hierarchies.
- Who can change permissions.
- Context constraints (e.g., must be owner).
- Users switching roles.

## 9) Hierarchical RBAC

Hierarchical RBAC adds a role hierarchy $RH \subset ROLES \times ROLES$.

The access control model is:
$$AC:=PA\space \circ \space RH \space \circ UA$$
i.e
$$AC:=\{(u,p)\in \text{Users }\times\text{ Permissions}\space \mid \space \exists r, r'\in ROLES. (u, r)\in UA\space \land \space(r, r')\in RH\space \land\space (r', p)\in PA \}$$

Example hierarchy and assignments:
$$
\begin{aligned}
RH=\{(\text{admin, admin}),\\ (\text{admin, finance}),\\(\text{admin, hr}),\\(\text{finance, finance}),\\(\text{finance, employee}),\\(\text{HR, HR}),\\(\text{HR, employee})\}
\end{aligned}
$$
$$
\begin{aligned}
\text{Permissions} = \{\text{read-DS, write-DS, read-HR, write-HR, read-CRM, write-CRM}\}
\end{aligned}
$$
$$
\begin{aligned}
UA = \{(\text{alice, admin}),\\ (\text{bob, admin}),\\ (\text{charlie, finance}),\\(\text{eve, finance}),\\(\text{Dove, HR}),\\(\text{Fiona, HR}), \\(\text{George, employee}), \\(\text{Hugh, employee}), \\(\text{Isabelle, employee}), \\(\text{employee, read-DS}),, \\(\text{employee, read-CRM}),, \\(\text{employee, read-HR}),\}
\end{aligned}
$$

## 10) Compartments, labels, and ordering

- Compartments (categories) implement "need-to-know" (e.g., SAT, EUR, ASI).
- Labels can combine clearance + compartments.
- You can only see information if you are cleared for all categories.

Examples of labeled info:
- Top Secret, UK
- Top Secret, Canada
- Top Secret, UK and Canada

### Partially ordered sets
- A set $S$ with a relation $\leq$, written $(S, \leq)$, is partially ordered if:
  - Reflexive: $\forall a \in S, a \leq a.$
  - Transitive: $\forall a,b,c \in S$ if $a\leq b$ and $b \leq c$ then a $a \leq c$
  - Anti-symmetric: $\forall a, b \in S$ if $a\leq b$ and $b\leq a$. then $a=b$
- Examples:
  - Natural numbers with less-than-or-equal (total order).
  - Sets under subset relations (not total).
  - Natural numbers ordered by divisibility.

### Lattices
- A partially ordered $(S, \leq)$ where any two elements have a least upper
  bound and greatest lower bound.
$$a \leq u, b\leq u \space \space \mid ((a\leq v) \land (b \leq v)) \implies (u \leq v)\text{. for all }v\in S$$
$$l \leq a, l\leq b \space \space \mid ((k\leq a) \land (k \leq b)) \implies (k \leq l)\text{. for all }k\in S$$

Examples:
- Natural numbers in an interval ($0...n$).
- Linear order of clearances $U\leq C \leq S \leq TS$.
- Powerset of categories under inclusion (SAT, EUR, ASI).

Why lattices:
- Find the minimal clearance needed to read two objects.
- Find the maximal label an object can have that can still be read by two users.
- Fit "need-to-know" + least privilege.

## 11) Bell-LaPadula (BLP) model (confidentiality, MAC)

- Combines lattice labels with state transitions.
- Read-down (Simple Security Policy):
  - Subject with label $x_s$ can read object with label $x_0$ only if $x_s$
    dominates $x_0$.
- Write-up (Star Property):
  - Subject with label $x_s$ can write to object with label $x_0$ only if $x_0$
    dominates $x_s$.
- Main insight: prohibiting write down prevents reclassification/leaks.
- If implemented securely, no information leakage (no read up + no write down).
- Limits: blocks some legitimate sharing from high to low.
  - Workarounds: temporary downgrade or trusted subjects.
- MAC labels cannot be changed by normal subjects; used in systems like SELinux.

## 12) Other access control systems

| System | Idea | Example |
| --- | --- | --- |
| DAC | Owners can change permissions | Unix/Linux files |
| Break-glass | Override in emergencies | Hospital "emergency access" |
| MAC (general) | Central labels + policy | Military systems |

## 13) Usage control (after access control)

- Controls how you can use data after access.
- Examples: "watch 3 times in 2 weeks," "read but do not share."
- Techniques: DRM, watermarking, monitoring in trusted environments.

> [!summary] Quick exam checklist
> - [ ] Define CIA and explain tradeoffs.
> - [ ] Distinguish identification vs authentication vs authorization.
> - [ ] List the 4 auth factors with examples.
> - [ ] Explain ACM vs RBAC and why RBAC scales.
> - [ ] State BLP rules: no read up, no write down.
> - [ ] Explain labels, compartments, partial orders, and lattices.
> - [ ] Know DAC vs MAC vs RBAC use cases.

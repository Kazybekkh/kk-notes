 7. Foundations: Confidentiality Integrity, and Availability
8. Authentication and Identification
9. Access Control

# Foundations: Confidentiality Integrity, and Availability
## The Three Fundamental Concepts of Security: CIA


- **Confidentiality**
	- Protecting information from disclosure to unauthorized parties
- **Integrity**
	- Protecting information from being modified by unauthorized parties
- **Availability**
	- Ensuring that information is available (accessible) to authorized parties

# Authentication and Identification

To decide if a **subject**(e.g a human person) is a member of an authorized party that can **access** (i.e execute an operation such as read, write, or execute on) an **object** (resource) (i.e a physical object, a function call, data/information), we need to solve
- Identification
	- Associating an  **identity** with a **subject**
- Authentication
	- Verifying the validity of something (usually the **identity** claimed by a system entity)
- Authorization
	- Granting (or denying) the right or permission of a system entity to access an object
- Access Control
	- Controlling **access** of system entities (on behalf of **subjects**) to **objects** based on an **access control policy** ("security policy").

## Mechanisms for Identity Authentication
1. Something that you **know**
	1. e.g password or a PIN
2. Something that you **have**
	1. E.g a smart card or a one-time password generator
3. Something that you **are**
	1. E.g Biometric characteristics e.g a facial scan/photograph
4. Context location, e.g **your current location**
	1. E.g being physically close to an object, being in a secure building

### Example of Something That You **Know**: Passwords
- **Passwords**
	- Are widely used
	- Hard to remember
- Good passwords are: **long and random**
- Good systems:
	- Allow for passwords of arbitrary length
	- store passwords hashed and salted
- Questions that we are interested in
	- How to store and validate passwords securely
	- How to access systems securely that require a password

### Example of Something That You Have: Hardware Tokens
- Examples
	- Chip Cards
	- One-time password generators
	- Your UniCard
- Today, we see a shift towards soft-tokens, eng. a one-time password app on your mobile
- Is your UniCard a good hardware token?

### Example of Something That You Are: Biometrics
- Uses characteristics of your body. e.g
	- Fingerprint
	- Retina Scan
- On the first sight: very promising
- Many unsolved problems:
	- Is a fingerprint a secret protected by the first amendment, i.e the protection of free speech
	- Biometric sensors can be tricked




## Access Control

- Typical **Access Control System** focus on **authorization**:
	- Specification of who is allowed to do what (permissions)
	- How to update/change permissions
- A simple access control model $AC$ is a relation
$$AC=\text{Subject} \times \text{Object} \times \text{Request} $$
- Example of a simple permission check:
$$\text{(Achim, Exam2426, set)} \in AC$$
- In reality, quite complex:
	- Might depend on the system state (or context)
	- Subjects and permissions change over time
	- Access rights might require the fulfillment of obligations
	- implementation bugs
	- Access control needs to be enforced

## Forms of Access Control
- Access Control might come in various forms:
	- Physical protection
		- e,g gates, turnstiles
	- Network traffic
		- e.g firewalls
	- Hardware
		- e.g memory management
	- Operating System
		- e.g file system
	- Application level
		- e.g Google login, databases

## Policies vs Models

- A **security policy** defines what is allowed (and/or forbidden)
	- It is analogous to a set of laws
	- Defined in terms of rules and/ or requirements
- A **security model** is a (formal) *representation* if a class if systems (and their behavior)
	- highlights security features on a chosen level of abstraction
	- provides a vocabulary to develop specific policies
## The Access Control Matrix Model
(Introduction)
- Based on the ideas of **privileges** of ***subjects*** on ***objects*** 
	- Subjects: users, processes, agents, groups
	- Objects: data, memory banks, other processes, files...
	- Privileges: right to read, write, modify
- Abstract: a model
- Implementation: a mechanism

### (Protection State)
- A **protection state**, relative to a set of **privileges** $P$, is a triple $(S,O, M)$ with:
	- A set of current subjects $S$
	- A set of current objects $O$
	- A access control matrix $M$, defining
		- the privileges for each $(s,o)\in S \times O$, i.e 
		- a relation $S\times O \times P$
		- equivalently, a function $S \times O \implies \rho (P)$
- Example
	- ![[../../../../../../Screenshots/Screenshot 2025-12-20 at 3.34.43 AM.png]]
- Does this scale ?
- What about systems with thousands (millions) of subjects and objects?




# Role-Based Access Control (RBAC)

(Introduction)

- How can we formalize a policy for more than 
	- thousands or millions of subjects
	- a similar number of objects
- An Access Control Matrix is most likely **unmaintainable**
- Observation
	- Subjects(users) often have roles e.g
		- customer, employee, student
	- Roles share the same rights e.g
		- students can attend lecture
- Core idea of **RBAC**
	- Create roles for job functions in enterprises
	- Assign users to roles (based on their responsibilities)
	- Assign a set of permissions to each role
- RBAC decouples users and permissions by introducing roles

### Formalization

- RBAC is formalized by
	- a set of *ROLES*
	- a set of *USERS*
	- a relation $UA\subset USER \times ROLES$
	- a relation $PA \subset ROLES \times PERMISSION$
- The access control model is
$$AC:=PA\circ UA$$
i.e
$$AC:=\{(u,c)\in\text{Users} \times \text{Permissions}\space |\space \exists r\in ROLES.(u, r)\in UA \land (r, p)\in PA\}$$
![[../../../../../../Screenshots/Screenshot 2025-12-21 at 9.00.42 AM.png]]

Or formally
$$ROLES = \{\text{User, SuperUser}\}$$
$$USERS = \{\text{Alice, Bob, John}\}$$
$$UA = \{(\text{Alice, User}), (\text{Alice, SuperUser}), (\text{Bob, User}), (\text{John, User})\}$$
$$PA=\{(\text{User, read file 1}, (\text{Superuser, write file 1}))\}$$
- What are the permissions of John?
- What are the permissions of Alice?

### Extending RBAC
- Would recommend simple RBAC to your bank?
	- role hierarchies
	- who can change permission
	- context information (constraints, e.g subject must be the owner of the object)
	- users switching roles

### Hierarchical RBAC
Hierarchical RBAC extends RBAC with a role hierarchy $RH$: 
- a set of $ROLES$
- a set of $USERS$
- a relation $UA\subset USER \times ROLES$
- **a relation $RH \subset ROLES \times ROLES$** 
  describing the role hierarchy
- a relation $PA\subset ROLES \times PERMISSION$

The access control model is:
$$AC:=PA\space \circ \space RH \space \circ UA$$
i.e
$$AC:=\{(u,p)\in \text{Users }\times\text{ Permissions}\space \mid \space \exists r, r'\in ROLES. (u, r)\in UA\space \land \space(r, r')\in RH\space \land\space (r', p)\in PA \}$$



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
![[../../../../../../Screenshots/Screenshot 2025-12-24 at 6.30.57 PM.png]]



### Compartments
A **compartment** (or category) specifies a domain for **need-to-know** policy. Examples: SAT= Satellite Data, EUR = Europe, ASI = Asia.
- Compartments are critical in complex coalitions
- Examples
	- The US may also have allies that do not with to share information(perhaps the UK and Canada, Policy must support)
	- Top Secret, UK
	- Top Secret, Canada
	- Top Secret, UK and Canada
### Labeling and ordering
![[../../../../../../Screenshots/Screenshot 2025-12-24 at 6.54.44 PM.png]]
- Both notions of classification induce an ordering
- Bell and La Padula suggesting using lattices here
- You can only see information if you are cleared to access all categories labelling it under the ordering relation

### Partially-ordered sets
- A set $S$ with a relation $\leq$, written $(S, \leq)$, is **partially ordered**
- if $\leq$ is:
	- **Reflexive**: $\forall a \in S, a \leq a.$
	- **Transitive**: $\forall a,b,c \in S$ if $a\leq b$ and $b \leq c$ then a $a \leq c$
	- **Anti-symmetric**: $\forall a, b \in S$ if $a\leq b$ and $b\leq a$. then $a=b$
- Examples
	- Natural numbers with less-than-or-equal (total order)
	- Sets under subset relations (not a total order)
	- Natural numbers ordered by divisibility
### Latices
- A partially ordered $(S, \leq)$ where for all $a, b \in S$ there exists a **least upper bound** $u in S$ and a **greatest lower bound** $l\in S$, i.e
$$a \leq u, b\leq u \space \space \mid ((a\leq v) \land (b \leq v)) \implies (u \leq v)\text{. for all }v\in S$$
$$l \leq a, l\leq b \space \space \mid ((k\leq a) \land (k \leq b)) \implies (k \leq l)\text{. for all }k\in S$$
Examples
- Natural numbers in an interval ($0...n$) with less-than-or-equal
- Linear order of clearances $U\leq C \leq S \leq TS$
- Powerset of a a set under inclusion (of security categories e.g SAT, EUR, ASI)
Moreover, you build new lattices from existing ones, e.g by component-wise combination(lattice product)

### Computing clearance (an example)
![[../../../../../../Screenshots/Screenshot 2025-12-24 at 7.47.53 PM.png]]
### Why lattices
- Recall all pairs of lattice elements have a **least upper bound** and a **great lower bound**
- If labels form a lattice, we can uniquely answer questions like
	- Given two objects with different labels. what is the **minimal label** a subject requires to be allowed to read both objects?
	- Given two subjects with different labels, what is the **maximal label** an object can have that can still be read by both subjects?
- Well suited for **need-to-know** policies, where each subject is assigned a label reflecting **least privilege** required for his function

# The Bell-Lapudla (BLP) Model (1975)

![[../../../../../../Screenshots/Screenshot 2025-12-24 at 8.03.00 PM.png]]

### BLP Setup
- Combines lattice on labels with state-transition systems
- Access decisions satisfy following properties
	- **Read-down** (also called **Simple Security Policy**)
		- A subject with label $x_s$, can only read information in an object with label $x_0$ if $x_s$ **dominates** $x_0$
	- **Write-up** (also called **Property**)
		- A subject with label $x_s$ can only write information to an object with a security label $x_0$ **dominates** $x_s$
- Main Insight: **Prohibiting write down** is essential confidentiality as otherwise information can effectively be reclassified. 

### BLP -- disallowed operations
![[../../../../../../Screenshots/Screenshot 2025-12-24 at 8.07.29 PM.png]]

### BLP -- Conclusions
- No information leakage possible! (if implementation secure)
	- No read-up and no write-down prevent subjects from simultaneously having read access to information at least one level and write access to information at a lower level.
	- Since MAC. labels cannot be changed (by subjects or malware)
- But also prevents "legitimate" communication from high-level subjects to low-level ones. Possible solutions
	- temporarily downgrade the subject's security level
	- Identify a set of **trusted subjects** that may violate the star-minus property
- Mechanism support provided by some systems, e.g BLP module for SELinux

# Other Access Control Systems

- Discretionary access control (DAC): owners can change permissions
	- Example: unix/ linux file system
- Break-Glass access control allows to override the access control "in emergencies"


### Next Step After Access Control: Usage Control
- Traditional access control(as discussed previously) focuses
	- controlling access to documents/data/information
	- decisions that are fast to evaluate/decide
	- decisions that can immediately be enforced
- Usage Control
	- controlling the use of documents
		- you are allowed to read the book but no give it to someone else
		- you are allowed to watch this movie three times within the next two weeks
	- Techniques used for usage control or (DRM Digital Rights Management)
		- watermarking (violations/misuse is pursued economically/legally)
		- monitoring (easier in a closed/trusted environment. e.g using a trusted OS and/ or a trusted viewer)


# Key Take-Aways
- Traditionally, the three fundamental goals of cybersecurity are
	- Confidentiality
	- Integrity
	- Availability
	  (Already the three CIA goals are conflicting!)
- Common access control models are
	- DAC, often used in end-user file systems
	- Extended RBAC models, often used in business software
	- Bell-LaPadula variants are common in military applications
- Access control list/matrix models are often supported by file systems
- Many access control models have a similar expressiveness(one can be emulated by other)





One-Time Pad (OTP) encrypts m1…mnm1…mn with a random key k1…knk1…kn via ci=(mi+ki)  lci=(mi+ki)modl, giving perfect secrecy if the key is truly random, as long as the message, and never reused.
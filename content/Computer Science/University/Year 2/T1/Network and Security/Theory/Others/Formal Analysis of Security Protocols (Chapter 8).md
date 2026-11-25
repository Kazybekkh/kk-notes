Open C

## What are formal methods?

A language is formal when it has a well-defined syntax and semnatics,. Additionally, there is often a deductive system for determining the truth of statements. Examples: propositional logic, first order logic

- A model (or construction) is formal when it is specified in a formal language
- Standard protocol notation is not formal

## Formal modelling and analysis of protocols

Specification -> (satisfies - proof) -> Security Properties

Goal: formally model protocols and their properties and provide a mathematically sound means for reasoning about these models
Basis: suitable abstraction of protocols


Our Goal: An Automated Verification Tool

We would like to have a program $V$ with:
- input
	- some description of a program (protocol) $P$
	- Some description of a functional specification (security goals) $S$
- Output: Yes or no
- Bonus: in case No givea counter example


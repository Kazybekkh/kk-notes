# Discrete Math Glossary

Review key terms and their definitions from the Discrete Math course.

### [Binary and Bases](https://www.codecademy.com/paths/computer-science/tracks/cspath-discrete-math/modules/binary-and-bases/lessons/binary-and-bases/exercises/dm-what-is-a-number-base)

_Boolean Values_: A data type with two possible values, 0 and 1, often representing True/False data in computation

### [Congruences](https://www.codecademy.com/paths/computer-science/tracks/cspath-discrete-math/modules/congruences/lessons/congruences-lesson/exercises/what-are-congruences)

_a divides b_: A property on two integers a and b that holds if there exists an integer k for which a*k = b.

_a is congruent to b mod n_: A property on three integers a, b, and n, where n > 0, such that n divides a - b.

_Caesar cipher_: A cipher that takes a given phrase or string of letters and shifts each one three places down the alphabet.

_Function_: A relation such that each input x has at most one corresponding output y.

_Linear Congruence_: Congruence relationship where the unknown variable is contained in a linear expression. 

_Linear Expression_: Expression in the form `ax + b`, where a and b are constants and `x` is our unknown variable.

_mod_: Short-hand for modulus.

_Modular Arithmetic_: The operation that returns the remainder of b/a for two numbers a and b.

_Modulus_: The operator used to perform modular arithmetic.

_Reflexive Property for Congruences_: For two numbers a and n, n > 0, a is congruent to a mod n.

_Symmetric Property for Congruences_: For three numbers a, b, and n, n > 0, if a is congruent to b mod n, then b is congruent to a mod n.

_Transitive Property for Congruences_: For the integers a, b, c, and n, n > 0, if a is congruent to b mod n and b is congruent to c mod n, then a is congruent to c mod n.

_x relates to y_: A relationship where a given input x has a corresponding output y.

### [Counting Theory](https://www.codecademy.com/paths/computer-science/tracks/cspath-discrete-math/modules/counting-theory/lessons/counting-theory-lesson/exercises/introduction)

_Bit string (or) bitstring_: A sequence of bits (0 or 1).

_Hockey stick pattern_: When you descend Pascal’s triangle diagonally at first, then slant to form the shape of a hockey stick, the number in the slanted portion is the sum of the numbers that descended diagonally.

_Pascal’s Triangle_: To build the triangle, start with a ‘1’ at the top, then continue placing numbers below it in a triangular pattern. Each number is the sum of the numbers directly above it.

_Principle of Inclusion and Exclusion (PIE)_: For two sets A and B, |A ∪ B| = |A| + |B| − |A ⋂ B|.

_Product Rule_: If there are n(P) ways to do P and n(Q) independent ways to do Q, then the number of ways to do P and Q is n(P) * n(Q).

_Sum Rule_: If there are n(P) ways to do P and, distinct from them, n(Q) ways to do Q, then the number of ways to do P or Q is n(P) + n(Q).

### [Induction and Strong Induction](https://www.codecademy.com/paths/computer-science/tracks/cspath-discrete-math/modules/proofs/lessons/induction-and-strong-induction/exercises/intro-to-proofs-and-induction)

_Base Case(s)_: The smallest possible case(s) for which a given statement is true.

_Conjecture_: Mathematical term with the same meaning as a statement. 

_Induction_: A method of proof that is often used to prove statements with summations or recursions.

_Induction Hypothesis (for Mathematical Induction)_: The supposition that a given statement is true for some integer k exceeding the base case.

_Induction Hypothesis (for Strong Induction)_: The supposition that a given statement is true for all integers between the largest base case and some integer k exceeding that largest base case.

_Induction Proof_: A mathematical proof that uses induction.

_Inductive Step_: The process of constructing and proving the induction hypothesis.

_Mathematical Induction_: An induction technique that proves a statement by providing one base case, assuming the statement is true for some larger integer `k`, then proving the statement is true for `k+1` using said assumption (induction hypothesis).

_Mathematical Proof_: A mathematical explanation for why a given statement is either true or false.

_Nonnegative integer_: An integer `n` such that `n >= 0`.

_Strong Induction_: An induction technique that proves a statement by providing more than one base case, assuming the statement is true for all integers from the largest base case to some even larger integer `k`, and then proving the statement is true for `k+1` using that assumption (induction hypothesis).

_Summation_: Operation (denoted by the Greek letter capital Sigma) that adds consecutive terms together.

### [Permutations and Combinations](https://www.codecademy.com/paths/computer-science/tracks/cspath-discrete-math/modules/permutations-and-combinations/lessons/permutation-combination/exercises/enumeration)

_Combination_: An arrangement, or selection, in which the order does not matter.

_Enumeration_: The number of ways to select from, or arrange, a set of _n_ objects.

_Permutation_: An arrangement, or selection, in which the order matters.

### [Recurrence Relations](https://www.codecademy.com/paths/computer-science/tracks/cspath-discrete-math/modules/recurrence-relations/lessons/recurrence-relations/exercises/review-of-recursion)

_Boundary condition_: The starting value for a recurrence relation. In a sequence, this is the first number.

_Characteristic equation_: A polynomial equation derived from a linear recurrence relation the roots of which raised to nth power constitute the closed-form solution.

_Closed-form solution (for recurrence relations)_: A mathematical function, f(n), that computes the nth term of a sequence described by a recurrence relation.

_Coefficient_: multiplier that comes before a variable.

_Dynamic Programming_: A technique in which values are cached to be used for future computations.

_Homogeneous linear recurrence relation_: A linear recurrence relation that has no explicit dependence on n.

_Homogeneous solution_: The part of the closed-form solution to an inhomogeneous recurrence relation obtained by ignoring the f(n) term.

_Inhomogeneous linear recurrence relation_: A linear recurrence relation that contains a dependence on n; i.e., a recurrence relation that contains an f(n) term.

_Initial condition_: Same as boundary condition. This and “boundary condition” are used interchangeably.

_Linear recurrence relation_: A recurrence relation in which there is a linear dependence on previous values.

_Multiplicity of a root_: The number of times a root appears in the solution of a characteristic equation.

_Non-linear recurrence relation_: A recurrence relation in which there is a non-linear dependence on previous values.

_Particular solution_: The part of the closed-form solution to an inhomogeneous recurrence relation that assumes a solution must be of the same form as f(n).

_Recursive function, recurrence relation_: A function that computes a value by making a call to itself.

_Fibonacci sequence_: A sequence that starts with 0 and 1, with each next term being a sum of the terms before it.

### [Sequences and Summations](https://www.codecademy.com/paths/computer-science/tracks/cspath-discrete-math/modules/sequences-and-summations/lessons/sequences-and-summations/exercises/what-is-a-sequence)

_Closed Form Solution (for Sequences and Summations)_: A mathematical expression expressed using a finite number of standard operations, instead of an infinite summation/sequence.

_Finite sequence_: A sequence of numbers that eventually comes to an end.

_Infinite sequence_: A sequence of numbers that never comes to end (continues infinitely).

_Natural Root (e)_: It is the base of the natural logarithm, approximately equal to 2.71828.

### [Sets and Set Operations](https://www.codecademy.com/paths/computer-science/tracks/cspath-discrete-math/modules/sets-and-set-operations/lessons/sets-and-operations/exercises/introduction)

_Cardinality of a set_: It is the number of elements in the set. 

_Complement of a set_: The set of all elements in the universal set U that are not in this set.

_Dataset_: A collection of numbers or values that relate to a particular subject.

_Difference of two sets_: It is the set of all elements of the first set that are not present in the second.

_Domination Law for intersection_: Any set intersected with an empty set gives the empty set.

_Domination Law for union_: The union of any set with the Universal set is the Universal set.

_Identity Property for intersection_: The intersection of a set with the Universal set is the set itself.

_Identity Property for union_: The union of a set and the empty set is the set itself.

_Intersection of two sets_: It is the set containing all the elements that the two sets have in common.

_Null set_: A set with no elements, usually denoted by ∅ or by { }.

_SQL (Structured Query Language)_: A language used to communicate with a database. 

_Subset_: A set formed by taking parts of the original set.

_Union of two sets_: It is the set of all their elements together (without repeating any elements that they share).

_Universal set_: A set that contains all the elements of other sets (and its own elements), usually denoted by the symbol ‘U’.

_Venn diagram_: A visual representation of sets.
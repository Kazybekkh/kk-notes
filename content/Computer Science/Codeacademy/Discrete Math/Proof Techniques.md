
# Induction: Base Case

$$\sum_{i=1}^{n}{(2i-1)}=n^2$$
Steps:
1. Identify the *base case*
		1. For example: show $x\leq x^2$
		2. Since our chases are all of positive integers, our base case for this example is the smallest possible integer, which is 1 , $1=1^2$
		3. Therefore, we have proven the base case for this conjecture. 

# Induction: Induction Hypothesis

> The induction hypothesis supposes that our statement is true for some integer $k$, with the caveat that $k$ must exceed the number set as the base case.

# Induction: Proving the Inductive Step

Final task is to prove that our induction hypothesis is true for the integer $k+1$, where $k$ is the value we supposed in the induction hypothesis. For our example, we want to prove that:
$$\sum_{i=1}^{n+1}{(2i-1)}=(n+1)^2$$
1. Take a look at the sum and say that:
$$\sum_{i=1}^{n+1}(2i-1)=2(n+1)-1+n^2$$

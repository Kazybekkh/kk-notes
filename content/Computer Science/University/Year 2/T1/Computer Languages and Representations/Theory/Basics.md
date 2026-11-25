# Functional Programming

In **functional programming**, programs are represented by **pure functions**, and computation is implemented by **function application**

- Haskell
	- Tutorials point haskell compiler
	- Thinking functionally (mathematical fp book on haskell)

# Logic Programming

In **logic programming**, programming are represented by Horn clauses, and computation is **presented** by **resolution proofs**

Prolog
- M. Bramer, Logic Programming with Prolog
- Implementations
	- https://swish.swi-prolog.org
'

# Finite State Machines
In finite state machines, programs are represented by state machines, and computation is represented by by state transitions


# Boolean Types
The `Bool` type is that of **booleans**. There are just two values of this type, `True` or `False`

```hs
main
	= print (True && (False || True))
```


# Integer types
The `Int` type is that of **limited-precision integers**. The range of values of this type is at least as large as that of 29-bit signed binary integers
```
main
	= print (8 + 3 * 4)
```
# Characters
The `char` type is that of characters. As is increasingly common, a character can be any Unicode one.
```
main
	= print '+'
```

# Floats
The `float` type is that of single-precision floating point numbers. A floating-point number is one where the position of the decimal point depends on the number.
```
main
	= print (2 * pi * 4)
```

# Functions
A **function** transforms information received on its inputs to information transmitted on its output.
- Inputs are referred to as **arguments**
- outputs are referred to as **results**
The information on the inputs (only) determines the information on the outputs
- no concept of global state

# Program definitions
One possible definition of the `factorial` function uses **pattern matching**
```hs
factorial 1
	= 1
factorial n
	= n * factorial(n - 1)
```

Any argument must match the pattern for an equation to apply.
Any argument matches a variable pattern
## Program definitions (ctd)
Another possible definition of the `factorial` function uses **guards**
```hs
factorial n
	| n == 1 = 1
	| otherwise = n * factorial(n - 1)
```
A **guard** is a boolean expression that must be true for the equation to apply. The special final guard, `otherwise` is always true.

Exercise (fib) 

```hs
fibonacci Int :: Integer
fibonacci 0 = 1
fibonacci 1 = 1
fibonacci n = fibonacci(n-1) + fibonacci(n-2)
```

### other examples
```hs
square 
```

# Where definitions
A **where** definition allows one to name a value, and to use it in an expression.

```hs
prime :: Int -> Bool
prime n
	| n < 2 = False
	| otherwise = not (factorisable n 2)
	  where
	  factorisable n f
	  | n <= f = False
	  | otherwise = mod n f == 0
				  || factorisable n (f+1)	
```

Polynomial Expression example $x^{2}-8x+6$
```
roots :: (Float, Float, Float) -> (Float, Float)
roots (a, b, c) = (x1, x2) where
	x1 = e + sqrt d / (2 * a)
	x2 = e - sqrt d / (2 * a)
	d = b * b - 4 * a * c
	e = - b / (2 * a)
main = do
	putStrLn "The roots of our polynomial equation are:"
	print (roots(1, -8, 6))
```
## Let definitions

A **let** definition allows one to name a value, and to use it in an expression.
```hs
prime :: Int -> Bool
prime n
	| n < 2 = False
	| otherwise = 
		let
			factorisable n f
				| n <= f = False
				| otherwise = mod n f == 0
							|| factorisable n (f+1)
		in
			not (factorisable n 2)
```


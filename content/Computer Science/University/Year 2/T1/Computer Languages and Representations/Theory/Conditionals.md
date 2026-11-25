# Conditional Expressions

A conditional expression evaluates to one expression or the other, depending on the value of a boolean expression

```hs
ph :: Int -> String
ph x
	= if x < 7 then
		"acid"
	else if x > 7 then
		"alkaline"
	else
		"neutral"
```

- You must have an `else` clause, as opposed to python where you can just end with an `if`

# Case expressions
A case expression evaluates to the expression for a given case.
```hs
move :: Char -> (Int, Int) -> (Int, Int)
move c (x, y)
	= case c of
		'u' -> (x, y+1)
		'd' -> (x, y-1)
		'l' -> (x-1, y)
		'r' -> (x+1, y)
```

A case expressions. may have a default case


jijij
- E.g
	- Write a function that give the city where an airport is located
```
city :: String -> String
city s
	= case s of
		'ams' -> 'Amsterdam',
		'cdg' -> 'Paris',
		'fco' -> 'Rome',
		'gla' -> 'Flasgow',
		'lhr' -> 'London Heathrow',
		'vce' -> 'Venice',

```     wha


hhhihih

gugu


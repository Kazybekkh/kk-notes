The list type is that of a **sequence** of items of the **same** type

A list of integers would be `[Int]`

## List processing

List processing is naturally recursive. The result of a computation on a list is often most easily described in terms of its **head** (the first item) and a recursive computation on its **tail** (the rest of the items), until finally a base list is reached. 

## Example 1: Count

`[1, 2, 3, 4, 5]`
A count of the items in a list may be computed by adding one to the recursive count of the items in the tail of the list, until the list is empty and the result is zero.

```hs
count :: [Int] -> Int
count []
	= 0
count (x :: xs)
	= 1 + count xs
```
![[../../../../../../Screenshots/Screenshot 2025-11-01 at 1.28.34 AM.png]]

## Example 2: Keep
The result of keeping a number of items from a list is computed by prepending the head of the list onto the recursive result of keeping one fewer items from the tail of the list
```
keep :: Int -> [Int] -> [Int]
keep n []
	= []
keep n (x:xs)
	| n == 0 = []
	| otherwise = x : keep(n - 1) xs
```


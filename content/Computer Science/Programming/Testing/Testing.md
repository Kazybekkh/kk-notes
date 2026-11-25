# Unit Tests vs. Integration Tests

A unit test is a smallet test, one that checks that a single component operates in the right way. To ISOLATE what's broken in my application and fix it faster

Two types of tests
1. An integration test checks that components in your application operate with each other.
2. A unit test checks a small component in your application.

### E.g (Unit test)
```python
assert sum([1, 2, 3]) == 6, "should be 6"
```
Won't output anything on the REPL, cuz results correct
- If fail, throws `AssertionError` and the message `"should be 6"`. 

Instead of testing on the REPL, better to put this into a new Python file called `test_sum.py` and execute it again.

```python
def test_sum():
	assert sum([1, 2, 3]) == 6, "Should be 6"
	
if __name__ == "__main__":
	test_sum()
	print("Everything passed")
```
```Shell
$ python test_sum.py
Everything passed
```


## Choosing a Python Test Runner

- `unittest`  (built into the python standard library)
- `nose` or `nose 2`
- `pytest`
### unittest framework
- contains both a testing framework and a test runner.
- requirements for writing n exec tests:
	- put your tests into classes as methods
	- Use a series of special assertion methods in the `unittest`. `TestCase` class instead of the built-in `assert` statement.
- Earlier example:
```python
import unittest

class TestSum(unittest.TestCase):
	def test_sum(self): # success
		self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
	def test_sum_tuple(self):# fail
		self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
	
if __name__ == "__main__":
	unittest.main()
```

### nose framework
- can be used as a drop-in replacement for the `unittest` runner. But better to use `nose2` due to lack of open source dev of OG `nose`
```
pip install nose2
python -m nose2
.F
=================================================================
FAIL: test_sum_tuple (__main__.TestSum)
-----------------------------------------------------------------
Traceback (most recent call last):
  File "test_sum_unittest.py", line 9, in test_sum_tuple
    self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
AssertionError: Should be 6
-----------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```

Just executed the test created in `test_sum_unittest.py` from the `nose2` test runner.
- Offers many command line flags for filtering the tests that you execute, check the docs.

### pytest framework

`pytest` supports execution of `unittest` test cases. 
- Advantage: `pytest` test cases.
- `pytest` cases are a series of functions in a Python file starting with the name test_.
`pytest` has some great features:

- Support for in-built `assert()`
- Support for filtering for test cases
- Ability to re-run from the last failing test
- An ecosystem of hundreds of plugins to extend the functionality

`TestSum` case example for `pytest` would look like this:
```python
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"
```



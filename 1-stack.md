## What is a stack:
* Stacks are a data structure that are rather similar to lists and can be implemented using a python list.
* They are characterized by their "first in, last out, last in, first out" operational structure.
## When is it useful:
* This is useful when a queue needs to be made. Think of using the control + z command. This is a stack structure as it will undo the last action made.
* Most situations where an undo would be helpful.
## Operations:
1. push(_value_)
* adds the value to the back of the stack
``` python
stack.append(value)
```
* O(1) performance
2. pop
* This removes and returns the data at the back of the stack
``` python
holder = stack.pop()
```
* O(1) performance
3. size
* gives the size of the stack
```python
holder = len(stack)
```
* O(1) performance
4. empty
* returns True if there is no data in the stack
```python
if len(stack) == 0:
``` 
* O(1) performance

## Problem
### Scenario
* Your mother is making pancakes as you wait.
She puts some on the nearby plate and, in turn,
you take some.

* At some point you decide to count how many are on the plate.
After that, your mother stops cooking and takes some pancakes
for her self.
* You check to see if there are any more and find none.
### Problem to solve
## 1. Print the stack:
* finish the function to
print each item in the stack.

## 2. Remove from the stack:
* You need to remove from the back of the
stack as if you are popping a pancake off the
top of the stack.

## 3. Check the size:
* Finish the function for checking the length
of the stack.
* This will be the same as checking the length
of a list.

## 4. Check if empty:
* Finish the function for checking if the stack
is empty.
* Return True if the stack is empty
* Return False if not.
### Link to Problem:
[Problem](Problems/stack.py)
### Link to Solution:
[Solution](Solutions/stack_solution.py)
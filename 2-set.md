## What is a set?
* A set is essentially a type of unordered list that does not allow duplicates.
* The set does this through hashing the data that is put in and assigning it to a spot (index position) in the set.
* If something already has that spot, it will be placed in the same spot (effectively replacing it.)
## Times when sets are useful:
* When you need fast perfornmance when adding, removing or finding the presence of data.
* When you don't care about or want duplicates.
* When you don't care about the order the data is in. This is because the hashing of the data will be different each time the program is run and the position in the set is not based on the order the data was added.
## Basic Operations:
1. ___set___.add(_value_)
* This adds a value or data to the set.
* This is O(1) performance.
2. ___set___.remove(_value_)
* This removes a value or piece of data from the set.
* This is O(1) performance
3. if _value_ in ___set___: (also known as the ___member___ operation)
* This line of code is to check if a value or piece of data is in the set.
* This is O(1) performance.
4. length = len(___set___) (This is known as the ___length___ operation)



### Example:
```python
# show example of names using sets for uniqueness
names = set()
names.append("Geralt")
names.append("William")
names.append("Allan")

if "Geralt" not in names:
    names.append("Geralt")
else:
    print("Error! Name already exists!")
```
### Explanation:
* The three names are turned into a numerical value and assigned to an index position in the set.
* The check will turn the second instance of "Geralt" into a hash.
* That hash will be used to find to check the index position to see if there was something there.
* Because there is something at the position, the if-else statement will move to the else condition.
## Scenario:
* You and your D&D party are trying to solve a puzzle.

* The puzzle involves a series of numbers on four dials most of the numbers look the same, but there are a few differences.

* You reason that the numbers that don't appear on the other dials are the key to the puzzle.

* Your job is to find the differences between each of the four dials using sets.

## Problem to Solve:
### 1. Find the odd one out:
* Check each set against the three other sets.
* For each item that is not in the others,
put it in a set dedicated to those
numbers.
* Return the set so it can be viewed by you.

### link to problem:
[problem](Problems/set.py)
### link to solution:
[solution](Solutions/set_solution.py)
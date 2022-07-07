def single_out(set1,set2,set3,set4):
    """
    You need to check for an odd number out in each set. Return the numbers
    so that you can see what the solution to the puzzle is.
    """
    remaining = set()
    for i in set1:
        if i not in set2 and i not in set3 and i not in set4:
            remaining.add(i)
    for i in set2:
        if i not in set1 and i not in set3 and i not in set4:
            remaining.add(i)
    for i in set3:
        if i not in set2 and i not in set2 and i not in set4:
            remaining.add(i)
    for i in set4:
        if i not in set2 and i not in set3 and i not in set3:
            remaining.add(i)
    return remaining

dial1={1,2,4,5,6,8,9}
dial2={0,1,2,5,6,8,9}
dial3={1,2,5,6,7,8,9}
dial4={1,2,3,5,6,8,9}

print(single_out(dial1, dial2, dial3, dial4)) # should {0,3,4,7}
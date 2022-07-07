def single_out(set1,set2,set3,set4):
    """
    You need to check for an odd number out in each set. Return the discovered
    numbers so that you can see what the solution to the puzzle is.
    """
    pass

dial1={1,2,4,5,6,8,9}
dial2={0,1,2,5,6,8,9}
dial3={1,2,5,6,7,8,9}
dial4={1,2,3,5,6,8,9}

print(single_out(dial1, dial2, dial3, dial4)) # should {0,3,4,7}
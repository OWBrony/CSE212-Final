class stack():
    def __init__(self):
        self.pile = list()

    ###########################################
    # Problem 1                               #
    ###########################################

    def print_stack(self):
        pass

    ###########################################
    # End of Problem 1                        #
    ###########################################

    def pile_up(self, data):
        self.pile.append(data)

    ###########################################
    # Problem 2                               #
    ###########################################

    def undo(self):
        pass

    ###########################################
    # End of Problem 2                        #
    ###########################################

    ###########################################
    # Problem 3                               #
    ###########################################

    def give_size(self):
        pass

    ###########################################
    # End of Problem 3                        #
    ###########################################

    ###########################################
    # Problem 4                               #
    ###########################################
    def check_empty(self):
        pass

    ###########################################
    # End of Problem 4                        #
    ###########################################

pancakes = stack()

pancakes.pile_up(1)
pancakes.pile_up(2)
pancakes.pile_up(3)

print()
print("Problem 1")
print("--------------")

pancakes.print_stack() # should be 1 2 3

pancakes.undo()
pancakes.undo()

print()
print("Problem 2")
print("--------------")

pancakes.print_stack() # should 1

pancakes.pile_up(10)
pancakes.pile_up(20)

print()
print("Problem 3")
print("--------------")

print(pancakes.give_size()) # should be 3

pancakes.undo()
pancakes.undo()
pancakes.undo()

print()
print("Problem 4")
print("--------------")

print(pancakes.check_empty()) # should be True
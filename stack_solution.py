class stack():
    def __init__(self):
        self.first = list()
        # self.second = list()

    def pile_up(self, data):
        self.first.append(data)

    def undo(self):
        self.first.pop()

    def give_size(self):
        return len(self.first)

    def check_empty(self):
        if len(self.first) == 0:
            return True
        return False

    def print_stack(self):
        for i in self.first:
            print(i)

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
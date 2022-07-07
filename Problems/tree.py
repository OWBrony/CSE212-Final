class tree():
    class node():
        def __init__(self,key,name):
            self.left = None
            self.right = None
            self.key = key
            self.name = name
    
    def __init__(self):
        self.root = None

    def add_root(self,key,name):
        self.root = tree.node(key,name)

    def insert(self,name):
        key = hash(name)
        if self.root == None:
            self.add_root(key,name)
        else:
            self._insert(key, name, self.root)
    ###########################################
    # Problem 1                               #
    ###########################################

    def _insert(self,key,name,node):
        """Code the path the item and its key should
        take. If the the key is lower than the current
        node's key, it should go to the node's left branch.
        The opposite if the key is greater. Remember to assign
        the node so it has a place. Remember, This is so you can
        track your items later."""
        pass

    ###########################################
    # End of Problem 1                        #
    ###########################################

    def __iter__(self):
        """Do not touch this one"""
        yield from self._read_tree(self.root)

    ###########################################
    # Problem 2                               #
    ###########################################

    def _read_tree(self,node):
        """
        This is for reading off what is in the tree
        so far. This will be called from the __iter__
        function. Use the 'yield' and 'yield from'
        commands to get the code to span the entire
        tree and return the name of the items
        in your inventory.
        """
        pass

    ###########################################
    # End of Problem 2                        #
    ###########################################
    def __reversed__(self):
        """Do not touch this one"""
        yield from self._read_reverse_tree(self.root)

    ###########################################
    # Problem 3                               #
    ###########################################

    def _read_reverse_tree(self,node):
        """
        This is merely the reverse of _read_tree.
        Sometimes, if you have a large list, it can
        be hard to find what you are looking for.
        This will be called by the __reversed__ function.
        """
        pass

    ###########################################
    # End of Problem 3                        #
    ###########################################

    ###########################################
    # Problem 4                               #
    ###########################################

    def search_tree(self,key,node):
        """
        This will be for searching for whether
        or not a specific item is in your
        inventory. You need to check if a node has the
        key of your item and if it does it should report that.
        Otherwise, you will need to search the tree. Remember
        that there is no need to search a node that does not
        exist. This function will call itself until an answer
        is found. Once the search reaches the furthest it can go
        be sure that the answer is transfered all the way back up
        the function. Hint: there will be many if-else statements.  
        """
        pass
    ###########################################
    # End of Problem 4                        #
    ###########################################
# Order of results may vary
bag = tree()
bag.insert("sword")
bag.insert("flask")
bag.insert("flying_boots")

for x in bag:
    print(x) # should show flask, sword, flying_boots

print("--------------------")

bag.insert("shield")
bag.insert("ale")
bag.insert("plate_armor")
bag.insert("purse")

for x in reversed(bag):
    print(x)
    # should have flying_boots, purse, shield
    # plate_armor, flask, ale, sword

print("--------------------")

print(bag.search_tree(hash("water_bag"), bag.root)) # should return false
print(bag.search_tree(hash("shield"), bag.root)) # should return true
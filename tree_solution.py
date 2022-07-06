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

    def _insert(self,key,name,node):
        if key < node.key:
            if node.left is None:
                node.left = tree.node(key, name)
            else:
                if key != node.left.key:
                    self._insert(key, name, node.left)
        else:
            if node.right is None:
                node.right = tree.node(key, name)
            else:
                if key != node.right.key:
                    self._insert(key, name, node.right)
    
    def __iter__(self):
        """Do not touch this one"""
        yield from self._read_tree(self.root)

    def _read_tree(self,node):
        if node is not None:
            yield from self._read_tree(node.left)
            yield node.name
            yield from self._read_tree(node.right)

    def __reversed__(self):
        """Do not touch this one"""
        yield from self._read_reverse_tree(self.root)

    def _read_reverse_tree(self,node):
        if node is not None:
            yield from self._read_reverse_tree(node.right)
            yield node.name
            yield from self._read_reverse_tree(node.left)

    def search_tree(self,key,node):
        if key == node.key:
            return True
        elif key < node.key:
            if node.left is not None:
                if self.search_tree(name,node.left):
                    return True
                else:
                    return False
        elif key > node.key:
            if node.right is not None:
                if self.search_tree(key, node.right):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
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
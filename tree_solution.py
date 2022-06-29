class tree():
    class node():
        def __init__(self,key,name):
            self.left = None
            self.right = None
            self.key = None
            self.name = None
    
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
                    self._insert(key, name, node)
    
    def read_tree(self,node):
        if node is not None:
            yield from self.read_tree(node.left)
            yield node.name
            yield from self.read_tree(node.right)
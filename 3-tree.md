## What is a tree:
* A tree is similar to a linked list.
* The tree has a node which acts as the starting point of the entire data structure, this is called the root.
* A root can be linked to many different nodes, however this will be a tutorial for a binary tree so you will need to only worry about left or right nodes.
* Nodes that branch from the root can have their own sub-trees, meaning that they, themselves have nodes to the left or right branching off them.
* Nodes that do not branch further into other nodes are called leaves (these are the bottom of the tree).
* Trees are structures that use recursion in their functions.
## Times when trees are useful:
* Trees are incredibly useful when you need to search a large amount of data for some reason. This is because their search operation narrows down where the data is instead of searching the entire tree for it.
## Operations:
1. insert(_value_)
* to insert into tree
* O(log n) performance
2. remove(_value_)
* remove something from the tree
* O(log n) performance
3. contains(_value_)
* checks to see if the data is in the tree
* O(log n) performance
4. traverse_forward
* visits every node in the tree, least to greatest
* O(n), because it is using every node and the speed is more dependant on the size of the tree
5. reverse
* inverse of traverse_forward
* needs a "__ reverse __" iterator
* O(n) performance
6. height(_node_)
* figures out the height of the node, use the root for tree height
* O(n), recursively find the height of left and right subtrees and return height + 1(for root)
7. size
* give total size of the tree
* O(1) performance
8. empty
* return True if root is None
* O(1) performance

### Operations refernces:
### Adding example:
```python
class tree:
    class node:
        def __init__(self,data):
            self.left = None
            self.right = None
            self.data = None

    def __init__(self):
        self.root = None

    def add_node(self,data)
        if self.root == None:
            self.root = tree.node(data,self.root)
        else:
            self._add_node(data)
    
    def _add_node(self,data,node):
        if key < node.data:
            if node.left is None:
                node.left = tree.node(data)
            else:
                if data != node.left.data:
                    self._add_node(data,node.left)
        else:
            if node.right is None:
                node.right = tree.node(data)
            else:
                if data != node.right.data:
                    self._add_node(data,node.right)
```
### Explanation
* The tree needs a node class imbedded inside of it (this is mostly to keep the tree self-contained).
* The node has either a left or right that can be traveled down.
* The tree itself, upon startup, has no root, but it needs something so it is given "None."
* When the tree's "add_node" is called, the system will first check to see if the tree has a root. In this case it doesn't, so it calls a node with the data that is to be inputed and assigns the node to the root.
* Once the "add_node" function is called again, it will instead call the "_add_node" function. This function works with recursion, which means the function calls itself until a condition is satisfied (think of it as like a loop).
* The function will attach a new node on either the left or right side of the root.
### Traverse Example:
```python
def __iter__(self):
    yield from self._traverse_through(self.root)

def _traverse_through(self,node):
    if node is not None:
        yield from self._traverse_through(node.left)
        yield node.data
        yield from self._traverse_through(node.right)
```
### Explanation:
* The "iter" function here is critical. If you were to try to call the tree without this, you would get an error due to the tree not inherently having an iterator like lists do.
* The "iter" function will call another function that will handle the tree traversal.
* In "_traverse_through," which is a recursive function, the yield from for the left side will take the function as far as it will go.
* It will then yield (basically returning a value) the current node's data.
* The function will then do the same for the right side.
* The line "if node is not None" is there to ensure the function does not call itself infinitely.

## The Problem:
### Scenario:
* Throughout your travels in the realm you
have discovered many items of value to you.
However, you detirmine that it would be easier
let your computer handle your inventory instead
of writing it down.
* Your job is to finish constructing the tree structure
that will act as your inventory.

### 1. Finish the insert:
* Construct the _insert function so it puts
the new nodes on either the left or right of the
current node if the side does not already have one.
* If the node on the side the data goes on is filled,
then recall the function with the node that is in the direction
the data needs to go.
### 2. Implement the _read_tree function:
* Using the "yield" and "yield from" commands and recursion
to traverse through the tree to return the list.
* make sure to return the the current node's data before the
code goes back through itself.
### 3. Implement the _read_reverse_tree function:
* This is merely the opposite of the _read_tree
function.
* Implement the previous problem's solution in
reverse.
### 4. Implement search_tree function:
* This will be for searching for whether
or not a specific item is in your inventory.
* First check if the item's key matches the root.
* If not, check if the key is greater or less than
the root's key and use recursion to check the next
node.
* If the function makes it to the end of the tree and
still has not found the item, then have the function
return "false"
* If the Item is found have the function
return true back to itself.

### Link to Problem:
[Problem](Problems/tree.py)
### Link to Solution:
[solution](Solutions/tree_solution.py)
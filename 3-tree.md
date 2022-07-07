Throughout your travels in the realm you
have discovered many items of value to you.
However, you detirmine that it would be easier
let your computer handle your inventory instead
of writing it down.

Your job is to finish constructing the tree structure
that will act as your inventory.

## 1. Finish the insert:
* Construct the _insert function so it puts
the new nodes on either the left or right of the
current node if the side does not already have one.
* If the node on the side the data goes on is filled,
then recall the function with the node that is in the direction
the data needs to go.
## 2. Implement the _read_tree function:
* Using the "yield" and "yield from" commands and recursion
to traverse through the tree to return the list.
* make sure to return the the current node's data before the
code goes back through itself.
## 3. Implement the _read_reverse_tree function:
* This is merely the opposite of the _read_tree
function.
* Implement the previous problem's solution in
reverse.
## 4. Implement search_tree function:
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
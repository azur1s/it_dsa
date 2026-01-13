class BSTNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self) -> bool:
        return self.root is None

    def insert(self, data: int):
        if self.is_empty():
            self.root = BSTNode(data)
        else:
            def _insert(current_node: BSTNode, data: int):
                # If the data is less than current node
                if (data < current_node.data):
                    # Then check if the left branch is empty
                    if current_node.left is None:
                        # If so, set the left branch to this node
                        current_node.left = BSTNode(data)
                    else:
                        # Else, traverse that branch
                        _insert(current_node.left, data)
                else:
                    # Same for the right side
                    if current_node.right is None:
                        current_node.right = BSTNode(data)
                    else:
                        _insert(current_node.right, data)
            _insert(self.root, data)

    # Pre-order traversal is when you process the root node and then recursively
    # traverse the left node and then the right node
    def preorder(self):
        # Print current data, then traverse left & right
        def traverse(node: BSTNode):
            if node is not None:
                print("->", node.data, end=" ")
                traverse(node.left)
                traverse(node.right)
        traverse(self.root) # Start from root
        print() # Final newline

    # In-order traversal is when you process the left subtree first, then the
    # root node and then the right subtree
    def inorder(self):
        # Process left subtree, print current, then traverse right subtree
        def traverse(node: BSTNode):
            if node is not None:
                traverse(node.left)
                print("->", node.data, end=" ")
                traverse(node.right)
        traverse(self.root)
        print()

    # Post-order traversal is when you you process the left & right subtree
    # first, then the root node
    def postorder(self):
        def traverse(node: BSTNode):
            if node is not None:
                traverse(node.left)
                traverse(node.right)
                print("->", node.data, end=" ")
        traverse(self.root)
        print()

    def traverse(self):
        if not self.is_empty():
            print("Preorder: ", end="")
            self.preorder()
            print("Inorder: ", end="")
            self.inorder()
            print("Postorder: ", end="")
            self.postorder()
        else:
            print("This is an empty binary search tree.")

    # Find the minimum/smallest value in the tree
    def find_min(self) -> int:
        if self.is_empty():
            return None

        # Since the left node will always be smaller than the current node,
        # we can just get the leftmost node
        def traverse(node: BSTNode) -> int:
            if node.left is None:
                return node.data
            else:
                return traverse(node.left)

        return traverse(self.root)

    # Find the maximum/largest value in the tree
    def find_max(self) -> int:
        if self.is_empty():
            return None

        # Same as `find_min` but traverse for rightmost instead
        def traverse(node: BSTNode) -> int:
            if node.right is None:
                return node.data
            else:
                return traverse(node.right)

        return traverse(self.root)

    def find(self, node: BSTNode, target: int) -> BSTNode:
        # Base case: node is None or node's data matches target
        if node is None:
            return None
        if node.data == target:
            return node

        # If target is less than current node's data, search left subtree
        if target < node.data:
            return self.find(node.left, target)
        else:
            # Else, search right subtree
            return self.find(node.right, target)

    def delete(self, data: int):
        def _delete(node: BSTNode, data: int) -> BSTNode:
            if node is None:
                print("Delete Error, " + str(data) + " is not found in Binary Search Tree.")
                return node

            # Traverse the tree to find the node to delete
            if data < node.data:
                node.left = _delete(node.left, data)
            elif data > node.data:
                node.right = _delete(node.right, data)
            else:
                # Node with only one child or no child
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                # Node with two children: Get the inorder successor (smallest
                # in the right subtree)
                temp = self.find_min_node(node.right)

                # Copy the inorder successor's content to this node
                node.data = temp.data

                # Delete the inorder successor
                node.right = _delete(node.right, temp.data)

            return node

        # Start from root
        self.root = _delete(self.root, data)

def main():
  my_bst = BST()
  while 1:
    text = input()
    if text == "Done":
      break
    condition, data = text.split(": ")
    if condition == "I":
      my_bst.insert(int(data))
    elif condition == "D":
      my_bst.delete(int(data))
    else:
      print("Invalid Condition")
  my_bst.traverse()

main()
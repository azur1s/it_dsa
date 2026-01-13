class BSTNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data: int):
        if self.root is None:
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

    def preorder(self):
        # Print current data, then traverse left & right
        def traverse(node: BSTNode):
            if node is not None:
                print("->", node.data, end=" ")
                traverse(node.left)
                traverse(node.right)
        # Start from root
        traverse(self.root)
        print() # Final newline

def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))

  print("Preorder: ", end="")
  my_bst.preorder()

main()
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

def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()

main()
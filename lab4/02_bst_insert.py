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
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node: BSTNode, data: int):
        if data < node.data:
            if node.left is None:
                node.left = BSTNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = BSTNode(data)
            else:
                self._insert_recursive(node.right, data)

    def preorder(self):
        values = []

        def traverse(node: BSTNode):
            if node is not None:
                values.append(str(node.data))
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)
        print("-> " + " -> ".join(values))

def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))

  print("Preorder: ", end="")
  my_bst.preorder()

main()
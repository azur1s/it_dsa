class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert_last(self, data):
        new_node = DataNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.count += 1

    def traverse(self):
        if self.count == 0:
            print("This is an empty list.")
            return

        current = self.head
        for _ in range(self.count):
            if self.count - 1 == _:
                print(current.data)
            else:
                print(current.data, "->", end=' ')
            current = current.next

def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    mylist.insert_last(input())
  mylist.traverse()

main()

class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert_front(self, data):
        new_node = DataNode(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def insert_last(self, data):
        new_node = DataNode(data)
        # If the list is empty, insert at the head
        if not self.head:
            self.head = new_node
        # Else, traverse to the end and insert
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.count += 1

    def insert_before(self, target_data, new_data):
        new_node = DataNode(new_data)
        # If the list is empty, do nothing
        if not self.head:
            print("Cannot insert,", target_data, "does not exist.")
            return
        # If the target is at the head
        if self.head.data == target_data:
            self.insert_front(new_data)
            return
        # Traverse the list to find the target
        current = self.head
        while current.next and current.next.data != target_data:
            current = current.next
        # If the target is found, insert before it
        if current.next and current.next.data == target_data:
            new_node.next = current.next
            current.next = new_node
            self.count += 1
        else:
            print("Cannot insert,", target_data, "does not exist.")

    def delete(self, target_data):
        # If the list is empty, do nothing
        if not self.head:
            print("Cannot delete,", target_data, "does not exist.")
            return
        # If the target is at the head
        if self.head.data == target_data:
            self.head = self.head.next
            self.count -= 1
            return
        # Traverse the list to find the target
        current = self.head
        while current.next and current.next.data != target_data:
            current = current.next
        # If the target is found, delete it and update links
        if current.next and current.next.data == target_data:
            current.next = current.next.next
            self.count -= 1
        else:
            print("Cannot delete,", target_data, "does not exist.")

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

    def get(self, index):
        if index < 0 or index >= self.count:
            return "Error"
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

sl = SinglyLinkedList()
while True:
    x = input()
    if x == "Last":
        break
    sl.insert_last(x)

index = int(input())
print(sl.get(index - 1))

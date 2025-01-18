class Node:
        def __init__(self, data):
                self.data = data
                self.next = None
class Linkedlist:
        def __init__(self):
                self.head = None
        def append(self, data):
                new_node = Node(data)
                if self.head is None:
                        self.head = new_node
                else:
                        current = self.head
                        while current.next:
                                current = current.next
                        current.next = new_node
linked_list = Linkedlist()
linked_list.append(1)
print(linked_list)

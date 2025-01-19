class Node:
        def __init__(self, data):
                self.data = data
                self.next = None

        def get_value(self):
                return self.data
        
        def get_next_node(self):
                return self.next
        
        def set_next_node(self, next_node):
                self.next = next_node

class Linkedlist:
        def __init__(self, data=None):
                self.head = Node(data)

        def get_head_node(self):
                return self.head
        
        def insert_new_head(self, data):
                new_node = Node(data)
                new_node.set_next_node(self.head)
                self.head = new_node   
        
        def insert_tail_node(self, data):
                new_node = Node(data)
                if self.head is None:
                        self.head = new_node
                current = self.head
                while current.next:
                        current = current.next
                current.next = new_node
        
        def preview(self):
                preview = ""
                current = self.head
                while current:
                        if current.get_value() != None:
                                preview += str(current.get_value()) + "\n"
                        current = current.get_next_node()
                return preview
        
#correct output is 2 5 2

ii = Linkedlist(5)
ii.insert_new_head(2)
ii.insert_tail_node(2)
print(ii.preview())






        
                










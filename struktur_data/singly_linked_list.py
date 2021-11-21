class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = val

class SingleLinkedList:
    def __init__(self):
        self.linked_list_head = None

    def insert(self, new_node):
        if self.linked_list_head is None:
            self.linked_list_head = new_node
        else:
            temp = self.linked_list_head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    
    def insert_after(self, after_node_val, new_node):
        temp = self.linked_list_head
        while temp.val != after_node_val:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def print_linked_list(self):
        result = []
        temp = self.linked_list_head
        while temp is not None:
            result.append(temp.val)
            temp = temp.next
        print(result)


linked_list = SingleLinkedList()
linked_list.insert(Node(5))
linked_list.insert(Node(3))
linked_list.insert(Node(4))
linked_list.insert_after(3, Node(6))
linked_list.print_linked_list()

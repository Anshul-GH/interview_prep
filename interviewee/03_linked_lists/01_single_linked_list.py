class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def traverse_list(self):
        print_node = self.head
        while print_node is not None:
            print(print_node.value)
            print_node = print_node.next
    
    def add_node_begining(self, value):
        new_node = Node(value=value)
        new_node.next = self.head
        self.head = new_node


    def add_node_end(self, value):
        new_node = Node(value=value)
        last = self.head.next
        while last.next is not None:
            last = last.next
        
        last.next = new_node


singleLinkedList = SingleLinkedList()
node1 = Node(1)
node2 = Node(2)

singleLinkedList.head = node1
singleLinkedList.head.next = node2

print('Original List:')
singleLinkedList.traverse_list()
print('Appended List:')
print('At the begning:')
singleLinkedList.add_node_begining(0)
singleLinkedList.traverse_list()
print('At the end:')
singleLinkedList.add_node_end(3)
singleLinkedList.traverse_list()

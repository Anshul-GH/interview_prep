class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


singleLinkedList = SingleLinkedList()
node1 = Node(1)
node2 = Node(2)

singleLinkedList.head = node1
singleLinkedList.head.next = node2
singleLinkedList.tail = node2

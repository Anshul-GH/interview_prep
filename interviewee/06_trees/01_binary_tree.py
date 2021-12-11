class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

    def insert_node(self, data):
        if self.data:
            if data < self.data:
                if not self.left:
                    self.left = Node(data)
                else:
                    self.left.insert_node(data)
            elif data > self.data:
                if not self.right:
                    self.right = Node(data)
                else:
                    self.right.insert_node(data)
        else:
            self.data = data

    def traverse_tree(self):
        if self.left:
            self.left.traverse_tree()
        print(self.data)
        if self.right:
            self.right.traverse_tree()

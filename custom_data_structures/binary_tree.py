class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
            return
        if self.data == data:
            return
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def search(self, data):
        if self.data is None:
            print("Tree is empty")
        elif self.data == data:
            print("Node is found")
            return
        elif data < self.data:
            if self.left is None:
                print("Node is not present in tree")
            else:
                self.left.search(data)
        else:
            if self.right is None:
                print("Node is not present in tree")
            else:
                self.right.search(data)

    # node left right
    def preorder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    # left node right - ascending order
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=' ')
        if self.right:
            self.right.inorder()

    # left right node
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=' ')

    def min_node(self):
        curr = self
        while curr.left:
            curr = curr.left
        return f'\nNode with smallest data is : {curr.data}'

    def max_node(self):
        curr = self
        while curr.right:
            curr = curr.right
        return f'\nNode with biggest data is : {curr.data}'


def count(node):
    if node is None:
        return 0
    return 1 + count(node.left) + count(node.right)


root = Node()
list1 = [20, 2, 30, 40, 5, 12, 8, 25, 50, 45, 47, 100]
for i in list1:
    root.insert(i)
root.search(100)
print("Pre-order")
root.preorder()
print("\nIn-order")
root.inorder()
print("\nPost-order")
root.postorder()
# print(f'\nTotal nodes : {count(root)}')
# root.inorder()
# print(root.min_node())
# print(root.max_node())

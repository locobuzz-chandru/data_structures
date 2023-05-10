class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            return "Linked list is empty"
        else:
            node = self.head
            list_ = []
            while node:
                list_.append(node.data)
                node = node.next
            return list_

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node

    def insert_at_index(self, index, data):
        new_node = Node(data)
        node = self.head
        for i in range(index - 1):
            node = node.next
        new_node.next = node.next
        node.next = new_node

    def reverse(self):
        prev = None
        node = self.head
        while node is not None:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        self.head = prev

    def delete_at_head(self):
        node = self.head
        self.head = node.next
        node.next = None

    def delete_at_tail(self):
        node = self.head.next
        prev = self.head
        while node.next is not None:
            node = node.next
            prev = prev.next
        prev.next = None

    def delete_at_index(self, index):
        node = self.head.next
        prev = self.head
        for i in range(index - 1):
            node = node.next
            prev = prev.next
        prev.next = node.next
        node.next = None


if __name__ == '__main__':
    L = SingleLinkedList()
    print(L.display())
    L.insert_at_head(20)
    L.insert_at_tail(30)
    L.insert_at_tail(40)
    L.insert_at_tail(60)
    L.insert_at_head(10)
    L.insert_at_index(4, 50)
    print(L.display())
    L.reverse()
    print(L.display())
    # L.delete_at_head()
    # print(L.display())
    # L.delete_at_tail()
    # print(L.display())
    # L.delete_at_index(2)
    # print(L.display())

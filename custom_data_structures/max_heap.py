class MaxHeap:
    def __init__(self):
        self.heap = []

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left_child(i):
        return 2 * i + 1

    @staticmethod
    def right_child(i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None
        self.swap(0, len(self.heap) - 1)
        max_item = self.heap.pop()
        self.heapify_down(0)
        return max_item

    def is_empty(self):
        return len(self.heap) == 0

    def heapify_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify_down(self, i):
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.swap(i, largest)
            self.heapify_down(largest)


if __name__ == '__main__':
    heap = MaxHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    heap.insert(2)

    while not heap.is_empty():
        print(heap.extract_max())

# QUEUE is a user-defined data structure in python that is used to store data in the First In First Out (FIFO) manner.
# In queues, the insertion and deletion are done at different ends, where the insertion is done at the rear end and the
# deletion is done at the front end. So, the data which is inserted first will be removed from the queue first.
# Since the first element inserted is served and removed first, the queue data structures in python are also known as
# the First Come First Served data structure.
import queue


def queue_function1():
    queue_ = []
    for x in range(1, 6):
        queue_.append(x)
    for x in range(len(queue_)):
        queue_.pop(0)
    return queue_


def queue_function2():
    import collections
    queue_ = collections.deque()
    for x in range(1, 6):
        queue_.appendleft(x)
    for x in range(len(queue_)):
        queue_.pop()
    return queue_


def queue_function3():
    queue_ = queue.Queue()
    for x in range(1, 6):
        queue_.put(x)
    for x in range(5):
        queue_.get()
    return queue_


def priority_queue():
    queue_ = queue.PriorityQueue()
    queue_.put(10)
    queue_.put(30)
    queue_.put(20)
    for x in range(3):
        queue_.get()
    return queue_


if __name__ == '__main__':
    queue_function1()
    queue_function2()
    queue_function3()
    priority_queue()

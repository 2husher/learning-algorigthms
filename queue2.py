from dllists import *

class Queue:
    def __init__(self):
        self.queue = DoubleLinkedList()

    def enqueue(self, value):
        self.queue.shift(value)

    def dequeue(self):
        return self.queue.pop()

    def first(self):
        return self.queue.first()

    def last(self):
        return self.queue.last()

    def count(self):
        return self.queue.count()

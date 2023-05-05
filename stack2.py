from sllists import *

class Stack:

    def __init__(self):
        self.stack = SingleLinkedList()

    def push(self, value):
        self.stack.shift(value)

    def pop(self):
        return self.stack.unshift()

    def top(self):
        return self.stack.first()

    def count(self):
        return self.stack.count()

    def dump(self, msg):
        self.stack.dump(msg)

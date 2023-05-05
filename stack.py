class StackNode:

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

class Stack:

    def __init__(self):
        self.begin = None

    def push(self, value):
        node = StackNode(value, None)
        node.next = self.begin
        self.begin = node

    def pop(self):
        if self.begin == None:
            return None
        else:
            top = self.begin
            self.begin = self.begin.next
            return top.value

    def top(self):
        if self.begin == None:
            return None
        else:
            return self.begin.value

    def count(self):
        size = 0
        ref = self.begin
        while ref != None:
            ref = ref.next
            size += 1
        return size
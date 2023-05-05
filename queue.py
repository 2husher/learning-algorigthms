class QueueNode:
    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

class Queue:
    def __init__(self):
        self.begin = None
        self.end = None

    def enqueue(self, value):
        node = QueueNode(value, None, None)
        if self.begin == None:
            self.begin = node
            self.end = node
        else:
            node.next = self.begin
            self.begin.prev = node
            self.begin = node

    def dequeue(self):
        if self.end == None:
            return None
        elif self.begin == self.end:
            last = self.end
            self.begin = None
            self.end = None
            return last.value
        else:
            last = self.end
            self.end = self.end.prev
            self.end.next = None
            return last.value

    def first(self):
        if self.begin == None:
            return None
        else:
            return self.begin.value


    def last(self):
        if self.end == None:
            return None
        else:
            return self.end.value

    def count(self):
        ref = self.begin
        size = 0
        while ref != None:
            size += 1
            ref = ref.next
        return size
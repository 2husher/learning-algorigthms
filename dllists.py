class DoubleLinkedListNode:

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

class DoubleLinkedList:

    def _invariants(self):
        if self.count() == 0:
            assert self.begin == None and self.end == None
        if self.count() == 1:
            assert self.begin == self.end
        if self.begin != None:
            assert self.begin.prev == None
        if self.end != None:
            assert self.end.next == None

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        self._invariants()
        node = DoubleLinkedListNode(obj, None, None)
        if self.begin == None:
            self.begin = node
            self.end = node
        else:    
            self.end.next = node
            node.prev = self.end
            self.end = node
        self._invariants()

    def pop(self):
        self._invariants()
        if self.begin == None:
            self._invariants()
            return None
        elif self.begin == self.end:
            last = self.begin
            self.begin = None
            self.end = None
            self._invariants()
            return last.value
        else:
            last = self.end
            self.end = last.prev
            self.end.next = None
            self._invariants()
            return last.value

    def shift(self, obj):
        self._invariants()
        node = DoubleLinkedListNode(obj, None, None)
        if self.begin == None:
            self.begin = node
            self.end = node
        else:
            node.next = self.begin
            self.begin.prev = node
            self.begin = node
        self._invariants()

    def unshift(self):
        self._invariants()
        if self.begin == None:
            self._invariants()
            return None
        elif self.begin == self.end:
            first = self.begin
            self.begin = None
            self.end = None
            self._invariants()
            return first.value
        else:
            first = self.begin
            self.begin = self.begin.next
            self.begin.prev = None
            self._invariants()
            return first.value

    def detach_node(self, node):
        self._invariants()
        if self.begin == None:
            return
        if node == self.begin and self.begin == self.end: 
            self.begin = None
            self.end = None
        elif node == self.begin:
            self.begin = self.begin.next
            self.begin.prev = None
        elif node == self.end:
            self.end = self.end.prev
            self.end.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self._invariants()

    def remove(self, obj):
        self._invariants()
        ref = self.begin
        index = 0
        while ref != None:
            if ref.value == obj:
                self.detach_node(ref)
                self._invariants()
                return index
            ref = ref.next
            index += 1
        self._invariants()

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
        _count = 0
        while ref != None:
            ref = ref.next
            _count += 1
        return _count

    def get(self, index):
        ref = self.begin
        idx = 0
        while ref != None:
            if index == idx:
                return ref.value
            idx += 1
            ref = ref.next
        return None

    def dump(self, mark):
        ref = self.begin
        print(mark, "BEGIN", end = " ")
        while ref != None:
            print(ref.value, end = " ")
            ref = ref.next
        print("END")

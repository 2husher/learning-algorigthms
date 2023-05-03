class SingleLinkedListNode:

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class SingleLinkedList:
     
    def __init__(self):
        self.begin = None

    def push(self, obj):
        node = SingleLinkedListNode(obj, None)
        if self.begin == None:
            self.begin = node
            return
    
        ref = self.begin
        while ref.next != None:
            ref = ref.next
        ref.next = node

    def pop(self):
        if self.begin == None:
            return None

        if self.begin.next == None:
            last = self.begin
            self.begin = None
            return last.value
    
        prev = self.begin
        ref = self.begin.next
        while ref.next != None:
            ref = ref.next
            prev = prev.next
        prev.next = None
        return ref.value

    def shift(self, obj):
        node = SingleLinkedListNode(obj, None)
        
        if self.begin == None:
            self.begin = node
            return
    
        first = self.begin
        node.next = first
        self.begin = node

    def unshift(self):
        if self.begin == None:
            return None

        if self.begin.next == None:
            first = self.begin
            self.begin = None
            return first.value
    
        first = self.begin
        self.begin = first.next
        return first.value
    
    def remove(self, obj):
        if self.begin == None:
            return None

        if self.begin.value == obj:
            if self.begin.next == None:
                self.begin = None
                return 0
            else:
                self.begin = self.begin.next
                return 0
        
        ref = self.begin.next
        prev = self.begin
        index = 1
        while ref != None:
            if ref.value == obj:
                prev.next = ref.next
                return index
            else:
                prev = ref
                ref = ref.next
                index += 1
        return None

    def first(self):
        if self.begin == None:
            return None
        
        return self.begin.value

    def last(self):
        if self.begin == None:
            return None

        ref = self.begin
        while ref.next != None:
            ref = ref.next
        return ref.value

    def count(self):
        elems_count = 0
        pos = self.begin
        while pos != None:
            pos = pos.next
            elems_count += 1
        return elems_count
        
    def get(self, index):
        idx = 0 
        ref = self.begin
        while ref != None:
            if idx == index:
                return ref.value
            idx += 1
            ref = ref.next
        return None

    def dump(self, msg):
        print(f"DEBUG # {msg}", end = ": ")
        ref = self.begin
        while ref != None:
            print(ref.value, end = " ")
            ref = ref.next
        print("# GEDUB")

def main():
    sllist = SingleLinkedListNode(1, None)
    sllist.next = SingleLinkedListNode(2, None)
    sllist.next.next = SingleLinkedListNode(3, None)
    sllist.next.next.next = SingleLinkedListNode(4, None)
    sllist.next.next.next.next = SingleLinkedListNode(5, None)
    
    pos = sllist
    while pos != None:
        print(pos.value, end = " ")
        pos = pos.next  
    print()
main()


        
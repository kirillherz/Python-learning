class Node:
    
    def __init__(self, data, next):
        self.data = data
        self.next = next

class List:
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def add(self, data):
        newNode = Node(data, None)
        if self._size == 0:
            self._head = newNode
            self._tail = newNode
        else:
            self._tail.next = newNode
            self._tail = newNode
        self._size += 1


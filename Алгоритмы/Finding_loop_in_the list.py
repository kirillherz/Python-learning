class Node:
    
    def __init__(self, data, next):
        self.data = data
        self.next = next

class List:
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    

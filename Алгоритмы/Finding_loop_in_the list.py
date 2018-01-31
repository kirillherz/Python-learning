class Node:
    
    def __init__(self, data, next):
        self.data = data
        self.next = next

class List:
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        self._nextHead = None
    
    def add(self, data):
        newNode = Node(data, None)
        if self._size == 0:
            self._nextHead = newNode
            self._head = newNode
            self._tail = newNode
        else:
            self._tail.next = newNode
            self._tail = newNode
        self._size += 1

    def findNode(self, searchIndex):
        currentIndex = 0
        node = self._head
        prevNode = None
        while currentIndex != searchIndex:
            prevNode = node
            node = node.next
            currentIndex += 1
        return node

    def addLoop(self, index, data):
        self._tail =  Node(data, self.findNode(index))    def next(self):
        newNode =  Node(data, self.findNode(index))
        self._tail.next = newNode
        self._tail = newNode

    def next(self):
        data = self._nextHead.data
        self._nextHead = self._nextHead.next
        return data

    def FindLoop(self):
        slow = self._head.next
        fast=  self._head.next.next
        isLoop = True
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
            if (slow == None) or (fast == None):
                isLoop = False
                break
        index = None
        if isLoop:
            index = 0
            slow = self._head
            while slow != fast:
                slow = slow.next
                fast = fast.next
                index += 1
        return index

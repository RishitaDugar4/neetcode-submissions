class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        newNode = Node(value)
        lastNode = self.tail.prev

        lastNode.next = newNode
        newNode.prev = lastNode
        newNode.next = self.tail
        self.tail.prev = newNode

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        firstNode = self.head.next
        firstNode.prev = newNode
        newNode.next = firstNode

        self.head.next = newNode
        newNode.prev = self.head

    def pop(self) -> int:
        if self.isEmpty(): return -1
            
        lastNode = self.tail.prev
        val = lastNode.val
        lastNode.prev.next = self.tail
        self.tail.prev = lastNode.prev

        return val

    def popleft(self) -> int:
        if self.isEmpty(): return -1

        firstNode = self.head.next
        val = firstNode.val
        self.head.next = firstNode.next
        firstNode.next.prev = self.head

        return val

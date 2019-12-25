# title: design-circular-deque
# detail: https://leetcode.com/submissions/detail/287744065/
# datetime: Sun Dec 22 20:39:30 2019
# runtime: 88 ms
# memory: 13 MB

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = k
        self.length = 0
        self.queue = [None] * self.size
        self.head = 0
        self.tail = 0
        
    def _reset(self):
        self.head = 0
        self.tail = 0
        
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 1
            self.tail = 0
        self.head = (self.head - 1) % self.size
        self.queue[self.head] = value
        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
            self.tail = -1
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        self.length += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        val = self.queue[self.head]
        self.head = (self.head + 1) % self.size
        self.length -= 1
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        val = self.queue[self.tail]
        self.tail = (self.tail - 1) % self.size
        self.length -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.tail]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.length == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.length == self.size

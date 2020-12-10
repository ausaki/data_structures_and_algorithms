# title: design-front-middle-back-queue
# detail: https://leetcode.com/submissions/detail/425013655/
# datetime: Sat Nov 28 23:51:20 2020
# runtime: 88 ms
# memory: 15.1 MB

class Node:
    def __init__(self, val=-1, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class FrontMiddleBackQueue:

    def __init__(self):
        self.head = Node()
        self.head.next = self.head.prev = self.head
        self.mid = self.head
        self.n = 0
    
    def pushFront(self, val: int) -> None:
        node = Node(val, self.head.next, self.head)
        self.head.next = node
        node.next.prev = node
        if self.n == 0:
            self.mid = node
        elif self.n % 2:
            self.mid = self.mid.prev
        self.n += 1

    def pushMiddle(self, val: int) -> None:
        if self.n % 2 == 0:
            self.mid = self.mid.next
        node = Node(val, self.mid, self.mid.prev)
        node.prev.next = node
        self.mid.prev = node
        self.mid = self.mid.prev
        self.n += 1
        
        
    def pushBack(self, val: int) -> None:
        node = Node(val, self.head, self.head.prev)
        node.prev.next = node
        self.head.prev = node
        if self.n == 0:
            self.mid = node
        elif self.n % 2 == 0:
            self.mid = self.mid.next
        self.n += 1        
        
        
    def popFront(self) -> int:
        if self.n == 0:
            return -1
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        if self.n % 2 == 0:
            self.mid = self.mid.next
        self.n -= 1
        return node.val

    def popMiddle(self) -> int:
        if self.n == 0:
            return -1
        node = self.mid
        node.prev.next = node.next
        node.next.prev = node.prev
        if self.n % 2:
            self.mid = self.mid.prev
        else:
            self.mid = self.mid.next
        self.n -= 1
        return node.val

    def popBack(self) -> int:
        if self.n == 0:
            return -1
        node = self.head.prev
        self.head.prev = node.prev
        node.prev.next = self.head
        if self.n % 2:
            self.mid = self.mid.prev
        self.n -= 1
        return node.val
    
    def __str__(self):
        curr = self.head.next
        s = []
        while curr is not self.head:
            s.append(str(curr.val))
            curr = curr.next
        return ' -> '.join(s)
# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
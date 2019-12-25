# title: implement-queue-using-stacks
# detail: https://leetcode.com/submissions/detail/194336143/
# datetime: Mon Dec 10 14:59:15 2018
# runtime: 20 ms
# memory: 7 MB

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.front = None
        
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if len(self.stack1) == 0:
            self.front = x
        self.stack1.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack2) == 0:
            size = len(self.stack1)
            while size:
                self.stack2.append(self.stack1.pop())
                size -= 1
        v = self.stack2.pop()
        return v
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack2) == 0:
            size = len(self.stack1)
            while size:
                self.stack2.append(self.stack1.pop())
                size -= 1
        return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack1) + len(self.stack2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
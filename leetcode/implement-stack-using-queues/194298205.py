# title: implement-stack-using-queues
# detail: https://leetcode.com/submissions/detail/194298205/
# datetime: Mon Dec 10 11:25:07 2018
# runtime: 20 ms
# memory: 7 MB

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        size = len(self.queue)
        while size > 1:
            v = self.queue.pop(0)
            self.queue.append(v)
            size -= 1
        return self.queue.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        size = len(self.queue)
        while size > 0:
            v = self.queue.pop(0)
            self.queue.append(v)
            size -= 1
        return v
    
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
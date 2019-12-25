# title: implement-stack-using-queues
# detail: https://leetcode.com/submissions/detail/194302533/
# datetime: Mon Dec 10 11:47:27 2018
# runtime: 28 ms
# memory: 7 MB

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self._top = None

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        self._top = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        size = len(self.queue)
        while size > 1:
            self._top = self.queue.pop(0)
            self.queue.append(self._top)
            size -= 1
        return self.queue.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._top
    
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
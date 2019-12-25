# title: peeking-iterator
# detail: https://leetcode.com/submissions/detail/284769404/
# datetime: Mon Dec  9 17:51:53 2019
# runtime: 24 ms
# memory: 12.9 MB

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
from collections import deque
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._it = iterator
        self.buffer = deque()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.buffer and self._it.hasNext():
            self.buffer.append(self._it.next())
        return self.buffer[0] if self.buffer else None
        

    def next(self):
        """
        :rtype: int
        """
        if self.buffer:
            return self.buffer.popleft()
        return self._it.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.buffer) or self._it.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
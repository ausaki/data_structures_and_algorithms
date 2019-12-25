# title: peeking-iterator
# detail: https://leetcode.com/submissions/detail/284769987/
# datetime: Mon Dec  9 17:57:09 2019
# runtime: 32 ms
# memory: 12.8 MB

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
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._it = iterator
        self.holder = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.holder and self._it.hasNext():
            self.holder = self._it.next()
        return self.holder
        

    def next(self):
        """
        :rtype: int
        """
        if self.holder:
            n = self.holder
            self.holder = None
            return n
        return self._it.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.holder) or self._it.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
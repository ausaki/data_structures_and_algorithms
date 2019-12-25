# title: flatten-nested-list-iterator
# detail: https://leetcode.com/submissions/detail/284987144/
# datetime: Tue Dec 10 16:14:59 2019
# runtime: 92 ms
# memory: 16.4 MB

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nested_list = nestedList
        self.stack = []
        self.curr_list = nestedList
        self.index = 0
    
    def _next(self):
        if self.index >= len(self.curr_list):
            if self.stack:
                self.curr_list, self.index = self.stack.pop()
                return self._next()
            return -1
        ele = self.curr_list[self.index]
        if ele.isInteger():
            return self.index
        self.stack.append((self.curr_list, self.index + 1))
        self.curr_list = ele.getList()
        self.index = 0
        return self._next()
    
    def next(self) -> int:
        i = self._next()
        if i >= 0:
            self.index += 1
            return self.curr_list[i]
        return -1
    
    def hasNext(self) -> bool:
        return self._next() >= 0
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
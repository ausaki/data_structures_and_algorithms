# title: flatten-nested-list-iterator
# detail: https://leetcode.com/submissions/detail/284989451/
# datetime: Tue Dec 10 16:29:43 2019
# runtime: 84 ms
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
        self.stack = [[nestedList, 0]]
    
    def next(self) -> int:
        if self.hasNext():
            lst, i = self.stack[-1]
            v = lst[i]
            self.stack[-1][1] += 1
            return v
    
    def hasNext(self) -> bool:
        while self.stack:
            lst, i = self.stack[-1]
            if i >= len(lst):
                self.stack.pop()
            else:
                ele = lst[i]
                if ele.isInteger():
                    return True
                self.stack[-1][1] += 1
                self.stack.append([ele.getList(), 0])
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
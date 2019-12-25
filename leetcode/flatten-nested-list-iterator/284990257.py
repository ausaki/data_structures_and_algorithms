# title: flatten-nested-list-iterator
# detail: https://leetcode.com/submissions/detail/284990257/
# datetime: Tue Dec 10 16:34:57 2019
# runtime: 100 ms
# memory: 16.2 MB

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
        self.elems = []
        self.flat(nestedList)
        self.index = -1
        
    def flat(self, nestedlist):
        for elem in nestedlist:
            if elem.isInteger():
                self.elems.append(elem)
            else:
                self.flat(elem.getList())
        
    def next(self) -> int:
        self.index += 1
        return self.elems[self.index]
    
    def hasNext(self) -> bool:
        return self.index + 1 < len(self.elems)
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
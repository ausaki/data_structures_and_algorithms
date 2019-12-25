# title: mini-parser
# detail: https://leetcode.com/submissions/detail/282915805/
# datetime: Sun Dec  1 17:40:16 2019
# runtime: 76 ms
# memory: 16.2 MB

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        self.s = s
        self.end = len(s)
        # return self._parse()
        return self._parse2()
    
    def _parse_int(self, i):
        obj = NestedInteger()
        j = i + 1
        while j < self.end and self.s[j].isdigit():
            j += 1
        obj.setInteger(int(self.s[i:j]))
        return j - 1, obj
    
    def _parse_list(self, i):
        obj = NestedInteger()
        i += 1
        while i < self.end:
            char = self.s[i]
            if char == ',':
                i += 1
            elif char == '[':
                j, lst = self._parse_list(i)
                obj.add(lst)
                i = j + 1
            elif char == ']':
                break
            else:
                j, integer = self._parse_int(i)
                obj.add(integer)
                i = j + 1
        return i, obj
    
    def _parse(self):
        if self.end == 0:
            return NestedInteger()
        char = self.s[0]
        if char == '[':
            i, obj = self._parse_list(0)
            return obj
        i, obj = self._parse_int(0)
        return obj
    
    def _parse2(self):
        stack = []
        i = 0
        while i < self.end:
            char = self.s[i]
            if char == ',':
                i += 1
            elif char == ']':
                tmp = []
                while stack and stack[-1] != '[':
                    tmp.append(stack.pop())
                stack.pop()
                obj = stack.pop()
                while tmp:
                    obj.add(tmp.pop())
                stack.append(obj)
                i += 1
            elif char == '[':
                obj = NestedInteger()
                stack.append(obj)
                stack.append('[')
                i += 1
            else:
                obj = NestedInteger()
                j = i + 1
                while j < self.end and self.s[j].isdigit():
                    j += 1
                obj.setInteger(int(self.s[i:j]))
                stack.append(obj)
                i = j
        return stack.pop()
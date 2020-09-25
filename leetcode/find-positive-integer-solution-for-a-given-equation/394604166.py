# title: find-positive-integer-solution-for-a-given-equation
# detail: https://leetcode.com/submissions/detail/394604166/
# datetime: Sat Sep 12 21:34:57 2020
# runtime: 28 ms
# memory: 13.8 MB

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        class Row:
            def __init__(self, row, length):
                self.row = row
                self.length = length
            def __getitem__(self, i):
                return customfunction.f(self.row, i + 1)
            def __len__(self):
                return self.length

        m= 1000
        result = []
        j = 1000
        for i in range(1, m + 1):
            row = Row(i, j)
            j = bisect.bisect_left(row, z)
            if j < len(row) and row[j] == z:
                result.append([i, j + 1])
            if j == 0:
                break
        return result
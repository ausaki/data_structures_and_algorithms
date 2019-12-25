# title: triangle
# detail: https://leetcode.com/submissions/detail/148134170/
# datetime: Mon Apr  2 17:42:23 2018
# runtime: 68 ms
# memory: N/A

class Solution(object):
    def minimumTotal_(self, triangle, row, col):
        if row == len(triangle) - 1:
            return triangle[row][col]
        if row in self.cache and col in self.cache[row]:
            return self.cache[row][col]
        
        m = min(self.minimumTotal_(triangle, row + 1, col),
                self.minimumTotal_(triangle, row + 1, col + 1))
        m += triangle[row][col]
        c = self.cache.setdefault(row, {})
        c[col] = m
        return m
    
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.cache = {}
        return self.minimumTotal_(triangle, 0, 0)
        
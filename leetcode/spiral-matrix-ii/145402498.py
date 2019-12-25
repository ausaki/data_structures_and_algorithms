# title: spiral-matrix-ii
# detail: https://leetcode.com/submissions/detail/145402498/
# datetime: Fri Mar 16 16:19:14 2018
# runtime: 37 ms
# memory: N/A

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        num = 1
        px = 0
        py = 0
        
        matrix = [[None for i in range(n)] for i in range(n)]
        
        while n > 0:
            l, t, r, b = py, px, py + n - 1, px + n - 1
            for y in range(l, r + 1):
                matrix[t][y] = num
                num += 1
            for x in range(t + 1, b + 1):
                matrix[x][r] = num
                num += 1
            for y in range(r - 1, l - 1, -1):
                matrix[b][y] = num
                num += 1
            for x in range(b - 1, t, -1):
                matrix[x][l] = num
                num += 1
            px += 1
            py += 1
            n -= 2
            
        return matrix
        
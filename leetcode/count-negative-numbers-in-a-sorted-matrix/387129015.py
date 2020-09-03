# title: count-negative-numbers-in-a-sorted-matrix
# detail: https://leetcode.com/submissions/detail/387129015/
# datetime: Thu Aug 27 22:15:15 2020
# runtime: 116 ms
# memory: 14.7 MB

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        m = len(grid)
        n = len(grid[0])
        j = n - 1
        for i in range(m):
            for k in range(j, -1, -1):
                if grid[i][k] >= 0:
                    break
            if k == 0 and grid[i][k] < 0:
                k -= 1
            result += (m - i) * (j - k)
            if k == -1:
                break
            j = k
        return result
            
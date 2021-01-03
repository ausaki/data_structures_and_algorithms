# title: where-will-the-ball-fall
# detail: https://leetcode.com/submissions/detail/434989104/
# datetime: Sun Dec 27 11:13:32 2020
# runtime: 356 ms
# memory: 14.6 MB

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def fall(col):
            i, j = 0, col
            while i < m:
                if grid[i][j] == 1:
                    if j == n - 1 or grid[i][j + 1] == -1:
                        return -1
                    i += 1
                    j += 1
                else:
                    if j == 0 or grid[i][j - 1] == 1:
                        return -1
                    i += 1
                    j -= 1
            return j
        
        m, n = len(grid), len(grid[0])
        res = [-1] * n
        return [fall(i) for i in range(n)]
            
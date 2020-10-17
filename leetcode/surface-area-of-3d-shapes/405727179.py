# title: surface-area-of-3d-shapes
# detail: https://leetcode.com/submissions/detail/405727179/
# datetime: Wed Oct  7 22:48:54 2020
# runtime: 84 ms
# memory: 14.2 MB

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        s = 0
        for i in range(m):
            for j in range(m):
                v = grid[i][j]
                if not v:
                    continue
                s += 6 + (v - 1) * 4
                if i:
                    s -= 2 * min(grid[i - 1][j], v) 
                if j:
                    s -= 2 * min(grid[i][j - 1], v)
        return s
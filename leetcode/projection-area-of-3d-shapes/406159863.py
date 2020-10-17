# title: projection-area-of-3d-shapes
# detail: https://leetcode.com/submissions/detail/406159863/
# datetime: Thu Oct  8 22:13:18 2020
# runtime: 68 ms
# memory: 14.2 MB

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        result = 0
        m = len(grid)
        for i in range(m):
            row_max = 0
            for j in range(m):
                if grid[i][j]:
                    result += 1
                row_max = max(row_max, grid[i][j])
                grid[i][j] = max(grid[i][j], grid[i - 1][j] if i else 0)
            result += row_max
        result += sum(grid[m - 1])
        return result
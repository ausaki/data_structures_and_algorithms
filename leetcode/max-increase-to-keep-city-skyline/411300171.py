# title: max-increase-to-keep-city-skyline
# detail: https://leetcode.com/submissions/detail/411300171/
# datetime: Wed Oct 21 11:35:48 2020
# runtime: 76 ms
# memory: 14.3 MB

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row = [0] * n
        col = [0] * n
        for i in range(n):
            for j in range(n):
                row[i] = max(row[i], grid[i][j])
                col[j] = max(col[j], grid[i][j])
        inc = 0
        for i in range(n):
            for j in range(n):
                inc += min(row[i], col[j]) - grid[i][j]
        return inc
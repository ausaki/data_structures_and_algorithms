# title: count-servers-that-communicate
# detail: https://leetcode.com/submissions/detail/394039523/
# datetime: Fri Sep 11 12:25:28 2020
# runtime: 560 ms
# memory: 15.2 MB

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        rows = [0] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    result += 1
        return result
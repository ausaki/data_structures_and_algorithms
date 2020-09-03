# title: minimum-cost-to-make-at-least-one-valid-path-in-a-grid
# detail: https://leetcode.com/submissions/detail/386553308/
# datetime: Wed Aug 26 15:30:07 2020
# runtime: 384 ms
# memory: 14.4 MB

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        t = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = collections.deque()

        def append(i, j, cost):
            while 0 <= i < m and 0 <= j < n and grid[i][j] > 0:
                q.append(i * n + j)
                di, dj = t[grid[i][j] - 1]
                grid[i][j] = -cost
                if i == m - 1 and j == n - 1:
                    break
                i += di
                j += dj
                
        append(0, 0, 0)
        while q:
            i = q.popleft()
            i, j = divmod(i, n)
            if grid[m - 1][n - 1] <= 0:
                return -grid[m - 1][n - 1]
            for di, dj in t:
                append(i + di, j + dj, -grid[i][j] + 1)
                if grid[m - 1][n - 1] <= 0:
                    return -grid[m - 1][n - 1]            
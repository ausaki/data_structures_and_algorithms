# title: minimum-cost-to-make-at-least-one-valid-path-in-a-grid
# detail: https://leetcode.com/submissions/detail/386546604/
# datetime: Wed Aug 26 15:12:36 2020
# runtime: 372 ms
# memory: 15.3 MB

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        t = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        q = collections.deque()

        def append(i, j, cost):
            while 0 <= i < m and 0 <= j < n:
                ii = i * n + j
                if ii in visited:
                    break
                q.append((ii, cost))
                visited.add(ii)
                di, dj = t[grid[i][j] - 1]
                i += di
                j += dj
        append(0, 0, 0)
        while q:
            i, c = q.popleft()
            i, j = divmod(i, n)
            if i == m - 1 and j == n - 1:
                return c
            for di, dj in t:
                append(i + di, j + dj, c + 1)

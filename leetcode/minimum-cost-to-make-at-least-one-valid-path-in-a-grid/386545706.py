# title: minimum-cost-to-make-at-least-one-valid-path-in-a-grid
# detail: https://leetcode.com/submissions/detail/386545706/
# datetime: Wed Aug 26 15:10:22 2020
# runtime: 344 ms
# memory: 15.2 MB

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        t = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        q = collections.deque()
        i = j = 0
        
        def append(i, j, cost):
            while True:
                if 0 <= i < m and 0 <= j < n:
                    ii = i * n + j
                    if ii in visited:
                        break
                    q.append((ii, cost))
                    visited.add(ii)
                    di, dj = t[grid[i][j] - 1]
                    i += di
                    j += dj
                else:
                    break
        append(0, 0, 0)
        # print(q)
        while q:
            i, c = q.popleft()
            # visited.add(i)
            i, j = divmod(i, n)
            # print(i, j, c)
            if i == m - 1 and j == n - 1:
                return c
            k = grid[i][j] - 1
            for di, dj in t:
                ii = i + di
                jj = j + dj
                if 0 <= ii < m and 0 <= jj < n:
                    if ii * n + jj in visited:
                        continue
                    append(ii, jj, c + 1)
        return -1
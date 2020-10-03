# title: rotting-oranges
# detail: https://leetcode.com/submissions/detail/401713916/
# datetime: Mon Sep 28 14:46:39 2020
# runtime: 44 ms
# memory: 14.1 MB

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        k = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j])
                if grid[i][j] == 1:
                    k += 1
        minutes = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 1:
                        q.append([ii, jj])
                        k -= 1
                        grid[ii][jj] = 2
            if q: minutes += 1
        return minutes if k == 0 else -1
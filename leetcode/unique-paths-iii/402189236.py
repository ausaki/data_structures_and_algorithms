# title: unique-paths-iii
# detail: https://leetcode.com/submissions/detail/402189236/
# datetime: Tue Sep 29 16:51:23 2020
# runtime: 52 ms
# memory: 14 MB

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def walk(i, j, k):
            if grid[i][j] == 2:
                return 1 if k - 1 == z else 0
            old = grid[i][j]
            grid[i][j] = -1
            result = 0
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                ii, jj = i + di, j + dj
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] >= 0:
                    w = walk(ii, jj, k + 1)
                    result += w
            grid[i][j] = old
            return result
        
        m, n = len(grid), len(grid[0])
        x, y = -1, -1
        z = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j
                if grid[i][j] == 0:
                    z += 1
        return walk(x, y, 0)
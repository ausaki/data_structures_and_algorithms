# title: path-with-maximum-gold
# detail: https://leetcode.com/submissions/detail/395438742/
# datetime: Mon Sep 14 13:13:06 2020
# runtime: 1192 ms
# memory: 13.7 MB

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            gold = grid[i][j]
            grid[i][j] = 0
            g = 0
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                ii = i + di
                jj = j + dj
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] != 0:
                    g = max(g, dfs(ii, jj))
            grid[i][j] = gold
            return gold + g
    
        return max(dfs(i, j) for i in range(m) for j in range(n) if grid[i][j] != 0)
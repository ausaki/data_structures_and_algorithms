# title: detect-cycles-in-2d-grid
# detail: https://leetcode.com/submissions/detail/389885658/
# datetime: Wed Sep  2 17:28:14 2020
# runtime: 3368 ms
# memory: 222.7 MB

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for i in range(m)]
        
        def dfs(i, j, pi, pj):
            if visited[i][j]:
                return True
            visited[i][j] = 1
            a = grid[i][j]
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                ii = i + di
                jj =j + dj
                if not (0 <= ii < m and 0 <= jj < n) or grid[ii][jj] != a or (ii == pi and jj == pj):
                    continue
                if dfs(ii, jj, i, j):
                    return True
            return False
                
                
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                if dfs(i, j, -1, -1):
                    return True
        return False
                
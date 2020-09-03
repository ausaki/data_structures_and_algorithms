# title: detect-cycles-in-2d-grid
# detail: https://leetcode.com/submissions/detail/389882983/
# datetime: Wed Sep  2 17:18:11 2020
# runtime: 3188 ms
# memory: 228.8 MB

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for i in range(m)]
        
        def dfs(i, j, k):
            if visited[i][j]:
                return k - visited[i][j] >= 4
            visited[i][j] = k
            a = grid[i][j]
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                ii = i + di
                jj =j + dj
                if not (0 <= ii < m and 0 <= jj < n) or grid[ii][jj] != a:
                    continue
                if dfs(ii, jj, k + 1):
                    return True
            return False
                
                
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                if dfs(i, j, 1):
                    return True
        return False
                
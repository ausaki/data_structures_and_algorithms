# title: detect-cycles-in-2d-grid
# detail: https://leetcode.com/submissions/detail/389886307/
# datetime: Wed Sep  2 17:30:32 2020
# runtime: 3524 ms
# memory: 237.3 MB

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        
        def dfs(i, j, pi, pj):
            k = i * n + j
            if k in visited:
                return True
            visited.add(k)
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
                if (i * n + j) in visited:
                    continue
                if dfs(i, j, -1, -1):
                    return True
        return False
                
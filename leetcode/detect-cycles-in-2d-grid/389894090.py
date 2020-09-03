# title: detect-cycles-in-2d-grid
# detail: https://leetcode.com/submissions/detail/389894090/
# datetime: Wed Sep  2 17:58:25 2020
# runtime: 2664 ms
# memory: 221.1 MB

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        visited = [[False] * n for _ in range(m)]
        
        def check(i, j, lasti, lastj):
            if visited[i][j]:
                return True
            visited[i][j] = True
            for delta in [[-1,0],[1,0],[0,1],[0,-1]]:
                ni = i + delta[0]
                nj = j + delta[1]
                if ni == lasti and nj == lastj:
                    continue
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                if grid[ni][nj] != grid[i][j]:
                    continue
                if check(ni,nj,i,j):
                    return True
            return False
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                if check(i,j,-1,-1):
                    return True
        return False
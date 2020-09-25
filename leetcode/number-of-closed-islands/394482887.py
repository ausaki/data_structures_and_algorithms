# title: number-of-closed-islands
# detail: https://leetcode.com/submissions/detail/394482887/
# datetime: Sat Sep 12 13:43:01 2020
# runtime: 144 ms
# memory: 14.2 MB

class DisjSet:
    def __init__(self, n):
        self.disj_set = [-1] * n
    
    def set_edge(self, x):
        self.disj_set[x] = -2
        
    def find(self, x):
        while self.disj_set[x] >= 0:
            x = self.disj_set[x]
        return x
    
    def union(self, x, y):
        i = self.find(x)
        j = self.find(y)
        if i == j:
            return
        if self.disj_set[j] == -2:
            self.disj_set[i] = -2
        self.disj_set[j] = i
    
    def count_set(self):
        return self.disj_set.count(-1)

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j, val):
            if 0<=i<m and 0<=j<n and grid[i][j]==0:
                grid[i][j] = val
                dfs(i, j+1, val)
                dfs(i+1, j, val)
                dfs(i-1, j, val)
                dfs(i, j-1, val)
        
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and grid[i][j] == 0:
                    dfs(i, j, 1)
                
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, 1)
                    res += 1
                    
        return res
                
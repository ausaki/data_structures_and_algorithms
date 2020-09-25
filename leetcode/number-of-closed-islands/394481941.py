# title: number-of-closed-islands
# detail: https://leetcode.com/submissions/detail/394481941/
# datetime: Sat Sep 12 13:39:54 2020
# runtime: 128 ms
# memory: 14.3 MB

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
        m, n = len(grid), len(grid[0])
        disj = DisjSet(m * n)
        for i in range(m):
            for j in range(n):
                k = i * n + j
                if grid[i][j] == 1:
                    disj.disj_set[k] = 1
                    continue
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    disj.set_edge(k)
                if j - 1 >= 0 and grid[i][j - 1] == 0:
                    disj.union(k, k - 1)
                if i - 1 >= 0 and grid[i - 1][j] == 0:
                    disj.union(k, k - n)
        return disj.count_set()
                
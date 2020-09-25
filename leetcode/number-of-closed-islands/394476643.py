# title: number-of-closed-islands
# detail: https://leetcode.com/submissions/detail/394476643/
# datetime: Sat Sep 12 13:22:59 2020
# runtime: 132 ms
# memory: 13.8 MB

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
        count = 0
        for i in self.disj_set:
            if i == -1:
                count += 1
        return count

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
                    disj.union(k - 1, k)
                if i - 1 >= 0 and grid[i - 1][j] == 0:
                    disj.union(k - n, k)
        return disj.count_set()
                
# title: minimum-number-of-days-to-disconnect-island
# detail: https://leetcode.com/submissions/detail/389996546/
# datetime: Wed Sep  2 23:33:50 2020
# runtime: 2308 ms
# memory: 13.9 MB

class DisjSet:
    def __init__(self, n):
        self.disj_set = [-1] * n
        
    def find(self, x):
        while self.disj_set[x] >= 0:
            x = self.disj_set[x]
        return x
    
    def union(self, x, y):
        i = self.find(x)
        if i == -1:
            return
        j = self.find(y)
        if j == -1:
            return
        if i == j:
            return
        if self.disj_set[i] < self.disj_set[j]:
            self.disj_set[j] = i
        else:
            if self.disj_set[i] == self.disj_set[j]:
                self.disj_set[j] -= 1
            self.disj_set[i] = j
    
    def count_set(self):
        count = 0
        for i in self.disj_set:
            if i < 0:
                count += 1
        return count

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def conn():
            disj = DisjSet(m * n)
            for i in range(m):
                for j in range(n):
                    k = i * n + j
                    if grid[i][j] == 0:
                        disj.disj_set[k] = 0
                        continue
                    if j > 0 and grid[i][j - 1] == 1:
                        disj.union(k, k - 1)
                    if i > 0 and grid[i - 1][j] == 1:
                        disj.union(k, k - n)
            return disj.count_set()
        
        if conn() != 1:
            return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                grid[i][j] = 0
                if conn() != 1:
                    return 1
                grid[i][j] = 1
        return 2
        
                
                
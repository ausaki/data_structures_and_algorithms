# title: regions-cut-by-slashes
# detail: https://leetcode.com/submissions/detail/402966117/
# datetime: Thu Oct  1 12:39:25 2020
# runtime: 92 ms
# memory: 14.2 MB

class DisjSet:
    def __init__(self, n ):
        self.disj_set = [-1] * n
        
    def find(self, x):
        while self.disj_set[x] >= 0:
            x = self.disj_set[x]
        return x
    
    def union(self, x, y):
        i = self.find(x)
        j = self.find(y)
        if i == j:
            return
        if self.disj_set[i] < self.disj_set[j]:
            self.disj_set[j] = i
        else:
            if self.disj_set[i] == self.disj_set[j]:
                self.disj_set[j] -= 1
            self.disj_set[i] = j
    def count_set(self):
        return sum(1 for i in self.disj_set if i < 0)
    
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        disj = DisjSet(m * n * 2)
        for i in range(m):
            for j in range(n):
                p = (i * n + j) * 2
                if grid[i][j] == ' ':
                    disj.union(p, p + 1)
                if j:
                    if grid[i][j - 1] == ' ':
                        disj.union(p, p - 2)
                    else:
                        disj.union(p, p - 2 + 1)
                if i:
                    if grid[i - 1][j] == '/':
                        disj.union(p + 1 if grid[i][j] == '\\' else p, p - 2 * n + 1)
                    else:
                        disj.union(p + 1 if grid[i][j] == '\\' else p, p - 2 * n)
        return disj.count_set()
                            
                        
                            

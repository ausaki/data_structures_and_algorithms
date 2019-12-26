# title: max-area-of-island
# detail: https://leetcode.com/submissions/detail/288467047/
# datetime: Wed Dec 25 22:52:05 2019
# runtime: 156 ms
# memory: 12.9 MB

class DisjSet:
    def __init__(self):
        self.elements = {}
        self.disj_set = []
        
    def add(self, x):
        if x not in self.elements:
            self.elements[x] = len(self.disj_set)
            self.disj_set.append(-1)
        
    def find(self, x):
        if x not in self.elements:
            return -1
        i = self.elements[x]
        while self.disj_set[i] >= 0:
            i = self.disj_set[i]
        return i
    
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
            self.disj_set[i] += self.disj_set[j]
            self.disj_set[j] = i
        else:
            self.disj_set[j] += self.disj_set[i]
            self.disj_set[i] = j
            
    def max_set(self):
        return min(self.disj_set) if self.disj_set else 0
    
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if N == 0:
            return 0
        M = len(grid[0])
        disj = DisjSet()
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    continue
                disj.add(i * M + j)
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    disj.union((i - 1) * M + j, i * M + j)
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    disj.union(i * M + j - 1, i * M + j)
        return -disj.max_set()
# title: making-a-large-island
# detail: https://leetcode.com/submissions/detail/409064810/
# datetime: Thu Oct 15 22:14:42 2020
# runtime: 132 ms
# memory: 14.3 MB

class DisjSet:
    def __init__(self, n ):
        self.disj_set = [-1] * n
        self.set_size = [1] * n
        
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
            self.set_size[i] += self.set_size[j]
            self.set_size[j] = 0
        else:
            if self.disj_set[i] == self.disj_set[j]:
                self.disj_set[j] -= 1
            self.disj_set[i] = j
            self.set_size[j] += self.set_size[i]
            self.set_size[i] = 0
    
    def max_size(self):
        return max(self.set_size)
    
    def get_size(self, i):
        return self.set_size[i]
    
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        disj = DisjSet(m * n)
        for i in range(m):
            for j in range(n):
                p = i * n + j
                if grid[i][j] == 0:
                    continue
                if i and grid[i - 1][j] == 1:
                    disj.union(p, p - n)
                if j and grid[i][j - 1] == 1:
                    disj.union(p, p - 1)
        sz = disj.max_size()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                s = set()
                for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 1:
                        s.add(disj.find(ii * n + jj))
                sz = max(sz, sum(disj.get_size(s0) for s0 in s) + 1)
        return sz
                                        
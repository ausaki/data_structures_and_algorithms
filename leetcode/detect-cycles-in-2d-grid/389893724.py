# title: detect-cycles-in-2d-grid
# detail: https://leetcode.com/submissions/detail/389893724/
# datetime: Wed Sep  2 17:57:04 2020
# runtime: 2804 ms
# memory: 22.5 MB

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
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        disj = DisjSet(m * n)
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                k = i * n + j
                d1 = d2 = -1
                if i > 0 and c == grid[i - 1][j]:
                    d1 = disj.find(k - n)
                    disj.union(k, k - n)
                if j > 0 and c == grid[i][j - 1]:
                    d2 = disj.find(k - 1)
                    disj.union(k, k - 1)
                if d1 == d2 and d1 != -1:
                    return True
        return False
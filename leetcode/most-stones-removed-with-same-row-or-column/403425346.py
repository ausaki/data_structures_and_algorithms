# title: most-stones-removed-with-same-row-or-column
# detail: https://leetcode.com/submissions/detail/403425346/
# datetime: Fri Oct  2 14:50:26 2020
# runtime: 128 ms
# memory: 14.7 MB

class DisjSet:
    def __init__(self, n ):
        self.disj_set = [-1] * n
        self.sizes = [1] * n
        
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
            self.sizes[i] += self.sizes[j]
            self.sizes[j] = 0
        else:
            if self.disj_set[i] == self.disj_set[j]:
                self.disj_set[j] -= 1
            self.disj_set[i] = j
            self.sizes[j] += self.sizes[i]
            self.sizes[i] = 0
    
    def count(self):
        return sum(sz - 1 for sz in self.sizes if sz > 1)
    
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        disj = DisjSet(n)
        row = {}
        col = {}
        for i, (x, y) in enumerate(stones):
            if x not in row:
                row[x] = i
            else:
                disj.union(i, row[x])
            if y not in col:
                col[y] = i
            else:
                disj.union(i, col[y])
        return disj.count()
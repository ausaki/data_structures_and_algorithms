# title: most-stones-removed-with-same-row-or-column
# detail: https://leetcode.com/submissions/detail/403428978/
# datetime: Fri Oct  2 15:00:42 2020
# runtime: 152 ms
# memory: 14.6 MB

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
    
    def count(self):
        return sum(1 for i in self.disj_set if i < 0)
    
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        disj = DisjSet(n)
        row = {}
        col = {}
        for i, (x, y) in enumerate(stones):
            disj.union(i, row.setdefault(x, i))
            disj.union(i, col.setdefault(y, i))
        return n - disj.count()
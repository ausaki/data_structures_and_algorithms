# title: most-stones-removed-with-same-row-or-column
# detail: https://leetcode.com/submissions/detail/403428519/
# datetime: Fri Oct  2 14:59:17 2020
# runtime: 148 ms
# memory: 14.4 MB

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
            if x not in row:
                row[x] = i
            else:
                disj.union(i, row[x])
            if y not in col:
                col[y] = i
            else:
                disj.union(i, col[y])
        return n - disj.count()
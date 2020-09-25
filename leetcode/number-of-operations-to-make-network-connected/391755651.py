# title: number-of-operations-to-make-network-connected
# detail: https://leetcode.com/submissions/detail/391755651/
# datetime: Sun Sep  6 16:24:17 2020
# runtime: 556 ms
# memory: 33.8 MB

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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        cables = 0
        disj = DisjSet(n)
        for a, b in connections:
            if disj.find(a) == disj.find(b):
                cables += 1
            else:
                disj.union(a, b)
        m = disj.count_set()
        return m - 1 if cables >= m - 1 else -1
            
            
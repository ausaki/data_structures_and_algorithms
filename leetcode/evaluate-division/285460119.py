# title: evaluate-division
# detail: https://leetcode.com/submissions/detail/285460119/
# datetime: Thu Dec 12 18:01:12 2019
# runtime: 40 ms
# memory: 12.8 MB

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
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def query(a, b, val, seen):
            if a == b:
                return val
            for c, v in mapping[a].items():
                if c in seen:
                    continue
                seen.add(c)
                res = query(c, b, val * v, seen)
                if res != -1:
                    return res
            return -1
                
        mapping = {}
        for (a, b), val in zip(equations, values):
            if a not in mapping:
                mapping[a] = {}
            mapping[a][b] = val
            if b not in mapping:
                mapping[b] = {}
            mapping[b][a] = 1 / val
            
        res = []
        for a, b in queries:
            if a not in mapping or b not in mapping:
                val = -1.0
            else:
                val = query(a, b, 1, set())
            res.append(val)
        return res
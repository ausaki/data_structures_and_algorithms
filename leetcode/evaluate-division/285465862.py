# title: evaluate-division
# detail: https://leetcode.com/submissions/detail/285465862/
# datetime: Thu Dec 12 19:03:28 2019
# runtime: 24 ms
# memory: 12.9 MB

class DisjSet:
    def __init__(self):
        self.elements = {}
        
    def add(self, x):
        if x in self.elements:
            return self.elements[x]
        self.elements[x] = [x, 1]
        
    def find(self, x):
        if x not in self.elements:
            return 
        return self.elements[x][0]
    
    def getvalue(self, x):
        return self.elements[x][1]
    
    def union(self, x, y, val):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 is None or s2 is None:
            return
        v1 = self.getvalue(x)
        v2 = self.getvalue(y)
        val = val * v1 / v2
        for elem, value in self.elements.items():
            if value[0] == s2:
                value[0] = s1
                value[1] *= val
        
        
    
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        disjset = DisjSet()
        for (a, b), val in zip(equations, values):
            disjset.add(b)
            disjset.add(a)
            disjset.union(b, a, val)
        print(disjset.elements)
        res = []
        for a, b in queries:
            val = -1
            s1 = disjset.find(a)
            s2 = disjset.find(b)
            if s1 is not None and s1 == s2:
                val = disjset.getvalue(a) / disjset.getvalue(b)
            res.append(val)
        return res
        
    def calcEquation2(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
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
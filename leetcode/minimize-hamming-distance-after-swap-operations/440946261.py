# title: minimize-hamming-distance-after-swap-operations
# detail: https://leetcode.com/submissions/detail/440946261/
# datetime: Sun Jan 10 11:00:51 2021
# runtime: 1492 ms
# memory: 60.2 MB

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
            return i
        if self.disj_set[i] < self.disj_set[j]:
            self.disj_set[j] = i
            return i
        if self.disj_set[i] == self.disj_set[j]:
            self.disj_set[j] -= 1
        self.disj_set[i] = j
        return j 
    
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        dj = DisjSet(n)
        for i, j in allowedSwaps:
            dj.union(i, j)
        g = collections.defaultdict(collections.Counter)
        for i in range(n):
            j = dj.find(i) 
            g[j][source[i]] +=1
        res = 0
        for i in range(n):
            j = dj.find(i)
            v = target[i]
            k = g[j].get(v, 0)
            if k > 0:
                if k > 1:
                    g[j][v] = k - 1
                else:
                    g[j].pop(v)
            else:
                res += 1
        return res            
        
        
        
        
        
        
        
        
        
# title: graph-connectivity-with-threshold
# detail: https://leetcode.com/submissions/detail/410181261/
# datetime: Sun Oct 18 16:44:54 2020
# runtime: 1080 ms
# memory: 49.2 MB

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
            
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        m = len(queries)
        if threshold == 0:
            return [True] * m
        disj = DisjSet(n + 1)
        for i in range(1, n + 1):
            for j in range(2, int(math.sqrt(i)) + 1):
                q, r = divmod(i, j)
                if r == 0:
                    if j > threshold:
                        disj.union(i, j)
                    if q > threshold:
                        disj.union(i, q)
        return [disj.find(a) == disj.find(b) for a, b in queries]
        
        
# title: graph-connectivity-with-threshold
# detail: https://leetcode.com/submissions/detail/410179249/
# datetime: Sun Oct 18 16:36:15 2020
# runtime: 944 ms
# memory: 49.3 MB

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
                if i % j == 0:
                    if j > threshold:
                        disj.union(i, j)
                    j = i // j
                    if j > threshold:
                        disj.union(i, j)
        return [disj.find(a) == disj.find(b) for a, b in queries]
        
        
# title: rank-transform-of-a-matrix
# detail: https://leetcode.com/submissions/detail/412920233/
# datetime: Sun Oct 25 16:54:03 2020
# runtime: 1164 ms
# memory: 44.9 MB

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
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        g = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                g[matrix[i][j]].append((i, j))
        rank = [0] * (m + n)
        result = [[0] * n for i in range(m)]
        unique_values = sorted(g)
        for val in unique_values:
            disj = DisjSet(m + n)
            rank2 = rank[:]
            for i, j in g[val]:
                s1 = disj.find(i)
                s2 = disj.find(j + m)
                s = disj.union(i, j + m)
                rank2[s] = max(rank2[s1], rank2[s2])
            for i, j in g[val]:
                rank[i] = rank[j + m] = result[i][j] = rank2[disj.find(i)] + 1
        return result
# title: find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree
# detail: https://leetcode.com/submissions/detail/380377775/
# datetime: Thu Aug 13 23:21:11 2020
# runtime: 1932 ms
# memory: 13.8 MB

class DisjSet:
    def __init__(self, size):
        self.disj_set = [-1] * size
        
    # def add(self, x):
    #     if x not in self.elements:
    #         self.elements[x] = len(self.disj_set)
    #         self.disj_set.append(-1)
        
    def find(self, i):
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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def find_mst(deleted=-1, keep=-1):
            disj_set = DisjSet(n)
            w = 0
            if keep != -1:
                edge = edges[keep][1]
                disj_set.union(edge[0], edge[1])
                w += edge[2]
            for i, edge_ in enumerate(edges):
                if i == deleted:
                    continue
                edge = edge_[1]
                s1 = disj_set.find(edge[0])
                s2 = disj_set.find(edge[1])
                if s1 == s2 and s1 != -1:
                    continue
                disj_set.union(edge[0], edge[1])
                w += edge[2]
            if disj_set.count_set() == 1 and len(disj_set.disj_set) == n:
                return w
            return float('inf')
        
        
        edges = sorted(zip(range(len(edges)), edges), key=lambda a: a[1][2])
        critical = []
        pseudo = []
        mst = find_mst()
        print(mst)
        for i, edge_ in enumerate(edges):
            j, edge = edge_
            if find_mst(i) > mst:
                critical.append(j)
            elif find_mst(-1, i) == mst:
                pseudo.append(j)
        return [critical, pseudo]
        
            
        
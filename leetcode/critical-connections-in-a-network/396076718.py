# title: critical-connections-in-a-network
# detail: https://leetcode.com/submissions/detail/396076718/
# datetime: Tue Sep 15 20:35:03 2020
# runtime: 2628 ms
# memory: 84.2 MB

class Tarjan:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.idx = 1
        self.dfn = [0] * n
        self.low = [0] * n
        self.g = collections.defaultdict(list)
        for v, w in self.edges:
            self.g[v].append(w)
            self.g[w].append(v)
            
    def run(self):
        for i in range(self.n):
            if self.dfn[i] == 0:
                self.dfs(i, -1)
        result = []
        for v, w in self.edges:
            if self.low[w] > self.dfn[v] or self.low[v] > self.dfn[w]:
                result.append([v, w])
        return result
    
    def dfs(self, v, parent):
        self.dfn[v] = self.low[v] = self.idx
        self.idx += 1
        for w in self.g[v]:
            if w == parent:
                continue
            if self.dfn[w] == 0:
                self.dfs(w, v)
                self.low[v] = min(self.low[v], self.low[w])
            else:
                self.low[v] = min(self.low[v], self.dfn[w])
                
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        t = Tarjan(n, connections)
        return t.run()
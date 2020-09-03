# title: kth-ancestor-of-a-tree-node
# detail: https://leetcode.com/submissions/detail/380792702/
# datetime: Fri Aug 14 21:43:00 2020
# runtime: 1132 ms
# memory: 53.9 MB

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.pars = [parent]
        self.n = n
        for k in range(17):
            row = []
            for i in range(n):
                p = self.pars[-1][i]
                if p != -1:
                    p = self.pars[-1][p]
                row.append(p)
            self.pars.append(row)
        
        
    def build_cache(self):
        self.step = 300
        self.children = {}
        leaf_nodes = set(range(self.n))
        for i, p in enumerate(self.parent):
            if p not in self.children:
                self.children[p] = [i, -1]
            else:
                self.children[p][1] = i
            if p != -1:
                leaf_nodes.discard(p)
        self.cache = {}
        for node in leaf_nodes:
            self._build_cache(node)
            
    def _build_cache(self, node):
        if node in self.cache:
            return
        p = self.parent[node]
        children = self.children[p]
        c = children[0]
        if c == node:
            c = children[1]
        if c in self.cache:
            self.cache[node] = self.cache[c]
            return
        i = 0
        cache = []
        self.cache[node] = cache
        if c != -1:
            self.cache[c] = cache
        while i < self.step and node != -1:
            # if i > 0 and node in self.cache:
            #     break
            cache.append(node)
            i += 1
            node = self.parent[node]
        if node != -1:
            self._build_cache(node)
        
    def getKthAncestor(self, node: int, k: int) -> int:
        i = 0
        while k:
            if node == -1: break
            if (k&1):
                node = self.pars[i][node]
            i += 1
            k >>= 1
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
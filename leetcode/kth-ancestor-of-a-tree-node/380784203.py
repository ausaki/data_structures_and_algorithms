# title: kth-ancestor-of-a-tree-node
# detail: https://leetcode.com/submissions/detail/380784203/
# datetime: Fri Aug 14 21:15:15 2020
# runtime: 5148 ms
# memory: 60.5 MB

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.n = n
        self.parent = parent
        self.build_cache()
        
        
    def build_cache(self):
        self.step = 1000
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
        while i < self.step and node != -1:
            cache.append(node)
            i += 1
            node = self.parent[node]
        if node != -1:
            self._build_cache(node)
        
    def getKthAncestor(self, node: int, k: int) -> int:
        while node not in self.cache and k and node != -1:
            node = self.parent[node]
            k -= 1
        if k == 0 or node == -1:
            return node
        while k >= len(self.cache[node]):
            k -= len(self.cache[node])
            node = self.cache[node][-1]
            node = self.parent[node]
            if node == -1:
                break
        return self.cache[node][k] if node != -1 else -1


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
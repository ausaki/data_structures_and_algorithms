# title: kth-ancestor-of-a-tree-node
# detail: https://leetcode.com/submissions/detail/380803242/
# datetime: Fri Aug 14 22:17:05 2020
# runtime: 988 ms
# memory: 52.9 MB

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.parents = [parent]
        for i in range(1, 17):
            p1 = self.parents[-1]
            p2 = []
            for j in range(n):
                p = p1[j]
                if p != -1:
                    p = p1[p]
                p2.append(p)
            self.parents.append(p2)
        
    def getKthAncestor(self, node: int, k: int) -> int:
        i = 0
        while k:
            if k & 1:
                node = self.parents[i][node]
            if node == -1: break
            k = k >> 1
            i += 1
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
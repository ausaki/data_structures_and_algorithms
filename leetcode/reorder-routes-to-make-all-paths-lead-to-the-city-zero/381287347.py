# title: reorder-routes-to-make-all-paths-lead-to-the-city-zero
# detail: https://leetcode.com/submissions/detail/381287347/
# datetime: Sun Aug 16 00:51:49 2020
# runtime: 996 ms
# memory: 37.3 MB

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g1 = collections.defaultdict(list)
        g2 = collections.defaultdict(list)
        for v1, v2 in connections:
            g1[v1].append(v2)
            g2[v2].append(v1)
        
        def reorder(node, prev):
            result = 0
            if node in g1:
                for nd in g1.pop(node):
                    if nd == prev:
                        continue
                    result += 1 + reorder(nd, node) 
            if node in g2:
                for nd in g2.pop(node):
                    if nd == prev:
                        continue
                    result += reorder(nd, node)
            return result
        
        return reorder(0, -1)
                    
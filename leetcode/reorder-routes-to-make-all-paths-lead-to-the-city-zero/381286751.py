# title: reorder-routes-to-make-all-paths-lead-to-the-city-zero
# detail: https://leetcode.com/submissions/detail/381286751/
# datetime: Sun Aug 16 00:50:13 2020
# runtime: 920 ms
# memory: 38.8 MB

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
                for nd in g1[node]:
                    if nd == prev:
                        continue
                    result += 1 + reorder(nd, node) 
            if node in g2:
                for nd in g2[node]:
                    if nd == prev:
                        continue
                    result += reorder(nd, node)
            return result
        
        return reorder(0, -1)
                    
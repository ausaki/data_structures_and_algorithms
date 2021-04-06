# title: find-center-of-star-graph
# detail: https://leetcode.com/submissions/detail/467458358/
# datetime: Sun Mar 14 10:38:19 2021
# runtime: 916 ms
# memory: 50.2 MB

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        deg = [0] * n
        for u, v in edges:
            deg[u - 1] += 1
            deg[v - 1] += 1
            if deg[u - 1] > 1:
                return u
            if deg[v - 1] > 1:
                return v
        
        
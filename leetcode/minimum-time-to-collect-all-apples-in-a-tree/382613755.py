# title: minimum-time-to-collect-all-apples-in-a-tree
# detail: https://leetcode.com/submissions/detail/382613755/
# datetime: Tue Aug 18 16:07:45 2020
# runtime: 772 ms
# memory: 50.6 MB

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = collections.defaultdict(list)
        for v1, v2 in edges:
            g[v1].append(v2)
            g[v2].append(v1)
        
        def travel(node, parent):
            children = g[node]
            t = sum(travel(child, node) for child in children if child != parent)
            if t:
                return t + 2
            return 2 if hasApple[node] else 0
        
        t = travel(0, -1)
        return (t - 2) if t else 0
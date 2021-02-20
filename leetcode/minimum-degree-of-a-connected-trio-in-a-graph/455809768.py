# title: minimum-degree-of-a-connected-trio-in-a-graph
# detail: https://leetcode.com/submissions/detail/455809768/
# datetime: Sun Feb 14 12:58:05 2021
# runtime: 760 ms
# memory: 47.8 MB

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        if len(g) == 1:
            return 0
        A = sorted((len(g[a]), a)for a in g)
        B = sorted((len(g[a]) + len(g[b]), a, b) for a, b in edges)
        res = math.inf
        for d, a, b in B:
            if d >= res:
                continue
            for d2, c in A:
                if c in g[a] and c in g[b]:
                    res = min(res, d + d2)
                    break
        return -1 if math.isinf(res) else res - 6
                    
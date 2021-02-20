# title: minimum-degree-of-a-connected-trio-in-a-graph
# detail: https://leetcode.com/submissions/detail/455797332/
# datetime: Sun Feb 14 12:22:10 2021
# runtime: 11148 ms
# memory: 39.4 MB

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        if len(g) == 1:
            return 0
        res = math.inf
        for a, b, c in itertools.combinations(range(1, n + 1), 3):
            if b in g[a] and c in g[a] and c in g[b]:
                res = min(res, len(g[b]) + len(g[c]) + len(g[a]) - 6)
        return -1 if math.isinf(res) else res
                    
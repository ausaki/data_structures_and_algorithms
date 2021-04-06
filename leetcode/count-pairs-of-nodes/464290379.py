# title: count-pairs-of-nodes
# detail: https://leetcode.com/submissions/detail/464290379/
# datetime: Sun Mar  7 00:17:03 2021
# runtime: 6624 ms
# memory: 62.6 MB

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        g = collections.defaultdict(collections.Counter)
        deg = collections.Counter()
        for u, v in edges:
            g[u][v] += 1
            g[v][u] += 1
            deg[u] += 1
            deg[v] += 1
        D = sorted([(d, u) for u, d in deg.items()])
        zero = n - len(D)
        res = [0] * len(queries)
        for i, (d, u) in enumerate(D):
            for k, q in enumerate(queries):
                item = (q - d, 10 ** 9)
                j = bisect.bisect(D, item, i + 1)
                res[k] += len(D) - j
                # print(k, res[k])
                for v, dd in g[u].items():
                    if d + deg[v] > q and d + deg[v] - dd <= q:
                        res[k] -= 1
                if d > q:
                    res[k] += zero
            for v, dd in g[u].items():
                g[v].pop(u)
        return res
            
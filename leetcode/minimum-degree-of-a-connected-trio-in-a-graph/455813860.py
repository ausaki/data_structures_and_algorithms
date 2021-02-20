# title: minimum-degree-of-a-connected-trio-in-a-graph
# detail: https://leetcode.com/submissions/detail/455813860/
# datetime: Sun Feb 14 13:10:56 2021
# runtime: 796 ms
# memory: 48.6 MB

'''
我想到的是O(n^3) 的解法, 具体来说是 O(n * C(v, 2)).

下面的算法是在提交详情页面发现的一个更加高效的算法.
'''

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        if len(g) == 1:
            return 0
        A = sorted([a for a in g], key=lambda k: len(g[k]))
        B = sorted([(a, b) for a, b in edges], key=lambda k: len(g[k[0]]) + len(g[k[1]]))
        res = math.inf
        for a, b in B:
            d = len(g[a]) + len(g[b])
            if d >= res:
                continue
            for c in A:
                d2 = len(g[c])
                if c in g[a] and c in g[b]:
                    res = min(res, d + d2)
                    break
        return -1 if math.isinf(res) else res - 6
                    
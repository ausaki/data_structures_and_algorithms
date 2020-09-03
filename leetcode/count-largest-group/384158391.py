# title: count-largest-group
# detail: https://leetcode.com/submissions/detail/384158391/
# datetime: Fri Aug 21 19:06:54 2020
# runtime: 96 ms
# memory: 13.7 MB

class Solution:
    def countLargestGroup(self, n: int) -> int:
        g = {}
        for i in range(1, n + 1):
            s = 0
            while i:
                i, j = divmod(i, 10)
                s += j
            if s not in g:
                g[s] = 0
            g[s] += 1
        v = list(g.values())
        return v.count(max(v))
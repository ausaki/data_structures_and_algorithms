# title: flip-columns-for-maximum-number-of-equal-rows
# detail: https://leetcode.com/submissions/detail/399522817/
# datetime: Wed Sep 23 12:57:50 2020
# runtime: 1604 ms
# memory: 15.8 MB

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        g = {}
        for i in range(m):
            a = tuple(matrix[i])
            if a in g:
                g[a] += 1
            else:
                b = tuple(map(lambda i: (i + 1) % 2, matrix[i]))
                if b in g:
                    g[b] += 1
                else:
                    g[a] = g.get(a, 0) + 1
        return max(g.values())        
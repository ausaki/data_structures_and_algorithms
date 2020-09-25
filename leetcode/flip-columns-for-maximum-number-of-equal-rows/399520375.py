# title: flip-columns-for-maximum-number-of-equal-rows
# detail: https://leetcode.com/submissions/detail/399520375/
# datetime: Wed Sep 23 12:52:13 2020
# runtime: 1776 ms
# memory: 15.6 MB

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        g = {}
        for i in range(m):
            a = ''.join(map(str, matrix[i]))
            if a in g:
                g[a] += 1
            else:
                b = ''.join(map(lambda i: str((i + 1) % 2), matrix[i]))
                if b in g:
                    g[b] += 1
                else:
                    g[a] = g.get(a, 0) + 1
        return max(g.values())        
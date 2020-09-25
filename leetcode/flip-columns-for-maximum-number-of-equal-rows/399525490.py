# title: flip-columns-for-maximum-number-of-equal-rows
# detail: https://leetcode.com/submissions/detail/399525490/
# datetime: Wed Sep 23 13:03:50 2020
# runtime: 1932 ms
# memory: 15.6 MB

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def encode(row):
            i, l = row[0], 0
            result = ''
            result2 = ''
            for j in row:
                if j == i:
                    l += 1
                else:
                    result += f'{i}{l}'
                    result2 += f'{(i + 1) % 2}{l}'
                    i = j
                    l = 1
            result += f'{i}{l}'
            result2 += f'{(i + 1) % 2}{l}'
            return result, result2
        
        m, n = len(matrix), len(matrix[0])
        g = {}
        for i in range(m):
            a, b = encode(matrix[i])
            if a in g:
                g[a] += 1
            else:
                if b in g:
                    g[b] += 1
                else:
                    g[a] = g.get(a, 0) + 1
        return max(g.values())        